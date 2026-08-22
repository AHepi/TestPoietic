### P1 - Definitional predicate extension

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, Q/1
New theory theta': {exists x P(x), forall x(Q(x) <-> P(x))}

Witness model of theta: domain {a,b}, P^M = {a}
Expansion to theta': Q^M = {a}
Conservative: Q is defined as P. Every model of theta expands by setting Q = P.
No old-language formula gains or loses provability.

### N1 - Definitional predicate plus existence of complement

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, Q/1
New theory theta': {exists x P(x), forall x(Q(x) <-> P(x)), exists x not Q(x)}

Single difference from P1: theta' adds axiom exists x not Q(x).

Witness model of theta that cannot expand: domain {a}, P^M = {a}.
Q(a) <-> P(a) = true, so not Q(a) is false; no element satisfies not Q.
theta' proves exists x not P(x) (old language), which theta does not prove. NOT conservative.

### P2 - Function symbol mapping into predicate

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, f/1
New theory theta': {exists x P(x), forall x P(f(x))}

Witness model of theta: domain {a,b}, P^M = {a}
Expansion to theta': f(a) = a, f(b) = a
Conservative: f maps every element to a P-element. Any model of theta
has at least one P-element (by theta), so f can be a constant function to it.
No old-language formula gains or loses provability.

### N2 - Function symbol with anti-fixed-point constraint

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, f/1
New theory theta': {exists x P(x), forall x P(f(x)), forall x(f(x) != x)}

Single difference from P2: theta' adds axiom forall x(f(x) != x).

Witness model of theta that cannot expand: domain {a}, P^M = {a}.
f(a) must satisfy P (only a), so f(a) = a, but f(a) != a is required.
theta' proves exists xexists y(x != y) (old language), which theta does not prove. NOT conservative.

### P3 - Definitional binary predicate over old language

Sorts: U
Old signature eta: P/1, R/2
Old theory theta: {forall x R(x,x)}
New signature eta': P/1, R/2, S/2
New theory theta': {forall x R(x,x), forall xforall y(S(x,y) <-> R(x,y) /\ P(x))}

Witness model of theta: domain {a,b}, R^M = {(a,a),(b,b)}, P^M = {a}
Expansion to theta': S^M = {(a,a),(a,b)}
Conservative: S is defined over old predicates R and P. Every model
of theta expands by computing S from R and P. No old-language formula
gains or loses provability.

### N3 - Definitional binary predicate with surjectivity demand

Sorts: U
Old signature eta: P/1, R/2
Old theory theta: {forall x R(x,x)}
New signature eta': P/1, R/2, S/2
New theory theta': {forall x R(x,x), forall xforall y(S(x,y) <-> R(x,y) /\ P(x)), forall xexists y S(x,y)}

Single difference from P3: theta' adds axiom forall xexists y S(x,y).

From forall x R(x,x) and S(x,x) <-> R(x,x) /\ P(x), the surjectivity demand
forall xexists y S(x,y) forces P(x) for every x (take y = x).
theta' proves forall x P(x) (old language), which theta does not prove. NOT conservative.

### P4 - Fresh predicate defined as negation (too-strong wall)

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, Q/1
New theory theta': {exists x P(x), forall x(Q(x) <-> not P(x))}

Witness model of theta: domain {a,b}, P^M = {a}
Expansion to theta': Q^M = {b}
Conservative: Q is defined as not P. Every model of theta expands by setting
Q to the complement of P. No old-language formula gains provability.
A too-strict reading wrongly excludes this, treating the negation-based
definition as new structure when it is purely definitional.

### N4 - Fresh predicate defined as negation plus existence (too-weak wall)

Sorts: U
Old signature eta: P/1
Old theory theta: {exists x P(x)}
New signature eta': P/1, Q/1
New theory theta': {exists x P(x), forall x(Q(x) <-> not P(x)), exists x Q(x)}

Single difference from P4: theta' adds axiom exists x Q(x).

Witness model of theta that cannot expand: domain {a}, P^M = {a}.
Q(a) <-> not P(a) = false, so no element satisfies Q.
theta' proves exists x not P(x) (old language), which theta does not prove (theta is
satisfiable in a one-element model with P = {a}). NOT conservative.
A too-weak reading wrongly admits this because Q is defined over
the old language, ignoring the extra existence axiom.

### B1 - Skolem function for existential witness

Sorts: U
Old signature eta: R/2
Old theory theta: {forall xexists y R(x,y)}
New signature eta': R/2, f/1
New theory theta': {forall xexists y R(x,y), forall x R(x, f(x))}

Witness model of theta: domain {a,b}, R^M = {(a,b),(b,a)}
Expansion to theta': f(a) = b, f(b) = a

OPEN: Is this extension conservative? In classical first-order logic
with the axiom of choice, every model of theta expands to a model of theta'
by selecting a witness for each x, so the extension is conservative.
Without ambient choice, or in weak meta-theories, the existence of
a uniform selection function may not be guaranteed. The question:
does conservativity of Skolemization depend on meta-theoretic
assumptions (e.g., choice) beyond the object theory theta?

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | c35dbaadd59ff58a |
| N1 | near-miss | P1 | 920640e0bec65938 |
| P2 | positive | N2 | 33f758f47162a5f2 |
| N2 | near-miss | P2 | 3d4671e852965421 |
| P3 | positive | N3 | 7e18b962e5256c03 |
| N3 | near-miss | P3 | bf72d9461e35258d |
| P4 | positive | N4 | 8791c04b5b2f2206 |
| N4 | near-miss | P4 | 6e87ea89efff257c |
| B1 | boundary | - | 774af70d47ebd9af |
