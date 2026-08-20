# H/J-Cluster Signature Freeze — Record v1

record_id: SIG-HJ-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: SIGNATURE_FREEZE_HJ_V1.md
plain_language_file: SIGNATURE_FREEZE_HJ_V1_PLAIN_LANGUAGE.md
digest_manifest: SIGNATURE_FREEZE_HJ_V1_FREEZE.json
parent_records: DSF-v1 (Section 3.4(1),(4),(5),(6), Section 13 item 4); SPA-v1 (Sections 3, 4.2, 6.1, unchanged); HKEY-v1; CAP-v1; SIG-EPI-v1
scope: complete displayed signatures for the H-fragment Boolean tables (FPartOf, FCarries, FBlindCopy, FErrorCorrect, FBuildWithResources), the population Eq table, and the interface key/label/Transport maps, implementing part of DSF-v1 Section 13 item 4
claims: freezes typed signatures and one definitional identification; classifies every addition; names affected cones; records a non-deciding argument
non_claims: does not edit SPA-v1 in place; does not interpret the tables beyond their signatures; does not supply cross-fragment carrier identifications (reserved for the identity record); does not test or discharge an original N-row; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4.
Check structures are record artifacts, not semantic additions.

## 1. Defects addressed

DSF-v1 3.4(4): FPartOf, FCarries, FBlindCopy, FErrorCorrect, and
FBuildWithResources are load-bearing primitive Boolean tables without
displayed signatures. 3.4(5): Eq has no displayed signature; its required
agreement with Eval is prose. 3.4(6): the domains/signatures of key, the
label map, and Transport are incomplete. 3.4(1)'s FDG_K carrier gap: HKEY-v1's tau supplies the code-to-task
embedding used by the key binding, but at the w.C_Sigma/FDG_K site the
carrier assignment was left unresolved there and is recorded in this
record as a named collision with a disclosed reading (Section 2); the
remaining carrier identifications are deferred to the identity record and
named below.

## 2. New carriers (classification: primitive data, finite carriers)

- Recipe: finite carrier of recipe tokens; a witness's w.r is an element.
  (SPA-v1 4.2 uses w.r in FPartOf(w.r,w.Vveh) and FCarries(w.r,w.p)
  without a named carrier.)
- EnvH: finite carrier of H-fragment environments; a witness's w.E is an
  element. Recorded distinctions, not identifications: EnvH is not the
  error family w.E-bold of FDG_K (DSF-v1 3.4(1)'s naming collision is
  noted: the witness record carries both w.E-bold the error/recovery
  family vector and w.E the environment), and EnvH is not identified with
  the J-fragment Environment carrier in this record.
- Label: finite carrier of display labels; the codomain of the label map.
- KeyRec: the dependent record carrier over Fld, i.e. total maps
  k: Fld -> coprod_f D_f with val(k,f) in D_f, as already displayed in
  SPA-v1 6.1; this record names the carrier so that key, the label map,
  and Transport can be typed against it.

Named collision (recorded, not resolved): HKEY-v1 reads the witness field
w.CSigma as an element of Code and applies tau: Code -> Task to it, while
SPA-v1 3.2/4.2 supplies w.C_Sigma as FDG_K's first argument, a position
that expects a K-task. Under HKEY-v1's reading the FRouteData conjunct is
well-typed only as FDG_K(tau(w.C_Sigma), w.Sigma, w.E-bold). This record
adopts that reading explicitly (a definition reading, disclosed): the
witness field w.C_Sigma is an element of Code, FDG_K receives its
implemented task via tau, and FErrorCorrect below is typed on Code,
matching what FRouteData actually supplies. The residual semantic
question — whether the error-correction claim should key on the code or
on its implemented task — is a real choice and is named as open item
SIG-HJ-OPEN-1 for the identity record; it is not decided here.

## 3. Completed signatures (classification: primitive data, typed tables)

From SPA-v1 4.2's FRouteData uses, with W the witness carrier, Vehicle,
CodeFamily, Word_Sigma the dependent word fibres, Code the H-fragment code
carrier (HKEY-v1), and the witness field w.C_Sigma read as Code per the
collision note in Section 2:

    FPartOf:            Recipe x Vehicle -> {0,1}
    FCarries:           Recipe x (coprod_{Sigma in CodeFamily} Word_Sigma) -> {0,1}
    FBlindCopy:         W x (coprod_{Sigma} Word_Sigma) x CodeFamily -> {0,1}
    FErrorCorrect:      W x Code x (coprod_{Sigma} Word_Sigma) x CodeFamily -> {0,1}
    FBuildWithResources: W x Vehicle x EnvH -> {0,1}

Fibre coherence (definition, not a new constraint): each table's displayed
use in FRouteData evaluates it only on the coherent fibre, i.e. with
w.p in Word_{w.Sigma}; this record makes that evaluation discipline
explicit. The anti-splicing exclusion itself is INHERITED from SPA-v1
4.2's pre-existing guard conjunct w.p in Word_{w.Sigma}; the signatures
here leave all five tables total on the full coproduct and exclude
nothing on their own.

Pre-existing tension recorded, not resolved: SPA-v1 Section 3 states every
task is a TOTAL function f_C: D_C -> Q, while Section 3.2's own proof
refers to "the one partial function f_{C_Sigma}". This record re-states
the totality side without choosing; the discrepancy is named as open item
SIG-HJ-OPEN-2 for the identity record.

## 4. Eq identification (classification: definition change)

SPA-v1 4.1 declares Eq as "a finite deterministic structural-equation
table" and requires in prose that its row compute exactly
Eval_lambda(nu,xi,delta). This record identifies them:

    Eq := Eval,  i.e. for all lambda, nu, xi, delta:
    Eq(lambda,nu,xi,delta) = Eval(lambda,nu,xi,delta),
    with type Lineage x Evt^3 -> P_fin(U x U).

The identification removes an uninterpreted primitive: Eval is already a
defined aggregate (the actual continuation aggregate), so Eq's content is
fully inherited. Classification: definition change in the prospective
fragment SIG-HJ-v1; the prose requirement becomes a definitional equality.

## 5. Key, label map, Transport (classification: primitive data and one acceptance axiom)

    key:     (Arrow_IR u Arrow_RE u Arrow_CE) -> KeyRec   (primitive data;
             total on each arrow type, as SPA-v1 6.1 already requires of
             each key(a))
    Label map ell: KeyRec -> Label   (primitive data; MAY be
             non-injective; no axiom constrains it, matching SPA-v1)
    Transport: a subset of KeyRec x KeyRec   (primitive data)

    SIG-HJ-A1 (transport preserves every field):
    for all k1, k2 in KeyRec, Transport(k1,k2) implies
    for all f in Fld, val(k1,f) = val(k2,f).
                                          (classification: acceptance axiom)
    Non-redundancy and parse choice: SPA-v1 6.1 says "a typed identity
    transport in Transport preserves every field value" as prose. That
    sentence admits a weaker parse (only transports that are identity
    transports preserve fields); A1 selects the STRONGER parse (every
    Transport pair preserves fields), and that selection is acknowledged
    here. A1 does not make Transport reflexive, symmetric, or
    transitive, and no such property is claimed; label equality is never
    identity (ell(k1)=ell(k2) implies nothing about k1,k2), matching
    SPA-v1.

## 6. Affected dependency cones

- Semantic families: D4 (H family; via FRouteData's tables), D3/D6 (via Eq
  in the population fragment), D10 (interface joins/alignment, via key,
  ell, Transport).
- DSF-v1 Section 11 items: H-03 (FImplements/FOutput/FError were already
  typed; FBlindCopy/FErrorCorrect were the untyped companions — the full
  H-03 group is named here), H-04, K-03 (FDG_K's task argument is now
  read via HKEY-v1's tau per the Section 2 collision note), J-02
  (key/label/transport schema), J-07 (the IC-SP-001/002 fixture
  obligations are consumers of the key/ell/Transport schema — naming them
  creates no run obligation; fixtures remain forbidden in this tranche),
  P-02's evaluation cluster (Eq/Eval).
- DSF-v1 acceptance items: DSF-A6 (one rigid frame and explicit identity
  transport) is the direct downstream consumer of SIG-HJ-A1 and is named
  here.
- Audit heads: Hsrc-hat through H-hat (cone membership), Veh/DG cones,
  Link-hat, PhysExp-hat (via Transport), Sel-hat/FallSel-hat (via Eq).
- Original N-rows (cones only): N4, N6 (H tables), N3, N7, N11, N16
  (interface maps), N5, N15, N19 (Eq).
- Explicitly unchanged: HKEY-v1's SysBind/tau machinery (no shared
  definition site; this record types tables HKEY-v1 does not touch);
  CAP-v1 and SIG-EPI-v1 (disjoint clusters); all bridges; DSF-F3.
- ADM-RECHECK-v1 and SIG-EPI-v1 witness structures: unaffected (no shared
  tables).

## 7. Non-deciding argument

Signature completions assign types, not values: no clause in Sections 2--5
constrains any entry of the five H-fragment Boolean tables or of ell and
Transport, so for each table both row values remain admissible; the
argument of SIG-EPI-v1 Section 7 applies row by row. For the Eq
identification: Eq is set equal to an already-defined aggregate, so the
change removes freedom rather than adding a constraint on values — any
structure of SPA-v1 extends uniquely to SIG-HJ-v1 by taking Eq := Eval,
and no formula's truth value changes thereby. For SIG-HJ-A1: A1 excludes
transports that change a field value, which SPA-v1's prose already
intended; non-deciding witness: any KeyRec pair with Transport empty
satisfies A1, and any pair with Transport(k1,k2) and k1=k2 (identity
record) also satisfies it, while FJOIN_IRRE/FLinked values are unaffected
because they never invoke Transport. Steering defense: rationale-based
only.

## 8. Forbidden items

No original N-row change; no fixture construction or run; no source bridge
claim; no in-place SPA-v1 edit; no cross-fragment carrier identification
(EnvH/Environment, the task carriers across K/H/J, and the DSF-v1 Section 10
list are all reserved for the identity record); no claim about creativity
in any real system.

## 9. Residual status and next checkpoint

The H-cluster tables, Eq, and the interface key/label/Transport maps are
now fully typed in the prospective fragment SIG-HJ-v1. Row readiness is
unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows untestable; zero
discharged. Next checkpoint: the cross-fragment identity record (DSF-v1
Section 10): common task carrier across K/H/J; H code families embedded
into K states; population boundary/environment tied to J; lineage tied to
H route; agent episode/package/trace tied to J (including the episode-to-E
identification deferred from SIG-EPI-v1); H witnesses tied to J
realization/program; J obligation frames tied to original T, Lambda,
Lambda'; rigid eta/theta/varpi across fragments; and the complete
Transport signature's interaction with those identities.
