# F1-AR-BOOL4-001 Preregistration

**Frozen:** 2026-08-19, Australia/Brisbane  
**Kernel target:** Spark Conjecture C1, assembly–rigidity relation  
**Protocol family:** F1, assembly–rigidity challenge  
**Status at freeze:** NOT EXECUTED

## Question

Within a finite, exhaustively generated Boolean-expression domain, does greater minimum contextual assembly distance accompany greater local delivery rigidity under one fixed partial appraisal battery?

## Declared domain

Targets are Boolean functions on four inputs, represented by 16-bit truth tables. The expression repertoire has leaves `0`, `1`, `x0`, `x1`, `x2`, `x3`; unary operator `NOT`; and binary operators `AND`, `OR`, `XOR`. Expressions are rooted trees without shared subgraphs.

The target family is every gauge-inequivalent truth table whose minimum operator-node count is between 1 and 5 inclusive and for which the canonical minimum expression has at least four gauge-inequivalent local neighbours under the edit graph below. Gauge equivalence is equality of the complete 16-row truth table.

The canonical expression for a truth table is the lexicographically least prefix encoding among expressions at the minimum operator count found by exhaustive dynamic programming. Commutative binary children are stored in lexicographic order.

## Assembly distance

For target `a`, contextual assembly distance is the minimum number of operator nodes in any expression generating its full truth table from the declared leaves and operators. Leaves have distance 0. No target transcript is admitted as a construction leaf.

## Transcript and appraisal battery

One battery `F°` is generated before target enumeration by taking the first eight distinct input indices obtained from repeated SHA-256 blocks of the ASCII seed:

`SPARK-F1-AR-BOOL4-001-BATTERY`

Indices are reduced modulo 16 and duplicates are skipped. The battery demands exact agreement with the target on those eight inputs. The same battery is used for every target. The full truth table is used only for gauge quotienting and minimum-distance construction, not for delivery scoring.

## Local edit graph

A local edit changes exactly one syntax site of the canonical minimum expression by one of the following operations:

1. Replace a leaf with any other declared leaf.
2. Replace a binary operator with either of the other two binary operators while preserving its children.
3. Insert `NOT` immediately above any selected subtree.
4. Remove a selected `NOT` node, replacing it by its child.

Malformed edits are excluded. Edited expressions are evaluated on the full truth table, then quotiented by truth-table equality. The identity gauge class is excluded from the neighbour set.

## Local delivery rigidity

For target `a`, local delivery rigidity is the fraction of its unique gauge-inequivalent neighbour truth tables that fail at least one demand in `F°`. A neighbour that differs from `a` only outside `F°` remains delivered on this instrument and counts as non-rigid for this run.

## Budgets and exclusions

Construction is exhaustive through operator distance 5. Every canonical target receives all valid one-site edits. No failed construction, target, or neighbour is censored after outcomes are known. Targets with fewer than four gauge-inequivalent neighbours are excluded by the domain rule fixed above. There is no learned representation, external solver, target-specific decoder, or post-outcome repertoire change.

## Primary statistic and decision rule

The primary statistic is Spearman's rank correlation `rho` between minimum assembly distance and local delivery rigidity over the complete declared target family.

C1 **SURVIVES THIS CUT** only if all three conditions hold:

- `rho >= 0.20`;
- rigidity is non-degenerate, defined as interquartile range at least `0.10`;
- the median rigidity at each represented distance does not form a strictly decreasing sequence across all adjacent represented distances.

C1 is **REFUTED ON THIS DECLARED DOMAIN** if the survival rule fails while the run remains valid. The result is **INCONCLUSIVE** only if implementation verification fails, exhaustive generation does not complete, or an ambiguity in the frozen definitions prevents a unique calculation.

No p-value is used because the declared finite domain is exhaustively enumerated rather than sampled. A bootstrap interval may be reported descriptively but does not control the verdict.

## Verification checks

The implementation must verify:

- every stored expression evaluates to its indexed truth table;
- no truth table receives a later canonical expression at a larger distance;
- every generated neighbour differs from the target truth table;
- recomputation from the saved canonical-expression table reproduces every rigidity value;
- a second clean process reproduces the summary and verdict from saved artifacts.

## Scope of inference

The verdict applies only to this Boolean-tree repertoire, this distance cap, this canonicalization rule, this edit graph, and this fixed eight-input battery. Survival would not confirm C1 generally. Refutation would defeat C1 on this declared domain and reveal which part of the conjecture or instrument requires revision.
