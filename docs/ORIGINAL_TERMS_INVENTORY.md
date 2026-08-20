# ORIGINAL TERMS INVENTORY — Tranche After Cross-Fragment Identity Record

Purpose: inventory for DSF-v1 §13 step 5 ("pin remaining open original terms").
Sources (read via GitHub, branch `agent/hkey-v1-binding`, repo `AHepi/TestPoietic`):
- `docs/DOWNSTREAM_SEMANTIC_FREEZE_V1.md` (DSF-v1), esp. §6 (families D0–D21), §8 (N1–N20), §12 (N-specific primitive inventory)
- `docs/PIECEMEAL_PREMISE_CALCULUS.md` (equation anchors)
- `docs/PIECEMEAL_SOURCE_REGISTER.md` (source-grade anchors D/T/P/B)

Row-number convention: N1–N20 follow DSF-v1 §8 order:
N1=NE_INFORMATION_NOT_KNOWLEDGE, N2=NE_INFORMATION_NOT_CREATIVITY,
N3=NE_RETENTION_NOT_CREATIVITY, N4=NE_SELECTION_NOT_HIGH_FIDELITY,
N5=NE_SELECTION_NOT_CRITICISM, N6=NE_WHOLE_CREATOR_NOT_CLONABLE,
N7=NE_BOUNDARY_IS_EVIDENCE, N8=NE_FINITE_ENUMERATION_NOT_ALL_THEORIES,
N9=NE_P1_TT_EE_P2_NOT_GENERATOR, N10=NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE,
N11=NE_RECIPE_NOT_CREATIVITY, N12=NE_ARTIFACT_NOT_RECIPE,
N13=NE_BARE_RECORD_NOT_EVIDENCE, N14=NE_EVIDENCE_NOT_CONFIRMATION,
N15=NE_VARIATION_NOT_CONJECTURE_IDENTITY, N16=NE_NONREFUTABLE_NOT_CREATIVE,
N17=NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE, N18=NE_SUBSTRATE_SWAP_NOT_AUTOMATIC,
N19=NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE, N20=NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS.

---

## Part A — The 23 uninterpreted N-only leaves (DSF-v1 §12 list)

### 1. SameObservableLabel
- Anchor: calculus (63), inside `BoundaryMove_{η,θ}^{η',θ'} = B'≠B ∧ SameObservableLabel_{η,η'}(θ,θ') ∧ MovedConstructorPort_{η,η'}(θ,θ')`.
- N-rows: N7. Families: D12 (plus D0 gate).
- Fragment pin candidate: the J-02 label map / FKeyMatch (J-03). Mismatch: fragment label equality is intra-context key matching; the original is a cross-(η,θ) observable-label agreement. DSF §10 explicitly warns "label equality is not identity".
- Risk: medium. Over-weak pinning (pure string equality) manufactures the N7 countermodel trivially; over-strong (full task identity) destroys it.

### 2. MovedConstructorPort
- Anchor: calculus (63), same BoundaryMove conjunction.
- N-rows: N7. Families: D12.
- Fragment pin candidate: `PORT` / `ProgramOf(P_Σ)` in (12)/(42) and J port data. Mismatch: PORT binds a program port within one fixed θ; BoundaryMove requires tracking the constructor port across a boundary move B→B'. No fragment tracks a port across contexts.
- Risk: medium-high (this is the load-bearing limb of N7; pinning it as vacuous collapses the row).

### 3. Pass
- Anchor: calculus (63) `FiniteTheorySuite` fixes only `L ⊆ Theory_η ∧ |L|<∞`; Pass occurs in N8 row: `∀u∈L Pass(u) ∧ ∃u*∈Theory_η\L ¬Pass(u*)`.
- N-rows: N8. Families: D13.
- Fragment pin candidate: none found. (C-suite predicates FCritPkg test packages, not theory-suite membership.)
- Source-grade constraint: none direct; POPPER_LSCD §§18, 29–30 (comparison/application) is the closest background.
- Risk: medium — pinning Pass as "derivable" vs "survived test" changes whether a finite-suite/outside-failure model exists.

### 4. CreativeGenerator
- Anchor: N9 row `Epi ∧ ¬CreativeCap ∧ ¬CreativeGenerator_η(A)`. DSF §6 D8: "CreativeGenerator — none (no head consumers) — N9 — OPEN; outside SPA-v1".
- N-rows: N9. Families: D8.
- Fragment pin candidate: none. Explicitly outside SPA-v1; FCreativeCap (A-09) pins CreativeCap, not the generator predicate.
- Risk: HIGH / steering-sensitive. If pinned as implied by CreativeCap, N9's countermodel is destroyed by construction; if pinned as coextensive with a single Epi episode, it is manufactured. Must be pinned independently of both.

### 5. Possible (Possible_Φ)
- Anchor: N10 row `Possible_Φ(T) ∧ ¬∃b,k PK^cur`; fixture `PossibleTaskOnly` in (62b).
- N-rows: N10. Families: D14.
- Fragment pin candidate: none direct. Source-grade constraint: CT_FOUNDATION (constructor-theoretic task possibility, arXiv:1210.7439 §§3.1–3.2) supplies a physical possibility notion — a D/P-grade anchor that constrains but does not operationally define the audit-level predicate.
- Risk: medium. Pinning Possible as "no PK bearer" would destroy N10; pinning as "physical law permits" keeps it independent.

### 6. Artifact
- Anchor: N12 row `Artifact(p_code) ∧ ¬RecipeKnow ∧ ¬Exp`.
- N-rows: N12. Families: D15.
- Fragment pin candidate: `ArtifactClassified_η(p_code)` (Table 1.1, A_ARTIFACT_ROLE) is a partial candidate. Mismatch: ArtifactClassified feeds the RK-hat rule and presupposes the recipe/history lattice; the bare Artifact in N12 must hold *without* RecipeKnow, so it cannot be pinned to a predicate whose support implies RK-relevant certificates.
- Risk: medium-high. Pinning Artifact = ArtifactClassified destroys N12's ¬RecipeKnow limb unless the candidate's support is shown RK-free.

### 7. Record
- Anchor: N13 row `Record(o_χ) ∨ Deduction(d_χ) ∨ Prediction(d_χ)`; fixture `BareScore = Record(o_χ) ∧ ¬CritPkg` in (62b); channel typing in (28): `ω_χ ∈ Observation ∪̇ Deduction ∪̇ Prediction`.
- N-rows: N13. Families: D15 (channels feed D5 CritPkg).
- Fragment pin candidate: A-04 episode record schema / A-05 finite episode predicates. Mismatch: fragment records are already packaged inside FCritPkg-shaped tuples; N13 requires the bare record *outside* the package.
- Source-grade: POPPER_LSCD/POPPER_CNR constrain: "a bare result is not automatic falsification" / a record is evidence only in a typed package (calculus text after (28)).
- Risk: low-medium.

### 8. Deduction
- Anchor: same as Record — (28) channel, N13 row, (62b).
- N-rows: N13. Families: D15/D5.
- Fragment pin candidate: `FDerives` (C_DISCRIMINATOR ingredient, §3.4(3): lacks complete displayed signature). Mismatch: Derives_η(A⁻_χ∧Ξ_χ,d_χ) is package-internal; bare Deduction(d_χ) must be definable without the critical package.
- Risk: low-medium.

### 9. Prediction
- Anchor: same as Record/Deduction — (28), N13, (62b).
- N-rows: N13. Families: D15/D5.
- Fragment pin candidate: none beyond the shared channel typing; `Predeclared_η(ρ_χ,d_χ,D_χ)` in C_DISCRIMINATOR is package-internal only.
- Risk: low-medium.

### 10. Confirmed
- Anchor: calculus (30), the explicit N-grade non-entailment `CritPkg ∧ C_SURV ⇏ Confirmed(A⁻_χ)`; N14 row; fixture `CompleteAgreeingPackage` in (62b).
- N-rows: N14. Families: D15 (DSF §6) with D5 consumer.
- Fragment pin candidate: none (correctly — see risk). The π_C report value SURVIVED_DECLARED_ATTEMPT (62) is deliberately not Confirmed.
- Source-grade constraint: POPPER_CNR "a surviving attempted test is not confirmation"; register explicit-limit list ("a surviving result confirms an explanation" listed as NOT established).
- Risk: HIGH / steering-sensitive. Any pinning that lets C_SURV imply Confirmed destroys N14 and contradicts the register's explicit limit; any pinning that makes Confirmed unreachable manufactures trivial countermodels. Likely correct pin: Confirmed as a distinct, strong epistemic status never derivable in this calculus.

### 11. RepresentedConjecture
- Anchor: N15 row `TypedVEEAnalogue ∧ ¬RepresentedConjecture_η(λ)`; bridge (36) prose: the analogue "does not identify a biological variation with a represented conjecture".
- N-rows: N15. Families: D16.
- Fragment pin candidate: none. The PAT_VE role maps (35a) are typed-structural only; using them as the pin would violate the bridge's own scope (B-grade, register: "does not identify mutation with conjecture").
- Risk: HIGH-adjacent. Pinning RepresentedConjecture so that TypedVEEAnalogue implies it destroys N15 and exceeds source scope of (36).

### 12. NoPossibleCritic
- Anchor: N16 row `(NoPossibleCritic_η(A) ∨ FinalOutput_η(A)) ∧ ¬PhysExpEpisode`; fixture `FinalUncriticisableOutput` (62b).
- N-rows: N16. Families: D17.
- Fragment pin candidate: none. (FExternalEveryTarget / FAdmissible are unrelated context checks.)
- Risk: HIGH / steering-sensitive. A modal "no possible critic" predicate: pin too weakly (no *actual* critic) and N16 becomes trivial/manufactured; pin too strongly (no critic in any extension) and it may become unsatisfiable, destroying the countermodel. Needs an explicit modality scope decision.

### 13. FinalOutput
- Anchor: same as NoPossibleCritic — N16, (62b).
- N-rows: N16. Families: D17.
- Fragment pin candidate: none. H-layer output FOutput (H-03) is a code output, not a finality claim.
- Risk: medium-high; interacts with NoPossibleCritic in a disjunction, so the two pins must be coordinated.

### 14. RoleEq
- Anchor: N17 row `RoleEq_η(b,k) ∧ ¬SecondSubstance ∧ ¬CausalExemption`.
- N-rows: N17. Families: D18.
- Fragment pin candidate: none direct; closest is RealizationEq machinery (K_REALIZATION_EQUIVALENCE, Table 1.1) but that is an R-block existential over (b,k)-pairs — RoleEq is a role-level equality, not a realization equivalence.
- Source-grade constraint: FOR_EMERGENCE (Fabric of Reality ch. 1, pp. 27–28; paraphrase only) supports higher-level causal role autonomy compatible with physical realization — D/P-grade background, not an operational pin.
- Risk: HIGH-adjacent: if RoleEq is pinned to syntactic/label equality, N17's denials lose bite.

### 15. SecondSubstance
- Anchor: N17 row (negated conjunct).
- N-rows: N17. Families: D18.
- Fragment pin candidate: none. Source-grade: register explicit limit — "an ungrounded abstraction introduces a second ontology" is NOT licensed; FOR_EMERGENCE paraphrase rejects a second substance. This is a negative constraint: the pin must keep SecondSubstance false whenever RoleEq holds under FOR-style emergence, else N17 is destroyed.
- Risk: medium-high.

### 16. CausalExemption
- Anchor: N17 row (negated conjunct).
- N-rows: N17. Families: D18.
- Fragment pin candidate: none. Same negative constraint as SecondSubstance (FOR_EMERGENCE: no causally exempt abstract entity).
- Risk: medium-high.

### 17. SameSyntax
- Anchor: calculus (63), inside `SameLabelSwap_{η,θ}(b',k') = SameSyntax(b,k;b',k') ∧ ¬RealizationEq_η((b,k),(b',k');T,E)`; fixture `SameLabelDifferentTask` (62b); N18 row `∃b',k' SameLabelSwap`.
- N-rows: N18. Families: D19.
- Fragment pin candidate: J-02 label map / syntax of p_code (Σ*). Mismatch: fragment syntax equality is code-string level; the original requires syntactic identity of bearer-attribute pairs across realizations.
- Risk: medium-high. DSF §8 marks N18 "DO NOT TEST OR REPAIR" — this pair (SameSyntax, RealizationEq) is the most delicate conjunction in the inventory.

### 18. OneObservedToken
- Anchor: calculus (63), inside `OneCopyOnly_{η,θ} = OneObservedToken(b,k) ∧ ¬CounterfactualFamilyObserved_η(b,k)`; fixture (62b); N19 row.
- N-rows: N19. Families: D20.
- Fragment pin candidate: none direct (finite H/K carriers could supply token-count witnesses, but no existing F-predicate counts observed tokens).
- Source-grade constraint: FOR_GENE_STRUCTURE (FoR ch. 8 pp. 187–190; paraphrase): "a one-copy local inspection cannot by itself settle a gene's knowledge or replicator role" — directly motivates this leaf and its denial partner.
- Risk: low-medium (observational counting is comparatively safe to pin).

### 19. CounterfactualFamilyObserved
- Anchor: calculus (63), OneCopyOnly; N19 row.
- N-rows: N19. Families: D20.
- Fragment pin candidate: RetCover/CSRet-style counterfactual profiles ((15),(16)) are structurally analogous but are retention-route predicates over Δ*, not "family observed" claims over bearer variants. Mismatch: different quantification domain.
- Source-grade: FOR_REPLICATOR_NICHE (counterfactual role across bearer/environmental variants) and FOR_GENE_STRUCTURE constrain the denial.
- Risk: medium-high — pinning this as *implied by* OneObservedToken (e.g., by finite-cohort exhaustion) destroys N19; register limit explicitly says a finite cohort is not exhaustive.

### 20. ReplicationRole
- Anchor: N19 row denial `¬ReplicationRole_η(b,k)`.
- N-rows: N19. Families: D20.
- Fragment pin candidate: DSF-D7 replication-route proxy / FPT-HRoute (H-06). Mismatch: HRoute is a high-fidelity protocol route for a declared self-reproducer; ReplicationRole is the counterfactual replicator-role claim denied in N19. Also FPT is PARTIAL_KEY_AND_THRESHOLD_TYPING (DSF-F2).
- Source-grade: FOR_REPLICATOR_NICHE (ch. 8 pp. 172–176, glossary p. 192).
- Risk: medium-high; must not be pinned to HRep-adjacent notions or N19's independence from Sel/HRep is lost.

### 21. ConservativeExtension
- Anchor: calculus (3) ("no formula may identify parts of θ and θ' without a named equality, port, or conservative-extension relation"); (63) heading "for a conservative extension (η',θ')"; N7 row (M' class) and N20 row `ConservativeExtension_{η,θ}^{η',θ'}`; DSF §2.4 DSF-A1 gate and D0 family.
- N-rows: N7, N20 (and structurally all rows via D0/A1). Families: D12, D21 (D0 gate).
- Fragment pin candidate: none. SPA-v1 §7 total-expansion machinery is the intended consumer but does not define the extension relation.
- Risk: HIGH-adjacent / global. This is the connective tissue for every M'-class row; a too-liberal extension relation manufactures countermodels, a too-strict one destroys them. It should be pinned *before* the boundary/variant leaves that sit under it (SameObservableLabel, MovedConstructorPort, RetainsOrAdapts).

### 22. RetainsOrAdapts
- Anchor: N20 row: `∃(ν*,E*) ∈ (V_θ'×E_η')\U ∧ ¬RetainsOrAdapts_{η',θ'}(ν*,E*)`.
- N-rows: N20. Families: D21.
- Fragment pin candidate: FSel/lineage predicates (P-02/P-03/P-05, DSF-D6). Mismatch: FSel is an intra-context selection proxy; RetainsOrAdapts is a cross-environment variant-to-environment claim in the extended frame.
- Source-grade: FOR_REPLICATOR_NICHE paraphrase (replication/adaptation as contextual counterfactual roles).
- Risk: HIGH-adjacent / steering-sensitive. The N20 countermodel exists iff some outside-suite pair fails RetainsOrAdapts; pinning it as "finite-suite success extends" destroys the row, pinning as "always fails outside U" manufactures it.

### 23. EverettianUniversalClaim
- Anchor: N20 row denial `¬EverettianUniversalClaim_{η',θ'}(U)`.
- N-rows: N20. Families: D21.
- Fragment pin candidate: none.
- Source-grade constraint: FOR_GENE_STRUCTURE register limit — "The Everettian explanatory discussion does not turn other universes into observed data or make a finite cohort exhaustive." Purely negative constraint; the pin must keep this claim unavailable from finite data.
- Risk: medium — mostly a guard-rail term; main hazard is an accidental positive pin.

---

## Part B — Open load-bearing original items (DSF-v1 §12, second list)

### 24. TheoryMediatedCriticism
- Anchor: Table 1.1 V_FALLIBILITY: `NoGuarantee(ν,κ,δ) ∧ ErrorEliminationByEnvironment_η(λ) ∧ ¬TheoryMediatedCriticism_η(λ)`; N15 row denial.
- N-rows: N15 (and V_FALLIBILITY certificate consumers: FallSel-hat, VE-hat → N15; transitively Sel/FallSel rows N4,N5,N19 via V-block, though the ¬TMC conjunct only bites the fallibility limb).
- Families: D16 (head consumer V/VE).
- Fragment pin candidate: none; A-05 finite criticism predicates are episode-level, not population-level theory-mediation.
- Source-grade: DEUTSCH/POPPER_OK (theory-laden criticism) — background only.
- Risk: HIGH-adjacent: it appears negated inside V_FALLIBILITY, so a careless pin flips a frozen certificate's meaning; also the denial limb of N15.

### 25. RealizationEq
- Anchor: Table 1.1 K_REALIZATION_EQUIVALENCE `∃b',k' RealizationEq_η((b,k),(b',k');T,E)`; calculus (63) SameLabelSwap (negated); report π_{R_eq} (62a); applicability selectors R_EQ_APP/R_EQ_NA (12).
- N-rows: N18 directly; Rfull-hat cone (Section 7: N18). Families: D19 (and D2/D19 per §5 R-conditional block).
- Fragment pin candidate: none (no FRealizationEq exists; J-02 key/label machinery is the closest substrate). R_EQ optional subtest is report syntax only (PINNED syntactically, OPEN semantically).
- Risk: HIGH / steering-sensitive. SameLabelSwap = SameSyntax ∧ ¬RealizationEq: pin RealizationEq too coarsely (syntactic) and N18 becomes unsatisfiable (destroyed); pin it too finely (nothing is ever realization-equivalent) and N18 is manufactured. This is the pivot of the "DO NOT TEST OR REPAIR" row.

### 26. SelfReproduction
- Anchor: H_APP selector (12): `DeclaredHRepClaim ∧ SelfReproduction_B(F,T) ∧ GenericResources(E)`; HRep definition (22); fixture NonSelfReproducingCandidate (62b); N4 row (denied via HRep); N6 row `F=A ∧ CreativeCap ∧ ... ∧ ¬SelfReproduction_B(A,T) ∧ ¬HRep`.
- N-rows: N4, N6. Families: D4 (and D11 via N6's whole-clone context).
- Fragment pin candidate: FPT-HRoute (H-06)/DSF-D7 replication-route proxy. Mismatch: proxy is PARTIAL_KEY_AND_THRESHOLD_TYPING (DSF-F2) and is a protocol-route proxy, not the biological self-reproduction claim; H-route key not bound to system/task.
- Source-grade: CTL (conditional no-design accurate self-reproduction; P-grade import (24)).
- Risk: medium-high. Pinning must not make CreativeCap ⇒ SelfReproduction (would destroy N6) nor Sel ⇒ SelfReproduction-compatible-HRep (would destroy N4, which is the only other PARTIAL row).

### 27. ErrorCorrect
- Anchor: (8) HConseq conjunct `ErrorCorrect(c,b_c;r,p_code,Σ,C_Σ)`; CorrectionWitness (H_ERROR_CORRECTION, Table 1.1); N4 row denial.
- N-rows: N4. Families: D4.
- Fragment pin candidate: FErrorCorrect (DSF §3.4(4): primitive Boolean table without displayed signature) and FError (§3.4(2): defined only when output and word share one code-family tag — prose, not axiom). Mismatch: fragment versions lack signatures and the code-family precondition is unaxiomatized.
- Source-grade: CTL import (24) — P-grade, scoped to the H regime.
- Risk: medium. Pin is constrained by the CTL conditional; main hazard is signature/type repair crossing into semantic choice.

### 28. Admissible
- Anchor: (12) CAP_JOIN: `Admissible_η(A,μ) ∧ SameCapabilityContext_η(...)`; CreativeCap (45).
- N-rows: N2, N3, N6, N9, N11 (Cap-hat cone). Families: D7.
- Fragment pin candidate: FAdmissible (A-06, "proxy definition, PARTIAL/weak"; DSF §3.5: its range condition is redundant with q's codomain, leaving only reachability). Mismatch: FAdmissible is a weak reachability check; original Admissible is unconstrained (DSF-F3: OPEN_ADMISSIBILITY_B3, no definition/import/bridge).
- Risk: HIGH / steering-sensitive: since Admissible is a conjunctive gate on all four Can predicates, a weak pin makes CreativeCap too easy (manufactures capacity; threatens N2, N3, N9, N11 denials), a strong pin makes it impossible (threatens N6's positive CreativeCap limb).

### 29–32. The four original Can predicates
- Anchors: (12): CAP_NS = CanConstructNonSeed_η(A,μ); CAP_CA = CanSustainConsequentialAppraisal_η(A,μ); CAP_A5 = CanA5Promote_η(A,μ); CAP_OET = CanDrawOnOwnedEvaluatedTarget_η(A,μ); jointly in CreativeCap (45) and the Cap rule (53)/(56).
- N-rows: N2, N3, N6, N9, N11 (Cap-hat support/cone). Families: D7.
- Fragment pin candidates: the four FCan clauses (A-08) — all OPEN_UPDATE_TYPE under DSF-F1 (they call Update(x, π_μ, q_μ, s'') passing whole functions where one policy/selector is declared). Mismatch: the fragment clauses are currently ill-typed; they cannot pin the originals until DSF §13 step 1 (capacity-update signature) is done.
- Risk: HIGH / steering-sensitive as a group (same double-edged gate logic as Admissible; N6 requires CreativeCap true while WholeClone/WholeDigital/SelfReproduction/HRep all false — an unusually tight simultaneous pin).

### 33. Original-to-fragment row bridges (RowBridge_j, j=1..20)
- Anchor: DSF-A1 acceptance axiom (`Expand_SPA-v1(Mflat,Mhat) ∧ Mhat ⊨ T ∧ RowBridge_j(Mflat,Mhat)`); DSF §2.4: "records zero accepted total expansions and zero original-row bridges"; DSF §4.4: only B1–B4 head-level bridges exist, none is a row bridge.
- N-rows: N1–N20 (all; D0 gate). Families: D0.
- Fragment pin candidate: none — by definition these do not exist yet. SPA §8's two exact-row preregistrations (for N4 and N9 target fragments) are the only partial coverage and are not bridges.
- Risk: highest structural item: each bridge must satisfy grade/adequacy/circularity/no-splicing review (DSF §13 step 6) and the cross-domain identity freeze (§10). A bridge that silently identifies fragment and original predicates (e.g., FCreativeCap ≡ CreativeCap) would manufacture/destroy entire rows.
- Note: these are records to be *authored*, not terms to be pinned; they belong in the tranche plan as a gating deliverable after the term clusters.

---

## Part C — Proposed clustering into bounded tranche records

Clusters are by family and consumer overlap. Each cluster is one candidate tranche record.

### Cluster T1 — Capacity modal layer (family D7)
Terms: Admissible, CanConstructNonSeed, CanSustainConsequentialAppraisal, CanA5Promote, CanDrawOnOwnedEvaluatedTarget.
Affected N-row cones: N2, N3, N6, N9, N11 (all CreativeCap consumers).
Dependency: BLOCKED on DSF §13 step 1 (well-typed capacity-update signature, DSF-F1 repair) — the fragment FCan clauses are ill-typed, so original pins have no stable fragment counterpart yet. Also depends on FAdmissible strengthening (A-06) if the pin references it.
Rationale: one tightly-coupled conjunctive definition (45); pinning any conjunct alone is meaningless.

### Cluster T2 — H-replication layer (family D4)
Terms: SelfReproduction, ErrorCorrect.
Affected N-row cones: N4, N6 (with N6 shared with T1).
Dependency: BLOCKED on DSF §13 step 3 (H-route key binding, DSF-F2) and §3.4 items (FErrorCorrect/FError signatures, code-family tag axiom).
Rationale: both are CTL-scoped H-regime predicates appearing in HRep/HConseq; the P-grade import (24) fixes their joint direction.

### Cluster T3 — Epistemic evidence and generator layer (families D8, D13, D14, D15, D17)
Terms: Pass, Possible, Artifact, Record, Deduction, Prediction, Confirmed, CreativeGenerator, NoPossibleCritic, FinalOutput.
Affected N-row cones: N8 (Pass), N9 (CreativeGenerator), N10 (Possible), N12 (Artifact), N13 (Record/Deduction/Prediction), N14 (Confirmed), N16 (NoPossibleCritic/FinalOutput).
Dependency: none hard beyond the identity record; Confirmed, CreativeGenerator, NoPossibleCritic need explicit independence side-conditions (see Part D).
Rationale: all are "epistemic status of theories/outputs/agents" leaves with no fragment counterpart; they pin cleanly as a single semantics record of independent predicates.

### Cluster T4 — VE-identity layer (family D16)
Terms: TheoryMediatedCriticism, RepresentedConjecture.
Affected N-row cones: N15 (plus FallSel/VE-hat certificate cone for TMC: N4,N5,N15,N19 transitively through V_FALLIBILITY).
Dependency: none hard; must respect bridge (36) scope (typed analogue, not identity).
Rationale: smallest record; two predicates flanking the variation↔conjecture gap.

### Cluster T5 — Boundary/substrate/counterfactual layer (families D12, D18, D19, D20, D21)
Terms: ConservativeExtension, SameObservableLabel, MovedConstructorPort, SameSyntax, RealizationEq, RoleEq, SecondSubstance, CausalExemption, OneObservedToken, CounterfactualFamilyObserved, ReplicationRole, RetainsOrAdapts, EverettianUniversalClaim.
Affected N-row cones: N7 (BoundaryMove leaves), N17 (role/substance), N18 (substrate swap), N19 (one-copy/counterfactual), N20 (finite variants/Everettian). ConservativeExtension additionally gates every M'-class row via D0/A1.
Dependency: ConservativeExtension should be pinned FIRST within this cluster (it is the carrier relation for SameObservableLabel, MovedConstructorPort, RetainsOrAdapts); optionally split into T5a {ConservativeExtension, SameObservableLabel, MovedConstructorPort} and T5b {rest} if record size is a constraint — consumer overlap (N7 vs N17–N20) supports that split.
Rationale: all are cross-context/realization-comparison predicates; pinning them in different records risks inconsistent extension semantics.

### Gating deliverable G0 — Row bridges
RowBridge_1..20 (Part B item 33): not a pinning cluster; must be authored per-row after the clusters feeding that row are pinned, then reviewed per DSF §13 step 6.

---

## Part D — Risk notes: steering-sensitivity ranking

A term is steering-sensitive if the pinning choice can manufacture or destroy the future countermodel of its N-row.

1. **RealizationEq (N18)** — highest. It sits negated inside SameLabelSwap (63): coarse pin ⇒ swap impossible (row destroyed); fine pin ⇒ swap guaranteed (row manufactured). N18 is already flagged DO NOT TEST OR REPAIR.
2. **CreativeGenerator (N9)** — no anchor anywhere except the row; any coextensiveness with CreativeCap or Epi collapses the row one way or the other.
3. **NoPossibleCritic (N16)** — modal scope choice (actual vs possible-world critics) directly decides satisfiability of the row.
4. **Confirmed (N14)** — the register's explicit limit (survival ≠ confirmation) constrains one direction; but a pin making Confirmed *unobtainable in principle* manufactures the countermodel. Needs a positive-but-unreachable-in-calculus status.
5. **Admissible + four Can predicates (N2,N3,N6,N9,N11)** — conjunctive gate on CreativeCap; N6 uniquely requires CreativeCap TRUE with four other denials, so these pins simultaneously serve a positive and four negative limbs.
6. **RetainsOrAdapts (N20)** — the row's existential denial lives or dies on this predicate's extension behavior.
7. **TheoryMediatedCriticism (N15, V_FALLIBILITY)** — occurs negated in a frozen certificate; pin flips certificate semantics, not just row semantics.
8. **RepresentedConjecture (N15)** — must stay outside bridge (36)'s scope or the B-grade bridge is exceeded.
9. **ConservativeExtension (N7,N20, all M' rows)** — global carrier; under/over-permissive choice scales across rows.
10. **RoleEq (N17)** — pinning to syntactic equality guts the emergence claim (FOR_EMERGENCE constraint).
Lower risk: Record, Deduction, Prediction, Pass, Possible, Artifact, OneObservedToken, SameObservableLabel, MovedConstructorPort, SameSyntax, SecondSubstance, CausalExemption, CounterfactualFamilyObserved, ReplicationRole, EverettianUniversalClaim (mostly guard-rails or observation-level), FinalOutput (medium; coupled to NoPossibleCritic), SelfReproduction, ErrorCorrect (constrained by CTL P-import).

---

## Part E — Recommended tranche order

Order respects DSF §13 (capacity signature and H-route binding precede this tranche) and intra-tranche dependencies:

1. **T5a-lite: ConservativeExtension first** (carrier for N7/N20 and all M' rows) — or at minimum pin it in the first record of T5.
2. **T4 (VE-identity)** — smallest, unblocked, high steering-sensitivity per term; good calibration record.
3. **T3 (epistemic evidence/generator)** — unblocked; contains Confirmed/CreativeGenerator/NoPossibleCritic; pin with explicit independence side-conditions against CreativeCap, CritPkg, C_SURV.
4. **T5 remainder (boundary/substrate/counterfactual)** — after ConservativeExtension; includes RealizationEq (handle N18 pair SameSyntax/RealizationEq jointly in one record).
5. **T2 (H-replication)** — after DSF §13 step 3 lands.
6. **T1 (capacity)** — after DSF §13 step 1 lands (Update signature).
7. **G0 row bridges** — per row, only after every cluster feeding that row's cone is pinned; then two-sided restriction check (DSF §13 step 2) repeats.

Rows with earliest possible readiness after this order: N15 (needs T4 + already PARTIAL D3/D5/D6 cones), N14/N13/N8/N10/N12/N16 (T3 only, modulo D0), N7/N17–N20 (T5). N4/N6 wait for T2; N2/N3/N9/N11 wait for T1.

---

## Part F — Items NOT verifiable from the three files

1. **SPA-v1 (`PIECEMEAL_SEMANTIC_ANNEX_V1.md`) was not read.** All fragment pin candidates above (FCan clauses, FAdmissible, FPT-HRoute, FSel, FEpi, FCritPkg, FErrorCorrect, label/key maps, A-04 record schema, SPA §8 preregistrations) are cited only through DSF-v1 §§3–5 and §11 summaries. Their exact clause text, and hence the precise mismatch statements, could not be verified against the annex itself.
2. **The verification ledger (`PIECEMEAL_CALCULUS_VERIFICATION.md`) was not read**; the 20 countermodel obligation statuses were taken from DSF-v1 §8 (all REGISTERED_SCHEMA [N]).
3. **No fragment predicate text exists for many leaves** (Pass, CreativeGenerator, Confirmed, NoPossibleCritic, FinalOutput, RoleEq, SecondSubstance, CausalExemption, RetainsOrAdapts, EverettianUniversalClaim, ConservativeExtension): absence of a candidate is asserted from DSF §12's "uninterpreted" listing plus the §5 coverage table, not from an exhaustive SPA-v1 text search.
4. **Whether `ArtifactClassified_η` (Table 1.1) is intended to be the same predicate as `Artifact` in N12** is ambiguous in the calculus text; the distinction above (role-in-lattice vs bare artifact) is an inference from their respective row shapes, not a stated fact.
5. **The modality of NoPossibleCritic** (which possible-world/extension quantifier is intended) is nowhere specified in the three files.
6. **TH-v1, ADM-v1, RPS-v1, and the frozen plan JSON were not read**; tranche-record format requirements for the next tranche (beyond DSF §13's ordering) are unverified.
7. **DSF-D11's Partial/Open split** for "N-only abbreviations; calculus (46),(63)" is given in §4.1 as "PARTIAL/OPEN" without per-item assignment; per-leaf status for (46) vs (63) items is inferred from §6 (D8–D21 all OPEN).
