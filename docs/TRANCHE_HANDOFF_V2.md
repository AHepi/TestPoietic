# PoieticTest Tranche Handoff v2

record_id: TH-v2
version: 2.0
date: 2026-08-20
status: SEALED_HANDOFF_ONE_MINOR_SEMANTIC_PIN_TESTING_PROHIBITED
official_file: TRANCHE_HANDOFF_V2.md
plain_language_file: TRANCHE_HANDOFF_V2_PLAIN_LANGUAGE.md
digest_manifest: TRANCHE_HANDOFF_V2_FREEZE.json
sha256_official: TRANCHE_HANDOFF_V2_FREEZE.json#official_sha256
sha256_plain_language: TRANCHE_HANDOFF_V2_FREEZE.json#plain_language_sha256
parent_records: TRANCHE_HANDOFF_V1.md; DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: repository handoff after DSF-v1 and one minor semantic checkpoint fixing only the carrier of the finite H-route error threshold
claims: records the verified GitHub checkpoint; freezes TH2-D1 as a prospective finite-fragment type definition; records its conservative two-sided check; preserves the semantics-first stop rule
non_claims: does not modify SPA-v1 or the calculus, bind an H witness to its named system or task, validate HRep, test or discharge an original N-row, or prove creativity or non-creativity

## 1. Repository checkpoint

The downstream semantic freeze was committed and pushed before this record:

- branch: `agent/stress-test-continuation`;
- published commit: `994afa897b9633ce3a8ac9834021ad23bfa29cd2`;
- remote branch: `origin/agent/stress-test-continuation`;
- remote object check: exact match;
- DSF-v1 inventory: 25 unary heads, one binary head, eight reports, and all
  20 original N-rows;
- DSF-v1 row readiness: PINNED=0, PARTIAL=2, OPEN=18;
- original N-rows discharged: 0.

Only repository files are in publication scope. Credentials, personal files,
browser data, operating-system files, and unrelated computer contents are
excluded. No credential value is stored in this record or repository.

## 2. Minor semantic checkpoint

SPA-v1 gives each finite protocol R a threshold epsilon_{*,R} and compares it
with values of err_R and FError. Those error values lie in [0,1] intersect Q,
but SPA-v1 did not type the threshold itself.

### TH2-D1 — finite H-threshold carrier

For every R in the finite Protocol carrier,

    epsilon_{*,R} is an element of [0,1] intersect Q.

Classification: project-added stipulated semantic definition.

Scope: the prospective fragment class `SPA-H-THRESH-v1`. The bytes and claims
of SPA-v1 remain unchanged. Any later integrated annex must name this record
or restate the definition under a new version and hash.

Affected dependency cones: the finite H-route family; Hsrc, VehExists, Veh,
DG, and H audit heads; and original rows N4 and N6. This item does not supply
the missing system/vehicle or task/implementation identity and does not
bridge the finite proxy to source-level HRep.

## 3. Conservative two-sided check

TH2-D1 is a type declaration, not an answer to an H-route test. To make that
explicit, fix one protocol R with N_R=0, P_R={c0}, W_R={w},
enum_R(0)=c0, and epsilon_{*,R}=1/2. In both structures FComplete_R is true;
set hkey(w)=(F,T,R), FRouteData(w), FImplements(c0,w), and every other
nonterminal FProtocolChain conjunct true. Use the same singleton carriers,
key, witness, implementation, output, and non-error route data. No second
candidate or witness can supply an alternative passing chain.

- Structure M_pass assigns both err_R(c0) and its required matching value
  FError(FOutput(c0,w),w.p) the value 1/4. The terminal bound holds, so
  FProtocolChain and FPT-HRoute are true.
- Structure M_fail assigns both matching error values the value 3/4. Every
  other route conjunct remains true, but the terminal bound fails, so
  FProtocolChain and FPT-HRoute are false.

These are two expansions of the same TH2-D1 reduct. Both satisfy TH2-D1 and
agree on every symbol occurring in that definition; their error tables vary
only outside it. Therefore TH2-D1 entails neither the finite FPT-HRoute proxy
nor its negation.

This is a local conservativity check for the stipulated type only. It is not
an original N-row model, a total expansion of the source theory, a test of
HRep, or evidence about physical self-reproduction.

## 4. Resulting status

Relative to the prospective fragment `SPA-H-THRESH-v1`, only the isolated
threshold-typing defect is closed. The finite H-route family remains PARTIAL:
hkey(w)=(F,T,R) is still not tied to the checked vehicle w.Vveh or to the task
implemented by w.CSigma, and every other H-route gap recorded by DSF-v1 also
remains open. `KEY_BINDING` is a next-work flag, not an exhaustive status.

DSF-v1 remains the immutable historical inventory. Its published status is
not rewritten. For future work, this record supersedes only the threshold-
typing portion of DSF-F2.

No audit head becomes source-semantically PINNED. The original row readiness
therefore remains PINNED=0, PARTIAL=2, OPEN=18, with all 20 rows untestable and
zero discharged.

## 5. Handover for the next tranche

The next tranche must remain semantics-only and bounded to the H witness-key
binding. It must:

1. choose and type the relation between named F and checked w.Vveh;
2. choose and type the relation between named T and the task implemented by
   w.CSigma;
3. classify each addition as definition, acceptance axiom, import, or bridge;
4. name every affected head and N-row;
5. show that any test-domain restriction does not already decide the route;
6. publish official and plain-language forms with a digest manifest; and
7. run independent mathematical and publication reviews before commit.

Forbidden in that tranche: changing an original N-row, building or running a
row fixture, claiming a source bridge, editing SPA-v1 in place, or using a
semantic choice merely because it produces the desired separation.

After that tranche, continue the DSF-v1 order: finish primitive signatures,
freeze cross-domain identities, pin remaining source terms, and only then
design original-row tests.

## 6. Stop condition

This record completes exactly one minor semantic checkpoint after DSF-v1 and
updates the handover. Work stops after its commit is pushed and the remote
object is verified. No further semantic pin, fixture, row test, or repair is
authorized in this tranche.
