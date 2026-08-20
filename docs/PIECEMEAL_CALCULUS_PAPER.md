# A Piecemeal Premise Calculus for Physical and Epistemic Creativity Claims

## Method, formal architecture, and limits

### Abstract

This paper presents a finite, typed premise-consequence calculus for auditing
claims about the physical and epistemic conditions associated with creativity.
It is not a classifier of agents, and it does not settle the general question
of which systems are creative. Instead, it makes each proposed premise
explicit, records its authority and scope, and calculates exactly which
bounded audit conclusions follow from a supplied package of certificates.

The construction separates constructor-theoretic information (\(I\));
physically instantiated, role-coupled knowledge (\(R\)); a conditional
high-accuracy no-design replication route (\(H\)); variation and selection
(\(V\)); critical evidence (\(C\)); and the Popperian explanatory episode
(\(E\)). A finite signed premise package is closed under a finite rule
register. A countermodel register prevents familiar but invalid promotions:
information to knowledge, selection to criticism, survival of a test to
confirmation, or one historical episode to creative capacity. Missing
certificates yield non-establishment, not falsity or non-creativity.

The formal specification, source and licence record, and qualification ledger
are companion documents. This paper explains the method and reproduces the
central mathematical construction without reproducing lengthy source text.

**Keywords:** constructor theory; knowledge; creativity; conjecture and
criticism; variation and selection; evidence; countermodels; finite closure.

## 1. Aim and scope

A theory of creativity must say more than that a system produces surprising
outputs. It must constrain what physical systems can instantiate relevant
knowledge, what distinguishes a critical process from mere outcome
production, and what follows from particular evidence. Constructor theory of
information and knowledge bear on the physical question; Popper and Deutsch
bear on the epistemic one. The purpose of this calculus is to preserve those
distinctions while testing premise combinations exactly.

Its governing form is

\[
\text{declared premises}+\text{declared rules}
\quad\Longrightarrow\quad
\text{only their typed, finite consequences}.
\]

The conclusion is intentionally modest. The calculus does not define
creativity as self-reproduction, digitisation, information processing,
selection, a bare output, or a single problem-solving episode. Nor does it
deny creativity if one of those routes is absent. Its ordinary negative result
is \(\mathsf{NOT\_ESTABLISHED}\), not \(\mathsf{NON\_CREATIVE}\).

The physical picture has two joint aspects. Knowledge must be instantiated:
there must be a physical bearer and a physical role. Yet the role is not
exhausted by atom-tracking one token. A recipe or explanation can matter
through counterfactual relations among tasks, variants, environments, and
outcomes. This is a higher-level description of physical structure, not an
extra substance. Conversely, the possibility of a task does not show that a
candidate currently bears the knowledge required to perform it.

The authoritative formal artefact is
[PIECEMEAL_PREMISE_CALCULUS.md](PIECEMEAL_PREMISE_CALCULUS.md). The exact
primary sources, links, lawful short quotations, and licence notes are in
[PIECEMEAL_SOURCE_REGISTER.md](PIECEMEAL_SOURCE_REGISTER.md). The current
status of document qualification is in
[PIECEMEAL_CALCULUS_VERIFICATION.md](PIECEMEAL_CALCULUS_VERIFICATION.md).

## 2. Construction method

### 2.1 Freeze the experiment before calculating it

The construction begins with a frozen premise plan, not with an intended
verdict. The plan fixes 44 requirements, 13 negative controls, 20
non-entailment obligations, and four typed links. Its exact identifiers,
integrity hash, and scope are recorded in the
[Source Register](PIECEMEAL_SOURCE_REGISTER.md#what-this-register-is-for)
and the
[Verification Ledger](PIECEMEAL_CALCULUS_VERIFICATION.md#frozen-authority).

Freezing the alphabet prevents a premise from being quietly strengthened
after a result is seen, or a conclusion weakened until it appears to follow.
Every audit package is then a point in a finite space of supplied and
withheld certificates. The mathematical question becomes: which heads are
reachable from this package under the declared rule register?

### 2.2 Definitions, rules, theorems, bridges, and countermodels

The calculus uses five distinct kinds of assertion.

| Grade | Role | Permitted use |
|---|---|---|
| \(\mathsf D\) | Definition | Fix a sort, predicate, model class, or reporting term. |
| \(\mathsf P\) | Scoped import | Add a one-way result licensed by a named source or project kernel. |
| \(\mathsf B\) | Poietic bridge | Connect independently typed layers with extra assumptions exposed. |
| \(\mathsf T\) | Local theorem | State a consequence proved from the fixed calculus. |
| \(\mathsf N\) | Countermodel obligation | Require a model of an antecedent together with denial of a prohibited promotion. |

A claim is a definition when it fixes the domain over which later
propositions range, or when removing it changes the typed model class,
permits witness splicing, or changes the relevant countermodels. It need not
be a premise toggle. A claim is a rule when it directs a stated antecedent to
a stated conclusion. It becomes a theorem only if it is derived from the
already fixed definitions and rules. A connection motivated by several
sources but asserted by none of them in that combined form is a bridge.

This is also the criterion for retaining a load-bearing definition that does
not occur in an individual derivation. Boundaries, task types, bearer sorts,
and selected witnesses can be necessary for the grammar of a valid claim
without being varied by a finite premise experiment. Only conditions intended
to vary belong in the signed premise matrix.

### 2.3 Authority without argument from authority

The source register distinguishes a source definition or result from a
Poietic bridge and from an internal audit rule. It gives source identifiers,
chapter or section anchors, short lawful quotations or labelled paraphrases,
access links, and licence notes. The primary authorities are constructor
theory of information [CTI], constructor theory and physical knowledge
[CT_FOUNDATION], constructor theory of life [CTL], Deutsch on explanatory
creativity and emergence [DEUTSCH; FOR_EMERGENCE; FOR_REPLICATOR_NICHE;
FOR_GENE_STRUCTURE], and Popper [POPPER_LSCD; POPPER_CNR; POPPER_OK]. The
finite realisation import [KERNEL_P5_6] is explicitly project-internal.

The full bibliographic and reuse information is in the
[external primary sources table](PIECEMEAL_SOURCE_REGISTER.md#external-primary-sources)
and the
[evaluation and rule authority map](PIECEMEAL_SOURCE_REGISTER.md#equation-and-rule-authority-map).
A quotation is never used as a proof: the formal rule, grade, scope, and
countermodel obligation carry the mathematical burden.

## 3. Typed frame and six-lattice architecture

A calculation fixes a frame

\[
\eta=(\Phi,B,\mathcal E,H,\Delta^\ast,\mathcal T,\mathcal I,\Pi,t_0,t_1).
\]

Here \(\Phi\) is the law background; \(B\) the declared physical boundary;
\(\mathcal E\) an environment class; \(H\) actual history;
\(\Delta^\ast\) a finite intervention family; \(\mathcal T\) a task family;
\(\mathcal I\) an interpretation frame; and \(\Pi\) a provenance frame.
A context \(\theta\) supplies the candidate, tasks, bearers, code port,
population, evidence package, problem sequence, and physical-realisation
data. A witness context \(\varpi\) selects witnesses only from non-empty
witness families.

The distinction matters. A selected witness is fixed typing data, not a
certificate that may be borrowed from an unrelated boundary, task, or
history. Typed arrows and joins link information to its bearer, bearer to
evidence, and criticism to evidence. They block a superficially successful
conclusion assembled from incompatible tokens.

| Lattice | Requirements | Function |
|---|---:|---|
| \(I\) | 5 | Physical information variable; four unary conditions and one binary interoperability condition. |
| \(R\) | 13 | Instantiation, retention, recipe, history, causal role, and optional realisation equivalence. |
| \(H\) | 7 | Conditional no-design, high-accuracy self-reproduction route. |
| \(V\) | 5 | Population, inheritance, variation, selection, and fallibility. |
| \(C\) | 7 | Target, evidence channel, interpretation chain, auxiliaries, discriminator, protocol, and outcome. |
| \(E\) | 7 | \(P_1\), tentative theory, error elimination, revised problem, provenance, and fallibility. |

The separation is not cosmetic. An information medium is not thereby a
knowledge bearer; retained knowledge is not thereby explanatory creativity;
selection is not thereby theory-mediated criticism; and an explanatory
episode is not thereby general creative capacity.

### 3.1 Constructor-theoretic layers

The information lattice represents a declared physical variable with
distinct attributes and specified computation/permutation and cloning tasks:

\[
\operatorname{InfoVar}_{\Phi}(S_I,X_I;x_{I0}).
\]

It does not state that the whole candidate is clonable or digital. A separate
binary calculation is needed for interoperability, because it concerns a
pair of information media rather than an attribute of a lone candidate.

The knowledge lattice adds a physical bearer, a value, a task, suitable
environment conditions, a maintenance/retention route, counterfactual role
coverage, and an audit boundary. Its target has the general form

\[
\operatorname{PK}^{\rm cur}_{\eta}(b,k;X_I,T).
\]

The variables \(b,k,T,B,\mathcal E\) are part of the claim. Knowledge is
therefore neither a free-floating abstract recipe nor merely a static record.

The replication lattice is deliberately conditional. Only a declared
no-design, high-accuracy or indefinitely improvable self-reproduction route
imports the vehicle, recipe, digital-code, and error-correction package.
Digitality and error correction belong to the recipe architecture in that
route; they do not follow from selection, and they do not characterize every
creative system or every part of an agent.

### 3.2 Criticism, evidence, and evolutionary analogy

Variation and selection describe a fallible population process. Critical
evidence describes a different represented process. Observation, deduction,
and prediction become evidence only through a target, an interpretation
chain, auxiliary assumptions, a discriminator, and a predeclared protocol.
An instrument reading, an eye observation, or a derivation is theory laden
in this precise sense: its relation to an explanation is supplied by a chain
of theories about instruments, implementation, interpretation, and domain.

The epistemic episode has the form

\[
P_1\longrightarrow TT\longrightarrow EE\longrightarrow P_2,
\]

with problem, tentative theory, error elimination, and revised problem. A
refutation first applies to the declared conjunction of theory, auxiliaries,
interpretation, and protocol. A surviving attempt is therefore not a
confirmation result.

The calculus contains a typed bridge between fallible
variation/error-elimination and critical problem solving. It is not the
identity

\[
\text{variation}=\text{conjecture}
\qquad\text{or}\qquad
\text{selection}=\text{criticism}.
\]

Biological variants need not represent conjectures, and environmental
selection need not criticise a theory. The structural analogy remains useful
only when its type conditions are explicit.

## 4. The finite calculus

### 4.1 Provision states, rule heads, and closure

Let \(\mathcal P^{\rm mat}_{\eta,\theta}\) be the finite alphabet of material
certificates and typed selectors. A signed provision state is

\[
v:\mathcal P^{\rm mat}_{\eta,\theta}\longrightarrow\{+,-\},
\qquad
D(v)=\{a\in\mathcal P^{\rm mat}_{\eta,\theta}:v(a)=+\}.
\]

A plus sign means that a certificate has been supplied for this audit.
A minus sign means it has been withheld; it is not the semantic negation of
that certificate.

The finite target set contains hatted audit heads, such as \(\widehat I\),
\(\widehat{\mathrm{PK}}\), \(\widehat{\mathrm{RK}}\),
\(\widehat{\mathrm{Sel}}\), \(\widehat C\), \(\widehat E\),
\(\widehat{\mathrm{PhysExp}}\), and \(\widehat{\mathrm{Cap}}\). A hatted
head is distinct from its semantic denotation. This makes it possible to
distinguish a finite audit result from a complete world-description.

Each rule is a tuple

\[
r=(A_r,q_r,g_r,\sigma_r),
\]

where \(A_r\) is a finite antecedent, \(q_r\) a hatted head, \(g_r\) a grade,
and \(\sigma_r\) a selected-witness side condition. Representative rows are

\[
\begin{array}{rcl}
\mathrm{I\_APP}\land\bigwedge I_0&\Rightarrow&\widehat I,\\
\widehat I\land\mathrm{R\_APP}\land\bigwedge R_{\rm PK}\land J_{IR}
&\Rightarrow&\widehat{\mathrm{PK}},\\
\bigwedge V_0&\Rightarrow&\widehat{\mathrm{Sel}},\\
\bigwedge C_0&\Rightarrow&\widehat C,\\
\widehat C\land\bigwedge E_0\land\text{typed joins}
&\Rightarrow&\widehat E,\\
\widehat{\mathrm{FallSel}}\land\widehat E\land\operatorname{PAT}_{VE}
&\Rightarrow&\widehat{\mathrm{VE}}\quad[\mathsf B].
\end{array}
\]

The complete rule register, including guarded high-fidelity, realisation,
physical-explanatory, and capacity rows, is in equations (52) and (53) of
the formal calculus.

The closure is

\[
\begin{aligned}
\operatorname{Cl}_0(D;\varpi)&=D,\\
\operatorname{Cl}_{n+1}(D;\varpi)&=
\operatorname{Cl}_{n}(D;\varpi)\cup
\{q_r:A_r\subseteq\operatorname{Cl}_{n}(D;\varpi)
\ \text{and}\ \sigma_r(\varpi)\},\\
\mathcal F_{\eta,\theta}(v;\varpi)&=
\left(\bigcup_{0\le n\le|\mathcal Q_{\eta,\theta}|}
\operatorname{Cl}_{n}(D(v);\varpi)\right)
\cap\mathcal Q_{\eta,\theta}.
\end{aligned}
\]

This is a finite Horn closure. Since its head set is finite and steps only
add heads, it reaches a fixed point in at most
\(|\mathcal Q_{\eta,\theta}|\) head-addition stages. Removing a premise
therefore removes exactly the downstream heads whose declared route support
contains it.

The companion calculus states its local soundness result as

\[
q\in\mathcal F_{\eta,\theta}(v;\varpi)
\ \Longrightarrow\
\mathbb T_{\eta,\theta,\varpi}\cup D^\sharp(v)
\models\llbracket q\rrbracket_{\eta,\theta,\varpi}.
\]

This is soundness for the declared finite calculus, not a claim that its
certificates exhaust reality.

### 4.2 Binary information and route support

Interoperability has a distinct pair calculation on
\((\theta_1,\theta_2)\). Two unary information heads must first be derived;
then a declared compatibility certificate and composite applicability
selector may derive \(\widehat I_\otimes(\theta_1,\theta_2)\). If the
composite question is absent, the result is
\(\mathsf{NOT\_APPLICABLE}\). This prevents a unary test from silently
assuming facts about a second medium.

For every hatted head \(q\), the formal calculus supplies a transitive
audit-route support \(S_q\) and witness condition \(\sigma_q\):

\[
q\in\mathcal F_{\eta,\theta}(v;\varpi)
\quad\Longleftrightarrow\quad
S_q\subseteq D(v)\land\sigma_q(\varpi).
\]

The equality is exact for the closure route. It is not automatically a
semantic-minimality theorem about the physical phenomenon. Such a theorem
would need separate source-core and independence models showing that each
source-semantic condition is indispensable. That obligation is marked
\(\mathsf N\), not silently claimed.

### 4.3 Reported results

The primary report is

\[
\operatorname{Display}(v)=(\pi_I,\pi_R,\pi_H,\pi_V,\pi_C,\pi_E).
\]

Its principal values are \(\mathsf{MAY\_PASS}\),
\(\mathsf{NOT\_ESTABLISHED}\), and \(\mathsf{NOT\_APPLICABLE}\), supplemented
by scope-sensitive labels such as
\(\mathrm{EXTERNAL\_P\_NOT\_ATTRIBUTED}\) and
\(\mathrm{UNRESOLVED\_NOT\_NON\_CREATIVE}\). Interoperability and optional
multiple-realisation diagnostics are separate from the frozen six-vector.

There is deliberately no \(\mathrm{CONFIRMED}\) or
\(\mathrm{CREATIVITY\_PROVEN}\) output. A positive entry means that a stated
audit route is complete within the calculus, not that a universal claim about
a candidate has been established.

## 5. Physical explanatory episodes and capacity

A physical explanatory episode requires more than an impressive output.
The calculus requires a retained, attributed knowledge route; a closed
critical episode; a physically realised trace; typed links among bearer,
evidence, and criticism; and explicit alignment. The combined head is a
Poietic bridge because no cited authority independently states the whole
cross-layer conjunction.

This construction integrates the sources without erasing their differences.
Constructor theory constrains physical bearers and counterfactual tasks.
Popper constrains conjecture, criticism, refutation, and the limits of
confirmation. Deutsch motivates explanatory autonomy and the broad
evolutionary analogy. The bridge gives the explicit conditions under which an
audit may report a physically realised criticisable or refutational episode.

Creative capacity remains separate. It is a modal joint-capability predicate,
not the conclusion of one historical event. Thus a self-reproduction route,
selection history, retained recipe, or
\(P_1\to TT\to EE\to P_2\) episode does not by itself entail creative
capacity. This is enforced both by the rule register and by countermodels.

## 6. Countermodels and controls

Failure to derive a head says only that the current certificate package is
insufficient. To show an inference invalid, the calculus requires a model
family in which the alleged antecedent holds and the prohibited promotion
fails. This is the role of the 20 \(\mathsf N\)-obligations.

They include separations between:

- information and current physical knowledge;
- retained or recipe knowledge and explanatory capacity;
- selection and high-fidelity replication, digital error correction, or
  represented criticism;
- possible tasks and presently instantiated knowledge;
- one epistemic episode and a creative generator;
- a bare record, score, deduction, or prediction and critical evidence;
- survival of a declared test and confirmation;
- high-level causal role and a second substance;
- same-label substrate swapping and preservation of relevant task,
  side-effect, and environment conditions;
- finite observed theory, variant, or environment suites and all possible
  theories, variants, or environments.

The 13 negative controls are full signed provision states paired with typed
model fixtures. A transient information register, for example, can return
\(I=\mathsf{MAY\_PASS}\) while retention and epistemic coordinates remain
\(\mathsf{NOT\_ESTABLISHED}\). A complete critical package with an agreeing
outcome returns only
\(\mathrm{SURVIVED\_DECLARED\_ATTEMPT}\), not confirmation. The exact
thirteen vectors and the twenty model obligations are in the
[Verification Ledger](PIECEMEAL_CALCULUS_VERIFICATION.md#control-calculations)
and the
[formal calculus](PIECEMEAL_PREMISE_CALCULUS.md#6-countermodels-non-entailments-and-limits).

The controls are mathematical checks on the rule register, not empirical
refutations of real agents. They show that the calculus lacks an illicit
route to a stronger conclusion.

## 7. Verification boundary and reproduction

Verification has three layers: integrity of the frozen plan; static and
formal checks on the alphabet, rule routes, tags, links, controls, source
labels, and non-entailments; and read-only review of typing, scope, bridge
grading, non-splicing conditions, and route exactness. The
[Verification Ledger](PIECEMEAL_CALCULUS_VERIFICATION.md) is the sole
authoritative place for current command outputs, review verdicts, and
qualification statuses. It records the dated final document-qualification
results; this paper does not duplicate them.

A fully qualified document artefact would establish only the stated
properties of this finite construction. It would not establish that every
source interpretation is historically correct, that every possible model has
been considered, that a particular real-world agent is creative, or that
cited works carry a blanket reuse licence.

To reproduce a calculation:

1. Fix \((\eta,\theta,\varpi)\), including boundary, task, environment,
   evidence package, provenance frame, and selected witness data.
2. Choose a full signed provision state \(v\).
3. Compute \(\mathcal F_{\eta,\theta}(v;\varpi)\).
4. Apply \(\operatorname{Display}\) and inspect the provenance grade of each
   derived head.
5. Consult the source register for every \(\mathsf P\) and \(\mathsf B\)
   edge.
6. For a necessity or non-entailment claim, provide the independent
   source-core or countermodel obligation instead of relying on a failed
   route.

## 8. Conclusion

The piecemeal calculus is not an automated creativity detector. It is a
transparent calculus of permissible downstream claims. Its central
discipline is separation: information from knowledge, knowledge from
explanatory capacity, selection from criticism, outcome from evidence,
survival from confirmation, an episode from a generator, and higher-level
explanation from a second ontology.

That separation makes integration explicit rather than assumed. Physical
bearers, counterfactual roles, critical packages, explanatory episodes, and
provenance chains can be joined only by named, typed bridges. The finite
closure then shows what follows from adding or removing each audit
certificate, while countermodels prevent a missing route from being mistaken
for a negative verdict.

## References and companion records

The following are source identifiers, not reproduced source text. Full
bibliographic records, direct links, short lawful quotations, access
conditions, and licence information are in the
[Source Register](PIECEMEAL_SOURCE_REGISTER.md).

| Source ID | Work or record | Use here |
|---|---|---|
| CTI | Deutsch and Marletto, “Constructor theory of information” | Information variables, computation, cloning, interoperability. |
| CT_FOUNDATION | Deutsch, “Constructor Theory” | Physically instantiated knowledge, retention, and task scope. |
| CTL | Marletto, “Constructor theory of life” | Conditional no-design replication, vehicle, digital recipe, error correction. |
| DEUTSCH | Deutsch, *The Beginning of Infinity* | Conjecture, criticism, explanatory creativity, evolutionary analogy. |
| FOR_EMERGENCE | Deutsch, *The Fabric of Reality*, ch. 1 | Physically realised higher-level explanatory autonomy. |
| FOR_REPLICATOR_NICHE | Deutsch, *The Fabric of Reality*, ch. 8 | Bearer, niche, and counterfactual replicator role. |
| FOR_GENE_STRUCTURE | Deutsch, *The Fabric of Reality*, ch. 8 | One-copy and finite-domain guards. |
| POPPER_LSCD | Popper, *The Logic of Scientific Discovery* | Tests, auxiliaries, and scoped refutation. |
| POPPER_CNR | Popper, *Conjectures and Refutations* | Theory-laden observation and survival without confirmation. |
| POPPER_OK | Popper, *Objective Knowledge* | \(P_1\to TT\to EE\to P_2\). |
| KERNEL_P5_6 | [Poietic kernel v1.2](../subject/spark-poietic-layered-kernel-v1.2-purpose-guarded.md) | Scoped project-internal finite-realisation import. |

Companion artefacts:

- [Formal calculus](PIECEMEAL_PREMISE_CALCULUS.md)
- [Source and licence register](PIECEMEAL_SOURCE_REGISTER.md)
- [Verification ledger](PIECEMEAL_CALCULUS_VERIFICATION.md)
- [Frozen premise plan](../evidence/frozen/piecemeal-plan-v1.json)
- [Creativity and criticism provenance notes](../subject/provenance/the-creativity-criticism.md)
