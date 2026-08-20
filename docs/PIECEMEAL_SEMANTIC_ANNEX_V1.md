# Semantic Pinning Annex v1

record_id: SPA-v1
version: 1.0
date: 2026-08-20
status: SEALED_SEMANTIC_PINNING_SPECIFICATION_NO_N_DISCHARGE
official_file: PIECEMEAL_SEMANTIC_ANNEX_V1.md
plain_language_file: PIECEMEAL_SEMANTIC_ANNEX_V1_PLAIN_LANGUAGE.md
digest_manifest: PIECEMEAL_SEMANTIC_ANNEX_V1_FREEZE.json
sha256_official: PIECEMEAL_SEMANTIC_ANNEX_V1_FREEZE.json#official_sha256
sha256_plain_language: PIECEMEAL_SEMANTIC_ANNEX_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; evidence/frozen/piecemeal-plan-v1.json
scope: finite, named semantic fragment classes for future countermodels
claims: fixes operational meanings for selected finite fragments and requires class-relative reporting
non_claims: does not discharge an original N-row, prove any source import or bridge, or identify creativity in a real system

## Status, purpose, and non-claims

**Semantic-contract version:** `SPA-v1`
**Qualification status:** semantic-pinning specification only; no
non-entailment row is discharged by this document.
**Applies to:** the frozen `piecemeal-plan-v1` calculus, without changing its
44 premise requirements, 13 controls, 20 non-entailment identifiers, or four
typed links.

The finite calculus distinguishes a supplied audit certificate from its
semantic denotation. Its original model class is deliberately thin:

\[
\mathfrak M_{\eta,\theta,\varpi}=
\{M:M\text{ is sort-correct and }M\models\mathbb T_{\eta,\theta,\varpi}\}.
\]

That is sufficient for a finite closure calculation, but not for a
substantive physical or epistemic countermodel. A model cannot count as an
informative counterexample merely because it assigns an antecedent predicate
true and a conclusion predicate false.

This annex fixes a finite **fragment language** and its operational
interpretations. It is deliberately not claimed to be a subclass of the
original model class. A fragment structure has not yet interpreted every
primitive of \(\mathbb T_{\eta,\theta,\varpi}\), every imported principle, or
every fixed-witness judgment. A future certificate must supply a total
expansion \(\widehat M\) and independently verify

\[
\widehat M\models\mathbb T_{\eta,\theta,\varpi}.
\]

Only such an accepted expansion may be used in a class-relative discharge.
This avoids treating a partial finite structure as a model of the whole
calculus by fiat.

The annex does **not** claim that constructor theory, Popperian epistemology,
the Poietic kernel, or any bridge is true. It does **not** identify a real
creative agent. It specifies versioned, class-relative semantics in which
future countermodels can be constructed and independently checked.

The relevant source claims and their limits remain in the
[source register](PIECEMEAL_SOURCE_REGISTER.md). A semantic pin is an
explicit modelling choice unless a cited source itself supplies the relevant
constraint.

## 1. Two-axis status for \(\mathsf N\)-rows

Each non-entailment result has two independent statuses.

| Obligation status | Meaning |
|---|---|
| `UNREGISTERED` | No typed non-entailment formula has been frozen. |
| `REGISTERED_SCHEMA [N]` | A formula and intended countermodel schema are frozen, but no model has been accepted. |
| `MODEL_UNDER_CONSTRUCTION` | A candidate finite structure and derivation record exist but have not passed independent review. |
| `DISCHARGED_RELATIVE` | An explicit model certificate has passed the stated checks for one named annex version and model class. |

| Semantic-pinning status | Meaning |
|---|---|
| `UNPINNED` | The relevant primitive vocabulary may still be assigned freely subject only to the thin base theory. |
| `PARTIALLY_PINNED` | Some predicates have operational clauses, but the target claim or a required interface remains open. |
| `PINNED_CLASS_RELATIVE` | Every load-bearing primitive for the named class-relative result has a fixed interpretation in one named fragment. |
| `ADEQUACY_UNCLAIMED` | The class is operationally precise but has no claim of exhaustiveness, source equivalence, or physical universality. |

Thus a legitimate future result has the form

\[
\texttt{DISCHARGED\_RELATIVE}\bigl[
  \texttt{SPA-v1},\ \mathcal C,\ \operatorname{SHA256}(\text{annex})
\bigr],
\]

not an unqualified statement that a physical separation has been proved.

## 2. Fragment structures, expansions, and rigid frame data

Let \(\Sigma_{\mathrm{SPA}}\) be the finite signature defined in Sections
3–6. A finite fragment structure is

\[
M^{\flat}=(\mathcal K,\mathcal P,\mathcal H,\mathcal A,\mathcal J,\eta,\theta,\varpi),
\]

where:

- \(\mathcal K\) is a finite task/intervention structure;
- \(\mathcal P\) is a finite population-transition structure;
- \(\mathcal H\) is a finite replication-route structure;
- \(\mathcal A\) is a finite agent/episode transition structure;
- \(\mathcal J\) is a finite interface-and-composition structure; and
- \(\eta,\theta,\varpi\) are rigid declared constants, not freely changed
  between antecedent and conclusion.

Write \(\mathcal C^{\mathrm{SPA-v1}}_{\eta,\theta,\varpi}\) for the class
of fragment structures satisfying the exact clauses below. It is not given a
subset relation to \(\mathfrak M_{\eta,\theta,\varpi}\).

**Notation discipline.** Every operational predicate introduced by this
annex has a leading \(F\): for example \(\operatorname{FSel}\),
\(\operatorname{FEpi}\), and \(\operatorname{FCompOK}\). These are finite
fragment predicates, not the correspondingly named predicate of the frozen
calculus. A result about an original \(\mathsf N\)-row requires, in addition,
an explicit row bridge in a total expansion; no such bridge is supplied here.

A certificate that proposes a semantic discharge must instead provide a pair
\((M^{\flat},\widehat M)\) satisfying:

\[
\operatorname{Expand}_{\mathrm{SPA-v1}}(M^{\flat},\widehat M)
\Longleftrightarrow
\left\{
\begin{array}{l}
\widehat M\models\mathbb T_{\eta,\theta,\varpi},\\
\widehat M\text{ agrees with every }\Sigma_{\mathrm{SPA}}\text{ interpretation in }M^{\flat},\\
\widehat M\text{ contains the declared fixed witnesses and source/bridge assumptions.}
\end{array}\right.
\]

Existence of such an expansion is a certificate obligation, not an axiom of
this annex. Every certificate must include finite carrier sets, relation
tables, transition tables, all used primitive interpretations, and an
independent check of the expansion condition.

## 3. Shared task and intervention semantics

### 3.1 Finite task graphs and interventions

The task fragment is

\[
\mathcal K=(Q,\mathcal C,\Delta,\Phi,(D_C,f_C)_{C\in\mathcal C},
\mathsf{S}_{\mathrm{do}},
\mathsf{Succ}),
\]

where \(Q\), \(\mathcal C\), and \(\Delta\) are finite; \(\Phi\) is a
rigid declared law-background label; every task is a total function on its declared domain
\(f_C:D_C\to Q\) with \(D_C\subseteq Q\); and

\[
\mathsf{S}_{\mathrm{do}}:Q\times\Delta\to\{0,1\},\qquad
\mathsf{Succ}:Q\times\Delta\longrightarrow\mathcal P(Q)
\]

is a finite successor table. A certificate may invoke
\([\mathrm{do}_\delta]_\Phi\) only when the pair \((s,\delta)\) is declared
suitable and its table entry is nonempty. For nonempty \(U,V\subseteq Q\),

\[
\begin{aligned}
\operatorname{FFace}(C,U,V)
&\Longleftrightarrow U\subseteq D_C\ \land\ f_C[U]\subseteq V,\\
[\mathrm{do}_\delta]_\Phi\varphi(s)
&\Longleftrightarrow \mathsf{S}_{\mathrm{do}}(s,\delta)=1\land\mathsf{Succ}(s,\delta)\neq\varnothing\ \land\
\forall s'\in\mathsf{Succ}(s,\delta)\ \varphi(s').
\end{aligned}
\]

State-level single-valuedness is built into \(f_C\). Two input faces that
overlap at a physical state therefore cannot prescribe incompatible outputs
at that state. Empty successor sets never establish retention, causal role,
or a counterfactual result.

### 3.2 Finite local digital guard

Let \(\Sigma=(\sigma_1,\ldots,\sigma_n)\) be pairwise disjoint nonempty
subsets of \(Q\), and let \(\mathbf E=(E_1,\ldots,E_n)\) be declared error
sets. For one task \(C_\Sigma\), define

\[
\begin{aligned}
\operatorname{FRecover}(C_\Sigma,\Sigma,\mathbf E)
\Longleftrightarrow{}&
\bigwedge_{j=1}^n\operatorname{FFace}(C_\Sigma,\sigma_j,\sigma_j)\ \land\\
&\bigwedge_{i=1}^n[
\operatorname{FFace}(C_\Sigma,E_i,\sigma_i)\land
E_i\setminus\sigma_i\neq\varnothing],\\
\operatorname{FDG}_{\mathcal K}(C_\Sigma,\Sigma,\mathbf E)
\Longleftrightarrow{}&
\operatorname{FRecover}(C_\Sigma,\Sigma,\mathbf E).
\end{aligned}
\]

The associated finite lemma is:

\[
\operatorname{FRecover}(C_\Sigma,\Sigma,\mathbf E)
\Longrightarrow
\bigwedge_{i=1}^n
\left(E_i\setminus\bigcup_{j=1}^n\sigma_j\neq\varnothing\right).
\]

If \(z\in E_i\setminus\sigma_i\) lay in another \(\sigma_j\), then the
one partial function \(f_{C_\Sigma}\) would send \(z\) into both disjoint
cells \(\sigma_i\) and \(\sigma_j\). This is a local theorem about the
declared code and task only. It says nothing about whole-agent digitality,
clonability, or creativity.

## 4. Population-transition semantics

### 4.1 Finite causal-lineage structure

A finite population structure is

\[
\begin{aligned}
\mathcal P=(&\mathsf{Lineage},U,X,\mathsf{Boundary},\mathsf{Env},\mathsf{Time}_{P},\mathsf{Time}_{\mathsf{Evt}},\mathsf{Evt},\prec_c,
\mathsf{evt}_I,\mathsf{evt}_T,\mathsf{val},\mathsf{parent},N,\\
&\mathsf{viable},\mathsf{reinstates},\mathsf{Alt},\mathsf{SameBg},
\mathsf{Eq},\mathsf{Eval}).
\end{aligned}
\]

All carriers and tables are finite.  \(\mathsf{Lineage}\) is the finite
carrier of grounded lineage records, with typed projections

\[
\begin{array}{ll}
\pi_V,\pi_{V^+}:\mathsf{Lineage}\to\mathcal P_{\mathrm{fin}}(U),&
\pi_B:\mathsf{Lineage}\to\mathsf{Boundary},\\
\pi_E:\mathsf{Lineage}\to\mathsf{Env},&
\pi_\nu,\pi_\kappa,\pi_\delta,\pi_{\kappa_0}:\mathsf{Lineage}\to\mathsf{Evt},\\
\pi_{\equiv}:\mathsf{Lineage}\to\mathsf{Equiv}(X),&
\pi_{\sim_I}:\mathsf{Lineage}\to\mathcal P_{\mathrm{fin}}(X\times X).
\end{array}
\]

The typed tables are

\[
\begin{array}{ll}
\mathsf{Time}_{P}:U\to\mathbb N,&
\mathsf{Time}_{\mathsf{Evt}}:\mathsf{Evt}\to\mathbb N,\\
\mathsf{val}:\mathsf{Evt}\times U\to X,\\
\mathsf{evt}_I:U\to\mathsf{Evt},&
\mathsf{evt}_T:U\times U\rightharpoonup\mathsf{Evt},\\
\mathsf{parent}:U\rightharpoonup U,&
\mathsf{viable}:\mathsf{Evt}\times\mathsf{Env}\times U\to\{0,1\},\\
\mathsf{reinstates}:U\times X\to\{0,1\},&
\mathsf{Alt}:\mathsf{Evt}\to\mathcal P_{\mathrm{fin}}(\mathsf{Evt}),\\
\mathsf{SameBg}:\mathsf{Evt}^{4}\to\{0,1\},&
\mathsf{Eval}:\mathsf{Lineage}\times\mathsf{Evt}^{3}\to\mathcal P_{\mathrm{fin}}(U\times U).
\end{array}
\]

Here \(\prec_c\) is a time-respecting DAG on \(\mathsf{Evt}\), meaning
\(e\prec_c e^{\prime}\Longrightarrow\mathsf{Time}_{\mathsf{Evt}}(e)<\mathsf{Time}_{\mathsf{Evt}}(e^{\prime})\), and
\(N\subseteq U\times U\) is the actual continuation relation satisfying
\[
(u,u')\in N\Longrightarrow\mathsf{Time}_{P}(u)<\mathsf{Time}_{P}(u').
\]
\(\mathsf{Eq}\) is a finite deterministic structural-equation table.  When a
lineage \(\lambda\) is supplied, its declared evaluation is the actual
continuation aggregate
\[
\mathsf{Eval}_{\lambda}(\nu,\xi,\delta):=\mathsf{Eval}(\lambda,\nu,\xi,\delta)=
\{(u,u'):u\in V\land u'\in\operatorname{FCont}^{\xi}_{\lambda,\delta}(u)\}.
\]
The corresponding \(\mathsf{Eq}\) row is required to compute exactly this
finite set; it is not an independently selectable Boolean valuation.  Write
\(\preceq_c^*\) for the reflexive-transitive causal closure and \(N^+\) for
the strict transitive closure of \(N\).

A lineage is the typed record

\[
\lambda=(V,V^+,B,E,\nu,\kappa,\delta,\equiv_B,\sim_{\!I},\kappa_0)\in\mathsf{Lineage},
\]

with \(V,V^+\subseteq U\), boundary \(B\), environment \(E\), pairwise
distinct intervention/event tokens \(\nu,\kappa,\delta\in\mathsf{Evt}\), a
finite boundary equivalence \(\equiv_B\) on \(X\), an inheritance relation
\(\sim_{\!I}\subseteq X\times X\), and baseline
\(\kappa_0\in\mathsf{Alt}(\kappa)\).  For
\(\xi\in\{\kappa\}\cup\mathsf{Alt}(\kappa)\), set

\[
\operatorname{FCont}^{\xi}_{\lambda,\delta}(u)=
\{u'\in V^+:
\mathsf{parent}(u')\downarrow\land\mathsf{parent}(u')=u\land
(u,u')\in N\land\mathsf{evt}_T(u,u')\downarrow\land
\xi\preceq_c^*\mathsf{evt}_T(u,u')\land
\delta\preceq_c^*\mathsf{evt}_T(u,u')\land
\mathsf{viable}(\xi,E,u)=1\}.
\]

The finite predicates are:

\[
\begin{aligned}
\operatorname{FVariant}_{\lambda}
\Longleftrightarrow{}&
\exists u\neq v\in V\,[\nu\preceq_c^*\mathsf{evt}_I(u)\land
\neg\bigl(\mathsf{val}(\nu,u)\,\pi_{\equiv}(\lambda)\,\mathsf{val}(\nu,v)\bigr)],\\
\operatorname{FInherited}_{\lambda}
\Longleftrightarrow{}&
\forall u'\in V^+\ \exists u\in V\,[\mathsf{parent}(u')\downarrow\land
\mathsf{parent}(u')=u\land
(\mathsf{val}(\nu,u'),\mathsf{val}(\nu,u))\in\pi_{\sim_I}(\lambda)],\\
\operatorname{FCommonConstraint}_{\lambda}
\Longleftrightarrow{}&
\forall u\in V\ \mathsf{viable}(\kappa,E,u)\in\{0,1\}\land
\exists u\in V\,[\operatorname{FCont}^{\kappa}_{\lambda,\delta}(u)\neq
\operatorname{FCont}^{\kappa_0}_{\lambda,\delta}(u)],\\
\operatorname{FDifferentialContinuation}_{\lambda}
\Longleftrightarrow{}&
\exists u\neq v\in V\,[\operatorname{FCont}^{\kappa}_{\lambda,\delta}(u)\neq
\operatorname{FCont}^{\kappa}_{\lambda,\delta}(v)],\\
\operatorname{FLaterReinstantiation}(\lambda)
\Longleftrightarrow{}&
\exists u'\in V^+\ \exists w\in U\,[
(u',w)\in N^+\land\mathsf{Time}_{P}(w)>\mathsf{Time}_{P}(u')\land
\mathsf{reinstates}(w,\mathsf{val}(\nu,u'))=1].
\end{aligned}
\]

Causal effect is a same-background structural comparison:

\[
\begin{aligned}
\operatorname{FCausalAffects}_{\lambda}(\nu,\kappa,\delta)
\Longleftrightarrow{}&
\nu\preceq_c^*\kappa\land\kappa\preceq_c^*\delta\land
\mathsf{SameBg}(\nu,\kappa,\delta,\kappa_0)=1\land\\
&\mathsf{Eval}_{\lambda}(\nu,\kappa,\delta)\neq
\mathsf{Eval}_{\lambda}(\nu,\kappa_0,\delta).
\end{aligned}
\]

This makes both \(\kappa\) and \(\delta\) operational: the declared
intervention must occur on the same finite causal continuation path and its
profile must differ from the named same-background baseline.  The selection
fragment predicate is

\[
\begin{aligned}
\operatorname{FSel}_{\mathcal P}(\lambda)
\Longleftrightarrow{}&
|V|\ge2\land\operatorname{FVariant}_{\lambda}\land
\operatorname{FInherited}_{\lambda}\land\\
&\operatorname{FCommonConstraint}_{\lambda}\land
\operatorname{FDifferentialContinuation}_{\lambda}\land\\
&\operatorname{FCausalAffects}_{\lambda}(\nu,\kappa,\delta)\land
\operatorname{FLaterReinstantiation}(\lambda).
\end{aligned}
\]

### 4.2 Finite target-accuracy replication proxy

The original \(H\)-predicate is a scoped imported claim about no-design,
high or indefinitely improvable accuracy self-reproduction.  A finite table
cannot decide that unrestricted physical claim.  This annex uses the narrower
finite predicate \(\operatorname{FPT\text{-}HRoute}\), not
\(\operatorname{HRep}\).

The finite replication-route structure is

\[
\mathcal H=(\mathsf{Vehicle},\mathsf{Task},\mathsf{Protocol},
\mathsf{CodeFamily},\mathsf W,\mathsf{Word}_{(-)},\mathsf{Cells}_{(-)},
\mathsf{Encode}_{(-)},\mathsf{Output}_{(-)},\mathsf{hkey},
\mathsf{FPartOf},\mathsf{FCarries},\mathsf{FBlindCopy},
\mathsf{FErrorCorrect},\mathsf{FBuildWithResources},\mathsf{FImplements},
\mathsf{FOutput},\mathsf{FError}),
\]

where every carrier and table is finite.  \(\mathsf{Vehicle}\),
\(\mathsf{Task}\), and \(\mathsf{Protocol}\) are the finite carriers of
\(F\), \(T\), and \(\mathcal R\).  \(\mathsf{CodeFamily}\) is the finite
carrier of declared code-cell families.  For
\(\Sigma\in\mathsf{CodeFamily}\), the cells of that family are also denoted
\(\Sigma\), with finite word and output fibres
\(\mathsf{Word}_{\Sigma}\) and \(\mathsf{Output}_{\Sigma}\).  The dependent
code tables are

\[
\mathsf{Cells}_{\Sigma}:\mathsf{Word}_{\Sigma}\to
\mathcal P_{\mathrm{fin}}(\Sigma),\qquad
\mathsf{Encode}_{\Sigma}(p,\sigma)=1\Longleftrightarrow
\sigma\in\mathsf{Cells}_{\Sigma}(p).
\]

A finite witness carrier and its route key are

\[
\mathsf{hkey}:\mathsf W\to
\mathsf{Vehicle}\times\mathsf{Task}\times\mathsf{Protocol},
\qquad
\mathsf W_{\mathcal R}:=
\{w\in\mathsf W:\pi_3(\mathsf{hkey}(w))=\mathcal R\}.
\]

For every protocol \(\mathcal R\), write

\[
\mathcal R=(P_{\mathcal R},\operatorname{enum}_{\mathcal R},
\operatorname{err}_{\mathcal R},\operatorname{refine}_{\mathcal R},
N_{\mathcal R},\epsilon_{*,\mathcal R}),
\]

where \(P_{\mathcal R}\) is finite,
\(N_{\mathcal R},m_{\mathcal R}\in\mathbb N\),
\(\operatorname{enum}_{\mathcal R}:\{0,\ldots,m_{\mathcal R}\}\to
P_{\mathcal R}\),
\(\operatorname{err}_{\mathcal R}:P_{\mathcal R}\to[0,1]\cap\mathbb Q\),
and
\(\operatorname{refine}_{\mathcal R}:P_{\mathcal R}\times
\{0,\ldots,N_{\mathcal R}-1\}\rightharpoonup P_{\mathcal R}\).
Its completeness condition is

\[
\operatorname{FComplete}_{\mathcal R}
\Longleftrightarrow
P_{\mathcal R}=\operatorname{range}(\operatorname{enum}_{\mathcal R}).
\]

The implementation and output tables are dependent coproduct maps:

\[
\begin{aligned}
\mathsf{FImplements}:&
\coprod_{\mathcal R\in\mathsf{Protocol}}
(P_{\mathcal R}\times\mathsf W_{\mathcal R})\to\{0,1\},\\
\mathsf{FOutput}:&
\coprod_{\mathcal R\in\mathsf{Protocol}}
(P_{\mathcal R}\times\mathsf W_{\mathcal R})\to
\coprod_{\Sigma\in\mathsf{CodeFamily}}\mathsf{Output}_{\Sigma},\\
\mathsf{FError}:&
\coprod_{\Sigma\in\mathsf{CodeFamily}}
(\mathsf{Output}_{\Sigma}\times\mathsf{Word}_{\Sigma})\to
[0,1]\cap\mathbb Q.
\end{aligned}
\]

Whenever \(\mathsf{FOutput}(c,w)\) is evaluated, its value is required to
lie in \(\mathsf{Output}_{w.\Sigma}\).  Thus
\(\mathsf{FError}(\mathsf{FOutput}(c,w),w.p)\) is defined only on the
common code-family fibre; an output, word, or protocol from another route
cannot be spliced into the chain.

A route witness is

\[
\begin{aligned}
w={}&(w.V_{\mathrm{veh}},w.r,w.p,w.\Sigma,w.C_\Sigma,w.\mathbf E,w.E,
w.\mathbf c)\in\mathsf W,\\
&\mathsf{hkey}(w)=(F,T,\mathcal R),\quad
w.\Sigma\in\mathsf{CodeFamily},\quad
w.p\in\mathsf{Word}_{w.\Sigma},\quad
\mathsf{Cells}_{w.\Sigma}(w.p)\subseteq w.\Sigma,
\end{aligned}
\]

where \(w.\mathbf c=(c_0,\ldots,c_{N_{\mathcal R}})\).
The recovery family \(w.\mathbf E=(E_i)_i\) remains a separate argument of
\(\operatorname{FDG}_{\mathcal K}\); it is not a code-cell subset.  The
route data and chain are

\[
\begin{aligned}
\operatorname{FRouteData}(w)
\Longleftrightarrow{}&
\mathsf{FPartOf}(w.r,w.V_{\mathrm{veh}})=1\land
\mathsf{FCarries}(w.r,w.p)=1\land
w.p\in\mathsf{Word}_{w.\Sigma}\land\\
&\mathsf{Cells}_{w.\Sigma}(w.p)\subseteq w.\Sigma\land
\operatorname{FDG}_{\mathcal K}(w.C_\Sigma,w.\Sigma,w.\mathbf E)\land
\mathsf{FBlindCopy}(w,w.p,w.\Sigma)=1\land\\
&\mathsf{FErrorCorrect}(w,w.C_\Sigma,w.p,w.\Sigma)=1\land
\mathsf{FBuildWithResources}(w,w.V_{\mathrm{veh}},w.E)=1,\\
\operatorname{FProtocolChain}(w,\mathcal R)
\Longleftrightarrow{}&
w\in\mathsf W_{\mathcal R}\land
w.\mathbf c=(c_0,\ldots,c_{N_{\mathcal R}})\in
P_{\mathcal R}^{N_{\mathcal R}+1}\land
\bigwedge_{j\le N_{\mathcal R}}[
\mathsf{FImplements}(c_j,w)=1\land
\operatorname{err}_{\mathcal R}(c_j)=
\mathsf{FError}(\mathsf{FOutput}(c_j,w),w.p)]\land\\
&\bigwedge_{j<N_{\mathcal R}}[
\operatorname{refine}_{\mathcal R}(c_j,j)\downarrow\land
c_{j+1}=\operatorname{refine}_{\mathcal R}(c_j,j)\land
\operatorname{err}_{\mathcal R}(c_{j+1})<
\operatorname{err}_{\mathcal R}(c_j)]\land
\operatorname{err}_{\mathcal R}(c_{N_{\mathcal R}})
\le\epsilon_{*,\mathcal R}.
\end{aligned}
\]

Every true tuple must occur in the named table and pass its task-graph
coherence check.  Therefore an unrelated low-error chain cannot certify a
different carrier, word, copy route, or output.  Define

\[
\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R)
\Longleftrightarrow
\operatorname{FComplete}_{\mathcal R}\land
\exists w\in\mathsf W\,[\mathsf{hkey}(w)=(F,T,\mathcal R)\land
\operatorname{FRouteData}(w)\land
\operatorname{FProtocolChain}(w,\mathcal R)].
\]
This establishes a finite target-accuracy/refinement route only, never
indefinite improvability.  Exhaustive failure over the complete \(\mathcal R\)
yields only

\[
\operatorname{FSel}_{\mathcal P}(\lambda)\land
\neg\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R),
\]

not \(\neg\operatorname{HRep}_{\eta}(F,T,\epsilon)\).  A later connection
to the frozen selection/\(H\) row requires a separately justified adequacy
bridge for the named finite class.
## 5. Agent, episode, and modal-capacity semantics

### 5.1 Finite labelled transition system

A finite agent/episode structure is

\[
\begin{aligned}
\mathcal A=(&A,S,s_0,\Tau,\mathsf{Candidate},\mathsf{Assessment},\mathsf{Evidence},\mathsf{Outcome},\mathsf{Promotion},\mathsf{Policy},\mathsf{Selector},\mathsf{Edge},\mathsf{src},\mathsf{tgt},\to,
\mathsf{Kind},\mathsf{Owner},\mathsf{In},\mathsf{Out},\mathsf{Trace},\mathsf{Time}_{A},\\
&\mathsf{Pkg},\mathsf{Evid},\mathsf{Prov},\mathsf{Nodes},\mathsf{ProvEdge},
\mathsf{psrc},\mathsf{ptgt},\mathsf{RootKind},\mathsf{InputNodes},
\mathsf{EvidenceNode},\mathsf{OutcomeNode},\mathsf{Rev},\\
&\mathsf{FDerives},\mathsf{FInterprets},\mathsf{OutcomeSpace},
\mathsf{FSuitable},\mathsf{FIncompatible},\\
&\mathsf{Assess},\mathsf{AssessEvidence},\mathsf{Update},\mathsf{Select},\mathsf{Promote},\mathsf{Cand},\\
&\mathsf{NonSeed},\mathsf{Ancestry},\mathsf{A5},
\mathsf{CandidateOutput},\mathsf{AssessmentOutput},\mathsf{PromotionOutput},
\mathsf{PolicyUpdateOutput},\mathsf{AssessmentTarget},\mathsf{EvidenceTarget},
\mathsf{FExternalEveryTarget}).
\end{aligned}
\]

All carriers and tables are finite.  In particular,

\[
\begin{array}{ll}
\mathsf{src},\mathsf{tgt}:\mathsf{Edge}\to S,&
\mathsf{Owner}:\mathsf{Edge}\to A\cup\{\mathrm{external}\},\\
\mathsf{Trace}:\mathsf{Edge}\to\Tau,&
\mathsf{Time}_{A}:S\to\mathbb N,\\
\mathsf{Cand}:S\rightharpoonup\mathsf{Candidate},&
\mathsf{Ancestry}:\mathsf{Candidate}\rightharpoonup\mathcal P_{\mathrm{fin}}(\mathsf{Candidate}),\\
\mathsf{Assess}:S\rightharpoonup\mathsf{Assessment},&
\mathsf{AssessEvidence}:\mathsf{Assessment}\rightharpoonup\mathsf{Evidence},\\
\mathsf{Update}:\mathsf{Assessment}\times\mathsf{Policy}\times\mathsf{Selector}\times S\to\{0,1\},&
\mathsf{Select}:\mathsf{Selector}\times S\times S\rightharpoonup\mathsf{Edge},\\
\mathsf{Promote}:S\rightharpoonup\mathsf{Promotion},&
\mathsf{A5}:\mathsf{Promotion}\to\{0,1\},\\
\mathsf{CandidateOutput}:\mathsf{Edge}\rightharpoonup\mathsf{Candidate},&
\mathsf{AssessmentOutput}:\mathsf{Edge}\rightharpoonup\mathsf{Assessment},\\
\mathsf{PromotionOutput}:\mathsf{Edge}\rightharpoonup\mathsf{Promotion},&
\mathsf{PolicyUpdateOutput}:\mathsf{Edge}\to\{0,1\},\\
\mathsf{AssessmentTarget}:\mathsf{Assessment}\to\mathsf{Nodes}(\mathsf{Prov}),&
\mathsf{EvidenceTarget}:\mathsf{Evidence}\to\mathsf{Nodes}(\mathsf{Prov}),\\
\mathsf{InputNodes}:\Tau\to\mathcal P_{\mathrm{fin}}(\mathsf{Nodes}(\mathsf{Prov})),&
\mathsf{EvidenceNode}:\mathsf{Evidence}\to\mathsf{Nodes}(\mathsf{Prov}),\\
\mathsf{OutcomeNode}:\mathsf{Outcome}\to\mathsf{Nodes}(\mathsf{Prov}),&
\mathsf{Rev}:\Tau\times\mathsf{Outcome}\to\mathcal P_{\mathrm{fin}}(\mathsf{Edge}).
\end{array}
\]

For this fragment, \(\mathsf{Selector}=\mathsf{Nodes}(\mathsf{Prov})\); a selected target is therefore a provenance-addressable node.

The transition relation is not primitive prose:

\[
s\to s'\quad\Longleftrightarrow\quad
\exists g\in\mathsf{Edge}\,[\mathsf{src}(g)=s\land\mathsf{tgt}(g)=s'].
\]

Write \(\operatorname{Reach}(s,s')\) for its reflexive-transitive closure.
The nonempty owned-action relation is
\[
\operatorname{OwnedActionPath}(a,s,s')\Longleftrightarrow
\exists m\ge1\ \exists(g_1,\ldots,g_m)\in\mathsf{Edge}^{m}\,
[\mathsf{src}(g_1)=s\land\mathsf{tgt}(g_m)=s'\land
\bigwedge_{j<m}\mathsf{tgt}(g_j)=\mathsf{src}(g_{j+1})\land
\bigwedge_{j\le m}\mathsf{Owner}(g_j)=a].
\]
For a terminal edge token \(g\), define
\[
\operatorname{TerminalOwnedEdge}(a,s,s';g)\Longleftrightarrow
\exists m\ge1\ \exists(g_1,\ldots,g_m)\in\mathsf{Edge}^{m}\,
[g_m=g\land\mathsf{src}(g_1)=s\land\mathsf{tgt}(g)=s'\land
\bigwedge_{j<m}\mathsf{tgt}(g_j)=\mathsf{src}(g_{j+1})\land
\bigwedge_{j\le m}\mathsf{Owner}(g_j)=a].
\]
Thus a qualifying construction, appraisal, or promotion is produced by a
named terminal agent-owned edge; a static record at the initial state does
not count.

\(\mathsf{Prov}\) is a finite DAG with node carrier
\(\mathsf{Nodes}(\mathsf{Prov})\), edge carrier \(\mathsf{ProvEdge}\),
source/target maps \(\mathsf{psrc},\mathsf{ptgt}\), and
\(\mathsf{RootKind}:\mathsf{Nodes}(\mathsf{Prov})\to
\{\mathrm{seed},\mathrm{external},\mathrm{internal}\}\).
For a finite node set \(Y\), write \(\operatorname{Anc}_{\mathsf{Prov}}(Y)\)
for its backward closure.  It is provenance-closed exactly when every node
in that finite closure with no incoming provenance edge has root kind
`seed` or `external`.  This makes the upstream termination condition
explicit rather than an open historical narrative.

An episode token is the typed record

\[
e=(p_1,h,\chi,\omega,p_2,\tau),\qquad
\tau=(s_1,s_2,s_3,s_4),
\]

with ordered transitions \(s_1\to s_2\to s_3\to s_4\).  Its critical
package is the typed record

\[
\chi=(h,\Xi,\mathcal D,d,\rho,\mathcal I_\chi,o),
\]

whose fields are, respectively, target account, finite auxiliaries and
initial conditions, domain, discriminator, protocol, nonempty finite acyclic
interpretation graph, and declared outcome.  The package target is literally
its first field: \(\operatorname{Target}(\chi)=h\).  The episode predicates
are:

\[
\begin{aligned}
\operatorname{FCritPkg}(\chi)
\Longleftrightarrow{}&
\mathcal I_\chi\neq\varnothing\land d\in\rho\land
\mathsf{FDerives}(h,\Xi,d)=1\land o\in\mathsf{OutcomeSpace}(\rho),\\
\operatorname{FEvidenceLinked}(e,\chi)
\Longleftrightarrow{}&
\mathsf{Pkg}(e)=\chi\land\mathsf{Evid}(e)=\omega\land
\mathsf{FInterprets}(\mathcal I_\chi,\omega,o)=1,\\
\operatorname{FProvenanceClosed}(e)
\Longleftrightarrow{}&
\mathsf{InputNodes}(\tau)\neq\varnothing\land
\{\mathsf{EvidenceNode}(\omega),\mathsf{OutcomeNode}(o)\}\subseteq
\mathsf{InputNodes}(\tau)\subseteq\mathsf{Nodes}(\mathsf{Prov})\land\\
&\operatorname{Anc}_{\mathsf{Prov}}(\mathsf{InputNodes}(\tau))\text{ is provenance-closed},\\
\operatorname{FFallible}(e)
\Longleftrightarrow{}&
\exists o'\in\mathsf{OutcomeSpace}(\rho)\,[\mathsf{FSuitable}(\rho,o')=1\land
\mathsf{FIncompatible}(o',d)=1\land\\
&\exists g\in\mathsf{Rev}(\tau,o')\,[\mathsf{src}(g)=s_3\land
\operatorname{Reach}(\mathsf{tgt}(g),s_4)]],\\
\operatorname{FEpi}_{\mathcal A}(e)
\Longleftrightarrow{}&
\mathsf{Kind}(s_1)=P1(p_1)\land\mathsf{Kind}(s_2)=TT(p_1,h)\land\\
&\mathsf{Kind}(s_3)=EE(h,\chi,\omega)\land
\mathsf{Kind}(s_4)=P2(p_1,h,\chi,p_2)\land\\
&\operatorname{FCritPkg}(\chi)\land\operatorname{FEvidenceLinked}(e,\chi)\land
\operatorname{FProvenanceClosed}(e)\land\operatorname{FFallible}(e).
\end{aligned}
\]

The displayed tables are exhaustive over their stated finite carriers; their
rows, types, pointers, and graph closures are checked rather than selected as
later Boolean valuations.  A criticisable episode may have a survived,
disputed, or inconclusive test.  `CreativeGenerator` is outside this
fragment until a separate role-completeness semantics is frozen.

### 5.2 Capacity over agent-owned reachable control

A policy context is a finite tuple \(\mu=(a,s,\pi,q,t)\), where
\(a\in A\), \(\mathsf{Time}_{A}(s)=t\),
\(\pi:\{u:\operatorname{Reach}(s_0,u)\}\to\mathsf{Policy}\), and
\(q:\{u:\operatorname{Reach}(s_0,u)\}\to\mathsf{Selector}\) are total
finite tables.  Define

\[
\operatorname{FAdmissible}(\mu)
\Longleftrightarrow
\operatorname{Reach}(s_0,s)\land
\operatorname{range}(q)\subseteq\mathsf{Nodes}(\mathsf{Prov}).
\]

Write \(a_\mu,s_\mu,\pi_\mu,q_\mu,t_\mu\) for the projections of one
context.  Its external-target condition is the finite universal query

\[
\operatorname{FExternalEveryTarget}(a_\mu,\mu)=1
\Longleftrightarrow
\forall s',s''\in S\,[
\operatorname{Reach}(s_\mu,s')\land
\mathsf{Select}(q_\mu(s'),s',s'')\downarrow
\Longrightarrow
\mathsf{Owner}(\mathsf{Select}(q_\mu(s'),s',s''))=\mathrm{external}].
\]
The four capacity clauses are then exact finite queries:

\[
\begin{aligned}
\operatorname{FCanConstructNonSeed}(\mu)
\Longleftrightarrow{}&
\exists s',g,c\,[\operatorname{TerminalOwnedEdge}(a_\mu,s_\mu,s';g)\land
\mathsf{CandidateOutput}(g)=c=\mathsf{Cand}(s')\land
\mathsf{NonSeed}(c)=1\land\mathsf{Ancestry}(c)\downarrow],\\
\operatorname{FCanSustainConsequentialAppraisal}(\mu)
\Longleftrightarrow{}&
\exists s',s'',g,g',x\,[\operatorname{TerminalOwnedEdge}(a_\mu,s_\mu,s';g)\land
\mathsf{AssessmentOutput}(g)=x=\mathsf{Assess}(s')\land\\
&\mathsf{AssessEvidence}(x)\downarrow\land
\operatorname{TerminalOwnedEdge}(a_\mu,s',s'';g')\land
\mathsf{PolicyUpdateOutput}(g')=1\land
\mathsf{Update}(x,\pi_\mu,q_\mu,s'')=1],\\
\operatorname{FCanA5Promote}(\mu)
\Longleftrightarrow{}&
\exists s',g,p\,[\operatorname{TerminalOwnedEdge}(a_\mu,s_\mu,s';g)\land
\mathsf{PromotionOutput}(g)=p=\mathsf{Promote}(s')\land\mathsf{A5}(p)=1],\\
\operatorname{FCanDrawOnOwnedEvaluatedTarget}(\mu)
\Longleftrightarrow{}&
\exists s',s'',g,x\,[\operatorname{TerminalOwnedEdge}(a_\mu,s_\mu,s';g)\land
\mathsf{AssessmentOutput}(g)=x=\mathsf{Assess}(s')\land\\
&\mathsf{AssessEvidence}(x)\downarrow\land
\mathsf{AssessmentTarget}(x)=q_\mu(s')=
\mathsf{EvidenceTarget}(\mathsf{AssessEvidence}(x))\land\\
&\mathsf{Select}(q_\mu(s'),s',s'')\downarrow\land
\mathsf{Owner}(\mathsf{Select}(q_\mu(s'),s',s''))=a_\mu\land\\
&\mathsf{Update}(x,\pi_\mu,q_\mu,s'')=1\land
\mathsf{FExternalEveryTarget}(a_\mu,\mu)=0].
\end{aligned}
\]

Finally,

\[
\operatorname{FCreativeCap}_{\mathcal A}(a,t)
\Longleftrightarrow
\exists\mu=(a,s,\pi,q,t)\,[\operatorname{FAdmissible}(\mu)\land
\operatorname{FCanConstructNonSeed}(\mu)\land
\operatorname{FCanSustainConsequentialAppraisal}(\mu)\land
\operatorname{FCanA5Promote}(\mu)\land
\operatorname{FCanDrawOnOwnedEvaluatedTarget}(\mu)].
\]

An externally sequenced \(P_1\to TT\to EE\to P_2\) trace can satisfy
\(\operatorname{FEpi}\) while exhaustive finite context inspection finds no
single \(\mu\) satisfying all five capacity clauses.  This is a finite
class-relative fact, not a universal theory of creativity.
## 6. Interface and composition semantics

### 6.1 Typed interface structure

The finite interface structure is

\[
\begin{aligned}
\mathcal J=(&I,\mathsf{Boundary},\mathsf{Bearer},K,\Chi,E,\Omega,R,P,\Tau,
\mathsf{Problem},\mathsf{Account},\mathsf{Task},\mathsf{Environment},\mathsf{ProvFrame},\mathsf{ObligationFrame},\mathsf{AlignFrame},\mathsf{Program},\mathsf{Scope},\\
&\mathsf{Arrow}_{IR},\mathsf{Arrow}_{RE},\mathsf{Arrow}_{CE},
\mathsf{src}_{IR},\mathsf{tgt}_{IR},\mathsf{src}_{RE},\mathsf{tgt}_{RE},
\mathsf{src}_{CE},\mathsf{tgt}_{CE},\\
&\mathsf{key},\mathsf{PkgOf},\mathsf{EvidOf},\mathsf{omega},
\mathsf{trace}_E,\mathsf{trace}_R,\mathsf{iport},\mathsf{tport},\\
&\mathsf{p1}_E,\mathsf{hplus}_E,\mathsf{target}_E,\mathsf{target}_R,
\mathsf{succ}_E,\mathsf{succ}_R,\mathsf{environment}_E,\mathsf{prov}_E,\mathsf{frame},\mathsf{frameTask},\mathsf{frameLower},\mathsf{frameUpper},
\mathsf{program},\mathsf{program}_R,\mathsf{uses},\\
&\mathsf{scope},\mathsf{scopeBoundary},\mathsf{scopeTask},\mathsf{scopeEnvironment},\ell,\mathsf{Transport}).
\end{aligned}
\]

All carriers are finite and disjoint where their types require it.  The arrow
maps have the fixed types

\[
\begin{array}{lll}
\mathsf{src}_{IR}:\mathsf{Arrow}_{IR}\to I,&
\mathsf{tgt}_{IR}:\mathsf{Arrow}_{IR}\to\mathsf{Bearer}\times K,\\
\mathsf{src}_{RE}:\mathsf{Arrow}_{RE}\to\mathsf{Bearer}\times K,&
\mathsf{tgt}_{RE}:\mathsf{Arrow}_{RE}\to E,\\
\mathsf{src}_{CE}:\mathsf{Arrow}_{CE}\to\Chi,&
\mathsf{tgt}_{CE}:\mathsf{Arrow}_{CE}\to E.
\end{array}
\]

The remaining alignment maps have the declared types

\[
\begin{array}{ll}
\mathsf{PkgOf}:E\to\Chi,&\mathsf{EvidOf}:E\to\Omega,
\qquad\mathsf{omega}:\Chi\to\Omega,\\
\mathsf{trace}_E:E\to\Tau,&\mathsf{trace}_R:R\to\Tau,\\
\mathsf{iport}:E\to I\times\mathsf{Bearer}\times K,&
\mathsf{tport}:R\times P\to\mathsf{Bearer}\times K,\\
\mathsf{p1}_E,\mathsf{target}_E:E\to\mathsf{Problem},&
\mathsf{target}_R:R\to\mathsf{Problem},\\
\mathsf{hplus}_E,\mathsf{succ}_E:E\to\mathsf{Account},&
\mathsf{succ}_R:R\to\mathsf{Account},\\
\mathsf{environment}_E:E\to\mathsf{Environment},&
\mathsf{prov}_E:E\to\mathsf{ProvFrame},\\
\mathsf{frame}:E\times R\times P\to\mathsf{AlignFrame},&
\mathsf{frameTask}:\mathsf{AlignFrame}\to\mathsf{Task},\\
\mathsf{frameLower},\mathsf{frameUpper}:\mathsf{AlignFrame}\to\mathsf{ObligationFrame},&
\mathsf{program}:P\to\mathsf{Program},\\
\mathsf{program}_R:R\to\mathsf{Program},&
\mathsf{uses}:R\times P\to\{0,1\},\\
\mathsf{scope}:E\times R\times P\to\mathsf{Scope},&
\mathsf{scopeBoundary}:\mathsf{Scope}\to\mathsf{Boundary},\\
\mathsf{scopeTask}:\mathsf{Scope}\to\mathsf{Task},&
\mathsf{scopeEnvironment}:\mathsf{Scope}\to\mathsf{Environment}.
\end{array}
\]

The label map \(\ell\) may be non-injective.  Let

\[
\mathsf{Fld}=\{B,\tau,T,i,b,k,e,\mathcal E,\omega,\Pi,\Lambda,\Lambda',\eta\},
\]

with finite field carriers

\[
\begin{array}{cccccc}
D_B=\mathsf{Boundary},&D_\tau=\Tau,&D_T=\mathsf{Task},&D_i=I,&
D_b=\mathsf{Bearer},&D_k=K,\\
D_e=E,&D_{\mathcal E}=\mathsf{Environment},&D_\omega=\Omega,&D_\Pi=\mathsf{ProvFrame},\\
D_\Lambda=D_{\Lambda'}=\mathsf{ObligationFrame},&D_\eta=\mathsf{Scope}.
\end{array}
\]

Each key is a total dependent record
\(\mathsf{key}(a):\mathsf{Fld}\to\coprod_fD_f\), with
\(\operatorname{val}(\mathsf{key}(a),f)\in D_f\).  A typed identity
transport in \(\mathsf{Transport}\) preserves every field value; label
equality is never identity.

For \(\alpha,\zeta,\gamma\) of the IR, RE, CE arrow types respectively,
set

\[
\begin{aligned}
\operatorname{FCandidateTriple}(\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\alpha\in\mathsf{Arrow}_{IR}\land\zeta\in\mathsf{Arrow}_{RE}\land
\gamma\in\mathsf{Arrow}_{CE},\\
\operatorname{FKeyMatch}(\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\forall f\in\mathsf{Fld}\,[
\operatorname{val}(\mathsf{key}(\alpha),f)=\operatorname{val}(\mathsf{key}(\zeta),f)\land
\operatorname{val}(\mathsf{key}(\zeta),f)=\operatorname{val}(\mathsf{key}(\gamma),f)],\\
\operatorname{FKeyPayload}(\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\operatorname{val}(\mathsf{key}(\alpha),i)=\mathsf{src}_{IR}(\alpha)=
\pi_I(\mathsf{iport}(\mathsf{tgt}_{RE}(\zeta)))\land\\
&\operatorname{val}(\mathsf{key}(\alpha),b)=\pi_{\mathsf{Bearer}}(\mathsf{tgt}_{IR}(\alpha))=
\pi_{\mathsf{Bearer}}(\mathsf{src}_{RE}(\zeta))\land\\
&\operatorname{val}(\mathsf{key}(\alpha),k)=\pi_K(\mathsf{tgt}_{IR}(\alpha))=
\pi_K(\mathsf{src}_{RE}(\zeta))\land\\
&\operatorname{val}(\mathsf{key}(\alpha),e)=\mathsf{tgt}_{RE}(\zeta)=
\mathsf{tgt}_{CE}(\gamma)\land\\
&\operatorname{val}(\mathsf{key}(\alpha),\tau)=
\mathsf{trace}_E(\mathsf{tgt}_{RE}(\zeta))\land
\operatorname{val}(\mathsf{key}(\alpha),\mathcal E)=
\mathsf{environment}_E(\mathsf{tgt}_{RE}(\zeta))\land\\
&\operatorname{val}(\mathsf{key}(\alpha),\omega)=
\mathsf{EvidOf}(\mathsf{tgt}_{CE}(\gamma))=
\mathsf{omega}(\mathsf{src}_{CE}(\gamma))\land
\operatorname{val}(\mathsf{key}(\alpha),\Pi)=
\mathsf{prov}_E(\mathsf{tgt}_{RE}(\zeta)),\\
\operatorname{FJOIN}_{IRRE}(\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\operatorname{FCandidateTriple}(\alpha,\zeta,\gamma)\land
\mathsf{tgt}_{IR}(\alpha)=\mathsf{src}_{RE}(\zeta)\land
\mathsf{tgt}_{RE}(\zeta)=\mathsf{tgt}_{CE}(\gamma)\land\\
&\operatorname{FKeyMatch}(\alpha,\zeta,\gamma)\land
\operatorname{FKeyPayload}(\alpha,\zeta,\gamma),\\
\operatorname{FJOIN}_{CE}(\gamma)
\Longleftrightarrow{}&
\mathsf{PkgOf}(\mathsf{tgt}_{CE}(\gamma))=\mathsf{src}_{CE}(\gamma)\land
\mathsf{EvidOf}(\mathsf{tgt}_{CE}(\gamma))=
\mathsf{omega}(\mathsf{src}_{CE}(\gamma)),\\
\operatorname{FLinked}(\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\operatorname{FJOIN}_{IRRE}(\alpha,\zeta,\gamma).
\end{aligned}
\]

`FLinked` preserves the frozen IR–RE–CE/IRRE face; the distinct
package/evidence condition is required by full composition.

### 6.2 Physical-episode alignment and no-splicing

The maps \(\mathsf{iport}:E\to I\times\mathsf{Bearer}\times K\) and
\(\mathsf{tport}:R\times P\to\mathsf{Bearer}\times K\) deliberately have
different arities.  For \(e\in E,r\in R,p\in P\), define

\[
\begin{aligned}
\operatorname{FPEALIGN}_\eta(e,r,p;\alpha,\zeta,\gamma)
\Longleftrightarrow{}&
\mathsf{trace}_E(e)=\mathsf{trace}_R(r)=
\operatorname{val}(\mathsf{key}(\alpha),\tau)\land\\
&\pi_I(\mathsf{iport}(e))=\mathsf{src}_{IR}(\alpha)=
\operatorname{val}(\mathsf{key}(\alpha),i)\land\\
&\pi_{\mathsf{Bearer}\times K}(\mathsf{iport}(e))=\mathsf{tport}(r,p)=
\mathsf{tgt}_{IR}(\alpha)=\mathsf{src}_{RE}(\zeta)\land\\
&\mathsf{p1}_E(e)=\mathsf{target}_E(e)=\mathsf{target}_R(r)\land
\mathsf{hplus}_E(e)=\mathsf{succ}_E(e)=\mathsf{succ}_R(r)\land\\
&\mathsf{uses}(r,p)=1\land\mathsf{program}(p)=\mathsf{program}_R(r)\land
\mathsf{frameTask}(\mathsf{frame}(e,r,p))=
\operatorname{val}(\mathsf{key}(\alpha),T)\land\\
&\mathsf{frameLower}(\mathsf{frame}(e,r,p))=
\operatorname{val}(\mathsf{key}(\alpha),\Lambda)\land
\mathsf{frameUpper}(\mathsf{frame}(e,r,p))=
\operatorname{val}(\mathsf{key}(\alpha),\Lambda')\land\\
&\mathsf{scope}(e,r,p)=\eta=\operatorname{val}(\mathsf{key}(\alpha),\eta)\land
\mathsf{scopeBoundary}(\eta)=\operatorname{val}(\mathsf{key}(\alpha),B)\land
\mathsf{scopeTask}(\eta)=\operatorname{val}(\mathsf{key}(\alpha),T)\land
\mathsf{scopeEnvironment}(\eta)=\operatorname{val}(\mathsf{key}(\alpha),\mathcal E)\land\\
&\mathsf{prov}_E(e)=\operatorname{val}(\mathsf{key}(\alpha),\Pi)\land
\mathsf{tgt}_{RE}(\zeta)=e=\mathsf{tgt}_{CE}(\gamma),\\
\operatorname{FCompOK}_\eta(\alpha,\zeta,\gamma;e,r,p)
\Longleftrightarrow{}&
\operatorname{FLinked}(\alpha,\zeta,\gamma)\land
\operatorname{FJOIN}_{CE}(\gamma)\land
\operatorname{FPEALIGN}_\eta(e,r,p;\alpha,\zeta,\gamma).
\end{aligned}
\]

The retained \(i\)-coordinate of \(\mathsf{iport}(e)\) is bound to the IR
arrow, separately from the \((b,k)\)-port equality.  Environment, evidence,
provenance, alignment-frame, program, trace, boundary, task, and scope faces
are all explicit.  This is a finite fragment of the frozen PEALIGN relation:
it can support a later row bridge only if that bridge identifies these records
with the corresponding \((T,\Lambda,\Lambda',J_\Lambda,F_\beta)\) objects in
one total expansion.  The no-splicing condition is local, never global:

\[
\begin{aligned}
\forall(\alpha,\zeta,\gamma)\,[&
\operatorname{FCandidateTriple}(\alpha,\zeta,\gamma)\land
\neg\operatorname{FKeyMatch}(\alpha,\zeta,\gamma)]\\
&\Longrightarrow
\neg\operatorname{FJOIN}_{IRRE}(\alpha,\zeta,\gamma)\land
\neg\operatorname{FLinked}(\alpha,\zeta,\gamma).
\end{aligned}
\]

A mismatch in an unrelated triple cannot invalidate a valid link elsewhere.
Two adversarial certificates are mandatory before an interface-dependent
fragment result is called tested:

1. `IC-SP-001` has individually valid arrows but a key mismatch in the
   proposed triple.  It establishes three arrow records but
   \(\neg\operatorname{FJOIN}_{IRRE}\) and \(\neg\operatorname{FLinked}\).
2. `IC-SP-002` has valid arrows, `FJOIN_IRRE`, `FJOIN_CE`, and `FLinked` for
   one episode, but pairs it with an independently valid realization whose
   trace, retained information token, or terminal knowledge-port token
   differs—even when display labels agree.  It establishes
   \(\neg\operatorname{FPEALIGN}_\eta\) and
   \(\neg\operatorname{FCompOK}_\eta\).

Both outcomes withhold a physical explanatory audit head as
`NOT_ESTABLISHED`; neither derives its negation.  Label/sort-compatibility
mutants test the guard's sensitivity, not adequacy of the pins.
## 7. Freeze, certificate, and mutation protocol

### 7.1 Freeze before model construction

Before a countermodel is constructed, record

\[
(\text{annex ID},\ \text{annex SHA-256},\ \text{calculus SHA-256},\
\text{frozen-plan SHA-256},\ \text{target \(\mathsf N\)-rows},\
\text{model-class ID}).
\]

No semantic clause, target row, or expected result may change while a model
is under review. A revision creates `SPA-v2`; it cannot silently alter an
`SPA-v1` result.

### 7.2 Fixture status versus row discharge

A finite result with items 1–6 below is a
`VERIFIED_FIXTURE [SPA-v1]`. It establishes only the stated finite fragment
formula. It must include:

1. the exact \(\mathsf N\)-formula and its finite fragment replacement, if
   any;
2. annex version and digest, calculus and frozen-plan digests;
3. finite carrier sets, transition tables, task graphs, interface records,
   and all fragment interpretations used;
4. a derivation of the antecedent and denied fragment conclusion from the
   finite structures, not a negative valuation;
5. the boundary, environment, resource, time, and provenance scope; and
6. an independent replay/check result.

A `DISCHARGED_RELATIVE` result requires everything above **plus**:

7. a total expansion \(\widehat M\), together with an independent check that
   \(\widehat M\models\mathbb T_{\eta,\theta,\varpi}\); and
8. an explicit row bridge showing how the fragment formula relates to the
   original \(\mathsf N\)-row in that same \(\widehat M\).

Without items 7–8, it must be reported only as

> verified fixture under `SPA-v1` over the named finite model class.

After all eight requirements pass, the permitted report phrase is

> discharged relative to `SPA-v1` over the named finite model class.

Both phrases must name the annex digest and model-class identifier. Neither
may be shortened to “the physical non-entailment is proved.”

### 7.3 What mutation testing can and cannot show

Mutation tests answer a different question from semantic pinning. They test
whether an evaluator detects a pre-enumerated defect catalogue. Required
mutants include:

- information \(\Rightarrow\) knowledge;
- local digital code \(\Rightarrow\) whole-agent digitality;
- survived attempt \(\Rightarrow\) confirmation;
- typed variation analogue \(\Rightarrow\) identity with conjecture and
  criticism;
- episode \(\Rightarrow\) capacity; and
- interface-key equality weakened to sort or label compatibility.

An additional **semantic-annex mutant** is a named restricted class, not an
open displayed schema:

\[
\mathcal C^{\mathrm{SPA\text{-}v1+H}}=
\{\mathcal M\in\mathcal C^{\mathrm{SPA\text{-}v1}}:
\forall\lambda\in\mathsf{Lineage}\ \forall F\in\mathsf{Vehicle}\ \forall T\in\mathsf{Task}\ \forall\mathcal R\in\mathsf{Protocol}\,
[\operatorname{FSel}_{\mathcal P}(\lambda)\Longrightarrow
\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R)]\}.
\]

The intended target
\(\operatorname{FSel}_{\mathcal P}(\lambda)\land
\neg\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R)\) has no member of this
mutant class.
The harness must report `PINNING_OVERSTRENGTH` when this added axiom makes the
intended target
\(\operatorname{FSel}_{\mathcal P}(\lambda)\land
\neg\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R)\) inconsistent, not
a successful countermodel.  Mutant rejection demonstrates sensitivity to the
enumerated mutations only.  It does not demonstrate that every relevant
predicate has been pinned or that the class is physically adequate.
## 8. First bounded follow-up

The next implementation task is intentionally narrow:

1. freeze this annex and record its digest;
2. construct one finite population-transition certificate for
   \(\operatorname{FSel}_{\mathcal P}(\lambda)\land
   \neg\operatorname{FPT\text{-}HRoute}(F,T;\mathcal R)\);
3. construct one finite externally sequenced episode certificate for
   \(\operatorname{FEpi}_{\mathcal A}(e)\land
   \neg\operatorname{FCreativeCap}_{\mathcal A}(a,t)\);
4. construct `IC-SP-001`, `IC-SP-002`, and their label/sort-compatibility
   mutants; and
5. provide the total expansion, row bridge, and independent check before changing a fixture status to `DISCHARGED_RELATIVE`.

Those certificates will test a pinned fragment rather than merely exploit an
uninterpreted vocabulary. They remain class-relative and cannot upgrade an
original frozen \(\mathsf N\)-row without the separately justified bridge.