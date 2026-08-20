# H Witness-Key Binding — Record v1

record_id: HKEY-v1
version: 1.0
date: 2026-08-20
status: SEALED_HKEY_BINDING_PINNED_TESTING_PROHIBITED
official_file: HKEY_BINDING_V1.md
plain_language_file: HKEY_BINDING_V1_PLAIN_LANGUAGE.md
digest_manifest: HKEY_BINDING_V1_FREEZE.json
parent_records: DSF-v1 (Finding DSF-F2); TH-v2 (Sections 2--5); SPA-v1 (unchanged); TH2-D1 via TH-v2
scope: typed relations binding hkey(w)=(F,T,R) to the checked vehicle w.Vveh and the task implemented by w.CSigma, implementing TH-v2 Section 5 items 1--5
claims: defines the candidate pins, their classifications, affected cones, and independence checks
non_claims: no original N-row tested or changed; no fixture constructed or run; no SPA-v1 in-place edit; no source-level HRep claim; no bridge claimed

## 1. Defect addressed

DSF-F2: SPA-v1 fixes hkey(w)=(F,T,R) and then checks w.Vveh and w.CSigma,
but no typed condition connects the named system F to w.Vveh, or the named
task T to the task implemented by w.CSigma. TH2-D1 closed only the
threshold-typing portion. This record closes the key-binding portion at the
finite-fragment level only.

## 2. Carriers (from SPA-v1, read-only)

- SysName: carrier of nameable systems; F ranges over it.
- Vehicle: carrier of checked vehicles; w.Vveh is an element.
- Code: carrier of code words. This record takes w.CSigma to be an ELEMENT
  of Code. The family reading of CSigma is deferred; if a later tranche
  adopts it, the key check and HKEY-A2 must be restated in quantified form
  under a new version.
- Task: the task-graph carrier used by FDG_K.
- Protocol: finite protocol carrier; unchanged.

## 3. System binding — selected option S2

Add primitive Boolean table

    SysBind: SysName x Vehicle -> {0,1}        (classification: primitive data)

Add acceptance axiom HKEY-A1 (functionality), stated per structure:

    for all F, v1, v2: SysBind(F,v1) and SysBind(F,v2) -> v1 = v2
                                                      (classification: acceptance axiom)

Owner-resolved option Q1: functionality is AT MOST ONE vehicle per system
name. Models in which a nameable system has no checked vehicle are not
excluded.

Rejected alternatives, with reasons:
- S1 (carrier identification, F = w.Vveh): rejected by overcommitment. It
  stipulates that a system name is a vehicle, merges two carriers, and
  forces a new fragment version for a modeling claim the source text does
  not state.
- S3 (unrestricted implementation relation ImplSys: Vehicle x SysName):
  rejected by scope risk. Without uniqueness, one key (F,T,R) can be
  discharged by a passing implementing vehicle while another implementing
  vehicle of the same system fails — the F8-D single-witness scope error at
  fragment level.

## 4. Task binding — selected option T1

Add primitive (partial) map

    tau: Code -> Task                            (classification: primitive data)

Owner-resolved option Q2: tau is PARTIAL. Totality would stipulate
implementability of arbitrary code.

Add acceptance axiom HKEY-A2 (definedness on used codes):

    for every witness w whose key is admissible, tau is defined on w.CSigma.
                                                      (classification: acceptance axiom)

Note on benign circularity: admissibility (below) partly requires tau
definedness, and HKEY-A2 requires definedness for admissible keys. When tau
is undefined on w.CSigma the key is inadmissible and HKEY-A2 is vacuously
satisfied; this vacuity is what keeps structure M_unbind (Check 2) a model
of all pins except the extended key check.

Rejected alternative:
- T2 (unrestricted matching relation TaskMatch: Task x Code): rejected as a
  uniqueness/determinacy defect. TaskMatch(T, w.CSigma) and
  TaskMatch(T', w.CSigma) can both hold for the same witness, so the key
  fails to determine which task the checked code implements. This is a
  per-witness determinacy failure, distinct from S3's cross-instance scope
  error; the shared root is the absence of functionality.

## 5. Extended key check — definition change

Owner-resolved option Q3: the binding lives in hkey ADMISSIBILITY, not as
extra FPT-HRoute conjuncts, keeping the route formula unchanged.

The key hkey(w)=(F,T,R) is admissible only if:

    SysBind(F, w.Vveh)  and  tau is defined on w.CSigma  and
    tau(w.CSigma) = T   (equality in the Task carrier).

Classification: DEFINITION CHANGE to key admissibility in the prospective
fragment SPA-HKEY-v1. SPA-v1, SPA-H-THRESH-v1, and the route predicate text
are not edited.

## 6. Affected dependency cones (TH-v2 item 4)

- Audit heads: Hsrc-hat, VehExists-hat, Veh-hat, DG-hat, H-hat.
- Original N-rows: N4, N6 (via family D4).
- Semantic family: D4. Its threshold half was closed by TH2-D1; its key half
  is this record. D4 remains PARTIAL until SPA-HKEY-v1 is sealed and any
  remaining D4 gaps are resolved.
- Definition sites directly modified (in SPA-HKEY-v1 only): the hkey
  admissibility definition; the meaning of FPT-HRoute's admissible-key
  argument changes accordingly, though its formula text does not. These are
  subsumed under H-hat in the head inventory and are named here explicitly.
- Cross-fragment items (DSF-v1 Section 10): "lineage tied to H route"
  partially; all others untouched.
- Secondary closure: T1 supplies the missing code-to-task embedding flagged
  in DSF-v1 3.4(1) for FDG_K; both consumers are named here.

Cone completeness was established by tracing the consumers of hkey and
FRouteData in the DSF-v1 Section 6 registry and Section 10 identity list;
it is a manual trace and should be re-derived mechanically in a later
tranche. No other head, row, family, bridge, or report projection is
believed affected, subject to that caveat.

## 7. Independence checks (TH-v2 item 5)

All checks use the singleton reduct of the TH2-D1 conservativity
demonstration recorded in TH-v2 Section 3 (N_R=0, P_R={c0}, W_R={w},
epsilon_{*,R}=1/2, every nonterminal route conjunct true, hkey(w)=(F,T,R),
FRouteData(w), FImplements(c0,w)), extended by the pins above.

Check 1 — the pins do not decide the route (required two-sided check).
Fix SysBind(F, w.Vveh)=true, tau defined on w.CSigma, tau(w.CSigma)=T.
- M_pass: err_R(c0) = 1/4 and FError(FOutput(c0,w),w.p) = 1/4. The terminal
  bound against epsilon=1/2 holds; FPT-HRoute is true.
- M_fail: err_R(c0) = 3/4 and FError(FOutput(c0,w),w.p) = 3/4. Every other
  route conjunct remains true, but the terminal bound against epsilon=1/2
  fails; FPT-HRoute is false.
Both structures satisfy HKEY-A1, HKEY-A2, and TH2-D1 and agree on every
symbol of the new pins; they differ only in the two error-table entries.
Therefore the binding restriction entails neither FPT-HRoute nor its
negation.

Check 2 — the pins are not redundant (add independent pressure).
Stated premise: in this reduct W_R={w}, so hkey(w) is the UNIQUE candidate
key; under the extended admissibility definition, failure of hkey(w)'s
admissibility therefore leaves no admissible key for the route.
M_unbind: identical to M_pass except SysBind(F, w.Vveh)=false. Every old
conjunct, including the terminal error bound at 1/4, still holds, but the
key is inadmissible and FPT-HRoute fails. (The same holds with tau undefined
on w.CSigma; by the Section 4 vacuity note, M_unbind still satisfies HKEY-A2
and every other pin.) Therefore the new clauses are not implied by the
existing fragment.

Check 3 — steering defense (claim downgraded after independent review).
No new structure is exhibited; M_both would duplicate M_pass. The defense
against outcome-steering is rationale-based, not witness-based: the
selection of S2/T1 over S1/S3/T2 rests on the documented structural
objections in Sections 3--4 (overcommitment; F8-D scope risk; determinacy),
and Check 1 establishes that the selected pins are non-deciding. No
comparative non-deciding check was run for the rejected alternatives, and
none is claimed.

If any check fails under a future restatement, the failure is recorded and
the pin is not silently revised.

## 8. Versioning and publication obligations

- Prospective fragment name: SPA-HKEY-v1, additive to SPA-v1 and
  SPA-H-THRESH-v1; neither is edited.
- Every addition carries its classification (Sections 3--5).
- Official, plain-language, and digest-manifest forms per RPS-v1.
- Independent mathematical review completed: verdict REVISE with ten
  findings; all ten repaired in this version (repair log available on
  request). Owner confirmed the three resolved options and accepted the
  official/plain-language pair on 2026-08-20, sealing this record.
- DSF-v1 remains immutable history; this record supersedes only the
  key-binding portion of DSF-F2, as TH-v2 superseded its threshold portion.

## 9. Forbidden items (TH-v2 Section 5)

No original N-row change; no fixture construction or run; no source bridge
claim; no in-place SPA-v1 edit; no semantic choice justified by a desired
separation; no HRep test; no claim about physical self-reproduction. All
confirmed by the independent review.

## 10. Residual status

The finite H-route family remains PARTIAL: the key is now typed and bound in
the prospective fragment, but the finite proxy still does not bridge to
source-level HRep, and DSF-F3 (free original admissibility) and DSF-F1
(capacity update typing) are untouched. Row readiness is unchanged:
PINNED=0, PARTIAL=2, OPEN=18; all 20 rows untestable; zero discharged.
