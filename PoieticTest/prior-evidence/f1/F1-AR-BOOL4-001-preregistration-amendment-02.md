# F1-AR-BOOL4-001 Preregistration Amendment 02

**Frozen before execution:** 2026-08-19, Australia/Brisbane  
**Reason:** make representation and descriptive-statistic conventions unique.  
**Outcome access before amendment:** none; the experiment code had not been run.

Input row `i` is the four-bit assignment whose `xj` value is bit `j` of `i`, so `x0` is least significant. Truth-table bit `i` is the output on row `i`.

The exact ASCII prefix encodings are `0`, `1`, `x0`, `x1`, `x2`, `x3`, `N(e)`, `A(e1,e2)`, `O(e1,e2)`, and `X(e1,e2)`. For commutative binary nodes, children are ordered by ordinary bytewise ASCII lexicographic order before encoding. Canonical ties use that same order.

Spearman correlation is Pearson correlation of average ranks, with equal values receiving their mean rank. Quartiles use the linear interpolation convention with rank position `(n-1)q` for `q=0.25` and `q=0.75`. Medians use the corresponding `q=0.5` convention. “Strictly decreasing across all adjacent represented distances” means every later distance-bin median is numerically smaller than the immediately preceding represented distance-bin median.

This amendment changes no domain, statistic, threshold, exclusion, or verdict rule.
