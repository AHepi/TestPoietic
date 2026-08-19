from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from testpoietic.candidate import RUN_FILES, SCOPE, evaluate_candidate
from testpoietic.constants import PRIMARY_SHA256
from testpoietic.piecemeal import CANONICAL_PLAN, FROZEN_PLAN_SHA256

ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads(CANONICAL_PLAN.read_text(encoding="utf-8"))


def _canonical_json(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _packet(lattice_id: str, verdict: str, applicability: str = "CLAIMED") -> dict[str, object]:
    status = "NOT_APPLICABLE" if applicability == "NOT_APPLICABLE" else "SATISFIED"
    return {
        "applicability": applicability,
        "claimed_verdict": verdict,
        "responses": [
            {
                "assertion": f"declared structural binding for {requirement['id']}",
                "evidence_refs": ["record-1"],
                "object_refs": ["candidate-1"],
                "refuter": "refuter-1",
                "requirement_id": requirement["id"],
                "status": status,
            }
            for requirement in PLAN["lattices"][lattice_id]["pass_requirements"]
        ],
        "scope": "declared-domain-1",
    }


def _valid_witness() -> dict[str, object]:
    packets = {
        "constructor_information": _packet("constructor_information", "MAY_PASS"),
        "knowledge_retention": _packet("knowledge_retention", "MAY_PASS"),
        "no_design_replication": _packet(
            "no_design_replication", "NOT_APPLICABLE", "NOT_APPLICABLE"
        ),
        "evolutionary_selection": _packet("evolutionary_selection", "MAY_PASS"),
        "critical_evidence": _packet(
            "critical_evidence", "SURVIVED_DECLARED_ATTEMPT"
        ),
        "explanatory_creativity": _packet(
            "explanatory_creativity", "CRITICISABLE_TRACE_AUDITED"
        ),
    }
    return {
        "schema": "TESTPOIETIC_CANDIDATE_WITNESS_V1",
        "witness_id": "witness-1",
        "pins": {
            "subject_sha256": PRIMARY_SHA256,
            "plan_schema": PLAN["schema"],
            "plan_sha256": FROZEN_PLAN_SHA256,
        },
        "attribution": {
            "claim_id": "claim-1",
            "claim_type": "STRUCTURAL_CANDIDATE_AUDIT",
            "target_problem_id": "problem-1",
            "declared_domain": "declared-domain-1",
            "finite_cohort": "one declared candidate in one finite test domain",
            "environment_scope": "declared laboratory environment",
            "model_assumptions": "declared auxiliary assumptions only",
            "excluded_universal_claims": "no universal attribution or confirmation claim",
        },
        "candidate": {
            "candidate_id": "candidate-1",
            "boundary": {
                "inside_component_ids": ["candidate-1"],
                "outside_component_ids": [
                    "environment-1",
                    "instrument-1",
                    "reduction-1",
                    "observer-1",
                ],
                "interface_ids": ["interface-1"],
                "environment_class": "declared laboratory environment",
                "resource_ids": ["resource-1"],
                "temporal_window": "episode-1",
                "boundary_rationale": "candidate boundary is stated for the finite task",
                "alternative_boundaries": ["candidate-plus-interface-1"],
            },
        },
        "physical_bearers": [
            {
                "bearer_id": "candidate-1",
                "role": "candidate physical substrate",
                "description": "declared physical candidate",
                "boundary_status": "INSIDE",
            },
            {
                "bearer_id": "environment-1",
                "role": "environment",
                "description": "declared finite environment",
                "boundary_status": "OUTSIDE",
            },
            {
                "bearer_id": "interface-1",
                "role": "interface",
                "description": "candidate-environment interface",
                "boundary_status": "INTERFACE",
            },
            {
                "bearer_id": "instrument-1",
                "role": "measurement instrument",
                "description": "declared measuring instrument",
                "boundary_status": "OUTSIDE",
            },
            {
                "bearer_id": "reduction-1",
                "role": "data-reduction system",
                "description": "declared reduction or calibration system",
                "boundary_status": "OUTSIDE",
            },
            {
                "bearer_id": "observer-1",
                "role": "observer or inference system",
                "description": "declared observer or inference bearer",
                "boundary_status": "OUTSIDE",
            },
        ],
        "evidence_records": [
            {
                "record_id": "record-1",
                "kind": "declared measurement record",
                "artifact_ref": "declared-only:record-1",
                "sha256": "a" * 64,
                "producer": "candidate-1",
                "access_scope": "declared but not dereferenced",
            }
        ],
        "counterfactual_tests": [
            {
                "test_id": "counterfactual-1",
                "baseline": "declared baseline task execution",
                "change_or_removal": "remove the declared value",
                "close_variant": "same finite environment with only the declared value changed",
                "task_success_criterion": "declared finite task criterion",
                "permitted_side_effects": "declared finite side effects",
                "environment_class": "declared laboratory environment",
                "resource_conditions": "declared finite resources",
                "predicted_difference": "declared task failure or relevant change",
                "record_refs": ["record-1"],
                "finite_domain": "declared-domain-1",
            }
        ],
        "knowledge_items": [
            {
                "knowledge_id": "knowledge-1",
                "role": "K_CONSTRUCTION_RECIPE",
                "value_description": "declared causal recipe value",
                "bearer_id": "candidate-1",
                "task_id": "task-1",
                "history_location": "CANDIDATE",
                "history_node_id": "candidate-1",
                "history_evidence_refs": ["record-1"],
                "retention_route_id": "retention-1",
                "counterfactual_test_ids": ["counterfactual-1"],
            }
        ],
        "critical_evidence_packages": [
            {
                "package_id": "critical-1",
                "target_claim_id": "proposal-1",
                "problem_id": "problem-1",
                "channel": "THEORY_LADEN_OBSERVATION",
                "record_refs": ["record-1"],
                "interpretation_chain": [
                    {
                        "component_id": "instrument-1",
                        "role": "INSTRUMENT_OR_SENSE",
                        "failure_mode": "calibration error",
                    },
                    {
                        "component_id": "reduction-1",
                        "role": "CALIBRATION_OR_DATA_REDUCTION",
                        "failure_mode": "software reduction error",
                    },
                    {
                        "component_id": "observer-1",
                        "role": "INFERENCE",
                        "failure_mode": "interpretive error",
                    },
                ],
                "auxiliary_claim_ids": ["auxiliary-1"],
                "initial_condition_ids": ["initial-1"],
                "rival_or_incompatibility": "declared rival explanation",
                "discriminator": "declared distinguishable consequence",
                "discriminator_id": "refuter-1",
                "declared_conjunction": "proposal-1 plus declared auxiliaries",
                "declared_domain": "declared-domain-1",
                "protocol": "predeclared attempted-refutation protocol",
                "attempts": ["attempt-1"],
                "revision_event_ids": ["revision-1"],
                "outcome": "SURVIVED_DECLARED_ATTEMPT",
            }
        ],
        "creation_episodes": [
            {
                "episode_id": "episode-1",
                "p1": "declared problem",
                "proposals": [
                    {
                        "proposal_id": "proposal-1",
                        "explanatory_content": "declared tentative explanation",
                        "origin": "candidate-1",
                        "error_domain": "declared error domain",
                        "possible_refuter_ids": ["refuter-1"],
                        "critical_package_ids": ["critical-1"],
                        "revision_route": "revision-1",
                    }
                ],
                "ee": "declared error-elimination attempt",
                "p2": "declared revised problem",
            }
        ],
        "provenance_graph": {
            "nodes": [
                {"node_id": "candidate-1", "node_type": "CANDIDATE"},
                {"node_id": "environment-1", "node_type": "ENVIRONMENT"},
            ],
            "edges": [],
            "input_class_disclosure": {
                input_class: "ABSENT_ON_DECLARED_BOUNDARY"
                for input_class in (
                    "PROMPT",
                    "SEED",
                    "TRAINING",
                    "DATASET",
                    "TOOL",
                    "ORACLE",
                    "SCORE",
                    "HUMAN",
                    "PARENT",
                    "EXTERNAL_BUILDER",
                )
            },
            "unresolved_input_ids": [],
        },
        "selection_processes": [
            {
                "population_boundary": "declared finite population",
                "lineage": "declared lineage",
                "inheritance": "declared inheritance relation",
                "viable_offspring_criterion": "declared viability criterion",
                "variation_mechanism": "declared variation mechanism",
                "nonspecificity_evidence": "declared non-specificity evidence",
                "not_guaranteed_in_advance": "declared fallibility condition",
                "finite_resource_environment": "declared finite resources",
                "differential_continuation_records": ["record-1"],
                "bridge_role": "TYPED_FALLIBILITY_ANALOGUE_ONLY",
            }
        ],
        "lattices": packets,
    }


def _add_external_bearer(
    witness: dict[str, object],
    *,
    bearer_id: str,
    node_type: str,
    with_path: bool = True,
) -> None:
    boundary = witness["candidate"]["boundary"]
    boundary["outside_component_ids"].append(bearer_id)
    witness["physical_bearers"].append(
        {
            "bearer_id": bearer_id,
            "role": f"declared {node_type.lower()} bearer",
            "description": f"physical bearer for declared {node_type.lower()} input",
            "boundary_status": "OUTSIDE",
        }
    )
    provenance = witness["provenance_graph"]
    provenance["nodes"].append({"node_id": bearer_id, "node_type": node_type})
    provenance["input_class_disclosure"][node_type] = "PRESENT"
    if with_path:
        provenance["edges"].append(
            {
                "source_id": bearer_id,
                "target_id": "candidate-1",
                "relation": "declared causal or relevant input path",
                "evidence_refs": ["record-1"],
            }
        )


def _claim_high_accuracy_replication(witness: dict[str, object]) -> None:
    h_packet = witness["lattices"]["no_design_replication"]
    h_packet["applicability"] = "CLAIMED"
    h_packet["claimed_verdict"] = "MAY_PASS"
    for response in h_packet["responses"]:
        response["status"] = "SATISFIED"

    def binding(**fields: object) -> dict[str, object]:
        return {
            "recipe_knowledge_id": "knowledge-1",
            "bearer_id": "candidate-1",
            "evidence_refs": ["record-1"],
            "counterfactual_test_ids": ["counterfactual-1"],
            **fields,
        }

    witness["replication_claim"] = {
        "accuracy_measure": "declared high and indefinitely improvable accuracy",
        "no_design_basis": "declared no-design-law scope",
        "generic_resources": "declared generic resources",
        "recipe_knowledge_id": "knowledge-1",
        "digital_unit_variable": binding(
            variable_id="recipe-unit-variable-1",
            nonallowed_value_separation="forbidden interpolation is declared",
            attributes=["recipe-unit-0", "recipe-unit-1"],
        ),
        "error_detection_task": binding(
            task_id="detect-recipe-error-1",
            criterion="declared recipe-value mismatch criterion",
        ),
        "error_correction_task": binding(
            task_id="correct-recipe-error-1",
            criterion="declared recipe-value correction criterion",
        ),
        "blind_copying": binding(
            task_id="blind-copy-recipe-unit-1",
            modular_unit_ids=["recipe-unit-0", "recipe-unit-1"],
        ),
        "vehicle_boundary": "candidate-1",
        "evidence_refs": ["record-1"],
    }


def _run(witness: dict[str, object], output: Path) -> tuple[dict[str, object], dict[str, object]]:
    witness_path = output.parent / f"{output.name}.json"
    witness_path.write_bytes(_canonical_json(witness))
    manifest = evaluate_candidate(witness_path, output)
    audit = json.loads((output / "candidate_audit.json").read_text(encoding="utf-8"))
    return manifest, audit


class CandidateWitnessTests(unittest.TestCase):
    def test_valid_witness_is_structural_only_and_deterministic(self) -> None:
        witness = _valid_witness()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first_manifest, first_audit = _run(witness, root / "first")
            second_manifest, _ = _run(witness, root / "second")

            self.assertEqual(
                first_manifest["outcome"],
                "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION",
            )
            self.assertEqual(first_manifest["scope"], SCOPE)
            self.assertIn("does not dereference evidence", first_manifest["warning"])
            self.assertEqual(first_audit["attribution"]["declared_domain"], "declared-domain-1")
            self.assertTrue(first_audit["package_complete"])
            self.assertEqual(
                {row["path"] for row in first_manifest["files"]},
                set(RUN_FILES),
            )
            for name in (*RUN_FILES, "manifest.json"):
                self.assertEqual(
                    (root / "first" / name).read_bytes(),
                    (root / "second" / name).read_bytes(),
                    name,
                )
            self.assertEqual(first_manifest, second_manifest)

    def test_wrong_witness_plan_pin_is_not_plan_authentication_failure(self) -> None:
        witness = _valid_witness()
        witness["pins"]["plan_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        self.assertTrue(audit["package_complete"])

    def test_missing_critical_chain_downgrades_critical_and_explanatory_lattices(self) -> None:
        witness = _valid_witness()
        critical_responses = witness["lattices"]["critical_evidence"]["responses"]
        witness["lattices"]["critical_evidence"]["responses"] = [
            row for row in critical_responses if row["requirement_id"] != "C_CHAIN"
        ]
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["critical_evidence"], "EVIDENCE_PACKAGE_INCOMPLETE")
        self.assertEqual(outcomes["explanatory_creativity"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_bare_score_cannot_substitute_for_critical_package(self) -> None:
        witness = _valid_witness()
        witness["critical_evidence_packages"] = []
        witness["evidence_records"][0]["kind"] = "score"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_confirmation_is_schema_invalid(self) -> None:
        witness = _valid_witness()
        witness["critical_evidence_packages"][0]["outcome"] = "CONFIRMED"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        checks = {row["id"]: row for row in audit["schema_checks"]}
        self.assertFalse(checks["NO_CONFIRMATION_OUTCOME"]["passed"])

    def test_creativity_proof_claim_type_is_rejected(self) -> None:
        witness = _valid_witness()
        witness["attribution"]["claim_type"] = "CREATIVITY_PROVEN"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        checks = {row["id"]: row for row in audit["schema_checks"]}
        self.assertFalse(checks["NO_CREATIVITY_PROOF_CLAIM"]["passed"])

    def test_counterfactual_and_lattice_scopes_must_match_attribution_domain(self) -> None:
        cases = (
            (
                "counterfactual-domain",
                lambda witness: witness["counterfactual_tests"][0].update(
                    {"finite_domain": "other-domain"}
                ),
            ),
            (
                "lattice-domain",
                lambda witness: witness["lattices"]["constructor_information"].update(
                    {"scope": "other-domain"}
                ),
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, mutate in cases:
                with self.subTest(name=name):
                    witness = _valid_witness()
                    mutate(witness)
                    manifest, _ = _run(witness, root / name)
                    self.assertEqual(
                        manifest["outcome"],
                        "EVIDENCE_PACKAGE_INCOMPLETE",
                    )
    def test_external_recipe_is_not_candidate_attributed(self) -> None:
        witness = _valid_witness()
        _add_external_bearer(
            witness,
            bearer_id="builder-1",
            node_type="EXTERNAL_BUILDER",
        )
        witness["knowledge_items"][0]["history_location"] = "EXTERNAL_BUILDER"
        witness["knowledge_items"][0]["history_node_id"] = "builder-1"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "PROVENANCE_UNRESOLVED")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["knowledge_retention"], "EXTERNAL_P_NOT_ATTRIBUTED")

    def test_non_self_reproducer_can_declare_h_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(_valid_witness(), Path(temporary) / "run")

        self.assertEqual(
            manifest["outcome"],
            "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION",
        )

    def test_claimed_replication_requires_linked_recipe_and_error_correction_evidence(self) -> None:
        witness = _valid_witness()
        _claim_high_accuracy_replication(witness)
        witness["replication_claim"]["recipe_knowledge_id"] = "unknown-knowledge"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["no_design_replication"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_claimed_replication_rejects_unlinked_digital_or_correction_labels(self) -> None:
        witness = _valid_witness()
        _claim_high_accuracy_replication(witness)
        witness["replication_claim"]["digital_unit_variable"] = "digital-ish label"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_typed_claimed_replication_can_be_structurally_audited(self) -> None:
        witness = _valid_witness()
        _claim_high_accuracy_replication(witness)
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(
            manifest["outcome"],
            "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION",
        )
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["no_design_replication"], "STRUCTURALLY_COMPLETE")

    def test_selection_without_critical_trace_cannot_discharge_explanatory_lattice(self) -> None:
        witness = _valid_witness()
        witness["creation_episodes"] = []
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["explanatory_creativity"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_unrefutable_proposal_is_incomplete(self) -> None:
        witness = _valid_witness()
        witness["creation_episodes"][0]["proposals"][0]["possible_refuter_ids"] = []
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_malformed_refuted_package_cannot_trigger_refutation_outcome(self) -> None:
        witness = _valid_witness()
        witness["critical_evidence_packages"][0]["outcome"] = "REFUTED_CONJUNCTION"
        witness["critical_evidence_packages"][0]["record_refs"] = []
        witness["lattices"]["critical_evidence"]["claimed_verdict"] = "REFUTED_CONJUNCTION"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_valid_refutation_is_scoped_to_the_declared_conjunction_and_domain(self) -> None:
        witness = _valid_witness()
        witness["critical_evidence_packages"][0]["outcome"] = "REFUTED_CONJUNCTION"
        witness["lattices"]["critical_evidence"]["claimed_verdict"] = "REFUTED_CONJUNCTION"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "REFUTATION_RECORDED_ON_DECLARED_DOMAIN")
        self.assertEqual(
            audit["refutation_scopes"],
            [
                {
                    "declared_conjunction": "proposal-1 plus declared auxiliaries",
                    "declared_domain": "declared-domain-1",
                    "target_claim_id": "proposal-1",
                }
            ],
        )

    def test_empty_or_malformed_references_fail_closed(self) -> None:
        cases = (
            ("empty-response-evidence", lambda witness: witness["lattices"]["constructor_information"]["responses"][0].update({"evidence_refs": []}), "EVIDENCE_PACKAGE_INCOMPLETE"),
            ("invalid-record-hash", lambda witness: witness["evidence_records"][0].update({"sha256": "not-a-hash"}), "WITNESS_SCHEMA_INVALID"),
            ("unlisted-bearer", lambda witness: witness["knowledge_items"][0].update({"bearer_id": "unlisted"}), "EVIDENCE_PACKAGE_INCOMPLETE"),
            ("scalar-list-entry", lambda witness: witness["physical_bearers"].append(7), "WITNESS_SCHEMA_INVALID"),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, mutate, expected in cases:
                with self.subTest(name=name):
                    witness = _valid_witness()
                    mutate(witness)
                    manifest, _ = _run(witness, root / name)
                    self.assertEqual(manifest["outcome"], expected)

    def test_scalar_containers_fail_closed(self) -> None:
        cases = (
            (
                "witness-id-container",
                lambda witness: witness.update({"witness_id": []}),
                "WITNESS_SCHEMA_INVALID",
            ),
            (
                "attribution-domain-container",
                lambda witness: witness["attribution"].update({"declared_domain": {}}),
                "WITNESS_SCHEMA_INVALID",
            ),
            (
                "record-kind-container",
                lambda witness: witness["evidence_records"][0].update({"kind": []}),
                "WITNESS_SCHEMA_INVALID",
            ),
            (
                "physical-status-container",
                lambda witness: witness["physical_bearers"][0].update(
                    {"boundary_status": []}
                ),
                "WITNESS_SCHEMA_INVALID",
            ),
            (
                "selection-lineage-container",
                lambda witness: witness["selection_processes"][0].update(
                    {"lineage": {}}
                ),
                "EVIDENCE_PACKAGE_INCOMPLETE",
            ),
            (
                "selection-records-container",
                lambda witness: witness["selection_processes"][0].update(
                    {"differential_continuation_records": {}}
                ),
                "EVIDENCE_PACKAGE_INCOMPLETE",
            ),
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name, mutate, expected in cases:
                with self.subTest(name=name):
                    witness = _valid_witness()
                    mutate(witness)
                    manifest, _ = _run(witness, root / name)
                    self.assertEqual(manifest["outcome"], expected)

    def test_critical_chain_requires_declared_physical_bearer(self) -> None:
        witness = _valid_witness()
        witness["critical_evidence_packages"][0]["interpretation_chain"][0][
            "component_id"
        ] = "ghost-instrument"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "EVIDENCE_PACKAGE_INCOMPLETE")

    def test_present_input_requires_evidence_backed_path_to_candidate(self) -> None:
        witness = _valid_witness()
        _add_external_bearer(
            witness,
            bearer_id="training-1",
            node_type="TRAINING",
            with_path=False,
        )
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        checks = {row["id"]: row for row in audit["schema_checks"]}
        self.assertFalse(checks["PROVENANCE_PRESENT_INPUT_PATHS"]["passed"])

    def test_external_proposal_origin_is_not_candidate_attributed(self) -> None:
        witness = _valid_witness()
        _add_external_bearer(
            witness,
            bearer_id="builder-1",
            node_type="EXTERNAL_BUILDER",
        )
        witness["creation_episodes"][0]["proposals"][0]["origin"] = "builder-1"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "PROVENANCE_UNRESOLVED")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["explanatory_creativity"], "PROVENANCE_UNRESOLVED")

    def test_parent_knowledge_outside_boundary_is_not_candidate_attributed(self) -> None:
        witness = _valid_witness()
        _add_external_bearer(witness, bearer_id="parent-1", node_type="PARENT")
        witness["knowledge_items"][0]["history_location"] = "PARENT"
        witness["knowledge_items"][0]["history_node_id"] = "parent-1"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "PROVENANCE_UNRESOLVED")
        outcomes = {row["lattice_id"]: row["outcome"] for row in audit["lattices"]}
        self.assertEqual(outcomes["knowledge_retention"], "EXTERNAL_P_NOT_ATTRIBUTED")

    def test_physical_boundary_status_must_match_partition(self) -> None:
        witness = _valid_witness()
        witness["physical_bearers"][0]["boundary_status"] = "OUTSIDE"
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        checks = {row["id"]: row for row in audit["schema_checks"]}
        self.assertFalse(checks["PHYSICAL_BOUNDARY_AGREEMENT"]["passed"])

    def test_unresolved_input_requires_unresolved_node_type(self) -> None:
        witness = _valid_witness()
        witness["provenance_graph"]["input_class_disclosure"]["PROMPT"] = "UNRESOLVED"
        witness["provenance_graph"]["unresolved_input_ids"] = ["unknown-prompt-1"]
        witness["provenance_graph"]["nodes"].append(
            {"node_id": "unknown-prompt-1", "node_type": "PROMPT"}
        )
        with tempfile.TemporaryDirectory() as temporary:
            manifest, audit = _run(witness, Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "WITNESS_SCHEMA_INVALID")
        checks = {row["id"]: row for row in audit["schema_checks"]}
        self.assertFalse(checks["UNRESOLVED_INPUT_TYPES"]["passed"])
    def test_candidate_audit_does_not_mutate_frozen_plan(self) -> None:
        before = hashlib.sha256(CANONICAL_PLAN.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory() as temporary:
            manifest, _ = _run(_valid_witness(), Path(temporary) / "run")

        self.assertEqual(manifest["outcome"], "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION")
        self.assertEqual(hashlib.sha256(CANONICAL_PLAN.read_bytes()).hexdigest(), before)
