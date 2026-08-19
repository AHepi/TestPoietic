from __future__ import annotations

import unittest

from testpoietic.constants import PRIMARY_SUBJECT
from testpoietic.purpose_guard import audit_purpose_guard


def complete_transport_fixture() -> dict[str, object]:
    record = {
        "source_nodes": ["old"],
        "target_nodes": ["new"],
        "grade": "same",
        "refuter": "F-test",
    }
    return {
        "rows": {
            row: {face: dict(record) for face in ("K", "S", "F", "M")}
            for row in (
                "what_creativity_is",
                "what_a_creator_must_be",
                "how_attribution_and_refutation_proceed",
            )
        }
    }


class PurposeGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = PRIMARY_SUBJECT.read_text(encoding="utf-8")

    def test_surface_score_but_not_semantic_transport_reproduces(self) -> None:
        result = audit_purpose_guard(self.source)
        self.assertEqual(result["table_rows"], 3)
        self.assertEqual(result["nonempty_face_cells"], 12)
        self.assertTrue(result["surface_pcov_12_reproduced"])
        self.assertFalse(result["transport_manifest"]["valid"])
        self.assertFalse(result["retroactive_pret_verdict_recomputable"])
        self.assertEqual(
            result["audit_verdict"],
            "SURFACE SCORE REPRODUCES; SEMANTIC TRANSPORT DOES NOT",
        )

    def test_guard_is_a_standing_inheritance_gate_with_no_declared_inference(self) -> None:
        result = audit_purpose_guard(self.source)
        self.assertTrue(result["standing_inheritance_gate"])
        self.assertEqual(result["declared_inferential_force"], "none")

    def test_typed_complete_manifest_is_a_discrimination_control(self) -> None:
        result = audit_purpose_guard(self.source, complete_transport_fixture())
        self.assertTrue(result["transport_manifest"]["valid"])
        self.assertEqual(result["transport_manifest"]["mapped_faces"], 12)
        self.assertTrue(result["retroactive_pret_verdict_recomputable"])

    def test_incomplete_manifest_is_rejected(self) -> None:
        fixture = complete_transport_fixture()
        fixture["rows"]["what_creativity_is"]["K"]["refuter"] = ""
        result = audit_purpose_guard(self.source, fixture)
        self.assertFalse(result["transport_manifest"]["valid"])


if __name__ == "__main__":
    unittest.main()
