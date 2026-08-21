# Semantic Pinning Record — Epistemic Cluster v1 (T3)

record_id: PIN-EPIST-v1
version: 1.0
date: 2026-08-21
status: REVIEWED_PENDING_OWNER_SEAL
official_file: PIN_EPIST_V1.md
plain_language_file: PIN_EPIST_V1_PLAIN_LANGUAGE.md
digest_manifest: PIN_EPIST_V1_FREEZE.json
sha256_official: PIN_EPIST_V1_FREEZE.json#official_sha256
sha256_plain_language: PIN_EPIST_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md (frozen calculus); ORIGINAL_TERMS_INVENTORY.md (pinned catalog); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, pinned per ERR-SPA-v1 to a9f62ebb...); SPA_PIN_ERRATUM_V1.md (ERR-SPA-v1); DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); PIN_CONS_V1.md; PIN_VE_V1.md; PIN_SUB_V1.md; PIN_ROLE_V1.md; RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: original-side candidate pins for the epistemic cluster (DSF-v1 Section 12 leaves): Pass, Possible, Artifact, Record, Deduction, Prediction, Confirmed, CreativeGenerator, NoPossibleCritic, FinalOutput — feeding rows N8, N9, N10, N12, N13, N14, N16 and families D8, D13, D14, D15, D17
claims: freezes ten named, classified candidate meanings (PIN-EPIST-D1..D10) plus one acceptance axiom (PIN-EPIST-A1, the Confirmed negative guard-rail); records two named OPEN items; per-row two-sided independence checks
non_claims: does not test, discharge, or change any original N-row; does not move any readiness count; does not edit the frozen calculus, SPA-v1, or any sealed record; does not identify Artifact with the frozen ArtifactClassified_eta; does not identify any original predicate with an F-prefixed fragment predicate; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4.
This record uses the definition bucket plus one acceptance axiom. Check
structures are record artifacts, not semantic additions.

## 1. Scope and method

Per DSF-v1 Section 13 item 5 and the pinned catalog, this is the T3
epistemic cluster: ten leaves feeding six rows. The catalog's steering
warnings for this cluster: Confirmed (the register's
survival-is-not-confirmation limit), CreativeGenerator (anchorless
outside its row), and NoPossibleCritic (modal scope decides
satisfiability). Method rule unchanged: weakest meaning making the frozen
occurrences well-typed, with each row's antecedent-and-denial shape kept
satisfiable and its failure kept satisfiable.

## 2. Exact anchors

N-rows (transcribed from math form):

> N8 NE_FINITE_ENUMERATION_NOT_ALL_THEORIES: M models
> FiniteTheorySuite_{eta,theta}(L) and for all u in L Pass(u) and
> exists u* in Theory_eta minus L with not Pass(u*)

> N9 NE_P1_TT_EE_P2_NOT_GENERATOR: M models Epi_{eta,theta} and not
> CreativeCap_eta(A,t) and not CreativeGenerator_eta(A)

> N10 NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE: M models Possible_Phi(T) and
> not exists b,k PK^cur_eta(b,k;X_I,T)

> N12 NE_ARTIFACT_NOT_RECIPE: M models Artifact(p_code) and not
> RecipeKnow_eta(p_code,T) and not Exp_{eta,theta}

> N13 NE_BARE_RECORD_NOT_EVIDENCE: M models (Record(o_chi) or
> Deduction(d_chi) or Prediction(d_chi)) and not CritPkg_eta(chi)

> N14 NE_EVIDENCE_NOT_CONFIRMATION: M models CritPkg_eta(chi) and
> C_SURV and not Confirmed(A^-_chi)

> N16 NE_NONREFUTABLE_NOT_CREATIVE: M models (NoPossibleCritic_eta(A) or
> FinalOutput_eta(A)) and not PhysExpEpisode_{eta,theta}

Calculus (30), graded N (transcribed): CritPkg_eta(chi) and C_SURV does
NOT imply Confirmed(A^-_chi).

Calculus (62b) control abbreviations using cluster leaves (transcribed):
BareScore iff Record(o_chi) and not CritPkg_eta(chi);
CompleteAgreeingPackage iff CritPkg_eta(chi) and C_SURV and not
Confirmed(A^-_chi); FinalUncriticisableOutput iff FinalOutput_eta(A) and
NoPossibleCritic_eta(A) and not CritPkg_eta(chi); PossibleTaskOnly iff
Possible_Phi(T) and no PK bearer; UninstantiatedRecipe iff
AbstractRecipe(p_code) and no Inst witness.

Table 1.1 anchors: FiniteTheorySuite fixes finiteness (DSF-v1 Section 12;
pinned as a disclosed reading already in PIN-CONS-v1 D5's sibling
FiniteVariantSuite — note FiniteTheorySuite is family D13, distinct);
A_ARTIFACT_ROLE uses the frozen predicate ArtifactClassified_eta(p_code)
— NOT the bare Artifact of N12. DSF-v1 families: D8 CreativeGenerator
(N9), D13 FiniteTheorySuite/Pass (N8), D14 Possible (N10), D15
Artifact/Record/Deduction/Prediction (N12,N13), D17
NoPossibleCritic/FinalOutput (N16).

## 3. The Artifact ambiguity, named and not resolved

The catalog flagged it: whether ArtifactClassified_η (Table 1.1, frozen)
and Artifact (N12, leaf) coincide is ambiguous in the text. This record
does NOT identify them. PIN-EPIST-D3 pins the bare leaf only, and the
relationship is recorded as PIN-EPIST-OPEN-2: any future identification
is a bridge with a grade/adequacy/circularity review, never an edit.

## 4. The pins (all definition bucket unless stated)

- PIN-EPIST-D1 — Pass(u): theory u is marked as passing the declared
  finite suite's declared checks. Declaration-level; no inference from
  passing to truth or to all theories (that is exactly N8's shape).
- PIN-EPIST-D2 — Possible_Phi(T): task T is declared possible under the
  law background Phi in the task register. No bearer and no current
  knowledge is required (N10's point: possibility without a PK bearer).
  Rejected: possible-means-instantiated (would contradict the row).
- PIN-EPIST-D3 — Artifact(p_code): p_code is recorded as a produced
  object in the declared production records. Production status only; no
  recipe role and no explanation role implied (N12's point). NOT
  identified with ArtifactClassified_eta (Section 3).
- PIN-EPIST-D4 — Record(o_chi): o_chi is recorded as an observed result
  record. Bare membership in the observed-record class; no critical
  package chain implied.
- PIN-EPIST-D5 — Deduction(d_chi): d_chi is recorded as a deductive
  consequence in the declared deduction records. Bare membership; no
  package chain implied.
- PIN-EPIST-D6 — Prediction(d_chi): d_chi is recorded as a forecast in
  the declared prediction records. Bare membership; no package chain
  implied.
- PIN-EPIST-D7 — Confirmed(A^-_chi): negative direction pinned as
  acceptance axiom PIN-EPIST-A1 (below), per the register's
  survival-is-not-confirmation limit and calculus (30)'s N-grade
  non-implication. The positive semantics (what WOULD confirm) is left
  OPEN as PIN-EPIST-OPEN-1: no frozen row needs it (the term occurs only
  negated, exactly like EverettianUniversalClaim in PIN-CONS-v1).
- PIN-EPIST-D8 — CreativeGenerator_eta(A): A is declared to hold a
  generator role: a declared disposition to produce open-ended novel
  problems, not merely to resolve one. Independence from CreativeCap is
  by construction and is REQUIRED for N9, which denies both while Epi
  holds: the pin asserts no entailment in either direction between
  CreativeGenerator and CreativeCap (a disposition-role declaration and a
  current-capacity query live on different axes; neither's truth value
  constrains the other's). The catalog's "anchorless" warning is
  honored: no source register entry grounds this term, so the pin is a
  project candidate meaning, labeled as such, weakest available.
- PIN-EPIST-D9 — NoPossibleCritic_eta(A): the declared criticism space
  for A's declared output, under the declared protocol, is empty. This is
  deliberately a DECLARED-SPACE reading, not metaphysical
  uncriticisability: the catalog's modal-scope warning says the strong
  reading would be unverifiable by design, and the row N16 only needs
  the declared-space reading to coexist with no physical episode.
- PIN-EPIST-D10 — FinalOutput_eta(A): a declared terminal output token
  of A exists. Declaration-level.

- PIN-EPIST-A1 (acceptance axiom; the Confirmed negative guard-rail):
  no survived declared attempt (C_SURV), and no finite audit, entails
  Confirmed(A^-_chi). This restates calculus (30)'s N-grade
  non-implication as a numbered acceptance constraint on certificates,
  exactly parallel to PIN-CONS-A2. It forbids a derivation nobody should
  perform; it constrains no table entry.

## 5. Two-sided checks per row

- N8: M-pass has a finite suite all of whose members are marked Pass and
  an outside theory marked not-Pass (the row shape); M-nopass has the
  outside theory marked Pass (row fails). Pass marks are free per
  theory; D1 decides nothing.
- N9: M-epi has a typed episode with no capacity and no generator role
  (both denials hold; N9 shape). M-gen adds a declared generator role —
  the CreativeGenerator denial fails while Epi and the CreativeCap denial
  stand. D8 decides nothing in either direction.
- N10: M-possible declares T possible with no PK bearer (row shape);
  M-bearer adds a PK^cur bearer (denial fails). D2 decides nothing.
- N12: M-art has p_code recorded as produced with no recipe role and no
  Exp (row shape); M-rec adds RecipeKnow. D3 decides nothing.
- N13: M-bare has an observed record with no package (row shape via D4);
  M-pkg adds CritPkg. D4/D5/D6 decide nothing.
- N14: M-surv has CritPkg with C_SURV and no Confirmed — and PIN-EPIST-A1
  GUARANTEES the denial limb survives any survival: the negative
  guard-rail keeps the N14 shape satisfiable by construction. M-conf
  adds a declared Confirmed independently (A1 forbids deriving it from
  survival, not declaring it) — the limb fails. Both directions remain.
- N16: M-uncrit has an empty declared criticism space (D9) and/or a
  declared final output (D10), with no physical episode (row shape);
  M-exp adds PhysExpEpisode. D9/D10 decide nothing.

## 6. What this record deliberately does NOT pin

Confirmed's positive semantics (PIN-EPIST-OPEN-1); the
Artifact/ArtifactClassified_eta relationship (PIN-EPIST-OPEN-2).
FiniteTheorySuite is already defined at (63) and its finiteness-only
reading was disclosed in PIN-CONS-v1's sibling treatment; family D13
notes Pass is newly pinned here but the suite itself is untouched.
Nothing about CritPkg, Epi, CreativeCap, PhysExpEpisode, PK^cur — frozen
or pinned elsewhere.

## 7. Affected dependency cones (no readiness change)

- Semantic families: D8, D13, D14, D15, D17 (leaves pinned; none
  reclassified).
- N-rows (cones only): N8, N9, N10, N12, N13, N14, N16.
- Controls: NC_BARE_POSSIBILITY_WITHOUT_PRIOR_KNOWLEDGE,
  NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE,
  NC_AGREEING_RESULT_NOT_CONFIRMATION, NC_UNREFUTABLE_OUTPUT,
  NC_NONPHYSICAL_RECIPE consume (62b) abbreviations; recorded vectors
  unchanged.
- Explicitly unchanged: the frozen calculus, SPA-v1, all sealed records,
  all bridges, ADM counts, IC-SP-001/002 (unrun).
- Row readiness unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
  untestable; zero discharged; testing PROHIBITED.

## 8. Forbidden items

No original N-row change, test, or repair; no fixture construction or
run; no total expansion or row bridge; no source import as theorem; no
in-place edit of any frozen or sealed file; no semantic choice justified
by a desired row outcome; no claim about creativity in any real system.

## 9. Residual status and next checkpoint

Frozen: PIN-EPIST-D1..D10 and acceptance axiom PIN-EPIST-A1. Open:
PIN-EPIST-OPEN-1 (Confirmed positive semantics), PIN-EPIST-OPEN-2
(Artifact vs ArtifactClassified_eta relationship — any future
identification is a reviewed bridge, never an edit). This completes the
pinning stage's term coverage: every Section 12 leaf is now either pinned
by a named record or carried as a named OPEN item. Next checkpoint:
DSF-v1 Section 13 item 6, the bridge review — every future and existing
bridge reviewed for grade, adequacy, circularity, and no-splicing.
