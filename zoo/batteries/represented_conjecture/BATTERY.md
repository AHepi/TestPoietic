### P1 - Gene variant with symbol as hypothesis but no criticism (positive: biological variation, not a represented conjecture)

Sorts: Gene, Variant, Agent, Symbol
Elements: g1, v1, a1, s1
Relations: has_variant(g1, v1), has_symbol(a1, s1), refers_to(s1, v1),
  used_as_hypothesis(s1)
Note: s1 is NOT subject_to_criticism. The variant v1 is a biological
variation. Agent a1 has a symbol s1 referring to v1 and used as a
hypothesis, but s1 is not subject to criticism. This is NOT a
represented conjecture.

### N1 - Same gene variant with symbol as hypothesis subject to criticism (near-miss: IS a represented conjecture)

Sorts: Gene, Variant, Agent, Symbol
Elements: g1, v1, a1, s1
Relations: has_variant(g1, v1), has_symbol(a1, s1), refers_to(s1, v1),
  used_as_hypothesis(s1), subject_to_criticism(s1)
Difference from P1: adds subject_to_criticism(s1). Now s1 is an explicit
symbol used as a hypothesis subject to criticism. This IS a represented
conjecture, so it does NOT satisfy "not RepresentedConjecture."

### P2 - Population allele with symbol referring to it but not used as hypothesis (positive: biological variation, not a represented conjecture)

Sorts: Population, Locus, Allele, Agent, Symbol
Elements: pop1, loc1, al_A, al_G, a1, s1
Relations: in_pop(al_A, pop1), in_pop(al_G, pop1), at_locus(al_A, loc1),
  at_locus(al_G, loc1), has_symbol(a1, s1), refers_to(s1, al_G),
  subject_to_criticism(s1)
Note: s1 is NOT used_as_hypothesis. The allele al_G is a biological
variation. Agent a1 has a symbol s1 referring to al_G and subject to
criticism, but s1 is not used as a hypothesis. This is NOT a
represented conjecture.

### N2 - Same allele with symbol used as hypothesis and subject to criticism (near-miss: IS a represented conjecture)

Sorts: Population, Locus, Allele, Agent, Symbol
Elements: pop1, loc1, al_A, al_G, a1, s1
Relations: in_pop(al_A, pop1), in_pop(al_G, pop1), at_locus(al_A, loc1),
  at_locus(al_G, loc1), has_symbol(a1, s1), refers_to(s1, al_G),
  used_as_hypothesis(s1), subject_to_criticism(s1)
Difference from P2: adds used_as_hypothesis(s1). Now s1 is an explicit
symbol referring to al_G, used as a hypothesis, subject to criticism.
This IS a represented conjecture.

### P3 - Somatic mutation with symbol used as hypothesis and criticized but not referring to mutation (positive: biological variation, not a represented conjecture)

Sorts: Tissue, Sample, Mutation, Agent, Symbol
Elements: tis_tumor, sam1, mut1, a1, s1
Relations: from_tissue(sam1, tis_tumor), has_mutation(sam1, mut1),
  has_symbol(a1, s1), used_as_hypothesis(s1), subject_to_criticism(s1)
Note: s1 does NOT refer_to(mut1). The mutation mut1 is a biological
variation. Agent a1 has a symbol s1 used as a hypothesis and subject to
criticism, but s1 does not refer to mut1. This is NOT a represented
conjecture about mut1.

### N3 - Same somatic mutation with symbol referring to it as hypothesis (near-miss: IS a represented conjecture)

Sorts: Tissue, Sample, Mutation, Agent, Symbol
Elements: tis_tumor, sam1, mut1, a1, s1
Relations: from_tissue(sam1, tis_tumor), has_mutation(sam1, mut1),
  has_symbol(a1, s1), refers_to(s1, mut1), used_as_hypothesis(s1),
  subject_to_criticism(s1)
Difference from P3: adds refers_to(s1, mut1). Now s1 is an explicit
symbol referring to mut1, used as a hypothesis, subject to criticism.
This IS a represented conjecture.

### P4 - Genuine represented conjecture: symbol refers to variant, used as hypothesis, subject to criticism (positive: too-strong wall -- wrongly excluded by too-strong reading)

Sorts: Gene, Variant, Agent, Symbol, Criticism
Elements: g1, v1, a1, s1, c1
Relations: has_variant(g1, v1), has_symbol(a1, s1), refers_to(s1, v1),
  used_as_hypothesis(s1), subject_to_criticism(s1), criticizes(c1, s1)
Agent a1 has explicit symbol s1 referring to variant v1, used as a
hypothesis, subject to criticism c1. This IS a genuine represented
conjecture. The too-strong reading of RepresentedConjecture (nothing
can ever count) wrongly excludes this.

### N4 - Mere typed-structural analogy: symbol shares type with variant but no reference, no hypothesis, no criticism (near-miss: too-weak wall -- wrongly admitted by too-weak reading)

Sorts: Gene, Variant, Agent, Symbol, Type
Elements: g1, v1, a1, s1, t1
Relations: has_variant(g1, v1), has_symbol(a1, s1), type_of(s1, t1),
  type_of(v1, t1)
Symbol s1 and variant v1 share type t1 (structural analogy), but s1
does not refer to v1, is not used as a hypothesis, and is not subject
to criticism. The too-weak reading admits this as a represented
conjecture because of the typed-structural analogy, but it should be
excluded. This is NOT a represented conjecture.

### B1 - Symbol refers to variant and is used as a label but not explicitly as a hypothesis (boundary: OPEN -- does labeling count as hypothesis use?)

Sorts: Gene, Variant, Agent, Symbol, Label
Elements: g1, v1, a1, s1, lab1
Relations: has_variant(g1, v1), has_symbol(a1, s1), refers_to(s1, v1),
  is_label(s1, lab1)
Symbol s1 refers to variant v1 and is used as label lab1. It is unclear
whether mere labeling without explicit hypothesis or criticism
structure counts as use as a hypothesis subject to criticism.
OPEN: Does a symbol that refers to a biological variation and is used
as a label, but not explicitly as a hypothesis subject to criticism,
count as a represented conjecture?

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | ae6e401d16068506 |
| N1 | near-miss | P1 | cbcb45c125a25e6d |
| P2 | positive | N2 | e67efb81c642fb25 |
| N2 | near-miss | P2 | 0afdefe493e27974 |
| P3 | positive | N3 | 4503bb345ca60237 |
| N3 | near-miss | P3 | 696f0590b6842d5c |
| P4 | positive | N4 | eb9ef81c391942fb |
| N4 | near-miss | P4 | ff6b520b8f68a30b |
| B1 | boundary | - | 1a84d8e71422439e |
