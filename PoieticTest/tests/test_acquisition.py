"""Executable, discriminating checks for the finite S12 acquisition results."""

from __future__ import annotations

from fractions import Fraction
import unittest

from testpoietic.acquisition import (
    ExactQuery,
    FiniteAcquisitionModel,
    canonical_binary_queries,
    corollary_12_2_certificate,
    exact_majority_error,
    exhaustive_binary_campaign,
    mutant_best_case_cost,
    optimal_worst_cost,
    proposition_12_3_certificate,
    reachable_states,
    required_odd_repetitions,
    theorem_12_1_certificate,
)


class ModelValidationTests(unittest.TestCase):
    def test_rejects_empty_or_duplicate_hypotheses(self) -> None:
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel((), ())
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel(("h", "h"), ())

    def test_rejects_malformed_query_and_nonpositive_cost(self) -> None:
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel(
                ("a", "b"),
                (ExactQuery("short", (0,), Fraction(1)),),
            )
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel(
                ("a", "b"),
                (ExactQuery("free", (0, 1), Fraction(0)),),
            )

    def test_rejects_unknown_availability_and_cost_rows(self) -> None:
        whole = frozenset(("a", "b"))
        query = ExactQuery("q", (0, 1))
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel(
                ("a", "b"),
                (query,),
                availability={whole: ("missing",)},
            )
        with self.assertRaises(ValueError):
            FiniteAcquisitionModel(
                ("a", "b"),
                (query,),
                state_costs={("q", whole): Fraction(-1)},
            )


class Theorem121Tests(unittest.TestCase):
    def test_exact_bellman_fixture_and_tight_bounds(self) -> None:
        model = FiniteAcquisitionModel(
            hypotheses=("00", "01", "10", "11"),
            queries=(
                ExactQuery("high_bit", (0, 0, 1, 1), Fraction(1)),
                ExactQuery("low_bit", (0, 1, 0, 1), Fraction(1)),
            ),
        )
        certificate = theorem_12_1_certificate(model)
        self.assertEqual(optimal_worst_cost(model), Fraction(2))
        self.assertTrue(certificate["assumptions_satisfied"])
        self.assertTrue(certificate["lower_bound_holds_exactly"])
        self.assertTrue(certificate["upper_bound_holds_exactly"])
        self.assertAlmostEqual(float(certificate["lower_bound"]), 2.0, places=12)
        self.assertAlmostEqual(float(certificate["upper_bound"]), 2.0, places=12)

    def test_no_separating_test_makes_claim_inapplicable(self) -> None:
        model = FiniteAcquisitionModel(
            hypotheses=("a", "b", "c"),
            queries=(ExactQuery("constant", (0, 0, 0)),),
        )
        certificate = theorem_12_1_certificate(model)
        self.assertIsNone(optimal_worst_cost(model))
        self.assertFalse(certificate["assumptions_satisfied"])
        self.assertIsNone(certificate["theorem_holds"])

    def test_explicit_missing_stage_availability_is_not_silently_filled(self) -> None:
        whole = frozenset(("a", "b", "c"))
        model = FiniteAcquisitionModel(
            hypotheses=("a", "b", "c"),
            queries=(
                ExactQuery("first", (0, 1, 1)),
                ExactQuery("tail", (0, 0, 1)),
            ),
            availability={whole: ("first",)},
        )
        self.assertIn(frozenset(("b", "c")), reachable_states(model))
        self.assertIsNone(optimal_worst_cost(model))
        self.assertFalse(theorem_12_1_certificate(model)["assumptions_satisfied"])

    def test_bad_best_case_mutant_is_killed(self) -> None:
        whole = frozenset(("a", "b", "c"))
        tail = frozenset(("b", "c"))
        model = FiniteAcquisitionModel(
            hypotheses=("a", "b", "c"),
            queries=(
                ExactQuery("first", (0, 1, 1), Fraction(1)),
                ExactQuery("tail", (0, 0, 1), Fraction(10)),
            ),
            availability={whole: ("first",), tail: ("tail",)},
        )
        correct = optimal_worst_cost(model)
        mutant = mutant_best_case_cost(model)
        self.assertEqual(correct, Fraction(11))
        self.assertEqual(mutant, Fraction(1))
        self.assertNotEqual(mutant, correct, "the best-case Bellman mutant survived")

    def test_all_binary_maps_are_canonical_and_nonconstant(self) -> None:
        queries = canonical_binary_queries(4)
        self.assertEqual(len(queries), 7)
        self.assertEqual(len({query.outcomes for query in queries}), 7)
        self.assertTrue(all(query.outcomes[0] == 0 for query in queries))
        self.assertTrue(all(len(set(query.outcomes)) == 2 for query in queries))

    def test_exhaustive_binary_campaign(self) -> None:
        result = exhaustive_binary_campaign(max_hypotheses=4)
        self.assertEqual(result["enumerated_models"], 2214)
        self.assertEqual(result["models_by_hypothesis_count"], {"2": 2, "3": 26, "4": 2186})
        self.assertGreater(result["theorem_applicable_models"], 0)
        self.assertEqual(
            result["theorem_applicable_models"],
            result["corollary_applicable_models"],
        )
        self.assertEqual(result["theorem_failures"], [])
        self.assertEqual(result["corollary_failures"], [])
        self.assertTrue(result["all_applicable_claims_hold"])


class Corollary122Tests(unittest.TestCase):
    def test_unbalanced_five_way_fixture_obeys_declared_limits(self) -> None:
        hypotheses = tuple(f"h{index}" for index in range(5))
        queries = tuple(
            ExactQuery(
                f"is_{index}",
                tuple(1 if position == index else 0 for position in range(5)),
                Fraction(3, 2),
            )
            for index in range(4)
        )
        model = FiniteAcquisitionModel(hypotheses, queries)
        certificate = corollary_12_2_certificate(
            model,
            contraction=Fraction(4, 5),
            cost_limit=Fraction(3, 2),
        )
        self.assertTrue(certificate["separability_satisfied"])
        self.assertTrue(certificate["conclusion_checked"])
        self.assertLessEqual(
            certificate["constructed_policy_worst_queries"],
            certificate["query_limit"],
        )

    def test_fails_when_cost_bound_is_not_met(self) -> None:
        model = FiniteAcquisitionModel(
            ("a", "b"),
            (ExactQuery("split", (0, 1), Fraction(2)),),
        )
        certificate = corollary_12_2_certificate(
            model,
            contraction=Fraction(1, 2),
            cost_limit=Fraction(1),
        )
        self.assertFalse(certificate["separability_satisfied"])
        self.assertIsNone(certificate["conclusion_checked"])

    def test_rejects_invalid_parameters_and_singleton_model(self) -> None:
        singleton = FiniteAcquisitionModel(("a",), ())
        with self.assertRaises(ValueError):
            corollary_12_2_certificate(singleton, Fraction(1, 2), Fraction(1))
        binary = FiniteAcquisitionModel(("a", "b"), (ExactQuery("q", (0, 1)),))
        for invalid_lambda in (Fraction(0), Fraction(1), Fraction(2)):
            with self.assertRaises(ValueError):
                corollary_12_2_certificate(binary, invalid_lambda, Fraction(1))


class Proposition123Tests(unittest.TestCase):
    def test_exact_majority_tail_known_value(self) -> None:
        self.assertEqual(exact_majority_error(3, Fraction(1, 4)), Fraction(5, 32))

    def test_required_odd_r_meets_bound_and_exact_tail(self) -> None:
        certificate = proposition_12_3_certificate(
            hypothesis_count=16,
            contraction=Fraction(1, 2),
            failure_tolerance=Fraction(1, 100),
            noise_rate=Fraction(1, 10),
            repetition_cost=Fraction(2),
            majority_cost=Fraction(3),
        )
        self.assertEqual(certificate["logical_steps_m"], 4)
        self.assertTrue(certificate["odd_repetition_count"])
        self.assertTrue(certificate["displayed_threshold_met"])
        self.assertTrue(certificate["theorem_guarantee_applies"])
        self.assertTrue(certificate["exact_union_within_delta"])

    def test_small_r_and_even_r_do_not_receive_theorem_guarantee(self) -> None:
        required, _ = required_odd_repetitions(3, Fraction(1, 10), Fraction(1, 4))
        too_small = proposition_12_3_certificate(
            8,
            Fraction(1, 2),
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(1),
            Fraction(0),
            repetitions=required - 2,
        )
        even = proposition_12_3_certificate(
            8,
            Fraction(1, 2),
            Fraction(1, 10),
            Fraction(1, 4),
            Fraction(1),
            Fraction(0),
            repetitions=required + 1,
        )
        self.assertFalse(too_small["theorem_guarantee_applies"])
        self.assertFalse(even["theorem_guarantee_applies"])
        self.assertIsNone(even["exact_worst_iid_majority_error"])

    def test_rational_parameter_grid_has_exact_union_control(self) -> None:
        for hypotheses in (2, 3, 8, 17):
            for contraction in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
                for delta in (Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)):
                    for noise in (Fraction(0), Fraction(1, 10), Fraction(1, 4), Fraction(2, 5)):
                        with self.subTest(
                            N=hypotheses,
                            lambda_=contraction,
                            delta=delta,
                            nu=noise,
                        ):
                            certificate = proposition_12_3_certificate(
                                hypotheses,
                                contraction,
                                delta,
                                noise,
                                Fraction(1),
                                Fraction(0),
                            )
                            self.assertTrue(certificate["theorem_guarantee_applies"])
                            self.assertTrue(certificate["exact_union_within_delta"])

    def test_rejects_noise_boundary_and_nonpositive_logical_inputs(self) -> None:
        with self.assertRaises(ValueError):
            required_odd_repetitions(1, Fraction(1, 10), Fraction(1, 2))
        with self.assertRaises(ValueError):
            required_odd_repetitions(0, Fraction(1, 10), Fraction(1, 4))
        with self.assertRaises(ValueError):
            proposition_12_3_certificate(
                1,
                Fraction(1, 2),
                Fraction(1, 10),
                Fraction(1, 4),
                Fraction(1),
                Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
