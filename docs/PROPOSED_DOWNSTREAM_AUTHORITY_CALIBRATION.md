# Proposed downstream-authority calibration

## Status

**PROPOSED — NOT YET RUN.**

This protocol follows the semantic-pinning prerequisite in
[SPA-v1](PIECEMEAL_SEMANTIC_ANNEX_V1.md). No semantic countermodel check may
be reported as discharged until the relevant annex class, hash, model
certificate, and independent replay are recorded. The present document is
designed for human inspection before any new rule, source claim, or test
fixture is added.

## Why this is a two-stage test

The finite calculus is deliberately a rule-governed consequence system. Once
its rule register is frozen, it cannot produce a mysterious new theorem: its
useful “surprises” are instead one of the following:

- an intended result is not derivable from the premises thought to support it;
- a result has an unintended smaller support;
- two routes splice across an undeclared boundary, cut, bearer, or episode;
- a prohibited promotion becomes derivable; or
- a source statement requires a premise or a scope condition the calculus
  does not currently express.

Therefore the proposed test has three distinct stages.

0. **Semantic-pinning and model-class audit.** Freeze the annex, inspect
   whether every primitive used by a proposed countermodel has an operational
   interpretation, and reject vacuous valuation-only witnesses. This tests
   whether a later semantic countermodel would mean anything in its named
   class.

1. **Consequence sweep.** Derive all hatted closure heads and their
   one-premise-deletion consequences from the frozen register. This tests the
   mathematics and independent implementation of the construction itself.

2. **Authority calibration.** Pre-register a finite list of source claims,
   encode only their stated premises, and compare the resulting closure with
   the source claim and its explicit limits. This tests source conformance,
   not creativity in the world.

Because CTI, CTL, Popper, Deutsch, and the project kernel informed the
construction, the first authority calibration is **not blind**. A genuinely
held-out test must use an authority selected from a pre-registered eligible
corpus after this calculus is frozen, and must not be used to rewrite the
rules until the result is recorded.

## Gate 0: freeze the test

Before running the test, record:

| item | required value |
|---|---|
| calculus version | SHA-256 of **PIECEMEAL_PREMISE_CALCULUS.md** |
| frozen plan | **piecemeal-plan-v1.json** and its pinned SHA-256 |
| source register | SHA-256 of **PIECEMEAL_SOURCE_REGISTER.md** |
| semantic annex | SHA-256 of **PIECEMEAL_SEMANTIC_ANNEX_V1.md**, target model class, and intended \(\mathsf N\)-row scope |
| test sheet | this document plus a dated result sheet |
| rule-change policy | no rule, support, source grade, or expected result may change during a run |
| mismatch policy | record **CHALLENGE**, **UNDER-SPECIFIED**, or **PROHIBITED-PROMOTION**; do not repair the calculus before the mismatch is reviewed |

The source documents and lawful short quotations are listed in
[PIECEMEAL_SOURCE_REGISTER.md](PIECEMEAL_SOURCE_REGISTER.md). This protocol
uses source IDs and paraphrases rather than reproducing copyrighted passages.

## Stage 1: consequence sweep

### Valid provision states

A test case never supplies a bare support \(S_q\). It first forms a complete,
well-formed audit provision state

\[
v_q=\operatorname{Complete}(S_q,\Sigma_q),
\]

where \(\Sigma_q\) supplies exactly one of
\(\mathrm{I\_APP}/\mathrm{I\_NA}\),
\(\mathrm{R\_APP}/\mathrm{R\_NA}\), and
\(\mathrm{H\_APP}/\mathrm{H\_NA}\); uses the declared optional
multiple-realisation selector; and, whenever all of \(C_0\) are supplied,
selects exactly one critical outcome. The E-scope selectors must likewise be
consistent with the stated target.

Deleting an ordinary material certificate means withholding that certificate
while retaining a valid selector completion. Deleting an applicability
selector is tested by the valid substitution
\(\mathrm{APP}\mapsto\mathrm{NA}\), never by leaving an invalid partial
state.

For every hatted target \(q\) in the finite target set \(\mathcal Q\):

1. form \(\operatorname{Complete}(S_q,\Sigma_q)\), including its activation
   condition \(\sigma_q\);
2. derive \(\mathcal F(v_q;\varpi)\);
3. record \(q\), its provenance set \(\operatorname{Ann}(q)\), and the
   displayed six-coordinate result;
4. remove each non-selector material certificate \(a\in S_q\), one at a
   time, while retaining a valid completion;
5. test selector changes by the corresponding valid
   \(\mathrm{APP}\mapsto\mathrm{NA}\) substitution;
6. verify that every downstream head whose route support includes the
   deleted item is no longer derived, unless a distinct declared route still
   derives it; and
7. separately test each mutually-exclusive critical-outcome selector.

This is a finite **support-family/deletion sweep**, not a \(2^{44}\)
enumeration and not an antichain claim: some declared supports are properly
nested. It directly answers “what follows if this premise is added or
removed?” while preserving the calculus’s rule that a missing route means
\(\mathsf{NOT\_ESTABLISHED}\), not a negative fact about creativity.

### Required sweep report

| result class | what must be recorded |
|---|---|
| complete state | all material certificates plus the exact valid selector vector |
| derived head | exact support, activation condition, provenance grades |
| lost head after deletion | deleted certificate or selector substitution and every affected downstream head |
| alternative route | independent support that still derives the head |
| not applicable | selector and its declared scope |
| unexpected result | full supplied state and the first rule path that produced it |
| prohibited promotion | full supplied state, source/bridge rule path, and frozen non-entailment ID |

No result may be described as “creativity proven.”

## Stage 2: source-led conformance suite

The first calibration suite has seven deliberately different test cases.
Each is a source-led downstream consequence check. The source formulation,
scope, and explicit limit must be read alongside the result sheet.

| ID | authority and target claim | support package | valid selector completion | must derive | closure prohibition / semantic non-entailment check |
|---|---|---|---|---|---|
| A1 | **CTI:** an information medium requires a physical variable, computation, and cloning; it is not thereby knowledge. | \(S_{\widehat I}\), with retention material withheld. | \(\mathrm{I\_APP,R\_APP,H\_NA,R\_EQ\_NA}\); incomplete \(C\). | \(\widehat I\); \(I=\mathsf{MAY\_PASS}\). | \(\widehat{\mathrm{PK}},\widehat{\mathrm{RK}},\widehat{\mathrm{PhysExp}},\widehat{\mathrm{Cap}}\) absent. |
| A2 | **CTL:** a declared no-design, high/improvable-accuracy self-reproduction route has a vehicle/recipe/digital-error-correction consequence. | \(S_{\widehat H_{\rm src}}\), selected CTL witness context, H recipe/digital/correction package, and \(J_{p\Sigma C}\). | \(\mathrm{I\_NA,R\_NA,H\_APP,R\_EQ\_NA}\); incomplete \(C\). | \(\widehat H_{\rm src}\), selected vehicle/DG route, and \(\widehat H\). | \(\widehat{\mathrm{Cap}}\) absent; run the case-specific **A2-H-SCOPE** countermodel below for whole-agent digitality/clonability and a general creativity verdict. |
| A3 | **CTL:** selection can begin with a poor-fidelity “naked” replicator. | \(V_0\). | \(\mathrm{I\_NA,R\_NA,H\_NA,R\_EQ\_NA}\); incomplete \(C\). | \(\widehat{\mathrm{Sel}}\); \(V=\mathsf{MAY\_PASS}\), \(H=\mathsf{NOT\_APPLICABLE}\). | \(\widehat H,\widehat{\mathrm{DG}}\) absent; run **NE_SELECTION_NOT_HIGH_FIDELITY** for vehicle/error-correction scope. |
| A4 | **Popper/Deutsch:** a survived declared critical attempt is not confirmation. | complete \(C_0\) package; survived outcome selector; no full episode/capacity support. | \(\mathrm{I\_NA,R\_NA,H\_NA,R\_EQ\_NA,C\_SURV}\). | critical-package status \(\mathsf{SURVIVED\_DECLARED\_ATTEMPT}\). | \(\widehat E,\widehat{\mathrm{Cap}}\) absent; run **NE_EVIDENCE_NOT_CONFIRMATION** for \(\operatorname{Confirmed}\). |
| A5 | **Popper:** \(P_1\!\to TT\!\to EE\!\to P_2\) is a criticisable episode, not a generator theorem. | \(S_{\widehat E}\), without physical-realisation or capacity support. | \(\mathrm{I\_NA,R\_NA,H\_NA,R\_EQ\_NA,C\_REF}\). | \(\widehat E\). | \(\widehat{\mathrm{PhysExp}},\widehat{\mathrm{PhysRefExp}},\widehat{\mathrm{Cap}}\) absent; run **NE_P1_TT_EE_P2_NOT_GENERATOR**. |
| A6 | **Deutsch:** biological variation/selection and human conjecture/criticism have a typed common form, not identical mechanisms. | \(S_{\widehat{\mathrm{FallSel}}}\), \(S_{\widehat E}\), and \(\operatorname{PAT}_{VE}\). | \(\mathrm{I\_NA,R\_NA,H\_NA,R\_EQ\_NA,C\_REF}\). | \(\widehat{\mathrm{VE}}\). | run **NE_VARIATION_NOT_CONJECTURE_IDENTITY** for represented conjecture and theory-mediated criticism; neither is inferred from the closure head. |
| A7 | **Poietic kernel P5.6:** a coherent finite physical witness package yields a typed realisation map. | \(\{\mathrm{FIN},W_1,\ldots,W_5,\mathrm{COH}_5\}\), selected P5.6-map context, named port bridge. | \(\mathrm{I\_NA,R\_NA,H\_NA,R\_EQ\_NA}\); incomplete \(C\). | \(\widehat{\mathrm{P56}}_\exists\), then \(\widehat{\mathrm{Real}}_\exists\); a selected \(\widehat{\mathrm{Real}}\) only with its separate selection context. | \(\widehat{\mathrm{Core}},\widehat{\mathrm{Exp}},\widehat{\mathrm{Cap}}\) absent unless their independent supports are supplied. |

### A2-H-SCOPE countermodel obligation

A2 must not reuse **NE_WHOLE_CREATOR_NOT_CLONABLE**, because that frozen
countermodel deliberately has no \(H\) route. Instead it has this
case-specific, pre-registered source-scope obligation:

\[
M_{A2}\models
F=A\land\operatorname{Agent}(A)
\land\operatorname{HRep}_\eta(A,T,\epsilon)
\land\operatorname{HConseq}_\eta(A,T,\epsilon;w_\theta)
\land\neg\operatorname{WholeDigital}_B(A)
\land\neg\operatorname{WholeClone}_B(A)
\land\neg\operatorname{CreativeCap}_\eta(A,t).
\]

It is a model of the CTL condition’s stated scope: the digital/error-correcting
constraint is carried by the selected recipe variable and its copying task,
not by the whole declared self-reproducer; nor does that conditional
replication result establish explanatory capacity. The test result must name
this obligation **A2-H-SCOPE**, not a frozen non-entailment ID.
## Human verification sheet

For each case, fill this table before accepting it:

| field | entry to verify |
|---|---|
| case ID | A1–A7 |
| source ID and passage | source-register ID, chapter/section/page anchor |
| source statement | short paraphrase; any direct quotation remains within the source-register quotation policy |
| declared scope | boundary, candidate, cut, task, environment/domain, and exception clauses |
| supplied certificates | exact \(S_q\), selectors, joins, and witness context |
| closure result | \(\mathcal F(v;\varpi)\) and \(\operatorname{Display}(v)\) |
| required result | the “must derive” entry above |
| prohibited closure head | hatted head that must be absent from \(\mathcal F\), if applicable |
| semantic non-entailment check | named frozen \(\mathsf N\) obligation or explicitly pre-registered case-specific countermodel required for any non-head claim |
| test-independence class | construction-source, held-out authority, or empirical; only the second is out-of-sample source conformance |
| human finding | **SOURCE-LED CONFORMANCE MATCH**, **HELD-OUT CONFORMANCE MATCH**, **CHALLENGE**, **UNDER-SPECIFIED**, or **PROHIBITED-PROMOTION** |
| rationale | concise explanation, including any source-scope mismatch |

## Pass/fail semantics

A source-led conformance case passes only if all of the following hold:

\[
\text{required hatted head derived}
\;\land\;
\text{prohibited hatted head absent}
\;\land\;
\text{source scope preserved}
\;\land\;
\text{no unregistered bridge used}.
\]

A semantic prohibition is reported separately. It is `REGISTERED_SCHEMA` until
an annex-relative model certificate has been independently replayed; only then
may it be reported as `DISCHARGED_RELATIVE`. A source-led match never
confirms the import, source interpretation, or real-world creativity claim.

A mismatch is informative:

- **CHALLENGE** — the source requires a downstream result not licensed by the
  present calculus, or the calculus derives a result the source disallows.
- **UNDER-SPECIFIED** — the source claim needs a boundary, temporal,
  counterfactual, interpretation, or provenance condition not yet represented.
- **PROHIBITED-PROMOTION** — the calculus has crossed a frozen
  non-entailment guard. This is a blocking defect.
- **MATCH** — only the pre-registered scoped result is derived.

## Proposed genuinely held-out authority test

After the source-led suite, pre-register an eligible corpus, exclusions, and
selection procedure before the comparison passages are read. Exclusions must
cover every source, commentary, derivative note, and prior reading that
informed the construction. Select a stratified or random sample from that
corpus, record the selection, and keep the calculus, source register, annex,
and mapping grammar frozen during the comparison.

Use two independent roles:

1. a neutral extractor produces a typed semantic pin from each passage—its
   antecedent, consequent, modality, quantifier, boundary, task/environment,
   temporal/counterfactual conditions, and explicit exceptions—without seeing
   an expected calculus head; and
2. a separate mapper translates that pin to the fixed certificate vocabulary.
   If no faithful map exists, record `UNDER-SPECIFIED` rather than inventing a
   bridge.

The held-out suite must also be run against deliberately flawed copy-registers
that weaken an enumerated guard. It demonstrates discriminatory power only if
it accepts the frozen register while rejecting the appropriate mutants. This
still tests only the enumerated mutation catalogue; it does not substitute for
semantic pinning.

If the held-out authority exposes a gap, first record the gap, pin, mapping,
closure trace, and any model/counterexample. Only then decide whether a new
versioned calculus may be proposed. Do not silently tune a rule to make the
authority pass.

## Recommended next action

I recommend that you first review and either approve or alter SPA-v1 and the
scope of its first three finite certificates: population/FPT-H, externally
sequenced episode/capacity, and interface splicing. Only after those semantic
pins are frozen should the source-led A1–A7 cases run. The completed run should
produce:

1. a machine-readable premise/result table;
2. a human-readable derivation report for every case;
3. one deletion matrix for each derived head;
4. annex-relative model certificates and independent replay results; and
5. a separate mismatch register, even if it is empty.

That sequence derives a substantial set of downstream consequences while
keeping three questions distinct: whether the closure is implemented
correctly, whether a finite semantic countermodel is meaningful in its named
class, and whether a held-out authority pressures the frozen register.