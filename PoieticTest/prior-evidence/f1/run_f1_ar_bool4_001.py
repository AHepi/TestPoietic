#!/usr/bin/env python3
"""Execute preregistered F1-AR-BOOL4-001 exactly as frozen."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Sequence

N_INPUTS = 4
N_ROWS = 1 << N_INPUTS
FULL_MASK = (1 << N_ROWS) - 1
MAX_COST = 5
SEED = b"SPARK-F1-AR-BOOL4-001-BATTERY"
LEAVES = ("0", "1", "x0", "x1", "x2", "x3")
BINARY_OPS = ("A", "O", "X")

Node = str | tuple


def variable_mask(j: int) -> int:
    value = 0
    for i in range(N_ROWS):
        if (i >> j) & 1:
            value |= 1 << i
    return value


LEAF_MASKS = {
    "0": 0,
    "1": FULL_MASK,
    **{f"x{j}": variable_mask(j) for j in range(N_INPUTS)},
}


def battery_indices() -> list[int]:
    seen: set[int] = set()
    result: list[int] = []
    counter = 0
    while len(result) < 8:
        digest = hashlib.sha256(SEED + b":" + str(counter).encode("ascii")).digest()
        for byte in digest:
            idx = byte % N_ROWS
            if idx not in seen:
                seen.add(idx)
                result.append(idx)
                if len(result) == 8:
                    break
        counter += 1
    return result


def encode(node: Node) -> str:
    if isinstance(node, str):
        return node
    op = node[0]
    if op == "N":
        return f"N({encode(node[1])})"
    return f"{op}({encode(node[1])},{encode(node[2])})"


def parse_expr(text: str, pos: int = 0) -> tuple[Node, int]:
    if text.startswith("x", pos):
        token = text[pos : pos + 2]
        if token not in LEAF_MASKS:
            raise ValueError(f"invalid variable at {pos}: {text}")
        return token, pos + 2
    ch = text[pos]
    if ch in "01":
        return ch, pos + 1
    if ch == "N":
        if text[pos + 1] != "(":
            raise ValueError(text)
        child, next_pos = parse_expr(text, pos + 2)
        if text[next_pos] != ")":
            raise ValueError(text)
        return ("N", child), next_pos + 1
    if ch in "AOX":
        if text[pos + 1] != "(":
            raise ValueError(text)
        left, next_pos = parse_expr(text, pos + 2)
        if text[next_pos] != ",":
            raise ValueError(text)
        right, next_pos = parse_expr(text, next_pos + 1)
        if text[next_pos] != ")":
            raise ValueError(text)
        return (ch, left, right), next_pos + 1
    raise ValueError(f"invalid expression at {pos}: {text}")


def parse_complete(text: str) -> Node:
    node, pos = parse_expr(text)
    if pos != len(text):
        raise ValueError(f"trailing text: {text[pos:]}")
    return node


def eval_node(node: Node) -> int:
    if isinstance(node, str):
        return LEAF_MASKS[node]
    op = node[0]
    if op == "N":
        return (~eval_node(node[1])) & FULL_MASK
    left = eval_node(node[1])
    right = eval_node(node[2])
    if op == "A":
        return left & right
    if op == "O":
        return left | right
    if op == "X":
        return left ^ right
    raise ValueError(op)


def canonical_binary(op: str, left: str, right: str) -> str:
    if right < left:
        left, right = right, left
    return f"{op}({left},{right})"


def build_minimal_expressions(max_cost: int = MAX_COST) -> tuple[dict[int, tuple[int, str]], list[dict[int, str]], list[dict[str, int]]]:
    best: dict[int, tuple[int, str]] = {}
    by_cost: list[dict[int, str]] = []
    diagnostics: list[dict[str, int]] = []

    cost0: dict[int, str] = {}
    for leaf in LEAVES:
        value = LEAF_MASKS[leaf]
        old = cost0.get(value)
        if old is None or leaf < old:
            cost0[value] = leaf
    by_cost.append(cost0)
    for value, expr in cost0.items():
        best[value] = (0, expr)
    diagnostics.append({"cost": 0, "new_functions": len(cost0), "candidate_functions": len(cost0)})

    for cost in range(1, max_cost + 1):
        exact_candidates: dict[int, str] = {}

        # Unary NOT adds one operator node.
        for value, child_expr in by_cost[cost - 1].items():
            out = (~value) & FULL_MASK
            expr = f"N({child_expr})"
            old = exact_candidates.get(out)
            if old is None or expr < old:
                exact_candidates[out] = expr

        # Binary roots: child costs sum to cost - 1.
        for left_cost in range(cost):
            right_cost = cost - 1 - left_cost
            if left_cost > right_cost:
                continue
            left_items = sorted(by_cost[left_cost].items(), key=lambda item: item[1])
            right_items = sorted(by_cost[right_cost].items(), key=lambda item: item[1])
            if left_cost == right_cost:
                for i, (left_value, left_expr) in enumerate(left_items):
                    for right_value, right_expr in right_items[i:]:
                        for op in BINARY_OPS:
                            if op == "A":
                                out = left_value & right_value
                            elif op == "O":
                                out = left_value | right_value
                            else:
                                out = left_value ^ right_value
                            expr = canonical_binary(op, left_expr, right_expr)
                            old = exact_candidates.get(out)
                            if old is None or expr < old:
                                exact_candidates[out] = expr
            else:
                for left_value, left_expr in left_items:
                    for right_value, right_expr in right_items:
                        for op in BINARY_OPS:
                            if op == "A":
                                out = left_value & right_value
                            elif op == "O":
                                out = left_value | right_value
                            else:
                                out = left_value ^ right_value
                            expr = canonical_binary(op, left_expr, right_expr)
                            old = exact_candidates.get(out)
                            if old is None or expr < old:
                                exact_candidates[out] = expr

        new_at_cost: dict[int, str] = {}
        for value, expr in exact_candidates.items():
            if value in best:
                # A later expression cannot replace a lower-cost minimum.
                continue
            old = new_at_cost.get(value)
            if old is None or expr < old:
                new_at_cost[value] = expr

        by_cost.append(new_at_cost)
        for value, expr in new_at_cost.items():
            best[value] = (cost, expr)
        diagnostics.append(
            {
                "cost": cost,
                "new_functions": len(new_at_cost),
                "candidate_functions": len(exact_candidates),
            }
        )
    return best, by_cost, diagnostics


def iter_paths(node: Node, prefix: tuple[int, ...] = ()) -> Iterable[tuple[tuple[int, ...], Node]]:
    yield prefix, node
    if isinstance(node, tuple):
        if node[0] == "N":
            yield from iter_paths(node[1], prefix + (1,))
        else:
            yield from iter_paths(node[1], prefix + (1,))
            yield from iter_paths(node[2], prefix + (2,))


def replace_at(node: Node, path: Sequence[int], replacement: Node) -> Node:
    if not path:
        return replacement
    if isinstance(node, str):
        raise ValueError("path enters leaf")
    index = path[0]
    if node[0] == "N":
        if index != 1:
            raise ValueError(path)
        return ("N", replace_at(node[1], path[1:], replacement))
    if index == 1:
        return (node[0], replace_at(node[1], path[1:], replacement), node[2])
    if index == 2:
        return (node[0], node[1], replace_at(node[2], path[1:], replacement))
    raise ValueError(path)


def local_neighbour_values(node: Node, target_value: int) -> set[int]:
    neighbours: set[int] = set()
    for path, subtree in iter_paths(node):
        # Insert NOT above any selected subtree.
        edited = replace_at(node, path, ("N", subtree))
        neighbours.add(eval_node(edited))

        if isinstance(subtree, str):
            for leaf in LEAVES:
                if leaf != subtree:
                    edited = replace_at(node, path, leaf)
                    neighbours.add(eval_node(edited))
        elif subtree[0] == "N":
            edited = replace_at(node, path, subtree[1])
            neighbours.add(eval_node(edited))
        else:
            for op in BINARY_OPS:
                if op != subtree[0]:
                    edited = replace_at(node, path, (op, subtree[1], subtree[2]))
                    neighbours.add(eval_node(edited))

    neighbours.discard(target_value)
    return neighbours


def average_ranks(values: Sequence[float]) -> list[float]:
    indexed = sorted(enumerate(values), key=lambda pair: pair[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i + 1
        while j < len(indexed) and indexed[j][1] == indexed[i][1]:
            j += 1
        avg_rank = ((i + 1) + j) / 2.0
        for k in range(i, j):
            ranks[indexed[k][0]] = avg_rank
        i = j
    return ranks


def pearson(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y) or not x:
        raise ValueError("invalid vectors")
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    dx = [v - mean_x for v in x]
    dy = [v - mean_y for v in y]
    denom = math.sqrt(sum(v * v for v in dx) * sum(v * v for v in dy))
    if denom == 0:
        return float("nan")
    return sum(a * b for a, b in zip(dx, dy)) / denom


def spearman(x: Sequence[float], y: Sequence[float]) -> float:
    return pearson(average_ranks(x), average_ranks(y))


def linear_quantile(values: Sequence[float], q: float) -> float:
    if not values:
        raise ValueError("empty quantile")
    ordered = sorted(values)
    position = (len(ordered) - 1) * q
    lo = math.floor(position)
    hi = math.ceil(position)
    if lo == hi:
        return float(ordered[lo])
    weight = position - lo
    return float(ordered[lo] * (1.0 - weight) + ordered[hi] * weight)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    battery = battery_indices()
    best, by_cost, generation_diagnostics = build_minimal_expressions()

    rows: list[dict[str, object]] = []
    verification_errors: list[str] = []

    for value, (cost, expr) in sorted(best.items(), key=lambda item: (item[1][0], item[0])):
        if not (1 <= cost <= MAX_COST):
            continue
        node = parse_complete(expr)
        evaluated = eval_node(node)
        if evaluated != value:
            verification_errors.append(f"expression mismatch {value:04x} {expr} -> {evaluated:04x}")
            continue
        neighbours = local_neighbour_values(node, value)
        if len(neighbours) < 4:
            continue
        if value in neighbours:
            verification_errors.append(f"identity neighbour survived for {value:04x}")
        failing = sum(
            1
            for neighbour in neighbours
            if any(((neighbour ^ value) >> index) & 1 for index in battery)
        )
        rigidity = failing / len(neighbours)
        rows.append(
            {
                "truth_table_hex": f"{value:04x}",
                "distance": cost,
                "canonical_expression": expr,
                "neighbour_count": len(neighbours),
                "failing_neighbour_count": failing,
                "rigidity": f"{rigidity:.17g}",
            }
        )

    csv_path = output_dir / "F1-AR-BOOL4-001-targets.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    distances = [float(row["distance"]) for row in rows]
    rigidities = [float(row["rigidity"]) for row in rows]
    rho = spearman(distances, rigidities)
    q1 = linear_quantile(rigidities, 0.25)
    q3 = linear_quantile(rigidities, 0.75)
    iqr = q3 - q1

    grouped: dict[int, list[float]] = defaultdict(list)
    for row in rows:
        grouped[int(row["distance"])].append(float(row["rigidity"]))
    medians = {str(cost): linear_quantile(grouped[cost], 0.5) for cost in sorted(grouped)}
    represented = sorted(grouped)
    strictly_decreasing = (
        len(represented) >= 2
        and all(medians[str(b)] < medians[str(a)] for a, b in zip(represented, represented[1:]))
    )

    survival = (
        not verification_errors
        and not math.isnan(rho)
        and rho >= 0.20
        and iqr >= 0.10
        and not strictly_decreasing
    )
    if verification_errors or math.isnan(rho):
        verdict = "INCONCLUSIVE"
    elif survival:
        verdict = "SURVIVED THIS CUT"
    else:
        verdict = "REFUTED ON THIS DECLARED DOMAIN"

    summary = {
        "experiment_id": "F1-AR-BOOL4-001",
        "battery_indices": battery,
        "max_operator_distance": MAX_COST,
        "generated_function_count_total": len(best),
        "generated_function_count_by_minimum_distance": {
            str(cost): len(items) for cost, items in enumerate(by_cost)
        },
        "generation_diagnostics": generation_diagnostics,
        "declared_target_count": len(rows),
        "target_count_by_distance": {str(cost): len(grouped[cost]) for cost in sorted(grouped)},
        "spearman_rho": rho,
        "rigidity_q1": q1,
        "rigidity_q3": q3,
        "rigidity_iqr": iqr,
        "median_rigidity_by_distance": medians,
        "strictly_decreasing_median_sequence": strictly_decreasing,
        "survival_conditions": {
            "rho_at_least_0_20": rho >= 0.20 if not math.isnan(rho) else False,
            "iqr_at_least_0_10": iqr >= 0.10,
            "median_sequence_not_strictly_decreasing": not strictly_decreasing,
        },
        "verification_error_count": len(verification_errors),
        "verification_errors": verification_errors[:100],
        "verdict": verdict,
    }

    summary_path = output_dir / "F1-AR-BOOL4-001-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    verdict_path = output_dir / "F1-AR-BOOL4-001-verdict.md"
    verdict_path.write_text(
        "\n".join(
            [
                "# F1-AR-BOOL4-001 Verdict Record",
                "",
                f"**Verdict:** {verdict}",
                "",
                f"**Declared targets:** {len(rows)}",
                f"**Fixed battery indices:** {battery}",
                f"**Spearman rho:** {rho:.12f}",
                f"**Rigidity IQR:** {iqr:.12f}",
                f"**Median rigidity by distance:** {json.dumps(medians, sort_keys=True)}",
                f"**Strictly decreasing medians:** {strictly_decreasing}",
                f"**Verification errors:** {len(verification_errors)}",
                "",
                "The verdict follows the frozen rule mechanically. It applies only to the declared Boolean-expression domain, distance cap, canonicalization, edit graph, and eight-input battery.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    manifest = {
        "code_sha256": sha256_file(Path(__file__)),
        "targets_csv_sha256": sha256_file(csv_path),
        "summary_json_sha256": sha256_file(summary_path),
        "verdict_md_sha256": sha256_file(verdict_path),
    }
    (output_dir / "F1-AR-BOOL4-001-output-hashes.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if verdict != "INCONCLUSIVE" else 2


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd() / "run-output"
    raise SystemExit(main(out))
