# Semantic Pinning Record — N18 Joint Pair v1

record_id: PIN-SUB-v1
version: 1.0
date: 2026-08-21
status: REVIEWED_PENDING_OWNER_SEAL
official_file: PIN_SUB_V1.md
plain_language_file: PIN_SUB_V1_PLAIN_LANGUAGE.md
digest_manifest: PIN_SUB_V1_FREEZE.json
sha256_official: PIN_SUB_V1_FREEZE.json#official_sha256
sha256_plain_language: PIN_SUB_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md (frozen calculus); ORIGINAL_TERMS_INVENTORY.md (pinned catalog); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, pinned per ERR-SPA-v1 to a9f62ebb...); SPA_PIN_ERRATUM_V1.md (ERR-SPA-v1); DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); PIN_CONS_V1.md; PIN_VE_V1.md; RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: joint original-side pins for SameSyntax and RealizationEq (DSF-v1 family D19), the two conjuncts of the SameLabelSwap abbreviation at calculus (63), feeding N-row N18 (NE_SUBSTRATE_SWAP_NOT_AUTOMATIC) and the K_REALIZATION_EQUIVALENCE certificate row with its pi_{R_eq} report
claims: freezes two named, classified candidate meanings (PIN-SUB-D1, PIN-SUB-D2) pinned JOINTLY with an explicit two-sided independence requirement; records one named OPEN item
non_claims: does not test, discharge, repair, or change N-row N18 (DSF-v1 marks N18 DO NOT TEST OR REPAIR; this record pins vocabulary only); does not move any readiness count; does not edit the frozen calculus, SPA-v1, or any sealed record; does not decide the K_REALIZATION_EQUIVALENCE existential; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4.
This record uses the definition bucket plus one acceptance axiom. Check
structures are record artifacts, not semantic additions.

## 1. Scope, method, and why this pair is joint

DSF-v1 Section 8 marks N18 "OPEN: DO NOT TEST OR REPAIR" — the row is a
pure existential with no denial limb, and its two constituent terms are the
conjuncts of one abbreviation joined by a negation. Pinning either
conjunct alone rigs the row: a loose SameSyntax manufactures the
existential for free; a loose RealizationEq destroys it, since the
abbreviation requires its negation. The catalog and PIN-CONS-v1's manifest
therefore deferred SameSyntax/RealizationEq to one joint record. This is
that record. Pinning vocabulary is not testing or repairing N18; testing
remains PROHIBITED.

Method rule (as in PIN-CONS-v1): weakest meanings that make the frozen
occurrences well-typed, PLUS the joint independence requirement of
Section 5, which this pair needs and single-term records did not.

## 2. Exact anchors

Calculus (63), the N-only abbreviation (transcribed from math form):

> SameLabelSwap_{eta,theta}(b',k') iff
> SameSyntax(b,k;b',k') and not RealizationEq_eta((b,k),(b',k');T,E)

Table 1.1, R block, K_REALIZATION_EQUIVALENCE (transcribed):

> exists b',k' RealizationEq_eta((b,k),(b',k');T,E)

Applicability vocabulary (calculus, transcribed):

> R_EQ_APP iff DeclaredMultipleRealizationClaim_eta(b,k,T)
> R_EQ_NA  iff MultipleRealizationScopeOmitted_eta

Report projection (62a), pi_{R_eq} (structure of the cases): MAY_PASS when
R_EQ_APP is declared and R-full-hat is in the closure; NOT_ESTABLISHED
when R_EQ_APP without the closure; NOT_APPLICABLE otherwise. The R-full
rule (transcribed): R_APP and R_EQ_APP and the big conjunction R_full
imply R-full-hat, graded D.

N18 row NE_SUBSTRATE_SWAP_NOT_AUTOMATIC (transcribed):

> M models exists b',k' SameLabelSwap_{eta,theta}(b',k')

The row is a pure existential: it asserts only that a same-label,
non-realization-equivalent swap pair EXISTS. Control surface: (62b)
abbreviates SameLabelDifferentTask as the same existential and the control
NC_UNCONSTRAINED_SUBSTRATE_SWAP consumes it; that control's six-coordinate
vector is recorded in the ledger and is unchanged by this record.

DSF-v1 anchors: Section 6 family D19 — "SameLabelSwap (63), SameSyntax,
RealizationEq | Rfull | N18 | OPEN"; Section 12 lists SameSyntax
among the uninterpreted N-only leaves, and RealizationEq
among the open load-bearing originals; Section 8 row N18 is OPEN with DO
NOT TEST OR REPAIR. The stress-test campaign's target-essentiality finding
("target variation changes only idle metadata while the operative program
and award stay fixed — DEFINITION ADMITS SPURIOUS ATTRIBUTION") is the
direct motivation for PIN-SUB-D2's role-based reading.

## 3. PIN-SUB-D1: SameSyntax (definition; load-bearing)

Occurrences: (63) only. Options:

- SS-presentation (SELECTED): SameSyntax(b,k;b',k') holds iff the declared
  syntactic presentations of the pairs (b,k) and (b',k') are equal — the
  same label/code presentation token — with NO condition on task, role,
  environment, or content. This is a display-level equality: it is exactly
  the kind of equality that label-equality-is-never-identity governs.
- SS-task-invariant (REJECTED): same syntax AND same task. Rejected: it
  imports a task condition into a conjunct that the abbreviation pairs
  AGAINST realization equivalence, which is itself task-relative;
  folding the task into SameSyntax would make the two conjuncts share a
  parameter and destroy their independence (the joint requirement of
  Section 5).
- SS-physical (REJECTED): same physical substrate. Rejected: no frozen
  occurrence mentions substrate; it would make SameLabelSwap nearly
  impossible and thereby decide N18 negatively by pin choice.

Selection: SS-presentation. Weakest reading; keeps the conjunct
independent of RealizationEq; matches the control name
SameLabelDifferentTask (a label-level phenomenon by name). Load-bearing,
recorded. Steering defense: RATIONALE_BASED_ONLY.

## 4. PIN-SUB-D2: RealizationEq (definition; load-bearing)

Occurrences: (63) negated; K_REALIZATION_EQUIVALENCE existential
(certificate row); the R_EQ_APP/R_EQ_NA applicability vocabulary presumes
a declared multiple-realization claim but does not define the relation.
Options:

- RE-role (SELECTED): RealizationEq_eta((b,k),(b',k');T,E) holds iff the
  two pairs occupy the same causal role with respect to the declared task
  T and environment E — role equality read as equality of the
  counterfactual role profile across the declared nearby variants of the
  bearer in environment E (source-constrained by FOR_EMERGENCE and
  FOR_REPLICATOR_NICHE: realization roles are contextual and
  counterfactual; a one-off output match is NOT role equality). Crucially,
  role equality is relative to (T,E): a pair syntactically identical but
  occupying different roles — the stress test's target-essentiality seam,
  where variation touches only idle metadata while the operative program
  and award stay fixed — FAILS role equality. That failure mode must
  remain possible, or SameLabelSwap is unsatisfiable.
- RE-output (REJECTED): same input-output behavior on the observed run.
  Rejected: it makes RealizationEq nearly free whenever SameSyntax holds
  (same code, same run), so ¬RealizationEq would almost never hold and
  the N18 existential would be destroyed by pin choice.
- RE-substrate-independent (REJECTED): any pair sharing syntax counts as
  realization-equivalent regardless of task/environment. Rejected: it
  collapses SameLabelSwap to a contradiction (SameSyntax would imply
  RealizationEq), which is the strongest possible rigging of N18.

Selection: RE-role. Steering defense: RATIONALE_BASED_ONLY.

## 5. Joint independence requirement

PIN-SUB-A1 (acceptance axiom): the two pins are jointly constrained to
leave BOTH combinations open. In the pinned vocabulary there must exist:

- M1 (swap exists): pairs (b,k),(b',k') with equal syntactic
  presentations but different (T,E)-role profiles — concretely, a pair
  differing only in idle metadata coordinates while the operative program
  is role-distinguished. Then SameLabelSwap holds, and N18's existential
  is satisfiable.
- M2 (no swap): every equal-presentation pair shares its role profile
  (e.g., a structure whose only same-syntax pair is an exact duplicate).
  Then no SameLabelSwap exists, and N18's existential fails.

M1 and M2 both satisfy PIN-SUB-D1, PIN-SUB-D2, and every prior pin. The
joint pin therefore neither forces nor forbids a SameLabelSwap witness.
Additionally, the K_REALIZATION_EQUIVALENCE certificate existential is
undecided: M2-style structures with no realized pair leave it false, and
adding one declared role-equal pair makes it true, with SameSyntax
unaffected. This is the two-sided condition DSF-v1's DO-NOT-TEST marking
exists to protect: the pin makes the row TESTABLE in principle someday
without deciding it.

## 6. What this record deliberately does NOT pin

OneCopyOnly's leaves (OneObservedToken, CounterfactualFamilyObserved) and
ReplicationRole belong to the N19 record, not here. RoleEq,
SecondSubstance, and CausalExemption (N17) are a separate cluster.
Nothing is pinned about R_full's other conjuncts. Recorded OPEN item:
PIN-SUB-OPEN-1 — whether RE-role's counterfactual role profile needs a
minimum variant family to be well-defined in degenerate structures (a
structure with no declared variants); if a future fixture needs it, that
is a new version.

## 7. Affected dependency cones (no readiness change)

- Semantic family: D19 (leaves pinned jointly; family status NOT
  reclassified).
- Audit heads: Rfull-hat (cone membership); the pi_{R_eq} report reads
  its inputs unchanged.
- Certificate row: K_REALIZATION_EQUIVALENCE (undecided by the pins;
  Section 5).
- N-rows (cones only): N18 directly; N19 shares the counterfactual
  vocabulary but is not touched.
- Control: NC_UNCONSTRAINED_SUBSTRATE_SWAP consumes (62b)'s abbreviation;
  its recorded vector is unchanged.
- Explicitly unchanged: the frozen calculus, SPA-v1, all sealed records,
  all bridges, ADM counts, IC-SP-001/002 (unrun).
- Row readiness unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
  untestable; zero discharged; testing PROHIBITED. N18 remains DO NOT
  TEST OR REPAIR; this record does not test or repair it.

## 8. Forbidden items

No original N-row change, test, or repair; no fixture construction or run;
no total expansion or row bridge; no source bridge claim; no in-place edit
of the calculus, SPA-v1, or any sealed record; no semantic choice
justified by a desired row outcome; no claim about creativity in any real
system.

## 9. Residual status and next checkpoint

Frozen jointly: PIN-SUB-D1 (SameSyntax, presentation reading), PIN-SUB-D2
(RealizationEq, role reading), PIN-SUB-A1 (joint independence). Open:
PIN-SUB-OPEN-1 (degenerate-structure variant family). Next checkpoint per
the catalog order: the N17/N19 leaves and the deferred RetainsOrAdapts
pin, then the T3 epistemic cluster, then DSF-v1 Section 13 item 6 bridge
review.
