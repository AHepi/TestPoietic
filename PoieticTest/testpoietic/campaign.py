"""Deterministic campaign assembly and replay helpers."""

from __future__ import annotations

import csv
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from .claims import extract_claims, grade_audit, section_metrics, verify_subject_tree
from .constants import PRIMARY_SUBJECT, REPOSITORY_ROOT
from .f3_identifiability import run_bitpatch_family
from .formal_models import all_formal_models
from .protocols import audit_protocol_file
from .purpose_guard import audit_primary_purpose_guard


RUN_ID = "campaign-001"
RUN_FILES = (
    "authentication.json",
    "source_audit.json",
    "protocol_audit.json",
    "purpose_guard.json",
    "formal_models.json",
    "f3_bitpatch.json",
    "finite_exhaustion.json",
    "acquisition.json",
    "unit_tests.json",
    "f1_replay.json",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _git_tag_commit(tag: str = "stress-plan-v1") -> str | None:
    """Resolve the semantic freeze from a local tag or its tracked remote ref."""

    for reference in (tag, f"origin/freeze/{tag}"):
        process = subprocess.run(
            ["git", "rev-parse", f"{reference}^{{commit}}"],
            cwd=REPOSITORY_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if process.returncode == 0:
            return process.stdout.strip()
    return None


def run_unit_tests() -> dict[str, object]:
    suite = unittest.defaultTestLoader.discover(str(REPOSITORY_ROOT / "tests"))
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)
    return {
        "tests_run": result.testsRun,
        "failures": [test.id() for test, _ in result.failures],
        "errors": [test.id() for test, _ in result.errors],
        "skipped": [test.id() for test, _ in result.skipped],
        "expected_failures": [test.id() for test, _ in result.expectedFailures],
        "unexpected_successes": [test.id() for test in result.unexpectedSuccesses],
        "successful": result.wasSuccessful(),
    }


def verify_f1_sidecars() -> list[dict[str, object]]:
    directory = REPOSITORY_ROOT / "prior-evidence" / "f1"
    rows: list[dict[str, object]] = []
    for sidecar in sorted(directory.glob("*.sha256")):
        fields = sidecar.read_text(encoding="utf-8").strip().split(maxsplit=1)
        expected = fields[0]
        declared_name = Path(fields[1].strip()).name
        target = directory / declared_name
        actual = sha256_file(target) if target.exists() else None
        rows.append(
            {
                "sidecar": sidecar.name,
                "target": declared_name,
                "expected": expected,
                "actual": actual,
                "match": actual == expected,
            }
        )
    return rows


def replay_f1() -> dict[str, object]:
    directory = REPOSITORY_ROOT / "prior-evidence" / "f1"
    sidecars = verify_f1_sidecars()
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="testpoietic-f1-") as temp_name:
        run_directory = Path(temp_name) / "run-001"
        shutil.copytree(directory / "run-001", run_directory)
        processes: list[dict[str, object]] = []
        for verifier in (
            "verify_f1_ar_bool4_001.py",
            "verify_f1_ar_bool4_001_full_domain.py",
        ):
            process = subprocess.run(
                [sys.executable, "-B", str(directory / verifier), str(run_directory)],
                cwd=REPOSITORY_ROOT,
                env=environment,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            processes.append(
                {
                    "verifier": verifier,
                    "returncode": process.returncode,
                    "stderr": process.stderr,
                }
            )
        row_report = json.loads(
            (run_directory / "F1-AR-BOOL4-001-clean-process-verification.json").read_text(
                encoding="utf-8"
            )
        )
        domain_report = json.loads(
            (run_directory / "F1-AR-BOOL4-001-full-domain-verification.json").read_text(
                encoding="utf-8"
            )
        )
    return {
        "experiment_id": "F1-AR-BOOL4-001",
        "sidecars": sidecars,
        "all_sidecars_match": all(row["match"] for row in sidecars),
        "processes": processes,
        "row_verifier": row_report,
        "full_domain_verifier": domain_report,
        "reproduced": (
            all(row["match"] for row in sidecars)
            and all(row["returncode"] == 0 and row["stderr"] == "" for row in processes)
            and bool(row_report["passed"])
            and bool(domain_report["passed"])
        ),
        "scope": "C1 only on the frozen Boolean expression domain",
    }


def _optional_campaign_function(module_name: str, candidates: tuple[str, ...]) -> object:
    module = importlib.import_module(module_name)
    for name in candidates:
        function = getattr(module, name, None)
        if function is not None:
            return function()
    raise AttributeError(f"{module_name} exposes none of {candidates!r}")


def collect_campaign() -> dict[str, object]:
    claims = extract_claims()
    source_audit = {
        "grade_audit": grade_audit(claims),
        "section_metrics": section_metrics(),
        "subject_line_count": len(PRIMARY_SUBJECT.read_text(encoding="utf-8").splitlines()),
    }
    finite = _optional_campaign_function(
        "testpoietic.finite_exhaustion",
        ("finite_exhaustion_evidence", "all_finite_checks", "run_all", "campaign_results"),
    )
    acquisition = _optional_campaign_function(
        "testpoietic.acquisition",
        ("all_acquisition_checks", "run_all", "campaign_results"),
    )
    return {
        "authentication.json": {
            "run_id": RUN_ID,
            "frozen_tag": "stress-plan-v1",
            "frozen_commit": _git_tag_commit(),
            "subject_tree": verify_subject_tree(REPOSITORY_ROOT),
        },
        "source_audit.json": source_audit,
        "protocol_audit.json": audit_protocol_file(),
        "purpose_guard.json": audit_primary_purpose_guard(),
        "formal_models.json": all_formal_models(),
        "f3_bitpatch.json": run_bitpatch_family(),
        "finite_exhaustion.json": finite,
        "acquisition.json": acquisition,
        "unit_tests.json": run_unit_tests(),
        "f1_replay.json": replay_f1(),
    }


def write_campaign(output_directory: Path) -> dict[str, object]:
    output_directory.mkdir(parents=True, exist_ok=True)
    payload = collect_campaign()
    for name in RUN_FILES:
        (output_directory / name).write_bytes(_json_bytes(payload[name]))
    manifest_rows = [
        {
            "path": name,
            "sha256": sha256_file(output_directory / name),
            "bytes": (output_directory / name).stat().st_size,
        }
        for name in RUN_FILES
    ]
    manifest = {
        "run_id": RUN_ID,
        "files": manifest_rows,
        "all_declared_checks_green": (
            bool(payload["authentication.json"]["subject_tree"]["all_match"])
            and bool(payload["unit_tests.json"]["successful"])
            and bool(payload["f1_replay.json"]["reproduced"])
        ),
        "warning": "green reproduction does not imply that the audited theory survives",
    }
    (output_directory / "manifest.json").write_bytes(_json_bytes(manifest))
    return manifest


def compare_directories(expected: Path, actual: Path) -> dict[str, object]:
    names = (*RUN_FILES, "manifest.json")
    rows: list[dict[str, object]] = []
    for name in names:
        expected_path = expected / name
        actual_path = actual / name
        expected_hash = sha256_file(expected_path) if expected_path.exists() else None
        actual_hash = sha256_file(actual_path) if actual_path.exists() else None
        rows.append(
            {
                "path": name,
                "expected_sha256": expected_hash,
                "actual_sha256": actual_hash,
                "match": expected_hash is not None and expected_hash == actual_hash,
            }
        )
    return {"files": rows, "all_match": all(row["match"] for row in rows)}
