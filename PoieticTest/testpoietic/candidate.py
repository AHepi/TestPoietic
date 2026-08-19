"""Conservative structural audit for claim-scoped candidate witness packages.

The evaluator never dereferences raw evidence and never attributes creativity.  It
only checks whether a declared witness is structurally suitable for later,
criticisable review against the authenticated piecemeal plan.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .constants import PRIMARY_SHA256
from .piecemeal import (
    CANONICAL_PLAN,
    FROZEN_PLAN_SHA256,
    authenticate_frozen_plan,
    sha256_file,
)

WITNESS_SCHEMA = "TESTPOIETIC_CANDIDATE_WITNESS_V1"
RUN_ID = "candidate-witness-001"
SCOPE = "STRUCTURAL_CANDIDATE_WITNESS_AUDIT_ONLY"
RUN_FILES = ("authentication.json", "candidate_audit.json", "provenance_audit.json")
OUTCOMES = (
    "PLAN_AUTHENTICATION_FAILED",
    "WITNESS_SCHEMA_INVALID",
    "EVIDENCE_PACKAGE_INCOMPLETE",
    "PROVENANCE_UNRESOLVED",
    "REFUTATION_RECORDED_ON_DECLARED_DOMAIN",
    "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION",
)
RESPONSE_STATUSES = frozenset(
    {"SATISFIED", "UNSATISFIED", "UNRESOLVED", "NOT_APPLICABLE"}
)
APPLICABILITY = frozenset({"CLAIMED", "NOT_APPLICABLE", "UNASSERTED"})
ATTRIBUTION_CLAIM_TYPES = frozenset({"STRUCTURAL_CANDIDATE_AUDIT"})
CRITICAL_CHANNELS = frozenset(
    {
        "THEORY_LADEN_OBSERVATION",
        "LOGICAL_DEDUCTION",
        "PREDICTED_CONSEQUENCE",
    }
)
CRITICAL_OUTCOMES = frozenset(
    {
        "REFUTED_CONJUNCTION",
        "SURVIVED_DECLARED_ATTEMPT",
        "INTERPRETATION_DISPUTED",
        "INCONCLUSIVE",
    }
)
HISTORY_LOCATIONS = frozenset(
    {
        "CANDIDATE",
        "PARENT",
        "EXTERNAL_BUILDER",
        "EVOLUTIONARY_POPULATION",
        "UNRESOLVED",
    }
)

HISTORY_NODE_TYPES = {
    "CANDIDATE": "CANDIDATE",
    "PARENT": "PARENT",
    "EXTERNAL_BUILDER": "EXTERNAL_BUILDER",
    "EVOLUTIONARY_POPULATION": "POPULATION",
    "UNRESOLVED": "UNRESOLVED_INPUT",
}

PROVENANCE_INPUT_CLASSES = frozenset(
    {
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
    }
)
PROVENANCE_DISCLOSURES = frozenset(
    {"PRESENT", "ABSENT_ON_DECLARED_BOUNDARY", "UNRESOLVED"}
)
PROVENANCE_NODE_TYPES = frozenset(
    {"CANDIDATE", "ENVIRONMENT", "POPULATION", "UNRESOLVED_INPUT", *PROVENANCE_INPUT_CLASSES}
)

CRITICAL_CHAIN_REQUIREMENTS = {
    "THEORY_LADEN_OBSERVATION": frozenset({"INSTRUMENT_OR_SENSE", "CALIBRATION_OR_DATA_REDUCTION", "INFERENCE"}),
    "LOGICAL_DEDUCTION": frozenset({"PREMISE", "DERIVATION", "INFERENCE"}),
    "PREDICTED_CONSEQUENCE": frozenset({"THEORY", "DERIVATION", "INFERENCE"}),
}


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _rows(value: object) -> list[Mapping[str, Any]]:
    return [row for row in value if isinstance(row, Mapping)] if isinstance(value, list) else []


def _string_list(value: object) -> list[str]:
    return value if isinstance(value, list) and all(isinstance(item, str) for item in value) else []


def _valid_string_list(value: object, *, require_nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) and bool(item) for item in value)
        and (bool(value) or not require_nonempty)
    )

def _valid_mapping_rows(value: object, *, require_nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(row, Mapping) for row in value)
        and (bool(value) or not require_nonempty)
    )

def _text_fields(mapping: Mapping[str, Any], names: tuple[str, ...]) -> bool:
    return all(isinstance(mapping.get(name), str) and bool(mapping[name].strip()) for name in names)


def _required(mapping: Mapping[str, Any], names: tuple[str, ...]) -> list[str]:
    return [
        name
        for name in names
        if name not in mapping
        or mapping[name] is None
        or (isinstance(mapping[name], str) and not mapping[name].strip())
    ]


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(character in "0123456789abcdef" for character in value)

def _critical_chain_valid(row: Mapping[str, Any], physical_bearer_ids: set[str]) -> bool:
    chain = row.get("interpretation_chain")
    if not _valid_mapping_rows(chain, require_nonempty=True):
        return False
    roles: set[str] = set()
    for link in _rows(chain):
        if _required(_mapping(link), ("component_id", "role", "failure_mode")):
            return False
        component_id = link.get("component_id")
        if not isinstance(component_id, str) or component_id not in physical_bearer_ids:
            return False
        role = link.get("role")
        if not isinstance(role, str):
            return False
        roles.add(role)
    channel = row.get("channel")
    if not isinstance(channel, str):
        return False
    return CRITICAL_CHAIN_REQUIREMENTS.get(channel, frozenset()).issubset(roles)
def _recipe_task_binding_valid(
    value: object,
    *,
    recipe_knowledge_id: str,
    bearer_ids: set[str],
    record_ids: set[str],
    counterfactual_ids: set[str],
    text_fields: tuple[str, ...],
    list_fields: tuple[str, ...] = (),
    minimum_distinct_attributes: int = 0,
) -> bool:
    """Check a physical, evidence-linked H task bound to one recipe P."""

    binding = _mapping(value)
    attributes = _string_list(binding.get("attributes"))
    return (
        isinstance(value, Mapping)
        and not _required(
            binding,
            (
                "recipe_knowledge_id",
                "bearer_id",
                "evidence_refs",
                "counterfactual_test_ids",
                *text_fields,
                *list_fields,
            ),
        )
        and binding.get("recipe_knowledge_id") == recipe_knowledge_id
        and isinstance(binding.get("bearer_id"), str)
        and binding.get("bearer_id") in bearer_ids
        and _text_fields(binding, text_fields)
        and all(
            _valid_string_list(binding.get(field), require_nonempty=True)
            for field in list_fields
        )
        and _valid_string_list(binding.get("evidence_refs"), require_nonempty=True)
        and set(_string_list(binding.get("evidence_refs"))).issubset(record_ids)
        and _valid_string_list(
            binding.get("counterfactual_test_ids"),
            require_nonempty=True,
        )
        and set(
            _string_list(binding.get("counterfactual_test_ids"))
        ).issubset(counterfactual_ids)
        and (
            not minimum_distinct_attributes
            or len(set(attributes)) >= minimum_distinct_attributes
        )
    )
def _has_directed_path(
    edges: list[Mapping[str, Any]],
    start_id: str,
    target_id: str,
) -> bool:
    """Return whether declared, evidence-backed edges connect start to target."""

    pending = [start_id]
    visited: set[str] = set()
    while pending:
        current = pending.pop()
        if current == target_id:
            return True
        if current in visited:
            continue
        visited.add(current)
        pending.extend(
            edge["target_id"]
            for edge in edges
            if edge.get("source_id") == current
            and isinstance(edge.get("target_id"), str)
        )
    return False


def _record(checks: list[dict[str, object]], identifier: str, passed: bool, detail: str) -> None:
    checks.append({"detail": detail, "id": identifier, "passed": bool(passed)})


def _load_witness(path: Path) -> tuple[Mapping[str, Any], str | None, str | None]:
    try:
        raw = path.read_bytes()
    except OSError:
        return {}, None, "WITNESS_UNREADABLE"
    digest = _sha256_bytes(raw)
    try:
        value = json.loads(raw)
    except UnicodeDecodeError:
        return {}, digest, "WITNESS_UTF8_INVALID"
    except json.JSONDecodeError:
        return {}, digest, "WITNESS_JSON_INVALID"
    return (_mapping(value), digest, None) if isinstance(value, Mapping) else ({}, digest, "WITNESS_JSON_NOT_OBJECT")


def _unique_ids(rows: list[Mapping[str, Any]], key: str) -> tuple[set[str], bool]:
    values = [row.get(key) for row in rows]
    strings = [value for value in values if isinstance(value, str) and value]
    return set(strings), len(strings) == len(rows) and len(set(strings)) == len(rows)


def _audit_packet(
    lattice_id: str,
    packet_value: object,
    plan_lattice: Mapping[str, Any],
    record_ids: set[str],
    object_ids: set[str],
    refuter_ids: set[str],
    declared_domain: str,
) -> tuple[dict[str, object], bool, bool]:
    packet = _mapping(packet_value)
    requirement_ids, requirements_unique = _unique_ids(
        _rows(plan_lattice.get("pass_requirements")),
        "id",
    )
    verdicts = set(_string_list(plan_lattice.get("verdicts")))
    claimed_verdict = packet.get("claimed_verdict")
    applicability = packet.get("applicability")
    responses = _rows(packet.get("responses"))
    response_ids, responses_unique = _unique_ids(responses, "requirement_id")
    response_shape = _valid_mapping_rows(packet.get("responses"), require_nonempty=True)
    response_refs = True
    response_statuses: list[str] = []
    for response in responses:
        missing = _required(
            response,
            ("requirement_id", "status", "assertion", "object_refs", "evidence_refs", "refuter"),
        )
        response_shape = response_shape and not missing
        status = response.get("status")
        response_statuses.append(status if isinstance(status, str) else "")
        evidence_refs = _string_list(response.get("evidence_refs"))
        object_refs = _string_list(response.get("object_refs"))
        response_refs = (
            response_refs
            and _valid_string_list(response.get("object_refs"), require_nonempty=True)
            and _valid_string_list(response.get("evidence_refs"), require_nonempty=True)
            and set(object_refs).issubset(object_ids)
            and set(evidence_refs).issubset(record_ids)
            and isinstance(response.get("assertion"), str)
            and isinstance(response.get("refuter"), str)
            and response.get("refuter") in refuter_ids
        )
    known_claim = isinstance(claimed_verdict, str) and claimed_verdict in verdicts
    status_valid = all(status in RESPONSE_STATUSES for status in response_statuses)
    identifiers_valid = requirements_unique and responses_unique and response_ids == requirement_ids
    basic_valid = (
        isinstance(applicability, str)
        and applicability in APPLICABILITY
        and known_claim
        and identifiers_valid
        and response_shape
        and response_refs
        and status_valid
        and isinstance(packet.get("scope"), str)
        and packet.get("scope") == declared_domain
    )
    if applicability == "NOT_APPLICABLE":
        structural_complete = (
            basic_valid
            and claimed_verdict == "NOT_APPLICABLE"
            and all(status == "NOT_APPLICABLE" for status in response_statuses)
        )
    elif applicability == "CLAIMED":
        structural_complete = basic_valid and all(status == "SATISFIED" for status in response_statuses)
    else:
        structural_complete = False
    return (
        {
            "applicability": applicability if isinstance(applicability, str) else None,
            "claimed_verdict": claimed_verdict if isinstance(claimed_verdict, str) else None,
            "lattice_id": lattice_id,
            "outcome": "STRUCTURALLY_COMPLETE" if structural_complete else "EVIDENCE_PACKAGE_INCOMPLETE",
            "requirement_ids": sorted(requirement_ids),
            "response_ids": sorted(response_ids),
        },
        basic_valid,
        structural_complete,
    )


def _audit_witness(
    witness: Mapping[str, Any],
    plan: Mapping[str, Any],
) -> tuple[dict[str, object], dict[str, object], dict[str, bool]]:
    schema_checks: list[dict[str, object]] = []
    package_checks: list[dict[str, object]] = []
    required_top = (
        "schema",
        "witness_id",
        "pins",
        "attribution",
        "candidate",
        "physical_bearers",
        "evidence_records",
        "knowledge_items",
        "counterfactual_tests",
        "critical_evidence_packages",
        "creation_episodes",
        "provenance_graph",
        "lattices",
    )
    _record(
        schema_checks,
        "TOP_LEVEL_FIELDS",
        not _required(witness, required_top),
        "required witness fields are present",
    )
    _record(
        schema_checks,
        "WITNESS_SCHEMA",
        witness.get("schema") == WITNESS_SCHEMA,
        "witness declares the candidate-witness schema",
    )

    _record(
        schema_checks,
        "WITNESS_ID",
        _text_fields(witness, ("witness_id",)),
        "witness identity is nonempty text",
    )

    attribution = _mapping(witness.get("attribution"))
    attribution_valid = not _required(
        attribution,
        (
            "claim_id",
            "claim_type",
            "target_problem_id",
            "declared_domain",
            "finite_cohort",
            "environment_scope",
            "model_assumptions",
            "excluded_universal_claims",
        ),
    )
    attribution_valid = attribution_valid and _text_fields(
        attribution,
        (
            "claim_id",
            "claim_type",
            "target_problem_id",
            "declared_domain",
            "finite_cohort",
            "environment_scope",
            "model_assumptions",
            "excluded_universal_claims",
        ),
    )
    attribution_valid = (
        attribution_valid
        and attribution.get("claim_type") in ATTRIBUTION_CLAIM_TYPES
    )
    _record(
        schema_checks,
        "NO_CREATIVITY_PROOF_CLAIM",
        attribution.get("claim_type") in ATTRIBUTION_CLAIM_TYPES,
        "the witness may make only the structural, non-attributive claim type",
    )
    _record(
        schema_checks,
        "ATTRIBUTION_SCOPE",
        attribution_valid,
        "the witness limits its claim to a declared finite domain rather than a universal creativity verdict",
    )

    candidate = _mapping(witness.get("candidate"))
    boundary = _mapping(candidate.get("boundary"))
    boundary_fields = (
        "inside_component_ids",
        "outside_component_ids",
        "interface_ids",
        "environment_class",
        "resource_ids",
        "temporal_window",
        "boundary_rationale",
        "alternative_boundaries",
    )
    boundary_valid = (
        not _required(boundary, boundary_fields)
        and all(
            _valid_string_list(boundary.get(name), require_nonempty=True)
            for name in ("inside_component_ids", "outside_component_ids", "interface_ids", "resource_ids", "alternative_boundaries")
        )
        and _text_fields(boundary, ("environment_class", "temporal_window", "boundary_rationale"))
    )
    _record(
        schema_checks,
        "CANDIDATE_BOUNDARY",
        _text_fields(candidate, ("candidate_id",)) and boundary_valid,
        "candidate boundary, environment, resources, and alternatives are declared",
    )

    physical_rows = _rows(witness.get("physical_bearers"))
    bearer_ids, bearers_unique = _unique_ids(physical_rows, "bearer_id")
    physical_valid = (
        _valid_mapping_rows(witness.get("physical_bearers"), require_nonempty=True) and bearers_unique
        and bool(physical_rows)
        and all(
            not _required(row, ("bearer_id", "role", "description", "boundary_status"))
            and _text_fields(row, ("bearer_id", "role", "description", "boundary_status"))
            for row in physical_rows
        )
    )
    _record(
        schema_checks,
        "PHYSICAL_BEARERS",
        physical_valid,
        "physical bearers are declared separately from abstract descriptions",
    )
    boundary_references = set()
    for name in ("inside_component_ids", "outside_component_ids", "interface_ids"):
        boundary_references.update(_string_list(boundary.get(name)))
    _record(
        schema_checks,
        "BOUNDARY_PHYSICAL_REFERENCES",
        physical_valid and boundary_references.issubset(bearer_ids),
        "the declared system boundary refers only to named physical bearers",
    )
    boundary_sets = {
        "INSIDE": set(_string_list(boundary.get("inside_component_ids"))),
        "OUTSIDE": set(_string_list(boundary.get("outside_component_ids"))),
        "INTERFACE": set(_string_list(boundary.get("interface_ids"))),
    }
    inside_component_ids = boundary_sets["INSIDE"]
    physical_boundary_agreement = all(
        isinstance(row.get("bearer_id"), str)
        and isinstance(row.get("boundary_status"), str)
        and row["boundary_status"] in boundary_sets
        and row["bearer_id"] in boundary_sets[row["boundary_status"]]
        for row in physical_rows
    )
    _record(
        schema_checks,
        "PHYSICAL_BOUNDARY_AGREEMENT",
        physical_valid and physical_boundary_agreement,
        "every physical bearer is classified by the declared system boundary",
    )

    evidence_rows = _rows(witness.get("evidence_records"))
    record_ids, records_unique = _unique_ids(evidence_rows, "record_id")
    records_valid = _valid_mapping_rows(witness.get("evidence_records"), require_nonempty=True) and records_unique and all(
        not _required(row, ("record_id", "kind", "artifact_ref", "sha256", "producer", "access_scope"))
        and _text_fields(row, ("record_id", "kind", "artifact_ref", "sha256", "producer", "access_scope"))
        and _is_sha256(row.get("sha256"))
        for row in evidence_rows
    )
    _record(
        schema_checks,
        "RECORD_INDEX",
        bool(evidence_rows) and records_valid,
        "declared record index is content-addressed and unique",
    )

    counterfactual_rows = _rows(witness.get("counterfactual_tests"))
    counterfactual_ids, counterfactual_unique = _unique_ids(counterfactual_rows, "test_id")
    counterfactual_valid = _valid_mapping_rows(witness.get("counterfactual_tests"), require_nonempty=True) and counterfactual_unique and bool(counterfactual_rows) and all(
        not _required(
            row,
            (
                "test_id",
                "baseline",
                "change_or_removal",
                "close_variant",
                "task_success_criterion",
                "permitted_side_effects",
                "environment_class",
                "resource_conditions",
                "predicted_difference",
                "record_refs",
                "finite_domain",
            ),
        )
        and _text_fields(row, ("test_id", "baseline", "change_or_removal", "close_variant", "task_success_criterion", "permitted_side_effects", "environment_class", "resource_conditions", "predicted_difference", "finite_domain"))
        and row.get("finite_domain") == attribution.get("declared_domain")
        and _valid_string_list(row.get("record_refs"), require_nonempty=True)
        and set(_string_list(row.get("record_refs"))).issubset(record_ids)
        for row in counterfactual_rows
    )
    _record(
        package_checks,
        "COUNTERFACTUAL_TESTS",
        counterfactual_valid,
        "counterfactual tests name close variants, task criteria, and finite domains",
    )

    knowledge_rows = _rows(witness.get("knowledge_items"))
    knowledge_ids, knowledge_unique = _unique_ids(knowledge_rows, "knowledge_id")
    knowledge_valid = _valid_mapping_rows(witness.get("knowledge_items"), require_nonempty=True) and knowledge_unique and bool(knowledge_rows) and all(
        not _required(
            row,
            (
                "knowledge_id",
                "role",
                "value_description",
                "bearer_id",
                "task_id",
                "history_location",
                "history_node_id",
                "history_evidence_refs",
                "retention_route_id",
                "counterfactual_test_ids",
            ),
        )
        and _text_fields(row, ("knowledge_id", "role", "value_description", "bearer_id", "task_id", "history_location", "history_node_id", "retention_route_id"))
        and isinstance(row.get("history_location"), str)
        and row.get("history_location") in HISTORY_LOCATIONS
        and isinstance(row.get("bearer_id"), str)
        and row.get("bearer_id") in bearer_ids
        and _valid_string_list(row.get("history_evidence_refs"), require_nonempty=True)
        and set(_string_list(row.get("history_evidence_refs"))).issubset(record_ids)
        and _valid_string_list(row.get("counterfactual_test_ids"), require_nonempty=True)
        and set(_string_list(row.get("counterfactual_test_ids"))).issubset(counterfactual_ids)
        for row in knowledge_rows
    )
    _record(
        package_checks,
        "KNOWLEDGE_LOCATION_AND_RETENTION",
        knowledge_valid,
        "knowledge claims name physical bearers, history, retention, and counterfactual tests",
    )

    critical_rows = _rows(witness.get("critical_evidence_packages"))
    critical_ids, critical_unique = _unique_ids(critical_rows, "package_id")
    _record(
        schema_checks,
        "NO_CONFIRMATION_OUTCOME",
        not any(row.get("outcome") == "CONFIRMED" for row in critical_rows),
        "agreement is never represented as confirmation",
    )
    critical_valid = _valid_mapping_rows(witness.get("critical_evidence_packages"), require_nonempty=True) and critical_unique and bool(critical_rows) and all(
        not _required(
            row,
            (
                "package_id",
                "target_claim_id",
                "problem_id",
                "channel",
                "record_refs",
                "interpretation_chain",
                "auxiliary_claim_ids",
                "initial_condition_ids",
                "rival_or_incompatibility",
                "discriminator",
                "discriminator_id",
                "declared_conjunction",
                "declared_domain",
                "protocol",
                "attempts",
                "revision_event_ids",
                "outcome",
            ),
        )
        and _text_fields(row, ("package_id", "target_claim_id", "problem_id", "channel", "rival_or_incompatibility", "discriminator", "discriminator_id", "declared_conjunction", "declared_domain", "protocol", "outcome"))
        and isinstance(row.get("channel"), str)
        and row.get("channel") in CRITICAL_CHANNELS
        and row.get("problem_id") == attribution.get("target_problem_id")
        and row.get("declared_domain") == attribution.get("declared_domain")
        and isinstance(row.get("outcome"), str)
        and row.get("outcome") in CRITICAL_OUTCOMES
        and _valid_string_list(row.get("record_refs"), require_nonempty=True)
        and set(_string_list(row.get("record_refs"))).issubset(record_ids)
        and _critical_chain_valid(row, bearer_ids)
        and _valid_string_list(row.get("auxiliary_claim_ids"), require_nonempty=True)
        and _valid_string_list(row.get("initial_condition_ids"), require_nonempty=True)
        and _valid_string_list(row.get("attempts"), require_nonempty=True)
        and _valid_string_list(row.get("revision_event_ids"), require_nonempty=True)
        and isinstance(row.get("discriminator_id"), str)
        for row in critical_rows
    )
    _record(
        package_checks,
        "CRITICAL_EVIDENCE_PACKAGES",
        critical_valid,
        "critical packages contain a channel, interpretation chain, auxiliaries, discriminator, and protocol",
    )
    refutation_recorded = critical_valid and any(row.get("outcome") == "REFUTED_CONJUNCTION" for row in critical_rows)

    episodes = _rows(witness.get("creation_episodes"))
    episode_ids, episodes_unique = _unique_ids(episodes, "episode_id")
    episodes_valid = _valid_mapping_rows(witness.get("creation_episodes"), require_nonempty=True) and episodes_unique and bool(episodes) and all(
        not _required(row, ("episode_id", "p1", "proposals", "ee", "p2"))
        and _text_fields(row, ("episode_id", "p1", "ee", "p2"))
        and _valid_mapping_rows(row.get("proposals"), require_nonempty=True)
        and all(
            not _required(
                _mapping(proposal),
                (
                    "proposal_id",
                    "explanatory_content",
                    "origin",
                    "error_domain",
                    "possible_refuter_ids",
                    "critical_package_ids",
                    "revision_route",
                ),
            )
            and _text_fields(_mapping(proposal), ("proposal_id", "explanatory_content", "origin", "error_domain", "revision_route"))
            and _valid_string_list(_mapping(proposal).get("possible_refuter_ids"), require_nonempty=True)
            and _valid_string_list(_mapping(proposal).get("critical_package_ids"), require_nonempty=True)
            and set(_string_list(_mapping(proposal).get("critical_package_ids"))).issubset(critical_ids)
            for proposal in row.get("proposals")
        )
        for row in episodes
    )
    proposal_rows = [
        proposal
        for episode in episodes
        for proposal in _rows(episode.get("proposals"))
    ]
    proposal_ids, proposals_unique = _unique_ids(proposal_rows, "proposal_id")
    critical_by_id = {
        row["package_id"]: row
        for row in critical_rows
        if isinstance(row.get("package_id"), str)
    }
    trace_links_valid = proposals_unique and bool(proposal_rows)
    for proposal in proposal_rows:
        package_ids = _string_list(proposal.get("critical_package_ids"))
        possible_refuters = set(_string_list(proposal.get("possible_refuter_ids")))
        linked_packages = [critical_by_id.get(package_id) for package_id in package_ids]
        revision_ids: set[str] = set()
        for package in linked_packages:
            if package is not None:
                revision_ids.update(_string_list(package.get("revision_event_ids")))
        trace_links_valid = (
            trace_links_valid
            and all(package is not None for package in linked_packages)
            and all(package.get("target_claim_id") == proposal.get("proposal_id") for package in linked_packages if package is not None)
            and any(isinstance(package.get("discriminator_id"), str) and package.get("discriminator_id") in possible_refuters for package in linked_packages if package is not None)
            and proposal.get("revision_route") in revision_ids
        )
    episodes_valid = episodes_valid and trace_links_valid
    _record(
        package_checks,
        "P1_TT_EE_P2_TRACE",
        episodes_valid,
        "episodes declare problems, tentative explanations, error elimination, and revised problems",
    )

    provenance = _mapping(witness.get("provenance_graph"))
    nodes = _rows(provenance.get("nodes"))
    node_ids, nodes_unique = _unique_ids(nodes, "node_id")
    node_type_by_id = {
        row["node_id"]: row.get("node_type")
        for row in nodes
        if isinstance(row.get("node_id"), str)
    }
    edges = _rows(provenance.get("edges"))
    disclosure = _mapping(provenance.get("input_class_disclosure"))
    disclosure_valid = (
        set(disclosure) == PROVENANCE_INPUT_CLASSES
        and all(
            isinstance(value, str) and value in PROVENANCE_DISCLOSURES
            for value in disclosure.values()
        )
    )
    present_classes = {
        input_class
        for input_class, status in disclosure.items()
        if status == "PRESENT"
    }
    unresolved_classes = {
        input_class
        for input_class, status in disclosure.items()
        if status == "UNRESOLVED"
    }
    candidate_id = candidate.get("candidate_id") if isinstance(candidate.get("candidate_id"), str) else ""
    present_node_ids = {
        node_id
        for node_id, node_type in node_type_by_id.items()
        if node_type in present_classes
    }
    unresolved_inputs = _string_list(provenance.get("unresolved_input_ids"))
    unresolved_inputs_typed = all(
        node_type_by_id.get(node_id) == "UNRESOLVED_INPUT"
        for node_id in unresolved_inputs
    )
    edges_valid = (
        _valid_mapping_rows(provenance.get("edges"))
        and len(edges) == len(provenance.get("edges"))
        and all(
            not _required(edge, ("source_id", "target_id", "relation", "evidence_refs"))
            and _text_fields(edge, ("source_id", "target_id", "relation"))
            and edge.get("source_id") in node_ids
            and edge.get("target_id") in node_ids
            and _valid_string_list(edge.get("evidence_refs"), require_nonempty=True)
            and set(_string_list(edge.get("evidence_refs"))).issubset(record_ids)
            for edge in edges
        )
    )
    present_paths_valid = bool(candidate_id) and all(
        _has_directed_path(edges, node_id, candidate_id)
        for node_id in present_node_ids
    )
    provenance_valid = (
        nodes_unique
        and _valid_mapping_rows(provenance.get("nodes"), require_nonempty=True)
        and bool(nodes)
        and all(
            not _required(row, ("node_id", "node_type"))
            and _text_fields(row, ("node_id", "node_type"))
            and row.get("node_type") in PROVENANCE_NODE_TYPES
            for row in nodes
        )
        and edges_valid
        and disclosure_valid
        and present_classes.issubset(
            {row.get("node_type") for row in nodes if isinstance(row.get("node_type"), str)}
        )
        and present_paths_valid
        and _valid_string_list(provenance.get("unresolved_input_ids"))
        and len(set(unresolved_inputs)) == len(unresolved_inputs)
        and set(unresolved_inputs).issubset(node_ids)
        and unresolved_inputs_typed
        and (not unresolved_classes or bool(unresolved_inputs))
        and any(
            row.get("node_type") == "CANDIDATE" and row.get("node_id") == candidate_id
            for row in nodes
        )
    )
    _record(
        schema_checks,
        "PROVENANCE_GRAPH",
        provenance_valid,
        "provenance names candidate and external-input nodes without dereferencing them",
    )
    _record(
        schema_checks,
        "PROVENANCE_PRESENT_INPUT_PATHS",
        present_paths_valid,
        "each declared present input has an evidence-backed path to the candidate",
    )
    _record(
        schema_checks,
        "UNRESOLVED_INPUT_TYPES",
        unresolved_inputs_typed,
        "each unresolved input resolves to an explicitly typed unresolved node",
    )
    provenance_references_valid = (
        all(
            isinstance(row.get("producer"), str)
            and row.get("producer") in node_ids
            and row.get("producer") in bearer_ids
            for row in evidence_rows
        )
        and all(
            isinstance(proposal.get("origin"), str)
            and proposal.get("origin") in node_ids
            and proposal.get("origin") in bearer_ids
            for proposal in proposal_rows
        )
        and all(
            isinstance(row.get("history_node_id"), str)
            and row.get("history_node_id") in node_ids
            and row.get("history_node_id") in bearer_ids
            and isinstance(row.get("history_location"), str)
            and node_type_by_id.get(row.get("history_node_id"))
            == HISTORY_NODE_TYPES.get(row.get("history_location"))
            for row in knowledge_rows
        )
        and present_node_ids.issubset(bearer_ids)
    )
    _record(
        schema_checks,
        "PROVENANCE_REFERENCES",
        provenance_references_valid,
        "records, proposals, and knowledge histories resolve to typed physical provenance nodes",
    )
    _record(
        schema_checks,
        "CANDIDATE_PHYSICAL_ID",
        physical_valid and candidate.get("candidate_id") in bearer_ids,
        "the candidate itself is one of the declared physical bearers",
    )
    external_or_unknown_knowledge = any(
        row.get("history_location") != "CANDIDATE"
        and (
            not isinstance(row.get("history_node_id"), str)
            or row.get("history_node_id") not in inside_component_ids
        )
        for row in knowledge_rows
    )
    external_or_unknown_proposals = any(
        not isinstance(proposal.get("origin"), str)
        or proposal.get("origin") not in inside_component_ids
        for proposal in proposal_rows
    )

    refuter_ids = {
        row.get("discriminator_id")
        for row in critical_rows
        if isinstance(row.get("discriminator_id"), str)
    }
    for proposal in proposal_rows:
        refuter_ids.update(_string_list(proposal.get("possible_refuter_ids")))

    plan_lattices = _mapping(plan.get("lattices"))
    packets = _mapping(witness.get("lattices"))
    lattice_audits: list[dict[str, object]] = []
    packet_schema_valid = True
    complete_by_lattice: dict[str, bool] = {}
    for lattice_id in sorted(plan_lattices):
        audit, basic_valid, complete = _audit_packet(
            lattice_id,
            packets.get(lattice_id),
            _mapping(plan_lattices.get(lattice_id)),
            record_ids,
            bearer_ids,
            refuter_ids,
            attribution.get("declared_domain")
            if isinstance(attribution.get("declared_domain"), str)
            else "",
        )
        lattice_audits.append(audit)
        packet_schema_valid = packet_schema_valid and basic_valid
        complete_by_lattice[lattice_id] = complete
    _record(
        package_checks,
        "LATTICE_PACKETS",
        set(packets) == set(plan_lattices) and packet_schema_valid,
        "each frozen-plan requirement has exactly one declared witness response",
    )

    critical_packet = _mapping(packets.get("critical_evidence"))
    critical_claimed_verdict = critical_packet.get("claimed_verdict")
    critical_outcome_alignment = (
        critical_packet.get("applicability") != "CLAIMED"
        or (
            isinstance(critical_claimed_verdict, str)
            and any(row.get("outcome") == critical_claimed_verdict for row in critical_rows)
        )
    )
    _record(
        package_checks,
        "CRITICAL_OUTCOME_ALIGNMENT",
        critical_outcome_alignment,
        "the critical-evidence lattice declares the same outcome as an evidence package",
    )
    if complete_by_lattice.get("critical_evidence") and not critical_outcome_alignment:
        complete_by_lattice["critical_evidence"] = False
    refutation_recorded = refutation_recorded and critical_outcome_alignment

    replication = _mapping(witness.get("replication_claim"))
    h_packet = _mapping(packets.get("no_design_replication"))
    recipe_knowledge_id = replication.get("recipe_knowledge_id")
    recipe_id = recipe_knowledge_id if isinstance(recipe_knowledge_id, str) else ""
    if h_packet.get("applicability") == "CLAIMED":
        digital_variable_valid = _recipe_task_binding_valid(
            replication.get("digital_unit_variable"),
            recipe_knowledge_id=recipe_id,
            bearer_ids=bearer_ids,
            record_ids=record_ids,
            counterfactual_ids=counterfactual_ids,
            text_fields=("variable_id", "nonallowed_value_separation"),
            list_fields=("attributes",),
            minimum_distinct_attributes=2,
        )
        detection_valid = _recipe_task_binding_valid(
            replication.get("error_detection_task"),
            recipe_knowledge_id=recipe_id,
            bearer_ids=bearer_ids,
            record_ids=record_ids,
            counterfactual_ids=counterfactual_ids,
            text_fields=("task_id", "criterion"),
        )
        correction_valid = _recipe_task_binding_valid(
            replication.get("error_correction_task"),
            recipe_knowledge_id=recipe_id,
            bearer_ids=bearer_ids,
            record_ids=record_ids,
            counterfactual_ids=counterfactual_ids,
            text_fields=("task_id", "criterion"),
        )
        blind_copying_valid = _recipe_task_binding_valid(
            replication.get("blind_copying"),
            recipe_knowledge_id=recipe_id,
            bearer_ids=bearer_ids,
            record_ids=record_ids,
            counterfactual_ids=counterfactual_ids,
            text_fields=("task_id",),
            list_fields=("modular_unit_ids",),
        )
        replication_valid = (
            not _required(
                replication,
                (
                    "accuracy_measure",
                    "no_design_basis",
                    "generic_resources",
                    "recipe_knowledge_id",
                    "digital_unit_variable",
                    "error_detection_task",
                    "error_correction_task",
                    "blind_copying",
                    "vehicle_boundary",
                    "evidence_refs",
                ),
            )
            and h_packet.get("claimed_verdict") == "MAY_PASS"
            and _text_fields(
                replication,
                ("accuracy_measure", "no_design_basis", "generic_resources"),
            )
            and recipe_id in knowledge_ids
            and isinstance(replication.get("vehicle_boundary"), str)
            and replication.get("vehicle_boundary") in bearer_ids
            and _valid_string_list(
                replication.get("evidence_refs"),
                require_nonempty=True,
            )
            and set(
                _string_list(replication.get("evidence_refs"))
            ).issubset(record_ids)
            and digital_variable_valid
            and detection_valid
            and correction_valid
            and blind_copying_valid
        )
    elif h_packet.get("applicability") == "NOT_APPLICABLE":
        replication_valid = h_packet.get("claimed_verdict") == "NOT_APPLICABLE"
    else:
        replication_valid = False
    _record(
        package_checks,
        "CONDITIONAL_REPLICATION_SCOPE",
        replication_valid,
        "digital error correction is checked only for a claimed high-accuracy no-design reproduction task",
    )

    selection_rows = _rows(witness.get("selection_processes"))
    selection_valid = (
        _valid_mapping_rows(witness.get("selection_processes"), require_nonempty=True) and bool(selection_rows)
        and all(
            not _required(
                row,
                (
                    "population_boundary",
                    "lineage",
                    "inheritance",
                    "viable_offspring_criterion",
                    "variation_mechanism",
                    "nonspecificity_evidence",
                    "not_guaranteed_in_advance",
                    "finite_resource_environment",
                    "differential_continuation_records",
                    "bridge_role",
                ),
            )
            and _text_fields(
                row,
                (
                    "population_boundary",
                    "lineage",
                    "inheritance",
                    "viable_offspring_criterion",
                    "variation_mechanism",
                    "nonspecificity_evidence",
                    "not_guaranteed_in_advance",
                    "finite_resource_environment",
                    "bridge_role",
                ),
            )
            and _valid_string_list(
                row.get("differential_continuation_records"),
                require_nonempty=True,
            )
            and set(
                _string_list(row.get("differential_continuation_records"))
            ).issubset(record_ids)
            and row.get("bridge_role") == "TYPED_FALLIBILITY_ANALOGUE_ONLY"
            for row in selection_rows
        )
    )
    _record(
        package_checks,
        "TYPED_SELECTION_BRIDGE",
        selection_valid,
        "selection is declared as a typed fallibility analogue, not represented criticism",
    )

    if external_or_unknown_knowledge:
        for audit in lattice_audits:
            if audit["lattice_id"] == "knowledge_retention":
                audit["outcome"] = "EXTERNAL_P_NOT_ATTRIBUTED"
    if external_or_unknown_proposals:
        for audit in lattice_audits:
            if audit["lattice_id"] == "explanatory_creativity":
                audit["outcome"] = "PROVENANCE_UNRESOLVED"
    if complete_by_lattice.get("critical_evidence") and not critical_valid:
        complete_by_lattice["critical_evidence"] = False
    if complete_by_lattice.get("explanatory_creativity") and not (complete_by_lattice.get("critical_evidence") and critical_valid and episodes_valid):
        complete_by_lattice["explanatory_creativity"] = False
    if complete_by_lattice.get("knowledge_retention") and not (knowledge_valid and counterfactual_valid):
        complete_by_lattice["knowledge_retention"] = False
    if complete_by_lattice.get("no_design_replication") and not replication_valid:
        complete_by_lattice["no_design_replication"] = False
    if complete_by_lattice.get("evolutionary_selection") and not selection_valid:
        complete_by_lattice["evolutionary_selection"] = False

    for audit in lattice_audits:
        if (
            not complete_by_lattice.get(audit["lattice_id"])
            and audit["outcome"] == "STRUCTURALLY_COMPLETE"
        ):
            audit["outcome"] = "EVIDENCE_PACKAGE_INCOMPLETE"

    package_complete = (
        all(check["passed"] for check in package_checks)
        and all(complete_by_lattice.values())
    )
    schema_valid = all(check["passed"] for check in schema_checks)
    candidate_audit = {
        "attribution": dict(attribution),
        "refutation_scopes": [
            {"declared_conjunction": row.get("declared_conjunction"), "declared_domain": row.get("declared_domain"), "target_claim_id": row.get("target_claim_id")}
            for row in critical_rows
            if row.get("outcome") == "REFUTED_CONJUNCTION"
        ],
        "lattices": lattice_audits,
        "package_checks": package_checks,
        "package_complete": package_complete,
        "run_id": RUN_ID,
        "schema_checks": schema_checks,
        "scope": SCOPE,
    }
    provenance_audit = {
        "external_or_unknown_knowledge": external_or_unknown_knowledge,
        "external_or_unknown_proposals": external_or_unknown_proposals,
        "input_class_disclosure": dict(disclosure),
        "knowledge_ids": sorted(knowledge_ids),
        "node_ids": sorted(node_ids),
        "provenance_valid": provenance_valid,
        "run_id": RUN_ID,
        "scope": SCOPE,
        "unresolved_input_ids": unresolved_inputs,
    }
    return candidate_audit, provenance_audit, {
        "package_complete": package_complete,
        "provenance_unresolved": (
            external_or_unknown_knowledge
            or external_or_unknown_proposals
            or bool(unresolved_inputs)
            or bool(unresolved_classes)
            or not provenance_valid
        ),
        "refutation_recorded": refutation_recorded,
        "schema_valid": schema_valid,
    }


def evaluate_candidate(
    witness_path: Path,
    output_directory: Path,
    *,
    plan_path: Path = CANONICAL_PLAN,
    subject_sha256: str = PRIMARY_SHA256,
) -> dict[str, object]:
    """Audit a witness package structurally; never issue a creativity verdict."""

    plan, plan_report = authenticate_frozen_plan(plan_path, subject_sha256)
    witness, witness_sha256, witness_error = _load_witness(witness_path)
    pins = _mapping(witness.get("pins"))
    authentication_checks: list[dict[str, object]] = []
    _record(
        authentication_checks,
        "FROZEN_PLAN_AUTHENTICATED",
        bool(plan_report["authenticated"]),
        "the supplied plan matches the reviewed frozen digest and integrity checks",
    )
    _record(
        authentication_checks,
        "WITNESS_READABLE",
        witness_error is None,
        witness_error or "witness JSON object loaded",
    )
    _record(
        authentication_checks,
        "WITNESS_SUBJECT_PIN",
        pins.get("subject_sha256") == subject_sha256,
        "witness subject pin matches the supplied subject",
    )
    _record(
        authentication_checks,
        "WITNESS_PLAN_SCHEMA_PIN",
        pins.get("plan_schema") == plan.get("schema"),
        "witness plan-schema pin matches the authenticated plan",
    )
    _record(
        authentication_checks,
        "WITNESS_PLAN_DIGEST_PIN",
        pins.get("plan_sha256") == FROZEN_PLAN_SHA256,
        "witness plan digest pin matches the reviewed freeze",
    )
    authentication = {
        "checks": authentication_checks,
        "plan_authentication": plan_report["authentication"],
        "plan_audit": plan_report["plan_audit"],
        "negative_controls": plan_report["negative_controls"],
        "frozen_plan_authenticated": bool(plan_report["authenticated"]),
        "run_id": RUN_ID,
        "scope": SCOPE,
        "witness_sha256": witness_sha256,
    }
    candidate_audit, provenance_audit, flags = _audit_witness(witness, plan)
    frozen_plan_authenticated = bool(authentication_checks[0]["passed"])
    witness_authentication_valid = all(check["passed"] for check in authentication_checks[1:])
    if not frozen_plan_authenticated:
        outcome = "PLAN_AUTHENTICATION_FAILED"
    elif not witness_authentication_valid or not flags["schema_valid"]:
        outcome = "WITNESS_SCHEMA_INVALID"
    elif flags["refutation_recorded"]:
        outcome = "REFUTATION_RECORDED_ON_DECLARED_DOMAIN"
    elif flags["provenance_unresolved"]:
        outcome = "PROVENANCE_UNRESOLVED"
    elif not flags["package_complete"]:
        outcome = "EVIDENCE_PACKAGE_INCOMPLETE"
    else:
        outcome = "STRUCTURALLY_AUDITED_NO_CREATIVITY_ATTRIBUTION"

    payload = {
        "authentication.json": authentication,
        "candidate_audit.json": candidate_audit,
        "provenance_audit.json": provenance_audit,
    }
    output_directory.mkdir(parents=True, exist_ok=True)
    for name in RUN_FILES:
        (output_directory / name).write_bytes(_json_bytes(payload[name]))
    files = [
        {
            "bytes": (output_directory / name).stat().st_size,
            "path": name,
            "sha256": sha256_file(output_directory / name),
        }
        for name in RUN_FILES
    ]
    manifest = {
        "files": files,
        "outcome": outcome,
        "run_id": RUN_ID,
        "scope": SCOPE,
        "warning": (
            "This is a structural witness audit only. It does not dereference evidence, "
            "confirm a theory, or attribute creativity."
        ),
    }
    (output_directory / "manifest.json").write_bytes(_json_bytes(manifest))
    return manifest
