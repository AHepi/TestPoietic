from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = ROOT / "scripts" / "author_piecemeal_plan.py"
PLAN = ROOT / "evidence" / "frozen" / "piecemeal-plan-v1.json"
SIDECAR = PLAN.with_suffix(".sha256")
OLD_MISSING_SHA256 = "291e5bab4d8629ac00016f434abe60d9ee26061c76bbbf664a34005515d48eb3"


class PiecemealPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.plan_bytes = PLAN.read_bytes()
        cls.plan = json.loads(cls.plan_bytes)
        digest, path = SIDECAR.read_text(encoding="ascii").strip().split(maxsplit=1)
        cls.sidecar_digest = digest
        cls.sidecar_path = path

    def test_author_script_reproduces_frozen_bytes(self) -> None:
        result = subprocess.run(
            [sys.executable, "-B", str(AUTHOR), "--check"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_sidecar_authenticates_repaired_plan(self) -> None:
        self.assertEqual(self.sidecar_path, "evidence/frozen/piecemeal-plan-v1.json")
        self.assertEqual(self.sidecar_digest, hashlib.sha256(self.plan_bytes).hexdigest())
        self.assertEqual(self.plan["freeze"]["kind"], "REPAIRED_REFREEZE")
        prior = self.plan["freeze"]["unrecoverable_prior_sidecar"]
        self.assertEqual(prior["sha256"], OLD_MISSING_SHA256)
        self.assertNotEqual(self.sidecar_digest, OLD_MISSING_SHA256)

    def test_required_lattices_remain_distinct(self) -> None:
        self.assertEqual(self.plan["schema"], "TESTPOIETIC_PIECEMEAL_PLAN_V1")
        lattices = self.plan["lattices"]
        required = {
            "constructor_information",
            "knowledge_retention",
            "no_design_replication",
            "evolutionary_selection",
            "critical_evidence",
            "explanatory_creativity",
        }
        self.assertTrue(required.issubset(lattices))
        for name in required:
            self.assertTrue(lattices[name]["pass_requirements"], name)

        self.assertIn("knowledge_retention", lattices["constructor_information"]["does_not_entail"])
        self.assertIn("explanatory_creativity", lattices["knowledge_retention"]["does_not_entail"])
        self.assertIn("high_fidelity_reproduction", lattices["evolutionary_selection"]["does_not_entail"])
        self.assertIn("epistemic_criticism", lattices["evolutionary_selection"]["does_not_entail"])
        self.assertIn("explanatory_creativity", lattices["critical_evidence"]["does_not_entail"])

        information = {row["id"]: row["requirement"] for row in lattices["constructor_information"]["pass_requirements"]}
        knowledge = {row["id"]: row["requirement"] for row in lattices["knowledge_retention"]["pass_requirements"]}
        reproduction = {row["id"]: row["requirement"] for row in lattices["no_design_replication"]["pass_requirements"]}
        evidence = {row["id"]: row["requirement"] for row in lattices["critical_evidence"]["pass_requirements"]}
        creativity = {row["id"]: row["requirement"] for row in lattices["explanatory_creativity"]["pass_requirements"]}

        self.assertIn("disjoint possible physical attributes", information["I_VARIABLE"])
        self.assertIn("fixed receptive target attribute x0", information["I_CLONING"])
        self.assertIn("bare physical possibility", knowledge["K_REALIZATION_SCOPE"])
        self.assertIn("physical embodiment", knowledge["K_PHYSICAL_INSTANTIATION"])
        self.assertIn("changing or removing P", knowledge["K_RECIPE_CAUSAL_ROLE"])
        self.assertIn("higher-level explanatory claim", knowledge["X_EXPLANATORY_LEVEL"])
        self.assertIn("specified physical form", knowledge["R_COUNTERFACTUAL_CAUSAL_ROLE"])
        self.assertIn("do not assume arbitrary substrate swapping", knowledge["K_REALIZATION_EQUIVALENCE"])
        self.assertIn("all possible environments", knowledge["R_FINITE_EVIDENCE_BOUND"])
        self.assertIn("product, information bearer, construction recipe, or proposed explanation", knowledge["A_ARTIFACT_ROLE"])
        self.assertIn("discrete or digital", reproduction["H_DIGITAL_RECIPE"])
        self.assertIn("causal error-detection and correction", reproduction["H_ERROR_CORRECTION"])
        self.assertIn("blind copying", reproduction["H_ERROR_CORRECTION"])
        self.assertIn("theory-laden observation, logical deduction, or predicted consequence", evidence["C_CHANNEL"])
        self.assertIn("instrument, software, data-reduction, and observer", evidence["C_CHAIN"])
        self.assertIn("critical_evidence package", creativity["E_EVIDENCE_LINK"])
        self.assertIn("revisable guesses", creativity["E_FALLIBILITY"])
        self.assertNotIn("TRACE_CONFIRMED", lattices["explanatory_creativity"]["verdicts"])
        self.assertNotIn("CREATIVITY_PROVEN", lattices["explanatory_creativity"]["verdicts"])

    def test_knowledge_roles_and_integration_are_explicit(self) -> None:
        roles = {row["id"]: row for row in self.plan["knowledge_roles"]["roles"]}
        self.assertEqual(self.plan["knowledge_roles"]["status"], "TYPED_SCOPE_REGISTER")
        self.assertEqual(
            set(roles),
            {
                "K_CONSTRUCTION_RECIPE",
                "K_CREATOR_LOCATION",
                "K_PHYSICAL_COUNTERFACTUAL_ROLE",
                "K_ARTIFACT_CLASSIFICATION",
                "K_EXPLANATORY_PROPOSAL",
            },
        )
        self.assertEqual(roles["K_CONSTRUCTION_RECIPE"]["directness"], "DIRECT_CONDITIONAL_CT")
        self.assertIn("not fixed by constructor theory alone", roles["K_CREATOR_LOCATION"]["definition"])
        self.assertEqual(roles["K_PHYSICAL_COUNTERFACTUAL_ROLE"]["directness"], "DIRECT_FABRIC_SCOPE")
        self.assertIn("without a second substance", roles["K_PHYSICAL_COUNTERFACTUAL_ROLE"]["definition"])
        self.assertIn("must be tested separately", roles["K_ARTIFACT_CLASSIFICATION"]["definition"])
        self.assertIn("does not settle it", roles["K_EXPLANATORY_PROPOSAL"]["definition"])

        integration = self.plan["integration_contract"]
        self.assertEqual(integration["status"], "POIETIC_BRIDGE_CONJECTURE")
        links = {(row["from"], row["to"]): row["rule"] for row in integration["typed_links"]}
        self.assertIn(("constructor_information", "knowledge_retention"), links)
        self.assertIn(("critical_evidence", "explanatory_creativity"), links)
        self.assertIn("not represented criticism", links[("evolutionary_selection", "explanatory_creativity")])
        self.assertIn("counterfactual causal structure", integration["claim"])
        self.assertIn("without adding a second ontology", integration["claim"])

    def test_negative_controls_block_false_greens(self) -> None:
        controls = {row["id"]: row["expected"] for row in self.plan["negative_controls"]}
        lattices = self.plan["lattices"]
        for control_id, expected in controls.items():
            for lattice_name, outcome in expected.items():
                self.assertIn(
                    outcome, lattices[lattice_name]["verdicts"], f"{control_id}:{lattice_name}"
                )
        self.assertEqual(
            controls["NC_NAKED_REPLICATOR"],
            {
                "evolutionary_selection": "MAY_PASS",
                "no_design_replication": "NOT_APPLICABLE",
                "explanatory_creativity": "NOT_ESTABLISHED",
            },
        )
        self.assertEqual(
            controls["NC_CREATOR_WITHOUT_SELF_REPRODUCTION"]["no_design_replication"],
            "NOT_APPLICABLE",
        )
        self.assertEqual(
            controls["NC_BARE_POSSIBILITY_WITHOUT_PRIOR_KNOWLEDGE"]["knowledge_retention"],
            "NOT_APPLICABLE",
        )
        self.assertEqual(
            controls["NC_EXTERNAL_RECIPE_WITHOUT_CANDIDATE_ATTRIBUTION"]["knowledge_retention"],
            "EXTERNAL_P_NOT_ATTRIBUTED",
        )
        self.assertEqual(
            controls["NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE"]["critical_evidence"],
            "NOT_ESTABLISHED",
        )
        self.assertEqual(
            controls["NC_AGREEING_RESULT_NOT_CONFIRMATION"]["critical_evidence"],
            "SURVIVED_DECLARED_ATTEMPT",
        )
        agreeing_fixture = next(
            row["fixture"] for row in self.plan["negative_controls"] if row["id"] == "NC_AGREEING_RESULT_NOT_CONFIRMATION"
        )
        self.assertIn("complete critical_evidence package", agreeing_fixture)
        self.assertEqual(
            controls["NC_UNREFUTABLE_OUTPUT"]["explanatory_creativity"],
            "NOT_ESTABLISHED",
        )
        self.assertEqual(
            controls["NC_UNCONSTRAINED_SUBSTRATE_SWAP"]["knowledge_retention"],
            "NOT_ESTABLISHED",
        )
        self.assertEqual(
            controls["NC_ONE_COPY_INSPECTION"]["evolutionary_selection"],
            "NOT_ESTABLISHED",
        )
        self.assertEqual(
            controls["NC_NONPHYSICAL_RECIPE"]["knowledge_retention"],
            "NOT_ESTABLISHED",
        )

        non_entailments = {row["id"]: row["rule"] for row in self.plan["non_entailments"]}
        self.assertTrue(
            {
                "NE_INFORMATION_NOT_CREATIVITY",
                "NE_SELECTION_NOT_HIGH_FIDELITY",
                "NE_WHOLE_CREATOR_NOT_CLONABLE",
                "NE_BOUNDARY_IS_EVIDENCE",
                "NE_FINITE_ENUMERATION_NOT_ALL_THEORIES",
                "NE_P1_TT_EE_P2_NOT_GENERATOR",
                "NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE",
                "NE_RECIPE_NOT_CREATIVITY",
                "NE_ARTIFACT_NOT_RECIPE",
                "NE_BARE_RECORD_NOT_EVIDENCE",
                "NE_EVIDENCE_NOT_CONFIRMATION",
                "NE_VARIATION_NOT_CONJECTURE_IDENTITY",
                "NE_NONREFUTABLE_NOT_CREATIVE",
                "NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE",
                "NE_SUBSTRATE_SWAP_NOT_AUTOMATIC",
                "NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE",
                "NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS",
            }.issubset(non_entailments)
        )
        self.assertIn("declared high-fidelity recipe variable", non_entailments["NE_WHOLE_CREATOR_NOT_CLONABLE"])
        self.assertIn("does not entail temporally prior knowledge", non_entailments["NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE"])
        self.assertIn("does not confirm", non_entailments["NE_EVIDENCE_NOT_CONFIRMATION"])
        self.assertIn("does not entail a second substance", non_entailments["NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE"])

    def test_authority_scopes_are_explicit(self) -> None:
        sources = {row["id"]: row for row in self.plan["source_register"]}
        self.assertEqual(
            set(sources),
            {
                "CTI",
                "CT_FOUNDATION",
                "FOR_EMERGENCE",
                "FOR_REPLICATOR_NICHE",
                "FOR_GENE_STRUCTURE",
                "CTL",
                "POPPER",
                "DEUTSCH",
            },
        )
        self.assertIn("neither defines creativity", sources["CTI"]["scope_limit"])
        self.assertIn("temporal ordering to subsidiary theories", sources["CT_FOUNDATION"]["direct_imports"][0])
        self.assertIn("right knowledge applied", sources["CT_FOUNDATION"]["direct_imports"][2])
        self.assertIn("declared high-accuracy recipe variable", sources["CTL"]["scope_limit"])
        self.assertIn("higher-level explanations", sources["FOR_EMERGENCE"]["direct_imports"][0])
        self.assertIn("counterfactual causal roles", sources["FOR_REPLICATOR_NICHE"]["direct_imports"][0])
        self.assertIn("one-copy local inspection", sources["FOR_GENE_STRUCTURE"]["direct_imports"][0])
        lattices = self.plan["lattices"]
        self.assertTrue(any("observations are selective" in claim for claim in sources["POPPER"]["direct_imports"]))
        self.assertTrue(any("whole declared system" in claim for claim in sources["POPPER"]["direct_imports"]))
        self.assertIn("chapters 3 and 7", sources["POPPER"]["citation"])
        self.assertIn("critical-evidence package", sources["POPPER"]["poietic_operationalization"])
        self.assertIn("Poietic operational attribution test", lattices["explanatory_creativity"]["source_scope"])
        self.assertEqual(self.plan["bridge_conjecture"]["status"], "CONJECTURE")
        self.assertIn("conjecture and criticism", sources["DEUTSCH"]["direct_imports"][0])
        self.assertNotIn("typed selectionist form", sources["DEUTSCH"]["direct_imports"])
        self.assertNotIn("output alone does not settle where knowledge originated", sources["DEUTSCH"]["direct_imports"])
        self.assertIn("candidate process", sources["DEUTSCH"]["poietic_operationalization"])
        self.assertIn("instrument", sources["DEUTSCH"]["poietic_operationalization"])
        direct_anchors = sources["DEUTSCH"]["direct_import_anchors"]
        self.assertEqual({row["claim_index"] for row in direct_anchors}, {0, 1, 2, 3})
        anchors_by_claim = {row["claim_index"]: row["anchor"] for row in direct_anchors}
        self.assertIn("chapter 4", anchors_by_claim[0])
        self.assertIn("chapter 4", anchors_by_claim[1])
        self.assertIn("chapters 1-2", anchors_by_claim[2])
        self.assertIn("chapter 7", anchors_by_claim[3])
        self.assertIn("do not rule out", sources["DEUTSCH"]["direct_imports"][3])
        self.assertFalse(
            any(
                term in claim.lower()
                for claim in sources["DEUTSCH"]["direct_imports"]
                for term in ("prompt", "training", "tool", "score")
            )
        )
        self.assertIn("Poietic/Popper guard", sources["DEUTSCH"]["poietic_scope_guard"])


if __name__ == "__main__":
    unittest.main()
