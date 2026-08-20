# Semantic Pinning Record — ConservativeExtension / Boundary-Move Cluster v1

record_id: PIN-CONS-v1
version: 1.0
date: 2026-08-21
status: DRAFT_PENDING_REVIEW
official_file: PIN_CONS_V1.md
plain_language_file: PIN_CONS_V1_PLAIN_LANGUAGE.md
digest_manifest: PIN_CONS_V1_FREEZE.json
sha256_official: PIN_CONS_V1_FREEZE.json#official_sha256
sha256_plain_language: PIN_CONS_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md (frozen calculus); ORIGINAL_TERMS_INVENTORY.md (the term catalog, NOW PINNED in this repository at docs/ORIGINAL_TERMS_INVENTORY.md, pushed-bytes sha256 fe4e1f9a8c08a5179d45b1167ca23437085213695ba77d85a53e0a26e8c575bb, recorded in the manifest parent_records); PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, pinned per ERR-SPA-v1 to the committed bytes a9f62ebb..., the defective pin 40681e6c... retired); SPA_PIN_ERRATUM_V1.md (ERR-SPA-v1, governing re-binding erratum); DOWNSTREAM_SEMANTIC_FREEZE_V1.md (DSF-v1); IDENTITY_FREEZE_V1.md (IDF-v1, current format template); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: original-side semantic pins for the ConservativeExtension / boundary-move cluster of DSF-v1 Section 13 item 5 — the terms ConservativeExtension, SameObservableLabel, MovedConstructorPort, the BoundaryMove complex of calculus (63), and the N20-side items FiniteVariantSuite (definitional reading), RetainsOrAdapts (left OPEN), and EverettianUniversalClaim (negative guard-rail pin; positive semantics left OPEN)
claims: freezes named, classified candidate finite meanings (PIN-CONS-D1..D3, D5, plus the declared primitive datum PIN-CONS-D2a) and two acceptance axioms (PIN-CONS-A1 no-splicing; PIN-CONS-A2 Everettian negative guard-rail) for the boundary-move leaves; records two named OPEN items (PIN-CONS-OPEN-1, PIN-CONS-OPEN-2) where a pin would require a source-level bridge not yet justified; records per-decision and cluster non-deciding arguments; names affected dependency cones without changing any readiness count
non_claims: does not test, discharge, or change any original N-row; does not move any readiness count (PINNED=0, PARTIAL=2, OPEN=18 stand); does not construct or run a fixture; does not add a row bridge or a total expansion (D0/DSF-A1 remain OPEN with zero accepted expansions and zero row bridges); does not edit the frozen calculus, SPA-v1, or any sealed record; does not claim any source-level bridge; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4
(definition, acceptance axiom, import, bridge). This record uses only the
definition and acceptance-axiom buckets. All pins are ORIGINAL-SIDE
candidate meanings for uninterpreted leaves of the frozen calculus; none is
a fragment predicate, and none identifies an original predicate with an
F-prefixed fragment predicate. Label equality is never identity.

## 1. Scope and method

DSF-v1 Section 13 item 5 directs the next tranche to "pin remaining open
original terms". The prepared catalog (ORIGINAL_TERMS_INVENTORY.md, cluster
T5, with the T5a/T5a-lite split it authorizes — now pinned in this
repository and digest-pinned in the manifest, so catalog citations in this
record are against fixed bytes) assigns this first record
the ConservativeExtension / boundary-move cluster: the terms
ConservativeExtension, SameObservableLabel, MovedConstructorPort, and the
BoundaryMove complex anchored at calculus (63), feeding N-rows N7
(NE_BOUNDARY_IS_EVIDENCE) and N20 (NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS).
ConservativeExtension additionally gates every M'-class row via the D0
family and the acceptance gate DSF-A1; Section 9 states that gating
carefully.

These terms are uninterpreted original-side leaves. This record PINS
candidate finite meanings; it proves nothing. Where a term admits
materially different pinnings, the options are stated, one is selected with
a structural rationale, and the selection is recorded as load-bearing with
steering defense RATIONALE_BASED_ONLY. Where a pin would require a bridge
to source-level semantics that this tranche cannot justify, the item is
recorded as a named OPEN item instead of being pinned.

Method rule: each pin is the WEAKEST meaning that (i) makes the frozen
occurrences well-typed and (ii) keeps each conjunct of the frozen
abbreviations in (63) an independent condition. Rejected alternatives are
recorded with the structural reason for rejection.

## 2. Exact anchors

Calculus (3), the frozen identification discipline (quoted verbatim):

> "Within a θ-indexed formula, an un-subscripted symbol is an abbreviation
> for its θ-projection. No formula may identify parts of θ and θ′ without
> a named equality, port, or conservative-extension relation."

Calculus (46), the whole-agent definitions (quoted verbatim; included for
the D11 family boundary of this cluster; no pin is made here):

> "WholeClone_B(A) ⟺ a declared task clones the complete bounded state of
> A,  WholeDigital_B(A) ⟺ every declared state variable of the complete
> bounded state of A is a digital code variable."

Calculus (63), the N-only abbreviations, heading and the two conjuncts
load-bearing for this record (quoted verbatim):

> "For a conservative extension (η′,θ′) define the closed abbreviations
>
> BoundaryMove_{η,θ}^{η′,θ′} ⟺ B′≠B ∧
>   SameObservableLabel_{η,η′}(θ,θ′) ∧ MovedConstructorPort_{η,η′}(θ,θ′),
> FiniteTheorySuite_{η,θ}(L) ⟺ L ⊆ Theory_η ∧ |L|<∞,
> FiniteVariantSuite_{η,θ}(U) ⟺ U ⊆ V_θ × E_η ∧ |U|<∞, ..."

N7 row (NE_BOUNDARY_IS_EVIDENCE), quoted verbatim:

> "M′ ⊨ Linked_{η,θ} ∧ BoundaryMove_{η,θ}^{η′,θ′} ∧
> ¬Linked_{η′,θ′}"

N20 row (NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS), quoted verbatim:

> "M′ ⊨ ConservativeExtension_{η,θ}^{η′,θ′} ∧
> FiniteVariantSuite_{η,θ}(U) ∧ ∃(ν*,E*)[(ν*,E*) ∈
> (V_{θ′}×E_{η′})∖U ∧ ¬RetainsOrAdapts_{η′,θ′}(ν*,E*)] ∧
> ¬EverettianUniversalClaim_{η′,θ′}(U)"

Port anchors for MovedConstructorPort: calculus (2)/(3) declare
"P_Σ : the declared program port, distinct from ℙ_Σ"; the dictionary (12)
gives "PORT ⟺ ProgramOf(P_Σ)=(r,p_code,S_Σ) ∧ Uses(R,P_Σ)=(b,k)"; PEALIGN
(42) repeats "ProgramOf(P_Σ)=(r,p_code,S_Σ) ∧ Uses(R,P_Σ)=(b,k)".

DSF-v1 anchors: Section 6 family D12 — "BoundaryMove (63),
ConservativeExtension — none — N7,N20 — OPEN"; family D21 —
"FiniteVariantSuite (63), RetainsOrAdapts, EverettianUniversalClaim —
none — N20 — OPEN"; Section 12 — "BoundaryMove uses SameObservableLabel
and MovedConstructorPort; ... FiniteVariantSuite fixes finiteness, not
extension/adaptation"; ConservativeExtension, SameObservableLabel,
MovedConstructorPort, RetainsOrAdapts, and EverettianUniversalClaim are all
on the Section 12 uninterpreted-leaf list. DSF-A1 (Section 2.4) is the
total-expansion gate: "Expand_SPA-v1(Mflat,Mhat) and Mhat satisfies
T_eta,theta,varpi and RowBridge_j(Mflat,Mhat)".

Fragment pin candidates (SPA-v1), referenced only as candidates and
mismatches, per the catalog: the J-02 key/label schema (the label map ℓ,
"may be non-injective", and FKeyMatch field equality, SPA-v1 6.1) for
SameObservableLabel; PORT/ProgramOf(P_Σ) data at the fragment level for
MovedConstructorPort. No fragment predicate exists for
ConservativeExtension, RetainsOrAdapts, or EverettianUniversalClaim; the
mismatches (intra-context key matching vs cross-(η,θ) agreement; port
bound within one fixed θ vs tracked across B→B′) are recorded in the
catalog and confirmed against SPA-v1 6.1 text.

## 3. PIN-CONS-D1: ConservativeExtension (definition; LOAD-BEARING)

The term occurs at (3) ("conservative-extension relation"), at the (63)
heading ("for a conservative extension (η′,θ′)"), in the N20 row
antecedent, and implicitly in every M'-class row (N7's M′ is quantified
over the conservative-extension class per Section 6 of the calculus: "the
fixed or conservative extension class").

Options stated:

- CE-strong (SELECTED): (η′,θ′) is a conservative extension of (η,θ) in
  the logical sense, specialized to this typed setting: every carrier and
  constant of θ is embedded into the corresponding carrier of θ′ by
  declared typed embeddings ι (named per context pair, satisfying calculus
  (3)'s named-relation discipline), and for every formula φ in the OLD
  language of (η,θ) — the vocabulary of Table 1.1 and (12)–(13) over
  θ-projections — M ⊨ φ at (η,θ) iff M′ ⊨ ι(φ) at (η′,θ′). No new
  old-language truths arise in the extension; old-language falsehoods are
  likewise preserved. New vocabulary (θ′-projections with no
  θ-counterpart, e.g. Linked_{η′,θ′}, V_{θ′}, E_{η′}) is unconstrained by
  the relation.
- CE-weak (REJECTED): only a designated finite list of "observable"
  predicates is preserved. Rejected: it makes SameObservableLabel in (63)
  redundant — the label conjunct would collapse into the extension
  relation, destroying the independence of the BoundaryMove conjuncts —
  and, depending on the list, either manufactures the N7 witness
  condition trivially (list empty) or destroys it (list contains the
  Linked ingredients).
- CE-elementary (REJECTED): full elementary extension (all parameters,
  all formulas of the expanded language). Rejected as over-strong: it
  would force new-context formulas to mirror old ones, which is exactly
  what N7's denial limb ¬Linked_{η′,θ′} must remain free to violate; no
  frozen occurrence requires elementarity.

Selection: CE-strong. Structural rationale: the standard notion of
conservative extension is proof-theoretic — an extension is conservative
if it proves no new theorems in the old language. The pin here is the
model-level analogue of that notion, stated accurately as such: truth
preservation of old-language formulas under the named embeddings
(M ⊨ φ at (η,θ) iff M′ ⊨ ι(φ) at (η′,θ′)), not the proof-theoretic
statement itself, because this record pins semantics for structures, not
a proof system. It is the weakest option under which all three
BoundaryMove conjuncts remain mutually independent conditions; and it
leaves every new-context predicate free, which is what both M'-class rows
require. Recorded as LOAD-BEARING: the choice changes which structures
can serve as M′ in N7 and N20.

Non-deciding two-structure argument (the required concrete argument for
the most load-bearing pin). Fix (η,θ,ϖ) with Linked_{η,θ} true, and an
extension (η′,θ′,ϖ′) with B′≠B, declared embeddings ι, label agreement
on all embedded fields, and the port program triple preserved (the D2/D3
pins below). Consider two structures:

- S1: at θ′ the IR/RE/CE arrows exist but CommonScope at the new boundary
  B′ fails, so JOIN_IRRE fails and Linked_{η′,θ′} is FALSE.
- S2: identical except the θ′ arrows satisfy every join condition at B′,
  so Linked_{η′,θ′} is TRUE.

Both structures satisfy CE-strong: Linked_{η,θ} is an old-language
formula and holds in both at (η,θ); conservativity constrains only
old-language formulas, and Linked_{η′,θ′} is new-context vocabulary,
unconstrained either way. Every other conjunct of the N7 antecedent is
held fixed across S1 and S2. Therefore PIN-CONS-D1 decides neither the
N7 denial limb nor its negation; the pin is non-deciding for the row it
gates. The same pair, read with FiniteVariantSuite data added, shows D1
decides neither the existence nor the non-existence of an outside-suite
failing pair in N20.

## 4. PIN-CONS-D2: SameObservableLabel (definition; load-bearing, weaker risk)

Anchor: the middle conjunct of BoundaryMove in (63). The catalog warns:
over-weak pinning (pure string equality) manufactures the N7 countermodel
trivially; over-strong (full task identity) destroys it.

PIN-CONS-D2a (primitive data declaration; definition bucket): the pin
below presupposes an "observable label" datum on θ-components, and no
such datum exists anywhere in the frozen calculus vocabulary. Following
the IDF-v1 precedent (IDENT-D6e/D7a), this record therefore DECLARES that
datum explicitly as new primitive data rather than smuggling it in: for
each context θ there is an observable-label map ObsLabel_θ assigning to
each θ-component its declared observable label (a display-level tag, not
an identifier), and under an extension (η′,θ′) with embeddings ι the
θ′-side map ObsLabel_θ′ is part of the declared extension data.
Classification: primitive data, definition bucket — it is newly declared
here, and PIN-CONS-D2 depends on it explicitly. Declaring it adds no
constraint on any table entry or row antecedent; it only names data the
label conjunct needs in order to be well-typed.

Options stated:

- SOL-label-under-embedding (SELECTED): SameObservableLabel_{η,η′}(θ,θ′)
  holds iff for every θ-component with a declared observable label (per
  the primitive data PIN-CONS-D2a declared above), the label of the
  component equals the label of its ι-image in θ′, where
  "label" is the display-label reading (fragment analogue: the SPA-v1 6.1
  label map ℓ, which "may be non-injective"). This is a LABEL-LEVEL
  predicate. Per DSF-v1 Section 10 and SPA-v1 6.1, label equality is
  never identity: SOL-label-under-embedding does not identify any
  θ-component with any θ′-component; identification across contexts
  remains forbidden except through the named relation PIN-CONS-D1.
- SOL-identity (REJECTED): label agreement read as component/task
  identity. Rejected as over-strong and as a violation of calculus (3):
  it would identify parts of θ and θ′ without a named equality, and it
  would make BoundaryMove imply Linked_{η′,θ′}-preservation pressure that
  the N7 denial limb exists to deny — destroying the row by construction.
- SOL-free-string (REJECTED): raw string equality of display texts with
  no embedding discipline. Rejected as under-disciplined: with no tie to
  ι, any pair of contexts can be given matching strings, manufacturing
  the BoundaryMove antecedent for free (the catalog's trivial-manufacture
  hazard).

Selection: SOL-label-under-embedding. It keeps the conjunct independent
of both B′≠B and MovedConstructorPort, it matches the fragment label
machinery (J-02/ℓ/FKeyMatch) as a candidate reading without identifying
the original with any fragment predicate, and it is the weakest option
that respects calculus (3). Load-bearing, recorded.

## 5. PIN-CONS-D3: MovedConstructorPort (definition; LOAD-BEARING)

Anchor: the third conjunct of BoundaryMove in (63). The port vocabulary is
the declared program port P_Σ of (2)/(3), with ProgramOf(P_Σ) =
(r,p_code,S_Σ) in PORT (12) and PEALIGN (42). The catalog flags this as
the load-bearing limb of N7: pinning it as vacuous collapses the row.

Options stated:

- MCP-program-preserved (SELECTED): MovedConstructorPort_{η,η′}(θ,θ′)
  holds iff the declared constructor port of θ is tracked into θ′ through
  the named extension relation of PIN-CONS-D1: the ι-image of P_Σ is the
  declared program port of θ′, and the program triple is preserved —
  ProgramOf(ι(P_Σ)) = (ι(r), ι(p_code), ι(S_Σ)) — while the boundary
  coordinate changes from B to B′. The predicate is about the PORT MOVING
  across the boundary with its program intact; it asserts no preservation
  of the knowledge-bearing use (Uses(R,P_Σ)=(b,k)) into the new context,
  which remains a separate, deniable condition.
- MCP-vacuous (REJECTED): the conjunct is always true. Rejected: it
  collapses BoundaryMove to B′≠B ∧ SameObservableLabel, deleting the
  port limb of N7 — the exact collapse the catalog warns against.
- MCP-use-preserved (REJECTED): the port moves AND its (b,k)-use is
  preserved into θ′. Rejected as over-strong, but with the rejection
  stated honestly: the rejection survives on the weakest-reading rule
  alone (Section 1 method rule: pick the weakest meaning that keeps the
  conjuncts well-typed and independent, and use-preservation is a
  strictly stronger reading than program-preservation). The stronger
  mechanism one might cite — that preserved Uses would formally pre-decide
  N7 — is UNPROVEN here: the N7 row invokes Linked, and Linked does not
  invoke Uses/PORT, so no formal channel from use-preservation to the
  denial limb ¬Linked_{η′,θ′} has been exhibited. The pressure is
  intuitive, not derivational; this record does not claim it.

Selection: MCP-program-preserved. Rationale: it is the weakest reading
under which the conjunct is non-vacuous yet independent of the N7 denial
limb; it uses only vocabulary already declared in (2)/(3)/(12)/(42); and
the mismatch with the fragment (PORT binds a program port within one
fixed θ; no fragment tracks a port across contexts) is honestly recorded —
this is an ORIGINAL-side pin with no fragment counterpart, not an
identification. Load-bearing, recorded.

## 6. The BoundaryMove complex and the no-splicing condition

BoundaryMove_{η,θ}^{η′,θ′} itself is a frozen DEFINITION (63), not a
leaf; this record makes no new decision about it. Under D1–D3 its three
conjuncts are mutually independent: B′≠B (boundary inequality),
SOL-label-under-embedding (label-level agreement under ι), and
MCP-program-preserved (port program preserved across the move).

PIN-CONS-A1 (acceptance axiom, no-splicing): in any structure and any
certificate invoking BoundaryMove_{η,θ}^{η′,θ′} or
ConservativeExtension_{η,θ}^{η′,θ′}, the embeddings ι, the label
comparisons, and the port tracking are ONE named package of data per
context pair: the same ι witnesses the conservativity conjunct, the label
conjunct, and the port conjunct. Mixing witnesses between conjuncts (one
embedding for conservativity, another for the port) is excluded. This
restates calculus (3)'s named-relation discipline as a numbered axiom for
the extension context, parallel to DSF-v1 Section 10's no-splicing freeze
and IDF-v1's IDENT-A2 rigidity. Non-deciding per conjunct by the Section 3
two-structure argument, which uses one fixed ι throughout: A1 excludes
only cross-conjunct witness mixing, and no frozen predicate's truth value
depends on such mixing.

## 7. N20-side items

FiniteVariantSuite (PIN-CONS-D5; definition reading, disclosed, no new
constraint): (63) already defines FiniteVariantSuite_{η,θ}(U) ⟺
U ⊆ V_θ × E_η ∧ |U|<∞. DSF-v1 Section 12 records that it "fixes
finiteness, not extension/adaptation". This record adopts that reading
verbatim: the abbreviation is pinned as fixing ONLY finiteness and suite
membership; it says nothing about which (ν,E) pairs retain or adapt. No
new constraint is added; classified as a disclosed definition reading,
parallel to IDF-v1's IDENT-D10.

PIN-CONS-OPEN-1 — RetainsOrAdapts (LEFT OPEN): the N20 existential denial
∃(ν*,E*) ∈ (V_{θ′}×E_{η′})∖U ∧ ¬RetainsOrAdapts_{η′,θ′}(ν*,E*) lives or
dies on this predicate's extension behavior (catalog: steering-sensitive,
rank 6). A pin requires the FOR_REPLICATOR_NICHE source-grade constraint
(replication/adaptation as contextual counterfactual roles), which is a
B/D-grade bridge to source-level semantics this tranche cannot yet
justify; the only fragment candidate (FSel/lineage predicates,
P-02/P-03/P-05) is an intra-context selection proxy, not a
cross-environment variant-to-environment claim. Pinning it as
"finite-suite success extends" would destroy N20; pinning it as "always
fails outside U" would manufacture N20. Recorded OPEN and assigned to the
next T5-cluster record, after the D1 extension relation is sealed.

PIN-CONS-OPEN-2 — EverettianUniversalClaim (negative guard-rail PINNED;
positive semantics LEFT OPEN). PIN-CONS-A2 (ACCEPTANCE AXIOM, negative
constraint only — reclassified from the definition bucket, since it
constrains admissible derivations rather than giving the term a
meaning): EverettianUniversalClaim_{η′,θ′}(U) is never
established by any data finite over U; in particular no finite variant
suite U and no finite audit over (η′,θ′) entails it. This pins the
guard-rail direction the source register requires ("The Everettian
explanatory discussion does not turn other universes into observed data
or make a finite cohort exhaustive") and keeps the N20 denial limb
¬EverettianUniversalClaim_{η′,θ′}(U) available in every finite
countermodel. The POSITIVE semantics of the claim (what would establish
it) is left OPEN as PIN-CONS-OPEN-2: a positive pin is not needed for any
frozen row (the term occurs only negated) and an accidental positive pin
is the catalog's stated hazard for this term. Non-deciding: the negative
constraint only forbids a derivation nobody performs; it constrains no
table entry and no row antecedent.

## 8. What this record deliberately does NOT pin

Per the catalog's T5 split, the remaining T5 terms — SameSyntax,
RealizationEq, RoleEq, SecondSubstance, CausalExemption, OneObservedToken,
CounterfactualFamilyObserved, ReplicationRole — are NOT covered here.
RealizationEq and SameSyntax (the N18 pair, "DO NOT TEST OR REPAIR") must
be pinned jointly in one later record; this deferral is recorded in the
manifest crosswalk (PIN-CONS-N18-DEFERRAL). RetainsOrAdapts's positive pin
(PIN-CONS-OPEN-1) belongs with them or in an N20-focused successor record.
Transparency note: the format-template parent IDF-v1 is currently
REVIEWED_PENDING_OWNER_SEAL (reviewed, not yet owner-sealed); this record
follows its format without claiming its seal status.
Calculus (46) (WholeClone/WholeDigital, family D11, N6) is quoted in
Section 2 for boundary completeness only; it is outside this cluster and
nothing is pinned about it.

## 9. The D0/A1 gating statement (careful form)

ConservativeExtension is the connective tissue of every M'-class row. The
precise statement this record freezes:

1. N7 and N20 are the only rows whose displayed formulas NAME the
   conservative-extension relation ((63) heading for N7; the explicit
   ConservativeExtension conjunct in N20). For those rows, PIN-CONS-D1
   supplies the original-side reading of that relation.
2. Structurally, ALL twenty rows sit under the D0 family via DSF-A1: a
   row certificate requires Expand_SPA-v1(Mflat,Mhat) ∧ Mhat ⊨ T ∧
   RowBridge_j(Mflat,Mhat). DSF-v1 records ZERO accepted total expansions
   and ZERO original-row bridges. PIN-CONS-D1 does not change that: it is
   not an expansion, not a bridge, and not an existence axiom. It
   constrains WHICH structures may serve as the M′ of a future N7/N20
   countermodel; it neither supplies such a structure nor forbids one.
3. Because D1 scales across rows, its over/under-permissiveness hazards
   scale too (catalog rank 9). The CE-strong selection plus the Section 3
   two-structure argument is this record's evidence that the chosen pin
   is non-deciding for the rows it gates. No readiness count moves: N7
   and N20 remain OPEN, REGISTERED_SCHEMA [N], DO NOT TEST.

## 10. Cluster non-deciding summary and steering defense

Cluster (D1, D2, D2a, D3, D5, A1, A2): D1 non-deciding by the exhibited S1/S2 pair
(Section 3). D2 is a label-level predicate: flipping a display label on a
non-embedded θ′-component flips SameObservableLabel while every embedded
field, every table entry, and every other conjunct is unchanged — two
structures, both satisfying D1/D3/A1, one with the conjunct true and one
false. D3: preserving or varying the θ′-uses table (whether any R′ with
Uses(R′,ι(P_Σ))=(ι(b),ι(k)) exists) flips nothing in D3 itself — the pin
is about the program triple only — while the N7 denial limb varies
freely, as S1/S2 already show. D5 adds no constraint. A1 excludes only
cross-conjunct witness mixing (Section 6). A2 (the Everettian negative
guard-rail) forbids a derivation nobody performs and constrains no table
entry.

Steering defense: RATIONALE_BASED_ONLY, per the HKEY-v1/IDF-v1
convention. The selections (CE-strong over CE-weak/CE-elementary;
SOL-label-under-embedding over identity or free-string readings;
MCP-program-preserved over vacuous or use-preserved readings; refusal of
the RetainsOrAdapts and Everettian-positive pins) rest on the documented
structural objections in Sections 3–7 (conjunct independence, calculus
(3) discipline, row non-pre-decision, source-bridge scope). No
comparative non-deciding checks were run for rejected alternatives; none
is claimed.

## 11. Affected dependency cones (no readiness change)

- Semantic families (DSF-v1 Section 6): D12 (BoundaryMove,
  ConservativeExtension — leaves now pinned original-side; family status
  NOT reclassified), D21 (FiniteVariantSuite reading disclosed;
  RetainsOrAdapts OPEN; EverettianUniversalClaim guard-railed). D0
  unchanged (OPEN). D11 quoted only.
- N-rows (cones only, rows untouched): N7, N20 directly; all rows via the
  D0/A1 statement of Section 9. Row readiness unchanged: PINNED=0,
  PARTIAL=2, OPEN=18; all 20 rows untestable; zero discharged; testing
  remains PROHIBITED.
- Explicitly unchanged: the frozen calculus; SPA-v1 (pinned per
  ERR-SPA-v1 to a9f62ebb...); DSF-v1; IDF-v1 and its SPA-IDENT-v1
  fragment; all four project bridges (grade B, unclaimed); ADM-v1 counts
  (B1=0, B2=0, B3=3); IC-SP-001/002 (unrun; no run obligation created).

## 12. Forbidden items

No original N-row change; no fixture construction or run; no total
expansion or row bridge; no source bridge claim (RetainsOrAdapts's
required FOR_REPLICATOR_NICHE constraint is recorded as OPEN rather than
imported); no in-place edit of the calculus, SPA-v1, or any sealed
record; no semantic choice justified by a desired separation outcome; no
readiness-count movement; no claim about creativity or non-creativity in
any real system.

## 13. Residual status and next checkpoint

Frozen decisions: PIN-CONS-D1 (ConservativeExtension, CE-strong),
PIN-CONS-D2 (SameObservableLabel, label-under-embedding), PIN-CONS-D3
(MovedConstructorPort, program-preserved), PIN-CONS-D2a
(observable-label map, declared primitive data), PIN-CONS-D5
(FiniteVariantSuite, disclosed definition reading); acceptance axioms
PIN-CONS-A1 (extension no-splicing) and PIN-CONS-A2
(EverettianUniversalClaim, negative guard-rail). Left open: PIN-CONS-OPEN-1
(RetainsOrAdapts), PIN-CONS-OPEN-2 (EverettianUniversalClaim positive
semantics). All selections carry steering defense RATIONALE_BASED_ONLY.
Readiness: PINNED=0, PARTIAL=2, OPEN=18; rows discharged: 0; testing:
PROHIBITED. Next checkpoint per DSF-v1 Section 13 item 5 and the catalog's
tranche order: the remaining T5 records (RealizationEq/SameSyntax
jointly; the N17/N19 leaves; RetainsOrAdapts with its source-grade
constraint), then item 6 bridge review.
