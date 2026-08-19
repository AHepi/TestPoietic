"""Piecemeal combinatorial calculus over the authenticated six-lattice signature.

The frozen piecemeal plan supplies a vocabulary of local obligations, verdict
domains, typed links, non-entailments, and negative controls.  It does not
supply a scalar confidence score or a Boolean creativity predicate.  This
module reconstructs the missing algebra without inventing either:

    J = product_i P(V_i)
    A <= B iff, for every coordinate i, A_i is a subset of B_i.

A smaller coordinate set is a more *refined* judgement, not a more true or
more creative one.  Empty coordinate sets record an inconsistent declaration.
Fully determined states form the 1,800-profile finite combinatorial space
declared by the frozen plan.  This finite space tests the calculus only; it
does not enumerate theories, environments, or possible creators.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any

from .constants import PRIMARY_SHA256
from .piecemeal import (
    CANONICAL_PLAN,
    FROZEN_PLAN_SHA256,
    REQUIRED_EDGES,
    authenticate_frozen_plan,
)

LATTICE_ORDER = (
    "constructor_information",
    "knowledge_retention",
    "no_design_replication",
    "evolutionary_selection",
    "critical_evidence",
    "explanatory_creativity",
)
SCOPE = "PIECEMEAL_COMBINATORIAL_CALCULUS_ONLY"
FORBIDDEN_OUTPUT_TOKENS = frozenset({"CREATIVITY_PROVEN", "CONFIRMED", "PASS"})
PROFILE_OUTCOMES = frozenset(
    {
        "INCONSISTENT_PROFILE",
        "UNDERDETERMINED_PROFILE",
        "REFUTED_ON_DECLARED_DOMAIN",
        "REFUTATION_RECORDED_ON_DECLARED_DOMAIN",
        "PROVENANCE_UNRESOLVED",
        "UNRESOLVED_NOT_NON_CREATIVE",
        "CRITICISABLE_REALIZER_TRACE_AUDITED",
        "CRITICISABLE_TRACE_REALIZER_NOT_ESTABLISHED",
        "SELECTION_ANALOGUE_ONLY",
        "NOT_ESTABLISHED",
    }
)
CRITICAL_PACKAGE_OUTCOMES = frozenset(
    {
        "REFUTED_CONJUNCTION",
        "SURVIVED_DECLARED_ATTEMPT",
        "INTERPRETATION_DISPUTED",
        "INCONCLUSIVE",
    }
)
POSITIVE_VERDICTS = {
    "constructor_information": frozenset({"MAY_PASS"}),
    "knowledge_retention": frozenset({"MAY_PASS"}),
    "no_design_replication": frozenset({"MAY_PASS"}),
    "evolutionary_selection": frozenset({"MAY_PASS"}),
    "critical_evidence": CRITICAL_PACKAGE_OUTCOMES,
    "explanatory_creativity": frozenset({"CRITICISABLE_TRACE_AUDITED"}),
}

# A scoped refutation is an evidential result, not a bare status label.  It
# therefore needs the same complete local gate discipline as an audited trace,
# while remaining distinct from an affirmative/positive verdict.
GATE_REQUIRED_VERDICTS = {
    **POSITIVE_VERDICTS,
    "explanatory_creativity": frozenset(
        {"CRITICISABLE_TRACE_AUDITED", "REFUTED_ON_DECLARED_DOMAIN"}
    ),
}


class CalculusError(ValueError):
    """Raised for malformed calculus signatures, constraints, or profiles."""


@dataclass(frozen=True)
class BridgeRule:
    """A visible Poietic bridge rule, never a hidden source-theorem import."""

    rule_id: str
    status: str
    source_lattices: tuple[str, ...]
    target_lattice: str
    effect: str
    prohibited_reverse_inference: str


BRIDGE_RULES = (
    BridgeRule(
        "B_I_R_BEARER_GATE",
        "POIETIC_OPERATIONAL_BRIDGE",
        ("constructor_information",),
        "knowledge_retention",
        "An information variable can constrain a knowledge bearer only through "
        "a declared boundary link; it does not make a whole candidate clonable "
        "or derive retained knowledge.",
        "knowledge from information-medium capability alone",
    ),
    BridgeRule(
        "B_R_E_REALIZER_CONSTRAINT",
        "POIETIC_BRIDGE_CONJECTURE",
        ("knowledge_retention",),
        "explanatory_creativity",
        "Retained construction knowledge constrains a physical realizer for an "
        "attribution; it does not discharge explanatory creativity.",
        "explanatory creativity from retention or construction knowledge alone",
    ),
    BridgeRule(
        "B_C_E_CRITICISM_LINK",
        "POIETIC_OPERATIONAL_BRIDGE",
        ("critical_evidence",),
        "explanatory_creativity",
        "A complete theory-mediated critical package can discharge an "
        "E_EVIDENCE_LINK only when a proposed explanation supplies its own "
        "target, provenance, and revision route.",
        "explanatory creativity or confirmation from a critical package alone",
    ),
    BridgeRule(
        "B_V_E_TYPED_ANALOGUE",
        "POIETIC_BRIDGE_CONJECTURE",
        ("evolutionary_selection",),
        "explanatory_creativity",
        "Variation and selection instantiate a typed fallibility analogue, not "
        "represented conjecture, criticism, or explanatory creativity.",
        "epistemic criticism or explanatory creativity from selection alone",
    ),
    BridgeRule(
        "B_H_CONDITIONAL_BRANCH",
        "DIRECT_CONDITIONAL_CT_SCOPE",
        ("no_design_replication",),
        "no_design_replication",
        "High-accuracy no-design reproduction is a conditional digital-recipe "
        "branch.  Its non-applicability is not a non-creativity verdict.",
        "whole-agent clonability or non-creativity from H being not applicable",
    ),
)
BRIDGE_RULE_BY_ID = {rule.rule_id: rule for rule in BRIDGE_RULES}

RELATION_NAMES = frozenset(
    {
        "INFORMATION_VARIABLE_CANDIDATE",
        "PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED",
        "CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED",
        "TYPED_VARIATION_SELECTION_ANALOGUE",
        "THEORY_MEDIATED_CRITICISM_PACKAGE",
        "CRITICISABLE_EXPLANATORY_TRACE",
        "CRITICISABLE_REALIZER_TRACE",
    }
)


@dataclass(frozen=True)
class NegativeControl:
    """A partial frozen control profile."""

    control_id: str
    expected: tuple[tuple[str, str], ...]

    def expected_dict(self) -> dict[str, str]:
        return dict(self.expected)


@dataclass(frozen=True)
class CalculusSignature:
    """Immutable projection of the authenticated frozen semantic signature."""

    plan_schema: str
    plan_sha256: str
    lattice_order: tuple[str, ...]
    requirement_ids: tuple[tuple[str, tuple[str, ...]], ...]
    verdict_domains: tuple[tuple[str, tuple[str, ...]], ...]
    typed_links: tuple[tuple[str, str, str], ...]
    non_entailment_ids: tuple[str, ...]
    negative_controls: tuple[NegativeControl, ...]

    @property
    def requirement_count(self) -> int:
        return sum(len(ids) for _, ids in self.requirement_ids)

    @property
    def profile_count(self) -> int:
        result = 1
        for _, domain in self.verdict_domains:
            result *= len(domain)
        return result

    def requirements_for(self, lattice: str) -> tuple[str, ...]:
        for name, requirements in self.requirement_ids:
            if name == lattice:
                return requirements
        raise CalculusError(f"unknown lattice: {lattice}")

    def verdicts_for(self, lattice: str) -> tuple[str, ...]:
        for name, verdicts in self.verdict_domains:
            if name == lattice:
                return verdicts
        raise CalculusError(f"unknown lattice: {lattice}")


@dataclass(frozen=True)
class LocalGate:
    """A lattice-local necessary-condition vector over frozen requirement IDs.

    Complete satisfaction makes that lattice's positive verdict(s) available;
    it does not assert that any such verdict is true. Missing any frozen
    requirement removes only the positive verdict(s), preserving the other
    scope-qualified possibilities.
    """

    lattice: str
    required_requirement_ids: frozenset[str]
    satisfied_requirement_ids: frozenset[str]

    @property
    def missing_requirement_ids(self) -> frozenset[str]:
        return self.required_requirement_ids - self.satisfied_requirement_ids

    @property
    def is_complete(self) -> bool:
        return not self.missing_requirement_ids


@dataclass(frozen=True)
class TypedLinkWitness:
    """A declared identity-preserving bridge between two lattice packets.

    The witness does not dereference raw evidence. It records the boundary,
    bearer, target claim, and (where needed) revision route that must be
    checked by a later candidate-evidence audit before a typed bridge is used.
    """

    rule_id: str
    source_lattice: str
    target_lattice: str
    scope_id: str
    source_id: str
    target_id: str
    knowledge_bearer_id: str | None = None
    target_claim_id: str | None = None
    critical_outcome: str | None = None
    revision_route_id: str | None = None


@dataclass(frozen=True)
class CalculusContext:
    """Local-gate and identity-link certificates for a composition attempt."""

    local_gates: tuple[LocalGate, ...] = ()
    link_witnesses: tuple[TypedLinkWitness, ...] = ()


@dataclass(frozen=True)
class VerdictProfile:
    """One fully determined point in the declared six-coordinate product."""

    constructor_information: str
    knowledge_retention: str
    no_design_replication: str
    evolutionary_selection: str
    critical_evidence: str
    explanatory_creativity: str

    @classmethod
    def from_mapping(
        cls,
        values: Mapping[str, str],
        signature: CalculusSignature,
    ) -> "VerdictProfile":
        if set(values) != set(signature.lattice_order):
            raise CalculusError("profile must specify all and only the six lattice names")
        profile = cls(*(values[name] for name in signature.lattice_order))
        validate_profile(profile, signature)
        return profile

    def as_dict(self) -> dict[str, str]:
        return {
            "constructor_information": self.constructor_information,
            "knowledge_retention": self.knowledge_retention,
            "no_design_replication": self.no_design_replication,
            "evolutionary_selection": self.evolutionary_selection,
            "critical_evidence": self.critical_evidence,
            "explanatory_creativity": self.explanatory_creativity,
        }


@dataclass(frozen=True)
class JudgmentState:
    """A partially refined product-lattice judgement."""

    possibilities: tuple[frozenset[str], ...]

    @classmethod
    def initial(cls, signature: CalculusSignature) -> "JudgmentState":
        return cls(
            tuple(frozenset(signature.verdicts_for(name)) for name in signature.lattice_order)
        )

    def as_dict(self, signature: CalculusSignature) -> dict[str, frozenset[str]]:
        _validate_state_shape(self, signature)
        return dict(zip(signature.lattice_order, self.possibilities, strict=True))

    def permitted(self, signature: CalculusSignature, lattice: str) -> frozenset[str]:
        return self.as_dict(signature)[lattice]

    def constrain(
        self,
        signature: CalculusSignature,
        lattice: str,
        allowed: Iterable[str],
    ) -> "JudgmentState":
        _validate_state_shape(self, signature)
        if lattice not in signature.lattice_order:
            raise CalculusError(f"unknown lattice: {lattice}")
        if isinstance(allowed, str):
            allowed_values = frozenset({allowed})
        else:
            allowed_values = frozenset(allowed)
        unknown = allowed_values - frozenset(signature.verdicts_for(lattice))
        if unknown:
            raise CalculusError(
                f"unknown verdict(s) for {lattice}: {sorted(unknown)!r}"
            )
        index = signature.lattice_order.index(lattice)
        refined = list(self.possibilities)
        refined[index] = refined[index] & allowed_values
        return JudgmentState(tuple(refined))

    def meet(
        self,
        other: "JudgmentState",
        signature: CalculusSignature,
    ) -> "JudgmentState":
        _validate_state_shape(self, signature)
        _validate_state_shape(other, signature)
        return JudgmentState(
            tuple(
                left & right
                for left, right in zip(self.possibilities, other.possibilities, strict=True)
            )
        )

    def refines(
        self,
        other: "JudgmentState",
        signature: CalculusSignature,
    ) -> bool:
        _validate_state_shape(self, signature)
        _validate_state_shape(other, signature)
        return all(
            left.issubset(right)
            for left, right in zip(self.possibilities, other.possibilities, strict=True)
        )

    def is_consistent(self, signature: CalculusSignature) -> bool:
        _validate_state_shape(self, signature)
        return all(self.possibilities)

    def is_determined(self, signature: CalculusSignature) -> bool:
        return self.is_consistent(signature) and all(
            len(values) == 1 for values in self.possibilities
        )

    def profile(self, signature: CalculusSignature) -> VerdictProfile:
        if not self.is_determined(signature):
            raise CalculusError("only a consistent singleton state has a verdict profile")
        return VerdictProfile.from_mapping(
            {
                lattice: next(iter(values))
                for lattice, values in self.as_dict(signature).items()
            },
            signature,
        )


@dataclass(frozen=True)
class CalculusFinding:
    """A rule application or explicit refusal to infer across a type boundary."""

    rule_id: str
    result: str
    rationale: str


@dataclass(frozen=True)
class ProfileEvaluation:
    """A scope-qualified calculus result, never a creativity attribution."""

    profile: VerdictProfile | None
    outcome: str
    relations: tuple[str, ...]
    findings: tuple[CalculusFinding, ...]
    scope: str = SCOPE


@dataclass(frozen=True)
class ClosureResult:
    """A fixed-point product refinement with explicit refused inferences."""

    state: JudgmentState
    findings: tuple[CalculusFinding, ...]
    scope: str = SCOPE


@dataclass(frozen=True)
class ControlResult:
    """Evaluation of one partial frozen negative control."""

    control_id: str
    expected: tuple[tuple[str, str], ...]
    profile: VerdictProfile
    evaluation: ProfileEvaluation
    passed: bool


@dataclass(frozen=True)
class ExhaustionResult:
    """Summary of the finite declared profile product, not an all-theories claim."""

    profile_count: int
    outcome_counts: tuple[tuple[str, int], ...]
    forbidden_output_absent: bool
    admissible_profile_count: int = 0
    scope: str = SCOPE


@dataclass(frozen=True)
class NonEntailmentGuard:
    """A versioned refusal rule derived from one frozen NE clause."""

    rule_id: str
    kind: str
    profile_conditions: tuple[tuple[str, tuple[str, ...]], ...] = ()
    gate_lattice: str | None = None
    withheld_requirement_ids: tuple[str, ...] = ()
    prohibited_relations: tuple[str, ...] = ()
    prohibited_outcomes: tuple[str, ...] = ()
    rationale: str = ""


@dataclass(frozen=True)
class GuardResult:
    """One executable non-entailment check, never an attribution verdict."""

    rule_id: str
    kind: str
    passed: bool
    finding: CalculusFinding


NON_ENTAILMENT_GUARDS = (
    NonEntailmentGuard(
        "NE_INFORMATION_NOT_KNOWLEDGE",
        "PROFILE_COUNTERMODEL",
        (("constructor_information", ("MAY_PASS",)),
         ("knowledge_retention", ("NOT_APPLICABLE", "EXTERNAL_P_NOT_ATTRIBUTED", "NOT_ESTABLISHED"))),
        prohibited_relations=("PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_REALIZER_TRACE"),
        prohibited_outcomes=("CRITICISABLE_REALIZER_TRACE_AUDITED",),
        rationale="Information-medium capability without a linked retained value is not knowledge.",
    ),
    NonEntailmentGuard(
        "NE_INFORMATION_NOT_CREATIVITY",
        "PROFILE_COUNTERMODEL",
        (("constructor_information", ("MAY_PASS",)),
         ("knowledge_retention", ("NOT_APPLICABLE", "EXTERNAL_P_NOT_ATTRIBUTED", "NOT_ESTABLISHED")),
         ("critical_evidence", ("NOT_ESTABLISHED",))),
        prohibited_relations=("CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"),
        prohibited_outcomes=("CRITICISABLE_REALIZER_TRACE_AUDITED",),
        rationale="Information tasks alone cannot discharge explanation, criticism, or provenance.",
    ),
    NonEntailmentGuard(
        "NE_RETENTION_NOT_CREATIVITY",
        "PROFILE_COUNTERMODEL",
        (("knowledge_retention", ("MAY_PASS",)), ("critical_evidence", ("NOT_ESTABLISHED",))),
        prohibited_relations=("CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"),
        prohibited_outcomes=("CRITICISABLE_REALIZER_TRACE_AUDITED",),
        rationale="Retained construction knowledge does not itself provide an explanatory trace.",
    ),
    NonEntailmentGuard(
        "NE_SELECTION_NOT_HIGH_FIDELITY",
        "PROFILE_COUNTERMODEL",
        (("evolutionary_selection", ("MAY_PASS",)),
         ("no_design_replication", ("NOT_APPLICABLE", "NOT_ESTABLISHED"))),
        prohibited_relations=("CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED",),
        rationale="Selection does not entail digital heredity, correction, or a vehicle.",
    ),
    NonEntailmentGuard(
        "NE_SELECTION_NOT_CRITICISM",
        "PROFILE_COUNTERMODEL",
        (("evolutionary_selection", ("MAY_PASS",)), ("critical_evidence", ("NOT_ESTABLISHED",))),
        prohibited_relations=("THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE"),
        rationale="Selection remains a typed fallibility analogue, not represented criticism.",
    ),
    NonEntailmentGuard(
        "NE_WHOLE_CREATOR_NOT_CLONABLE",
        "PROFILE_COUNTERMODEL",
        (("no_design_replication", ("NOT_APPLICABLE",)),),
        prohibited_relations=("CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED",),
        rationale="H non-applicability cannot impose whole-agent digitality or non-creativity.",
    ),
    NonEntailmentGuard(
        "NE_BOUNDARY_IS_EVIDENCE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("R_BOUNDARY",),
        rationale="A physical knowledge claim is unavailable without its declared bearer boundary.",
    ),
    NonEntailmentGuard(
        "NE_FINITE_ENUMERATION_NOT_ALL_THEORIES",
        "SCOPE_OUTPUT_GUARD",
        rationale="The 1,800-profile product is never promoted to all possible theories.",
    ),
    NonEntailmentGuard(
        "NE_P1_TT_EE_P2_NOT_GENERATOR",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="explanatory_creativity",
        withheld_requirement_ids=("E_EVIDENCE_LINK", "E_PROVENANCE"),
        rationale="The cycle is criticisable only when evidence linking and provenance are also supplied.",
    ),
    NonEntailmentGuard(
        "NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE",
        "PROFILE_COUNTERMODEL",
        (("knowledge_retention", ("NOT_APPLICABLE",)),),
        prohibited_relations=("PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED",),
        prohibited_outcomes=("CRITICISABLE_REALIZER_TRACE_AUDITED",),
        rationale="Bare possibility receives no temporal prior-knowledge inference.",
    ),
    NonEntailmentGuard(
        "NE_RECIPE_NOT_CREATIVITY",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("K_RECIPE_CAUSAL_ROLE",),
        rationale="A named recipe without its causal task role cannot establish construction knowledge or creativity.",
    ),
    NonEntailmentGuard(
        "NE_ARTIFACT_NOT_RECIPE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("A_ARTIFACT_ROLE",),
        rationale="A product is not automatically a recipe or explanatory knowledge bearer.",
    ),
    NonEntailmentGuard(
        "NE_BARE_RECORD_NOT_EVIDENCE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="critical_evidence",
        withheld_requirement_ids=("C_TARGET", "C_CHAIN"),
        rationale="A bare record lacks a theory-mediated target and interpretation chain.",
    ),
    NonEntailmentGuard(
        "NE_EVIDENCE_NOT_CONFIRMATION",
        "PROFILE_COUNTERMODEL",
        (("critical_evidence", ("SURVIVED_DECLARED_ATTEMPT",)),),
        rationale="Survival of an attempted refutation is never confirmation; a trace still requires its independent typed links.",
    ),
    NonEntailmentGuard(
        "NE_VARIATION_NOT_CONJECTURE_IDENTITY",
        "PROFILE_COUNTERMODEL",
        (("evolutionary_selection", ("MAY_PASS",)), ("critical_evidence", ("NOT_ESTABLISHED",))),
        prohibited_relations=("THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE"),
        rationale="A variant is not thereby a represented conjecture and selection is not criticism.",
    ),
    NonEntailmentGuard(
        "NE_NONREFUTABLE_NOT_CREATIVE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="explanatory_creativity",
        withheld_requirement_ids=("E_EE", "E_FALLIBILITY"),
        rationale="An uncriticisable or error-free output cannot admit an audited explanatory trace.",
    ),
    NonEntailmentGuard(
        "NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("X_EXPLANATORY_LEVEL",),
        rationale="The higher-level claim must retain its compatible physical realization.",
    ),
    NonEntailmentGuard(
        "NE_SUBSTRATE_SWAP_NOT_AUTOMATIC",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("K_REALIZATION_EQUIVALENCE",),
        rationale="A label-preserving substrate swap does not establish equivalent realization.",
    ),
    NonEntailmentGuard(
        "NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("R_COUNTERFACTUAL_CAUSAL_ROLE",),
        rationale="One-copy inspection cannot establish a contextual counterfactual role.",
    ),
    NonEntailmentGuard(
        "NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS",
        "LOCAL_GATE_COUNTERMODEL",
        gate_lattice="knowledge_retention",
        withheld_requirement_ids=("R_FINITE_EVIDENCE_BOUND",),
        rationale="Finite variants remain bounded by their declared environment/model domain.",
    ),
)


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string_tuple(value: object, context: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise CalculusError(f"{context} must be a nonempty list of nonempty strings")
    return tuple(value)


def _row_ids(value: object, context: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise CalculusError(f"{context} must be a list")
    identifiers: list[str] = []
    for row in value:
        mapping = _mapping(row)
        identifier = mapping.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise CalculusError(f"{context} contains a row without a nonempty id")
        identifiers.append(identifier)
    if not identifiers or len(set(identifiers)) != len(identifiers):
        raise CalculusError(f"{context} ids must be nonempty and unique")
    return tuple(identifiers)


def _signature_from_plan(plan: Mapping[str, Any]) -> CalculusSignature:
    schema = plan.get("schema")
    if not isinstance(schema, str) or not schema:
        raise CalculusError("plan schema is missing")
    lattices = _mapping(plan.get("lattices"))
    if set(lattices) != set(LATTICE_ORDER):
        raise CalculusError("plan must declare exactly the six calculus lattices")

    requirements: list[tuple[str, tuple[str, ...]]] = []
    verdicts: list[tuple[str, tuple[str, ...]]] = []
    for lattice in LATTICE_ORDER:
        definition = _mapping(lattices.get(lattice))
        requirements.append(
            (
                lattice,
                _row_ids(
                    definition.get("pass_requirements"),
                    f"{lattice}.pass_requirements",
                ),
            )
        )
        verdicts.append(
            (lattice, _string_tuple(definition.get("verdicts"), f"{lattice}.verdicts"))
        )

    integration = _mapping(plan.get("integration_contract"))
    links_value = integration.get("typed_links")
    if not isinstance(links_value, list):
        raise CalculusError("integration_contract.typed_links must be a list")
    typed_links: list[tuple[str, str, str]] = []
    for row in links_value:
        mapping = _mapping(row)
        source = mapping.get("from")
        target = mapping.get("to")
        rule = mapping.get("rule")
        if not all(isinstance(item, str) and item for item in (source, target, rule)):
            raise CalculusError("typed link is malformed")
        typed_links.append((source, target, rule))
    if {(source, target) for source, target, _ in typed_links} != REQUIRED_EDGES:
        raise CalculusError("plan typed links do not match the frozen bridge signature")

    non_entailments_value = plan.get("non_entailments")
    non_entailment_ids = _row_ids(non_entailments_value, "non_entailments")
    if len(non_entailment_ids) != 20:
        raise CalculusError("piecemeal calculus requires all 20 frozen non-entailments")

    controls_value = plan.get("negative_controls")
    if not isinstance(controls_value, list):
        raise CalculusError("negative_controls must be a list")
    controls: list[NegativeControl] = []
    for row in controls_value:
        mapping = _mapping(row)
        control_id = mapping.get("id")
        expected = _mapping(mapping.get("expected"))
        if not isinstance(control_id, str) or not control_id:
            raise CalculusError("negative control id is malformed")
        pairs: list[tuple[str, str]] = []
        for lattice, verdict in expected.items():
            if lattice not in LATTICE_ORDER:
                raise CalculusError(f"{control_id} names unknown lattice {lattice!r}")
            if not isinstance(verdict, str) or verdict not in dict(verdicts)[lattice]:
                raise CalculusError(f"{control_id} names invalid verdict for {lattice}")
            pairs.append((lattice, verdict))
        if not pairs:
            raise CalculusError(f"{control_id} must constrain at least one lattice")
        controls.append(NegativeControl(control_id, tuple(sorted(pairs))))
    if len(controls) != 13 or len({control.control_id for control in controls}) != len(controls):
        raise CalculusError("piecemeal calculus requires 13 uniquely named controls")

    return CalculusSignature(
        plan_schema=schema,
        plan_sha256=FROZEN_PLAN_SHA256,
        lattice_order=LATTICE_ORDER,
        requirement_ids=tuple(requirements),
        verdict_domains=tuple(verdicts),
        typed_links=tuple(typed_links),
        non_entailment_ids=non_entailment_ids,
        negative_controls=tuple(controls),
    )


def _validate_bridge_registry(signature: CalculusSignature) -> None:
    """Bind executable bridge metadata to the authenticated four plan arrows."""

    executable_edges = {
        (rule.source_lattices[0], rule.target_lattice)
        for rule in BRIDGE_RULES
        if rule.rule_id != "B_H_CONDITIONAL_BRANCH"
    }
    frozen_edges = {(source, target) for source, target, _ in signature.typed_links}
    if executable_edges != frozen_edges:
        raise CalculusError("bridge registry no longer matches frozen typed-link edges")
    if set(BRIDGE_RULE_BY_ID) != {
        "B_I_R_BEARER_GATE",
        "B_R_E_REALIZER_CONSTRAINT",
        "B_C_E_CRITICISM_LINK",
        "B_V_E_TYPED_ANALOGUE",
        "B_H_CONDITIONAL_BRANCH",
    }:
        raise CalculusError("bridge registry ids are incomplete or duplicated")


def _validate_guard_registry(signature: CalculusSignature) -> None:
    """Ensure every frozen non-entailment has exactly one executable guard."""

    guard_ids = {guard.rule_id for guard in NON_ENTAILMENT_GUARDS}
    if guard_ids != set(signature.non_entailment_ids) or len(NON_ENTAILMENT_GUARDS) != 20:
        raise CalculusError("non-entailment guard registry does not cover the frozen plan")
    for guard in NON_ENTAILMENT_GUARDS:
        if guard.kind not in {
            "PROFILE_COUNTERMODEL",
            "LOCAL_GATE_COUNTERMODEL",
            "SCOPE_OUTPUT_GUARD",
        }:
            raise CalculusError(f"unknown non-entailment guard kind: {guard.kind}")
        for lattice, allowed in guard.profile_conditions:
            if lattice not in signature.lattice_order or not allowed:
                raise CalculusError(f"malformed profile guard: {guard.rule_id}")
            unknown = set(allowed) - set(signature.verdicts_for(lattice))
            if unknown:
                raise CalculusError(f"invalid guard verdicts for {guard.rule_id}: {sorted(unknown)!r}")
        if guard.kind == "LOCAL_GATE_COUNTERMODEL":
            if guard.gate_lattice not in signature.lattice_order or not guard.withheld_requirement_ids:
                raise CalculusError(f"malformed local gate guard: {guard.rule_id}")
            unknown = set(guard.withheld_requirement_ids) - set(
                signature.requirements_for(guard.gate_lattice)
            )
            if unknown:
                raise CalculusError(f"invalid local gate ids for {guard.rule_id}: {sorted(unknown)!r}")
        if set(guard.prohibited_relations) - RELATION_NAMES:
            raise CalculusError(f"unknown guarded relation for {guard.rule_id}")
        if set(guard.prohibited_outcomes) - PROFILE_OUTCOMES:
            raise CalculusError(f"unknown guarded outcome for {guard.rule_id}")


def authenticate_calculus(
    plan_path: Path = CANONICAL_PLAN,
    subject_sha256: str = PRIMARY_SHA256,
) -> CalculusSignature:
    """Authenticate the fixed plan before using it as a calculus signature."""

    plan, report = authenticate_frozen_plan(plan_path, subject_sha256)
    if not report["authenticated"]:
        raise CalculusError("frozen piecemeal plan did not authenticate")
    signature = _signature_from_plan(plan)
    _validate_bridge_registry(signature)
    _validate_guard_registry(signature)
    return signature


def _validate_state_shape(
    state: JudgmentState,
    signature: CalculusSignature,
) -> None:
    if len(state.possibilities) != len(signature.lattice_order):
        raise CalculusError("judgment state has the wrong coordinate count")
    for lattice, possibilities in zip(
        signature.lattice_order, state.possibilities, strict=True
    ):
        if not isinstance(possibilities, frozenset):
            raise CalculusError("judgment coordinates must be frozensets")
        unknown = possibilities - frozenset(signature.verdicts_for(lattice))
        if unknown:
            raise CalculusError(
                f"judgment state has invalid {lattice} verdict(s): {sorted(unknown)!r}"
            )


def local_gate(
    signature: CalculusSignature,
    lattice: str,
    satisfied_requirement_ids: Iterable[str],
) -> LocalGate:
    """Construct one checked local gate from the frozen requirement signature."""

    if lattice not in signature.lattice_order:
        raise CalculusError(f"unknown lattice: {lattice}")
    if isinstance(satisfied_requirement_ids, str):
        supplied = frozenset({satisfied_requirement_ids})
    else:
        supplied = frozenset(satisfied_requirement_ids)
    if not all(isinstance(identifier, str) and identifier for identifier in supplied):
        raise CalculusError("satisfied requirement ids must be nonempty strings")
    required = frozenset(signature.requirements_for(lattice))
    unknown = supplied - required
    if unknown:
        raise CalculusError(
            f"unknown requirement id(s) for {lattice}: {sorted(unknown)!r}"
        )
    return LocalGate(lattice, required, supplied)


def refine_with_local_gate(
    state: JudgmentState,
    gate: LocalGate,
    signature: CalculusSignature,
) -> JudgmentState:
    """Apply one necessary-only local gate as a product-state refinement.

    This is deliberately one-directional: a complete gate leaves all verdicts
    possible, while an incomplete gate only removes the relevant positive
    verdict(s). It cannot manufacture retention, criticism, provenance, or a
    creativity claim.
    """

    _validate_state_shape(state, signature)
    if gate.lattice not in signature.lattice_order:
        raise CalculusError(f"unknown gate lattice: {gate.lattice}")
    required = frozenset(signature.requirements_for(gate.lattice))
    if gate.required_requirement_ids != required:
        raise CalculusError("local gate does not match the authenticated signature")
    if not gate.satisfied_requirement_ids.issubset(required):
        raise CalculusError("local gate has unknown satisfied requirement ids")
    if gate.is_complete:
        return state
    allowed = frozenset(signature.verdicts_for(gate.lattice)) - GATE_REQUIRED_VERDICTS[
        gate.lattice
    ]
    if not allowed:
        raise CalculusError(f"no non-positive verdict is available for {gate.lattice}")
    return state.constrain(signature, gate.lattice, allowed)


def refine_with_local_gates(
    state: JudgmentState,
    gates: Iterable[LocalGate],
    signature: CalculusSignature,
) -> JudgmentState:
    """Meet a sequence of local necessary-condition refinements."""

    refined = state
    for gate in gates:
        refined = refine_with_local_gate(refined, gate, signature)
    return refined


def complete_local_gate(signature: CalculusSignature, lattice: str) -> LocalGate:
    """Return the full frozen local gate for an explicitly stipulated premise."""

    return local_gate(signature, lattice, signature.requirements_for(lattice))


def _normalise_context(context: CalculusContext | None) -> CalculusContext:
    if context is None:
        return CalculusContext()
    if not isinstance(context, CalculusContext):
        raise CalculusError("calculus context must be a CalculusContext")
    return context


def _validate_witness(witness: TypedLinkWitness) -> None:
    rule = BRIDGE_RULE_BY_ID.get(witness.rule_id)
    if rule is None or witness.rule_id == "B_H_CONDITIONAL_BRANCH":
        raise CalculusError(f"unknown or non-link bridge witness: {witness.rule_id!r}")
    if (witness.source_lattice, witness.target_lattice) != (
        rule.source_lattices[0],
        rule.target_lattice,
    ):
        raise CalculusError(f"bridge witness does not match rule edge: {witness.rule_id}")
    for field in (witness.scope_id, witness.source_id, witness.target_id):
        if not isinstance(field, str) or not field:
            raise CalculusError("bridge witness requires nonempty scope and object ids")
    if witness.rule_id in {"B_I_R_BEARER_GATE", "B_R_E_REALIZER_CONSTRAINT"}:
        if not isinstance(witness.knowledge_bearer_id, str) or not witness.knowledge_bearer_id:
            raise CalculusError(f"{witness.rule_id} requires a declared knowledge bearer id")
    if witness.rule_id in {"B_R_E_REALIZER_CONSTRAINT", "B_C_E_CRITICISM_LINK"}:
        if not isinstance(witness.target_claim_id, str) or not witness.target_claim_id:
            raise CalculusError(f"{witness.rule_id} requires a declared target claim id")
    if witness.rule_id == "B_C_E_CRITICISM_LINK":
        if witness.critical_outcome not in CRITICAL_PACKAGE_OUTCOMES:
            raise CalculusError("C-to-E witness requires one declared critical outcome")
    if witness.revision_route_id is not None and (
        not isinstance(witness.revision_route_id, str) or not witness.revision_route_id
    ):
        raise CalculusError("revision route ids must be nonempty strings when supplied")


def _context_parts(
    context: CalculusContext | None,
    signature: CalculusSignature,
) -> tuple[dict[str, LocalGate], tuple[TypedLinkWitness, ...]]:
    normalized = _normalise_context(context)
    gates: dict[str, LocalGate] = {}
    for gate in normalized.local_gates:
        if not isinstance(gate, LocalGate):
            raise CalculusError("context local gates must be LocalGate values")
        if gate.lattice in gates:
            raise CalculusError(f"duplicate local gate for {gate.lattice}")
        refine_with_local_gate(JudgmentState.initial(signature), gate, signature)
        gates[gate.lattice] = gate
    witnesses: list[TypedLinkWitness] = []
    for witness in normalized.link_witnesses:
        if not isinstance(witness, TypedLinkWitness):
            raise CalculusError("context link witnesses must be TypedLinkWitness values")
        _validate_witness(witness)
        witnesses.append(witness)
    return gates, tuple(witnesses)


def _has_complete_gate(gates: Mapping[str, LocalGate], lattice: str) -> bool:
    return lattice in gates and gates[lattice].is_complete


def _witnesses_for(
    witnesses: Iterable[TypedLinkWitness],
    rule_id: str,
) -> tuple[TypedLinkWitness, ...]:
    return tuple(witness for witness in witnesses if witness.rule_id == rule_id)


def _critical_link_for_value(
    witnesses: Iterable[TypedLinkWitness],
    critical_outcome: str,
    *,
    require_revision_route: bool = False,
) -> TypedLinkWitness | None:
    for witness in _witnesses_for(witnesses, "B_C_E_CRITICISM_LINK"):
        if witness.critical_outcome != critical_outcome:
            continue
        if require_revision_route and not witness.revision_route_id:
            continue
        return witness
    return None


def _realizer_links_match(
    witnesses: Iterable[TypedLinkWitness],
    critical_outcome: str,
) -> bool:
    critical_link = _critical_link_for_value(witnesses, critical_outcome)
    if critical_link is None:
        return False
    for information_link in _witnesses_for(witnesses, "B_I_R_BEARER_GATE"):
        for retention_link in _witnesses_for(witnesses, "B_R_E_REALIZER_CONSTRAINT"):
            if (
                information_link.scope_id == retention_link.scope_id == critical_link.scope_id
                and information_link.knowledge_bearer_id == retention_link.knowledge_bearer_id
                and information_link.target_id == retention_link.source_id
                and retention_link.target_id == critical_link.target_id
                and retention_link.target_claim_id == critical_link.target_claim_id
            ):
                return True
    return False


def close(
    state: JudgmentState,
    signature: CalculusSignature,
    context: CalculusContext | None = None,
) -> ClosureResult:
    """Close a raw product state under local gates and typed C-to-E linkage.

    The raw Cartesian product remains useful for combinatorics. Closure removes
    only verdicts that lack a complete local certificate or a typed critical
    link; it never manufactures a positive verdict from another coordinate.
    """

    _validate_state_shape(state, signature)
    gates, witnesses = _context_parts(context, signature)
    refined = refine_with_local_gates(state, gates.values(), signature)
    findings: list[CalculusFinding] = []
    for gate in gates.values():
        if gate.is_complete:
            continue
        for guard in NON_ENTAILMENT_GUARDS:
            if (
                guard.kind == "LOCAL_GATE_COUNTERMODEL"
                and guard.gate_lattice == gate.lattice
                and set(guard.withheld_requirement_ids).issubset(gate.missing_requirement_ids)
            ):
                findings.append(
                    CalculusFinding(guard.rule_id, "LOCAL_GATE_REFUSAL", guard.rationale)
                )

    while refined.is_consistent(signature):
        allowed_e = refined.permitted(signature, "explanatory_creativity")
        gate_required_e = {
            "CRITICISABLE_TRACE_AUDITED",
            "REFUTED_ON_DECLARED_DOMAIN",
        } & set(allowed_e)
        if not gate_required_e:
            break
        c_values = refined.permitted(signature, "critical_evidence")
        complete_c_e = _has_complete_gate(gates, "explanatory_creativity") and _has_complete_gate(
            gates, "critical_evidence"
        )
        trace_supported = complete_c_e and any(
            _critical_link_for_value(
                witnesses,
                value,
                require_revision_route=value == "REFUTED_CONJUNCTION",
            )
            is not None
            for value in c_values & CRITICAL_PACKAGE_OUTCOMES
        )
        refutation_supported = complete_c_e and (
            "REFUTED_CONJUNCTION" in c_values
            and _critical_link_for_value(witnesses, "REFUTED_CONJUNCTION") is not None
        )
        remove: set[str] = set()
        if "CRITICISABLE_TRACE_AUDITED" in gate_required_e and not trace_supported:
            remove.add("CRITICISABLE_TRACE_AUDITED")
            findings.append(
                CalculusFinding(
                    "B_C_E_CRITICISM_LINK",
                    "CLOSURE_PRUNED_UNLINKED_E_AUDIT",
                    "An audited E coordinate requires complete C/E local gates and a "
                    "matching critical-package witness; co-occurring verdict labels are insufficient.",
                )
            )
        if "REFUTED_ON_DECLARED_DOMAIN" in gate_required_e and not refutation_supported:
            remove.add("REFUTED_ON_DECLARED_DOMAIN")
            findings.append(
                CalculusFinding(
                    "B_C_E_CRITICISM_LINK",
                    "CLOSURE_PRUNED_UNLINKED_E_REFUTATION",
                    "A refuted E coordinate requires complete C/E local gates and a "
                    "C-to-E witness for the declared refuted conjunction and scope.",
                )
            )
        if not remove:
            break
        refined = refined.constrain(
            signature,
            "explanatory_creativity",
            set(allowed_e) - remove,
        )
    return ClosureResult(refined, tuple(findings))


def validate_profile(
    profile: VerdictProfile,
    signature: CalculusSignature,
) -> None:
    for lattice, verdict in profile.as_dict().items():
        if verdict not in signature.verdicts_for(lattice):
            raise CalculusError(f"invalid {lattice} verdict: {verdict!r}")


def enumerate_profiles(
    signature: CalculusSignature,
    fixed_verdicts: Mapping[str, str] | None = None,
) -> Iterable[VerdictProfile]:
    """Enumerate only the declared six-status product, never 2**44 requirements."""

    fixed = dict(fixed_verdicts or {})
    if not set(fixed).issubset(signature.lattice_order):
        unknown = sorted(set(fixed) - set(signature.lattice_order))
        raise CalculusError(f"unknown fixed lattice(s): {unknown!r}")
    domains: list[tuple[str, ...]] = []
    for lattice in signature.lattice_order:
        if lattice not in fixed:
            domains.append(signature.verdicts_for(lattice))
            continue
        verdict = fixed[lattice]
        if verdict not in signature.verdicts_for(lattice):
            raise CalculusError(f"invalid fixed verdict for {lattice}: {verdict!r}")
        domains.append((verdict,))
    for values in product(*domains):
        yield VerdictProfile(*values)


def _default_profile(
    signature: CalculusSignature,
    expected: Mapping[str, str],
) -> VerdictProfile:
    values: dict[str, str] = {}
    for lattice in signature.lattice_order:
        values[lattice] = expected.get(
            lattice,
            "NOT_ESTABLISHED"
            if "NOT_ESTABLISHED" in signature.verdicts_for(lattice)
            else signature.verdicts_for(lattice)[0],
        )
    return VerdictProfile.from_mapping(values, signature)


def _finding(
    rule_id: str,
    result: str,
    rationale: str,
) -> CalculusFinding:
    return CalculusFinding(rule_id, result, rationale)


def _context_for_declared_gate_required_profile(
    signature: CalculusSignature,
    profile: VerdictProfile,
) -> CalculusContext:
    """Supply only full local gates for explicitly stipulated evidential statuses."""

    return CalculusContext(
        tuple(
            complete_local_gate(signature, lattice)
            for lattice, verdict in profile.as_dict().items()
            if verdict in GATE_REQUIRED_VERDICTS[lattice]
        )
    )


def _matching_profile_guards(
    profile: VerdictProfile,
) -> tuple[NonEntailmentGuard, ...]:
    values = profile.as_dict()
    return tuple(
        guard
        for guard in NON_ENTAILMENT_GUARDS
        if guard.kind == "PROFILE_COUNTERMODEL"
        and all(values[lattice] in allowed for lattice, allowed in guard.profile_conditions)
    )


def _scope_guard_findings() -> tuple[CalculusFinding, ...]:
    return tuple(
        CalculusFinding(guard.rule_id, "SCOPE_LIMIT_ENFORCED", guard.rationale)
        for guard in NON_ENTAILMENT_GUARDS
        if guard.kind == "SCOPE_OUTPUT_GUARD"
    )


def evaluate_non_entailment_guards(
    signature: CalculusSignature,
) -> tuple[GuardResult, ...]:
    """Run the complete frozen NE registry as profile, gate, and scope checks."""

    _validate_guard_registry(signature)
    results: list[GuardResult] = []
    for guard in NON_ENTAILMENT_GUARDS:
        if guard.kind == "SCOPE_OUTPUT_GUARD":
            passed = SCOPE == "PIECEMEAL_COMBINATORIAL_CALCULUS_ONLY" and not (
                FORBIDDEN_OUTPUT_TOKENS & {SCOPE}
            )
            result = "SCOPE_LIMIT_ENFORCED" if passed else "SCOPE_LIMIT_BREACHED"
        elif guard.kind == "LOCAL_GATE_COUNTERMODEL":
            assert guard.gate_lattice is not None
            required = frozenset(signature.requirements_for(guard.gate_lattice))
            gate = local_gate(
                signature,
                guard.gate_lattice,
                required - set(guard.withheld_requirement_ids),
            )
            refined = refine_with_local_gate(JudgmentState.initial(signature), gate, signature)
            passed = not bool(
                POSITIVE_VERDICTS[guard.gate_lattice]
                & refined.permitted(signature, guard.gate_lattice)
            )
            result = "LOCAL_GATE_REFUSAL" if passed else "LOCAL_GATE_BYPASS"
        else:
            values = {
                lattice: allowed[0]
                for lattice, allowed in guard.profile_conditions
            }
            profile = _default_profile(signature, values)
            evaluation = evaluate_profile(
                profile,
                signature,
                _context_for_declared_gate_required_profile(signature, profile),
            )
            passed = not (
                set(guard.prohibited_relations) & set(evaluation.relations)
                or evaluation.outcome in guard.prohibited_outcomes
            )
            result = "PROFILE_REFUSAL" if passed else "PROFILE_GUARD_BREACHED"
        results.append(
            GuardResult(
                guard.rule_id,
                guard.kind,
                passed,
                CalculusFinding(guard.rule_id, result, guard.rationale),
            )
        )
    return tuple(results)


def evaluate_profile(
    profile: VerdictProfile,
    signature: CalculusSignature,
    context: CalculusContext | None = None,
) -> ProfileEvaluation:
    """Compose a stipulated profile only through complete gates and typed links.

    A verdict tuple by itself is not an audit.  Positive/audited relations are
    emitted only where the corresponding frozen local gate is complete and the
    required boundary/target/revision witness is present.
    """

    validate_profile(profile, signature)
    gates, witnesses = _context_parts(context, signature)
    singleton = JudgmentState(
        tuple(frozenset({value}) for value in profile.as_dict().values())
    )
    closure = close(singleton, signature, context)
    values = profile.as_dict()
    information = (
        values["constructor_information"] == "MAY_PASS"
        and _has_complete_gate(gates, "constructor_information")
    )
    retention = (
        values["knowledge_retention"] == "MAY_PASS"
        and _has_complete_gate(gates, "knowledge_retention")
    )
    h_value = values["no_design_replication"]
    h_audited = h_value == "MAY_PASS" and _has_complete_gate(gates, "no_design_replication")
    selection = (
        values["evolutionary_selection"] == "MAY_PASS"
        and _has_complete_gate(gates, "evolutionary_selection")
    )
    critical = values["critical_evidence"]
    critical_package = (
        critical in CRITICAL_PACKAGE_OUTCOMES
        and _has_complete_gate(gates, "critical_evidence")
    )
    explanatory = values["explanatory_creativity"]
    e_gate_complete = _has_complete_gate(gates, "explanatory_creativity")
    e_audited = explanatory == "CRITICISABLE_TRACE_AUDITED" and e_gate_complete
    e_refuted = explanatory == "REFUTED_ON_DECLARED_DOMAIN" and e_gate_complete
    critical_link = (
        _critical_link_for_value(
            witnesses,
            critical,
            require_revision_route=critical == "REFUTED_CONJUNCTION",
        )
        if critical_package and e_audited
        else None
    )
    refutation_link = (
        _critical_link_for_value(witnesses, "REFUTED_CONJUNCTION")
        if critical == "REFUTED_CONJUNCTION" and critical_package and e_refuted
        else None
    )
    information_retention_link = bool(
        information
        and retention
        and _witnesses_for(witnesses, "B_I_R_BEARER_GATE")
    )
    retention_explanation_link = bool(
        retention
        and e_audited
        and _witnesses_for(witnesses, "B_R_E_REALIZER_CONSTRAINT")
    )
    realizer_trace = bool(
        e_audited
        and critical_link is not None
        and information_retention_link
        and retention_explanation_link
        and _realizer_links_match(witnesses, critical)
    )
    scoped_refutation = refutation_link is not None
    refutation_recorded = critical == "REFUTED_CONJUNCTION" and critical_package
    revision_linked = bool(
        critical == "REFUTED_CONJUNCTION"
        and _critical_link_for_value(
            witnesses,
            "REFUTED_CONJUNCTION",
            require_revision_route=True,
        )
        is not None
    )

    relations: set[str] = set()
    findings: list[CalculusFinding] = list(closure.findings)
    if information:
        relations.add("INFORMATION_VARIABLE_CANDIDATE")
    if information_retention_link:
        relations.add("PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED")
        findings.append(
            _finding(
                "B_I_R_BEARER_GATE",
                "BOUNDARY_LINKED_KNOWLEDGE_BEARER",
                "The information value and retained knowledge share a declared "
                "bearer boundary; no whole-agent clonability claim is made.",
            )
        )
    elif information:
        findings.append(
            _finding(
                "B_I_R_BEARER_GATE",
                "NO_KNOWLEDGE_INFERENCE",
                "Information-medium capability lacks a declared I-to-R bearer link.",
            )
        )

    if h_audited:
        relations.add("CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED")
        findings.append(
            _finding(
                "B_H_CONDITIONAL_BRANCH",
                "DIGITAL_ERROR_CORRECTION_GATE_COMPLETE",
                "The declared H verdict is accompanied by its complete local "
                "recipe, digitality, and causal correction gate.",
            )
        )
    elif h_value == "MAY_PASS":
        findings.append(
            _finding(
                "B_H_CONDITIONAL_BRANCH",
                "DIGITAL_ERROR_CORRECTION_NOT_ESTABLISHED",
                "A raw H verdict cannot be audited without the full H local gate.",
            )
        )
    elif h_value == "NOT_APPLICABLE":
        findings.append(
            _finding(
                "B_H_CONDITIONAL_BRANCH",
                "NOT_APPLICABLE_NOT_NON_CREATIVE",
                "No high-accuracy reproduction claim is being made; no "
                "non-creativity inference is permitted.",
            )
        )

    if selection:
        relations.add("TYPED_VARIATION_SELECTION_ANALOGUE")
        findings.append(
            _finding(
                "B_V_E_TYPED_ANALOGUE",
                "TYPED_ANALOGUE_ONLY",
                "Variation and selection are a fallibility analogue, not "
                "represented criticism or explanatory creativity.",
            )
        )

    if critical_package:
        relations.add("THEORY_MEDIATED_CRITICISM_PACKAGE")
    if e_audited and critical_link is not None:
        relations.add("CRITICISABLE_EXPLANATORY_TRACE")
        findings.append(
            _finding(
                "B_C_E_CRITICISM_LINK",
                "TARGET_AND_REVISION_LINK_DECLARED",
                "C and E are joined by a declared target, scope, and where "
                "needed a refutation-to-revision route.",
            )
        )
    elif critical_package:
        findings.append(
            _finding(
                "B_C_E_CRITICISM_LINK",
                "NO_EXPLANATORY_INFERENCE",
                "A C package without a matching E link cannot discharge E_EVIDENCE_LINK.",
            )
        )
    if scoped_refutation:
        findings.append(
            _finding(
                "B_C_E_CRITICISM_LINK",
                "SCOPED_REFUTATION_LINK_DECLARED",
                "The C-to-E witness binds the refuted conjunction to the declared "
                "target and finite scope; it does not automatically refute a component.",
            )
        )

    if retention_explanation_link:
        findings.append(
            _finding(
                "B_R_E_REALIZER_CONSTRAINT",
                "TARGET_LINKED_REALIZER_CONSTRAINT",
                "Retained knowledge is linked to the declared explanatory target.",
            )
        )
    elif retention:
        findings.append(
            _finding(
                "B_R_E_REALIZER_CONSTRAINT",
                "NO_EXPLANATORY_INFERENCE",
                "Retention without a target-linked E witness remains non-attributive.",
            )
        )
    if realizer_trace:
        relations.add("CRITICISABLE_REALIZER_TRACE")

    if scoped_refutation:
        outcome = "REFUTED_ON_DECLARED_DOMAIN"
    elif refutation_recorded and not revision_linked:
        outcome = "REFUTATION_RECORDED_ON_DECLARED_DOMAIN"
        findings.append(
            _finding(
                "B_C_E_CRITICISM_LINK",
                "REFUTATION_NOT_AUTOMATIC_COMPONENT_FALSIFICATION",
                "C records a scoped conjunction refutation; without a declared "
                "revision link it neither falsifies a named E component nor permits an audited trace.",
            )
        )
    elif not closure.state.is_consistent(signature):
        outcome = "INCONSISTENT_PROFILE"
        findings.append(
            _finding(
                "PRODUCT_CLOSURE",
                "UNSUPPORTED_POSITIVE_COORDINATE",
                "A stipulated positive/audited coordinate was removed by the local-gate or typed-link closure.",
            )
        )
    elif explanatory == "PROVENANCE_UNRESOLVED" or values["knowledge_retention"] == (
        "EXTERNAL_P_NOT_ATTRIBUTED"
    ):
        outcome = "PROVENANCE_UNRESOLVED"
    elif explanatory == "UNRESOLVED_NOT_NON_CREATIVE":
        outcome = "UNRESOLVED_NOT_NON_CREATIVE"
    elif explanatory == "CRITICISABLE_TRACE_AUDITED":
        if critical_link is None:
            outcome = "INCONSISTENT_PROFILE"
        elif realizer_trace:
            outcome = "CRITICISABLE_REALIZER_TRACE_AUDITED"
        else:
            outcome = "CRITICISABLE_TRACE_REALIZER_NOT_ESTABLISHED"
    elif selection:
        outcome = "SELECTION_ANALOGUE_ONLY"
    else:
        outcome = "NOT_ESTABLISHED"

    matching_guards = _matching_profile_guards(profile)
    for guard in matching_guards:
        if set(guard.prohibited_relations) & relations or outcome in guard.prohibited_outcomes:
            raise AssertionError(f"frozen non-entailment breached: {guard.rule_id}")
        findings.append(CalculusFinding(guard.rule_id, "PROFILE_REFUSAL", guard.rationale))
    findings.extend(_scope_guard_findings())
    if outcome not in PROFILE_OUTCOMES:
        raise AssertionError(f"unregistered calculus outcome: {outcome}")
    if FORBIDDEN_OUTPUT_TOKENS & (set(relations) | {outcome}):
        raise AssertionError("calculus emitted a forbidden attribution token")
    return ProfileEvaluation(
        profile=profile,
        outcome=outcome,
        relations=tuple(sorted(relations)),
        findings=tuple(findings),
    )


def evaluate_state(
    state: JudgmentState,
    signature: CalculusSignature,
    context: CalculusContext | None = None,
) -> ProfileEvaluation:
    """Close a partial product state before reporting uncertainty or conflict."""

    _validate_state_shape(state, signature)
    if state.is_determined(signature):
        return evaluate_profile(state.profile(signature), signature, context)
    closure = close(state, signature, context)
    if not closure.state.is_consistent(signature):
        return ProfileEvaluation(
            profile=None,
            outcome="INCONSISTENT_PROFILE",
            relations=(),
            findings=closure.findings
            + (
                _finding(
                    "PRODUCT_MEET",
                    "EMPTY_COORDINATE",
                    "At least one verdict coordinate has no compatible value after closure.",
                ),
            )
            + _scope_guard_findings(),
        )
    if closure.state.is_determined(signature):
        return evaluate_profile(closure.state.profile(signature), signature, context)
    return ProfileEvaluation(
        profile=None,
        outcome="UNDERDETERMINED_PROFILE",
        relations=(),
        findings=closure.findings
        + (
            _finding(
                "PRODUCT_REFINEMENT",
                "FURTHER_EVIDENCE_REQUIRED",
                "The closed verdict state has more than one remaining value in at least one coordinate.",
            ),
        )
        + _scope_guard_findings(),
    )


CONTROL_PROHIBITIONS = {
    "NC_INFORMATION_WITHOUT_RETENTION": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_RETENTION_WITHOUT_EXPLANATION": (
        frozenset({"CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_NAKED_REPLICATOR": (
        frozenset({"CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED", "THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_SELECTION_WITHOUT_CRITICISM": (
        frozenset({"THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_CREATOR_WITHOUT_SELF_REPRODUCTION": (
        frozenset({"CONDITIONAL_HIGH_FIDELITY_REPLICATION_AUDITED"}),
        frozenset(),
    ),
    "NC_BARE_POSSIBILITY_WITHOUT_PRIOR_KNOWLEDGE": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_EXTERNAL_RECIPE_WITHOUT_CANDIDATE_ATTRIBUTION": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE": (
        frozenset({"THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_AGREEING_RESULT_NOT_CONFIRMATION": (
        frozenset({"CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_UNREFUTABLE_OUTPUT": (
        frozenset({"THEORY_MEDIATED_CRITICISM_PACKAGE", "CRITICISABLE_EXPLANATORY_TRACE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_UNCONSTRAINED_SUBSTRATE_SWAP": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_ONE_COPY_INSPECTION": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "TYPED_VARIATION_SELECTION_ANALOGUE", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
    "NC_NONPHYSICAL_RECIPE": (
        frozenset({"PHYSICAL_KNOWLEDGE_REALIZER_CONSTRAINED", "CRITICISABLE_REALIZER_TRACE"}),
        frozenset({"CRITICISABLE_REALIZER_TRACE_AUDITED"}),
    ),
}


def evaluate_negative_controls(
    signature: CalculusSignature,
) -> tuple[ControlResult, ...]:
    """Evaluate every frozen partial control against its named shortcut ban."""

    if set(CONTROL_PROHIBITIONS) != {control.control_id for control in signature.negative_controls}:
        raise CalculusError("control-prohibition registry does not cover the frozen controls")
    results: list[ControlResult] = []
    for control in signature.negative_controls:
        expected = control.expected_dict()
        profile = _default_profile(signature, expected)
        evaluation = evaluate_profile(
            profile,
            signature,
            _context_for_declared_gate_required_profile(signature, profile),
        )
        prohibited_relations, prohibited_outcomes = CONTROL_PROHIBITIONS[control.control_id]
        passed = (
            all(profile.as_dict()[lattice] == verdict for lattice, verdict in expected.items())
            and not (prohibited_relations & set(evaluation.relations))
            and evaluation.outcome not in prohibited_outcomes
            and not (FORBIDDEN_OUTPUT_TOKENS & (set(evaluation.relations) | {evaluation.outcome}))
        )
        results.append(
            ControlResult(
                control_id=control.control_id,
                expected=control.expected,
                profile=profile,
                evaluation=evaluation,
                passed=passed,
            )
        )
    return tuple(results)


def find_countermodel(
    signature: CalculusSignature,
    fixed_verdicts: Mapping[str, str],
    prohibited_relations: Iterable[str] = (),
    prohibited_outcomes: Iterable[str] = (),
    context: CalculusContext | None = None,
) -> VerdictProfile | None:
    """Find a declared profile that blocks a nominated shortcut inference."""

    forbidden_relations = frozenset(prohibited_relations)
    forbidden_outcome_set = frozenset(prohibited_outcomes)
    unknown_relations = forbidden_relations - RELATION_NAMES
    unknown_outcomes = forbidden_outcome_set - PROFILE_OUTCOMES
    if unknown_relations:
        raise CalculusError(f"unknown prohibited relation(s): {sorted(unknown_relations)!r}")
    if unknown_outcomes:
        raise CalculusError(f"unknown prohibited outcome(s): {sorted(unknown_outcomes)!r}")
    for profile in enumerate_profiles(signature, fixed_verdicts):
        evaluation = evaluate_profile(profile, signature, context)
        if (
            not forbidden_relations.intersection(evaluation.relations)
            and evaluation.outcome not in forbidden_outcome_set
        ):
            return profile
    return None


def exhaust_declared_profile_space(
    signature: CalculusSignature,
    context: CalculusContext | None = None,
) -> ExhaustionResult:
    """Enumerate raw profiles and separately count closed admissible profiles."""

    counts = {outcome: 0 for outcome in PROFILE_OUTCOMES}
    forbidden_output_absent = True
    profile_count = 0
    admissible_profile_count = 0
    for profile in enumerate_profiles(signature):
        singleton = JudgmentState(
            tuple(frozenset({value}) for value in profile.as_dict().values())
        )
        if close(singleton, signature, context).state.is_determined(signature):
            admissible_profile_count += 1
        evaluation = evaluate_profile(profile, signature, context)
        counts[evaluation.outcome] += 1
        profile_count += 1
        forbidden_output_absent = forbidden_output_absent and not (
            FORBIDDEN_OUTPUT_TOKENS & (set(evaluation.relations) | {evaluation.outcome})
        )
    return ExhaustionResult(
        profile_count=profile_count,
        outcome_counts=tuple(sorted(counts.items())),
        forbidden_output_absent=forbidden_output_absent,
        admissible_profile_count=admissible_profile_count,
    )

__all__ = [
    "BRIDGE_RULES",
    "CRITICAL_PACKAGE_OUTCOMES",
    "FORBIDDEN_OUTPUT_TOKENS",
    "GATE_REQUIRED_VERDICTS",
    "LATTICE_ORDER",
    "NON_ENTAILMENT_GUARDS",
    "POSITIVE_VERDICTS",
    "PROFILE_OUTCOMES",
    "RELATION_NAMES",
    "SCOPE",
    "BridgeRule",
    "CalculusContext",
    "CalculusError",
    "CalculusFinding",
    "CalculusSignature",
    "ClosureResult",
    "ControlResult",
    "ExhaustionResult",
    "GuardResult",
    "JudgmentState",
    "LocalGate",
    "NegativeControl",
    "NonEntailmentGuard",
    "ProfileEvaluation",
    "TypedLinkWitness",
    "VerdictProfile",
    "authenticate_calculus",
    "close",
    "complete_local_gate",
    "enumerate_profiles",
    "evaluate_negative_controls",
    "evaluate_non_entailment_guards",
    "evaluate_profile",
    "evaluate_state",
    "exhaust_declared_profile_space",
    "find_countermodel",
    "local_gate",
    "refine_with_local_gate",
    "refine_with_local_gates",
    "validate_profile",
]