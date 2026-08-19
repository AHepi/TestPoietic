from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from testpoietic.constants import PRIMARY_SHA256
from testpoietic.piecemeal import authenticate_frozen_plan
from testpoietic.piecemeal_calculus import (
    BRIDGE_RULES,
    FORBIDDEN_OUTPUT_TOKENS,
    LATTICE_ORDER,
    NON_ENTAILMENT_GUARDS,
    POSITIVE_VERDICTS,
    CalculusContext,
    CalculusError,
    JudgmentState,
    LocalGate,
    TypedLinkWitness,
    VerdictProfile,
    authenticate_calculus,
    close,
    complete_local_gate,
    enumerate_profiles,
    evaluate_negative_controls,
    evaluate_non_entailment_guards,
    evaluate_profile,
    evaluate_state,
    exhaust_declared_profile_space,
    find_countermodel,
    local_gate,
    refine_with_local_gate,
    refine_with_local_gates,
)

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "evidence" / "frozen" / "piecemeal-plan-v1.json"


class PiecemealCalculusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.signature = authenticate_calculus()

    def profile(self, **overrides: str) -> VerdictProfile:
        values = {
            lattice: "NOT_ESTABLISHED"
            if "NOT_ESTABLISHED" in self.signature.verdicts_for(lattice)
            else self.signature.verdicts_for(lattice)[0]
            for lattice in self.signature.lattice_order
        }
        values.update(overrides)
        return VerdictProfile.from_mapping(values, self.signature)

    def context(
        self,
        lattices: tuple[str, ...] = (),
        witnesses: tuple[TypedLinkWitness, ...] = (),
    ) -> CalculusContext:
        return CalculusContext(
            tuple(complete_local_gate(self.signature, lattice) for lattice in lattices),
            witnesses,
        )

    def trace_witnesses(
        self,
        critical_outcome: str = "SURVIVED_DECLARED_ATTEMPT",
    ) -> tuple[TypedLinkWitness, ...]:
        revision = "revision-a" if critical_outcome == "REFUTED_CONJUNCTION" else None
        return (
            TypedLinkWitness(
                "B_I_R_BEARER_GATE",
                "constructor_information",
                "knowledge_retention",
                "scope-a",
                "information-variable-a",
                "recipe-a",
                knowledge_bearer_id="bearer-a",
            ),
            TypedLinkWitness(
                "B_R_E_REALIZER_CONSTRAINT",
                "knowledge_retention",
                "explanatory_creativity",
                "scope-a",
                "recipe-a",
                "proposal-a",
                knowledge_bearer_id="bearer-a",
                target_claim_id="claim-a",
            ),
            TypedLinkWitness(
                "B_C_E_CRITICISM_LINK",
                "critical_evidence",
                "explanatory_creativity",
                "scope-a",
                "critical-package-a",
                "proposal-a",
                target_claim_id="claim-a",
                critical_outcome=critical_outcome,
                revision_route_id=revision,
            ),
        )

    def full_trace_context(
        self,
        critical_outcome: str = "SURVIVED_DECLARED_ATTEMPT",
    ) -> CalculusContext:
        return self.context(
            (
                "constructor_information",
                "knowledge_retention",
                "critical_evidence",
                "explanatory_creativity",
            ),
            self.trace_witnesses(critical_outcome),
        )

    def test_authenticated_signature_binds_exact_product_bridges_and_guards(self) -> None:
        self.assertEqual(self.signature.lattice_order, LATTICE_ORDER)
        self.assertEqual(self.signature.requirement_count, 44)
        self.assertEqual(self.signature.profile_count, 1800)
        self.assertEqual(len(self.signature.typed_links), 4)
        self.assertEqual(len(self.signature.non_entailment_ids), 20)
        self.assertEqual(len(self.signature.negative_controls), 13)
        self.assertEqual(
            {guard.rule_id for guard in NON_ENTAILMENT_GUARDS},
            set(self.signature.non_entailment_ids),
        )
        executable_edges = {
            (rule.source_lattices[0], rule.target_lattice)
            for rule in BRIDGE_RULES
            if rule.rule_id != "B_H_CONDITIONAL_BRANCH"
        }
        self.assertEqual(
            executable_edges,
            {(source, target) for source, target, _ in self.signature.typed_links},
        )

    def test_product_refinement_and_closure_are_idempotent(self) -> None:
        initial = JudgmentState.initial(self.signature)
        c_missing = initial.constrain(
            self.signature, "critical_evidence", {"NOT_ESTABLISHED"}
        )
        closed = close(c_missing, self.signature)
        self.assertTrue(closed.state.refines(c_missing, self.signature))
        self.assertNotIn(
            "CRITICISABLE_TRACE_AUDITED",
            closed.state.permitted(self.signature, "explanatory_creativity"),
        )
        self.assertEqual(close(closed.state, self.signature).state, closed.state)
        self.assertEqual(
            evaluate_state(c_missing, self.signature).outcome,
            "UNDERDETERMINED_PROFILE",
        )

        conflict = c_missing.constrain(
            self.signature,
            "explanatory_creativity",
            {"CRITICISABLE_TRACE_AUDITED"},
        )
        self.assertFalse(close(conflict, self.signature).state.is_consistent(self.signature))

    def test_all_44_atomic_requirements_are_necessary_without_becoming_sufficient(self) -> None:
        initial = JudgmentState.initial(self.signature)
        complete_gates = []
        for lattice in self.signature.lattice_order:
            requirements = frozenset(self.signature.requirements_for(lattice))
            complete = local_gate(self.signature, lattice, requirements)
            complete_gates.append(complete)
            self.assertTrue(complete.is_complete, lattice)
            self.assertEqual(refine_with_local_gate(initial, complete, self.signature), initial)
            for requirement in requirements:
                gate = local_gate(self.signature, lattice, requirements - {requirement})
                refined = refine_with_local_gate(initial, gate, self.signature)
                self.assertFalse(gate.is_complete, f"{lattice}:{requirement}")
                self.assertFalse(
                    POSITIVE_VERDICTS[lattice]
                    & refined.permitted(self.signature, lattice),
                    f"{lattice}:{requirement}",
                )

        all_complete = refine_with_local_gates(initial, complete_gates, self.signature)
        self.assertEqual(all_complete, initial)
        self.assertEqual(
            evaluate_state(all_complete, self.signature).outcome,
            "UNDERDETERMINED_PROFILE",
        )

    def test_raw_positive_statuses_are_not_audited_without_local_gates(self) -> None:
        h_profile = self.profile(no_design_replication="MAY_PASS")
        raw_h = evaluate_profile(h_profile, self.signature)
        self.assertNotIn(
            "CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED", raw_h.relations
        )
        gated_h = evaluate_profile(
            h_profile,
            self.signature,
            self.context(("no_design_replication",)),
        )
        self.assertIn(
            "CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED", gated_h.relations
        )

        missing_correction = local_gate(
            self.signature,
            "no_design_replication",
            set(self.signature.requirements_for("no_design_replication"))
            - {"H_ERROR_CORRECTION"},
        )
        unsupported_h = evaluate_profile(
            h_profile,
            self.signature,
            CalculusContext((missing_correction,)),
        )
        self.assertEqual(unsupported_h.outcome, "INCONSISTENT_PROFILE")
        self.assertNotIn(
            "CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED", unsupported_h.relations
        )

    def test_c_to_e_requires_a_matching_typed_witness(self) -> None:
        profile = self.profile(
            critical_evidence="SURVIVED_DECLARED_ATTEMPT",
            explanatory_creativity="CRITICISABLE_TRACE_AUDITED",
        )
        no_link = evaluate_profile(
            profile,
            self.signature,
            self.context(("critical_evidence", "explanatory_creativity")),
        )
        self.assertEqual(no_link.outcome, "INCONSISTENT_PROFILE")
        self.assertNotIn("CRITICISABLE_EXPLANATORY_TRACE", no_link.relations)

        c_e_link = self.trace_witnesses()[2]
        linked = evaluate_profile(
            profile,
            self.signature,
            self.context(("critical_evidence", "explanatory_creativity"), (c_e_link,)),
        )
        self.assertEqual(linked.outcome, "CRITICISABLE_TRACE_REALIZER_NOT_ESTABLISHED")
        self.assertIn("CRITICISABLE_EXPLANATORY_TRACE", linked.relations)
        self.assertNotIn("CRITICISABLE_REALIZER_TRACE", linked.relations)

    def test_knowledge_bearer_boundary_link_is_not_whole_agent_clonability(self) -> None:
        profile = self.profile(
            constructor_information="MAY_PASS",
            knowledge_retention="MAY_PASS",
            no_design_replication="NOT_APPLICABLE",
            critical_evidence="SURVIVED_DECLARED_ATTEMPT",
            explanatory_creativity="CRITICISABLE_TRACE_AUDITED",
        )
        witnesses = self.trace_witnesses()
        without_i_r = evaluate_profile(
            profile,
            self.signature,
            self.context(
                (
                    "constructor_information",
                    "knowledge_retention",
                    "critical_evidence",
                    "explanatory_creativity",
                ),
                (witnesses[1], witnesses[2]),
            ),
        )
        self.assertEqual(
            without_i_r.outcome,
            "CRITICISABLE_TRACE_REALIZER_NOT_ESTABLISHED",
        )
        self.assertNotIn("PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", without_i_r.relations)

        linked = evaluate_profile(profile, self.signature, self.full_trace_context())
        self.assertEqual(linked.outcome, "CRITICISABLE_REALIZER_TRACE_AUDITED")
        self.assertIn("PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", linked.relations)
        self.assertIn("CRITICISABLE_REALIZER_TRACE", linked.relations)
        self.assertIn(
            "NE_WHOLE_CREATOR_NOT_CLONABLE",
            {finding.rule_id for finding in linked.findings},
        )

    def test_realizer_trace_requires_one_identity_preserving_chain(self) -> None:
        profile = self.profile(
            constructor_information="MAY_PASS",
            knowledge_retention="MAY_PASS",
            critical_evidence="SURVIVED_DECLARED_ATTEMPT",
            explanatory_creativity="CRITICISABLE_TRACE_AUDITED",
        )
        spliced = (
            TypedLinkWitness(
                "B_I_R_BEARER_GATE",
                "constructor_information",
                "knowledge_retention",
                "scope-a",
                "information-variable-a",
                "recipe-a",
                knowledge_bearer_id="bearer-a",
            ),
            TypedLinkWitness(
                "B_R_E_REALIZER_CONSTRAINT",
                "knowledge_retention",
                "explanatory_creativity",
                "scope-a",
                "recipe-b",
                "proposal-b",
                knowledge_bearer_id="bearer-a",
                target_claim_id="claim-a",
            ),
            TypedLinkWitness(
                "B_C_E_CRITICISM_LINK",
                "critical_evidence",
                "explanatory_creativity",
                "scope-a",
                "critical-package-c",
                "proposal-c",
                target_claim_id="claim-a",
                critical_outcome="SURVIVED_DECLARED_ATTEMPT",
            ),
        )
        evaluation = evaluate_profile(
            profile,
            self.signature,
            self.context(
                (
                    "constructor_information",
                    "knowledge_retention",
                    "critical_evidence",
                    "explanatory_creativity",
                ),
                spliced,
            ),
        )
        self.assertEqual(
            evaluation.outcome,
            "CRITICISABLE_TRACE_REALIZER_NOT_ESTABLISHED",
        )
        self.assertIn("CRITICISABLE_EXPLANATORY_TRACE", evaluation.relations)
        self.assertNotIn("CRITICISABLE_REALIZER_TRACE", evaluation.relations)
    def test_refuted_c_package_records_scope_without_auto_falsifying_e(self) -> None:
        audited_profile = self.profile(
            constructor_information="MAY_PASS",
            knowledge_retention="MAY_PASS",
            critical_evidence="REFUTED_CONJUNCTION",
            explanatory_creativity="CRITICISABLE_TRACE_AUDITED",
        )
        witnesses = self.trace_witnesses("REFUTED_CONJUNCTION")
        without_revision_link = evaluate_profile(
            audited_profile,
            self.signature,
            self.context(
                (
                    "constructor_information",
                    "knowledge_retention",
                    "critical_evidence",
                    "explanatory_creativity",
                ),
                witnesses[:2],
            ),
        )
        self.assertEqual(
            without_revision_link.outcome,
            "REFUTATION_RECORDED_ON_DECLARED_DOMAIN",
        )
        self.assertNotIn("CRITICISABLE_EXPLANATORY_TRACE", without_revision_link.relations)
        self.assertNotIn("CRITICISABLE_REALIZER_TRACE", without_revision_link.relations)

        revised = evaluate_profile(
            audited_profile,
            self.signature,
            self.full_trace_context("REFUTED_CONJUNCTION"),
        )
        self.assertEqual(revised.outcome, "CRITICISABLE_REALIZER_TRACE_AUDITED")
        self.assertIn("CRITICISABLE_REALIZER_TRACE", revised.relations)

        direct_refutation_link = TypedLinkWitness(
            "B_C_E_CRITICISM_LINK",
            "critical_evidence",
            "explanatory_creativity",
            "scope-a",
            "critical-package-a",
            "proposal-a",
            target_claim_id="claim-a",
            critical_outcome="REFUTED_CONJUNCTION",
        )
        unsupported_audit = evaluate_profile(
            audited_profile,
            self.signature,
            self.context(
                (
                    "constructor_information",
                    "knowledge_retention",
                    "critical_evidence",
                    "explanatory_creativity",
                ),
                witnesses[:2] + (direct_refutation_link,),
            ),
        )
        self.assertEqual(
            unsupported_audit.outcome,
            "REFUTATION_RECORDED_ON_DECLARED_DOMAIN",
        )

        refuted_profile = self.profile(
            critical_evidence="REFUTED_CONJUNCTION",
            explanatory_creativity="REFUTED_ON_DECLARED_DOMAIN",
        )
        raw_refutation = evaluate_profile(refuted_profile, self.signature)
        self.assertEqual(raw_refutation.outcome, "INCONSISTENT_PROFILE")
        self.assertNotIn("CRITICISABLE_EXPLANATORY_TRACE", raw_refutation.relations)

        scoped_refutation = evaluate_profile(
            refuted_profile,
            self.signature,
            self.context(
                ("critical_evidence", "explanatory_creativity"),
                (direct_refutation_link,),
            ),
        )
        self.assertEqual(scoped_refutation.outcome, "REFUTED_ON_DECLARED_DOMAIN")
        self.assertIn(
            "SCOPED_REFUTATION_LINK_DECLARED",
            {finding.result for finding in scoped_refutation.findings},
        )
        self.assertNotIn("CRITICISABLE_EXPLANATORY_TRACE", scoped_refutation.relations)

    def test_every_frozen_non_entailment_is_an_executable_refusal(self) -> None:
        results = evaluate_non_entailment_guards(self.signature)
        self.assertEqual(len(results), 20)
        self.assertEqual(
            {result.rule_id for result in results},
            set(self.signature.non_entailment_ids),
        )
        self.assertTrue(all(result.passed for result in results))
        self.assertEqual(
            {result.kind for result in results},
            {"PROFILE_COUNTERMODEL", "LOCAL_GATE_COUNTERMODEL", "SCOPE_OUTPUT_GUARD"},
        )

    def test_frozen_negative_controls_test_their_named_shortcut_bans(self) -> None:
        results = {row.control_id: row for row in evaluate_negative_controls(self.signature)}
        self.assertEqual(len(results), 13)
        self.assertTrue(all(row.passed for row in results.values()))
        self.assertEqual(
            results["NC_NAKED_REPLICATOR"].evaluation.outcome,
            "SELECTION_ANALOGUE_ONLY",
        )
        self.assertEqual(
            results["NC_CREATOR_WITHOUT_SELF_REPRODUCTION"].evaluation.outcome,
            "UNRESOLVED_NOT_NON_CREATIVE",
        )
        agreeing = results["NC_AGREEING_RESULT_NOT_CONFIRMATION"].evaluation
        self.assertIn("THEORY_MEDIATED_CRITICISM_PACKAGE", agreeing.relations)
        self.assertNotIn("CRITICISABLE_EXPLANATORY_TRACE", agreeing.relations)
        self.assertIn(
            "NE_EVIDENCE_NOT_CONFIRMATION",
            {finding.rule_id for finding in agreeing.findings},
        )

    def test_countermodels_and_profile_enumeration_remain_finite_and_typed(self) -> None:
        profiles = tuple(enumerate_profiles(self.signature))
        self.assertEqual(len(profiles), 1800)
        self.assertEqual(len({tuple(profile.as_dict().items()) for profile in profiles}), 1800)
        self.assertEqual(
            len(tuple(enumerate_profiles(self.signature, {"evolutionary_selection": "MAY_PASS"}))),
            900,
        )
        countermodel = find_countermodel(
            self.signature,
            {
                "constructor_information": "MAY_PASS",
                "knowledge_retention": "NOT_ESTABLISHED",
            },
            prohibited_relations={"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED"},
            context=self.context(("constructor_information",)),
        )
        self.assertIsNotNone(countermodel)

    def test_exhaustion_is_not_a_creativity_proof_or_all_theories_claim(self) -> None:
        result = exhaust_declared_profile_space(self.signature)
        self.assertEqual(result.profile_count, 1800)
        self.assertLess(result.admissible_profile_count, result.profile_count)
        self.assertEqual(sum(dict(result.outcome_counts).values()), 1800)
        self.assertTrue(result.forbidden_output_absent)
        for profile in enumerate_profiles(self.signature):
            evaluation = evaluate_profile(profile, self.signature)
            self.assertFalse(
                FORBIDDEN_OUTPUT_TOKENS & (set(evaluation.relations) | {evaluation.outcome})
            )

    def test_rehashed_tampered_plan_fails_the_fixed_digest_gate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tampered = root / "rewritten.json"
            plan_bytes = PLAN.read_bytes().replace(
                b"TESTPOIETIC_PIECEMEAL_PLAN_V1",
                b"TESTPOIETIC_PIECEMEAL_PLAN_X1",
                1,
            )
            tampered.write_bytes(plan_bytes)
            tampered.with_suffix(".sha256").write_text(
                f"{hashlib.sha256(plan_bytes).hexdigest()}  rewritten.json\n",
                encoding="ascii",
            )
            _, report = authenticate_frozen_plan(tampered, PRIMARY_SHA256)
            checks = {row["id"]: row for row in report["authentication"]["checks"]}
            self.assertFalse(checks["FROZEN_PLAN_DIGEST_MATCH"]["passed"])
            with self.assertRaises(CalculusError):
                authenticate_calculus(tampered)

    def test_invalid_or_forged_local_context_is_rejected(self) -> None:
        with self.assertRaises(CalculusError):
            local_gate(self.signature, "constructor_information", {"I_UNKNOWN"})
        forged = LocalGate(
            "constructor_information",
            frozenset({"I_BOUNDARY"}),
            frozenset({"I_BOUNDARY"}),
        )
        with self.assertRaises(CalculusError):
            evaluate_state(
                JudgmentState.initial(self.signature),
                self.signature,
                CalculusContext((forged,)),
            )


if __name__ == "__main__":
    unittest.main()