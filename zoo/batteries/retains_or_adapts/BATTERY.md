# Battery: RetainsOrAdapts

Term: RetainsOrAdapts (inventory section 22, N20 row, D21 family).
A cross-environment variant-to-environment claim in the extended frame:
a variant v, defined in environment U, when placed in a different
environment U', either retains its behavior (same behavior, still
appropriate) or adapts it (changes behavior to match what U' requires).

Sorts used across instances:
- V  : variants
- E  : environments
- B  : behaviors
- O  : outcomes {pass, fail}
- I  : inputs (where relevant)
- T  : test-suite members (where relevant)

Relations used across instances:
- defined_in(v, U)      : v originates in U
- placed_in(v, U')      : v is deployed in U'
- behavior(v, E, b)     : v exhibits behavior b in E
- behavior_on(v, E, i, o): outcome of v on input i in E
- requires(E, b)        : E demands behavior b
- test_suite(E, t)      : t is a test member for E

---

### P1 - Retains behavior unchanged

```
Sorts:
  V = {v1}
  E = {U, Up}
  B = {sort_ascending}
  O = {pass, fail}

Relations:
  defined_in  = {(v1, U)}
  placed_in   = {(v1, U), (v1, Up)}
  behavior    = {(v1, U, sort_ascending), (v1, Up, sort_ascending)}
  requires    = {(U, sort_ascending), (Up, sort_ascending)}
  outcome     = {(v1, U, pass), (v1, Up, pass)}

Claim: RetainsOrAdapts(v1, U, Up) HOLDS.
Reason: behavior(v1, Up) = behavior(v1, U) = sort_ascending,
        and requires(Up, sort_ascending).  Variant retains.
```

### N1 - Behavior degrades, neither retained nor adapted

```
Sorts:
  V = {v1}
  E = {U, Up}
  B = {sort_ascending, sort_descending}
  O = {pass, fail}

Relations:
  defined_in  = {(v1, U)}
  placed_in   = {(v1, U), (v1, Up)}
  behavior    = {(v1, U, sort_ascending), (v1, Up, sort_descending)}
  requires    = {(U, sort_ascending), (Up, sort_ascending)}
  outcome     = {(v1, U, pass), (v1, Up, fail)}

Claim: RetainsOrAdapts(v1, U, Up) does NOT hold.
Difference from P1: behavior(v1, Up) = sort_descending != sort_ascending.
  Not retained (differs from U), and not adapted (sort_descending does not
  match requires(Up) = sort_ascending).  Behavior degraded arbitrarily.
```

---

### P2 - Adapts behavior to match new environment

```
Sorts:
  V = {v2}
  E = {U, Up}
  B = {sort_ascending, sort_descending}
  O = {pass, fail}

Relations:
  defined_in  = {(v2, U)}
  placed_in   = {(v2, U), (v2, Up)}
  behavior    = {(v2, U, sort_ascending), (v2, Up, sort_descending)}
  requires    = {(U, sort_ascending), (Up, sort_descending)}
  outcome     = {(v2, U, pass), (v2, Up, pass)}

Claim: RetainsOrAdapts(v2, U, Up) HOLDS.
Reason: behavior(v2, Up) = sort_descending, and requires(Up, sort_descending).
  Behavior changed from U to Up, but the change matches what Up requires.
  Variant adapts.
```

### N2 - Adapts to wrong environment conventions

```
Sorts:
  V = {v2}
  E = {U, Up, Upp}
  B = {sort_ascending, sort_descending}
  O = {pass, fail}

Relations:
  defined_in  = {(v2, U)}
  placed_in   = {(v2, U), (v2, Up)}
  behavior    = {(v2, U, sort_ascending), (v2, Up, sort_descending)}
  requires    = {(U, sort_ascending), (Up, sort_ascending), (Upp, sort_descending)}
  outcome     = {(v2, U, pass), (v2, Up, fail)}

Claim: RetainsOrAdapts(v2, U, Up) does NOT hold.
Difference from P2: requires(Up) = sort_ascending (not sort_descending).
  The variant changed behavior to sort_descending, which matches Upp, not Up.
  Adaptation targets the wrong environment; outcome(v2, Up) = fail.
```

---

### P3 - Retains core logic, adapts surface arity

```
Sorts:
  V = {v3}
  E = {U, Up}
  B = {compare_pairs, compare_triples}
  O = {pass, fail}

Relations:
  defined_in     = {(v3, U)}
  placed_in      = {(v3, U), (v3, Up)}
  behavior       = {(v3, U, compare_pairs), (v3, Up, compare_triples)}
  requires       = {(U, compare_pairs), (Up, compare_triples)}
  outcome        = {(v3, U, pass), (v3, Up, pass)}
  core_unchanged = {(v3, U, Up)}

Claim: RetainsOrAdapts(v3, U, Up) HOLDS.
Reason: core comparison logic is unchanged (core_unchanged); surface arity
  adapted from compare_pairs to compare_triples to match requires(Up).
  Both retention (core) and adaptation (arity) are present.
```

### N3 - No source environment to retain or adapt from

```
Sorts:
  V = {v3}
  E = {U, Up}
  B = {compare_pairs, compare_triples}
  O = {pass, fail}

Relations:
  defined_in     = {}
  placed_in      = {(v3, Up)}
  behavior       = {(v3, Up, compare_triples)}
  requires     = {(U, compare_pairs), (Up, compare_triples)}
  outcome        = {(v3, Up, pass)}
  core_unchanged = {}

Claim: RetainsOrAdapts(v3, U, Up) does NOT hold.
Difference from P3: defined_in(v3, U) is absent; v3 is never placed_in U.
  There is no source behavior in U to retain or adapt from, so the
  cross-environment claim has no anchor.
```

---

### N4 - Too-weak wall: finite-suite success extends to U'

The too-weak reading admits this instance: a variant passes a finite
test suite in U, and that finite success is taken as evidence of
retention in Up.  The intended reading must EXCLUDE it because the
finite suite does not cover the input on which behavior actually
diverges.

```
Sorts:
  V = {v4}
  E = {U, Up}
  B = {sort_ascending}
  O = {pass, fail}
  I = {empty, singleton, multi}
  T = {empty, singleton}

Relations:
  defined_in   = {(v4, U)}
  placed_in    = {(v4, U), (v4, Up)}
  test_suite   = {(U, empty), (U, singleton)}
  behavior_on  = {(v4, U, empty, pass),
                  (v4, U, singleton, pass),
                  (v4, U, multi, pass),
                  (v4, Up, empty, pass),
                  (v4, Up, singleton, pass),
                  (v4, Up, multi, fail)}
  requires     = {(U, sort_ascending), (Up, sort_ascending)}

Too-weak reading: ADMITS RetainsOrAdapts(v4, U, Up).
  Justification: v4 passes test_suite(U) = {empty, singleton} in U,
  and also passes those same inputs in Up, so finite-suite success
  "extends."

Intended reading: EXCLUDES RetainsOrAdapts(v4, U, Up).
  Justification: behavior_on(v4, Up, multi) = fail !=
  behavior_on(v4, U, multi) = pass.  Behavior is not retained on the
  uncovered input, and the finite suite does not test it.  Finite-suite
  success is insufficient evidence of retention.
```

---

### P4 - Too-strong wall: always fails outside U

The too-strong reading excludes this instance: it demands that any
variant outside U must fail.  The intended reading must ADMIT it
because the variant adapts successfully in Up.

```
Sorts:
  V = {v5}
  E = {U, Up}
  B = {sort_ascending, sort_descending}
  O = {pass, fail}

Relations:
  defined_in  = {(v5, U)}
  placed_in   = {(v5, U), (v5, Up)}
  behavior    = {(v5, U, sort_ascending), (v5, Up, sort_descending)}
  requires    = {(U, sort_ascending), (Up, sort_descending)}
  outcome     = {(v5, U, pass), (v5, Up, pass)}

Too-strong reading: EXCLUDES RetainsOrAdapts(v5, U, Up).
  Justification: v5 is placed_in Up (outside U) and outcome(v5, Up) = pass.
  The too-strong reading says "always fails outside U," so any success
  outside U is forbidden.

Intended reading: ADMITS RetainsOrAdapts(v5, U, Up).
  Justification: behavior(v5, Up) = sort_descending = requires(Up).
  The variant adapted from sort_ascending to sort_descending and
  succeeded.  RetainsOrAdapts includes successful adaptation, not
  just retention.
```

---

### B1 - OPEN: retention in a vacuous environment

```
Sorts:
  V = {v6}
  E = {U, Up}
  B = {sort_ascending}
  O = {pass, fail}

Relations:
  defined_in  = {(v6, U)}
  placed_in   = {(v6, U), (v6, Up)}
  behavior    = {(v6, U, sort_ascending), (v6, Up, sort_ascending)}
  requires    = {(U, sort_ascending)}
  outcome     = {(v6, U, pass), (v6, Up, pass)}

OPEN: Does RetainsOrAdapts(v6, U, Up) hold when Up imposes no
  behavioral requirement (requires has no entry for Up)?
  The variant technically retains: behavior(v6, Up) = behavior(v6, U).
  But retention in a vacuous environment -- one that accepts any
  behavior -- may not count as meaningful cross-environment retention,
  because the "or adapts" disjunct is trivially satisfied by any
  behavior and the "retains" disjunct carries no environmental
  constraint to retain against.
  Question: is a vacuous target environment a valid test of
  RetainsOrAdapts, or does the term require Up to impose at least
  one behavioral requirement?
```

---

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | 2c2795cf7bdb6cf3 |
| N1 | near-miss | P1 | c1e1d40b49720d89 |
| P2 | positive | N2 | 0b0a1e0c115e1a88 |
| N2 | near-miss | P2 | 5aa171250caf6faf |
| P3 | positive | N3 | bfa45c2cadb1b4da |
| N3 | near-miss | P3 | 966cc657172ef815 |
| N4 | near-miss | - | ba22d826601c685a |
| P4 | positive | - | 33174aebc55d2953 |
| B1 | boundary | - | 87536bcf2857cbad |
