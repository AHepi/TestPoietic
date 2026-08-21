# Semantic Pinning Record — VE-Identity Cluster v1

record_id: PIN-VE-v1
version: 1.0
date: 2026-08-21
status: REVIEWED_PENDING_OWNER_SEAL
official_file: PIN_VE_V1.md
plain_language_file: PIN_VE_V1_PLAIN_LANGUAGE.md
digest_manifest: PIN_VE_V1_FREEZE.json
sha256_official: PIN_VE_V1_FREEZE.json#official_sha256
sha256_plain_language: PIN_VE_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md (frozen calculus); ORIGINAL_TERMS_INVENTORY.md (pinned catalog); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, pinned per ERR-SPA-v1 to a9f62ebb...); SPA_PIN_ERRATUM_V1.md (ERR-SPA-v1); DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); PIN_CONS_V1.md (PIN-CONS-v1, cluster precedent); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: original-side candidate pins for RepresentedConjecture and TheoryMediatedCriticism (DSF-v1 family D16; DSF-v1 Section 12 load-bearing leaves), feeding N-row N15 (NE_VARIATION_NOT_CONJECTURE_IDENTITY) and touching the V_FALLIBILITY certificate row
claims: freezes two named, classified candidate meanings (PIN-VE-D1, PIN-VE-D2) with options stated and one non-deciding two-structure argument for the N15 denial limbs; records one named OPEN item
non_claims: does not test, discharge, or change any original N-row; does not move any readiness count; does not edit the frozen calculus, SPA-v1, or any sealed record; does not strengthen the B-grade bridge (36) into an identity; does not identify any original predicate with an F-prefixed fragment predicate; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4.
This record uses only the definition bucket. Check structures are record
artifacts, not semantic additions.

## 1. Scope and method

Per DSF-v1 Section 13 item 5 and the pinned catalog's recommended order,
this is the smallest unblocked cluster (T4): the VE-identity pair
RepresentedConjecture and TheoryMediatedCriticism, feeding N15 and family
D16 (OPEN in DSF-v1 Section 6). The catalog ranks TheoryMediatedCriticism
steering-sensitive because it occurs NEGATED inside the frozen
V_FALLIBILITY certificate row (Table 1.1, V block) as well as negated in
N15; a careless pin can make V_FALLIBILITY vacuously easy or impossible.

Method rule (as in PIN-CONS-v1): each pin is the weakest meaning that
(i) makes the frozen occurrences well-typed and (ii) does not collapse
the analogue/identity distinction the calculus states in prose under (36):
"This is an analogue of typed transition structure only. It does not
identify a biological variation with a represented conjecture or survival
selection with criticism."

## 2. Exact anchors

Calculus (36), the typed bridge rule, graded B (transcribed from display
form into inline form):

> FallSel_eta(lambda_theta), Epi_{eta,theta}, PAT_{VE,theta} ⊢
> TypedVEEAnalogue_{eta,theta}   [B]   (36)

with the prose immediately following: "This is an analogue of typed
transition structure only. It does not identify a biological variation
with a represented conjecture or survival selection with criticism."

Calculus (35a), the pattern condition PAT_{VE,theta} (structure of the
quotation): role assignments r_e on the episode side
(s_TT -> G, s_chi -> X, s_EE -> L, s_P2 -> R) and r_lambda on the lineage
side (nu -> G, kappa -> X, delta -> L, LaterReinstantiation -> R), with
both chains' step relations; (35) declares the role order
V = (G < X < L < R). Graded B.

Calculus (27a): FallSel_eta(lambda) iff Sel_eta(lambda) and
NoGuarantee(nu,kappa,delta), graded D, with the prose "NoGuarantee is
required only for the fallibility bridge, not for selection itself."

Table 1.1, V block, V_FALLIBILITY row (transcribed from math form):

> NoGuarantee(nu,kappa,delta) and ErrorEliminationByEnvironment_eta(lambda)
> and not TheoryMediatedCriticism_eta(lambda)

N15 row NE_VARIATION_NOT_CONJECTURE_IDENTITY (transcribed from math form):

> M models TypedVEEAnalogue_{eta,theta} and not
> RepresentedConjecture_eta(lambda) and not
> TheoryMediatedCriticism_eta(lambda)

DSF-v1 anchors: Section 6 family D16 — "TypedVEEAnalogue (36),
RepresentedConjecture, TheoryMediatedCriticism | VE | N15 | OPEN";
Section 12 lists TheoryMediatedCriticism among open load-bearing
originals; DSF-B1 (Section 4.4) records bridge (36) as grade B,
"unclaimed; terminal/unreported; head absent from antecedent". Source
register: DEUTSCH constrains the typed-not-identical mapping between
human conjecture/criticism and biological variation/selection; CTL
constrains selection-versus-replication scope. Neither source supplies a
definition of representation or theory-mediation; both pins here are
therefore project candidate meanings, not source imports.

## 3. PIN-VE-D1: RepresentedConjecture (definition; load-bearing)

Occurrences: N15 denial limb only. Options:

- RC-representation (SELECTED): RepresentedConjecture_eta(lambda) holds
  iff the lineage lambda carries, in its own declared records, a
  represented problem token and a represented answer token standing in a
  declared derivation relation — i.e. there exist recordable content
  tokens p (a problem) and c (a candidate answer) in lambda's carrier
  with a declared derives-link from p to c. Content-free pattern
  satisfaction does not count: the role pattern PAT_{VE,theta} assigns
  roles G/X/L/R to lineage events, and no role assignment is a
  representation of anything.
- RC-behavioral (REJECTED): differential continuation success counts as
  conjecture. Rejected: it would make FallSel imply the denial limb's
  negation, collapsing N15 by construction (the analogue's own premises
  would entail RepresentedConjecture).
- RC-source-literal (REJECTED): require a Deutsch-grade conjecture with
  full epistemic packaging. Rejected as over-strong: no frozen occurrence
  requires it, and over-strong pins make the denial limb
  ¬RepresentedConjecture true almost everywhere — the N15 row's witness
  shape would then be available for free, manufactured rather than
  tested.

Selection: RC-representation, the weakest reading that requires actual
declared content tokens while staying independent of the analogue's
premises. Load-bearing, recorded. Steering defense:
RATIONALE_BASED_ONLY.

## 4. PIN-VE-D2: TheoryMediatedCriticism (definition; load-bearing)

Occurrences: N15 denial limb, and negated inside the frozen V_FALLIBILITY
certificate row. Options:

- TMC-account-mediated (SELECTED): TheoryMediatedCriticism_eta(lambda)
  holds iff some elimination of a variant within lambda is mediated by a
  declared account: there exists a criticism event in lambda whose
  discriminator is derived (via the declared Derives relation) from a
  declared target account. Environmental elimination without any
  account-derived discriminator — ErrorEliminationByEnvironment_eta alone
  — does not count.
- TMC-any-selection (REJECTED): any selection pressure counts as
  theory-mediated criticism. Rejected: it would equate
  ErrorEliminationByEnvironment with TMC, making V_FALLIBILITY's conjunct
  ¬TMC contradict its own ErrorEliminationByEnvironment conjunct —
  V_FALLIBILITY would become unsatisfiable, corrupting a frozen
  certificate row.
- TMC-full-package (REJECTED): require a complete CritPkg on the lineage
  side. Rejected as over-strong for the same manufacture hazard as
  RC-source-literal: ¬TMC would hold almost everywhere, including in
  every purely environmental lineage, making V_FALLIBILITY's ¬TMC
  conjunct trivially satisfiable and the certificate row untestable in
  the opposite direction.

Selection: TMC-account-mediated. It keeps V_FALLIBILITY coherent
(purely environmental elimination satisfies ¬TMC while an
account-derived discriminator satisfies TMC — both remain possible), and
it keeps the N15 denial limbs independent of the (36) premises, none of
which mentions a discriminator derived from an account. Load-bearing,
recorded. Steering defense: RATIONALE_BASED_ONLY.

## 5. Non-deciding argument for the N15 limbs

The analogue is derivable from (36) whenever FallSel, Epi, and PAT_VE
hold. Under D1 and D2, neither denial limb is among those premises nor
implied by them: role patterns are not content tokens, and environmental
elimination is not account-mediated criticism. Concretely:

- S1 (analogue without representation or theory-mediation): a structure
  with a FallSel lineage (two variants, differential continuation,
  NoGuarantee), a typed episode, and the PAT_VE role assignments, but
  whose lineage records carry NO problem/answer content tokens and NO
  account-derived discriminator. (36) fires, so TypedVEEAnalogue holds;
  RepresentedConjecture fails (no content tokens); TheoryMediatedCriticism
  fails (elimination is purely environmental). All three N15 conjuncts
  hold.
- S2 (analogue with both present): identical plus one declared content
  pair (p,c) with a derives-link and one criticism event whose
  discriminator is account-derived. Both denial limbs now fail.

S1 and S2 agree on every premise of (36) and on every pin of this record
as constraints; they differ only in the declared content/criticism data
that D1 and D2 make visible. Therefore the pins decide neither N15 limb.
This is exactly the non-collapse the prose under (36) demands, now
checked against typed pins rather than asserted. Note the honest scope:
S1's availability shows the N15 antecedent-and-denial shape is
CONSISTENT with the pins; it is not a countermodel certificate (no total
expansion, no row bridge; D0/DSF-A1 remain OPEN with zero accepted
expansions).

## 6. What this record deliberately does NOT pin

The episode-side criticism machinery (CritPkg, Derives, Predeclared) is
already frozen calculus vocabulary (Table 1.1 C block and (28)-(29)) and
is not repinned here. TypedVEEAnalogue itself is a derived bridge output
of (36); no new decision is made about it. The DSF-B1 bridge keeps its
grade B, unclaimed. The catalogue's N15-adjacent question — whether
FallSel's NoGuarantee limb should interact with V_FALLIBILITY's
certificate use — is recorded as PIN-VE-OPEN-1: a review of whether the
frozen V_FALLIBILITY row's ¬TMC conjunct remains satisfiable across the
intended control population once any future TMC tightening occurs. Any
such tightening is a new version, never an edit.

## 7. Affected dependency cones (no readiness change)

- Semantic family: D16 (leaves now pinned original-side; family status
  NOT reclassified — D16 was OPEN and stays open pending identity/bridge
  work).
- Audit head: VE-hat (unreported head; cone membership only).
- N-rows (cones only): N15 directly; no other row names either term.
- Certificate row: V_FALLIBILITY (Table 1.1, V block) — the D2 pin was
  chosen to keep it coherent; see Section 4's rejection rationale.
- Explicitly unchanged: the frozen calculus, SPA-v1, all sealed records,
  all bridges, DSF-F3, ADM counts, IC-SP-001/002 (unrun).
- Row readiness unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
  untestable; zero discharged; testing PROHIBITED.

## 8. Forbidden items

No original N-row change; no fixture construction or run; no total
expansion or row bridge; no source bridge claim; no in-place edit of the
calculus, SPA-v1, or any sealed record; no analogue-to-identity
strengthening; no semantic choice justified by a desired row outcome; no
claim about creativity in any real system.

## 9. Residual status and next checkpoint

Frozen as candidate definitions over newly declared free primitives — the
primitives themselves remain unpinned per DSF-v1 Section 1: PIN-VE-D1
(RepresentedConjecture, representation reading),
PIN-VE-D2 (TheoryMediatedCriticism, account-mediated reading). Open:
PIN-VE-OPEN-1 (V_FALLIBILITY satisfiability review under any future TMC
tightening). Next checkpoint per the catalog order: the remaining T5
records — the N18 pair (SameSyntax/RealizationEq) pinned jointly, the
N17/N19 leaves, and RetainsOrAdapts with its FOR_REPLICATOR_NICHE
source-grade constraint — then DSF-v1 Section 13 item 6 bridge review.
