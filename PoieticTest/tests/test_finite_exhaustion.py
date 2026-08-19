from __future__ import annotations

import json
import unittest

from testpoietic.finite_exhaustion import (
    canonical_evidence_json,
    capstone_literal_witness,
    f2_mutation_matrix,
    f3_target_alignment_witness,
    f4_lookup_false_green_control,
    finite_exhaustion_evidence,
    p31_exhaustion,
    p36_one_mastery_control,
    transition_mutation_evidence,
    transition_semantic_exhaustion,
)


class FiniteExhaustionTests(unittest.TestCase):
    def test_p31_exact_population_and_discriminating_mutant(self) -> None:
        evidence = p31_exhaustion()
        self.assertEqual(evidence["universe_size_range"], [2, 5])
        self.assertEqual(evidence["full_premise_model_count"], 2_592)
        self.assertEqual(evidence["full_premise_counterexample_count"], 0)
        self.assertEqual(evidence["weak_premise_counterexample_count"], 4_480)
        self.assertEqual(
            evidence["minimal_weak_counterexample"],
            {
                "universe_size": 2,
                "attributes": [[0], [1]],
                "corrected_attribute_index": 0,
                "recovery_domain": [1],
            },
        )

    def test_p36_one_mastery_control_exact_population(self) -> None:
        evidence = p36_one_mastery_control()
        self.assertEqual(evidence["copy_bound"], 4)
        self.assertEqual(evidence["state_count"], 50)
        self.assertEqual(evidence["both_capabilities_state_count"], 0)
        self.assertFalse(
            any(row["m0_current"] and row["m1_current"] for row in evidence["rows"])
        )

    def test_transition_mutation_population_is_complete_and_discriminating(self) -> None:
        evidence = transition_mutation_evidence()
        self.assertEqual(evidence["defined_case_ids"], evidence["executed_case_ids"])
        rows = {row["case_id"]: row for row in evidence["rows"]}
        self.assertEqual(
            set(rows),
            {
                "CONTROL",
                "HIDDEN_INTERNAL_ANSWER",
                "STALE_CRITERION",
                "UNLICENSED_AWARD",
                "CLOSED_PERMISSION",
                "OUTCOME_IGNORED",
                "NONRESISTANT_OUTCOME",
                "CANDIDATE_WRITE_BYPASS",
                "DIRECT_EXTERNAL_WRITE",
            },
        )
        self.assertTrue(rows["CONTROL"]["w3"])
        self.assertTrue(rows["CONTROL"]["a5"])
        for case_id in (
            "HIDDEN_INTERNAL_ANSWER",
            "STALE_CRITERION",
            "UNLICENSED_AWARD",
            "CLOSED_PERMISSION",
            "OUTCOME_IGNORED",
        ):
            self.assertTrue(rows[case_id]["w3"], case_id)
            self.assertFalse(rows[case_id]["a5"], case_id)
        self.assertIn(
            "G1_UNAUTHORIZED_SOURCE:hidden_answer:internal_unheld_answer",
            rows["HIDDEN_INTERNAL_ANSWER"]["a5_reasons"],
        )
        self.assertIn(
            "G3_STALE_OR_ABSENT_CRITERION",
            rows["STALE_CRITERION"]["a5_reasons"],
        )
        self.assertIn("G3_UNLICENSED", rows["UNLICENSED_AWARD"]["a5_reasons"])
        self.assertIn("G3_CHANNEL_CLOSED", rows["CLOSED_PERMISSION"]["a5_reasons"])
        self.assertFalse(rows["CANDIDATE_WRITE_BYPASS"]["w3"])
        self.assertFalse(rows["DIRECT_EXTERNAL_WRITE"]["w3"])

    def test_five_dimensional_transition_semantics_are_exhaustive(self) -> None:
        evidence = transition_semantic_exhaustion()
        self.assertEqual(evidence["assignment_count"], 32)
        self.assertEqual(evidence["w3_true_a5_false_count"], 31)
        self.assertEqual(evidence["w3_true_a5_true_count"], 1)
        rows = evidence["rows"]
        self.assertEqual(len(rows), 32)
        assignments = {
            tuple(row[name] for name in evidence["dimensions"]) for row in rows
        }
        self.assertEqual(len(assignments), 32)

    def test_capstone_literal_witness_exposes_vacuous_selected_edge_population(self) -> None:
        evidence = capstone_literal_witness()
        self.assertTrue(evidence["all_displayed_predicates_true_under_universal_reading"])
        self.assertFalse(evidence["length_one_prefix_exists"])
        self.assertTrue(evidence["literal_countermodel"])
        self.assertEqual(evidence["model"]["selected_transition_edges"], [])

    def test_f2_mutants_have_exact_distinct_first_observables(self) -> None:
        evidence = f2_mutation_matrix()
        self.assertEqual(evidence["defined_mutation_ids"], [row["mutation_id"] for row in evidence["rows"]])
        rows = {row["mutation_id"]: row for row in evidence["rows"]}
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows["BATTERY_ID_CHANGED_OUTPUTS_EQUAL"]["expected_gate"], "C2-P1")
        self.assertEqual(rows["LOSSY_POST_OUTCOME_TRANSPORT"]["expected_gate"], "C2-P1")
        self.assertEqual(rows["CONSTANT_IOTA"]["expected_gate"], "C2-P2")
        self.assertEqual(rows["HELDOUT_TARGET_ID_IN_IOTA"]["expected_gate"], "C2-P2")
        self.assertEqual(
            rows["REVERSED_TRANSMISSION_WITH_P1_P2_TRUE"],
            {
                "mutation_id": "REVERSED_TRANSMISSION_WITH_P1_P2_TRUE",
                "expected_gate": "C2",
                "expected_outcome": "REFUTE_ON_DECLARED_DOMAIN",
                "mechanism": "field prediction fails after both admissibility gates survive",
            },
        )

    def test_f3_target_alignment_has_exact_costs_and_target_sensitivity(self) -> None:
        evidence = f3_target_alignment_witness()
        self.assertTrue(evidence["rival_dominates_every_scaling_cut"])
        self.assertTrue(evidence["fringe_localization_usable_every_scaling_cut"])
        self.assertEqual(
            [row["fringe_closed_cost"] for row in evidence["scaling_rows"]],
            [3, 5, 7, 9, 11, 13],
        )
        self.assertEqual(
            [row["library_closed_cost"] for row in evidence["scaling_rows"]],
            [2, 2, 2, 2, 2, 2],
        )
        winners = [row["winner"] for row in evidence["complete_target_sensitivity_rows"]]
        self.assertEqual(winners.count("FRINGE"), 6)
        self.assertEqual(winners.count("LIBRARY"), 2)
        self.assertEqual(winners.count("TIE"), 0)

    def test_f4_finite_lookup_is_an_inconclusive_unrestricted_control(self) -> None:
        evidence = f4_lookup_false_green_control()
        self.assertTrue(evidence["lossless_on_declared_class"])
        self.assertFalse(evidence["receiver_owned_construction_required_by_encoding"])
        self.assertEqual(evidence["expected_unrestricted_verdict"], "INCONCLUSIVE")
        self.assertEqual(
            evidence["frozen_decoder"],
            {"t0": "a0", "t1": "a1", "t2": "a2", "t3": "a3"},
        )

    def test_complete_evidence_population_and_canonical_json_are_deterministic(self) -> None:
        evidence = finite_exhaustion_evidence()
        self.assertEqual(evidence["schema"], "TESTPOIETIC_FINITE_EXHAUSTION_V1")
        self.assertEqual(
            set(evidence),
            {
                "schema",
                "transition_mutations",
                "transition_semantic_exhaustion",
                "p3_1_exhaustion",
                "p3_6_one_mastery_control",
                "capstone_literal_witness",
                "f2_mutation_matrix",
                "f3_target_alignment_witness",
                "f4_lookup_false_green_control",
            },
        )
        first = canonical_evidence_json()
        second = canonical_evidence_json()
        self.assertEqual(first, second)
        self.assertTrue(first.endswith("\n"))
        self.assertEqual(json.loads(first), evidence)


if __name__ == "__main__":
    unittest.main()
