# Downstream Semantic Freeze v1

record_id: DSF-v1
version: 1.0
date: 2026-08-20
status: SEALED_DEPENDENCY_INVENTORY_TESTING_PROHIBITED
official_file: DOWNSTREAM_SEMANTIC_FREEZE_V1.md
plain_language_file: DOWNSTREAM_SEMANTIC_FREEZE_V1_PLAIN_LANGUAGE.md
digest_manifest: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json
sha256_official: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json#official_sha256
sha256_plain_language: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1); ADMISSIBILITY_GATE_AUDIT_V1.md (ADM-v1); TRANCHE_HANDOFF_V1.md (TH-v1); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: complete dependency inventory for all 25 unary audit heads, the binary information head, eight report projections, and all 20 original N-rows
claims: freezes the current typed dependencies and pinning status; records newly discovered semantic defects; prohibits original-row testing while any transitive cone is PARTIAL or OPEN
non_claims: does not repair a definition, add a row bridge, construct a fixture, discharge an N-row, validate an imported principle or project bridge, or prove creativity or non-creativity

## 1. Freeze result

This record implements Tranche 2 of TH-v1. It inventories every downstream
semantic dependency before any new fixture or original-row test is built. It
changes no formula in the frozen calculus or SPA-v1.

The status words are mutually exclusive and are assigned in this order:

1. PINNED: every load-bearing term in the whole transitive cone has a fixed,
   well-typed interpretation in the named class, including every required
   identity across domains.
2. PARTIAL: the item is not PINNED and a frozen parent record explicitly
   associates a target-specific operational counterpart with that exact
   inventory item. For an N-row this requires a preregistration or fixture for
   that exact row; a generic fragment for one subformula is not enough. For a
   head or semantic family, the item-specific mapping in Sections 6--7 is the
   applicable direct-coverage rule.
3. OPEN: neither condition above holds.

Ill-typed formulae, uninterpreted primitives, absent total expansions,
missing identity conditions, and missing row bridges are recorded separately
as blocking-defect flags. Any such flag prohibits testing. It does not by
itself choose PARTIAL rather than OPEN; that distinction is determined by the
target-specific registration rule above.

An exact Horn support is not a semantic pin. An F-prefixed finite predicate is
not an original predicate. A definition in terms of free primitives does not
pin those primitives. An imported principle or bridge keeps its stated grade.

| Inventory | PINNED | PARTIAL | OPEN | Test-ready |
|---|---:|---:|---:|---:|
| 25 unary audit-head transitive cones | 0 | 12 | 13 | 0 |
| binary information-product head | 0 | 0 | 1 | 0 |
| 20 original non-entailment rows | 0 | 2 | 18 | 0 |

No original audit-head semantic test and no original N-row test may begin
under DSF-v1. The finite closure and report functions remain exactly
calculable; that is different from semantic readiness.

## 2. Normative layers and model classes

### 2.1 Audit layer

For a signed provision state v, the audit layer is the finite closure
F_eta,theta(v;varpi) of calculus (51)--(53), with supports (56), the exact
route theorem (57), and reports (60)--(62a). This is PINNED as a finite
syntactic calculation.

The exact formulas are incorporated by digest-bound reference:

1. all 44 certificate meanings: calculus Table 1.1 and (4)--(5);
2. auxiliary and applicability meanings: calculus (12)--(13);
3. head denotations: calculus (54);
4. signed states and rules: calculus (49)--(53); and
5. reports and priorities: calculus (60)--(62a).

The DSF-v1 manifest fixes the parent bytes, so these references are normative.

### 2.2 Original semantic layer — Definition DSF-D1

The original class is exactly:

    M_eta,theta,varpi =
      { M : M is sort-correct and M satisfies T_eta,theta,varpi }.

T is the theory listed in calculus (54b). This class supports conditional
closure soundness but does not operationally interpret every primitive.

### 2.3 Finite-fragment layer — Definition DSF-D2

SPA-v1 intends the finite class:

    C_SPA-v1 =
      { Mflat = (K,P,H,A,J,eta,theta,varpi)
        satisfying SPA-v1 Sections 3--6 }.

Its F-prefixed terms are fragment predicates, not original predicates.
Section 3 shows that the present clauses do not yet define one fully
well-typed class.

### 2.4 Total expansion — Acceptance Axiom DSF-A1

An original-row certificate must satisfy all three conditions in one model:

    Expand_SPA-v1(Mflat,Mhat)
    and Mhat satisfies T_eta,theta,varpi
    and RowBridge_j(Mflat,Mhat).

This is a structural certificate gate, not an existence axiom. DSF-v1 records
zero accepted total expansions and zero original-row bridges. A separate
two-sided construction remains necessary for each row.

## 3. Newly discovered blockers

### 3.1 Capacity update is ill-typed — Finding DSF-F1

SPA-v1 declares:

    Update:
      Assessment x Policy x Selector x State -> {0,1}.

A policy context instead contains whole finite tables:

    pi: reachable states -> Policy
    q:  reachable states -> Selector.

Two capacity clauses call:

    Update(x, pi_mu, q_mu, s'').

They pass whole functions where the declared operation requires one policy and
one selector. Therefore FCanSustainConsequentialAppraisal,
FCanDrawOnOwnedEvaluatedTarget, FCreativeCap, and the positive structure used
in ADM-T1 are not well-typed under SPA-v1.

DSF-v1 chooses no repair. It records:

1. capacity status OPEN_UPDATE_TYPE;
2. ADM-T1 is not an established SPA-v1 independence theorem;
3. ADM-U3 cannot currently remain B2;
4. the current admissibility count is B1=0, B2=0, B3=3; and
5. ADM-v1 remains frozen as history, while DSF-v1 supersedes its
   present-tense B2/readiness claim.

All twenty original rows remain REGISTERED_SCHEMA [N]. The five original rows
that depend on CreativeCap all remain blocked by OPEN capacity semantics.

### 3.2 H-route key is not bound to the checked system/task — Finding DSF-F2

SPA-v1 fixes hkey(w)=(F,T,R), then checks w.Vveh and w.CSigma. No typed
condition connects named system F to actual vehicle w.Vveh, or named task T
to the task implemented by w.CSigma. The required relation might be identity,
containment, or implementation; this record deliberately does not select one.

The allowed-error threshold epsilon_{*,R} is compared with rational error
values but has no declared carrier or type.

FPT-HRoute is therefore PARTIAL_KEY_AND_THRESHOLD_TYPING.
NE_SELECTION_NOT_HIGH_FIDELITY remains PARTIAL and untestable.

### 3.3 Original admissibility is free — Finding DSF-F3

Original Admissible_eta(A,mu) occurs in CAP_JOIN and CreativeCap. It has no
definition, import, or bridge to FAdmissible. It remains
OPEN_ADMISSIBILITY_B3 independently of DSF-F1.

### 3.4 Other confirmed type and grounding gaps

1. FDG_K expects a task in the task-graph carrier and code/error subsets of
   its state carrier. FRouteData supplies w.CSigma, w.Sigma, and the recovery
   or error-family vector w.bold-E without displayed embeddings into those
   carriers. The distinct singular w.E is the environment used by
   FBuildWithResources.
2. FError(FOutput(c,w),w.p) is defined only when output and word share one
   code-family tag. SPA-v1 states this in prose, not a numbered class axiom.
3. Kind, Pkg, Evid, FDerives, FInterprets, OutcomeSpace, FSuitable,
   FIncompatible and NonSeed lack complete displayed signatures. No episode
   carrier identifies an agent episode record with interface carrier E.
4. FPartOf, FCarries, FBlindCopy, FErrorCorrect and FBuildWithResources are
   load-bearing primitive Boolean tables without displayed signatures.
5. Eq has no displayed signature; its required agreement with Eval is prose.
6. The domains/signatures of key, the label map and Transport are incomplete.
7. Select(q,s,s') is not required to return an edge with source s and target
   s'; agent transitions are not required to increase Time_A.

### 3.5 Automatic or redundant gates

These clauses cannot currently supply independent semantic pressure:

- FAdmissible's range condition follows from q's codomain, leaving reachability;
- FCommonConstraint's Boolean-codomain clause follows from viable's type;
- FCandidateTriple follows from already-typed arrow variables;
- Cells_Sigma(p) subset Sigma follows from Cells' codomain;
- FExternalEveryTarget=0 is intended to follow from the preceding owned
  selected edge when agents are distinct from external, but its Boolean
  codomain/signature is not declared, so this redundancy is not yet formal;
  and
- the local key-mismatch theorem follows because FJOIN_IRRE contains FKeyMatch.

They may remain audit checks, but no necessity or independence is claimed.

## 4. Numbered project semantic items

### 4.1 Definitions

| ID | Exact anchor/content | Consumers | Affected N-rows | Status |
|---|---|---|---|---|
| DSF-D1 | original thin class; calculus (54b) | all heads/rows | N1--N20 | PINNED as class definition; semantically thin |
| DSF-D2 | SPA fragment class; SPA Sections 3--6 | finite fixtures | N1,N2,N3,N4,N5,N6,N7,N9,N10,N11,N12,N13,N14,N15,N16,N19 | PARTIAL |
| DSF-D3 | signed states, closure, supports; calculus (49)--(57) | all 25 unary heads | N1--N7,N9--N16,N18,N19 | PINNED syntactically |
| DSF-D4 | report functions; calculus (60)--(62a) | displays | none directly | PINNED syntactically |
| DSF-D5 | task/intervention fragment; SPA Section 3 | FDG, future retention | N1,N3,N4,N6,N10,N11,N12,N16,N19 | PARTIAL overall |
| DSF-D6 | population/FSel fragment; SPA 4.1 | selection rows | N4,N5,N15,N19 | PARTIAL |
| DSF-D7 | replication-route proxy; SPA 4.2 | selection/H row | N4,N6 | PARTIAL_KEY_AND_THRESHOLD_TYPING |
| DSF-D8 | episode/FEpi fragment; SPA 5.1 | episode rows | N3,N5,N9,N11,N13,N14,N15,N16 | PARTIAL |
| DSF-D9 | capacity fragment; SPA 5.2 | capacity rows | N2,N3,N6,N9,N11 | OPEN_UPDATE_TYPE |
| DSF-D10 | interface composition; SPA 6 | link/alignment | N3,N7,N11,N16 | PARTIAL |
| DSF-D11 | N-only abbreviations; calculus (46),(63) | rows 6--8,18--20 | N6,N7,N8,N18,N19,N20 | PARTIAL/OPEN |

### 4.2 Acceptance axioms and test-domain restrictions

| ID | Restriction | Affected N-rows | Independence/status |
|---|---|---|---|
| DSF-A1 | total expansion plus same-model row bridge | N1--N20 | structural gate; OPEN until instantiated |
| DSF-A2 | suitable intervention requires declared suitable pair and nonempty successor set | N1,N3,N10,N11,N12,N16,N19 | no source-level two-sided proof; OPEN |
| DSF-A3 | finite H protocol exhaustively enumerated before evaluation | N4,N6 | finite proxy does not decide HRep; PARTIAL |
| DSF-A4 | contexts satisfy FAdmissible | N2,N3,N6,N9,N11 | ADM-T1 ill-typed; B3/OPEN |
| DSF-A5 | nonempty exhaustive context domain from ADM-A2 | N2,N3,N6,N9,N11 | prior proof ill-typed; B3/OPEN |
| DSF-A6 | one rigid frame and explicit identity transport | N3,N7,N11,N16 | IC-SP-001/002 required but unrun; PARTIAL |
| DSF-A7 | freeze before model and no mid-review revision | N1--N20 | PINNED procedure; no semantic conclusion |

Only a restriction with a valid two-sided result may be B2. No restriction in
DSF-A2--A5 currently has a source-level two-sided result.

### 4.3 Imported principles

| ID | Formula/anchor | Grade | Affected N-rows | Adequacy/circularity |
|---|---|---|---|---|
| DSF-P1 | binary information product, calculus (7d3) | P | none directly | source-scoped; no SPA product pin; head absent from antecedent |
| DSF-P2 | HRep to existential vehicle/code/correction package, (24) | P | N4,N6 | finite H proxy not equivalent; conclusion does not define HRep |
| DSF-P3 | Spark-cut witnesses to existential P56 map, (39) | P | N3,N11,N16 | kernel-scoped; no total SPA expansion; conclusion absent from premises |

These imports are not project proofs and are not validated here.

### 4.4 Bridges

| ID | Exact bridge | Grade | Consumers | Affected N-rows | Adequacy and no-splicing |
|---|---|---:|---|---|---|
| DSF-B1 | FallSel and Epi and PAT_VE imply TypedVEEAnalogue; (36) | B | VE-hat only | N15 | unclaimed; terminal/unreported; head absent from antecedent |
| DSF-B2 | selected P56 map plus KMAP_BIND and PORT imply Realized; (39a) | B | Real/RealCore/PhysExp | N3,N11,N16 | partial; same selected map, trace and program port required |
| DSF-B3 | Exp, RealCore, Epi, Linked, PEALIGN imply PhysExpEpisode; (43) | B | PhysRefExp, pi_E | N3,N11,N16 | open; common episode/trace/target/successor/frame/port/program/scope required |
| DSF-B4 | PhysExpEpisode and TRef imply PhysRefExpEpisode; (44) | B | pi_E | none directly | open; same theta required |

No bridge is reclassified as a theorem. No original-row bridge exists.

## 5. Exact primitive coverage

All exact right-hand sides remain calculus Table 1.1. Bare D1--D21 in
Sections 5--8 name the Section 6 semantic families, never the DSF-D1--DSF-D11
project-item identifiers in Section 4.

| Block | Identifiers | Family/status |
|---|---|---|
| I | I_BOUNDARY, I_VARIABLE, I_PERMUTATION, I_CLONING | D1 OPEN |
| binary I | I_INTEROPERABILITY | D1 OPEN |
| R-PK | R_BOUNDARY, R_VALUE, K_PHYSICAL_INSTANTIATION, K_REALIZATION_SCOPE, R_COUNTERFACTUAL_CAUSAL_ROLE, R_MAINTENANCE, R_VALUE_INTERVENTION, R_FINITE_EVIDENCE_BOUND | D2 OPEN |
| R-recipe | K_RECIPE_CAUSAL_ROLE, K_HISTORY, A_ARTIFACT_ROLE | D2 OPEN |
| R-conditional | X_EXPLANATORY_LEVEL, K_REALIZATION_EQUIVALENCE | D2/D19 OPEN |
| H | H_BOUNDARY, H_NO_DESIGN, H_ACCURACY, H_RECIPE, H_DIGITAL_RECIPE, H_ERROR_CORRECTION, H_VEHICLE | D4 PARTIAL |
| V | V_POPULATION, V_INHERITANCE, V_VARIATION, V_SELECTION, V_FALLIBILITY | D3 PARTIAL |
| C | C_TARGET, C_CHANNEL, C_CHAIN, C_AUXILIARIES, C_DISCRIMINATOR, C_PROTOCOL, C_OUTCOME | D5 PARTIAL |
| E | E_P1, E_TT, E_EE, E_EVIDENCE_LINK, E_P2, E_PROVENANCE, E_FALLIBILITY | D6 PARTIAL |

Auxiliary coverage:

| Group | Members/anchor | Status |
|---|---|---|
| applicability | I/R/R_EQ/H APP/NA and EXT_P; (12) | report syntax PINNED; source restrictions OPEN/PARTIAL |
| link identity | J_IR,J_RE,J_CE,J_KP,J_pSigmaC,JOIN_CE,JOIN_IRRE; (12) | D10 PARTIAL |
| episode/analogy | CYCLE,PAT_VE,TREF; (12),(32),(35a) | D5,D6,D16 PARTIAL/OPEN |
| Spark growth | NONSEED,G1--G4,TE,EXT,NR; (12) | D9 OPEN |
| explanation | FIRST_PROBLEM,TARGET_EQ,PROMOTED_ACCOUNT,GOOD_ACCOUNT,DISPLACEMENT_SUCCESSOR; (12) | D9 OPEN |
| realization | FIN,W1--W5,COH5,ID3,ALIGN,W0term,COH0,PORT,KMAP_BIND; (12) | D9 OPEN |
| alignment | PEALIGN; (42) | D10/D9 PARTIAL |
| capacity | CAP_NS,CAP_CA,CAP_A5,CAP_OET,CAP_JOIN; (12),(45) | D7 OPEN |
| E priority | E_DOMAINREF,E_PROVGAP,E_UNRES; (13) | report syntax exact; meanings OPEN |

## 6. Semantic-family registry

Here N1--N20 name the ordered rows in Section 8. The affected-row sets are
transitive dependency-impact sets, not entailment or discharge claims.

| Node | Exact anchor/content | Head consumers | Affected N-rows | Status |
|---|---|---|---|---|
| D0 | Expand plus RowBridge; SPA 2,7 | all | N1--N20 | OPEN |
| D1 | InfoVar (14), product (7d) | I/PK/product | N1,N2,N3,N10,N11,N12,N16,N19 | OPEN |
| D2 | RetCover (15), CSRet (16), PK (17), RecipeKnow (18) | PK/RK/PhysExp | N1,N3,N10,N11,N12,N16,N19 | OPEN |
| D3 | Sel (25), FallSel (27a), finite FSel | Sel/FallSel/VE | N4,N5,N15,N19 | PARTIAL |
| D4 | DG (19)--(21), HRep (22), VehPkg (23), import (24), finite H proxy | H family | N4,N6 | PARTIAL_KEY_AND_THRESHOLD_TYPING |
| D5 | CritPkg (28), outcomes (29), TRef (34), finite FCritPkg | C/E/TRef/VE/PhysExp | N3,N5,N9,N11,N13,N14,N15,N16 | PARTIAL |
| D6 | Epi (31)--(33), finite FEpi | E/TRef/VE/PhysExp | N3,N5,N9,N11,N15,N16 | PARTIAL |
| D7 | CreativeCap (45), finite capacity | Cap | N2,N3,N6,N9,N11 | OPEN_UPDATE_TYPE and OPEN_ADMISSIBILITY_B3 |
| D8 | CreativeGenerator | none | N9 | OPEN; outside SPA-v1 |
| D9 | Core/Exp/P56/Realized/RealCore/PhysExp (37)--(43) | physical route | N3,N11,N12,N16 | OPEN |
| D10 | Linked/PEALIGN (41)--(42), finite joins/alignment | Link/PhysExp | N3,N7,N11,N16 | PARTIAL |
| D11 | WholeClone/WholeDigital (46), SelfReproduction | none | N6 | OPEN |
| D12 | BoundaryMove (63), ConservativeExtension | none | N7,N20 | OPEN |
| D13 | FiniteTheorySuite (63), Pass | none | N8 | OPEN |
| D14 | Possible_Phi(T) | none | N10 | OPEN |
| D15 | Artifact, Record, Deduction, Prediction | none | N12,N13 | OPEN |
| D16 | TypedVEEAnalogue (36), RepresentedConjecture, TheoryMediatedCriticism | VE | N15 | OPEN |
| D17 | NoPossibleCritic, FinalOutput | none | N16 | OPEN |
| D18 | RoleEq, SecondSubstance, CausalExemption | none | N17 | OPEN |
| D19 | SameLabelSwap (63), SameSyntax, RealizationEq | Rfull | N18 | OPEN |
| D20 | OneCopyOnly (63), ReplicationRole | none | N19 | OPEN |
| D21 | FiniteVariantSuite (63), RetainsOrAdapts, EverettianUniversalClaim | none | N20 | OPEN |

## 7. Audit-head inventory

Target/cone means direct finite coverage followed by full transitive readiness.
The second value controls testing. N1--N20 again name the ordered rows in
Section 8; the affected-row column is transitive and does not assert entailment.

| Head | Target/anchor | Inputs/path | Consumer | Affected N-rows | Target/cone |
|---|---|---|---|---|---|
| I-hat | InfoVar (14) | SI; D | PK,pi_I | N1,N2,N3,N10,N11,N12,N16,N19 | OPEN/OPEN |
| PK-hat | PKcur (14)--(17) | I,SPK; D | RK | N1,N3,N10,N11,N12,N16,N19 | OPEN/OPEN |
| RK-hat | RecipeKnow (17)--(18) | PK,SRK; D | PhysExp,pi_R | N3,N11,N12,N16 | OPEN/OPEN |
| Rfull-hat | conjunction Rfull | SRfull; D | pi_{R_eq} | N18 | OPEN/OPEN |
| Hsrc-hat | HRep (22) | SHsrc; D | VehExists,H | N4,N6 | PARTIAL/PARTIAL |
| VehExists-hat | existential H consequence (24) | Hsrc; P | Veh | N4,N6 | PARTIAL/PARTIAL |
| Veh-hat | selected H witness (8)--(11) | VehExists; P,varpi30 | DG | N4,N6 | PARTIAL/PARTIAL |
| DG-hat | DG (20)--(21) | Veh,SDG; P,varpi30 | H | N4,N6 | PARTIAL/PARTIAL |
| H-hat | HRep and DG | Hsrc,DG; D+P | pi_H | N4,N6 | PARTIAL/PARTIAL |
| P56Exists-hat | existential P56Map (39) | SP56; P | RealExists | N3,N11,N16 | OPEN/OPEN |
| Sel-hat | Sel (25)--(26) | SSel; D | FallSel,pi_V | N4,N5,N15,N19 | PARTIAL/PARTIAL |
| FallSel-hat | FallSel (27a) | Sel,SFall; D | VE | N15 | PARTIAL/PARTIAL |
| C-hat | CritPkg (28) | SC; D | E,pi_C | N3,N5,N9,N11,N13,N14,N15,N16 | PARTIAL/PARTIAL |
| E-hat | Epi (33) | C,SE; D | TRef,VE,PhysExp,pi_E | N3,N5,N9,N11,N15,N16 | PARTIAL/PARTIAL |
| TRef-hat | TRef (34) | E,STRef; D | PhysRefExp,pi_E | N5 | PARTIAL/PARTIAL |
| VE-hat | TypedVEEAnalogue (36) | FallSel,E,SVE; B | none | N15 | PARTIAL/PARTIAL |
| Core-hat | Core (37) | SCore; D | Exp,RealCore | N3,N11,N12,N16 | OPEN/OPEN |
| Exp-hat | Exp (38) | Core,SExp; D | PhysExp | N3,N11,N12,N16 | OPEN/OPEN |
| RealExists-hat | existential Realized (39a) | P56Exists; P+B,varpi56 | Real | N3,N11,N16 | OPEN/OPEN |
| Real-hat | selected Realized witness | RealExists; D+P+B,varpi56,varpi49 | RealCore | N3,N11,N16 | OPEN/OPEN |
| RealCore-hat | RealCore (40) | Core,Real; D+P+B | PhysExp | N3,N11,N16 | OPEN/OPEN |
| Link-hat | Linked (41) | SLink; D | PhysExp | N3,N7,N11,N16 | PARTIAL/PARTIAL |
| PhysExp-hat | PhysExpEpisode (43) | RK,E,Exp,RealCore,Link; B with P ancestry | PhysRefExp,pi_E | N3,N11,N16 | PARTIAL/OPEN |
| PhysRefExp-hat | PhysRefExpEpisode (44) | PhysExp,TRef; B with P ancestry | pi_E | none directly | PARTIAL/OPEN |
| Cap-hat | CreativeCap (45) | SCap; D | none | N2,N3,N6,N9,N11 | OPEN/OPEN |
| binary I-product hat | product (7d) | two SI supports+interoperability; P | pi_{I^otimes} | none | OPEN/OPEN |
Direct target coverage is 0 PINNED, 14 PARTIAL, 11 OPEN. Full-cone readiness
is 0 PINNED, 12 PARTIAL, 13 OPEN. VE-hat and Cap-hat are unreported.

## 8. Twenty original N-rows

All remain REGISTERED_SCHEMA [N]. The family column below is direct/top-level;
the complete transitive cones are the inverse affected-row map in Section 6.

| ID | Row shape | Direct/top-level families | Status/reason |
|---|---|---|---|
| NE_INFORMATION_NOT_KNOWLEDGE | InfoVar and not PKcur | D0,D1,D2 | OPEN: no FInfoVar/FPK; DO NOT TEST |
| NE_INFORMATION_NOT_CREATIVITY | InfoVar and not CreativeCap | D0,D1,D7 | OPEN: bridges absent; DO NOT TEST |
| NE_RETENTION_NOT_CREATIVITY | PK or RecipeKnow; not Exp,PhysExp,CreativeCap | D0,D2,D7,D9 | OPEN; DO NOT TEST |
| NE_SELECTION_NOT_HIGH_FIDELITY | Sel; not HRep,DG,ErrorCorrect,VehPkg | D0,D3,D4 | PARTIAL: SPA Section 8 registers the exact FSel/not-FPT target fragment; source denials, key binding, and threshold typing remain open; DO NOT TEST |
| NE_SELECTION_NOT_CRITICISM | Sel; not CritPkg,TRef | D0,D3,D5 | OPEN; DO NOT TEST |
| NE_WHOLE_CREATOR_NOT_CLONABLE | F=A and CreativeCap; four denials | D0,D4,D7,D11 | OPEN; DO NOT TEST |
| NE_BOUNDARY_IS_EVIDENCE | Linked+BoundaryMove; not Linked in extension | D0,D10,D12 | OPEN: SPA interface fixtures test splicing, not this exact boundary-extension row; DO NOT TEST |
| NE_FINITE_ENUMERATION_NOT_ALL_THEORIES | finite passing suite plus outside failure | D0,D13 | OPEN; DO NOT TEST |
| NE_P1_TT_EE_P2_NOT_GENERATOR | Epi; not CreativeCap,CreativeGenerator | D0,D6,D7,D8 | PARTIAL: SPA Section 8 registers the exact FEpi/not-FCreativeCap target fragment; capacity is ill-typed and generator semantics remain open; DO NOT TEST |
| NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE | Possible; no PK bearer/value | D0,D2,D14 | OPEN; DO NOT TEST |
| NE_RECIPE_NOT_CREATIVITY | RecipeKnow; not CreativeCap,PhysExp | D0,D2,D7,D9 | OPEN; DO NOT TEST |
| NE_ARTIFACT_NOT_RECIPE | Artifact; not RecipeKnow,Exp | D0,D2,D9,D15 | OPEN; DO NOT TEST |
| NE_BARE_RECORD_NOT_EVIDENCE | Record/Deduction/Prediction; not CritPkg | D0,D5,D15 | OPEN; DO NOT TEST |
| NE_EVIDENCE_NOT_CONFIRMATION | CritPkg+C_SURV; not Confirmed | D0,D5 | OPEN; DO NOT TEST |
| NE_VARIATION_NOT_CONJECTURE_IDENTITY | analogue; not representation/criticism | D0,D16 | OPEN; DO NOT TEST |
| NE_NONREFUTABLE_NOT_CREATIVE | NoPossibleCritic or FinalOutput; not PhysExp | D0,D9,D17 | OPEN; DO NOT TEST |
| NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE | RoleEq; two denials | D0,D18 | OPEN; DO NOT TEST |
| NE_SUBSTRATE_SWAP_NOT_AUTOMATIC | exists SameLabelSwap | D0,D19 | OPEN; DO NOT TEST OR REPAIR |
| NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE | OneCopyOnly; not PK,Sel,ReplicationRole | D0,D2,D3,D20 | OPEN; DO NOT TEST |
| NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS | extension plus new failing pair; no universal claim | D0,D12,D21 | OPEN; DO NOT TEST |

Row count: PINNED=0, PARTIAL=2, OPEN=18.

The two PARTIAL classifications follow only from SPA Section 8's two exact-row
preregistrations. They do not mean that either original negative conclusion
is established. The boundary/interface row is OPEN: IC-SP-001/002 concern
witness splicing, not the exact boundary-extension formula in that row. Every
other row is likewise OPEN under the precedence rule in Section 1.

## 9. Reports and applicability

The eight report projections are exact audit definitions, not validation of
their input heads.

| Projection | Reads | Priority/applicability |
|---|---|---|
| pi_I | I-hat | I_NA, then Base |
| pi_R | RK-hat, EXT_P | EXT_P overrides; R_NA means not applicable |
| pi_H | H-hat | H_NA means not applicable |
| pi_V | Sel-hat | no NA selector |
| pi_C | C-hat and one C outcome | calculus (62) order |
| pi_E | TRef+domain, provenance gap, PhysRef, PhysExp, E, unresolved | calculus (62) order |
| pi_{I^otimes} | binary I head, product APP | APP absent means not applicable |
| pi_{R_eq} | Rfull, R_EQ_APP/NA | APP absent means not applicable |

Provision states require exactly one I APP/NA, R APP/NA and H APP/NA choice.
The optional realization test has at most one R_EQ choice. A complete critical
package has exactly one critical outcome. Selected witness conditions are
varpi30 for Veh/DG/H, varpi56 for RealExists, and varpi56 plus varpi49 for
Real/RealCore/PhysExp/PhysRefExp.

## 10. Cross-domain identity freeze

Future models must preserve, in one typed context:

1. IR/RE/CE endpoints and their shared eta,boundary,bearer,task,episode key;
2. critical package and exact evidence token;
3. episode/realization trace, information token, bearer/knowledge port,
   target, successor, task, environment, provenance, obligation frame,
   program and scope; and
4. selected realization map and program port.

Label equality is not identity. IC-SP-001 and IC-SP-002 are mandatory but
unrun adversarial fixtures.

Still-open cross-fragment identities include: common task carrier across K/H/J;
H code families embedded into K states; population boundary/environment tied
to J; lineage tied to H route; agent episode/package/trace tied to J; H
witnesses tied to J realization/program; J obligation frames tied to original
T,Lambda,Lambda-prime; rigid eta/theta/varpi across all fragments; and a
complete Transport signature.

## 11. Detailed SPA-v1 inventory

| ID | Content | Authority | Status |
|---|---|---|---|
| SPA-01 | two-axis status vocabulary | audit definition | PINNED |
| SPA-02 | fragment tuple/class | model-class definition | PARTIAL |
| SPA-03 | total expansion | acceptance obligation | OPEN |
| K-01 | task/intervention carriers/tables | primitive data | PARTIAL |
| K-02 | FFace/intervention operator | definitions | PINNED relative to tables |
| K-03 | FRecover/FDG | definitions | PARTIAL cross-domain |
| K-04 | local digital lemma | theorem | PINNED |
| P-01 | population carrier/tables | primitive data | PARTIAL |
| P-02 | lineage/FCont | definitions | PINNED relative to tables |
| P-03 | selection component predicates | definitions | PARTIAL |
| P-04 | FCausalAffects | definition | PARTIAL |
| P-05 | FSel | proxy definition | PARTIAL |
| H-01 | H carriers/words/cells/key | primitive schema | PARTIAL |
| H-02 | protocol/error/refinement/FComplete, including untyped epsilon threshold | data+definition | PARTIAL_KEY_AND_THRESHOLD_TYPING |
| H-03 | FImplements/FOutput/FError | primitive tables | PARTIAL |
| H-04 | witness/FRouteData | tables+definition | PARTIAL |
| H-05 | FProtocolChain | definition | PARTIAL |
| H-06 | FPT-HRoute | finite proxy | PARTIAL |
| A-01 | agent/provenance carriers/maps | primitive schema | PARTIAL |
| A-02 | transitions/reach/owned paths | definitions | PARTIAL |
| A-03 | provenance DAG/closure | prose acceptance meaning | PARTIAL |
| A-04 | episode/package records | record schema | PARTIAL |
| A-05 | finite criticism/episode predicates | proxy definitions | PARTIAL |
| A-06 | policy context/FAdmissible | proxy definition | PARTIAL/weak |
| A-07 | FExternalEveryTarget | definition with missing Boolean signature | PARTIAL; intended redundancy unproved |
| A-08 | four FCan clauses | operational definitions | OPEN_UPDATE_TYPE |
| A-09 | FCreativeCap | proxy definition | OPEN |
| J-01 | interface carriers/maps | primitive schema | PARTIAL |
| J-02 | key/label/transport | identity schema | PARTIAL |
| J-03 | key match/payload | definitions | PARTIAL |
| J-04 | joins/FLinked | definitions | PARTIAL |
| J-05 | FPEALIGN/FCompOK | composition definition | PARTIAL |
| J-06 | local key-mismatch theorem | theorem | PINNED but definitional |
| J-07 | IC-SP-001/002 | acceptance obligations | OPEN/unrun |
| Q-01 | freeze/no mid-review change | acceptance rule | PINNED procedure |
| Q-02 | VERIFIED_FIXTURE requirements | acceptance rule | PINNED rule/OPEN execution |
| Q-03 | expansion/row bridge | acceptance rule | OPEN |
| Q-04 | mutation catalogue/H mutant | mutant definition | PINNED definition/OPEN execution |

## 12. N-specific primitive inventory

Definitions built from open leaves:

- BoundaryMove uses SameObservableLabel and MovedConstructorPort;
- FiniteTheorySuite fixes finiteness, not Theory or Pass;
- FiniteVariantSuite fixes finiteness, not extension/adaptation;
- SameLabelSwap uses SameSyntax and RealizationEq;
- OneCopyOnly uses OneObservedToken and CounterfactualFamilyObserved; and
- WholeClone/WholeDigital are prose descriptions, not finite predicates.

Uninterpreted N-only leaves are SameObservableLabel, MovedConstructorPort,
Pass, CreativeGenerator, Possible, Artifact, Record, Deduction, Prediction,
Confirmed, RepresentedConjecture, NoPossibleCritic, FinalOutput, RoleEq,
SecondSubstance, CausalExemption, SameSyntax, OneObservedToken,
CounterfactualFamilyObserved, ReplicationRole, ConservativeExtension,
RetainsOrAdapts and EverettianUniversalClaim.

Also open and load-bearing are original TheoryMediatedCriticism,
RealizationEq, SelfReproduction, ErrorCorrect, Admissible, the four original
Can predicates and every original-to-fragment row bridge.

## 13. Frozen next step

The next tranche may only pin semantics. It must not construct an N-row
fixture. In order:

1. freeze a well-typed capacity-update signature without choosing it to force
   a desired model;
2. only then repeat the two-sided restriction check;
3. freeze the H-route system/task binding;
4. freeze missing primitive signatures and cross-fragment identities;
5. pin remaining open original terms; and
6. review every future bridge for grade, adequacy, circularity and no-splicing.

Any change creates a new version. It must not overwrite DSF-v1, SPA-v1,
ADM-v1, or recorded failed readiness statuses. Testing stays prohibited until
an entire row's dependency cone has no PARTIAL or OPEN item.
