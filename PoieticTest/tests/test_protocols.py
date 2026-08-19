from __future__ import annotations

import unittest

from testpoietic.constants import PRIMARY_SUBJECT
from testpoietic.protocols import (
    F3_POLICY_TERMS,
    LINE_ANCHORS,
    audit_protocol_text,
    check_line_anchors,
    f3_policy_closure_audit,
    optimism_f6_address_audit,
    rg_f8d_quantifier_audit,
    rx_refuter_scope_audit,
)


class ProtocolAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = PRIMARY_SUBJECT.read_text(encoding="utf-8")

    def test_all_frozen_line_anchors_match(self) -> None:
        rows = check_line_anchors(self.source)
        self.assertEqual(len(rows), len(LINE_ANCHORS))
        self.assertTrue(all(row["match"] for row in rows), rows)

    def test_line_insertion_is_detected(self) -> None:
        shifted = "inserted line\n" + self.source
        self.assertFalse(all(row["match"] for row in check_line_anchors(shifted)))

    def test_rg_f8d_quantifier_scope_has_discriminating_model(self) -> None:
        result = rg_f8d_quantifier_audit(self.source)
        witness = result["finite_discriminator"]
        self.assertTrue(result["outer_quantifier_is_existential"])
        self.assertTrue(result["protocol_claims_one_frozen_witness_failure_refutes_residue"])
        self.assertTrue(witness["frozen_G_fails"])
        self.assertTrue(witness["R_G_true"])
        self.assertTrue(result["mismatch"])

    def test_rg_repaired_verdict_is_a_negative_fixture(self) -> None:
        repaired = self.source.replace(
            "threshold miss refutes \\(R_G\\) on the declared family.",
            "threshold miss refutes only that frozen \\(G\\).",
            1,
        )
        self.assertNotEqual(repaired, self.source)
        self.assertFalse(rg_f8d_quantifier_audit(repaired)["mismatch"])
        anchor = next(
            row for row in check_line_anchors(repaired)
            if row["identifier"] == "protocol-f8-d"
        )
        self.assertFalse(anchor["match"])

    def test_rx_prose_refuter_is_weaker_than_existential_negation(self) -> None:
        result = rx_refuter_scope_audit(self.source)
        witness = result["finite_discriminator"]
        self.assertTrue(result["consequent_is_existential"])
        self.assertTrue(witness["prose_refuter_triggered"])
        self.assertTrue(witness["R_X_true"])
        self.assertTrue(result["mismatch"])

    def test_rx_full_class_refuter_is_a_negative_fixture(self) -> None:
        repaired = self.source.replace(
            "A live problem with no extension-ready good resolution refutes it at that cut.",
            "A nonempty \\(W_t\\) in which every member lacks an extension-ready task "
            "for the same cut refutes it at that cut.",
            1,
        )
        self.assertNotEqual(repaired, self.source)
        self.assertFalse(rx_refuter_scope_audit(repaired)["mismatch"])

    def test_o_is_routed_to_f6_without_an_o_verdict_rule(self) -> None:
        result = optimism_f6_address_audit(self.source)
        self.assertTrue(result["ledger_routes_O_to_F6"])
        self.assertTrue(result["O_declares_a_refuter"])
        self.assertTrue(result["F6_excludes_inference_from_O"])
        self.assertFalse(result["F6_has_O_specific_verdict_rule"])
        self.assertTrue(result["mismatch"])

    def test_o_specific_f6_rule_is_a_negative_fixture(self) -> None:
        needle = "the composition theorem remains intact but inapplicable."
        replacement = (
            needle
            + " A well-specified physically admissible problem for which no possible "
            "explanatory resolution or transforming knowledge exists refutes "
            "Conjecture O."
        )
        repaired = self.source.replace(needle, replacement, 1)
        self.assertNotEqual(repaired, self.source)
        result = optimism_f6_address_audit(repaired)
        self.assertTrue(result["F6_has_O_specific_verdict_rule"])
        self.assertFalse(result["mismatch"])

    def test_f3_arms_are_named_but_undefined_and_nonclosed(self) -> None:
        result = f3_policy_closure_audit(self.source)
        self.assertEqual(set(result["policy_terms_named_in_F3"]), set(F3_POLICY_TERMS))
        self.assertEqual(set(result["undefined_terms"]), set(F3_POLICY_TERMS))
        self.assertFalse(result["arm_assignment_closed"])
        self.assertTrue(result["mismatch"])
        overlap = result["overlap_witness_under_ordinary_reading"]
        self.assertTrue(overlap["failure-fringe targeting"])
        self.assertTrue(overlap["library-local"])
        self.assertTrue(overlap["promotion-shy"])

    def test_defined_exclusive_f3_arms_are_a_negative_fixture(self) -> None:
        definitions = """
A policy is failure-fringe targeting iff its next target is selected by a retained failure locator.
A policy is library-local iff its next operator is selected only from a frozen local library.
A policy is promotion-shy iff it withholds every intermediate operative promotion.
A policy is directionless iff target selection is independent of appraisal and failure records.
The F3 policy classes are mutually exclusive and exhaustive.
"""
        repaired = self.source + definitions
        result = f3_policy_closure_audit(repaired)
        self.assertEqual(result["undefined_terms"], [])
        self.assertTrue(result["mutually_exclusive_rule"])
        self.assertTrue(result["arm_assignment_closed"])
        self.assertFalse(result["mismatch"])

    def test_aggregate_observables_are_stable(self) -> None:
        result = audit_protocol_text(self.source)
        self.assertTrue(result["all_line_anchors_match"])
        self.assertEqual(result["mismatch_count"], 4)
        self.assertEqual(
            [row["id"] for row in result["findings"]],
            [
                "RG-F8D-QUANTIFIER-SCOPE",
                "RX-PROSE-REFUTER-SCOPE",
                "O-F6-MISSING-VERDICT-RULE",
                "F3-POLICY-ARMS-NONCLOSED",
            ],
        )


if __name__ == "__main__":
    unittest.main()
