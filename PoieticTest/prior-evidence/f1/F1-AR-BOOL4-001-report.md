# F1-AR-BOOL4-001 Experimental Report

## Verdict

**REFUTED ON THIS DECLARED DOMAIN**

The former positive Spark C1 conjecture predicted that, within a fixed repertoire and appraisal geometry, greater contextual assembly distance would tend to accompany greater local delivery rigidity. This experiment found the opposite weak tendency and a near-saturated rigidity instrument. The result defeats that positive-direction conjecture on the frozen Boolean-expression domain. It neither establishes a universal negative law nor reaches any other Spark or Poietic claim.

## Why this experiment was run first

F1 was selected because it could be executed exhaustively without constructing a simulation whose architecture already presupposed A5 or the bridge. Every target in the declared finite domain could be generated, every local edit could be evaluated, and the verdict could be computed without sampling a convenient subset after seeing outcomes.

The protocol was frozen before execution. Two amendments were also frozen before execution, solely to specify the SHA-256 battery procedure and the exact representation, rank, and quantile conventions. Neither amendment changed the domain, statistic, threshold, exclusion, or verdict rule.

## Frozen domain and instrument

The repertoire used four Boolean inputs, leaves `0`, `1`, `x0`, `x1`, `x2`, `x3`, unary `NOT`, and binary `AND`, `OR`, and `XOR`. Targets were all truth tables with a minimum canonical expression containing one through five operator nodes and at least four gauge-inequivalent one-site neighbours. Gauge equivalence was equality on the complete sixteen-row truth table.

Assembly distance was the exact minimum operator count. Local edits replaced leaves or binary operators, inserted `NOT` above a subtree, or removed a `NOT`. Delivery was scored on one fixed eight-row battery generated from the frozen seed. The full truth table was used only for gauge quotienting and exhaustive construction.

The primary statistic was Spearman rank correlation between minimum assembly distance and local delivery rigidity. Survival required correlation at least 0.20, rigidity IQR at least 0.10, and no strictly decreasing sequence of distance-bin medians. Failure of that rule in a valid completed run meant refutation on the declared domain.

## Results

| Quantity | Result |
|---|---:|
| Declared targets | 14,451 |
| Battery indices | 3, 15, 11, 8, 9, 10, 7, 6 |
| Spearman correlation | -0.0995637588 |
| Rigidity Q1 | 0.8787878788 |
| Rigidity Q3 | 0.9687500000 |
| Rigidity IQR | 0.0899621212 |
| Verification errors | 0 |
| Preregistered verdict | REFUTED ON THIS DECLARED DOMAIN |

| Minimum distance | Targets | Median rigidity | Mean rigidity | Fraction with rigidity 1 |
|---:|---:|---:|---:|---:|
| 1 | 22 | 1.000000 | 0.988636 | 0.863636 |
| 2 | 126 | 1.000000 | 0.963981 | 0.642857 |
| 3 | 691 | 0.960000 | 0.935920 | 0.403763 |
| 4 | 3,031 | 0.937500 | 0.918403 | 0.234576 |
| 5 | 10,581 | 0.935484 | 0.915837 | 0.127020 |

Both load-bearing survival thresholds failed. The correlation was negative rather than at least 0.20, and the IQR was below 0.10. Median rigidity was maximal at distances one and two, then declined across distances three through five.

## Interpretation

The clean conclusion is narrow: minimum assembly distance did not predict greater local delivery rigidity in this domain. The observed relation was weakly reversed.

The high rigidity values also expose a measurement problem. Canonical minimum expressions are already stripped of much redundant structure, so many one-site edits disrupt at least one demand. At larger expressions there are more distinct edits that alter only rows outside the partial battery, which can lower measured rigidity even while assembly distance rises. On this geometry, rigidity behaves at least partly as a property of the chosen canonicalization, edit neighbourhood, and finite battery rather than as a monotone shadow of construction difficulty.

That interpretation is not a replacement theorem. The run did not preregister a causal decomposition of the negative association, and it did not compare alternative batteries or representation classes. Those would be new experiments.

## Consequence for revision 1.3

Revision 1.3 withdraws the positive C1 conjecture and retains only the empirical question: under which repertoires and instruments, if any, does assembly distance predict local rigidity, and in which direction? The definitions of assembly distance and rigidity survive. No inverse law is added.

This is the intended asymmetry between criticism and administration. The experiment changed the content because it found a counterdomain. No ledger, inherited weight, or status rule protected the failed conjecture.

## Reproducibility

The frozen-before-execution manifest has SHA-256 `6e00f485171e374c987018e23ab7acab449b8f98a7879c90c962138d973d0398`. The preregistration hash is `d27f105cc365951e40256ab2345a047e25c3bf7412d33d666fdfed06f9777fec`; amendment hashes are `07370a43584deaaab53792773c00f16c58f1947547229e9a3f14ea1c8c1569ba` and `f6fa8d072e8df4215dfb2772be4e69ad5229abd63f56f8602a45a90e94134137`; the frozen execution code hash is `9e5d4c1aa230b909ad69d2e46e60b878d64e537c0a4c6e698033ab472306b689`.

The first run produced target-table hash `751a6d1aac959a543ae5d59a5bca3acf53cd42e4f419e2d1247065932df2abc0`, summary hash `4b0a1d81c258336ca799957dde408e7292cfbb31aff582a3ca4b583b7dce4cae`, and verdict hash `f29e02a701ada65a4d5475ba3f6f2fb128721639b1cfee764537b162f06beffc`. A clean-process verifier recomputed all 14,451 saved rows with zero discrepancies. A separately written full-domain verifier then re-enumerated all 14,457 minimum functions through distance five, rebuilt the complete 14,451-target declared domain, found no omitted or extra targets, matched every canonical expression and neighbourhood, and reproduced the verdict. Its report has SHA-256 `8cf7a6e2155d10302444369d0de09bdd1b27c27d68a6372265f5f0358b7809d5`; the verifier source has SHA-256 `c2b7924b78f002b20e83d6b5f2d2fe841c689544f68892f2cfdc55520d24f899`. A complete second execution reproduced the original target-table, summary, and verdict hashes exactly.

## Scope

The verdict applies only to the declared four-input Boolean-tree repertoire, operator-distance cap, canonical minimum representation, one-site edit graph, and fixed eight-row battery. It does not refute every possible assembly–rigidity relation. It does refute the former conjecture on a large, exhaustive, preregistered counterdomain, which is sufficient reason not to retain the positive direction as a general expectation.
