#!/usr/bin/env python3
"""Author the deterministic piecemeal-001 semantic re-freeze."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN_RELATIVE = "evidence/frozen/piecemeal-plan-v1.json"
PLAN_PATH = ROOT / PLAN_RELATIVE
SIDECAR_PATH = PLAN_PATH.with_suffix(".sha256")
MISSING_PLAN_SHA256 = "291e5bab4d8629ac00016f434abe60d9ee26061c76bbbf664a34005515d48eb3"
SUBJECT_SHA256 = "9c5d389afc1f334733604083710f6625638b8933825a6312c7403e7de08dafbc"


def canonical_json(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def criteria(*items: tuple[str, str]) -> list[dict[str, str]]:
    return [{"id": identifier, "requirement": requirement} for identifier, requirement in items]


def lattice(
    role: str,
    source_ids: list[str],
    requirements: list[dict[str, str]],
    non_entailments: list[str],
    **extra: object,
) -> dict[str, object]:
    result: dict[str, object] = {
        "role": role,
        "source_ids": source_ids,
        "pass_requirements": requirements,
        "does_not_entail": non_entailments,
    }
    result.update(extra)
    return result


def build_plan() -> dict[str, object]:
    return {
        "schema": "TESTPOIETIC_PIECEMEAL_PLAN_V1",
        "campaign_id": "piecemeal-001",
        "freeze": {
            "kind": "REPAIRED_REFREEZE",
            "subject_sha256": SUBJECT_SHA256,
            "reason": "The prior sidecar's JSON preimage is absent from all recovered repository history and chat writes.",
            "unrecoverable_prior_sidecar": {
                "path": PLAN_RELATIVE,
                "sha256": MISSING_PLAN_SHA256,
            },
        },
        "purpose": {
            "questions": [
                "What is creativity?",
                "What physical systems can instantiate creativity?",
                "What distinguishes creative from non-creative systems?",
                "How can an attribution be tested and refuted?",
            ],
            "rule": "A creative-attribution test must trace a fallible, criticisable process: physical information and knowledge retention constrain a realizer, while theory-mediated error elimination tests an explanatory claim without treating agreement as confirmation.",
        },
        "source_register": [
            {
                "id": "CTI",
                "type": "primary_peer_reviewed",
                "citation": "Deutsch and Marletto, Constructor theory of information, Proc. R. Soc. A 471 (2015) 20140540.",
                "url": "https://doi.org/10.1098/rspa.2014.0540",
                "anchors": ["sections 2-4", "section 6"],
                "direct_imports": [
                    "tasks are possible-or-impossible counterfactual specifications",
                    "a computation variable permits all permutations",
                    "an information variable is a clonable computation variable",
                    "interoperability is a proposed physical principle",
                ],
                "scope_limit": "It neither defines creativity nor requires an entire agent or every state to be clonable.",
            },
            {
                "id": "CT_FOUNDATION",
                "type": "primary_preprint",
                "citation": "Deutsch, Constructor Theory (2012), sections 2.15 and 3.1-3.2.",
                "url": "https://arxiv.org/abs/1210.7439",
                "anchors": ["time delegated to subsidiary theories", "knowledge as an abstract constructor", "right knowledge applied to a possible task"],
                "direct_imports": [
                    "constructor theory leaves temporal ordering to subsidiary theories",
                    "knowledge is information which, when physically instantiated in a suitable environment, tends to cause itself to remain instantiated",
                    "the right knowledge applied can effect any possible task",
                ],
                "scope_limit": "It does not establish temporal priority for arbitrary agents or identify an external builder's recipe with the candidate's knowledge.",
            },
            {
                "id": "FOR_EMERGENCE",
                "type": "primary_book",
                "citation": "Deutsch, The Fabric of Reality (1997/1998), chapter 1, pages 27-28.",
                "anchors": ["emergence and explanatory autonomy"],
                "direct_imports": [
                    "higher-level explanations may be explanatorily autonomous while remaining compatible with physical realization",
                ],
                "scope_limit": "It does not infer a second substance, causal exemption from physics, or unconstrained multiple realizability.",
            },
            {
                "id": "FOR_REPLICATOR_NICHE",
                "type": "primary_book",
                "citation": "Deutsch, The Fabric of Reality (1997/1998), chapter 8, pages 172-176 and glossary page 192.",
                "anchors": ["replicator form, niche, and counterfactual environmental role"],
                "direct_imports": [
                    "replication and adaptation are contextual counterfactual causal roles across bearer and environmental variants",
                ],
                "scope_limit": "It is not a creativity criterion or a generic substrate-neutrality claim: the bearer's specific physical form can be causally relevant.",
            },
            {
                "id": "FOR_GENE_STRUCTURE",
                "type": "primary_book",
                "citation": "Deutsch, The Fabric of Reality (1997/1998), chapter 8, pages 187-190.",
                "anchors": ["gene versus junk-DNA explanatory role across nearby variants"],
                "direct_imports": [
                    "one-copy local inspection cannot by itself determine a gene's knowledge or replicator role",
                ],
                "scope_limit": "Deutsch's Everettian explanatory account does not make other universes observable data or license a finite cohort to establish all possible environments.",
            },
            {
                "id": "CTL",
                "type": "primary_peer_reviewed",
                "citation": "Marletto, Constructor theory of life, J. R. Soc. Interface 12 (2015) 20141226.",
                "url": "https://doi.org/10.1098/rsif.2014.1226",
                "anchors": ["section 2.1", "sections 3.1-3.3"],
                "direct_imports": [
                    "recipe information can act to remain instantiated",
                    "under no-design laws, high or indefinitely improvable accuracy requires an error-correcting recipe variable with discrete or digital units",
                    "vehicle logic is conditional on accurate self-reproduction under no-design laws",
                    "selection can begin with poor-fidelity naked replicators",
                ],
                "scope_limit": "Its digitality conclusion applies to the declared high-accuracy recipe variable, not every component, whole creator, natural-selection case, or creativity claim.",
            },
            {
                "id": "POPPER",
                "type": "primary_book",
                "citation": "Popper, The Logic of Scientific Discovery (1959), sections 2-3, 18, and 29-30; Conjectures and Refutations (1963), chapter 1; Objective Knowledge (1972/1979), chapters 3 and 7.",
                "anchors": ["deductive criticism and auxiliary conditions", "theory-interpreted observation and predeclared refutation", "P1 -> TT -> EE -> P2, Objective Knowledge chapter 3", "problem- and theory-guided observation, Objective Knowledge chapter 7, pages 258-259"],
                "direct_imports": [
                    "there is no logical method of having new ideas",
                    "a tentative theory is tested through deductions, theory comparison, and empirical applications",
                    "a falsified predicted consequence initially criticizes the whole declared system used to derive it, including target theory and initial conditions",
                    "observations are selective, theory-interpreted, and fallible rather than pure data",
                    "tentative theories face attempted error elimination",
                    "scientific criticism can eliminate theories in place of their holders",
                    "P1 -> TT -> EE -> P2 describes problem solving through tentative theories and error elimination",
                ],
                "poietic_operationalization": "The reusable critical-evidence package, including an instrument/interpretation chain and a predeclared protocol, operationalizes these sources; it is not supplied by them as an automatic creativity test.",
                "scope_limit": "A lone record is not automatic final falsification: criticism requires declared auxiliaries, an interpretation, and a revisable acceptance/refutation protocol.",
            },
            {
                "id": "DEUTSCH",
                "type": "primary_book_and_essay",
                "citation": "Deutsch, The Beginning of Infinity (2011), chapters 1, 2, 4, and 7; Beyond Reward and Punishment (2019).",
                "anchors": ["fallible, theory-laden observation", "instrument-output explanation chains", "human conjecture and criticism versus biological variation and selection", "artificial-creativity provenance"],
                "direct_imports": [
                    "human knowledge is created through conjecture and criticism or experiment, while biological adaptations are created through mutation and natural selection",
                    "their mechanisms and explanatory reach differ",
                    "observations and their interpretations are theory-laden and fallible",
                    "variation and selection during a program run do not rule out an alternative explanation in which relevant knowledge was created by designers",
                ],
                "direct_import_anchors": [
                    {"claim_index": 0, "anchor": "The Beginning of Infinity, chapter 4, Creation, pages 77-79."},
                    {"claim_index": 1, "anchor": "The Beginning of Infinity, chapter 4, Creation, pages 77-79."},
                    {"claim_index": 2, "anchor": "The Beginning of Infinity, chapters 1-2, fallible observations and explanatory instrument chains."},
                    {"claim_index": 3, "anchor": "The Beginning of Infinity, chapter 7, Artificial Creativity, pages 160-162."},
                ],
                "poietic_operationalization": "A critical-evidence package must make its explanatory instrument and interpretation links explicit, and an attribution must distinguish knowledge created in the candidate process from knowledge supplied by designers, prompts, training, tools, scores, or external sources.",
                "poietic_scope_guard": "A fixed reward score or black-box behavior is not a proof of creativity, and an agreeing result is not confirmation; this is a Poietic/Popper guard, not a direct Deutsch import.",
                "scope_limit": "The cited passages make provenance and alternative explanations mandatory; they do not by themselves supply a behavior-only creativity criterion.",
            },
        ],
        "lattices": {
            "constructor_information": lattice(
                "physical substrate constraint",
                ["CTI", "CTL"],
                criteria(
                    ("I_BOUNDARY", "Declare the substrate and boundary that bear the candidate variable."),
                    ("I_VARIABLE", "Specify two or more disjoint possible physical attributes in the candidate variable."),
                    ("I_PERMUTATION", "Identify the possible permutation tasks and permitted side effects."),
                    ("I_CLONING", "Identify one fixed receptive target attribute x0 and a copying task for every claimed value."),
                    ("I_INTEROPERABILITY", "State whether composite-media interoperability is used, tested, or unasserted."),
                ),
                ["knowledge_retention", "high_fidelity_reproduction", "evolutionary_selection", "critical_evidence", "explanatory_creativity"],
                verdicts=["MAY_PASS", "NOT_APPLICABLE", "NOT_ESTABLISHED"],
                failure_guard="A stored bit pattern, program label, or observed message alone is not an established information medium.",
            ),
            "knowledge_retention": lattice(
                "knowledge realization, causal bearer, counterfactual role, and persistence constraint",
                ["CTI", "CT_FOUNDATION", "CTL", "FOR_EMERGENCE", "FOR_REPLICATOR_NICHE", "FOR_GENE_STRUCTURE"],
                criteria(
                    ("R_BOUNDARY", "Declare the physical bearer, environment class, and boundary supporting continuation."),
                    ("R_VALUE", "Identify the particular physically instantiated information value, not merely a storage device or abstract label."),
                    ("K_PHYSICAL_INSTANTIATION", "Identify the physical embodiment of P or another claimed knowledge value; do not posit a free-floating abstract recipe."),
                    ("K_REALIZATION_SCOPE", "Apply a prior-knowledge verdict only to an actual construction, maintenance, or H-scope claim; bare physical possibility receives no prior-knowledge verdict."),
                    ("K_RECIPE_CAUSAL_ROLE", "Identify task-specific recipe P, its physical bearer, V or resources, and an intervention showing that changing or removing P changes or defeats the claimed construction task."),
                    ("X_EXPLANATORY_LEVEL", "State the higher-level explanatory claim and its compatible physical realization; do not infer a second ontology or causal exemption."),
                    ("R_COUNTERFACTUAL_CAUSAL_ROLE", "Declare bearer, value, environment class, and close variants; test whether the specified physical form changes copying or retention outcomes across the declared counterfactuals."),
                    ("K_REALIZATION_EQUIVALENCE", "If claiming multiple realization, show that a substituted bearer preserves the declared task, relevant side effects, and environment class; do not assume arbitrary substrate swapping."),
                    ("R_MAINTENANCE", "Give a causal maintenance, re-instantiation, or reconstruction route."),
                    ("K_HISTORY", "For an actual construction claim, record whether P was instantiated in the candidate, a parent, an external builder, or an evolutionary population; do not infer temporal priority from constructor theory alone."),
                    ("R_VALUE_INTERVENTION", "State a value-change or removal comparison that could defeat attribution."),
                    ("R_FINITE_EVIDENCE_BOUND", "State the finite cohort and model domain used as evidence; do not promote it to all possible environments, variants, or an Everettian claim."),
                    ("A_ARTIFACT_ROLE", "Classify an output separately as product, information bearer, construction recipe, or proposed explanation; no classification entails the next."),
                ),
                ["explanatory_creativity", "truth", "good_explanation", "high_fidelity_reproduction", "prior_knowledge_temporal_axiom", "artifact_embodies_recipe", "extra_substance", "unconstrained_substrate_swap", "finite_variant_exhaustiveness"],
                source_scope="Direct CT imports construction knowledge as causal information P that can remain instantiated under stated conditions. Deutsch's higher-level and replicator explanations remain physically compatible and contextually counterfactual; content-sensitive retention, creator attribution, and explanatory knowledge are Poietic refinements.",
                verdicts=["MAY_PASS", "NOT_APPLICABLE", "EXTERNAL_P_NOT_ATTRIBUTED", "NOT_ESTABLISHED"],
                failure_guard="Persistence, copied syntax, an externally maintained record, a produced artifact, a one-copy inspection, or an unconstrained substrate-swap claim alone is insufficient to attribute P or explanatory knowledge to the candidate.",
            ),
            "no_design_replication": lattice(
                "conditional high-fidelity reproduction test",
                ["CTL"],
                criteria(
                    ("H_BOUNDARY", "Separate replicator, vehicle, and external resources at a declared boundary."),
                    ("H_NO_DESIGN", "State no-design-law and generic-resource assumptions."),
                    ("H_ACCURACY", "State the high or indefinitely improvable accuracy claim and error measure."),
                    ("H_RECIPE", "Identify the modular recipe P or program and its causal role in construction."),
                    ("H_DIGITAL_RECIPE", "If H is applicable, identify P and its unit variable Sigma; show that its attributes are discrete or digital in the constructor-theory sense, separated by non-allowed attributes."),
                    ("H_ERROR_CORRECTION", "Identify the causal error-detection and correction task for replication of P, its task- or value-dependent criterion, and blind copying of modular units where replication is claimed."),
                    ("H_VEHICLE", "Identify vehicle construction and reproduction where the accuracy claim requires it."),
                ),
                ["explanatory_creativity", "whole_creator_clonability", "isolated_component_self_reproduction"],
                applicability="Apply only to a claim of accurate or indefinitely improvable self-reproduction or replication under no-design laws.",
                not_applicable_rule="A non-self-reproducing candidate receives NOT_APPLICABLE, never NON_CREATIVE.",
                verdicts=["MAY_PASS", "NOT_APPLICABLE", "NOT_ESTABLISHED"],
                failure_guard="Absent the declared digital recipe and causal error-correction conditions, record H as NOT_ESTABLISHED rather than inferring NON_CREATIVE.",
            ),
            "evolutionary_selection": lattice(
                "population variation and selection test",
                ["CTL", "POPPER", "DEUTSCH"],
                criteria(
                    ("V_POPULATION", "Specify population, variants, and lineage boundary."),
                    ("V_INHERITANCE", "Specify inherited continuation and viable-offspring criterion."),
                    ("V_VARIATION", "Show variation is non-specific to the alleged end product and is not guaranteed in advance to meet the declared viable-offspring criterion."),
                    ("V_SELECTION", "Specify finite-resource environmental selection and differential continuation."),
                    ("V_FALLIBILITY", "Record selection as environment-relative error elimination, not represented explanation or confirmation."),
                ),
                ["high_fidelity_reproduction", "vehicle_architecture", "epistemic_criticism", "critical_evidence", "explanatory_creativity"],
                verdicts=["MAY_PASS", "NOT_ESTABLISHED"],
                failure_guard="A score, a single success, or an environmental survivor does not establish an explanation, theory-laden evidence, or knowledge creation.",
            ),
            "critical_evidence": lattice(
                "theory-mediated error-elimination interface",
                ["POPPER", "DEUTSCH"],
                criteria(
                    ("C_TARGET", "Identify the target claim, problem, and a rival or possible incompatibility."),
                    ("C_CHANNEL", "Classify the criticising content as a theory-laden observation, logical deduction, or predicted consequence; do not recast any channel as theory-free evidence."),
                    ("C_CHAIN", "Declare the instrument, software, data-reduction, and observer interpretation chain; include eyes, calibration, and perceptual or inferential links where relevant."),
                    ("C_AUXILIARIES", "State the background, initial-condition, and auxiliary explanations that connect the channel to the target claim."),
                    ("C_DISCRIMINATOR", "Derive a consequence, rival discriminator, or incompatibility that could expose error in the declared conjunction."),
                    ("C_PROTOCOL", "Predeclare the acceptance, reproducibility, and refutation protocol, including how instrument, observation, or inference error will be criticised."),
                    ("C_OUTCOME", "Record an attempted refutation, revision trigger, disputed interpretation, or inconclusive result; agreement is not confirmation."),
                ),
                ["confirmation", "truth", "automatic_target_falsification", "explanatory_creativity"],
                verdicts=["REFUTED_CONJUNCTION", "SURVIVED_DECLARED_ATTEMPT", "INTERPRETATION_DISPUTED", "INCONCLUSIVE", "NOT_ESTABLISHED"],
                source_scope="This is a Poietic operational package for Popperian and Deutschian criticism; neither source licenses a theory-free data tier or automatic attribution to one component of a failed conjunction.",
                failure_guard="A bare sensor value, reward, benchmark score, deduction, trace, or output is not evidence for this test without its explanatory chain and declared criticisable target.",
            ),
            "explanatory_creativity": lattice(
                "epistemic attribution test",
                ["POPPER", "DEUTSCH"],
                criteria(
                    ("E_P1", "Identify a problem, not only an externally supplied target or reward."),
                    ("E_TT", "Identify tentative, fallible explanatory proposals, provenance, and explanatory content."),
                    ("E_EE", "Identify criticism, possible refuters, or consequence tests that can revise proposals."),
                    ("E_EVIDENCE_LINK", "For each tentative theory, invoke a critical_evidence package linking a theory-laden observation, deduction, or predicted consequence to declared auxiliaries, a possible refuter, and a revision route."),
                    ("E_P2", "Identify the revised problem without treating finite enumeration as all theories."),
                    ("E_PROVENANCE", "Account for prompts, seeds, scores, oracles, tools, training, and human interventions."),
                    ("E_FALLIBILITY", "Show that proposals are revisable guesses with a declared error domain; an uncriticisable or error-free output cannot establish creativity."),
                ),
                ["physical_information_alone", "construction_knowledge_alone", "retention_alone", "selection_alone", "critical_evidence_alone", "behavioral_success_alone"],
                verdicts=["CRITICISABLE_TRACE_AUDITED", "PROVENANCE_UNRESOLVED", "NOT_ESTABLISHED", "REFUTED_ON_DECLARED_DOMAIN", "UNRESOLVED_NOT_NON_CREATIVE"],
                integration_requirement="Creation of explanatory knowledge is tested independently of construction knowledge P: a proposed explanation must be conjectured, criticised, revised, and provenance-accounted within the candidate process.",
                source_scope="This is a Poietic operational attribution test built from Popperian criticism and Deutschian provenance; neither source says every creator is a human scientist, that every selection process is criticism, or that a successful output establishes creativity.",
                failure_guard="No verdict may say CREATIVITY_PROVEN; a trace or agreeing result is insufficient when external knowledge, the instrument chain, or declared auxiliaries can account for it.",
            ),
        },
        "knowledge_roles": {
            "status": "TYPED_SCOPE_REGISTER",
            "roles": [
                {
                    "id": "K_CONSTRUCTION_RECIPE",
                    "directness": "DIRECT_CONDITIONAL_CT",
                    "definition": "A task-specific, physically instantiated recipe P is causal construction knowledge when it acts with V or resources to control a declared task and can cause its own continued instantiation under the stated conditions.",
                    "test_interfaces": ["K_REALIZATION_SCOPE", "K_RECIPE_CAUSAL_ROLE", "R_MAINTENANCE"],
                },
                {
                    "id": "K_CREATOR_LOCATION",
                    "directness": "BOUNDARY_AND_HISTORY_REQUIREMENT",
                    "definition": "Record whether P is in the candidate, a parent, an external builder, or an evolutionary population; its location and temporal order are not fixed by constructor theory alone.",
                    "test_interfaces": ["R_BOUNDARY", "K_HISTORY"],
                },
                {
                    "id": "K_PHYSICAL_COUNTERFACTUAL_ROLE",
                    "directness": "DIRECT_FABRIC_SCOPE",
                    "definition": "A higher-level causal role is physically instantiated and explanation-relevant through declared counterfactuals, without a second substance; the bearer's specific form and environment class remain part of the claim.",
                    "test_interfaces": ["K_PHYSICAL_INSTANTIATION", "X_EXPLANATORY_LEVEL", "R_COUNTERFACTUAL_CAUSAL_ROLE", "K_REALIZATION_EQUIVALENCE", "R_FINITE_EVIDENCE_BOUND"],
                },
                {
                    "id": "K_ARTIFACT_CLASSIFICATION",
                    "directness": "POIETIC_GUARD",
                    "definition": "A produced artifact may be a product, information bearer, construction recipe, or proposed explanation. These roles must be tested separately.",
                    "test_interfaces": ["A_ARTIFACT_ROLE", "E_PROVENANCE"],
                },
                {
                    "id": "K_EXPLANATORY_PROPOSAL",
                    "directness": "POIETIC_EPISTEMIC_TEST",
                    "definition": "A proposed explanation counts only through conjecture, theory-mediated criticism, revision, and provenance attribution; construction knowledge P alone does not settle it.",
                    "test_interfaces": ["E_TT", "E_EVIDENCE_LINK", "E_FALLIBILITY", "E_PROVENANCE"],
                },
            ],
        },
        "integration_contract": {
            "status": "POIETIC_BRIDGE_CONJECTURE",
            "claim": "A creativity attribution integrates physical instantiation of counterfactual causal structure, causal knowledge, fallible variant generation, and theory-mediated error elimination, without adding a second ontology or collapsing their different physical and epistemic roles.",
            "typed_links": [
                {"from": "constructor_information", "to": "knowledge_retention", "rule": "A declared physical variable can bear a causal knowledge value when its physical embodiment and relevant counterfactual task role are specified; information-medium capability alone is not knowledge."},
                {"from": "knowledge_retention", "to": "explanatory_creativity", "rule": "Construction knowledge P constrains what can be realized, while explanatory knowledge must independently survive criticism and provenance checks."},
                {"from": "critical_evidence", "to": "explanatory_creativity", "rule": "Observation, deduction, and prediction become criticism only through an explanatory chain, declared auxiliaries, and a revisable refutation protocol."},
                {"from": "evolutionary_selection", "to": "explanatory_creativity", "rule": "Variation and selection supply a typed fallible analogue, not represented criticism or explanatory creativity by themselves."},
            ],
        },
        "bridge_conjecture": {
            "status": "CONJECTURE",
            "claim": "Conjecture and criticism, and variation and selection, are typed, fallible instances of a problem-sensitive variation and error-elimination schema.",
            "role_mapping": [
                {"abstract_role": "variation", "epistemic": "conjectures", "evolutionary": "heritable variants"},
                {"abstract_role": "error_elimination", "epistemic": "criticism, argument, and experiment", "evolutionary": "differential continuation"},
            ],
            "fallibility": "Both modes generate candidates whose success is not guaranteed in advance. Calling a biological variant a guess is a Poietic bridge interpretation, not a claim that it represents a proposition.",
            "non_identity_guards": [
                "Criticism can eliminate proposals without eliminating their holder.",
                "Natural selection need not represent explanations or refuters.",
                "Explanatory reach and population adaptation have different attribution burdens.",
                "Neither a surviving variant nor a non-refuted theory is confirmation.",
            ],
        },
        "negative_controls": [
            {
                "id": "NC_INFORMATION_WITHOUT_RETENTION",
                "fixture": "A copied record with no value-dependent maintenance route.",
                "expected": {"constructor_information": "MAY_PASS", "knowledge_retention": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_RETENTION_WITHOUT_EXPLANATION",
                "fixture": "A self-maintaining hereditary value with no proposed explanation or criticism.",
                "expected": {"knowledge_retention": "MAY_PASS", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_NAKED_REPLICATOR",
                "fixture": "A poor-fidelity vehicle-less replicator in a sufficiently unchanging resource-rich environment.",
                "expected": {"evolutionary_selection": "MAY_PASS", "no_design_replication": "NOT_APPLICABLE", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_SELECTION_WITHOUT_CRITICISM",
                "fixture": "Population selection with no represented problems, rivals, or possible refuters.",
                "expected": {"evolutionary_selection": "MAY_PASS", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_CREATOR_WITHOUT_SELF_REPRODUCTION",
                "fixture": "A candidate creator not claiming to reproduce itself.",
                "expected": {"no_design_replication": "NOT_APPLICABLE", "explanatory_creativity": "UNRESOLVED_NOT_NON_CREATIVE"},
            },
            {
                "id": "NC_BARE_POSSIBILITY_WITHOUT_PRIOR_KNOWLEDGE",
                "fixture": "A bare physical-possibility claim with no actual construction, maintenance, or H-scope claim.",
                "expected": {"knowledge_retention": "NOT_APPLICABLE", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_EXTERNAL_RECIPE_WITHOUT_CANDIDATE_ATTRIBUTION",
                "fixture": "A task-specific recipe P is physically instantiated only in an external builder, while the candidate merely receives the product.",
                "expected": {"knowledge_retention": "EXTERNAL_P_NOT_ATTRIBUTED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE",
                "fixture": "A benchmark score or sensor number with no instrument interpretation chain, declared auxiliaries, rival, or refutation protocol.",
                "expected": {"critical_evidence": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_AGREEING_RESULT_NOT_CONFIRMATION",
                "fixture": "A complete critical_evidence package declares its channel, instrument/interpretation chain, auxiliaries, discriminator, and protocol; its result agrees with a prediction but is treated as confirming the target explanation.",
                "expected": {"critical_evidence": "SURVIVED_DECLARED_ATTEMPT", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_UNREFUTABLE_OUTPUT",
                "fixture": "A candidate claims an error-free final answer with no possible critic, consequence, or revision route.",
                "expected": {"critical_evidence": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_UNCONSTRAINED_SUBSTRATE_SWAP",
                "fixture": "Two candidates are declared equivalent because a label or syntax is preserved, while the task, side effects, physical form, and environment class are not shown to be preserved.",
                "expected": {"knowledge_retention": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_ONE_COPY_INSPECTION",
                "fixture": "A claim that a single local copy establishes a gene-like knowledge or replicator role without declared variants, environments, copying, or retention outcomes.",
                "expected": {"knowledge_retention": "NOT_ESTABLISHED", "evolutionary_selection": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
            {
                "id": "NC_NONPHYSICAL_RECIPE",
                "fixture": "An abstract recipe is claimed to cause construction without any declared physical bearer, task role, or compatible realization.",
                "expected": {"knowledge_retention": "NOT_ESTABLISHED", "explanatory_creativity": "NOT_ESTABLISHED"},
            },
        ],
        "non_entailments": [
            {"id": "NE_INFORMATION_NOT_KNOWLEDGE", "rule": "An information medium alone does not establish retained knowledge."},
            {"id": "NE_INFORMATION_NOT_CREATIVITY", "rule": "Information tasks alone do not establish explanatory creativity."},
            {"id": "NE_RETENTION_NOT_CREATIVITY", "rule": "Retained knowledge alone does not establish good explanation or creativity."},
            {"id": "NE_SELECTION_NOT_HIGH_FIDELITY", "rule": "Selection does not entail high-fidelity digital heredity, correction, or a vehicle."},
            {"id": "NE_SELECTION_NOT_CRITICISM", "rule": "Selection does not entail represented epistemic criticism."},
            {"id": "NE_WHOLE_CREATOR_NOT_CLONABLE", "rule": "No whole candidate agent, or component outside a declared high-fidelity recipe variable, is generally required to be digital, clonable, or self-reproducing."},
            {"id": "NE_BOUNDARY_IS_EVIDENCE", "rule": "Boundary choice is evidence, not bookkeeping."},
            {"id": "NE_FINITE_ENUMERATION_NOT_ALL_THEORIES", "rule": "A finite domain test cannot be promoted to all possible theories."},
            {"id": "NE_P1_TT_EE_P2_NOT_GENERATOR", "rule": "P1 -> TT -> EE -> P2 is a criticisable cycle, not a generator or sufficient creativity test."},
            {"id": "NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE", "rule": "Bare physical possibility does not entail temporally prior knowledge in the candidate or any fixed boundary."},
            {"id": "NE_RECIPE_NOT_CREATIVITY", "rule": "Construction knowledge P does not by itself establish explanatory creativity."},
            {"id": "NE_ARTIFACT_NOT_RECIPE", "rule": "A produced artifact does not by itself embody the recipe P or explanatory knowledge that produced it."},
            {"id": "NE_BARE_RECORD_NOT_EVIDENCE", "rule": "A bare observation, sensor value, score, trace, deduction, or predicted result is not evidence without an explanatory interpretation chain and criticisable target."},
            {"id": "NE_EVIDENCE_NOT_CONFIRMATION", "rule": "An agreeing theory-laden result may survive a declared attempted refutation but does not confirm the target explanation."},
            {"id": "NE_VARIATION_NOT_CONJECTURE_IDENTITY", "rule": "The typed fallibility bridge does not make a biological variant a represented conjecture or selection a criticism."},
            {"id": "NE_NONREFUTABLE_NOT_CREATIVE", "rule": "An uncriticisable, error-free, or final-output claim does not establish creativity."},
            {"id": "NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE", "rule": "A higher-level explanatory or informational structure is physically compatible and does not entail a second substance or causal exemption."},
            {"id": "NE_SUBSTRATE_SWAP_NOT_AUTOMATIC", "rule": "Preserving a label or syntax does not establish equivalent realization; the declared task, side effects, physical form, and environment class must be preserved."},
            {"id": "NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE", "rule": "One-copy local inspection does not establish a contextual counterfactual knowledge, replication, or adaptation role."},
            {"id": "NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS", "rule": "Finite observed variants provide evidence only for a declared model and domain, not all possible environments or an Everettian explanatory claim."},
        ],
    }


def expected_artifacts() -> tuple[bytes, bytes]:
    plan = canonical_json(build_plan())
    return plan, f"{hashlib.sha256(plan).hexdigest()}  {PLAN_RELATIVE}\n".encode("ascii")


def check_artifacts() -> list[str]:
    plan, sidecar = expected_artifacts()
    failures: list[str] = []
    for path, expected in ((PLAN_PATH, plan), (SIDECAR_PATH, sidecar)):
        if not path.exists():
            failures.append(f"missing: {path.relative_to(ROOT).as_posix()}")
        elif path.read_bytes() != expected:
            failures.append(f"mismatch: {path.relative_to(ROOT).as_posix()}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify frozen bytes without writing")
    args = parser.parse_args()
    if args.check:
        failures = check_artifacts()
        if failures:
            print("\n".join(failures), file=sys.stderr)
            return 1
        return 0
    plan, sidecar = expected_artifacts()
    PLAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_bytes(plan)
    SIDECAR_PATH.write_bytes(sidecar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
