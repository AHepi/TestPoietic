"""Small exact models aimed at distinct Spark-Poietic claim mechanisms."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    channel: str


def _paths(edges: Iterable[Edge], source: str, target: str) -> list[list[str]]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        adjacency[edge.source].append(edge.target)
    found: list[list[str]] = []

    def visit(node: str, path: list[str]) -> None:
        if node == target:
            found.append(path)
            return
        for nxt in adjacency[node]:
            if nxt not in path:
                visit(nxt, [*path, nxt])

    visit(source, [source])
    return found


def _ordered(path: list[str], required: list[str]) -> bool:
    cursor = -1
    for node in required:
        try:
            cursor = path.index(node, cursor + 1)
        except ValueError:
            return False
    return True


def literal_w3_satisfied(model: dict[str, object]) -> bool:
    """Evaluate only the path clauses that W3 actually states.

    Universal path conditions use their ordinary logical meaning: they are true
    when no relevant path exists.  Deliberately absent are requirements that the
    candidate determine the occupant and that a current criterion/open permission
    exist; those are A5 obligations not asserted by W3.
    """

    nodes: dict[str, dict[str, object]] = model["nodes"]  # type: ignore[assignment]
    edges = [Edge(**row) for row in model["edges"]]  # type: ignore[arg-type]
    by_kind: dict[str, list[str]] = defaultdict(list)
    for name, record in nodes.items():
        by_kind[str(record["kind"])].append(name)
    required_kinds = {"construction", "candidate", "exposure", "outcome", "award", "role_write"}
    if not required_kinds.issubset(by_kind):
        return False
    construction = by_kind["construction"][0]
    candidate = by_kind["candidate"][0]
    exposure = by_kind["exposure"][0]
    outcome = by_kind["outcome"][0]
    award = by_kind["award"][0]
    role_write = by_kind["role_write"][0]

    for source_kind in ("held", "seed", "target", "external_raw"):
        for source in by_kind.get(source_kind, []):
            for path in _paths(edges, source, role_write):
                if not _ordered(path, [construction]):
                    return False

    for path in _paths(edges, candidate, role_write):
        if not _ordered(path, [exposure, outcome, award, role_write]):
            return False

    if not bool(nodes[outcome].get("resistant")):
        return False
    if not _paths(edges, outcome, award):
        return False
    return True


def a5_satisfied(model: dict[str, object]) -> bool:
    nodes: dict[str, dict[str, object]] = model["nodes"]  # type: ignore[assignment]
    edges = [Edge(**row) for row in model["edges"]]  # type: ignore[arg-type]
    by_kind: dict[str, list[str]] = defaultdict(list)
    for name, record in nodes.items():
        by_kind[str(record["kind"])].append(name)
    needed = {"construction", "candidate", "exposure", "outcome", "award", "role_write"}
    if not needed.issubset(by_kind):
        return False
    candidate = by_kind["candidate"][0]
    role_write = by_kind["role_write"][0]
    award = by_kind["award"][0]
    if nodes[role_write].get("occupant_source") != candidate:
        return False
    if not bool(nodes[award].get("licensed_by_current_criterion")):
        return False
    if not bool(nodes[role_write].get("open_permission")):
        return False
    return literal_w3_satisfied(model)


def w3_vacuity_countermodel() -> dict[str, object]:
    model: dict[str, object] = {
        "nodes": {
            "build": {"kind": "construction"},
            "candidate": {"kind": "candidate"},
            "expose": {"kind": "exposure"},
            "world": {"kind": "outcome", "resistant": True},
            "award": {
                "kind": "award",
                "licensed_by_current_criterion": False,
            },
            "constant": {"kind": "internal_constant_generator"},
            "write": {
                "kind": "role_write",
                "occupant_source": "constant",
                "open_permission": False,
            },
        },
        "edges": [
            {"source": "build", "target": "candidate", "channel": "content"},
            {"source": "candidate", "target": "expose", "channel": "content"},
            {"source": "expose", "target": "world", "channel": "test"},
            {"source": "world", "target": "award", "channel": "verdict"},
            {"source": "award", "target": "write", "channel": "control"},
            {"source": "constant", "target": "write", "channel": "occupant"},
        ],
    }
    return {
        "claim": "W3 implies A5 under P5.3's stated identification",
        "subject_lines": [1231, 1263, 1273, 1293, 1303],
        "model": model,
        "literal_w3": literal_w3_satisfied(model),
        "a5": a5_satisfied(model),
        "counterexample": literal_w3_satisfied(model) and not a5_satisfied(model),
        "mechanism": (
            "W3 constrains paths but does not require the constructed candidate to determine "
            "the promoted occupant, nor a current criterion and open permission channel."
        ),
    }


def p35_cut_countermodel() -> dict[str, object]:
    predecessor = {"protected", "unselected"}
    beta = {"protected"}
    terminal = {"protected", "new"}
    direct_route_premises = (
        beta.issubset(terminal)
        and "new" in terminal
        and "new" not in predecessor
    )
    full_embedding_exists = predecessor.issubset(terminal)
    return {
        "claim": "P3.5 lifts protection of finite cut beta to a marked extension",
        "subject_lines": [1132, 1142, 1185, 1193],
        "predecessor_marks": sorted(predecessor),
        "protected_cut_beta": sorted(beta),
        "terminal_marks": sorted(terminal),
        "direct_route_premises_on_beta": direct_route_premises,
        "full_K_embedding_exists": full_embedding_exists,
        "counterexample": direct_route_premises and not full_embedding_exists,
        "mechanism": (
            "The direct route protects only beta, while the earlier marked-extension "
            "definition embeds all of K_B(Sigma).  The extension task may destroy an "
            "unselected predecessor mark."
        ),
    }


def rg_quantifier_countermodel() -> dict[str, object]:
    cuts = (1, 2, 3, 4)
    success = {
        "G_nominated": {1: True, 2: False, 3: False, 4: False},
        "G_other": {1: True, 2: True, 3: True, 4: True},
    }
    residue_truth = any(all(rows[n] for n in cuts) for rows in success.values())
    nominated_failure = not all(success["G_nominated"][n] for n in cuts)
    return {
        "claim": "F8-D: one failed frozen G refutes existential residue R_G",
        "subject_lines": [825, 843, 1614],
        "quantifier": "exists G, for all n in I, Success(G,n)",
        "declared_architectures": success,
        "nominated_G_fails": nominated_failure,
        "R_G_true_on_declared_class": residue_truth,
        "counterexample": nominated_failure and residue_truth,
        "mechanism": (
            "Failure of one existential candidate refutes only that witness.  R_G is "
            "refuted only by forall G exists n Failure(G,n), or by an exhaustive "
            "architecture-class reduction."
        ),
    }


def t7_repair_partition_countermodel() -> dict[str, object]:
    """Lowest cost need not be a retreat when repair kinds are not exhaustive."""

    repairs = [
        {"name": "strict_retreat", "cost": 2, "old_content": 3, "new_content": 2},
        {"name": "content_preserving", "cost": 3, "old_content": 3, "new_content": 3},
        {"name": "incomparable_expansion", "cost": 1, "old_content": 3, "new_content": 4},
    ]
    retreats = [row for row in repairs if row["name"] == "strict_retreat"]
    preservers = [row for row in repairs if row["name"] == "content_preserving"]
    comparison_premise = max(row["cost"] for row in retreats) < min(
        row["cost"] for row in preservers
    )
    selected = min(repairs, key=lambda row: int(row["cost"]))
    return {
        "claim": "T7's stated repair-cost comparison forces strict content descent",
        "subject_lines": [401, 403],
        "repairs": repairs,
        "strict_retreat_available": bool(retreats),
        "retreat_cheaper_than_every_content_preserving_repair": comparison_premise,
        "lowest_cost_selected": selected["name"],
        "selected_content_change": selected["new_content"] - selected["old_content"],
        "strict_descent": selected["new_content"] < selected["old_content"],
        "counterexample": comparison_premise
        and bool(retreats)
        and selected["new_content"] >= selected["old_content"],
        "mechanism": (
            "The statement does not require every admissible repair to be either a "
            "strict retreat or content-preserving; a cheaper incomparable repair wins."
        ),
    }


def fragility_reachability_countermodel() -> dict[str, object]:
    states = {
        "growing_guarded": {
            "content_guard": True,
            "retreat_permission_rule": False,
            "regime": "growing",
        },
        "rule_installed": {
            "content_guard": True,
            "retreat_permission_rule": True,
            "regime": "growing",
        },
    }
    transitions = [("growing_guarded", "rule_installed", "selected_A5_install")]
    reachable = {"growing_guarded"}
    frontier = ["growing_guarded"]
    while frontier:
        current = frontier.pop()
        for source, target, _ in transitions:
            if source == current and target not in reachable:
                reachable.add(target)
                frontier.append(target)
    exit_reachable = any(states[name]["regime"] != "growing" for name in reachable)
    return {
        "claim": "Fragility Proposition's displayed premises make regime exit reachable",
        "subject_lines": [514],
        "constructible_retreat_rule": True,
        "A5_admissible_install_path": True,
        "scheduler_selects_install_path": True,
        "states": states,
        "transitions": transitions,
        "exit_from_growing_regime_reachable": exit_reachable,
        "counterexample": not exit_reachable,
        "mechanism": (
            "Installing a retreat-permitting rule neither removes the standing content "
            "guard nor supplies and schedules a subsequent retreat transition."
        ),
    }


def target_essential_idle_metadata_countermodel() -> dict[str, object]:
    candidates = {
        "target_A": {"operative_program": "constant-7", "unused_metadata": "A"},
        "target_B": {"operative_program": "constant-7", "unused_metadata": "B"},
    }
    literal_candidate_changes = candidates["target_A"] != candidates["target_B"]
    operative_change = (
        candidates["target_A"]["operative_program"]
        != candidates["target_B"]["operative_program"]
    )
    return {
        "claim": "target-essentiality attributes operative growth to the target",
        "subject_lines": [347],
        "candidates": candidates,
        "award_A": "promote constant-7",
        "award_B": "promote constant-7",
        "literal_definition_satisfied": literal_candidate_changes,
        "operative_or_award_relevant_change": operative_change,
        "counterexample": literal_candidate_changes and not operative_change,
        "mechanism": "An idle target hash changes candidate bytes but no operative or award-relevant coordinate.",
    }


def tref_box_countermodel() -> dict[str, object]:
    facts = {
        "predecessor_problematic": True,
        "current_criteria_judge_predecessor_good": True,
        "rival_good": True,
        "rival_successor_recovers": True,
    }
    box_antecedent = (
        facts["predecessor_problematic"]
        and facts["rival_good"]
        and facts["rival_successor_recovers"]
    )
    full_tref = box_antecedent and not facts["current_criteria_judge_predecessor_good"]
    return {
        "claim": "The unified box's shorter antecedent entails TRef",
        "subject_lines": [193, 199, 1706, 1710],
        "facts": facts,
        "boxed_antecedent_true": box_antecedent,
        "TRef_true": full_tref,
        "counterexample": box_antecedent and not full_tref,
        "mechanism": "The box drops TRef's required not-good(predecessor) conjunct.",
    }


def provenance_distance_nonunique() -> dict[str, object]:
    certificates = {
        "direct": ["construct_z"],
        "expanded": ["construct_x", "construct_y_from_x", "construct_z_from_y"],
    }
    distances = {name: len(nodes) for name, nodes in certificates.items()}
    return {
        "claim": "A held structure's constructor-node count defines one provenance distance",
        "subject_lines": [339, 341],
        "same_held_structure": "z",
        "valid_certificates": certificates,
        "constructor_node_counts": distances,
        "unique_distance": len(set(distances.values())) == 1,
        "counterexample": len(set(distances.values())) > 1,
        "mechanism": "No minimum, canonical certificate, or certificate identity is specified.",
    }


def anj_reversal_gap() -> dict[str, object]:
    transitions = {"seed": {"promoted"}, "promoted": set()}
    reversal_reachable = "seed" in transitions["promoted"]
    return {
        "claim": "A-NJ's every-standing-change reversibility is supplied by the transition grammar",
        "subject_lines": [201, 301],
        "transition_algebra": {name: sorted(nexts) for name, nexts in transitions.items()},
        "standing_change_exists": "promoted" in transitions["seed"],
        "reversal_reachable": reversal_reachable,
        "counterexample": not reversal_reachable,
        "mechanism": "The declared grammar supplies promotion but no demotion, replacement, or revocation rule.",
    }


def rx_refuter_quantifier_countermodel() -> dict[str, object]:
    problems = {"q_unextendable": False, "q_extendable": True}
    residue_truth = any(problems.values())
    prose_failure_witness = any(not extendable for extendable in problems.values())
    return {
        "claim": "One live problem with no extension-ready resolution refutes existential R_X^Phi",
        "subject_lines": [1416, 1428],
        "problem_extendability": problems,
        "one_failed_problem_exists": prose_failure_witness,
        "R_X_true": residue_truth,
        "counterexample": prose_failure_witness and residue_truth,
        "mechanism": "An existential residue is refuted only when every eligible live problem fails.",
    }


def finite_prefix_transition_existence_gap() -> dict[str, object]:
    premises = {
        "creative_capacity_K0": True,
        "R_P0": True,
        "R_P_plus_on_every_selected_transition": True,
        "R_S_on_every_selected_transition": True,
        "R_X_on_every_selected_transition": True,
        "W0_W5_on_every_selected_transition": True,
        "A5_growth_on_every_selected_write": True,
    }
    selected_transitions: list[str] = []
    return {
        "claim": "The finite-prefix theorem's displayed premises entail a length-one selected prefix",
        "subject_lines": [1416, 1454],
        "premises": premises,
        "selected_transitions": selected_transitions,
        "universal_transition_clauses_vacuously_true": all(premises.values()),
        "length_one_prefix_exists": bool(selected_transitions),
        "countermodel_under_literal_universal_reading": not selected_transitions,
        "classification": "quantifier under-specification",
        "repair": (
            "Require, at each cut, an existential q-specific selected target-essential "
            "A5 transition jointly witnessed by R_P+, R_S, R_X and W0-W5."
        ),
    }


def capstone_residue_countermodels() -> list[dict[str, object]]:
    return [
        {
            "residue": "R_P0",
            "subject_lines": [620, 630],
            "premises": {
                "construct_non_seed_candidates": True,
                "consequential_appraisal": True,
                "A5_promotion": True,
                "owned_evaluated_target_source": True,
            },
            "open_nonvacuous_problem": False,
            "counterexample": True,
            "scope": "finite abstract Spark state",
        },
        {
            "residue": "R_P+",
            "subject_lines": [632, 642],
            "initial_open_problems": 1,
            "transition_resolves": 1,
            "new_problems_constructed": 0,
            "terminal_open_problems": 0,
            "counterexample": True,
            "scope": "one-step selected abstract history",
        },
        {
            "residue": "R_S",
            "subject_lines": [644, 657],
            "open_problem": "perform task forbidden by stipulated Phi",
            "physically_possible_good_members": 0,
            "counterexample": True,
            "scope": "finite law-relative constructor model",
        },
        {
            "residue": "R_X^Phi",
            "subject_lines": [1195, 1199, 1416, 1428],
            "open_good_resolution_exists": True,
            "new_capability_individually_possible": True,
            "unique_nonduplicable_mastery_substrate": True,
            "predecessor_preservable_with_new_capability": False,
            "counterexample": True,
            "scope": "P3.6-shaped finite law-relative model",
        },
    ]


def finite_prefix_quantifier_gap(max_depth: int = 12) -> dict[str, object]:
    branch_lengths = list(range(1, max_depth + 1))
    every_tested_depth_exists = all(
        any(length >= requested for length in branch_lengths)
        for requested in range(1, max_depth + 1)
    )
    return {
        "claim": "unbounded finite extendibility does not imply one infinite history",
        "subject_lines": [1458, 1470],
        "tree_schema": "root has one branch of each finite length n and no infinite branch",
        "checked_depth": max_depth,
        "branch_lengths": branch_lengths,
        "prefix_exists_at_every_checked_depth": every_tested_depth_exists,
        "infinite_branch_exists_by_schema": False,
        "counterexample_to_converse": every_tested_depth_exists,
    }


def c2_counterdomain() -> dict[str, object]:
    rows = [
        {"source": "a", "fibre_size": 1, "predicted_pinning": 3, "transmission": 0.20},
        {"source": "b", "fibre_size": 2, "predicted_pinning": 2, "transmission": 0.55},
        {"source": "c", "fibre_size": 4, "predicted_pinning": 1, "transmission": 0.90},
    ]
    pinning_correct = all(
        row["predicted_pinning"] == 4 - row["fibre_size"].bit_length()
        for row in rows
    )
    pinning_order = [row["source"] for row in sorted(rows, key=lambda r: -r["predicted_pinning"])]
    transmission_order = [row["source"] for row in sorted(rows, key=lambda r: -r["transmission"])]
    return {
        "claim": "C2 pinning geometry predicts transmission order",
        "subject_lines": [453, 457, 1594],
        "single_battery": True,
        "answer_free_iota": True,
        "matched_budget": True,
        "rows": rows,
        "pinning_prediction_correct": pinning_correct,
        "pinning_order": pinning_order,
        "transmission_order": transmission_order,
        "stable_reversal": pinning_order == list(reversed(transmission_order)),
        "counterdomain": pinning_correct and pinning_order == list(reversed(transmission_order)),
        "scope": "constructed finite reconstruction/transmission domain",
    }


def b_core_direct_write_countermodel() -> dict[str, object]:
    nodes = ("old_mark", "external_write", "new_mark", "retention")
    admissible_boundaries: list[tuple[str, ...]] = []
    for size in range(2, len(nodes) + 1):
        for subset in combinations(nodes, size):
            if "new_mark" in subset and "retention" in subset:
                admissible_boundaries.append(subset)
    missing_stages = {"construction", "exposure", "outcome", "award"}
    every_boundary_fails_a5 = all(bool(missing_stages) for _ in admissible_boundaries)
    return {
        "claim": "B-Core on the unrestricted law-relative model class",
        "subject_lines": [861, 1604],
        "poietic_information_variable": [0, 1],
        "new_value_content_sensitive_self_retention": True,
        "predecessor_mark_preserved": True,
        "new_capability_mark": True,
        "causal_graph": [
            ["old_mark", "old_mark", "persistence"],
            ["external_write", "new_mark", "direct occupant write"],
            ["new_mark", "retention", "value-selects-maintenance"],
            ["retention", "new_mark", "re-instantiation"],
        ],
        "admissible_boundary_count": len(admissible_boundaries),
        "a5_stages_absent_from_complete_model": sorted(missing_stages),
        "every_admissible_boundary_fails_a5": every_boundary_fails_a5,
        "countermodel": every_boundary_fails_a5,
        "scope": (
            "model-theoretic counterexample to an unrestricted bridge reading; "
            "not evidence that an actual-world instance exists"
        ),
    }


def all_formal_models() -> dict[str, object]:
    return {
        "w3_to_a5": w3_vacuity_countermodel(),
        "p35_cut_scope": p35_cut_countermodel(),
        "rg_quantifier": rg_quantifier_countermodel(),
        "t7_repair_partition": t7_repair_partition_countermodel(),
        "fragility_reachability": fragility_reachability_countermodel(),
        "target_essential_idle_metadata": target_essential_idle_metadata_countermodel(),
        "tref_box": tref_box_countermodel(),
        "provenance_distance": provenance_distance_nonunique(),
        "anj_reversal": anj_reversal_gap(),
        "rx_refuter_quantifier": rx_refuter_quantifier_countermodel(),
        "finite_prefix_transition_existence": finite_prefix_transition_existence_gap(),
        "capstone_residues": capstone_residue_countermodels(),
        "finite_prefix_gap": finite_prefix_quantifier_gap(),
        "c2_counterdomain": c2_counterdomain(),
        "b_core_direct_write": b_core_direct_write_countermodel(),
    }
