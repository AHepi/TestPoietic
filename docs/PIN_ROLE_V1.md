# Semantic Pinning Record — Role Cluster v1 (N17, N19, RetainsOrAdapts)

record_id: PIN-ROLE-v1
version: 1.0
date: 2026-08-21
status: REVIEWED_PENDING_OWNER_SEAL
official_file: PIN_ROLE_V1.md
plain_language_file: PIN_ROLE_V1_PLAIN_LANGUAGE.md
digest_manifest: PIN_ROLE_V1_FREEZE.json
sha256_official: PIN_ROLE_V1_FREEZE.json#official_sha256
sha256_plain_language: PIN_ROLE_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md (frozen calculus); ORIGINAL_TERMS_INVENTORY.md (pinned catalog); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, pinned per ERR-SPA-v1 to a9f62ebb...); SPA_PIN_ERRATUM_V1.md (ERR-SPA-v1); DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); PIN_CONS_V1.md (carries PIN-CONS-OPEN-1); PIN_VE_V1.md; PIN_SUB_V1.md (carries the role machinery this record reuses); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: original-side candidate pins for the role cluster: RoleEq, SecondSubstance, CausalExemption (N17); OneObservedToken, CounterfactualFamilyObserved, ReplicationRole (N19); and the deferred RetainsOrAdapts (N20 limb, previously PIN-CONS-OPEN-1)
claims: freezes seven named, classified candidate meanings (PIN-ROLE-D1..D7) with options stated and per-cluster two-sided independence arguments; resolves PIN-CONS-OPEN-1 with a disclosed conditionality
non_claims: does not test, discharge, or change any original N-row; does not move any readiness count; does not edit the frozen calculus, SPA-v1, or any sealed record; does not identify any original predicate with an F-prefixed fragment predicate; is conditional on the pending seals of PIN-CONS-v1 and PIN-SUB-v1 (it reuses their pins); does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4.
This record uses only the definition bucket. Check structures are record
artifacts, not semantic additions.

## 1. Scope and method

Per DSF-v1 Section 13 item 5 and the pinned catalog's order, this record
covers the remaining role-side leaves: the N17 triple, the N19 pair plus
ReplicationRole, and RetainsOrAdapts, which PIN-CONS-v1 left open
(PIN-CONS-OPEN-1) pending a non-rigging reading. That reading is now
available from PIN-SUB-v1's role machinery. Because both predecessors remain
unsealed (REVIEWED_PENDING_OWNER_SEAL), this record is explicitly
CONDITIONAL on their eventual seal; if either is amended, this record
must be re-checked.

Method rule: weakest meaning making the frozen occurrences well-typed;
for each row, the pins must leave the row's full antecedent-and-denial
shape satisfiable and its failure satisfiable.

## 2. Exact anchors

N17 row NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE (transcribed from math form):

> M models RoleEq_eta(b,k) and not SecondSubstance(b,k) and not
> CausalExemption(b,k)

N19 row NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE (transcribed):

> M models OneCopyOnly_{eta,theta} and not PK^cur_eta(b,k;X_I,T) and
> not Sel_eta(lambda) and not ReplicationRole_eta(b,k)

Calculus (63), OneCopyOnly abbreviation (transcribed):

> OneCopyOnly_{eta,theta} iff OneObservedToken(b,k) and not
> CounterfactualFamilyObserved_eta(b,k)

N20 row (transcribed in PIN-CONS-v1 Section 2), whose existential denial
limb contains not RetainsOrAdapts_{eta',theta'}(nu*,E*).

Source-register constraints (paraphrase-level, per the register's own
quotation discipline): FOR_EMERGENCE supplies higher-level explanatory
autonomy compatible with physical realization and expressly rejects a
second substance and a causally exempt abstract entity. FOR_REPLICATOR_NICHE
supplies replication/adaptation as contextual counterfactual causal roles
across bearer and environmental variants, with the express limit that it
is not a creativity criterion. FOR_GENE_STRUCTURE supplies the one-copy
guard: a one-copy local inspection cannot by itself settle a
counterfactual role across nearby variants. None of these is imported as
a theorem here; they constrain the pins' shape only.

## 3. N17 pins

PIN-ROLE-D1 — RoleEq (definition; load-bearing). RoleEq_eta(b,k) holds
iff the declared higher-level explanatory role of the pair (b,k) is
preserved under its declared physical realization: the higher-level
account and the realization account answer the same declared task.
Autonomy-with-realization, per FOR_EMERGENCE's shape. Rejected options:
RoleEq as identity of levels (would make SecondSubstance collapse into
it, tangling the conjuncts); RoleEq as mere co-occurrence (vacuous,
would manufacture the N17 antecedent).

PIN-ROLE-D2 — SecondSubstance (definition; load-bearing).
SecondSubstance(b,k) holds iff the structure's declared ontology for
(b,k) posits an additional substance beyond the physical bearer — an
ontologically independent extra entity. In any structure that posits no
such entity, it is false. Rejected option: reading it as any
higher-level talk (would make it true wherever RoleEq holds, destroying
N17).

PIN-ROLE-D3 — CausalExemption (definition; load-bearing).
CausalExemption(b,k) holds iff the higher-level account of (b,k) is
declared exempt from physical causation — an exemption claim, not a
feature of physical causation. Rejected option: reading it as causal
inertness in fact (unverifiable by design and would either be always
false or always true; both rig N17).

Two-sided check for N17: M-hi has RoleEq true (role preserved) with no
second substance and no exemption claim — the full N17 shape holds.
M-lo has RoleEq false (the realization does not answer the declared
task) — the antecedent fails. Both satisfy every pin. The pins decide
neither RoleEq nor the denial limbs.

## 4. N19 pins

PIN-ROLE-D4 — OneObservedToken (definition): exactly one observed token
of the pair (b,k) occurs in the declared evidence records. Counting
evidence, no role content.

PIN-ROLE-D5 — CounterfactualFamilyObserved (definition; load-bearing):
the declared evidence contains a family of nearby variants of the bearer
with observed outcomes in the declared environment — per
FOR_GENE_STRUCTURE's guard, this is what a one-copy inspection LACKS.
Rejected option: requiring observed counterfactual outcomes across
environments (over-strong; would make the negation in (63) nearly
always true, manufacturing OneCopyOnly).

PIN-ROLE-D6 — ReplicationRole (definition; load-bearing):
ReplicationRole_eta(b,k) holds iff (b,k) occupies a declared
counterfactual replication role: its role profile (per PIN-SUB-v1's
RE-role reading) is preserved across a declared family of bearer variants
in the declared niche/environment class, per FOR_REPLICATOR_NICHE.
Rejected option: any copied token counts (would make ReplicationRole
true whenever a copy exists, colliding with OneCopyOnly's surface reading
and destroying the N19 shape: the row needs one copy WITHOUT the role).

Two-sided check for N19: M-one has exactly one observed token, no variant
family observed, no replication role — OneCopyOnly holds and
ReplicationRole fails. M-fam adds a declared variant family with
preserved role — the denial limb fails. Both satisfy every pin; the pins
decide neither limb. (The row also denies PK^cur and Sel; those are
already frozen elsewhere and untouched here.)

## 5. RetainsOrAdapts — resolving PIN-CONS-OPEN-1

PIN-CONS-v1 left RetainsOrAdapts open because either natural pin rigged
N20: "finite-suite success extends" destroys the row (no failing outside
pair could exist), and "always fails outside U" manufactures it. The
role machinery from PIN-SUB-v1 supplies the non-rigging reading:

PIN-ROLE-D7 — RetainsOrAdapts (definition; load-bearing; CONDITIONAL on
PIN-SUB-v1's seal): RetainsOrAdapts_{eta',theta'}(nu,E) holds iff the
variant nu's declared counterfactual role profile is preserved or adapted
in environment E within the extension (eta',theta') — read exactly as
PIN-SUB-D2's role-profile comparison applied to the declared variant and
environment carriers. Whether the role holds for a given (nu,E) is table
data, free per pair: no suite-membership fact entails it either way.

Two-sided check for the N20 limb: in M-ret, the outside pair (nu*,E*)
has its role profile preserved — the limb fails. In M-noret, the same
pair's profile fails in E* — the limb holds. Both satisfy D7 and every
prior pin. The N20 existential-denial shape is neither destroyed nor
manufactured. This resolves PIN-CONS-OPEN-1; the resolution is recorded
in both this manifest and the ledger, with the conditionality stated:
if PIN-SUB-v1's RE-role reading is amended, D7 is re-checked.

## 6. What this record deliberately does NOT pin

Nothing about PK^cur, Sel, or the extension relation (frozen or pinned
elsewhere). No fragment predicate is introduced or identified. The
EverettianUniversalClaim positive semantics remain PIN-CONS-OPEN-2 and
untouched. No OPEN item is created beyond the disclosed conditionality;
SIG-HJ-OPEN-1/2 and IDENT-OPEN-1 are untouched.

## 7. Affected dependency cones (no readiness change)

- Semantic families: D18 (N17 leaves; status NOT reclassified), D20
  (N19 leaves; same), D21 (RetainsOrAdapts resolution inside it; same).
- N-rows (cones only): N17, N19 directly; N20 via the D7 resolution of
  its denial limb's predicate; N6 untouched (WholeClone/WholeDigital are
  family D11, not covered).
- Explicitly unchanged: the frozen calculus, SPA-v1, all sealed records,
  all bridges, ADM counts, the N18 joint pin, IC-SP-001/002 (unrun).
- Row readiness unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
  untestable; zero discharged; testing PROHIBITED.

## 8. Forbidden items

No original N-row change, test, or repair; no fixture construction or
run; no total expansion or row bridge; no source import (the register's
constraints shape the pins but nothing is imported as a theorem); no
in-place edit of any frozen or sealed file; no semantic choice justified
by a desired row outcome; no claim about creativity in any real system.

## 9. Residual status and next checkpoint

Frozen: PIN-ROLE-D1 (RoleEq, autonomy-with-realization), D2
(SecondSubstance, ontological posit), D3 (CausalExemption, exemption
claim), D4 (OneObservedToken, counting evidence), D5
(CounterfactualFamilyObserved, variant family with outcomes), D6
(ReplicationRole, preserved counterfactual role), D7 (RetainsOrAdapts,
role-profile preservation in the extension — resolving PIN-CONS-OPEN-1,
conditional on PIN-SUB-v1's seal). Next checkpoint per the catalog order:
the T3 epistemic cluster (Pass, Possible, Artifact, Record, Deduction,
Prediction, Confirmed, CreativeGenerator, NoPossibleCritic, FinalOutput),
then DSF-v1 Section 13 item 6 bridge review.
