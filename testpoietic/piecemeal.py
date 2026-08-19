"""Deterministic integrity checks for the frozen piecemeal plan.

This module audits the plan's declared interfaces and negative controls.  It does
not accept a candidate system or issue a creativity attribution.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

RUN_ID = "piecemeal-001"
SCOPE = "FROZEN_PLAN_INTEGRITY_AND_NEGATIVE_CONTROL_REGRESSION_ONLY"
RUN_FILES = (
    "authentication.json",
    "plan_audit.json",
    "negative_controls.json",
)
SCHEMA = "TESTPOIETIC_PIECEMEAL_PLAN_V1"
FROZEN_PLAN_SHA256 = "7569d32fd0c41066f6023b411c8a06ec2d3e9e316e5213be9539d41f62dcbb9f"
CANONICAL_PLAN = Path(__file__).resolve().parents[1] / "evidence" / "frozen" / "piecemeal-plan-v1.json"

REQUIRED_LATTICES = frozenset(
    {
        "constructor_information",
        "knowledge_retention",
        "no_design_replication",
        "evolutionary_selection",
        "critical_evidence",
        "explanatory_creativity",
    }
)
REQUIRED_SOURCES = frozenset(
    {
        "CTI",
        "CT_FOUNDATION",
        "FOR_EMERGENCE",
        "FOR_REPLICATOR_NICHE",
        "FOR_GENE_STRUCTURE",
        "CTL",
        "POPPER",
        "DEUTSCH",
    }
)
REQUIRED_REQUIREMENTS = {
    "constructor_information": frozenset(
        {"I_BOUNDARY", "I_VARIABLE", "I_PERMUTATION", "I_CLONING"}
    ),
    "knowledge_retention": frozenset(
        {
            "K_PHYSICAL_INSTANTIATION",
            "K_RECIPE_CAUSAL_ROLE",
            "R_COUNTERFACTUAL_CAUSAL_ROLE",
            "K_HISTORY",
        }
    ),
    "no_design_replication": frozenset(
        {"H_NO_DESIGN", "H_RECIPE", "H_DIGITAL_RECIPE", "H_ERROR_CORRECTION"}
    ),
    "evolutionary_selection": frozenset(
        {"V_POPULATION", "V_VARIATION", "V_SELECTION", "V_FALLIBILITY"}
    ),
    "critical_evidence": frozenset(
        {
            "C_CHANNEL",
            "C_CHAIN",
            "C_AUXILIARIES",
            "C_DISCRIMINATOR",
            "C_PROTOCOL",
        }
    ),
    "explanatory_creativity": frozenset(
        {"E_P1", "E_TT", "E_EE", "E_EVIDENCE_LINK", "E_PROVENANCE", "E_FALLIBILITY"}
    ),
}
REQUIRED_EDGES = frozenset(
    {
        ("constructor_information", "knowledge_retention"),
        ("knowledge_retention", "explanatory_creativity"),
        ("critical_evidence", "explanatory_creativity"),
        ("evolutionary_selection", "explanatory_creativity"),
    }
)
REQUIRED_NON_ENTAILMENTS = frozenset(
    {
        "NE_INFORMATION_NOT_KNOWLEDGE",
        "NE_SELECTION_NOT_HIGH_FIDELITY",
        "NE_SELECTION_NOT_CRITICISM",
        "NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE",
        "NE_BARE_RECORD_NOT_EVIDENCE",
        "NE_EVIDENCE_NOT_CONFIRMATION",
        "NE_VARIATION_NOT_CONJECTURE_IDENTITY",
        "NE_NONREFUTABLE_NOT_CREATIVE",
        "NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE",
        "NE_SUBSTRATE_SWAP_NOT_AUTOMATIC",
        "NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE",
    }
)
REQUIRED_CONTROLS = frozenset(
    {
        "NC_NAKED_REPLICATOR",
        "NC_SELECTION_WITHOUT_CRITICISM",
        "NC_CREATOR_WITHOUT_SELF_REPRODUCTION",
        "NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE",
        "NC_AGREEING_RESULT_NOT_CONFIRMATION",
        "NC_UNREFUTABLE_OUTPUT",
        "NC_NONPHYSICAL_RECIPE",
    }
)
GUARD_EXPECTATIONS = {
    "NC_NAKED_REPLICATOR": {
        "evolutionary_selection": "MAY_PASS",
        "no_design_replication": "NOT_APPLICABLE",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
    "NC_SELECTION_WITHOUT_CRITICISM": {
        "evolutionary_selection": "MAY_PASS",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
    "NC_CREATOR_WITHOUT_SELF_REPRODUCTION": {
        "no_design_replication": "NOT_APPLICABLE",
        "explanatory_creativity": "UNRESOLVED_NOT_NON_CREATIVE",
    },
    "NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE": {
        "critical_evidence": "NOT_ESTABLISHED",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
    "NC_AGREEING_RESULT_NOT_CONFIRMATION": {
        "critical_evidence": "SURVIVED_DECLARED_ATTEMPT",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
    "NC_UNREFUTABLE_OUTPUT": {
        "critical_evidence": "NOT_ESTABLISHED",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
    "NC_NONPHYSICAL_RECIPE": {
        "knowledge_retention": "NOT_ESTABLISHED",
        "explanatory_creativity": "NOT_ESTABLISHED",
    },
}


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _record(checks: list[dict[str, object]], identifier: str, passed: bool, detail: str) -> None:
    checks.append({"detail": detail, "id": identifier, "passed": bool(passed)})


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _row_ids(value: object) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {
        row["id"]
        for row in value
        if isinstance(row, Mapping) and isinstance(row.get("id"), str)
    }


def _string_list(value: object) -> list[str]:
    return value if isinstance(value, list) and all(isinstance(item, str) for item in value) else []


def _read_sidecar(plan_path: Path) -> tuple[str | None, str | None]:
    sidecar = plan_path.with_suffix(".sha256")
    try:
        fields = sidecar.read_text(encoding="ascii").strip().split(maxsplit=1)
    except (OSError, UnicodeDecodeError):
        return None, "SIDECAR_UNREADABLE"
    if not fields or len(fields[0]) != 64 or any(character not in "0123456789abcdef" for character in fields[0]):
        return None, "SIDECAR_MALFORMED"
    return fields[0], None


def _load_plan(plan_path: Path) -> tuple[Mapping[str, Any], str | None, str | None]:
    try:
        raw = plan_path.read_bytes()
    except OSError:
        return {}, None, "PLAN_UNREADABLE"
    try:
        parsed = json.loads(raw)
    except UnicodeDecodeError:
        return {}, _sha256_bytes(raw), "PLAN_UTF8_INVALID"
    except json.JSONDecodeError:
        return {}, _sha256_bytes(raw), "PLAN_JSON_INVALID"
    if not isinstance(parsed, Mapping):
        return {}, _sha256_bytes(raw), "PLAN_JSON_NOT_OBJECT"
    return parsed, _sha256_bytes(raw), None


def _reference_freeze_digest() -> tuple[str | None, str | None]:
    _, actual_digest, plan_error = _load_plan(CANONICAL_PLAN)
    declared_digest, sidecar_error = _read_sidecar(CANONICAL_PLAN)
    if plan_error is not None:
        return None, "REFERENCE_PLAN_UNREADABLE"
    if sidecar_error is not None:
        return None, "REFERENCE_SIDECAR_UNREADABLE"
    if (
        actual_digest != declared_digest
        or actual_digest != FROZEN_PLAN_SHA256
        or declared_digest != FROZEN_PLAN_SHA256
    ):
        return None, "REFERENCE_FREEZE_DIGEST_MISMATCH"
    return FROZEN_PLAN_SHA256, None


def _audit(
    plan: Mapping[str, Any],
    actual_plan_sha256: str | None,
    sidecar_sha256: str | None,
    plan_error: str | None,
    sidecar_error: str | None,
    reference_freeze_sha256: str | None,
    reference_error: str | None,
    supplied_subject_sha256: str,
) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    authentication_checks: list[dict[str, object]] = []
    audit_checks: list[dict[str, object]] = []
    control_checks: list[dict[str, object]] = []

    _record(authentication_checks, "PLAN_READABLE", plan_error is None, plan_error or "plan JSON object loaded")
    _record(
        authentication_checks,
        "SIDECAR_READABLE",
        sidecar_error is None,
        sidecar_error or "sidecar digest parsed",
    )
    _record(
        authentication_checks,
        "SIDECAR_DIGEST_MATCH",
        actual_plan_sha256 is not None and actual_plan_sha256 == sidecar_sha256,
        "sidecar digest matches plan bytes",
    )
    _record(
        authentication_checks,
        "REFERENCE_FREEZE_AUTHENTICATED",
        reference_error is None,
        reference_error or "repository freeze sidecar matches its plan bytes",
    )
    _record(
        authentication_checks,
        "FROZEN_PLAN_DIGEST_MATCH",
        actual_plan_sha256 is not None and actual_plan_sha256 == reference_freeze_sha256,
        "supplied plan bytes match the repository's authenticated frozen plan",
    )

    freeze = _mapping(plan.get("freeze"))
    declared_subject_sha256 = freeze.get("subject_sha256")
    _record(
        authentication_checks,
        "SUBJECT_HASH_MATCH",
        isinstance(declared_subject_sha256, str) and declared_subject_sha256 == supplied_subject_sha256,
        "declared and supplied subject hashes agree",
    )
    _record(
        authentication_checks,
        "PLAN_SCHEMA",
        plan.get("schema") == SCHEMA,
        "plan uses the declared piecemeal schema",
    )
    authentication = {
        "actual_plan_sha256": actual_plan_sha256,
        "checks": authentication_checks,
        "reference_freeze_sha256": reference_freeze_sha256,
        "declared_subject_sha256": declared_subject_sha256 if isinstance(declared_subject_sha256, str) else None,
        "passed": all(check["passed"] for check in authentication_checks),
        "run_id": RUN_ID,
        "scope": SCOPE,
        "sidecar_sha256": sidecar_sha256,
        "supplied_subject_sha256": supplied_subject_sha256,
    }

    lattices = _mapping(plan.get("lattices"))
    lattice_names = set(lattices)
    _record(
        audit_checks,
        "LATTICE_SET",
        lattice_names == REQUIRED_LATTICES,
        "all and only the six declared lattices remain present",
    )
    source_ids = _row_ids(plan.get("source_register"))
    _record(
        audit_checks,
        "SOURCE_REGISTER",
        REQUIRED_SOURCES.issubset(source_ids),
        "all required primary-source register entries remain present",
    )
    for lattice_name in sorted(REQUIRED_LATTICES):
        lattice = _mapping(lattices.get(lattice_name))
        declared_sources = lattice.get("source_ids")
        sources_are_declared = (
            isinstance(declared_sources, list)
            and all(isinstance(source, str) and source in source_ids for source in declared_sources)
        )
        _record(
            audit_checks,
            f"SOURCES_{lattice_name.upper()}",
            sources_are_declared,
            f"{lattice_name} names only registered sources",
        )
        requirements = _row_ids(lattice.get("pass_requirements"))
        required = REQUIRED_REQUIREMENTS[lattice_name]
        _record(
            audit_checks,
            f"REQUIREMENTS_{lattice_name.upper()}",
            required.issubset(requirements),
            f"{lattice_name} retains its required interfaces",
        )

    integration = _mapping(plan.get("integration_contract"))
    links = integration.get("typed_links")
    link_rows = links if isinstance(links, list) else []
    edges = {
        (row.get("from"), row.get("to"))
        for row in link_rows
        if isinstance(row, Mapping)
    }
    _record(
        audit_checks,
        "TYPED_LINKS",
        REQUIRED_EDGES.issubset(edges)
        and all(
            isinstance(left, str)
            and isinstance(right, str)
            and left in lattice_names
            and right in lattice_names
            for left, right in edges
        ),
        "typed links remain declared between known lattices",
    )
    _record(
        audit_checks,
        "BRIDGE_CONJECTURE_STATUS",
        _mapping(plan.get("bridge_conjecture")).get("status") == "CONJECTURE",
        "the bridge remains labelled as a conjecture",
    )
    _record(
        audit_checks,
        "NON_ENTAILMENTS",
        REQUIRED_NON_ENTAILMENTS.issubset(_row_ids(plan.get("non_entailments"))),
        "critical non-entailments remain explicit",
    )
    plan_audit = {
        "checks": audit_checks,
        "lattice_names": sorted(lattice_names),
        "passed": all(check["passed"] for check in audit_checks),
        "run_id": RUN_ID,
        "scope": SCOPE,
        "source_ids": sorted(source_ids),
    }

    controls = plan.get("negative_controls")
    control_rows = controls if isinstance(controls, list) else []
    control_by_id = {
        row["id"]: row
        for row in control_rows
        if isinstance(row, Mapping) and isinstance(row.get("id"), str)
    }
    _record(
        control_checks,
        "CONTROL_IDS_UNIQUE",
        len(control_by_id) == len(control_rows),
        "negative-control identifiers are unique and well formed",
    )
    _record(
        control_checks,
        "REQUIRED_CONTROLS",
        REQUIRED_CONTROLS.issubset(control_by_id),
        "required anti-collapse controls remain present",
    )
    normalized_controls: list[dict[str, object]] = []
    for control_id in sorted(control_by_id):
        expected = _mapping(control_by_id[control_id].get("expected"))
        valid_lattices = all(
            isinstance(lattice_name, str)
            and lattice_name in lattices
            and isinstance(verdict, str)
            and verdict in _string_list(_mapping(lattices.get(lattice_name)).get("verdicts"))
            for lattice_name, verdict in expected.items()
        )
        _record(
            control_checks,
            f"VERDICTS_{control_id}",
            bool(expected) and valid_lattices,
            f"{control_id} uses declared lattice verdicts",
        )
        normalized_controls.append({"expected": dict(expected), "id": control_id})
    for control_id, expected in sorted(GUARD_EXPECTATIONS.items()):
        actual = _mapping(control_by_id.get(control_id, {})).get("expected")
        _record(
            control_checks,
            f"GUARD_{control_id}",
            isinstance(actual, Mapping)
            and all(actual.get(lattice_name) == verdict for lattice_name, verdict in expected.items()),
            f"{control_id} retains its declared non-creative or non-confirmatory outcome",
        )
    negative_controls = {
        "checks": control_checks,
        "controls": normalized_controls,
        "passed": all(check["passed"] for check in control_checks),
        "run_id": RUN_ID,
        "scope": SCOPE,
    }
    return authentication, plan_audit, negative_controls


def run_campaign(plan_path: Path, output_directory: Path, subject_sha256: str) -> dict[str, object]:
    """Write deterministic frozen-plan integrity artifacts and return their manifest.

    A PASS validates only the frozen plan and its regression controls.  It is not
    a verdict about a candidate system or an attribution of creativity.
    """

    plan, actual_plan_sha256, plan_error = _load_plan(plan_path)
    sidecar_sha256, sidecar_error = _read_sidecar(plan_path)
    reference_freeze_sha256, reference_error = _reference_freeze_digest()
    authentication, plan_audit, negative_controls = _audit(
        plan,
        actual_plan_sha256,
        sidecar_sha256,
        plan_error,
        sidecar_error,
        reference_freeze_sha256,
        reference_error,
        subject_sha256,
    )
    payload = {
        "authentication.json": authentication,
        "plan_audit.json": plan_audit,
        "negative_controls.json": negative_controls,
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    for name in RUN_FILES:
        (output_directory / name).write_bytes(_json_bytes(payload[name]))
    files = [
        {
            "bytes": (output_directory / name).stat().st_size,
            "path": name,
            "sha256": sha256_file(output_directory / name),
        }
        for name in RUN_FILES
    ]
    passed = all(
        bool(payload[name]["passed"])
        for name in RUN_FILES
    )
    manifest = {
        "files": files,
        "run_id": RUN_ID,
        "scope": SCOPE,
        "verdict": "PASS" if passed else "FAIL",
        "warning": "PASS authenticates the frozen plan and controls only; it is not a creativity attribution.",
    }
    (output_directory / "manifest.json").write_bytes(_json_bytes(manifest))
    return manifest
