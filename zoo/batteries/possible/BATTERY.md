# Battery: Possible_Phi

Term: Possible_Phi(T) -- constructor-theoretic physical possibility of task T.
A task T is physically possible when the laws of physics permit a constructor
for T. This is distinct from mere absence of a current PK bearer (too-weak)
and from demonstrated realizability via an actual constructor (too-strong).

Source-grade constraint: CT_FOUNDATION (arXiv:1210.7439 sections 3.1-3.2).

Structural vocabulary:
  Sorts: Task, Laws
  Relations:
    law_permits_constructor : Laws x Task -> Bool
      -- the laws of physics permit a constructor for the task
    constructor_realized : Task -> Bool
      -- a constructor has been actually built/demonstrated for the task
    pk_bearer_exists : Task -> Bool
      -- a current PK bearer exists for the task
    decomposes : Task x Task x Task -> Bool  (B1 only)
      -- the first task decomposes into the second and third

  Possible_Phi(T) should hold iff law_permits_constructor(L, T).

### P1 - Physically possible task with realized constructor, no PK bearer

Sorts: Task = {t1}, Laws = {L1}
Relations:
  law_permits_constructor(L1, t1) = true
  constructor_realized(t1) = true
  pk_bearer_exists(t1) = false

### N1 - Minimal pair: same task but laws forbid a constructor

Sorts: Task = {t1}, Laws = {L1}
Relations:
  law_permits_constructor(L1, t1) = false
  constructor_realized(t1) = true
  pk_bearer_exists(t1) = false

Difference from P1: law_permits_constructor flips true -> false.

### P2 - Physically possible task, no realized constructor, PK bearer present

Sorts: Task = {t2}, Laws = {L2}
Relations:
  law_permits_constructor(L2, t2) = true
  constructor_realized(t2) = false
  pk_bearer_exists(t2) = true

### N2 - Minimal pair: same task but laws forbid a constructor

Sorts: Task = {t2}, Laws = {L2}
Relations:
  law_permits_constructor(L2, t2) = false
  constructor_realized(t2) = false
  pk_bearer_exists(t2) = true

Difference from P2: law_permits_constructor flips true -> false.

### P3 - Physically possible task with realized constructor and PK bearer

Sorts: Task = {t3}, Laws = {L3}
Relations:
  law_permits_constructor(L3, t3) = true
  constructor_realized(t3) = true
  pk_bearer_exists(t3) = true

### N3 - Minimal pair: same task but laws forbid a constructor

Sorts: Task = {t3}, Laws = {L3}
Relations:
  law_permits_constructor(L3, t3) = false
  constructor_realized(t3) = true
  pk_bearer_exists(t3) = true

Difference from P3: law_permits_constructor flips true -> false.

### P4 - Too-strong wall: physically possible, not realized, no PK bearer (PossibleTaskOnly)

Sorts: Task = {t4}, Laws = {L4}
Relations:
  law_permits_constructor(L4, t4) = true
  constructor_realized(t4) = false
  pk_bearer_exists(t4) = false

The too-strong reading (Possible = demonstrated realizability) excludes this
because constructor_realized(t4) = false. Possible_Phi must admit it: the laws
permit a constructor even though none has been built.

### N4 - Too-weak wall: no PK bearer but laws forbid a constructor

Sorts: Task = {t4}, Laws = {L4}
Relations:
  law_permits_constructor(L4, t4) = false
  constructor_realized(t4) = false
  pk_bearer_exists(t4) = false

The too-weak reading (Possible = NOT pk_bearer_exists) admits this because
pk_bearer_exists(t4) = false. Possible_Phi must exclude it: the laws forbid a
constructor, so the task is physically impossible.

Difference from P4: law_permits_constructor flips true -> false.

### B1 - OPEN: compositional possibility of a decomposed task

Sorts: Task = {t6, t7, t8}, Laws = {L6}
Relations:
  law_permits_constructor(L6, t7) = true
  law_permits_constructor(L6, t8) = true
  law_permits_constructor(L6, t6) = undefined
  constructor_realized(t6) = false
  constructor_realized(t7) = false
  constructor_realized(t8) = false
  pk_bearer_exists(t6) = false
  decomposes(t6, t7, t8) = true

OPEN: does Possible_Phi(t6) hold when t6 decomposes into t7 and t8, both
individually physically possible, but the structure contains no axiom
licensing composition of possibility? law_permits_constructor(L6, t6) is
undefined -- it is not derivable from law_permits_constructor(L6, t7) and
law_permits_constructor(L6, t8) without an additional composition principle.
The inventory candidate Possible_Phi(T) does not license this
transitive/compositional reading.

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | f2c44dbe82bbf61d |
| N1 | near-miss | P1 | 8b15b0196e65801a |
| P2 | positive | N2 | b714389e17bd02bf |
| N2 | near-miss | P2 | f23491b2d313bd0d |
| P3 | positive | N3 | ec2f6a4b8a8dddba |
| N3 | near-miss | P3 | 78cabf09363ec0bc |
| P4 | positive | N4 | 49568529a3b89020 |
| N4 | near-miss | P4 | dfdeb9294bc39251 |
| B1 | boundary | - | a5d2a31153e13cbf |
