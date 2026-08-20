# Admissibility Two-Sided Re-Check — Record v1

record_id: ADM-RECHECK-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: ADM_RECHECK_V1.md
plain_language_file: ADM_RECHECK_V1_PLAIN_LANGUAGE.md
digest_manifest: ADM_RECHECK_V1_FREEZE.json
sha256_official: ADM_RECHECK_V1_FREEZE.json#official_sha256
sha256_plain_language: ADM_RECHECK_V1_FREEZE.json#plain_language_sha256
parent_records: ADM-v1 (Theorem ADM-T1); DSF-v1 (Finding DSF-F1, Section 13 item 2); CAP-v1 (SPA-CAP-v1, dependency)
scope: re-derivation of the two-sided independence of the finite admissibility restriction under the repaired capacity typing, implementing DSF-v1 Section 13 item 2
claims: supplies an explicit witness pair showing the ADM-D1/ADM-A2 restriction entails neither FCreativeCap nor its negation under SPA-CAP-v1
non_claims: does not edit ADM-v1, DSF-v1, SPA-v1, or CAP-v1; does not define source-level admissibility (DSF-F3 untouched); does not test or discharge an original N-row; is conditional on the owner seal of CAP-v1

## 1. What is being re-derived and why it needed re-deriving

ADM-v1 Theorem ADM-T1 claimed that the class K_ADM of finite SPA-v1
fragment structures satisfying ADM-A2 models neither FCreativeCap(a,t) nor
its negation. Its positive witness M+ required "the policy update is
effective," i.e. a true Update entry — and the Update call was ill-typed
(DSF-F1). DSF-v1 therefore stripped ADM-T1 and moved ADM-U3 from B2 to B3,
leaving counts B1=0, B2=0, B3=3.

CAP-v1 repairs the call sites by pointwise evaluation at the successor
state and adds CAP-A1 (Select endpoint coherence). This record re-derives
the two-sided result under the prospective fragment SPA-CAP-v1. It is
conditional on the owner seal of CAP-v1; if CAP-v1 is amended, this record
must be re-checked against the amended text.

## 2. Restated target

Let K_ADM' be the class of finite fragment structures satisfying SPA-v1 as
modified by SPA-CAP-v1 (pointwise Update calls, CAP-A1) together with
ADM-D1 and ADM-A2. The claim, numbered ADM-T1-R:

    K_ADM'  does not model  FCreativeCap_A(a,t)      and
    K_ADM'  does not model  not FCreativeCap_A(a,t).

## 3. Witness pair

Both structures share one admissibility reduct: A={a}; singleton Policy
carrier {pi*}; singleton Selector carrier {q*}, with Selector =
Nodes(Prov) = {q*}; Time_A(s0)=0 and Time_A strictly positive at every
other state, so a context mu=(a,s,pi,q,t) with Time_A(s)=t has s=s0 when
t=0; unique total tables pi=const(pi*), q=const(q*). Then
C_adm_{a,0} = {mu0} with mu0=(a,s0,pi,q,0): membership is nonempty,
finite, and COMPLETE because C_adm is defined by comprehension over the
fixed carriers via ADM-D1 (every well-typed context with Time_A(s)=0 and
FAdmissible(mu) is included by construction); and membership is determined
entirely by reachability, the time table, and the fixed singleton tables,
so ADM-D1 and ADM-A2 hold in both structures and membership cannot depend
on any capacity table.

M_minus: states s0,s1,s2,s2',s3,s4; edges g0: s0->s3, gp: s0->s4,
g1: s0->s1, g2: s1->s2, gs: s1->s2', ALL externally owned. Then no
TerminalOwnedEdge(a,...) exists, so the construct, sustain, and promote
clauses fail for every admissible context. The draw-on clause fails too,
on two independent conjuncts: its selected edge must be owned by a_mu
(impossible; all edges are external), and FExternalEveryTarget=1 (every
defined selection is external), whereas the clause requires 0. Since every
clause fails for every admissible context — no uniqueness step is needed —
M_minus models not FCreativeCap(a,0).

M_plus: same carriers, states, and edge endpoints, with all five edges
owned by a. Tables: CandidateOutput(g0)=c=Cand(s3), NonSeed(c)=1,
Ancestry(c) defined; PromotionOutput(gp)=p=Promote(s4), A5(p)=1;
AssessmentOutput(g1)=x=Assess(s1), AssessEvidence(x) defined;
PolicyUpdateOutput(g2)=1; Select(q*,s1,s2')=gs (endpoint-coherent per
CAP-A1); AssessmentTarget(x)=q*=EvidenceTarget(AssessEvidence(x)); the
sustain clause's call, under the pointwise reading with pi_mu0(s2)=pi* and
q_mu0(s2)=q* in this singleton reduct, is the single row
Update(x, pi*, q*, s2), set to 1; the draw-on clause's own row
Update(x, pi*, q*, s2') = 1; and FExternalEveryTarget(a,mu0)=0 because gs
itself is a defined selection owned by a, i.e. some selected target is not
external (the definition's =1 case requires all selected targets
external). All four capacity clauses hold for mu0, and existence of one
admissible context suffices, so M_plus models FCreativeCap(a,0).

The two structures agree on every membership-determining input fixed by
ADM-D1 and ADM-A2 (carriers, s0, Time_A, reachability skeleton, policy and
selector tables, provenance nodes). They differ only in edge ownership and
capacity-relevant output/Update tables, none of which is an
admissibility-membership input. Therefore the stipulated admissibility
restriction alone entails neither the positive nor the negative capacity
result, which is ADM-T1-R.

## 4. What changed relative to ADM-T1, stated exactly

1. The ill-typed call Update(x, pi_mu, q_mu, s'') is replaced by the
   SPA-CAP-v1 pointwise form; in the singleton reduct it reduces to a
   single Update row.
2. The selection edge gs is required to be endpoint-coherent, which CAP-A1
   supplies; ADM-v1 did not state this condition.
3. Clause-level witnesses are secured by singleton Policy and Selector
   carriers: pi and q are forced to the constant tables, and with
   Time_A(s0)=0 stipulated strictly below all other states, mu0 is the
   unique admissible context at (a,0). Uniqueness is used only for the
   ADM-A2 membership claim; the negative direction of ADM-T1-R rests on
   uniform clause failure in M_minus and needs no uniqueness step, and the
   positive direction needs only existence.

## 5. Effect on counts and statuses

If this record is accepted AND CAP-v1 is sealed:

- ADM-U3 returns from B3 to B2. The current admissibility counts become
  B1=0, B2=1, B3=2.
- ADM-v1 remains immutable history; DSF-v1 remains immutable history. This
  record supersedes DSF-v1's present-tense stripping of ADM-T1, scope-
  limited to the finite fragment under SPA-CAP-v1.
- The five source-level rows keep substatus OPEN_ADMISSIBILITY_B3: DSF-F3
  (free source-level Admissible_eta) is untouched by this record.
- Row readiness is unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
  untestable; zero discharged. ADM-T1-R is a local independence result for
  a finite predicate, not an episode-versus-capacity fixture, not a total
  model of the frozen source theory, not an annex-to-source bridge.

## 6. Failure disclosure obligation

Per DSF-v1 Section 13 item 2: had the re-derivation failed, the failure
would have been recorded as the result. It did not fail. The residual
weakness is recorded instead: ADM-D1's second conjunct is automatic in the
fragment (Selectors are already provenance nodes), so the restriction the
independence result covers is weak — it is essentially reachability plus
non-filtering. This was true of ADM-T1 as well and is repeated here so the
restored B2 is not read as stronger than it is.

## 7. Forbidden items

No original N-row change; no fixture construction or run; no source bridge
claim; no in-place edit of any sealed record; no claim about creativity in
any real system; no use of the result to strengthen NOT_ESTABLISHED into
falsity.

## 8. Next checkpoint

DSF-v1 Section 13 item 4: the primitive-signature and cross-fragment
identity sweep (Kind, Pkg, Evid, FDerives, FInterprets, OutcomeSpace,
FSuitable, FIncompatible, NonSeed; FPartOf, FCarries, FBlindCopy,
FErrorCorrect, FBuildWithResources; Eq; key/label/Transport; the Time_A
half of 3.4(7); and the Section 10 identity list), one bounded record per
cluster, each with the same classification and non-deciding discipline.
Item 3 (H-route binding) was completed early as HKEY-v1; item 1 as CAP-v1;
item 2 is this record.
