#!/usr/bin/env python3
"""Clean-process verification of saved F1-AR-BOOL4-001 artifacts."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Sequence

ROWS = 16
MASK = (1 << ROWS) - 1
LEAVES = ("0", "1", "x0", "x1", "x2", "x3")
OPS = ("A", "O", "X")
SEED = b"SPARK-F1-AR-BOOL4-001-BATTERY"


def varmask(j: int) -> int:
    return sum(1 << i for i in range(ROWS) if (i >> j) & 1)


LM = {"0": 0, "1": MASK, **{f"x{j}": varmask(j) for j in range(4)}}


def battery() -> list[int]:
    out: list[int] = []
    seen: set[int] = set()
    c = 0
    while len(out) < 8:
        for byte in hashlib.sha256(SEED + b":" + str(c).encode("ascii")).digest():
            i = byte % 16
            if i not in seen:
                seen.add(i)
                out.append(i)
                if len(out) == 8:
                    break
        c += 1
    return out


def parse(s: str, p: int = 0):
    if s.startswith("x", p):
        return s[p:p+2], p + 2
    if s[p] in "01":
        return s[p], p + 1
    op = s[p]
    assert s[p+1] == "("
    a, q = parse(s, p + 2)
    if op == "N":
        assert s[q] == ")"
        return ("N", a), q + 1
    assert s[q] == ","
    b, q = parse(s, q + 1)
    assert s[q] == ")"
    return (op, a, b), q + 1


def ev(n) -> int:
    if isinstance(n, str):
        return LM[n]
    if n[0] == "N":
        return (~ev(n[1])) & MASK
    a, b = ev(n[1]), ev(n[2])
    return a & b if n[0] == "A" else a | b if n[0] == "O" else a ^ b


def paths(n, p=()):
    yield p, n
    if isinstance(n, tuple):
        yield from paths(n[1], p + (1,))
        if n[0] != "N":
            yield from paths(n[2], p + (2,))


def rep(n, p, v):
    if not p:
        return v
    if n[0] == "N":
        return ("N", rep(n[1], p[1:], v))
    return (n[0], rep(n[1], p[1:], v), n[2]) if p[0] == 1 else (n[0], n[1], rep(n[2], p[1:], v))


def neighbours(n, target: int) -> set[int]:
    out: set[int] = set()
    for p, sub in paths(n):
        out.add(ev(rep(n, p, ("N", sub))))
        if isinstance(sub, str):
            for leaf in LEAVES:
                if leaf != sub:
                    out.add(ev(rep(n, p, leaf)))
        elif sub[0] == "N":
            out.add(ev(rep(n, p, sub[1])))
        else:
            for op in OPS:
                if op != sub[0]:
                    out.add(ev(rep(n, p, (op, sub[1], sub[2]))))
    out.discard(target)
    return out


def ranks(v: Sequence[float]) -> list[float]:
    z = sorted(enumerate(v), key=lambda x: x[1])
    r = [0.0] * len(v)
    i = 0
    while i < len(z):
        j = i + 1
        while j < len(z) and z[j][1] == z[i][1]:
            j += 1
        a = ((i + 1) + j) / 2
        for k in range(i, j):
            r[z[k][0]] = a
        i = j
    return r


def corr(a: Sequence[float], b: Sequence[float]) -> float:
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    da, db = [x-ma for x in a], [x-mb for x in b]
    return sum(x*y for x,y in zip(da,db)) / math.sqrt(sum(x*x for x in da)*sum(y*y for y in db))


def quant(v: Sequence[float], q: float) -> float:
    s = sorted(v)
    x = (len(s)-1)*q
    lo, hi = math.floor(x), math.ceil(x)
    return float(s[lo]) if lo == hi else s[lo]*(hi-x)+s[hi]*(x-lo)


def main(run_dir: Path) -> int:
    rows = list(csv.DictReader((run_dir / "F1-AR-BOOL4-001-targets.csv").open(encoding="utf-8")))
    b = battery()
    d: list[float] = []
    r: list[float] = []
    errors: list[str] = []
    groups: dict[int, list[float]] = defaultdict(list)
    for row in rows:
        target = int(row["truth_table_hex"], 16)
        node, end = parse(row["canonical_expression"])
        if end != len(row["canonical_expression"]):
            errors.append(f"parse tail {row['truth_table_hex']}")
            continue
        if ev(node) != target:
            errors.append(f"eval {row['truth_table_hex']}")
        ns = neighbours(node, target)
        fail = sum(1 for x in ns if any(((x ^ target) >> i) & 1 for i in b))
        rigidity = fail / len(ns)
        if len(ns) != int(row["neighbour_count"]):
            errors.append(f"neighbour count {row['truth_table_hex']}")
        if fail != int(row["failing_neighbour_count"]):
            errors.append(f"failure count {row['truth_table_hex']}")
        if abs(rigidity - float(row["rigidity"])) > 1e-15:
            errors.append(f"rigidity {row['truth_table_hex']}")
        distance = int(row["distance"])
        d.append(float(distance)); r.append(rigidity); groups[distance].append(rigidity)
    rho = corr(ranks(d), ranks(r))
    iqr = quant(r, .75) - quant(r, .25)
    meds = {str(k): quant(groups[k], .5) for k in sorted(groups)}
    ks = sorted(groups)
    dec = len(ks) >= 2 and all(meds[str(b)] < meds[str(a)] for a,b in zip(ks,ks[1:]))
    verdict = "SURVIVED THIS CUT" if (not errors and rho >= .2 and iqr >= .1 and not dec) else "REFUTED ON THIS DECLARED DOMAIN"
    saved = json.loads((run_dir / "F1-AR-BOOL4-001-summary.json").read_text(encoding="utf-8"))
    comparisons = {
        "battery_match": b == saved["battery_indices"],
        "target_count_match": len(rows) == saved["declared_target_count"],
        "rho_match": abs(rho - saved["spearman_rho"]) < 1e-15,
        "iqr_match": abs(iqr - saved["rigidity_iqr"]) < 1e-15,
        "medians_match": all(abs(meds[k] - saved["median_rigidity_by_distance"][k]) < 1e-15 for k in meds),
        "verdict_match": verdict == saved["verdict"],
        "row_recalculation_errors": len(errors),
    }
    passed = all(v is True for k,v in comparisons.items() if k != "row_recalculation_errors") and not errors
    report = {"passed": passed, "recomputed_verdict": verdict, "comparisons": comparisons, "errors": errors[:100]}
    out = run_dir / "F1-AR-BOOL4-001-clean-process-verification.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1])))
