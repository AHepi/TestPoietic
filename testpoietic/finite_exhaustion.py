"""Deterministic finite witnesses for selected Spark--Poietic claims.

The functions in this module are deliberately small, stdlib-only model
checkers.  Their outputs are criteria/result objects suitable for canonical
JSON serialization.  A bounded survivor is not promoted into a universal
claim: each result states the exact finite population or countermodel it
observes.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations, product
import json
from typing import Iterable


@dataclass(frozen=True)
class _Transition:
    edges: frozenset[tuple[str, str]]
    node_types: tuple[tuple[str, str], ...]
    resistant_outcome: bool = True
    criterion_current: bool = True
    criterion_licenses: bool = True
    permission_open: bool = True
    outcome_affects_award: bool = True

    def types(self) -> dict[str, str]:
        return dict(self.node_types)


_STAGES = ("construct", "candidate", "exposure", "outcome", "award", "role")
_G1_SOURCE_TYPES = {
    "held",
    "seed",
    "target_record",
    "environment_record",
    "external_raw",
}
_W3_NAMED_SOURCE_TYPES = {"held", "seed", "target_record", "external_raw"}


def _reachable(
    edges: frozenset[tuple[str, str]],
    start: str,
    goal: str,
    forbidden: frozenset[str] = frozenset(),
) -> bool:
    if start in forbidden or goal in forbidden:
        return False
    pending = [start]
    seen = {start}
    while pending:
        current = pending.pop()
        if current == goal:
            return True
        for source, target in edges:
            if source != current or target in forbidden or target in seen:
                continue
            seen.add(target)
            pending.append(target)
    return False


def _all_paths_pass(
    edges: frozenset[tuple[str, str]], start: str, goal: str, required: str
) -> bool:
    """Return whether ``required`` dominates every finite start-to-goal path."""

    if not _reachable(edges, start, goal):
        return True
    return not _reachable(edges, start, goal, frozenset({required}))


def _w3_check(transition: _Transition) -> tuple[bool, list[str]]:
    node_types = transition.types()
    reasons: list[str] = []
    if not all(stage in node_types for stage in _STAGES):
        reasons.append("W3_STAGE_TOKENS")
    for node, node_type in node_types.items():
        if node_type not in _W3_NAMED_SOURCE_TYPES:
            continue
        if _reachable(transition.edges, node, "role") and not _all_paths_pass(
            transition.edges, node, "role", "construct"
        ):
            reasons.append(f"W3_SOURCE_BYPASS:{node}")
    for required in ("exposure", "outcome", "award"):
        if not _all_paths_pass(transition.edges, "candidate", "role", required):
            reasons.append(f"W3_CANDIDATE_BYPASS:{required}")
    if not transition.resistant_outcome:
        reasons.append("W3_NO_RESISTANT_INTERFACE")
    if ("outcome", "award") not in transition.edges:
        reasons.append("W3_NO_AWARD_RELEVANT_OUTCOME_PATH")
    unique_reasons = sorted(set(reasons))
    return not unique_reasons, unique_reasons


def _a5_check(transition: _Transition) -> tuple[bool, list[str]]:
    node_types = transition.types()
    reasons: list[str] = []
    indegree = {node: 0 for node in node_types}
    for source, target in transition.edges:
        indegree.setdefault(source, 0)
        indegree[target] = indegree.get(target, 0) + 1
    for node, degree in indegree.items():
        if degree != 0 or not _reachable(transition.edges, node, "construct"):
            continue
        node_type = node_types[node]
        if node_type not in _G1_SOURCE_TYPES:
            reasons.append(f"G1_UNAUTHORIZED_SOURCE:{node}:{node_type}")
    if not transition.resistant_outcome or not transition.outcome_affects_award:
        reasons.append("G2_NO_CONSEQUENTIAL_AWARD_DEPENDENCE")
    for required in ("exposure", "outcome", "award"):
        if not _all_paths_pass(transition.edges, "candidate", "role", required):
            reasons.append(f"G2_G3_MEDIATION_BYPASS:{required}")
    if not transition.criterion_current:
        reasons.append("G3_STALE_OR_ABSENT_CRITERION")
    if not transition.criterion_licenses:
        reasons.append("G3_UNLICENSED")
    if not transition.permission_open:
        reasons.append("G3_CHANNEL_CLOSED")
    for node, node_type in node_types.items():
        if node_type != "external_raw":
            continue
        if _reachable(transition.edges, node, "role") and not _all_paths_pass(
            transition.edges, node, "role", "construct"
        ):
            reasons.append("G4_DIRECT_EXTERNAL_INSERTION")
    unique_reasons = sorted(set(reasons))
    return not unique_reasons, unique_reasons


def transition_mutation_evidence() -> dict[str, object]:
    """Run isolated structural and semantic transition mutations."""

    node_types = {
        "held": "held",
        "target": "target_record",
        "external": "external_raw",
        "construct": "stage",
        "candidate": "stage",
        "exposure": "stage",
        "outcome": "stage",
        "award": "stage",
        "role": "stage",
        "criterion": "control",
        "permission": "control",
        "scheduler": "control",
    }
    edges = {
        ("held", "construct"),
        ("target", "construct"),
        ("external", "construct"),
        ("construct", "candidate"),
        ("candidate", "exposure"),
        ("exposure", "outcome"),
        ("outcome", "award"),
        ("award", "role"),
        ("criterion", "award"),
        ("permission", "role"),
        ("scheduler", "role"),
    }
    control = _Transition(frozenset(edges), tuple(sorted(node_types.items())))
    hidden_types = dict(node_types)
    hidden_types["hidden_answer"] = "internal_unheld_answer"

    cases: tuple[tuple[str, _Transition], ...] = (
        ("CONTROL", control),
        (
            "HIDDEN_INTERNAL_ANSWER",
            replace(
                control,
                edges=frozenset(edges | {("hidden_answer", "construct")}),
                node_types=tuple(sorted(hidden_types.items())),
            ),
        ),
        ("STALE_CRITERION", replace(control, criterion_current=False)),
        ("UNLICENSED_AWARD", replace(control, criterion_licenses=False)),
        ("CLOSED_PERMISSION", replace(control, permission_open=False)),
        ("OUTCOME_IGNORED", replace(control, outcome_affects_award=False)),
        ("NONRESISTANT_OUTCOME", replace(control, resistant_outcome=False)),
        (
            "CANDIDATE_WRITE_BYPASS",
            replace(control, edges=frozenset(edges | {("candidate", "role")})),
        ),
        (
            "DIRECT_EXTERNAL_WRITE",
            replace(control, edges=frozenset(edges | {("external", "role")})),
        ),
    )
    rows: list[dict[str, object]] = []
    for case_id, case in cases:
        w3, w3_reasons = _w3_check(case)
        a5, a5_reasons = _a5_check(case)
        rows.append(
            {
                "case_id": case_id,
                "w3": w3,
                "a5": a5,
                "w3_reasons": w3_reasons,
                "a5_reasons": a5_reasons,
            }
        )
    return {
        "claim": "structural W3 is not sufficient for semantic A5",
        "subject_lines": [321, 330, 853, 1231, 1263, 1273],
        "observable": "per-case W3/A5 booleans and exact reason codes",
        "defined_case_ids": [case_id for case_id, _ in cases],
        "executed_case_ids": [row["case_id"] for row in rows],
        "rows": rows,
    }


def transition_semantic_exhaustion() -> dict[str, object]:
    """Exhaust five semantic dimensions not fixed by a stage-only W3 graph."""

    dimensions = [
        "hidden_internal_answer",
        "criterion_current",
        "criterion_licenses",
        "permission_open",
        "outcome_affects_award",
    ]
    rows: list[dict[str, object]] = []
    for hidden, current, licensed, permission, affects in product(
        (False, True), repeat=5
    ):
        a5 = not hidden and current and licensed and permission and affects
        rows.append(
            {
                "hidden_internal_answer": hidden,
                "criterion_current": current,
                "criterion_licenses": licensed,
                "permission_open": permission,
                "outcome_affects_award": affects,
                "w3_structural": True,
                "a5_semantic": a5,
            }
        )
    mismatches = [row for row in rows if not row["a5_semantic"]]
    return {
        "population_equation": "assignments = {False,True}^5",
        "dimensions": dimensions,
        "assignment_count": len(rows),
        "w3_true_a5_false_count": len(mismatches),
        "w3_true_a5_true_count": len(rows) - len(mismatches),
        "observable": "exact 32-row Boolean population and mismatch partition",
        "rows": rows,
    }


def _nonempty_subsets(items: Iterable[int]) -> Iterable[frozenset[int]]:
    values = tuple(items)
    for size in range(1, len(values) + 1):
        for selection in combinations(values, size):
            yield frozenset(selection)


def p31_exhaustion(max_universe: int = 5) -> dict[str, object]:
    """Exhaust two-code-attribute P3.1 instances through ``max_universe``.

    An attribute-level task is well formed exactly when overlapping input
    faces do not demand distinct disjoint output attributes.
    """

    if max_universe < 2:
        raise ValueError("max_universe must be at least 2")
    full_models = 0
    full_counterexamples: list[tuple[object, ...]] = []
    weak_counterexamples: list[tuple[object, ...]] = []
    for universe_size in range(2, max_universe + 1):
        universe = frozenset(range(universe_size))
        subsets = tuple(_nonempty_subsets(universe))
        for x0 in subsets:
            for x1 in subsets:
                if x0 & x1:
                    continue
                attributes = (x0, x1)
                code_region = x0 | x1
                for corrected in (0, 1):
                    corrected_attribute = attributes[corrected]
                    for recovery in subsets:
                        if not recovery - corrected_attribute:
                            continue

                        def well_formed(protected: set[int]) -> bool:
                            faces = [
                                (attributes[index], index) for index in protected
                            ]
                            faces.append((recovery, corrected))
                            return all(
                                not (left & right) or left_output == right_output
                                for left, left_output in faces
                                for right, right_output in faces
                            )

                        witness = (
                            universe_size,
                            tuple(tuple(sorted(attribute)) for attribute in attributes),
                            corrected,
                            tuple(sorted(recovery)),
                        )
                        if well_formed({0, 1}):
                            full_models += 1
                            if not recovery - code_region:
                                full_counterexamples.append(witness)
                        if well_formed({corrected}) and not recovery - code_region:
                            weak_counterexamples.append(witness)
    weak_counterexamples.sort(
        key=lambda row: (
            row[0],
            sum(len(attribute) for attribute in row[1]),
            len(row[3]),
            row[1],
            row[2],
            row[3],
        )
    )
    minimal = weak_counterexamples[0]
    return {
        "claim": "P3.1 full-code protection forces recovery outside the code region",
        "subject_lines": [1144, 1150],
        "universe_size_range": [2, max_universe],
        "code_attribute_count": 2,
        "full_premise_model_count": full_models,
        "full_premise_counterexample_count": len(full_counterexamples),
        "weak_premise_counterexample_count": len(weak_counterexamples),
        "minimal_weak_counterexample": {
            "universe_size": minimal[0],
            "attributes": [list(attribute) for attribute in minimal[1]],
            "corrected_attribute_index": minimal[2],
            "recovery_domain": list(minimal[3]),
        },
        "observable": (
            "exact model counts and the lexicographically minimal historical-mutant "
            "counterexample under the declared enumeration"
        ),
        "scope": "bounded exhaustion supplements but does not replace the general proof",
    }


def p36_one_mastery_control(copy_bound: int = 4) -> dict[str, object]:
    """Enumerate the one-U control model used by P3.6."""

    if copy_bound < 0:
        raise ValueError("copy_bound must be non-negative")
    rows: list[dict[str, object]] = []
    both_capabilities: list[dict[str, object]] = []
    for mastery_value in (0, 1):
        for copies0 in range(copy_bound + 1):
            for copies1 in range(copy_bound + 1):
                m0 = mastery_value == 0 and copies0 > 0
                m1 = mastery_value == 1 and copies1 > 0
                row = {
                    "mastery": f"u{mastery_value}",
                    "copies_0": copies0,
                    "copies_1": copies1,
                    "m0_current": m0,
                    "m1_current": m1,
                }
                rows.append(row)
                if m0 and m1:
                    both_capabilities.append(row)
    return {
        "claim": "finite classical copies do not duplicate one disjoint mastery bearer",
        "subject_lines": [1195, 1201],
        "copy_bound": copy_bound,
        "state_count": len(rows),
        "both_capabilities_state_count": len(both_capabilities),
        "observable": "no enumerated state simultaneously carries m0 and m1",
        "rows": rows,
        "scope": "the general obstruction is the unique U bearer, not the copy bound",
    }


def capstone_literal_witness() -> dict[str, object]:
    """Expose vacuity when successor obligations quantify only selected edges."""

    model = {
        "states": ["s0"],
        "selected_transition_edges": [],
        "creative_capacity_s0": True,
        "initial_open_problem_s0": True,
        "physically_possible_good_member_s0": True,
        "extension_ready_task_s0": True,
        "r_p0": True,
        "r_p_plus_over_selected_history": True,
        "r_s": True,
        "r_x": True,
        "all_selected_transitions_joint_w0_w5": True,
        "all_selected_role_writes_a5_and_growth": True,
    }
    BooleanValue = bool
    displayed_predicates = [
        value for value in model.values() if isinstance(value, BooleanValue)
    ]
    all_predicates_true = all(displayed_predicates)
    length_one_prefix = bool(model["selected_transition_edges"])
    return {
        "claim": "the finite-prefix antecedent supplies a non-vacuous successor",
        "subject_lines": [1432, 1454],
        "model": model,
        "all_displayed_predicates_true_under_universal_reading": all_predicates_true,
        "length_one_prefix_exists": length_one_prefix,
        "literal_countermodel": all_predicates_true and not length_one_prefix,
        "needed_clause": (
            "At every selected cut, the residue witnesses and joint package determine "
            "at least one selected target-essential A5 explanatory-growth successor."
        ),
        "observable": "all Boolean antecedents true while selected edge set is empty",
        "scope": "quantifier under-specification, not a countermodel to the intended reading",
    }


def f2_mutation_matrix() -> dict[str, object]:
    """Return the complete isolated mutation population for an F2 interpreter."""

    rows = [
        {
            "mutation_id": "BATTERY_ID_CHANGED_OUTPUTS_EQUAL",
            "expected_gate": "C2-P1",
            "expected_outcome": "REJECT",
            "mechanism": "coincident output equality does not establish instrument identity",
        },
        {
            "mutation_id": "LOSSY_POST_OUTCOME_TRANSPORT",
            "expected_gate": "C2-P1",
            "expected_outcome": "REJECT",
            "mechanism": "a distinguishing demand lies in the transport loss set",
        },
        {
            "mutation_id": "CONSTANT_IOTA",
            "expected_gate": "C2-P2",
            "expected_outcome": "REJECT",
            "mechanism": "the predicted rank map is degenerate",
        },
        {
            "mutation_id": "HELDOUT_TARGET_ID_IN_IOTA",
            "expected_gate": "C2-P2",
            "expected_outcome": "REJECT",
            "mechanism": "held-out identity leaks into the prediction map",
        },
        {
            "mutation_id": "REVERSED_TRANSMISSION_WITH_P1_P2_TRUE",
            "expected_gate": "C2",
            "expected_outcome": "REFUTE_ON_DECLARED_DOMAIN",
            "mechanism": "field prediction fails after both admissibility gates survive",
        },
    ]
    return {
        "subject_lines": [444, 463, 1594],
        "population_equation": "all_mutations = five named distinct mechanisms",
        "defined_mutation_ids": [row["mutation_id"] for row in rows],
        "observable": "exact first gate and outcome for every mutation",
        "rows": rows,
    }


def _bitstrings(width: int) -> list[str]:
    return [format(value, f"0{width}b") for value in range(2**width)]


def _fringe_cost(target: str, test_cost: int = 1, edit_cost: int = 1) -> tuple[int, int]:
    candidate = ["0"] * len(target)
    cost = 0
    localization_count = 0
    while True:
        cost += test_cost
        mismatch = [
            index
            for index, (actual, wanted) in enumerate(zip(candidate, target))
            if actual != wanted
        ]
        if not mismatch:
            return cost, localization_count
        localization_count += 1
        candidate[mismatch[0]] = target[mismatch[0]]
        cost += edit_cost


def _library_cost(
    target: str,
    order: Iterable[str],
    test_cost: int = 1,
    construction_cost: int = 1,
) -> int:
    cost = 0
    for candidate in order:
        cost += construction_cost + test_cost
        if candidate == target:
            return cost
    raise ValueError("library order omitted the target")


def f3_target_alignment_witness(max_n: int = 6) -> dict[str, object]:
    """Construct a target/library alignment allowed by literal F3."""

    if max_n < 1:
        raise ValueError("max_n must be positive")
    scaling_rows: list[dict[str, object]] = []
    for width in range(1, max_n + 1):
        target = "1" * width
        library_order = reversed(_bitstrings(width))
        fringe_cost, localizations = _fringe_cost(target)
        library_cost = _library_cost(target, library_order)
        scaling_rows.append(
            {
                "n": width,
                "target": target,
                "fringe_closed_cost": fringe_cost,
                "library_closed_cost": library_cost,
                "usable_localization_count": localizations,
                "library_strictly_better": library_cost < fringe_cost,
            }
        )

    width = min(3, max_n)
    complete_order = list(reversed(_bitstrings(width)))
    sensitivity_rows: list[dict[str, object]] = []
    for target in _bitstrings(width):
        fringe_cost, localizations = _fringe_cost(target)
        library_cost = _library_cost(target, complete_order)
        winner = (
            "FRINGE"
            if fringe_cost < library_cost
            else "LIBRARY"
            if library_cost < fringe_cost
            else "TIE"
        )
        sensitivity_rows.append(
            {
                "target": target,
                "fringe_closed_cost": fringe_cost,
                "library_closed_cost": library_cost,
                "usable_localization_count": localizations,
                "winner": winner,
            }
        )
    return {
        "claim": "literal F3 permits target/library alignment to decide the tournament",
        "subject_lines": [570, 1596],
        "cost_convention": {
            "test": 1,
            "one_site_edit": 1,
            "library_candidate_construction": 1,
            "common_seed_cost": "equal and omitted from both displayed increments",
        },
        "target_family": "T_n is the n-bit all-ones target",
        "library_schema": "reverse-lexicographic enumeration of n-bit candidates",
        "rival_dominates_every_scaling_cut": all(
            row["library_strictly_better"] for row in scaling_rows
        ),
        "fringe_localization_usable_every_scaling_cut": all(
            row["usable_localization_count"] > 0 for row in scaling_rows
        ),
        "scaling_rows": scaling_rows,
        "complete_target_sensitivity_width": width,
        "complete_target_sensitivity_rows": sensitivity_rows,
        "observable": (
            "cost vectors [3,5,7,9,11,13] versus [2,2,2,2,2,2] at max_n=6, "
            "plus the complete three-bit winner partition"
        ),
        "scope": (
            "a declared-family counterwitness and protocol confound, not a universal "
            "ranking of fringe and library policies"
        ),
    }


def f4_lookup_false_green_control(size: int = 4) -> dict[str, object]:
    """Return a finite lookup decoder that must not decide unrestricted R."""

    if size < 1:
        raise ValueError("size must be positive")
    targets = [f"t{index}" for index in range(size)]
    accounts = [f"a{index}" for index in range(size)]
    decoder = dict(zip(targets, accounts))
    return {
        "claim": "finite fixed-decoder success does not decide open-ended Conjecture R",
        "subject_lines": [363, 1598],
        "finite_target_class": targets,
        "frozen_decoder": decoder,
        "lossless_on_declared_class": len(set(decoder.values())) == size,
        "receiver_owned_construction_required_by_encoding": False,
        "expected_unrestricted_verdict": "INCONCLUSIVE",
        "observable": (
            "all finite lookups succeed while the unrestricted verdict remains INCONCLUSIVE"
        ),
    }


def finite_exhaustion_evidence() -> dict[str, object]:
    """Return the complete deterministic evidence object for this module."""

    return {
        "schema": "TESTPOIETIC_FINITE_EXHAUSTION_V1",
        "transition_mutations": transition_mutation_evidence(),
        "transition_semantic_exhaustion": transition_semantic_exhaustion(),
        "p3_1_exhaustion": p31_exhaustion(),
        "p3_6_one_mastery_control": p36_one_mastery_control(),
        "capstone_literal_witness": capstone_literal_witness(),
        "f2_mutation_matrix": f2_mutation_matrix(),
        "f3_target_alignment_witness": f3_target_alignment_witness(),
        "f4_lookup_false_green_control": f4_lookup_false_green_control(),
    }


def canonical_evidence_json() -> str:
    """Serialize the complete evidence with deterministic bytes."""

    return json.dumps(
        finite_exhaustion_evidence(),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ) + "\n"


__all__ = [
    "canonical_evidence_json",
    "capstone_literal_witness",
    "f2_mutation_matrix",
    "f3_target_alignment_witness",
    "f4_lookup_false_green_control",
    "finite_exhaustion_evidence",
    "p31_exhaustion",
    "p36_one_mastery_control",
    "transition_mutation_evidence",
    "transition_semantic_exhaustion",
]
