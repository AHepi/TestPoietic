# Capacity Update Typing — Record v1

record_id: CAP-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: CAPACITY_UPDATE_TYPING_V1.md
plain_language_file: CAPACITY_UPDATE_TYPING_V1_PLAIN_LANGUAGE.md
digest_manifest: CAPACITY_UPDATE_TYPING_V1_FREEZE.json
sha256_official: CAPACITY_UPDATE_TYPING_V1_FREEZE.json#official_sha256
sha256_plain_language: CAPACITY_UPDATE_TYPING_V1_FREEZE.json#plain_language_sha256
parent_records: DSF-v1 (Finding DSF-F1, Section 13 item 1); SPA-v1 (Section 5.2, unchanged); TH-v2; HKEY-v1
scope: a well-typed repair of the Update call sites in the two capacity clauses of SPA-v1 Section 5.2, implementing DSF-v1 Section 13 item 1
claims: freezes candidate typings, selects one with stated rationale, classifies every change, names affected cones, and records a two-sided non-deciding check
non_claims: does not edit SPA-v1 in place; does not re-derive ADM-T1 or restore any B2 status; does not test or discharge an original N-row; does not construct a fixture; does not prove creativity or non-creativity

Classification taxonomy used throughout: the four buckets of TH-v1/DSF-v1
Section 4 (definition, acceptance axiom, import, bridge). The reduct and
witness structures of Section 4 are record artifacts used as checks, not
semantic additions; they carry no classification.

## 1. Defect addressed (DSF-F1, restated from source)

SPA-v1 Section 5.1 declares

    Update: Assessment x Policy x Selector x S -> {0,1}.

Section 5.2 defines a policy context mu=(a,s,pi,q,t) whose pi and q are
TOTAL FINITE TABLES over reachable states:

    pi: {u : Reach(s0,u)} -> Policy,
    q:  {u : Reach(s0,u)} -> Selector.

Two capacity clauses then call

    Update(x, pi_mu, q_mu, s'').

Both call sites pass whole tables where the declared operation requires one
Policy and one Selector. The expression is therefore ill-typed, and with it
FCanSustainConsequentialAppraisal, FCanDrawOnOwnedEvaluatedTarget,
FCreativeCap, and the positive structure used in ADM-T1. DSF-v1 recorded
this as OPEN_UPDATE_TYPE and stripped ADM-T1's B2 status. This record
repairs the typing only; it does not re-derive ADM-T1.

## 2. Reachability side condition and CAP-A1

The context tables are total only on {u : Reach(s0,u)}, so the repaired
call Update(x, pi_mu(s''), q_mu(s''), s'') is defined only if s'' is
reachable. The two clauses differ here:

- In FCanSustainConsequentialAppraisal, s'' is the target of a terminal
  owned edge chain from s_mu, and FAdmissible(mu) gives Reach(s0,s_mu).
  Since TerminalOwnedEdge(a,u,v;g) implies Reach(u,v) directly from the
  definitions of OwnedActionPath and the transition relation in SPA-v1
  5.1, Reach(s0,s'') holds. No change is needed at this call site beyond
  the pointwise evaluation.
- In FCanDrawOnOwnedEvaluatedTarget, s'' is introduced only by
  Select(q_mu(s'),s',s'') being defined. SPA-v1 does not require Select to
  return an edge with source s' and target s'' (the first half of DSF-v1
  3.4(7)). Without that coherence, Reach(s0,s'') is not guaranteed and the
  repaired call would import a latent partiality of exactly the kind this
  tranche exists to eliminate.

SPA-CAP-v1 therefore adds:

    CAP-A1 (endpoint coherence of selection):
    Select(q,s,s') = g  implies  src(g) = s and tgt(g) = s'.
                                          (classification: acceptance axiom)

Under CAP-A1, Select(q_mu(s'),s',s'') defined yields an edge s'->s'', hence
Reach(s',s''), hence Reach(s0,s'') via the clause's TerminalOwnedEdge into
s' and FAdmissible. CAP-A1 also addresses the first half of DSF-v1 3.4(7);
the second half (agent transitions increasing Time_A) remains open and
belongs to the Section 13 item 4 sweep. Both consumers are named here.

## 3. Candidate typings

Option U1 — pointwise evaluation at the successor state (SELECTED).
Replace both call sites by

    Update(x, pi_mu(s''), q_mu(s''), s'').

The declared signature of the primitive table Update is unchanged; the
context tables are evaluated at the state the clause binds. Classification:
DEFINITION CHANGE at two clause bodies in the prospective fragment
SPA-CAP-v1.

Option U2 — re-type the primitive to accept table families:

    Update: Assessment x (Reach -> Policy) x (Reach -> Selector) x S -> {0,1}.

Classification: primitive re-typing. Rejected: it enlarges the primitive's
footprint, makes each Update entry depend on whole tables including states
unrelated to the transition being appraised (a spurious-dependence
invitation of the kind the target-essentiality seam warns against), and
repairs the call sites by moving the defect into the signature rather than
resolving it.

Option U3 — pointwise evaluation at the assessment state:
Update(x, pi_mu(s'), q_mu(s'), s''). Typable. Rejected, with the reason
stated per clause because the two clauses differ:

- FCanSustainConsequentialAppraisal pairs the Update call with a
  policy-update edge g' terminating at s'' (PolicyUpdateOutput(g')=1), so
  evaluating the policy in force at s' would test the PRE-update policy
  against the POST-update state, contradicting that clause's pairing.
- FCanDrawOnOwnedEvaluatedTarget has no g' and no PolicyUpdateOutput; its
  s'' is the state selected into by q_mu(s'). For this clause U3 is not
  contradicted by an edge pairing — indeed U3's q_mu(s') is the selector
  that performed the selection. U1 is retained here for UNIFORMITY of the
  context-evaluation rule (the context is evaluated at the state where the
  outcome is registered) and for consistency with the first clause.

Recorded honestly: the source text forces neither U1 nor U3, and for the
second clause a mixed reading is also typable. U1 is a stipulated reading
defended by the first clause's pairing and by uniformity, not by any
desired outcome.

## 4. The choice is load-bearing

U1 and U3 can diverge. Take a fixed context mu with pi_mu(s') !=
pi_mu(s'') (this requires a two-element Policy carrier, so the witness is
a small extension of the Section 5 reduct, not the reduct itself) on the
same single-chain skeleton, where the clause-level existential witnesses
are unique (one candidate chain, one assessment x, one successor pair),
so the clause value equals the value of the single relevant Update entry.
Set

    Update(x, pi_mu(s''), q_mu(s''), s'') = 1  and
    Update(x, pi_mu(s'),  q_mu(s'),  s'') = 0:

under U1 the clause is true, under U3 false, and no other witness rescues
it because none exists. The selection is therefore recorded as a semantic
decision with a named justification, not absorbed silently.

## 5. Two-sided non-deciding check

Reduct: A={a}; S={s0,s1,s2,s2',s3,s4} with Time_A(s0)=0; Policy={pi*} and
Selector={q*} are SINGLETON carriers, so every admissible context has
pi=const(pi*), q=const(q*); FAdmissible forces s=s0 and t=0, so the
existentially quantified mu in FCreativeCap is UNIQUE in this reduct.
Edges, all owned by a: g0: s0->s3 with CandidateOutput(g0)=c=Cand(s3),
NonSeed(c)=1, Ancestry(c) defined; gp: s0->s4 with
PromotionOutput(gp)=p=Promote(s4), A5(p)=1; g1: s0->s1 with
AssessmentOutput(g1)=x=Assess(s1), AssessEvidence(x) defined; g2: s1->s2
with PolicyUpdateOutput(g2)=1. For the draw-on clause, a separate
selection edge gs: s1->s2' with Select(q*,s1,s2')=gs (coherent per
CAP-A1), AssessmentTarget(x)=q*=EvidenceTarget(AssessEvidence(x)), and
FExternalEveryTarget(a,mu)=0 witnessed by an external-owned selection
elsewhere in the table.

The four clause witnesses share pi, q, and the Update table, so
cross-clause dependence is made explicit by construction: the sustain
clause consults the Update row (x, pi*, q*, s2); the draw-on clause
consults the distinct row (x, pi*, q*, s2'), held fixed at 1 in both
structures; the construction and promotion clauses consult no Update row.
The only row flipped between the two structures is (x, pi*, q*, s2).

- M_cap: Update(x, pi*, q*, s2) = 1. All four capacity clauses hold for
  the unique admissible mu, so FCreativeCap(a,0) is true.
- M_nocap: Update(x, pi*, q*, s2) = 0; every other table and pin is
  unchanged. The sustain clause fails; since mu is unique in this reduct,
  no alternative context rescues it, so FCreativeCap(a,0) is false.

Both structures are well-typed under SPA-CAP-v1 and agree on every symbol
of the repair; they differ in exactly one Update row. Therefore the U1
typing entails neither FCreativeCap nor its negation. The singleton-carrier
device is what closes the existential re-quantification over mu; without
it, an alternative context could consult a different Update row and the
claim would fail, as the independent review demonstrated.

Check 2 (redundancy) is not the right axis for this tranche and is recorded
as such: the repair assigns a denotation to a previously ill-typed
expression; it adds no constraint that could be redundant. CAP-A1 is a real
added constraint; its non-redundancy is immediate because SPA-v1 permits
Select tables violating endpoint coherence, which CAP-A1 excludes. What had
to be shown for U1 is that no verdict is baked in, which the pair above
establishes.

Check 3 (steering): rationale-based only, per the HKEY-v1 downgrade. No
comparative non-deciding check was run for U2/U3; none is claimed.

## 6. Affected dependency cones

- Semantic family: D7 (CreativeCap and finite capacity), whose status moves
  from OPEN_UPDATE_TYPE to typed-pending-seal of SPA-CAP-v1.
- DSF-v1 Section 11 items: A-08 (four FCan clauses) and A-09 (FCreativeCap).
- Audit head: Cap-hat.
- Original N-rows (cones only, rows untouched): N2, N3, N6, N9, N11.
- Explicitly examined and unchanged: FAdmissible (used by the reduct; its
  own OPEN_ADMISSIBILITY_B3 status belongs to DSF-F3, untouched);
  FExternalEveryTarget (a conjunct of the draw-on clause; the repair does
  not touch it; A-07's missing Boolean signature remains open and belongs
  to the Section 13 item 4 sweep); A-06 (policy context/FAdmissible proxy,
  unchanged); report projections and E-priority items (no consumer of the
  repaired call sites).
- Secondary closure: CAP-A1 addresses the first half of DSF-v1 3.4(7); the
  Time_A half remains open.
- ADM-v1: ADM-T1 and ADM-U3 remain stripped/OPEN; the counts B1=0, B2=0,
  B3=3 are UNCHANGED, because re-deriving the two-sided independence
  result is a separate tranche (DSF-v1 Section 13 item 2), not a
  consequence of the typing repair.
- DSF-F3 (free original admissibility) is untouched.

Cone completeness is a manual trace over DSF-v1 Sections 6 and 11 with the
exclusions above stated explicitly; subject to the same caveat as HKEY-v1.

## 7. Versioning and obligations

- SPA-CAP-v1 is a prospective SUPERSESSION fragment: it revises the bodies
  of the two capacity clauses and adds CAP-A1, while SPA-v1,
  SPA-H-THRESH-v1, and SPA-HKEY-v1 remain unedited. Any integrated annex
  must name this record or restate the changes under a new version and
  hash.
- Every change carries its classification (Sections 2--3; taxonomy cited in
  the header note).
- Official, plain-language, and digest-manifest forms per RPS-v1.
- DSF-v1 and ADM-v1 remain immutable history; this record supersedes only
  the call-site typing portion of DSF-F1 and the first half of 3.4(7).

## 8. Forbidden items

No original N-row change; no fixture construction or run; no source bridge
claim; no in-place SPA-v1 edit; no typing chosen to produce a desired
capacity verdict; no re-derivation of ADM-T1; no claim about creativity in
any real system.

## 9. Residual status and next checkpoint

The repair entails no capacity verdict: Section 5 exhibits both a
satisfying and a falsifying structure under the repaired typing. Row
readiness is unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
untestable; zero discharged. The next checkpoint per DSF-v1 Section 13
item 2 is the two-sided restriction re-check: re-attempt ADM-T1's
independence result under SPA-CAP-v1, with the explicit warning that a
failed re-derivation is a result, not a repair license.
