from __future__ import annotations

import unittest

from testpoietic.claims import extract_claims, grade_audit, section_metrics, verify_subject_tree
from testpoietic.constants import PRIMARY_SUBJECT, REPOSITORY_ROOT


class SubjectAuthenticationTests(unittest.TestCase):
    def test_subject_and_declared_parents_are_byte_authenticated(self) -> None:
        result = verify_subject_tree(REPOSITORY_ROOT)
        self.assertTrue(result["all_match"])
        self.assertTrue(result["primary"]["match"])
        self.assertTrue(all(row["match"] for row in result["parents"]))

    def test_source_has_exact_line_count_and_anchor_text(self) -> None:
        lines = PRIMARY_SUBJECT.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 1805)
        self.assertIn("F3, failure-fringe policy tournament", lines[1595])
        self.assertIn("F8-D, answer-generic jump construction", lines[1613])
        self.assertIn("Purpose-coverage guard", lines[1542])

    def test_claim_inventory_is_nonempty_and_auditable(self) -> None:
        claims = extract_claims()
        audit = grade_audit(claims)
        self.assertGreater(audit["claim_count"], 40)
        self.assertIsInstance(audit["unknown_grades"], list)
        self.assertIsInstance(audit["ungraded_formal_claims"], list)

    def test_meta_partition_is_total(self) -> None:
        result = section_metrics()
        metrics = result["metrics"]
        self.assertEqual(metrics["meta"]["lines"] + metrics["theory"]["lines"], 1805)
        self.assertGreater(metrics["meta"]["words"], 0)
        self.assertGreater(metrics["theory"]["words"], metrics["meta"]["words"])


if __name__ == "__main__":
    unittest.main()
