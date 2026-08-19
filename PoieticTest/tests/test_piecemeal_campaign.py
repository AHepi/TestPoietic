from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from testpoietic import piecemeal
from testpoietic.constants import PRIMARY_SHA256
from testpoietic.piecemeal import RUN_FILES, SCOPE, run_campaign

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "evidence" / "frozen" / "piecemeal-plan-v1.json"
RUNNER = ROOT / "scripts" / "run_piecemeal_campaign.py"
CAMPAIGN_001 = ROOT / "evidence" / "runs" / "campaign-001"


def _canonical_json(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _tree_hashes(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


class PiecemealCampaignTests(unittest.TestCase):
    def test_authentic_plan_writes_integrity_only_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "run"
            manifest = run_campaign(PLAN, output, PRIMARY_SHA256)

            self.assertEqual(manifest["verdict"], "PASS")
            self.assertEqual(manifest["scope"], SCOPE)
            self.assertIn("not a creativity attribution", manifest["warning"])
            self.assertEqual(
                {row["path"] for row in manifest["files"]},
                set(RUN_FILES),
            )
            for name in (*RUN_FILES, "manifest.json"):
                self.assertTrue((output / name).is_file(), name)
            self.assertEqual(
                json.loads((output / "manifest.json").read_text(encoding="utf-8")),
                manifest,
            )
            audit = json.loads((output / "plan_audit.json").read_text(encoding="utf-8"))
            self.assertTrue(audit["passed"])
            self.assertEqual(audit["scope"], SCOPE)

    def test_cli_uses_public_runner_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "cli-run"
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(RUNNER),
                    "--plan",
                    str(PLAN),
                    "--out",
                    str(output),
                ],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["verdict"], "PASS")
            self.assertTrue((output / "manifest.json").is_file())

    def test_two_authentic_runs_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first"
            second = root / "second"
            self.assertEqual(run_campaign(PLAN, first, PRIMARY_SHA256)["verdict"], "PASS")
            self.assertEqual(run_campaign(PLAN, second, PRIMARY_SHA256)["verdict"], "PASS")

            for name in (*RUN_FILES, "manifest.json"):
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes(), name)

    def test_wrong_subject_hash_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "wrong-subject"
            manifest = run_campaign(PLAN, output, "0" * 64)

            self.assertEqual(manifest["verdict"], "FAIL")
            authentication = json.loads((output / "authentication.json").read_text(encoding="utf-8"))
            by_id = {check["id"]: check for check in authentication["checks"]}
            self.assertFalse(by_id["SUBJECT_HASH_MATCH"]["passed"])

    def test_rehashed_weakened_plan_fails_negative_control_regression(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            weakened = json.loads(PLAN.read_text(encoding="utf-8"))
            weakened["negative_controls"] = [
                row
                for row in weakened["negative_controls"]
                if row["id"] != "NC_SELECTION_WITHOUT_CRITICISM"
            ]
            plan_path = root / "weakened.json"
            plan_bytes = _canonical_json(weakened)
            plan_path.write_bytes(plan_bytes)
            plan_path.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  weakened.json\n",
                encoding="ascii",
            )

            manifest = run_campaign(plan_path, root / "weakened-run", PRIMARY_SHA256)

            self.assertEqual(manifest["verdict"], "FAIL")
            controls = json.loads(
                (root / "weakened-run" / "negative_controls.json").read_text(encoding="utf-8")
            )
            by_id = {check["id"]: check for check in controls["checks"]}
            self.assertFalse(by_id["REQUIRED_CONTROLS"]["passed"])

    def test_rehashed_plan_cannot_bypass_canonical_freeze(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rewritten = json.loads(PLAN.read_text(encoding="utf-8"))
            for lattice in rewritten["lattices"].values():
                lattice["source_ids"] = []
            plan_path = root / "rewritten.json"
            plan_bytes = _canonical_json(rewritten)
            plan_path.write_bytes(plan_bytes)
            plan_path.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  rewritten.json\n",
                encoding="ascii",
            )

            manifest = run_campaign(plan_path, root / "rewritten-run", PRIMARY_SHA256)

            self.assertEqual(manifest["verdict"], "FAIL")
            authentication = json.loads(
                (root / "rewritten-run" / "authentication.json").read_text(encoding="utf-8")
            )
            by_id = {check["id"]: check for check in authentication["checks"]}
            self.assertFalse(by_id["FROZEN_PLAN_DIGEST_MATCH"]["passed"])

    def test_rewritten_canonical_baseline_cannot_bypass_digest_pin(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            rewritten = json.loads(PLAN.read_text(encoding="utf-8"))
            rewritten["lattices"]["constructor_information"]["source_ids"] = []
            plan_path = root / "canonical-rewritten.json"
            plan_bytes = _canonical_json(rewritten)
            plan_path.write_bytes(plan_bytes)
            plan_path.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  canonical-rewritten.json\n",
                encoding="ascii",
            )

            with patch.object(piecemeal, "CANONICAL_PLAN", plan_path):
                manifest = piecemeal.run_campaign(
                    plan_path,
                    root / "canonical-rewritten-run",
                    PRIMARY_SHA256,
                )

            self.assertEqual(manifest["verdict"], "FAIL")
            authentication = json.loads(
                (root / "canonical-rewritten-run" / "authentication.json").read_text(
                    encoding="utf-8"
                )
            )
            by_id = {check["id"]: check for check in authentication["checks"]}
            self.assertFalse(by_id["REFERENCE_FREEZE_AUTHENTICATED"]["passed"])

    def test_malformed_typed_links_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            malformed = json.loads(PLAN.read_text(encoding="utf-8"))
            malformed["integration_contract"]["typed_links"] = {"unexpected": "mapping"}
            plan_path = root / "malformed.json"
            plan_bytes = _canonical_json(malformed)
            plan_path.write_bytes(plan_bytes)
            plan_path.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  malformed.json\n",
                encoding="ascii",
            )

            manifest = run_campaign(plan_path, root / "malformed-run", PRIMARY_SHA256)

            self.assertEqual(manifest["verdict"], "FAIL")
            audit = json.loads((root / "malformed-run" / "plan_audit.json").read_text(encoding="utf-8"))
            by_id = {check["id"]: check for check in audit["checks"]}
            self.assertFalse(by_id["TYPED_LINKS"]["passed"])

    def test_null_verdict_vocabulary_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            malformed = json.loads(PLAN.read_text(encoding="utf-8"))
            malformed["lattices"]["constructor_information"]["verdicts"] = None
            plan_path = root / "null-verdicts.json"
            plan_bytes = _canonical_json(malformed)
            plan_path.write_bytes(plan_bytes)
            plan_path.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  null-verdicts.json\n",
                encoding="ascii",
            )

            manifest = run_campaign(plan_path, root / "null-verdicts-run", PRIMARY_SHA256)

            self.assertEqual(manifest["verdict"], "FAIL")
            controls = json.loads(
                (root / "null-verdicts-run" / "negative_controls.json").read_text(
                    encoding="utf-8"
                )
            )
            by_id = {check["id"]: check for check in controls["checks"]}
            self.assertFalse(by_id["VERDICTS_NC_INFORMATION_WITHOUT_RETENTION"]["passed"])

    def test_non_utf8_plan_or_sidecar_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cases = (
                ("invalid-plan", b"\xff\xfe\xfd", None, "PLAN_READABLE"),
                ("invalid-sidecar", PLAN.read_bytes(), b"\xff", "SIDECAR_READABLE"),
            )
            for name, plan_bytes, sidecar_bytes, failed_check in cases:
                with self.subTest(name=name):
                    plan_path = root / f"{name}.json"
                    plan_path.write_bytes(plan_bytes)
                    sidecar_path = plan_path.with_suffix(".sha256")
                    if sidecar_bytes is None:
                        sidecar_path.write_text(
                            f"{hashlib.sha256(plan_bytes).hexdigest()}  {plan_path.name}\n",
                            encoding="ascii",
                        )
                    else:
                        sidecar_path.write_bytes(sidecar_bytes)

                    output = root / f"{name}-run"
                    manifest = run_campaign(plan_path, output, PRIMARY_SHA256)

                    self.assertEqual(manifest["verdict"], "FAIL")
                    self.assertTrue((output / "manifest.json").is_file())
                    authentication = json.loads(
                        (output / "authentication.json").read_text(encoding="utf-8")
                    )
                    by_id = {check["id"]: check for check in authentication["checks"]}
                    self.assertFalse(by_id[failed_check]["passed"])

    def test_piecemeal_run_leaves_campaign_001_untouched(self) -> None:
        before = _tree_hashes(CAMPAIGN_001)
        with tempfile.TemporaryDirectory() as temporary:
            manifest = run_campaign(PLAN, Path(temporary) / "piecemeal", PRIMARY_SHA256)
            self.assertEqual(manifest["verdict"], "PASS")
        self.assertEqual(_tree_hashes(CAMPAIGN_001), before)


if __name__ == "__main__":
    unittest.main()
