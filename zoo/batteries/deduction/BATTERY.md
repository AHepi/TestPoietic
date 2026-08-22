### P1 - Bare deduction with explicit derivation link

Sorts:
  Chi = {a_chi, xi_chi, d_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, d_chi) }
  Tag = { (d_chi, Deduction) }

Construction:
  Deduction(d_chi) where d_chi is derived from A-_chi AND Xi_chi
  via a bare derivation link. No critical package, no FDerives form.
  Definable without the critical package.

### N1 - Claimed deduction with no derivation link (minimal pair with P1)

Sorts:
  Chi = {a_chi, xi_chi, d_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = {}
  Tag = { (d_chi, Deduction) }

Construction:
  Deduction(d_chi) is claimed but Derives is empty;
  d_chi has no derivation link to A-_chi AND Xi_chi.

Difference from P1: Derives = {} vs Derives = { (a_chi AND xi_chi, d_chi) }.
All other sorts, relations, and tags are identical.

### P2 - Deduction in N13 disjoint union with non-FDerives derivation

Sorts:
  Chi = {a_chi, xi_chi, d_chi, o_chi, p_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, d_chi) }
  N13 = { Record(o_chi), Deduction(d_chi), Prediction(p_chi) }
  Tag = { (d_chi, Deduction), (o_chi, Record), (p_chi, Prediction) }

Construction:
  Deduction(d_chi) is the Deduction arm of the N13 row
  (Record OR Deduction OR Prediction). Derivation uses BareDerives,
  not the package-internal FDerives form. Definable without the critical package.

### N2 - Same N13 structure but d_chi tagged Prediction (minimal pair with P2)

Sorts:
  Chi = {a_chi, xi_chi, d_chi, o_chi, p_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, d_chi) }
  N13 = { Record(o_chi), Prediction(d_chi), Prediction(p_chi) }
  Tag = { (d_chi, Prediction), (o_chi, Record), (p_chi, Prediction) }

Construction:
  d_chi has a derivation link from A-_chi AND Xi_chi but is tagged
  Prediction(d_chi), not Deduction(d_chi), in the N13 row.

Difference from P2: Tag(d_chi) = Prediction (not Deduction); N13 arm is
Prediction(d_chi) (not Deduction(d_chi)). Derives is identical.

### P3 - Deduction supported by transitive derivation chain

Sorts:
  Chi = {a_chi, xi_chi, e_chi, d_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, e_chi), (e_chi, d_chi) }
  Tag = { (d_chi, Deduction) }

Construction:
  Deduction(d_chi) where d_chi is reached by a two-step bare derivation:
  a_chi AND xi_chi -> e_chi -> d_chi. The transitive closure links
  d_chi to A-_chi AND Xi_chi. No critical package, no FDerives form.

### N3 - Same chain but final step missing, d_chi unlinked (minimal pair with P3)

Sorts:
  Chi = {a_chi, xi_chi, e_chi, d_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, e_chi) }
  Tag = { (d_chi, Deduction) }

Construction:
  Deduction(d_chi) is claimed, but the derivation chain stops at e_chi.
  d_chi is not in the range of Derives and is not derivable from A-_chi AND Xi_chi.

Difference from P3: Derives lacks (e_chi, d_chi); the final derivation step
is absent. All sorts and tags are identical.

### P4 - too-strong wall: genuine bare derivation outside critical package

Sorts:
  Chi = {a_chi, xi_chi, d_chi}
  Pkg = {} (explicitly outside any critical package)
  DerivationForm = BareDerives (NOT FDerives)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi AND xi_chi, d_chi) }
  Tag = { (d_chi, Deduction) }

Construction:
  A genuine bare derivation of d_chi from A-_chi AND Xi_chi, presented
  outside any critical package. The derivation form is BareDerives, not
  the package-internal FDerives. The too-strong reading (only package-
  internal FDerives-shaped derivations count) WRONGLY excludes this.
  The correct reading ADMITS it.

### N4 - too-weak wall: claimed conclusion with no derivation link

Sorts:
  Chi = {a_chi, xi_chi, d_chi}
  Pkg = {} (no critical package)
  DerivationForm = none

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = {}
  Tag = { (d_chi, Deduction) }

Construction:
  d_chi is tagged Deduction(d_chi) but Derives is empty. There is no
  derivation link from A-_chi AND Xi_chi to d_chi. The too-weak reading
  (any claimed conclusion counts as a deduction) WRONGLY admits this.
  The correct reading EXCLUDES it.

Difference from P4: Derives = {} vs Derives = { (a_chi AND xi_chi, d_chi) }.
P4 has a genuine derivation link; N4 has none. All other structure is identical.

### B1 - OPEN: derivation from a proper subset of A-_chi AND Xi_chi

Sorts:
  Chi = {a_chi, xi_chi, d_chi}
  Pkg = {} (no critical package)

Relations (extensional):
  A_chi = {a_chi}
  Xi_chi = {xi_chi}
  Derives = { (a_chi, d_chi) }
  Tag = { (d_chi, Deduction) }

Construction:
  Deduction(d_chi) where d_chi is derived from A-_chi alone, not from
  the full conjunction A-_chi AND Xi_chi. The derivation link exists but
  uses only a proper subset of the theory content.

OPEN question: Does a derivation from a proper subset of A-_chi AND
Xi_chi count as a genuine Deduction? The too-weak wall excludes only
the total absence of a derivation link. The too-strong wall requires
only that the derivation not be package-internal FDerives. Neither wall
settles whether a partial-content derivation suffices.

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | a5b6717dee7d6df4 |
| N1 | near-miss | P1 | ecb77bb0baa3b41d |
| P2 | positive | N2 | 7edc06d86f462a40 |
| N2 | near-miss | P2 | 2270e626ded112c0 |
| P3 | positive | N3 | a03fade6a48923ec |
| N3 | near-miss | P3 | b1b9cff7998ad034 |
| P4 | positive | N4 | 419ac8f7bbe9240d |
| N4 | near-miss | P4 | 3916a3a71f23026b |
| B1 | boundary | - | 250a4faef26c37e9 |
