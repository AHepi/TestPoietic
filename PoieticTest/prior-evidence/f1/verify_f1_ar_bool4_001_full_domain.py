#!/usr/bin/env python3
"""Independent full-domain audit for F1-AR-BOOL4-001.

This verifier does not import the execution program. It separately enumerates
minimum Boolean-expression representatives through operator cost five, rebuilds
the declared target domain, recalculates every local neighbourhood and rigidity,
and compares the complete result with the saved run.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterator, Sequence

ROW_COUNT = 16
FULL = (1 << ROW_COUNT) - 1
MAX_OPERATOR_COST = 5
LEAF_NAMES = ("0", "1", "x0", "x1", "x2", "x3")
BINARY_NAMES = ("A", "O", "X")
BATTERY_SEED = b"SPARK-F1-AR-BOOL4-001-BATTERY"
Tree = str | tuple


def variable_truth_table(index: int) -> int:
    table = 0
    for row in range(ROW_COUNT):
        table |= ((row >> index) & 1) << row
    return table


LEAF_TABLES = {
    "0": 0,
    "1": FULL,
    "x0": variable_truth_table(0),
    "x1": variable_truth_table(1),
    "x2": variable_truth_table(2),
    "x3": variable_truth_table(3),
}


def fixed_battery() -> list[int]:
    result: list[int] = []
    seen: set[int] = set()
    counter = 0
    while len(result) < 8:
        block = hashlib.sha256(
            BATTERY_SEED + b":" + str(counter).encode("ascii")
        ).digest()
        for byte in block:
            row = byte % ROW_COUNT
            if row not in seen:
                seen.add(row)
                result.append(row)
                if len(result) == 8:
                    return result
        counter += 1
    raise AssertionError("unreachable")


def apply_binary(name: str, left: int, right: int) -> int:
    if name == "A":
        return left & right
    if name == "O":
        return left | right
    if name == "X":
        return left ^ right
    raise ValueError(name)


def binary_encoding(name: str, left: str, right: str) -> str:
    first, second = sorted((left, right))
    return f"{name}({first},{second})"


def independently_enumerate_minima() -> list[dict[int, str]]:
    """Enumerate exact minimum-cost functions with an all-splits recurrence.

    Unlike the execution program, this implementation visits every ordered cost
    split and every ordered pair, then canonicalises at insertion. The duplicate
    work is intentional: it makes the audit structurally separate from the
    execution program's symmetry-pruned loops.
    """
    levels: list[dict[int, str]] = []
    level_zero: dict[int, str] = {}
    for name in LEAF_NAMES:
        value = LEAF_TABLES[name]
        if value not in level_zero or name < level_zero[value]:
            level_zero[value] = name
    levels.append(level_zero)
    seen = set(level_zero)

    for total_cost in range(1, MAX_OPERATOR_COST + 1):
        candidates: dict[int, str] = {}

        for child_value, child_text in levels[total_cost - 1].items():
            output = (~child_value) & FULL
            text = f"N({child_text})"
            if output not in candidates or text < candidates[output]:
                candidates[output] = text

        for left_cost in range(total_cost):
            right_cost = total_cost - 1 - left_cost
            for left_value, left_text in levels[left_cost].items():
                for right_value, right_text in levels[right_cost].items():
                    for operator in BINARY_NAMES:
                        output = apply_binary(operator, left_value, right_value)
                        text = binary_encoding(operator, left_text, right_text)
                        if output not in candidates or text < candidates[output]:
                            candidates[output] = text

        current = {
            value: text
            for value, text in candidates.items()
            if value not in seen
        }
        levels.append(current)
        seen.update(current)

    return levels


def parse(text: str, position: int = 0) -> tuple[Tree, int]:
    if text.startswith("x", position):
        token = text[position : position + 2]
        if token not in LEAF_TABLES:
            raise ValueError(f"invalid variable in {text!r}")
        return token, position + 2
    token = text[position]
    if token in "01":
        return token, position + 1
    if token == "N":
        if text[position + 1] != "(":
            raise ValueError(text)
        child, end = parse(text, position + 2)
        if text[end] != ")":
            raise ValueError(text)
        return ("N", child), end + 1
    if token in BINARY_NAMES:
        if text[position + 1] != "(":
            raise ValueError(text)
        left, end = parse(text, position + 2)
        if text[end] != ",":
            raise ValueError(text)
        right, end = parse(text, end + 1)
        if text[end] != ")":
            raise ValueError(text)
        return (token, left, right), end + 1
    raise ValueError(f"invalid token in {text!r} at {position}")


def parse_all(text: str) -> Tree:
    tree, end = parse(text)
    if end != len(text):
        raise ValueError(f"unparsed suffix in {text!r}")
    return tree


def evaluate(tree: Tree) -> int:
    if isinstance(tree, str):
        return LEAF_TABLES[tree]
    if tree[0] == "N":
        return (~evaluate(tree[1])) & FULL
    return apply_binary(tree[0], evaluate(tree[1]), evaluate(tree[2]))


def walk(tree: Tree, path: tuple[int, ...] = ()) -> Iterator[tuple[tuple[int, ...], Tree]]:
    yield path, tree
    if isinstance(tree, tuple):
        yield from walk(tree[1], path + (1,))
        if tree[0] != "N":
            yield from walk(tree[2], path + (2,))


def replace(tree: Tree, path: Sequence[int], replacement: Tree) -> Tree:
    if not path:
        return replacement
    if isinstance(tree, str):
        raise ValueError("path entered a leaf")
    branch = path[0]
    if tree[0] == "N":
        if branch != 1:
            raise ValueError(path)
        return ("N", replace(tree[1], path[1:], replacement))
    if branch == 1:
        return (tree[0], replace(tree[1], path[1:], replacement), tree[2])
    if branch == 2:
        return (tree[0], tree[1], replace(tree[2], path[1:], replacement))
    raise ValueError(path)


def neighbour_tables(tree: Tree, target: int) -> set[int]:
    neighbours: set[int] = set()
    for path, subtree in walk(tree):
        neighbours.add(evaluate(replace(tree, path, ("N", subtree))))
        if isinstance(subtree, str):
            for leaf in LEAF_NAMES:
                if leaf != subtree:
                    neighbours.add(evaluate(replace(tree, path, leaf)))
        elif subtree[0] == "N":
            neighbours.add(evaluate(replace(tree, path, subtree[1])))
        else:
            for operator in BINARY_NAMES:
                if operator != subtree[0]:
                    neighbours.add(
                        evaluate(
                            replace(
                                tree,
                                path,
                                (operator, subtree[1], subtree[2]),
                            )
                        )
                    )
    neighbours.discard(target)
    return neighbours


def average_ranks(values: Sequence[float]) -> list[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    result = [0.0] * len(values)
    start = 0
    while start < len(ordered):
        stop = start + 1
        while stop < len(ordered) and ordered[stop][1] == ordered[start][1]:
            stop += 1
        mean_rank = ((start + 1) + stop) / 2.0
        for offset in range(start, stop):
            result[ordered[offset][0]] = mean_rank
        start = stop
    return result


def correlation(first: Sequence[float], second: Sequence[float]) -> float:
    first_mean = sum(first) / len(first)
    second_mean = sum(second) / len(second)
    first_delta = [value - first_mean for value in first]
    second_delta = [value - second_mean for value in second]
    denominator = math.sqrt(
        sum(value * value for value in first_delta)
        * sum(value * value for value in second_delta)
    )
    return sum(a * b for a, b in zip(first_delta, second_delta)) / denominator


def quantile(values: Sequence[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    upper_weight = position - lower
    return float(
        ordered[lower] * (1.0 - upper_weight)
        + ordered[upper] * upper_weight
    )


def main(run_directory: Path) -> int:
    errors: list[str] = []
    levels = independently_enumerate_minima()
    expected: dict[int, tuple[int, str]] = {}
    for cost, level in enumerate(levels):
        for value, text in level.items():
            expected[value] = (cost, text)

    battery = fixed_battery()
    expected_domain: dict[int, dict[str, object]] = {}
    expected_counts: dict[int, int] = defaultdict(int)
    for value, (cost, text) in expected.items():
        if cost == 0:
            continue
        tree = parse_all(text)
        if evaluate(tree) != value:
            errors.append(f"independent expression evaluation failed for {value:04x}")
            continue
        neighbours = neighbour_tables(tree, value)
        if len(neighbours) < 4:
            continue
        failing = sum(
            1
            for neighbour in neighbours
            if any(((neighbour ^ value) >> row) & 1 for row in battery)
        )
        rigidity = failing / len(neighbours)
        expected_domain[value] = {
            "distance": cost,
            "canonical_expression": text,
            "neighbour_count": len(neighbours),
            "failing_neighbour_count": failing,
            "rigidity": rigidity,
        }
        expected_counts[cost] += 1

    csv_path = run_directory / "F1-AR-BOOL4-001-targets.csv"
    with csv_path.open(newline="", encoding="utf-8") as handle:
        saved_rows = list(csv.DictReader(handle))
    saved_by_value = {
        int(row["truth_table_hex"], 16): row
        for row in saved_rows
    }

    missing = sorted(set(expected_domain) - set(saved_by_value))
    unexpected = sorted(set(saved_by_value) - set(expected_domain))
    if missing:
        errors.append(f"missing target rows: {len(missing)}; first={missing[:10]}")
    if unexpected:
        errors.append(f"unexpected target rows: {len(unexpected)}; first={unexpected[:10]}")

    row_mismatches = 0
    for value in sorted(set(expected_domain) & set(saved_by_value)):
        expected_row = expected_domain[value]
        saved = saved_by_value[value]
        mismatches: list[str] = []
        if int(saved["distance"]) != expected_row["distance"]:
            mismatches.append("distance")
        if saved["canonical_expression"] != expected_row["canonical_expression"]:
            mismatches.append("canonical_expression")
        if int(saved["neighbour_count"]) != expected_row["neighbour_count"]:
            mismatches.append("neighbour_count")
        if int(saved["failing_neighbour_count"]) != expected_row["failing_neighbour_count"]:
            mismatches.append("failing_neighbour_count")
        if abs(float(saved["rigidity"]) - float(expected_row["rigidity"])) > 1e-15:
            mismatches.append("rigidity")
        if mismatches:
            row_mismatches += 1
            if row_mismatches <= 20:
                errors.append(f"row mismatch {value:04x}: {','.join(mismatches)}")

    distances = [float(expected_domain[value]["distance"]) for value in sorted(expected_domain)]
    rigidities = [float(expected_domain[value]["rigidity"]) for value in sorted(expected_domain)]
    rho = correlation(average_ranks(distances), average_ranks(rigidities))
    q1 = quantile(rigidities, 0.25)
    q3 = quantile(rigidities, 0.75)
    iqr = q3 - q1
    grouped: dict[int, list[float]] = defaultdict(list)
    for value in expected_domain:
        grouped[int(expected_domain[value]["distance"])].append(
            float(expected_domain[value]["rigidity"])
        )
    medians = {
        str(cost): quantile(grouped[cost], 0.5)
        for cost in sorted(grouped)
    }
    represented = sorted(grouped)
    strictly_decreasing = all(
        medians[str(later)] < medians[str(earlier)]
        for earlier, later in zip(represented, represented[1:])
    )
    verdict = (
        "SURVIVED THIS CUT"
        if not errors and rho >= 0.20 and iqr >= 0.10 and not strictly_decreasing
        else "REFUTED ON THIS DECLARED DOMAIN"
    )

    saved_summary = json.loads(
        (run_directory / "F1-AR-BOOL4-001-summary.json").read_text(encoding="utf-8")
    )
    comparisons = {
        "minimum_function_count_by_distance_match": {
            str(cost): len(levels[cost])
            for cost in range(MAX_OPERATOR_COST + 1)
        } == saved_summary["generated_function_count_by_minimum_distance"],
        "total_minimum_function_count_match": len(expected)
        == saved_summary["generated_function_count_total"],
        "declared_domain_membership_match": not missing and not unexpected,
        "declared_target_count_match": len(expected_domain)
        == saved_summary["declared_target_count"],
        "target_count_by_distance_match": {
            str(cost): expected_counts[cost]
            for cost in sorted(expected_counts)
        } == saved_summary["target_count_by_distance"],
        "all_saved_rows_match": row_mismatches == 0,
        "battery_match": battery == saved_summary["battery_indices"],
        "rho_match": abs(rho - saved_summary["spearman_rho"]) < 1e-15,
        "q1_match": abs(q1 - saved_summary["rigidity_q1"]) < 1e-15,
        "q3_match": abs(q3 - saved_summary["rigidity_q3"]) < 1e-15,
        "iqr_match": abs(iqr - saved_summary["rigidity_iqr"]) < 1e-15,
        "medians_match": all(
            abs(medians[key] - saved_summary["median_rigidity_by_distance"][key]) < 1e-15
            for key in medians
        ),
        "verdict_match": verdict == saved_summary["verdict"],
    }
    passed = not errors and all(comparisons.values())
    report = {
        "audit": "independent full-domain enumeration",
        "passed": passed,
        "independently_enumerated_minimum_functions": len(expected),
        "independently_rebuilt_declared_targets": len(expected_domain),
        "row_mismatch_count": row_mismatches,
        "recomputed_spearman_rho": rho,
        "recomputed_rigidity_iqr": iqr,
        "recomputed_verdict": verdict,
        "comparisons": comparisons,
        "errors": errors[:100],
    }
    output_path = run_directory / "F1-AR-BOOL4-001-full-domain-verification.json"
    output_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_f1_ar_bool4_001_full_domain.py RUN_DIRECTORY")
    raise SystemExit(main(Path(sys.argv[1])))
