# Battery: Pass (T3 cluster, family D13)

Term: Pass(u) -- survived severe testing over finite suite L, a finite
subset of Theory_eta.  No pin candidate; bare Pass(u) is definable
without any critical package (FCritPkg tests critical packages, not
theory-suite membership).  Source: POPPER_LSCD sections 18, 29-30;
inventory section 3, calculus 63, N8 row.

Intended reading: Pass(u) iff u is in the finite suite L, at least one
test was run on u, and every test run on u had outcome pass.

Too-weak wall (N4): Pass = mere inL membership -- a u in L that failed
its test is wrongly admitted.

Too-strong wall (P4): Pass = survival against every test in Theory_eta
(or derivability from Theory_eta) -- a u that survived the finite suite
L but has not faced tests outside L is wrongly excluded.

### P1 - Single element passes single test

Sorts:
  Elem = {a}
  Test = {t1}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a}
  ran = {(t1, a)}
  result = {(t1, a) -> pass}

Intended Pass = {a}

### N1 - Same as P1, test outcome fail

Sorts:
  Elem = {a}
  Test = {t1}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a}
  ran = {(t1, a)}
  result = {(t1, a) -> fail}

Intended Pass = {}

Difference from P1: result(t1, a) = fail (was pass).

### P2 - Two elements each pass their test

Sorts:
  Elem = {a, b}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a, b}
  inEta = {a, b}
  ran = {(t1, a), (t2, b)}
  result = {(t1, a) -> pass, (t2, b) -> pass}

Intended Pass = {a, b}

### N2 - Same as P2, second element never examined

Sorts:
  Elem = {a, b}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a, b}
  inEta = {a, b}
  ran = {(t1, a)}
  result = {(t1, a) -> pass}

Intended Pass = {a}

Difference from P2: ran(t2, b) removed (b was never examined; present in P2).

### P3 - Element in L passes two tests, witness outside L

Sorts:
  Elem = {a, c}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a, c}
  ran = {(t1, a), (t2, a)}
  result = {(t1, a) -> pass, (t2, a) -> pass}

Intended Pass = {a}

N8 shape: for-all u in L Pass(u) (a passes); exists u* in Theory_eta
minus L with NOT Pass(u*) (c is outside L, untested, NOT Pass(c)).

### N3 - Same as P3, second test fails

Sorts:
  Elem = {a, c}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a, c}
  ran = {(t1, a), (t2, a)}
  result = {(t1, a) -> pass, (t2, a) -> fail}

Intended Pass = {}

Difference from P3: result(t2, a) = fail (was pass).

### P4 - TOO-STRONG WALL: survived finite suite L with failure outside L (N8 shape)

Sorts:
  Elem = {a, c}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a, c}
  ran = {(t1, a), (t2, c)}
  result = {(t1, a) -> pass, (t2, c) -> fail}

Intended Pass = {a}

Wall role: too-strong.  The too-strong reading (Pass = survival against
every test in Theory_eta) excludes a because a has not faced t2, a test
in the broader theory.  The correct reading admits a: a is in L,
was tested, and passed.  c is in Theory_eta minus L, was tested with
t2, and failed -- the N8 existential witness.

### N4 - TOO-WEAK WALL: element in L failed test, wrongly treated as Pass

Sorts:
  Elem = {a, c}
  Test = {t1, t2}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a, c}
  ran = {(t1, a), (t2, c)}
  result = {(t1, a) -> fail, (t2, c) -> fail}

Intended Pass = {}

Difference from P4: result(t1, a) = fail (was pass).

Wall role: too-weak.  The too-weak reading (Pass = mere inL membership)
admits a because a is in L, ignoring the failed test.  The correct
reading excludes a: a failed its test.

### B1 - OPEN: element outside L tested and passed

Sorts:
  Elem = {a, c}
  Test = {t1}
  Verdict = {pass, fail}

Relations:
  inL = {a}
  inEta = {a, c}
  ran = {(t1, a), (t1, c)}
  result = {(t1, a) -> pass, (t1, c) -> pass}

Intended Pass = {a}

OPEN: c is not in L but was tested with t1 and passed.  Does Pass(c)
hold?  The N8 row requires inL membership for the universal quantifier
but does not explicitly forbid Pass for elements outside L.  Is
L-membership necessary for Pass, or is test survival alone sufficient?
The fragment has no critical package to adjudicate severity of the test
run on c, so the classification of c is genuinely undecided.

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | b2f57a55e0bdf0c8 |
| N1 | near-miss | P1 | 8d4a5a01abd851c1 |
| P2 | positive | N2 | 9688c22c45d39269 |
| N2 | near-miss | P2 | ee399eff14b4b104 |
| P3 | positive | N3 | e1124b77e78814bc |
| N3 | near-miss | P3 | e0ab20c95a77907c |
| P4 | positive | N4 | c6cac8d6597e35b6 |
| N4 | near-miss | P4 | 0d4e23da0d966639 |
| B1 | boundary | - | 25632b2c13b027d6 |
