# Admissibility Gate Audit v1

record_id: ADM-v1
version: 1.0
date: 2026-08-20
status: SEALED_ADMISSIBILITY_CLASSIFICATION_NO_N_DISCHARGE
official_file: ADMISSIBILITY_GATE_AUDIT_V1.md
plain_language_file: ADMISSIBILITY_GATE_AUDIT_V1_PLAIN_LANGUAGE.md
digest_manifest: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json
sha256_official: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json#official_sha256
sha256_plain_language: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: the three downstream formula sites that invoke Admissible_eta or FAdmissible
claims: classifies all three sites; makes the one bucket-2 restriction explicit; proves local two-sided independence of that restriction
non_claims: does not define source-level admissibility, discharge an original N-row, prove an annex-to-source bridge, validate creativity, or establish adequacy of the finite fragment

## 1. Question and counting rule

The question is whether an admissibility condition is derived from already
fixed axioms or stipulated, and, if stipulated, whether it already decides the
claim it is meant to help test.

This audit counts a **use** only when a downstream formula invokes the literal
predicate \(\operatorname{Admissible}_\eta\) or
\(\operatorname{FAdmissible}\) as a gate. The clause that defines
\(\operatorname{FAdmissible}\) is the basis for classifying its downstream
use; it is not counted as a fourth gate. Unrelated English uses of
"admissible" and other well-formedness predicates are outside this count.

The three buckets are:

1. **B1 — derived:** the gate follows from earlier stated axioms.
2. **B2 — stipulated but independent:** the restriction is explicit, and
   models satisfying the same restriction exist with the tested claim true
   and with it false.
3. **B3 — open:** the restriction is stipulated or uninterpreted, but the
   required independence result or semantic bridge is absent, or the gate is
   circular.

## 2. Complete classification and counts

| Use ID | Downstream site | Predicate | Bucket | Immediate effect |
|---|---|---|---|---|
| ADM-U1 | Calculus (12), `CAP_JOIN` | \(\operatorname{Admissible}_\eta(A,\mu)\) | B3 | permits the finite audit route to \(\widehat{\mathrm{Cap}}\) when the four capacity certificates are also supplied |
| ADM-U2 | Calculus (45), `CreativeCap` | \(\operatorname{Admissible}_\eta(A,\mu)\) | B3 | enters the source-level capacity predicate used by five \(\mathsf N\)-rows and one semantic control fixture |
| ADM-U3 | SPA-v1 Section 5.2, `FCreativeCap` | \(\operatorname{FAdmissible}(\mu)\) | B2 | restricts the finite policy contexts over which the four operational capacity queries are joined |

Therefore the exact downstream-use counts are

\[
\boxed{\#\mathrm{B1}=0,\qquad \#\mathrm{B2}=1,\qquad
\#\mathrm{B3}=2.}
\tag{ADM-C1}
\]

There is no derivation in the fixed calculus for either occurrence of
\(\operatorname{Admissible}_\eta(A,\mu)\), and there is no frozen bridge
identifying that source-level predicate with the annex predicate
\(\operatorname{FAdmissible}(\mu)\). The two source-level uses must therefore
remain B3.

## 3. Bucket-2 definition and numbered acceptance axiom

The bucket-2 restriction is stipulated for the named finite annex class. It is
not represented as a source theorem.

**Definition ADM-D1 (stipulated finite semantics).** This is the existing
SPA-v1 defining biconditional, now given an identifier for this audit. For
every well-typed finite policy context \(\mu=(a,s,\pi,q,t)\),

\[
\operatorname{FAdmissible}(\mu)
\Longleftrightarrow
\operatorname{Reach}(s_0,s)\land
\operatorname{range}(q)\subseteq\mathsf{Nodes}(\mathsf{Prov}).
\tag{ADM-D1}
\]

In SPA-v1, \(\mathsf{Selector}=\mathsf{Nodes}(\mathsf{Prov})\) and \(q\) is
already typed into \(\mathsf{Selector}\). The second conjunct is consequently
automatic in that fragment. Thus ADM-D1 presently reduces to reachability of
the context state. This is explicit and non-circular, but weak; no claim of
semantic adequacy is made for it.

**Acceptance Axiom ADM-A2 (non-selective, nonempty test domain).** This is a
new, numbered fixture-acceptance restriction of ADM-v1, not an axiom already
present in SPA-v1. For a finite fixture that uses admissibility to test capacity at
\((a,t)\), define

\[
\mathcal C^{\mathrm{adm}}_{a,t}
=\{\mu=(a,s,\pi,q,t):\mu\text{ is well typed over the fixed carriers and }
\operatorname{FAdmissible}(\mu)\}.
\tag{ADM-A2a}
\]

The fixture is admissible for that test only if

\[
0<|\mathcal C^{\mathrm{adm}}_{a,t}|<\infty
\tag{ADM-A2b}
\]

and it quantifies over exactly this complete set. Membership may not depend on
\(\operatorname{FEpi}\), any of the four
\(\operatorname{FCan\cdots}\) predicates,
\(\operatorname{FCreativeCap}\), or their negations. Equivalently, two
finite fragment structures with the same carriers, fixed \(s_0\), queried
\(t\), \(\mathsf{Time}_{A}\), reachability, policy tables, selector tables, and
provenance-node table have the same
\(\mathcal C^{\mathrm{adm}}_{a,t}\), whatever values their capacity tables
take. ADM-A2 is the numbered restriction required for the sole bucket-2 gate.

ADM-A2 prevents a negative fixture from winning merely by declaring that no
context is admissible, and prevents either result from being obtained by
filtering contexts after their capacity values are known.

## 4. The restriction does not decide the tested claim

**Theorem ADM-T1 (two-sided local independence).** Let
\(\mathfrak K_{\mathrm{ADM}}\) be the class of finite SPA-v1 fragment
structures that also satisfy ADM-A2. In that named audit subclass,

\[
\mathfrak K_{\mathrm{ADM}}\not\models
\operatorname{FCreativeCap}_{\mathcal A}(a,t)
\quad\text{and}\quad
\mathfrak K_{\mathrm{ADM}}\not\models
\neg\operatorname{FCreativeCap}_{\mathcal A}(a,t).
\tag{ADM-T1}
\]

**Finite witness pair.** Use the same admissibility reduct in both structures:

- one agent \(a\);
- states \(s_0,s_c,s_x,s_u,s_p\), with only \(s_0\) at time \(t\);
- edges \(g_c:s_0\to s_c\), \(g_x:s_0\to s_x\),
  \(g_u:s_x\to s_u\), and \(g_p:s_0\to s_p\);
- a singleton policy carrier, a singleton selector/provenance-node carrier
  \(\{u\}\), and the unique total tables \(\pi_0\) and
  \(q_0(s)=u\).

Then
\(\mathcal C^{\mathrm{adm}}_{a,t}=\{\mu_0\}\), where
\(\mu_0=(a,s_0,\pi_0,q_0,t)\), so both structures satisfy ADM-D1 and ADM-A2.

In \(M^-\), make every edge externally owned. No
\(\operatorname{TerminalOwnedEdge}(a,\ldots)\) exists. Each of the four
operational capacity clauses is false, hence
\(M^-\models\neg\operatorname{FCreativeCap}_{\mathcal A}(a,t)\).

In \(M^+\), make the four edges agent-owned and define the finite output
tables so that:

- \(g_c\) produces a non-seed candidate with defined ancestry;
- \(g_x\) produces an assessment with evidence;
- \(g_u\) is the selected agent-owned update edge, and the policy update is
  effective;
- \(g_p\) produces an A5 promotion; and
- the assessment, evidence, and selector all name \(u\), so not every selected
  target is external.

The four operational capacity clauses are then true for the same \(\mu_0\),
so \(M^+\models\operatorname{FCreativeCap}_{\mathcal A}(a,t)\).

The two structures agree on every admissibility-reduct and
membership-determining input fixed by ADM-D1 and ADM-A2. They differ only in
capacity-relevant ownership and output tables. This proves that the
stipulated admissibility restriction itself entails neither the positive nor
the negative capacity result.

ADM-T1 is only a local independence result for the finite annex predicate. It
is not an episode-versus-capacity fixture, a total model of the frozen source
theory, an annex-to-source bridge, or a discharge of an original
\(\mathsf N\)-row.

## 5. Bucket-3 consequences: affected rows are open

The source-level predicate \(\operatorname{Admissible}_\eta(A,\mu)\) has no
operational definition in the fixed calculus and no bridge from ADM-D1. A
model could otherwise make a source-level capacity denial cheap by setting
the predicate false, or make the positive audit gate cheap by stipulating it
true. Accordingly:

- the semantic status of \(\widehat{\mathrm{Cap}}\) is
  `OPEN_ADMISSIBILITY_B3`; its syntactic closure route remains defined;
- the \(\neg\operatorname{CreativeCap}\) face of the `ExternalRoutine`
  fixture used by `NC_RETENTION_WITHOUT_EXPLANATION` is
  `OPEN_ADMISSIBILITY_B3`; the six-coordinate closure vector is unchanged;
- the following five original rows remain `REGISTERED_SCHEMA [N]` and acquire
  the explicit substatus `OPEN_ADMISSIBILITY_B3`:

  1. `NE_INFORMATION_NOT_CREATIVITY`;
  2. `NE_RETENTION_NOT_CREATIVITY`;
  3. `NE_WHOLE_CREATOR_NOT_CLONABLE`;
  4. `NE_P1_TT_EE_P2_NOT_GENERATOR`;
  5. `NE_RECIPE_NOT_CREATIVITY`.

No row is being downgraded from a discharged result: the project had zero
discharged original rows before this audit and still has zero. "Open" means
that no semantic result may be claimed from those rows until a later version
pins source-level admissibility, proves its own non-circularity, supplies the
required total model and row bridge, and passes independent review.

## 6. Separate findings not counted as admissibility uses

The read-only audit also found two independent reasons that proposed future
rows remain open:

1. the finite H-route key names \((F,T,\mathcal R)\), but SPA-v1 does not yet
   bind the named \(F\) and \(T\) to the route witness's actual vehicle and
   implemented task; this independently keeps
   `NE_SELECTION_NOT_HIGH_FIDELITY` open; and
2. the physical bridge and terminal V-E, H, and capacity heads are stipulated
   or terminal rather than downstream semantic integrations; they cannot be
   treated as source-derived conclusions.

These findings are recorded here as open blockers only. This bounded audit
does not repair them or add new bridge axioms.

## 7. Result

The direct answer is:

- the finite annex admissibility gate is stipulated, not axiom-derived;
- its meaning is explicit as ADM-D1 and its test-domain restriction is the
  numbered acceptance axiom ADM-A2;
- ADM-T1 shows that those two audit conditions alone decide neither capacity nor
  non-capacity; and
- both source-level uses remain open because their meaning and their bridge to
  the finite restriction are not yet fixed.

This record changes no frozen source claim and discharges no original row.
