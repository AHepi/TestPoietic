### P1 - Predeclaration of d_chi from D_chi before episode

sorts: Chi={d,a,b}, Ep={e}, Cmt={c}
D_chi = {d,a,b}
member: {(d,D_chi),(a,D_chi),(b,D_chi)}
predeclared: {(c,d,D_chi)}
before: {(c,e)}
tagged: {(c,Prediction)}

### N1 - d_chi outside D_chi (minimal pair with P1)

sorts: Chi={d,a,b}, Ep={e}, Cmt={c}
D_chi = {a,b}
member: {(a,D_chi),(b,D_chi)}
predeclared: {(c,d,D_chi)}
before: {(c,e)}
tagged: {(c,Prediction)}
DIFFERENCE: d_chi not in D_chi (committed value outside declared alternative space)

### P2 - Predeclaration with explicit alternative space before episode

sorts: Chi={d,a,b,x}, Ep={e}, Cmt={c2}
D_chi = {d,a,b,x}
member: {(d,D_chi),(a,D_chi),(b,D_chi),(x,D_chi)}
predeclared: {(c2,d,D_chi)}
before: {(c2,e)}
tagged: {(c2,Prediction)}

### N2 - Predeclaration after episode (minimal pair with P2)

sorts: Chi={d,a,b,x}, Ep={e}, Cmt={c2}
D_chi = {d,a,b,x}
member: {(d,D_chi),(a,D_chi),(b,D_chi),(x,D_chi)}
predeclared: {(c2,d,D_chi)}
before: {(e,c2)}
tagged: {(c2,Prediction)}
DIFFERENCE: commitment after episode (postdiction, not prediction)

### P3 - Bare predeclaration outside critical package

sorts: Chi={d,a}, Ep={e}, Cmt={c3}
D_chi = {d,a}
member: {(d,D_chi),(a,D_chi)}
predeclared: {(c3,d,D_chi)}
before: {(c3,e)}
tagged: {(c3,Prediction)}
package: none

### N3 - Possibility statement not commitment (minimal pair with P3)

sorts: Chi={d,a}, Ep={e}, Stmt={s3}
D_chi = {d,a}
member: {(d,D_chi),(a,D_chi)}
possible: {(s3,d,D_chi)}
before: {(s3,e)}
tagged: {(s3,Prediction)}
package: none
DIFFERENCE: possible (no commitment) instead of predeclared

### P4 - [too-strong wall] Genuine bare predeclaration outside critical package

sorts: Chi={d,a,b}, Ep={e}, Cmt={c4}
D_chi = {d,a,b}
member: {(d,D_chi),(a,D_chi),(b,D_chi)}
predeclared: {(c4,d,D_chi)}
before: {(c4,e)}
tagged: {(c4,Prediction)}
package: none
WALL: too-strong -- a pin admitting only package-internal Predeclared_eta tuples wrongly excludes this

### N4 - [too-weak wall] Statement tagged Prediction with no predeclared commitment

sorts: Chi={d,a,b}, Ep={e}, Stmt={s4}
D_chi = {d,a,b}
member: {(d,D_chi),(a,D_chi),(b,D_chi)}
before: {(s4,e)}
tagged: {(s4,Prediction)}
predeclared: {}
WALL: too-weak -- a pin admitting any future-tagged statement wrongly admits this
DIFFERENCE from P4: no predeclared relation (mere future claim, no commitment to d_chi relative to D_chi)

### B1 - Chained predeclaration: does transitivity through a prior predeclaration count?

sorts: Chi={d,a,b}, Ep={e}, Cmt={c1,c2}
D_chi = {d,a,b}
member: {(d,D_chi),(a,D_chi),(b,D_chi)}
predeclared: {(c1,d,D_chi),(c2,d,D_chi)}
before: {(c1,e)}
after: {(c2,e)}
derived_from: {(c2,c1)}
tagged: {(c2,Prediction)}
OPEN: c2 predeclares d_chi from D_chi but is after episode e; c1 predeclares d_chi from D_chi before e and c2 derives from c1. Does the chain c1 to c2 license c2 as Prediction(d_chi) via the prior predeclaration? The inventory candidate does not license a transitive reading of predeclared.

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | 090536e75a7123dd |
| N1 | near-miss | P1 | f87dbef06c023322 |
| P2 | positive | N2 | a2b72fe8a1054a2a |
| N2 | near-miss | P2 | 8ac1a7b70c6796c7 |
| P3 | positive | N3 | 3cb254715a861cee |
| N3 | near-miss | P3 | fa3300c092532a49 |
| P4 | positive | N4 | 3501cfe624e96ac9 |
| N4 | near-miss | P4 | c19abc784457629b |
| B1 | boundary | - | 88b3b94ed2032147 |
