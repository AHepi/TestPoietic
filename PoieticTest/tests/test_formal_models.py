from __future__ import annotations

import copy
import unittest

from testpoietic.formal_models import (
    a5_satisfied,
    all_formal_models,
    anj_reversal_gap,
    b_core_direct_write_countermodel,
    c2_counterdomain,
    finite_prefix_transition_existence_gap,
    fragility_reachability_countermodel,
    literal_w3_satisfied,
    p35_cut_countermodel,
    provenance_distance_nonunique,
    rg_quantifier_countermodel,
    rx_refuter_quantifier_countermodel,
    t7_repair_partition_countermodel,
    target_essential_idle_metadata_countermodel,
    tref_box_countermodel,
    w3_vacuity_countermodel,
)


class FormalModelTests(unittest.TestCase):
    def test_w3_does_not_supply_missing_a5_relations(self) -> None:
        witness = w3_vacuity_countermodel()
        self.assertTrue(witness["literal_w3"])
        self.assertFalse(witness["a5"])
        self.assertTrue(witness["counterexample"])

    def test_w3_countermodel_is_discriminating(self) -> None:
        model = copy.deepcopy(w3_vacuity_countermodel()["model"])
        model["nodes"]["write"]["occupant_source"] = "candidate"
        model["nodes"]["write"]["open_permission"] = True
        model["nodes"]["award"]["licensed_by_current_criterion"] = True
        self.assertTrue(literal_w3_satisfied(model))
        self.assertTrue(a5_satisfied(model))

    def test_p35_cut_scope_witness(self) -> None:
        witness = p35_cut_countermodel()
        self.assertTrue(witness["direct_route_premises_on_beta"])
        self.assertFalse(witness["full_K_embedding_exists"])
        self.assertTrue(witness["counterexample"])

    def test_rg_existential_witness_survives_nominated_failure(self) -> None:
        witness = rg_quantifier_countermodel()
        self.assertTrue(witness["nominated_G_fails"])
        self.assertTrue(witness["R_G_true_on_declared_class"])
        self.assertTrue(witness["counterexample"])

    def test_t7_nonexhaustive_repair_classes_break_descent(self) -> None:
        witness = t7_repair_partition_countermodel()
        self.assertTrue(witness["strict_retreat_available"])
        self.assertTrue(witness["retreat_cheaper_than_every_content_preserving_repair"])
        self.assertFalse(witness["strict_descent"])
        self.assertTrue(witness["counterexample"])

    def test_fragility_does_not_schedule_exit(self) -> None:
        witness = fragility_reachability_countermodel()
        self.assertTrue(witness["scheduler_selects_install_path"])
        self.assertFalse(witness["exit_from_growing_regime_reachable"])
        self.assertTrue(witness["counterexample"])

    def test_target_essentiality_accepts_idle_metadata(self) -> None:
        witness = target_essential_idle_metadata_countermodel()
        self.assertTrue(witness["literal_definition_satisfied"])
        self.assertFalse(witness["operative_or_award_relevant_change"])
        self.assertTrue(witness["counterexample"])

    def test_unified_tref_box_drops_required_conjunct(self) -> None:
        witness = tref_box_countermodel()
        self.assertTrue(witness["boxed_antecedent_true"])
        self.assertFalse(witness["TRef_true"])
        self.assertTrue(witness["counterexample"])

    def test_provenance_distance_is_not_unique(self) -> None:
        witness = provenance_distance_nonunique()
        self.assertFalse(witness["unique_distance"])
        self.assertTrue(witness["counterexample"])

    def test_transition_grammar_lacks_reversal(self) -> None:
        witness = anj_reversal_gap()
        self.assertTrue(witness["standing_change_exists"])
        self.assertFalse(witness["reversal_reachable"])
        self.assertTrue(witness["counterexample"])

    def test_rx_prose_refuter_reverses_existential_logic(self) -> None:
        witness = rx_refuter_quantifier_countermodel()
        self.assertTrue(witness["one_failed_problem_exists"])
        self.assertTrue(witness["R_X_true"])
        self.assertTrue(witness["counterexample"])

    def test_capstone_transition_clauses_can_be_vacuous(self) -> None:
        witness = finite_prefix_transition_existence_gap()
        self.assertTrue(witness["universal_transition_clauses_vacuously_true"])
        self.assertFalse(witness["length_one_prefix_exists"])
        self.assertTrue(witness["countermodel_under_literal_universal_reading"])

    def test_c2_is_exposed_on_a_finite_counterdomain(self) -> None:
        witness = c2_counterdomain()
        self.assertTrue(witness["pinning_prediction_correct"])
        self.assertTrue(witness["stable_reversal"])
        self.assertTrue(witness["counterdomain"])

    def test_b_core_modal_reading_has_direct_write_countermodel(self) -> None:
        witness = b_core_direct_write_countermodel()
        self.assertGreater(witness["admissible_boundary_count"], 0)
        self.assertTrue(witness["every_admissible_boundary_fails_a5"])
        self.assertTrue(witness["countermodel"])
        self.assertIn("not evidence", witness["scope"])

    def test_all_declared_counterexamples_remain_present(self) -> None:
        payload = all_formal_models()
        self.assertEqual(
            set(payload),
            {
                "w3_to_a5",
                "p35_cut_scope",
                "rg_quantifier",
                "t7_repair_partition",
                "fragility_reachability",
                "target_essential_idle_metadata",
                "tref_box",
                "provenance_distance",
                "anj_reversal",
                "rx_refuter_quantifier",
                "finite_prefix_transition_existence",
                "capstone_residues",
                "finite_prefix_gap",
                "c2_counterdomain",
                "b_core_direct_write",
            },
        )


if __name__ == "__main__":
    unittest.main()
