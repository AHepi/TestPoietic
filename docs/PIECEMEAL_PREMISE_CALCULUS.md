# Piecemeal Premise Calculus

## A typed finite-premise calculus for scoped creativity claims

This document reconstructs the requested **premise-combination calculus**.  It
does not classify a system as creative, and it does not turn a finite suite of
cases into an enumeration of all theories.  Its output is a finite, typed
closure calculation:

\[
\mathcal F_{\eta,\theta}(v;\varpi)
 =\bigcup_{0\le n\le|\mathcal Q_{\eta,\theta}|}\operatorname{Cl}_n(D(v);\varpi)
   \cap\mathcal Q_{\eta,\theta}.
\tag{0}
\]

Here \(v\) is a finite package of **supplied audit certificates**, not a
complete description of reality.  A missing certificate means
\(\textsf{NOT\_ESTABLISHED}\), never the negation of the claim and never
\(\textsf{NON\_CREATIVE}\).

The source and verification record for every imported claim is in
[PIECEMEAL_SOURCE_REGISTER.md](PIECEMEAL_SOURCE_REGISTER.md); the complete
run ledger is in [PIECEMEAL_CALCULUS_VERIFICATION.md](PIECEMEAL_CALCULUS_VERIFICATION.md).

### Grades

Every source import, bridge, and derived inference has exactly one primary
grade.  Every displayed biconditional introduced by "define" or "let" is a
\(\mathsf D\) definition by convention, whether or not its marker is repeated
inline.  Tuple formation, set enumeration, and other purely structural syntax
are explicitly ungraded notation.

\[
\mathsf D=\text{definition},\qquad
\mathsf T=\text{locally proved theorem},\qquad
\mathsf P=\text{scoped imported result},\qquad
\mathsf B=\text{explicit Poietic bridge},\qquad
\mathsf N=\text{countermodel/non-entailment obligation}.
\tag{0a}
\]

A definition fixes a model class or a term.  An import or bridge is
one-directional.  A theorem has a proof in the preceding fixed theory.
Consequently the closure report distinguishes:

\[
\text{route failure}\ne\neg\text{source claim}\ne\neg\text{creativity}.
\tag{0b}
\]

The grade of a derived head is its **provenance set**
\(\operatorname{Ann}(q)\), defined in Section 5; it is not overwritten by the
grade of its last local inference.

---

## 1. Typed frame, ground contexts, and the frozen alphabet

Fix a finite frame

\[
\eta=(\Phi,B,\mathcal E,H,\Delta^\ast,\mathcal T,\mathcal I,\Pi,t_0,t_1).
\tag{1}
\]

\(\Phi\) is the law background; \(B\) is the declared physical boundary;
\(\mathcal E\) is the environment class; \(H\) is actual history;
\(\Delta^\ast\) is a finite family of suitable interventions;
\(\mathcal T\) is a finite task family; \(\mathcal I\) is the interpretation
frame; and \(\Pi\) is the provenance frame.

A unary calculation fixes the following fully typed context:

\[
\begin{aligned}
\theta=(&F,T,\epsilon;\\
 S_I,X_I,x_{I0};\\
 b,i,k;\\
 r,p_{\rm code},S_\Sigma,\Sigma,x_{\Sigma0},\mathbf e,
 V_{\rm veh},c,b_c,\mathcal C_\Sigma;\\
&\alpha,\zeta,\gamma;\\
 \mathcal V,\mathcal V^+,\iota,\nu,\kappa,\delta,\lambda;\\
 \chi,e,r_e,r_\lambda,\mathbb V,
 s_{TT},s_\chi,s_{EE},s_{P2};\\
&p_1,h,h^+,p_2,\mathcal D_\chi;\\
 \tau,\mathcal K_{\le t},\Gamma,\mathbb P_\Sigma,\mathcal R_{\Gamma,\Sigma},P_\Sigma,R,w_0,g_1,g_2,g_3,g_4,w_1,w_2,w_3,w_4,w_5,
 J_\Lambda,F_\beta,\Lambda,\Lambda';\\
&A,t,\mu,B_{\rm ext})\in\Theta_\eta .
\end{aligned}
\tag{2}
\]

The required sorts are:

\[
\begin{array}{rcl}
F&:&\text{candidate constructor or declared self-reproducer},\\
T&:&\text{task},\qquad \epsilon:\text{accuracy parameter},\\
p_{\rm code}&=&\operatorname{code}_\Sigma(r)\in\Sigma^\ast,\\
\mathcal K_{\le t}&:&\text{the fixed finite Spark cut, with }\operatorname{TraceOf}(\mathcal K_{\le t})=\tau,\\
\Gamma&:&\text{the P5.6 realization frame for that cut},\\
\mathbb P_\Sigma&:&\text{a physical ecology for the declared finite cut/frame},\\
\mathcal R_{\Gamma,\Sigma}&:&\text{a typed map }\mathbb P_\Sigma\rightharpoonup\mathcal K_{\le t},\\
P_\Sigma&:&\text{the declared program port, distinct from }\mathbb P_\Sigma,\\
p_1,p_2&:&\text{problems, not code values},\\
V_{\rm veh}&:&\text{vehicle/program constructor},\\
\mathcal V,\mathcal V^+&:&\text{populations in }
 \lambda=(\mathcal V,\mathcal V^+,\iota,\nu,\kappa,\delta,t_0,t_1),\\
\alpha:i\to k,\quad\zeta:k\to e,\quad\gamma:\chi\to e
&:&\text{typed linking arrows},\\
\mathbf e=(e_1,\ldots,e_n)&:&\text{recovery domains of }\mathcal C_\Sigma,\\
r_e,r_\lambda&:&\text{role maps into the common skeleton }\mathbb V,\\
(s_{TT},s_\chi,s_{EE},s_{P2})&:&\text{designated stages of }e,\\
(g_j,w_j)&:&\text{witness tokens; }G_j,W_j\text{ denote their certificate propositions}.
\end{array}
\tag{3}
\]

Within a \(\theta\)-indexed formula, an un-subscripted symbol is an
abbreviation for its \(\theta\)-projection.  No formula may identify parts
of \(\theta\) and \(\theta'\) without a named equality, port, or
conservative-extension relation.

### 1.1 The exact 44 frozen requirements

There are \(5+13+7+5+7+7=44\) frozen requirements.  They split into
43 unary requirements—42 provision certificates and the fixed H_VEHICLE
binding context—and one necessarily binary interoperability requirement.
The table gives the exact interpretation of every identifier.

| lattice | frozen ID | typed certificate |
|---|---|---|
| \(I\) | I_BOUNDARY | \(\operatorname{InfoBoundary}_\eta(S_I,X_I,B)\) |
| \(I\) | I_VARIABLE | \(\operatorname{Var}_{S_I}(X_I)\land |X_I|\ge2\land\operatorname{PairwiseDisjoint}(X_I)\) |
| \(I\) | I_PERMUTATION | \(\operatorname{CompWitness}_{\Phi}(S_I,X_I)\) |
| \(I\) | I_CLONING | \(\operatorname{CloneWitness}_{\Phi}(S_I,X_I,x_{I0})\) |
| \(I^\otimes\) | I_INTEROPERABILITY | \(\operatorname{Compatible}_{\Phi}(S_{I,1},S_{I,2})\), in declared pair context \((\theta_1,\theta_2)\) |
| \(R\) | R_BOUNDARY | \(\operatorname{RetentionBoundary}_\eta(b,B)\) |
| \(R\) | R_VALUE | \(k\in X_I\land\operatorname{InfoAttr}(b,k;X_I)\) |
| \(R\) | K_PHYSICAL_INSTANTIATION | \(\operatorname{Inst}_{B,H}(b,k,t_0)\) |
| \(R\) | K_REALIZATION_SCOPE | \(\operatorname{ActualRetentionOrConstructionClaim}_\eta(b,k,p_{\rm code},T)\) |
| \(R\) | R_COUNTERFACTUAL_CAUSAL_ROLE | \(\operatorname{RoleCoupled}_\eta(b,k;T)\land\operatorname{RetCover}_\eta(b,k;X_I,T,\Delta^\ast)\) |
| \(R\) | R_MAINTENANCE | \(\operatorname{MaintenanceRoute}_\eta(b,k;X_I,T)\) |
| \(R\) | R_VALUE_INTERVENTION | \(\operatorname{CSRet}_\eta(b,k;X_I,T,\Delta^\ast)\) |
| \(R\) | R_FINITE_EVIDENCE_BOUND | \(\operatorname{FiniteAuditScope}_\eta(b,k,T;\Delta^\ast,\mathcal E,\mathcal T)\) |
| \(R\) | K_RECIPE_CAUSAL_ROLE | \(\operatorname{RecipeFor}_\eta(k,p_{\rm code},T)\land\operatorname{CausalRole}_\eta(b,k;p_{\rm code},T)\) |
| \(R\) | K_HISTORY | \(\operatorname{HistoryLocated}_\Pi(r,p_{\rm code})\) |
| \(R\) | A_ARTIFACT_ROLE | \(\operatorname{ArtifactClassified}_\eta(p_{\rm code})\) |
| \(R\) | X_EXPLANATORY_LEVEL | \(\operatorname{ExplanatoryLevelClaim}_\eta(p_{\rm code})\) |
| \(R\) | K_REALIZATION_EQUIVALENCE | \(\exists b',k'\,\operatorname{RealizationEq}_\eta((b,k),(b',k');T,\mathcal E)\) |
| \(H\) | H_BOUNDARY | \(\operatorname{DeclaredBoundary}(F,B)\) |
| \(H\) | H_NO_DESIGN | \(\operatorname{NoDesign}(\Phi)\) |
| \(H\) | H_ACCURACY | \(\operatorname{HighOrImprovableAccuracy}(F,T,\epsilon)\) |
| \(H\) | H_RECIPE | \(\operatorname{RecipeCarrier}(r,p_{\rm code},\Sigma)\) |
| \(H\) | H_DIGITAL_RECIPE | \(\operatorname{DigitalCodeWitness}(S_\Sigma,\Sigma,x_{\Sigma0})\) |
| \(H\) | H_ERROR_CORRECTION | \(\operatorname{CorrectionWitness}(c,b_c;r,p_{\rm code},\Sigma,\mathcal C_\Sigma)\) |
| \(H\) | H_VEHICLE | fixed selected-witness binding \(\varpi_{30,\theta}\downarrow\) in (11) |
| \(V\) | V_POPULATION | \(|\mathcal V|\ge2\) |
| \(V\) | V_INHERITANCE | \(\operatorname{Inherited}_{\iota}(\mathcal V,\mathcal V^+)\) |
| \(V\) | V_VARIATION | \(\operatorname{Variant}_{B,\nu}(\mathcal V)\land\operatorname{NonSpecificToClaimedEnd}_\eta(\nu)\) |
| \(V\) | V_SELECTION | \(\operatorname{SelectionCausalChain}_\eta(\lambda)\) |
| \(V\) | V_FALLIBILITY | \(\operatorname{NoGuarantee}(\nu,\kappa,\delta)\land\operatorname{ErrorEliminationByEnvironment}_\eta(\lambda)\land\neg\operatorname{TheoryMediatedCriticism}_\eta(\lambda)\) |
| \(C\) | C_TARGET | \(\operatorname{Targeted}_\eta(\chi,A^-_\chi)\) |
| \(C\) | C_CHANNEL | \(\omega_\chi\in\mathsf{Observation}\dot\cup\mathsf{Deduction}\dot\cup\mathsf{Prediction}\) |
| \(C\) | C_CHAIN | \(\operatorname{InterpretationChain}_\eta(\chi)\) |
| \(C\) | C_AUXILIARIES | \(\operatorname{AuxiliariesClosed}_\eta(\chi,\Xi_\chi)\) |
| \(C\) | C_DISCRIMINATOR | \(\operatorname{Derives}_\eta(A^-_\chi\land\Xi_\chi,d_\chi)\land\operatorname{Predeclared}_\eta(\rho_\chi,d_\chi,\mathcal D_\chi)\) |
| \(C\) | C_PROTOCOL | \(\operatorname{Protocol}_\eta(\rho_\chi)\) |
| \(C\) | C_OUTCOME | exactly one of \(\mathrm{C_REF},\mathrm{C_SURV},\mathrm{C_DISP},\mathrm{C_INC}\) |
| \(E\) | E_P1 | \(\operatorname{P1}_\eta(p_1)\) |
| \(E\) | E_TT | \(\operatorname{TT}_\eta(h,p_1)\) |
| \(E\) | E_EE | \(\operatorname{EE}_\eta(h,\chi)\) |
| \(E\) | E_EVIDENCE_LINK | \(\operatorname{EvidenceLinked}_\eta(e,\chi)\) |
| \(E\) | E_P2 | \(\operatorname{P2}_\eta(p_2;p_1,h,\chi)\) |
| \(E\) | E_PROVENANCE | \(\operatorname{ProvenanceClosed}_\Pi(e)\) |
| \(E\) | E_FALLIBILITY | \(\operatorname{Fallible}_\eta(e)\) |

The finite audit scope means

\[
\operatorname{FiniteAuditScope}_\eta(b,k,T;\Delta^\ast,\mathcal E,\mathcal T)
\Longleftrightarrow
|\Delta^\ast|<\infty\land
\operatorname{DeclaredCohort}_\eta(b,k,T)\land
\operatorname{DeclaredEnvironmentDomain}_\eta(\mathcal E)\land
\operatorname{NoUniversalPromotion}_\eta(\Delta^\ast,\mathcal E,\mathcal T).
\tag{4}
\]

It is therefore not the tautology that the frame happened to choose a finite
\(\Delta^\ast\).

Define the exact unary blocks

\[
\begin{aligned}
I_0={}&\{\mathrm{I\_BOUNDARY,I\_VARIABLE,I\_PERMUTATION,I\_CLONING}\},\\
R_{\rm PK}={}&\{\mathrm{R\_BOUNDARY,R\_VALUE,K\_PHYSICAL\_INSTANTIATION,
K\_REALIZATION\_SCOPE,R\_COUNTERFACTUAL\_CAUSAL\_ROLE,
R\_MAINTENANCE,R\_VALUE\_INTERVENTION,R\_FINITE\_EVIDENCE\_BOUND}\},\\
R_{\rm RK}={}&R_{\rm PK}\cup
\{\mathrm{K\_RECIPE\_CAUSAL\_ROLE,K\_HISTORY,A\_ARTIFACT\_ROLE}\},\\
R_{\rm full}={}&R_{\rm RK}\cup
\{\mathrm{X\_EXPLANATORY\_LEVEL,K\_REALIZATION\_EQUIVALENCE}\},\\
H_0={}&\{\mathrm{H\_BOUNDARY,H\_NO\_DESIGN,H\_ACCURACY,H\_RECIPE,
\mathrm{H\_DIGITAL\_RECIPE,H\_ERROR\_CORRECTION,H\_VEHICLE}\},\\
H_0^{\rm mat}={}&H_0\setminus\{\mathrm{H\_VEHICLE}\},\\
V_0={}&\{\mathrm{V\_POPULATION,V\_INHERITANCE,V\_VARIATION,V\_SELECTION}\},\\
C_0={}&\{\mathrm{C\_TARGET,C\_CHANNEL,C\_CHAIN,C\_AUXILIARIES,
\mathrm{C\_DISCRIMINATOR,C\_PROTOCOL,C\_OUTCOME}\},\\
E_0={}&\{\mathrm{E\_P1,E\_TT,E\_EE,E\_EVIDENCE\_LINK,E\_P2,
\mathrm{E\_PROVENANCE,E\_FALLIBILITY}\}.
\end{aligned}
\tag{5}
\]


### 1.2 The necessary binary information calculation

I_INTEROPERABILITY cannot truthfully be placed in a one-system state. Its
separate finite pair calculation uses \((\theta_1,\theta_2)\).

\[
\begin{aligned}
r_{I,1}:\quad&
 \mathrm{I\_APP}(\theta_1)\land\bigwedge I_0(\theta_1)
 \Longrightarrow\widehat I(\theta_1)\quad[\mathsf D],\\
r_{I,2}:\quad&
 \mathrm{I\_APP}(\theta_2)\land\bigwedge I_0(\theta_2)
 \Longrightarrow\widehat I(\theta_2)\quad[\mathsf D],\\
r_{\otimes}:\quad&
 \widehat I(\theta_1)\land\widehat I(\theta_2)\land
 \mathrm{I\_INTEROPERABILITY}\land\mathrm{I_\otimes APP}
 \Longrightarrow\widehat I_\otimes(\theta_1,\theta_2)
 \quad[\mathsf P].
\end{aligned}
\tag{7}
\]

Its binary material alphabet, target set, and rule register are

\[
\begin{aligned}
\mathcal P^\otimes_{\eta,\theta_1,\theta_2}
={}&S_{\widehat I(\theta_1)}\cup S_{\widehat I(\theta_2)}
 \cup\{\mathrm{I\_INTEROPERABILITY},\mathrm{I_\otimes APP}\},\\
\mathcal Q^\otimes_{\eta,\theta_1,\theta_2}
={}&\{\widehat I(\theta_1),\widehat I(\theta_2),
       \widehat I_\otimes(\theta_1,\theta_2)\},\\
\mathcal R^\otimes_{\eta,\theta_1,\theta_2}
={}&\{r_{I,1},r_{I,2},r_\otimes\}.
\end{aligned}
\tag{7a}
\]

A pair provision state and its supplied part are

\[
v_{12}:\mathcal P^\otimes_{\eta,\theta_1,\theta_2}\to\{+,-\},
\qquad
D^\otimes(v_{12})=\{a\in\mathcal P^\otimes_{\eta,\theta_1,\theta_2}:
v_{12}(a)=+\}.
\tag{7b}
\]

The binary closure is the finite recurrence

\[
\begin{aligned}
\operatorname{Cl}^{\otimes}_0(D^\otimes)&=D^\otimes,\\
\operatorname{Cl}^{\otimes}_{n+1}(D^\otimes)&=
\operatorname{Cl}^{\otimes}_{n}(D^\otimes)\cup
\{q_r:r\in\mathcal R^\otimes,\,
A_r\subseteq\operatorname{Cl}^{\otimes}_{n}(D^\otimes)\},\\
\mathcal F^\otimes_{\eta,\theta_1,\theta_2}(v_{12})&=
\bigcup_{0\le n\le|\mathcal Q^\otimes|}
\operatorname{Cl}^{\otimes}_n(D^\otimes(v_{12}))
\cap\mathcal Q^\otimes_{\eta,\theta_1,\theta_2}.
\end{aligned}
\tag{7c}
\]

Thus the two unary information heads are genuinely derived from the pair
package before the interoperability rule is eligible. The semantic target is

\[
\llbracket\widehat I_\otimes(\theta_1,\theta_2)\rrbracket^\otimes
\Longleftrightarrow
\exists x_{120}\,\operatorname{InfoVar}_\Phi
(S_{I,1}\otimes S_{I,2},X_{I,1}\times X_{I,2};x_{120}).
\tag{7d}
\]

\[
S_{\widehat I(\theta_j)}:=
\{\mathrm{I\_APP}(\theta_j)\}\cup I_0(\theta_j)
\qquad(j\in\{1,2\}).
\tag{7d1}
\]
The pair raw-certificate interpretation is total:
\[
\llbracket a\rrbracket^\otimes_{\eta,\theta_1,\theta_2}:=
\begin{cases}
\llbracket a\rrbracket_{\eta,\theta_j,\varpi},
 &a\in S_{\widehat I(\theta_j)},\ j\in\{1,2\},\\
\operatorname{Compatible}_\Phi(S_{I,1},S_{I,2}),
 &a=\mathrm{I\_INTEROPERABILITY},\\
\operatorname{CompositeInformationClaim}_\eta(\theta_1,\theta_2),
 &a=\mathrm{I_\otimes APP}.
\end{cases}
\tag{7d2}
\]
The finite rule and its source-level semantic import are kept distinct:
\[
r_\otimes^{\sharp}:\quad
\operatorname{InfoVar}_\Phi(S_{I,1},X_{I,1};x_{I0,1})\land
\operatorname{InfoVar}_\Phi(S_{I,2},X_{I,2};x_{I0,2})\land
\operatorname{Compatible}_\Phi(S_{I,1},S_{I,2})
\Longrightarrow
\exists x_{120}\,\operatorname{InfoVar}_\Phi
(S_{I,1}\otimes S_{I,2},X_{I,1}\times X_{I,2};x_{120}).
\qquad[\mathsf P]
\tag{7d3}
\]
\[
\mathbb T^\otimes_{\eta,\theta_1,\theta_2}:=
\mathbb T^I_{\eta,\theta_1}\cup\mathbb T^I_{\eta,\theta_2}
\cup\{r_\otimes^{\sharp}\},
\qquad
\mathbb T^I_{\eta,\theta_j}:=
\{\text{the ground instance of the definition (14) at }\theta_j\}.
\tag{7d3a}
\]
Thus the raw certificates supply the two unary information-media facts and
the compatibility fact; the finite rule \(r_\otimes\) records their audited
closure, while \(r_\otimes^{\sharp}\) licenses its CTI semantic consequence.
The declared composite-claim certificate gates whether this optional test is
run; it is not silently added as a premise to the CTI import.

For the CTI product import, the pair-register soundness condition is

\[
\widehat I_\otimes\in\mathcal F^\otimes_{\eta,\theta_1,\theta_2}(v_{12})
\Longrightarrow
\mathbb T^\otimes_{\eta,\theta_1,\theta_2}\cup
\{\llbracket a\rrbracket^\otimes:a\in D^\otimes(v_{12})\}
\models\llbracket\widehat I_\otimes\rrbracket^\otimes.
\qquad[\mathsf T]
\tag{7e}
\]

**Local proof.** A derivation of \(\widehat I_\otimes\) first derives both
unary heads from their supplied \(I_0\) packages. Expanding their two
instances of (14) yields the two \(\operatorname{InfoVar}\) antecedents;
the supplied interoperability certificate yields the third antecedent of
\(r_\otimes^\sharp\). Applying that imported CTI implication establishes
(7d). Thus (7e) is a local \(\mathsf T\) soundness theorem whose provenance
set inherits the \(\mathsf P\) import (7d3).
The pair rule is run only when
\(\mathrm{I_\otimes APP}\Longleftrightarrow
\operatorname{CompositeInformationClaim}_\eta(\theta_1,\theta_2)\) is
supplied. Otherwise the composite subtest is \(\mathsf{NOT\_APPLICABLE}\).
It is not a universal claim that a candidate or every component is
interoperable, digital, or clonable.

### 1.3 Selected witnesses are fixed typing contexts

Write \(w=(V_{\rm veh},r,S_\Sigma,p_{\rm code},\Sigma,x_{\Sigma0},
\mathbf e,c,b_c,\mathcal C_\Sigma)\), and define the closed selected term
\[
w_\theta:=(V_{{\rm veh},\theta},r_\theta,S_{\Sigma,\theta},p_{{\rm code},\theta},
\Sigma_\theta,x_{\Sigma0,\theta},\mathbf e_\theta,c_\theta,b_{c,\theta},
\mathcal C_{\Sigma,\theta}).
\tag{7f}
\]
Define the full constructor-theory consequent

\[
\begin{aligned}
\operatorname{HConseq}_\eta(F,T,\epsilon;w)
\Longleftrightarrow{}&
\operatorname{VehPkg}(F;V_{\rm veh},r,S_\Sigma,p_{\rm code},
 \Sigma,c,b_c,\mathcal C_\Sigma)\\
&\land\operatorname{InfoVar}_\Phi(S_\Sigma,\Sigma;x_{\Sigma0})
\land\operatorname{ProgConstr}(V_{\rm veh},p_{\rm code},T)\\
&\land\operatorname{RecipeUnits}(p_{\rm code},\Sigma)
\land\operatorname{BlindCopy}(c,r,p_{\rm code},\Sigma)\\
&\land\operatorname{ErrorCorrect}(c,b_c;r,p_{\rm code},\Sigma)
\land\operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e).
\end{aligned}
\tag{8}
\]

\[
\begin{aligned}
\mathscr Z_{30}&=\mathsf{Constructor}\times\mathsf{Task}\times\mathsf{Accuracy},
&
\mathcal W_{30,\eta}(F,T,\epsilon)
&=\{w:\operatorname{HConseq}_\eta(F,T,\epsilon;w)\},\\
\mathscr Z_{49}&=\mathsf{Trace}\times\mathsf{ProgramPort},
&
\mathcal W_{49,\eta}(\tau,P_\Sigma)
&=\{R:\operatorname{Realized}_\eta(\tau;P_\Sigma,R)\},\\
\mathscr Z_{56}&=\mathsf{Ecology}\times\mathsf{SparkCut}\times\mathsf{Frame},
&
\mathcal W_{56,\eta}(\mathbb P,\mathcal K,\Gamma)
&=\{\mathcal R:\operatorname{P56Map}_\eta(\mathbb P,\mathcal K,\Gamma,\mathcal R)\},\\
D_{30}&=\{(F,T,\epsilon)\in\mathscr Z_{30}:
  \mathcal W_{30,\eta}(F,T,\epsilon)\ne\varnothing\},\\
D_{49}&=\{(\tau,P_\Sigma)\in\mathscr Z_{49}:
  \mathcal W_{49,\eta}(\tau,P_\Sigma)\ne\varnothing\},\\
D_{56}&=\{(\mathbb P,\mathcal K,\Gamma)\in\mathscr Z_{56}:
  \mathcal W_{56,\eta}(\mathbb P,\mathcal K,\Gamma)\ne\varnothing\}.
\end{aligned}
\tag{9}
\]

A fixed witness context is
\(\varpi=(\operatorname{sel}_{30,\eta},\operatorname{sel}_{49,\eta},
\operatorname{sel}_{56,\eta})\), where the entries are total dependent
sections:

\[
\begin{aligned}
\operatorname{sel}_{30,\eta}&\in
\prod_{(F,T,\epsilon)\in D_{30}}\mathcal W_{30,\eta}(F,T,\epsilon),\\
\operatorname{sel}_{49,\eta}&\in
\prod_{(\tau,P_\Sigma)\in D_{49}}\mathcal W_{49,\eta}(\tau,P_\Sigma),\\
\operatorname{sel}_{56,\eta}&\in
\prod_{(\mathbb P,\mathcal K,\Gamma)\in D_{56}}
\mathcal W_{56,\eta}(\mathbb P,\mathcal K,\Gamma).
\end{aligned}
\tag{10}
\]

The side judgments are

\[
\begin{aligned}
\varpi_{30,\theta}\downarrow
&\Longleftrightarrow
(F_\theta,T_\theta,\epsilon_\theta)\in D_{30}\land
\operatorname{sel}_{30,\eta}(F_\theta,T_\theta,\epsilon_\theta)=w_\theta,\\
\varpi_{49,\theta}\downarrow
&\Longleftrightarrow
(\tau_\theta,P_{\Sigma,\theta})\in D_{49}\land
\operatorname{sel}_{49,\eta}(\tau_\theta,P_{\Sigma,\theta})=R_\theta,\\
\varpi_{56,\theta}\downarrow
&\Longleftrightarrow
(\mathbb P_{\Sigma,\theta},\mathcal K_{\le t,\theta},\Gamma_\theta)\in D_{56}\land
\operatorname{sel}_{56,\eta}(\mathbb P_{\Sigma,\theta},\mathcal K_{\le t,\theta},\Gamma_\theta)
=\mathcal R_{\Gamma,\Sigma,\theta}.
\end{aligned}
\tag{11}
\]

They are fixed typing data, not premise atoms and not objects varied by a
deletion or countermodel test.  All semantic comparisons are made inside the
fixed class \(\mathfrak M_{\eta,\theta,\varpi}\).

### 1.4 Auxiliary certificate dictionary

The finite unary certificate alphabet contains the following additional
ground certificates.  This dictionary gives all rule antecedents a typed
meaning.  It also contains the mutually exclusive applicability selectors
\(\mathrm{R\_EQ\_APP}\) and \(\mathrm{R\_EQ\_NA}\) for the optional
multiple-realization subtest.

\[
\begin{array}{rcl}
\mathrm{I_APP}&\Longleftrightarrow&\operatorname{InfoAuditQuery}_\eta(S_I,X_I),\\
\mathrm{I_NA}&\Longleftrightarrow&\operatorname{InfoScopeOmitted}_\eta(S_I,X_I),\\
\mathrm{R_APP}&\Longleftrightarrow&\operatorname{RetentionAuditQuery}_\eta(b,k,T),\\
\mathrm{R_NA}&\Longleftrightarrow&\operatorname{RetentionScopeOmitted}_\eta,\\
\mathrm{R_EQ_APP}&\Longleftrightarrow&\operatorname{DeclaredMultipleRealizationClaim}_\eta(b,k,T),\\
\mathrm{R_EQ_NA}&\Longleftrightarrow&\operatorname{MultipleRealizationScopeOmitted}_\eta,\\
\mathrm{H_APP}&\Longleftrightarrow&
 \operatorname{DeclaredHRepClaim}_\eta(F,T,\epsilon)\land
 \operatorname{SelfReproduction}_B(F,T)\land\operatorname{GenericResources}(\mathcal E),\\
\mathrm{H_NA}&\Longleftrightarrow&\operatorname{HScopeOmitted}_\eta,\\
\mathrm{EXT_P}&\Longleftrightarrow&
 B_{\rm ext}\ne B\land\operatorname{ExternalRecipeCausalRole}_\eta(r,p_{\rm code},T,B_{\rm ext})
 \land\neg\operatorname{CandidateRecipeRole}_\eta(b,k,p_{\rm code},T,B),\\
J_{IR}&\Longleftrightarrow&
 \operatorname{dom}(\alpha)=i\land\operatorname{cod}(\alpha)=k\land
 \operatorname{BearerOf}(\alpha)=b\land\operatorname{ScopeOf}(\alpha)=\eta,\\
J_{RE}&\Longleftrightarrow&
 \operatorname{dom}(\zeta)=k\land\operatorname{cod}(\zeta)=e\land
 \operatorname{ScopeOf}(\zeta)=\eta,\\
J_{CE}&\Longleftrightarrow&
 \operatorname{dom}(\gamma)=\chi\land\operatorname{cod}(\gamma)=e\land
 \operatorname{ScopeOf}(\gamma)=\eta,\\
J_{KP}&\Longleftrightarrow&
 \operatorname{Represents}_\eta(k,p_{\rm code},T)\land
 \operatorname{SameScope}_\eta(k,p_{\rm code}),\\
J_{p\Sigma C}&\Longleftrightarrow&
 p_{\rm code}=\operatorname{code}_{\Sigma}(r)\land r\preceq S_\Sigma\land
 \operatorname{Implements}(c,\mathcal C_\Sigma),\\
\operatorname{JOIN}_{CE}&\Longleftrightarrow&
 \operatorname{PackageOf}(e)=\chi\land\operatorname{EvidenceOf}(e)=\omega_\chi,\\
\operatorname{JOIN}_{IRRE}&\Longleftrightarrow&
 \operatorname{cod}(\alpha)=\operatorname{dom}(\zeta)=k\land
 \operatorname{PackageOf}(e)=\chi\land
 \operatorname{CommonScope}(\alpha,\zeta,\gamma)=(\eta,B,b,T,e),\\
\operatorname{CYCLE}&\Longleftrightarrow&\operatorname{CYCLE}_\theta,\\
\operatorname{PAT}_{VE}&\Longleftrightarrow&\operatorname{PAT}_{VE,\theta},\\
\mathrm{C\_OUTCOME}&\Longleftrightarrow&
(\mathrm{C\_REF}\lor\mathrm{C\_SURV}\lor\mathrm{C\_DISP}\lor\mathrm{C\_INC})\\
&&{}\land\bigwedge_{\substack{u,v\in\{\mathrm{C\_REF},\mathrm{C\_SURV},
\mathrm{C\_DISP},\mathrm{C\_INC}\}\\u\ne v}}\neg(u\land v),\\
\operatorname{TREF}&\Longleftrightarrow&
 \operatorname{NotGood}_{t_1}(A^-_\chi)\land\operatorname{Good}_{t_1}(A^+_\chi)
 \land\operatorname{Successor}_\eta(A^+_\chi,A^-_\chi,\mathcal D_\chi),\\
\operatorname{NONSEED}&\Longleftrightarrow&\operatorname{NonSeedPromotion}(\tau),\\
G_j&\Longleftrightarrow&\operatorname{SparkGrowthCondition}_{j,\eta}(\tau;g_j)
 \quad(j=1,2,3,4),\\
\operatorname{TE}&\Longleftrightarrow&\operatorname{TargetEssential}_{T}(\tau),\\
\operatorname{EXT}&\Longleftrightarrow&\operatorname{Ext}_{\Lambda}(J_\Lambda),\\
\operatorname{NR}&\Longleftrightarrow&
 \operatorname{NoSolelyObligationRetreat}_{\Lambda\to\Lambda'}(\tau),\\
\operatorname{FIRST\_PROBLEM}&\Longleftrightarrow&\operatorname{FirstClassProblem}_\eta(p_1),\\
\operatorname{TARGET\_EQ}&\Longleftrightarrow&\operatorname{Target}(\tau)=p_1,\\
\operatorname{PROMOTED\_ACCOUNT}&\Longleftrightarrow&\operatorname{PromotedAccount}(\tau,h^+),\\
\operatorname{GOOD\_ACCOUNT}&\Longleftrightarrow&\operatorname{Good}_{t_1}(h^+;p_1),\\
\operatorname{DISPLACEMENT\_SUCCESSOR}&\Longleftrightarrow&
 \forall u\,[\operatorname{Displaces}_{\tau}(u)\Rightarrow
 \operatorname{Successor}_\eta(h^+,u,\mathcal D_\chi)],\\
\operatorname{FIN}&\Longleftrightarrow&
 \operatorname{FiniteSparkCut}(\mathcal K_{\le t})\land
 \operatorname{TraceOf}(\mathcal K_{\le t})=\tau,\\
W_j&\Longleftrightarrow&
 \operatorname{RealizationWitness}_{j,\eta}(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma;w_j)
 \quad(j=1,\ldots,5),\\
\operatorname{COH}_5&\Longleftrightarrow&
 \operatorname{Coh}_{\eta}(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma;w_1,\ldots,w_5),\\
\operatorname{ID}_3&\Longleftrightarrow&
 \operatorname{Id}_{R}(w_3;g_1,g_2,g_3,g_4),\\
\operatorname{ALIGN}&\Longleftrightarrow&
 \operatorname{Align}_{R}(J_\Lambda,F_\beta),\\
W_0^{\rm term}&\Longleftrightarrow&
 \operatorname{W0Terminal}_\eta(b,k;w_0,R,F_\beta,\tau),\\
\operatorname{COH}_0&\Longleftrightarrow&
 \operatorname{Coh}_{\eta}(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma;w_0,w_1,\ldots,w_5),\\
\operatorname{PORT}&\Longleftrightarrow&
 \operatorname{ProgramOf}(P_\Sigma)=(r,p_{\rm code},S_\Sigma)\land
 \operatorname{Uses}(R,P_\Sigma)=(b,k),\\
\operatorname{KMAP\_BIND}&\Longleftrightarrow&
 \operatorname{TraceOf}(\mathcal K_{\le t})=\tau
 \land\operatorname{KernelProgramPortAlign}_\eta
(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma,\mathcal R_{\Gamma,\Sigma};P_\Sigma,R,b,k),\\
\operatorname{PEALIGN}&\Longleftrightarrow&\operatorname{PEALIGN}_\theta,\\
\operatorname{CAP}_{NS}&\Longleftrightarrow&\operatorname{CanConstructNonSeed}_\eta(A,\mu),\\
\operatorname{CAP}_{CA}&\Longleftrightarrow&\operatorname{CanSustainConsequentialAppraisal}_\eta(A,\mu),\\
\operatorname{CAP}_{A5}&\Longleftrightarrow&\operatorname{CanA5Promote}_\eta(A,\mu),\\
\operatorname{CAP}_{OET}&\Longleftrightarrow&\operatorname{CanDrawOnOwnedEvaluatedTarget}_\eta(A,\mu),\\
\operatorname{CAP}_{JOIN}&\Longleftrightarrow&
 \operatorname{Admissible}_\eta(A,\mu)\land
 \operatorname{SameCapabilityContext}_\eta
 (A,\mu;\operatorname{CAP}_{NS},\operatorname{CAP}_{CA},
 \operatorname{CAP}_{A5},\operatorname{CAP}_{OET}).
\end{array}
\tag{12}
\]

The four exclusive critical selectors are exactly the outcome predicates in
(29).  The three E-selectors are typed scope flags:

\[
\begin{aligned}
\mathrm{E_DOMAINREF}&\Longleftrightarrow
 \operatorname{DeclaredDomainRefutation}_\eta(e,\chi,\mathcal D_\chi),\\
\mathrm{E_PROVGAP}&\Longleftrightarrow
 \operatorname{ProvenanceGap}_\Pi(e),\\
\mathrm{E_UNRES}&\Longleftrightarrow
 \operatorname{CreativityAttributionUnresolved}_\eta(A,e).
\end{aligned}
\tag{13}
\]

For every \(a\in\mathcal P^{\rm mat}_{\eta,\theta}\), its raw denotation
\(\llbracket a\rrbracket_{\eta,\theta,\varpi}\) is the unique right-hand
formula in the finite lookup consisting of Table 1.1, the dictionary (12),
and (13), at the displayed \((\eta,\theta,\varpi)\).  The four outcome
selectors use (29); \(\operatorname{CYCLE}\), \(\operatorname{PAT}_{VE}\),
and \(\operatorname{PEALIGN}\) use respectively (32), (35a), and (42).
There is no default or unspecified raw-certificate case.

The Spark and realization symbols in (12) are the scoped predicates of the
pinned Poietic kernel.  Their finite-realization implication is therefore an
explicit \(\mathsf P\) import below, not a theorem silently assumed without
authority.



---

## 2. Source definitions and scoped imports

### 2.1 Information and role-coupled physical knowledge

\[
\operatorname{InfoVar}_\Phi(S,X;x_0)
\Longleftrightarrow
\operatorname{Var}_S(X)\land |X|\ge2\land
\operatorname{PairwiseDisjoint}(X)\land
\operatorname{CompWitness}_\Phi(S,X)\land
\operatorname{CloneWitness}_\Phi(S,X,x_0).
\qquad[\mathsf D]
\tag{14}
\]

The clone task is \((x,x_0)\mapsto(x,x)\) for \(x\in X\).  This is a
property of a declared medium/variable, not a claim that a complete agent is
clonable.

For each \(k\), a retention profile is a function
\(\varrho_k:\Delta^\ast\to\mathsf{Routes}\).  The counterfactual cover is

\[
\begin{aligned}
\operatorname{RetCover}_\eta(b,k;X,T,\Delta^\ast)
\Longleftrightarrow{}&
\exists\varrho_k:\Delta^\ast\to\mathsf{Routes}\ \forall\delta\in\Delta^\ast\\
&[{\rm do}_\delta]_\Phi\ \exists b',k'\,[\operatorname{Inst}_{B}(b',k',t_1)
 \land k'\cong_X k\\
&\hspace{31mm}\land
 \operatorname{RetentionRoute}_\eta(\varrho_k(\delta);b,k;b',k';T)].
\end{aligned}
\qquad[\mathsf D]
\tag{15}
\]

\([{\rm do}_\delta]_\Phi\varphi\) means that \(\varphi\) holds in every
declared suitable result of that intervention under \(\Phi\).  It is not the
vacuous formula \(\Diamond({\rm do}_\delta\Rightarrow\varphi)\).

Content-sensitive retention is pointwise in the actual value:

\[
\begin{aligned}
\operatorname{CSRet}_\eta(b,k;X,T,\Delta^\ast)
\Longleftrightarrow{}&
\exists\tilde k\in X\setminus\{k\}\ \exists s:k\rightsquigarrow\tilde k\\
\exists\varrho_k\,\exists\varrho_{\tilde k}\,[\\
&\operatorname{AdmSub}_\eta(s)\land
 \operatorname{RetProfile}_\eta(\varrho_k;b,k;X,T,\Delta^\ast)\land
 \operatorname{RetProfile}_\eta(\varrho_{\tilde k};b,\tilde k;X,T,\Delta^\ast)\\
&\land\varrho_{\tilde k}\simeq s_\ast\varrho_k
 \land\neg(\varrho_k\simeq_{\rm copy}\varrho_{\tilde k})].
\end{aligned}
\qquad[\mathsf D]
\tag{16}
\]

The first equivalence is covariance under the intended value substitution.
The last inequivalence says that merely copying or relabelling the carrier
does not explain the retention route.

\[
\begin{aligned}
\operatorname{PK}^{\rm cur}_\eta(b,k;X,T)
\Longleftrightarrow{}&
\operatorname{InfoAttr}(b,k;X)\land\operatorname{Inst}_{B,H}(b,k,t_0)\\
&\land\operatorname{RoleCoupled}_\eta(b,k;T)
\land\operatorname{RetCover}_\eta(b,k;X,T,\Delta^\ast)\\
&\land\operatorname{CSRet}_\eta(b,k;X,T,\Delta^\ast).
\end{aligned}
\qquad[\mathsf D]
\tag{17}
\]

\[
\operatorname{RecipeKnow}_\eta(p_{\rm code},T)
\Longleftrightarrow
\exists b,k,X\,[\operatorname{PK}^{\rm cur}_\eta(b,k;X,T)
\land\operatorname{RecipeFor}_\eta(k,p_{\rm code},T)
\land\operatorname{CausalRole}_\eta(b,k;p_{\rm code},T)] .
\qquad[\mathsf D]
\tag{18}
\]

The distinction matters: an artifact may be a product of recipe knowledge
without itself being a recipe, an information medium, or explanatory
knowledge.

### 2.2 The local digital guard

For \(\Sigma=\{\sigma_1,\ldots,\sigma_n\}\), define a well-formed correction
task by

\[
\begin{aligned}
\operatorname{WFRecover}(\mathcal C_\Sigma,\Sigma,\mathbf e)
\Longleftrightarrow{}&
\operatorname{WFTask}(\mathcal C_\Sigma)
\land\forall \ell\in\{1,\ldots,n\}\,
\operatorname{Face}(\mathcal C_\Sigma,\sigma_\ell,\sigma_\ell)\\
&\land\forall m\in\{1,\ldots,n\}\,
\operatorname{Face}(\mathcal C_\Sigma,e_m,\sigma_m)
\land\forall m\in\{1,\ldots,n\}\,
(e_m\setminus\sigma_m\ne\varnothing)\\
&\land\operatorname{SingleValuedTask}(\mathcal C_\Sigma)
\land\operatorname{PairwiseDisjoint}(\Sigma).
\end{aligned}
\qquad[\mathsf D]
\tag{19}
\]

\[
\operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e)
\Longleftrightarrow
\operatorname{InfoVar}_\Phi(S_\Sigma,\Sigma;x_{\Sigma0})
\land\operatorname{WFRecover}(\mathcal C_\Sigma,\Sigma,\mathbf e)
\land\forall m\in\{1,\ldots,n\}\,
[e_m\setminus\bigcup\Sigma\ne\varnothing].
\qquad[\mathsf D]
\tag{20}
\]

The local theorem is

\[
\frac{
\operatorname{InfoVar}_\Phi(S_\Sigma,\Sigma;x_{\Sigma0})\quad
\operatorname{WFRecover}(\mathcal C_\Sigma,\Sigma,\mathbf e)
}{
\operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e)
}
\quad[\mathsf T].
\tag{21}
\]

Proof.  If \(e_m\setminus\bigcup\Sigma=\varnothing\), choose
\(z\in e_m\setminus\sigma_m\).  Pairwise disjointness puts \(z\) in some
\(\sigma_\ell\), \(\ell\ne m\).  The recovery face and identity face of the same
single-valued task respectively send \(z\) to \(\sigma_m\) and to
\(\sigma_\ell\), a contradiction.  \(\square\)

### 2.3 High-accuracy no-design replication

\[
\begin{aligned}
\operatorname{HRep}_\eta(F,T,\epsilon)
\Longleftrightarrow{}&
\operatorname{NoDesign}(\Phi)\land\operatorname{GenericResources}(\mathcal E)
\land\operatorname{SelfReproduction}_{B}(F,T)\\
&\land\operatorname{HighOrImprovableAccuracy}(F,T,\epsilon)
\land\operatorname{DeclaredBoundary}(F,B).
\end{aligned}
\qquad[\mathsf D]
\tag{22}
\]

\[
\begin{aligned}
\operatorname{VehPkg}(F;&V_{\rm veh},r,S_\Sigma,p_{\rm code},
\Sigma,c,b_c,\mathcal C_\Sigma)\Longleftrightarrow{}\\
&V_{\rm veh},r\preceq F\land c,b_c\preceq V_{\rm veh}\land r\preceq S_\Sigma
\land\Sigma\subseteq\operatorname{Attr}(S_\Sigma)\\
&\land p_{\rm code}=\operatorname{code}_\Sigma(r)\in\Sigma^\ast
\land\operatorname{Implements}(c,\mathcal C_\Sigma)\\
&\land\operatorname{CopyPhase}(c,r,p_{\rm code},\Sigma)
\land\operatorname{BuildPhase}(b_c,r,p_{\rm code},V_{\rm veh},\mathcal E)\\
&\land\operatorname{AllExternalInputsGeneric}_{B}(F).
\end{aligned}
\qquad[\mathsf D]
\tag{23}
\]

The conditional import is exactly

\[
\operatorname{HRep}_\eta(F,T,\epsilon)
\Longrightarrow
\exists w\ \operatorname{HConseq}_\eta(F,T,\epsilon;w).
\qquad[\mathsf P]
\tag{24}
\]

It applies to a declared high/improvable accuracy self-reproduction claim.
It constrains the selected recipe variable \(\Sigma\), carrier \(r\), and
correction task—not the entire candidate, ordinary selection, or creativity.

---

## 3. Selection, criticism, and explanatory episodes

\[
\begin{aligned}
\operatorname{Sel}_\eta(\lambda)
\Longleftrightarrow{}&
|\mathcal V|\ge2\land\operatorname{Variant}_{B,\nu}(\mathcal V)
\land\operatorname{Inherited}_{\iota}(\mathcal V,\mathcal V^+)\\
&\land\operatorname{CommonConstraint}_{\kappa}(\mathcal V)
\land\operatorname{DifferentialContinuation}_{\delta}(\mathcal V,\mathcal V^+)\\
&\land\nu\leadsto_\lambda\kappa\leadsto_\lambda\delta
 \leadsto_\lambda\operatorname{LaterReinstantiation}_\lambda\\
&\land\operatorname{CausalAffects}_\lambda
(\delta,\operatorname{LaterReinstantiation}_\lambda).
\end{aligned}
\qquad[\mathsf D]
\tag{25}
\]

\[
\operatorname{SelectionCausalChain}_\eta(\lambda)
\Longleftrightarrow
\operatorname{CommonConstraint}_{\kappa}(\mathcal V)
\land\operatorname{DifferentialContinuation}_{\delta}(\mathcal V,\mathcal V^+)
\land\nu\leadsto_\lambda\kappa\leadsto_\lambda\delta
\leadsto_\lambda\operatorname{LaterReinstantiation}_\lambda
\land\operatorname{CausalAffects}_\lambda
(\delta,\operatorname{LaterReinstantiation}_\lambda).
\qquad[\mathsf D]
\tag{26}
\]

\[
\operatorname{FallSel}_\eta(\lambda)
\Longleftrightarrow
\operatorname{Sel}_\eta(\lambda)\land
\operatorname{NoGuarantee}(\nu,\kappa,\delta).
\qquad[\mathsf D]
\tag{27a}
\]

NoGuarantee is required only for the fallibility bridge, not for selection
itself.  A naked low-fidelity replicator can therefore satisfy
\(\operatorname{Sel}\) without satisfying HRep.

A critical package is

\[
\chi=(A^-_\chi,A^+_\chi,\Xi_\chi,\omega_\chi,o_\chi,d_\chi,
\rho_\chi,\mathcal D_\chi,t_0,t_1)
\tag{27}
\]

and

\[
\begin{aligned}
\operatorname{CritPkg}_\eta(\chi)
\Longleftrightarrow{}&
\operatorname{Targeted}_\eta(\chi,A^-_\chi)
\land \omega_\chi\in
\mathsf{Observation}\dot\cup\mathsf{Deduction}\dot\cup\mathsf{Prediction}\\
&\land\operatorname{InterpretationChain}_\eta(\chi)
\land\operatorname{AuxiliariesClosed}_\eta(\chi,\Xi_\chi)\\
&\land\operatorname{Derives}_\eta(A^-_\chi\land\Xi_\chi,d_\chi)
\land\operatorname{Predeclared}_\eta(\rho_\chi,d_\chi,\mathcal D_\chi)
\land\operatorname{Protocol}_\eta(\rho_\chi).
\end{aligned}
\qquad[\mathsf D]
\tag{28}
\]

Thus a record, score, deduction, or prediction is evidence only as a member
of this typed package.  Its chain includes the instrument, software/data
reduction, observer or inference, auxiliaries, and failure modes appropriate
to its channel.

\[
\begin{array}{rcl}
\mathrm{C_REF}&\Longleftrightarrow&\operatorname{Incompat}_\eta(o_\chi,d_\chi),\\
\mathrm{C_SURV}&\Longleftrightarrow&\operatorname{Compatible}_\eta(o_\chi,d_\chi),\\
\mathrm{C_DISP}&\Longleftrightarrow&\operatorname{InterpretationDisputed}_\eta(\chi),\\
\mathrm{C_INC}&\Longleftrightarrow&\operatorname{Inconclusive}_\eta(\chi).
\end{array}
\tag{29}
\]

The outcomes are exclusive.  In particular,

\[
\operatorname{CritPkg}_\eta(\chi)\land\mathrm{C_SURV}
\not\Longrightarrow\operatorname{Confirmed}(A^-_\chi).
\qquad[\mathsf N]
\tag{30}
\]



### 3.1 The closed \(P_1\to TT\to EE\to P_2\) episode

The episode token has all required projections:

\[
e=(p_1,h,\chi,\omega_\chi,p_2,h^+,\tau,\mathcal D_\chi;
s_{TT},s_\chi,s_{EE},s_{P2};\eta).
\tag{31}
\]

\[
\begin{aligned}
\operatorname{CYCLE}_\theta\Longleftrightarrow{}&
e_\theta.p_1=p_{1,\theta}\land
e_\theta.h=h_\theta=A^-_{\chi_\theta}\land
e_\theta.\chi=\chi_\theta\\
&\land e_\theta.h^+=h^+_\theta=A^+_{\chi_\theta}
\land e_\theta.p_2=p_{2,\theta}
\land e_\theta.\tau=\tau_\theta
\land e_\theta.\mathcal D=\mathcal D_{\chi_\theta}\\
&\land s_{TT,\theta}\leadsto_e s_{\chi,\theta}
\leadsto_e s_{EE,\theta}\leadsto_e s_{P2,\theta}\\
&\land\operatorname{StageOf}(s_{TT,\theta})=(TT,h_\theta)
\land\operatorname{StageOf}(s_{\chi,\theta})=(\chi,\chi_\theta)\\
&\land\operatorname{StageOf}(s_{EE,\theta})=(EE,\chi_\theta)
\land\operatorname{StageOf}(s_{P2,\theta})=(P2,p_{2,\theta})\\
&\land\operatorname{ProvEdge}_\Pi(p_{1,\theta},h_\theta)
\land\operatorname{ProvEdge}_\Pi(h_\theta,\chi_\theta)
\land\operatorname{ProvEdge}_\Pi(\chi_\theta,p_{2,\theta}).
\end{aligned}
\qquad[\mathsf D]
\tag{32}
\]

\[
\begin{aligned}
\operatorname{Epi}_{\eta,\theta}\Longleftrightarrow{}&
\operatorname{P1}_\eta(p_1)\land\operatorname{TT}_\eta(h,p_1)
\land\operatorname{EE}_\eta(h,\chi)\\
&\land\operatorname{EvidenceLinked}_\eta(e,\chi)
\land\operatorname{P2}_\eta(p_2;p_1,h,\chi)
\land\operatorname{ProvenanceClosed}_\Pi(e)\land\operatorname{Fallible}_\eta(e)\\
&\land\operatorname{CritPkg}_\eta(\chi)
\land J_{CE}\land\operatorname{JOIN}_{CE}\land\operatorname{CYCLE}.
\end{aligned}
\qquad[\mathsf D]
\tag{33}
\]

A refutational episode is

\[
\operatorname{TRef}_{\eta,\theta}
\Longleftrightarrow
\operatorname{Epi}_{\eta,\theta}\land\mathrm{C_REF}\land\operatorname{TREF}.
\qquad[\mathsf D]
\tag{34}
\]

It records a defect in the declared conjunction and declared domain.  It
does not automatically identify a particular component as false.

### 3.2 The typed variation–error-elimination bridge

Let

\[
\mathbb V=(\mathsf G\prec\mathsf X\prec\mathsf L\prec\mathsf R).
\tag{35}
\]

\[
\begin{aligned}
\operatorname{PAT}_{VE,\theta}\Longleftrightarrow{}&
r_{e,\theta}(s_{TT,\theta})=\mathsf G\land
r_{e,\theta}(s_{\chi,\theta})=\mathsf X\land
r_{e,\theta}(s_{EE,\theta})=\mathsf L\land
r_{e,\theta}(s_{P2,\theta})=\mathsf R\\
&\land r_{\lambda,\theta}(\nu_\theta)=\mathsf G\land
r_{\lambda,\theta}(\kappa_\theta)=\mathsf X\land
r_{\lambda,\theta}(\delta_\theta)=\mathsf L\\
&\land r_{\lambda,\theta}(\operatorname{LaterReinstantiation}_{\lambda_\theta})
=\mathsf R\\
&\land s_{TT,\theta}\leadsto_e s_{\chi,\theta}
\leadsto_e s_{EE,\theta}\leadsto_e s_{P2,\theta}\\
&\land\nu_\theta\leadsto_{\lambda_\theta}\kappa_\theta
\leadsto_{\lambda_\theta}\delta_\theta
\leadsto_{\lambda_\theta}\operatorname{LaterReinstantiation}_{\lambda_\theta}.
\end{aligned}
\qquad[\mathsf B]
\tag{35a}
\]

\[
\frac{
\operatorname{FallSel}_\eta(\lambda_\theta)\qquad
\operatorname{Epi}_{\eta,\theta}\qquad
\operatorname{PAT}_{VE,\theta}
}{
\operatorname{TypedVEEAnalogue}_{\eta,\theta}
}
\qquad[\mathsf B].
\tag{36}
\]

This is an analogue of typed transition structure only.  It does not identify
a biological variation with a represented conjecture or survival selection
with criticism.

---

## 4. Core growth, physical realization, and capacity

\[
\begin{aligned}
\operatorname{Core}_{\eta,\theta}\Longleftrightarrow{}&
\operatorname{NONSEED}\land G_1\land G_2\land G_3\land G_4
\land\operatorname{TE}\land\operatorname{EXT}\land\operatorname{NR}.
\end{aligned}
\qquad[\mathsf D]
\tag{37}
\]

\[
\begin{aligned}
\operatorname{Exp}_{\eta,\theta}\Longleftrightarrow{}&
\operatorname{Core}_{\eta,\theta}
\land\operatorname{FIRST\_PROBLEM}\land\operatorname{TARGET\_EQ}
\land\operatorname{PROMOTED\_ACCOUNT}\\
&\land\operatorname{GOOD\_ACCOUNT}
\land\operatorname{DISPLACEMENT\_SUCCESSOR}.
\end{aligned}
\qquad[\mathsf D]
\tag{38}
\]

The finite realization route is a scoped import from the pinned Poietic
kernel.  Fix the physical ecology \(\mathbb P_\Sigma\), finite Spark cut
\(\mathcal K_{\le t}\), and realization frame \(\Gamma\).  Write
\(\operatorname{P56Map}_\eta(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma,
\mathcal R_{\Gamma,\Sigma})\) for the kernel's exact typed conclusion:
\(\mathcal R_{\Gamma,\Sigma}:\mathbb P_\Sigma\rightharpoonup
\mathcal K_{\le t}\) satisfying R1--R5.

\[
\frac{
\operatorname{FIN}\qquad W_1\qquad W_2\qquad W_3\qquad W_4\qquad W_5
\qquad\operatorname{COH}_5
}{
\exists\mathcal R\,
\operatorname{P56Map}_\eta(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma,\mathcal R)
}
\qquad[\mathsf P].
\tag{39}
\]

The program port is not part of that source theorem.  Its explicitly named
Poietic bridge binds the selected P5.6 map to the same cut, program port, and
knowledge-bearing role:

\[
\frac{
\exists\mathcal R\,
\operatorname{P56Map}_\eta(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma,\mathcal R)
\qquad \operatorname{KMAP\_BIND}\qquad \operatorname{PORT}
}{
\exists R\,\operatorname{Realized}_\eta(\tau;P_\Sigma,R)
}
\qquad[\mathsf B\mid\varpi_{56,\theta}\downarrow].
\tag{39a}
\]

The selected \(R_\theta\) is available only under
\(\varpi_{49,\theta}\downarrow\).
\[
\begin{aligned}
\operatorname{RealCore}_{\eta,\theta}\Longleftrightarrow{}&
\operatorname{Core}_{\eta,\theta}\land
\operatorname{Realized}_\eta(\tau;P_\Sigma,R)\\
&\land\operatorname{ID}_3\land\operatorname{ALIGN}\land W_0^{\rm term}
\land\operatorname{COH}_0\land\operatorname{PORT}\land\operatorname{KMAP\_BIND}.
\end{aligned}
\qquad[\mathsf D]
\tag{40}
\]
The three typed arrows yield the definitional link

\[
\begin{aligned}
\operatorname{Linked}_{\eta,\theta}
\Longleftrightarrow
J_{IR}\land J_{RE}\land J_{CE}\land\operatorname{JOIN}_{IRRE}.
\end{aligned}
\qquad[\mathsf D]
\tag{41}
\]

The port-and-episode alignment is

\[
\begin{aligned}
\operatorname{PEALIGN}_\theta\Longleftrightarrow{}&
e.p_1=p_1\land e.h^+=h^+=A^+_\chi\land e.\tau=\tau\\
&\land\operatorname{Target}(\tau)=p_1
\land\operatorname{TraceOf}(R)=\tau\\
&\land\operatorname{FrameOf}(J_\Lambda,F_\beta)=(T,\Lambda,\Lambda')\\
&\land\operatorname{KnowledgePort}_\eta(e)=(i,b,k)
\land\operatorname{TerminalPort}_\eta(R,F_\beta,\tau)=(b,k)\\
&\land\operatorname{ProgramOf}(P_\Sigma)=(r,p_{\rm code},S_\Sigma)
\land\operatorname{Uses}(R,P_\Sigma)=(b,k)\\
&\land\operatorname{ScopeOf}(e,R,J_\Lambda,F_\beta)=\eta.
\end{aligned}
\qquad[\mathsf D]
\tag{42}
\]

\[
\frac{
\operatorname{Exp}_{\eta,\theta}\quad
\operatorname{RealCore}_{\eta,\theta}\quad
\operatorname{Epi}_{\eta,\theta}\quad
\operatorname{Linked}_{\eta,\theta}\quad
\operatorname{PEALIGN}_\theta
}{
\operatorname{PhysExpEpisode}_{\eta,\theta}
}
\qquad[\mathsf B].
\tag{43}
\]

\[
\operatorname{PhysExpEpisode}_{\eta,\theta}\land
\operatorname{TRef}_{\eta,\theta}
\Longrightarrow
\operatorname{PhysRefExpEpisode}_{\eta,\theta}.
\qquad[\mathsf B]
\tag{44}
\]

Thus the promoted account, criticised predecessor, successor, domain,
episode trace, physical trace, program port, and knowledge bearer are the
same declared objects.  No unrelated witnesses can be spliced.

Creative capacity remains a modal architectural predicate:

\[
\begin{aligned}
\operatorname{CreativeCap}_\eta(A,t)
\Longleftrightarrow\exists\mu\,[&
\operatorname{Admissible}_\eta(A,\mu)
\land\operatorname{CanConstructNonSeed}_\eta(A,\mu)\\
&\land\operatorname{CanSustainConsequentialAppraisal}_\eta(A,\mu)
\land\operatorname{CanA5Promote}_\eta(A,\mu)\\
&\land\operatorname{CanDrawOnOwnedEvaluatedTarget}_\eta(A,\mu)].
\end{aligned}
\qquad[\mathsf D]
\tag{45}
\]

No episode, selection history, retained recipe, or self-reproduction result
entails (45).  For the relevant whole-agent countermodel, define

\[
\begin{aligned}
\operatorname{WholeClone}_{B}(A)&\Longleftrightarrow
 \text{a declared task clones the complete bounded state of }A,\\
\operatorname{WholeDigital}_{B}(A)&\Longleftrightarrow
 \text{every declared state variable of the complete bounded state of }A
 \text{ is a digital code variable}.
\end{aligned}
\tag{46}
\]



---

## 5. The finite premise-to-consequence calculation

Let \(\mathcal J_\theta\) be exactly the auxiliary symbols in (12), together
with the exclusive critical selectors
\(\{\mathrm{C_REF,C_SURV,C_DISP,C_INC}\}\) and
\(\{\mathrm{E_DOMAINREF,E_PROVGAP,E_UNRES}\}\).  In particular it includes
\(\mathrm{FIRST\_PROBLEM,TARGET\_EQ,PROMOTED\_ACCOUNT,GOOD\_ACCOUNT}\), and
\(\mathrm{DISPLACEMENT\_SUCCESSOR}\).

The unary material alphabet is

\[
\mathcal P^{\rm mat}_{\eta,\theta}
=I_0\cup R_{\rm full}\cup H_0^{\rm mat}\cup
V_0\cup\{\mathrm{V\_FALLIBILITY}\}\cup C_0\cup E_0\cup\mathcal J_\theta.
\tag{47}
\]

I_INTEROPERABILITY belongs only to the pair calculation (7)–(7e); it has not
been dropped or silently made unary.

A signed state is a function

\[
v:\mathcal P^{\rm mat}_{\eta,\theta}\to\{+,-\}.
\tag{48}
\]

\(+a\) means that certificate \(a\) is supplied in this audit package.
\(-a\) means that it is withheld; it does **not** mean
\(\neg\llbracket a\rrbracket\).  Let

\[
D(v)=\{a\in\mathcal P^{\rm mat}_{\eta,\theta}:v(a)=+\}.
\tag{49}
\]

Let \(\mathcal B_{\eta,\theta}\) be the finite set of such provision states
that choose exactly one of I_APP/I_NA, R_APP/R_NA, and H_APP/H_NA;
choose at most one of R_EQ_APP/R_EQ_NA (and exactly one only when the
optional multiple-realization subtest is invoked); and choose at most one
of the four C outcome selectors, with exactly one required whenever all of
\(C_0\) are supplied.  This is an audit-package space, not a space of complete semantic
valuations.

The hatted targets are

\[
\begin{aligned}
\mathcal Q_{\eta,\theta}=\{&
\widehat I,\widehat{\mathrm{PK}},\widehat{\mathrm{RK}},\widehat R_{\rm full},
\widehat H_{\rm src},\widehat{\mathrm{Veh}}_\exists,\widehat{\mathrm{Veh}},
\widehat{\mathrm{DG}},\widehat H,\widehat{\mathrm{P56}}_\exists,\\
&\widehat{\mathrm{Sel}},\widehat{\mathrm{FallSel}},\widehat C,\widehat E,
\widehat{\mathrm{TRef}},\widehat{\mathrm{VE}},\widehat{\mathrm{Core}},
\widehat{\mathrm{Exp}},\widehat{\mathrm{Real}}_\exists,\widehat{\mathrm{Real}},
\widehat{\mathrm{RealCore}},\widehat{\mathrm{Link}},
\widehat{\mathrm{PhysExp}},\widehat{\mathrm{PhysRefExp}},\widehat{\mathrm{Cap}}\}.
\end{aligned}
\tag{50}
\]

Each rule \(r\in\mathcal R_{\eta,\theta}\) has a head \(q_r\), a finite
antecedent \(A_r\subseteq\mathcal P^{\rm mat}_{\eta,\theta}\cup
\mathcal Q_{\eta,\theta}\), a primary grade \(g_r\), and a side condition
\(\sigma_r(\varpi)\in\{\top,\varpi_{30,\theta}\downarrow,
\varpi_{49,\theta}\downarrow,\varpi_{56,\theta}\downarrow,
\varpi_{56,\theta}\downarrow\land\varpi_{49,\theta}\downarrow\}\).  The closure is therefore genuinely
defined by

\[
\begin{aligned}
\operatorname{Cl}_0(D;\varpi)&=D,\\
\operatorname{Cl}_{n+1}(D;\varpi)&=
\operatorname{Cl}_n(D;\varpi)\cup
\{q_r:r\in\mathcal R_{\eta,\theta},\\
 A_r\subseteq\operatorname{Cl}_n(D;\varpi),\\
 \sigma_r(\varpi)\},\\
\mathcal F_{\eta,\theta}(v;\varpi)&=
\bigcup_{0\le n\le|\mathcal Q_{\eta,\theta}|}\operatorname{Cl}_n(D(v);\varpi)
\cap\mathcal Q_{\eta,\theta}.
\end{aligned}
\tag{51}
\]

### 5.1 Rule register

\[
\begin{array}{rcll}
\mathrm{I_APP}\land\bigwedge I_0
&\Longrightarrow&\widehat I&[\mathsf D]\\
\widehat I\land\mathrm{R_APP}\land\bigwedge R_{\rm PK}\land J_{IR}
&\Longrightarrow&\widehat{\mathrm{PK}}&[\mathsf D]\\
\widehat{\mathrm{PK}}\land
\mathrm{K\_RECIPE\_CAUSAL\_ROLE}\land\mathrm{K\_HISTORY}\land
\mathrm{A\_ARTIFACT\_ROLE}\land J_{KP}
&\Longrightarrow&\widehat{\mathrm{RK}}&[\mathsf D]\\
\mathrm{R_APP}\land\mathrm{R_EQ_APP}\land\bigwedge R_{\rm full}
&\Longrightarrow&\widehat R_{\rm full}&[\mathsf D]\\
\mathrm{H_APP}\land\mathrm{H\_BOUNDARY}\land\mathrm{H\_NO\_DESIGN}\land
\mathrm{H\_ACCURACY}
&\Longrightarrow&\widehat H_{\rm src}&[\mathsf D]\\
\widehat H_{\rm src}
&\Longrightarrow&\widehat{\mathrm{Veh}}_\exists&[\mathsf P]\\
\widehat{\mathrm{Veh}}_\exists
&\Longrightarrow&\widehat{\mathrm{Veh}}
\quad[\mathsf P\mid\varpi_{30,\theta}\downarrow]\\
\widehat{\mathrm{Veh}}\land
\mathrm{H\_RECIPE}\land\mathrm{H\_DIGITAL\_RECIPE}\land
\mathrm{H\_ERROR\_CORRECTION}\land J_{p\Sigma C}
&\Longrightarrow&\widehat{\mathrm{DG}}&[\mathsf P]\\
\widehat H_{\rm src}\land\widehat{\mathrm{DG}}
&\Longrightarrow&\widehat H&[\mathsf D]\\
\bigwedge V_0&\Longrightarrow&\widehat{\mathrm{Sel}}&[\mathsf D]\\
\widehat{\mathrm{Sel}}\land\mathrm{V\_FALLIBILITY}
&\Longrightarrow&\widehat{\mathrm{FallSel}}&[\mathsf D]\\
\bigwedge C_0&\Longrightarrow&\widehat C&[\mathsf D]\\
\widehat C\land\bigwedge E_0\land J_{CE}\land\operatorname{JOIN}_{CE}
\land\operatorname{CYCLE}
&\Longrightarrow&\widehat E&[\mathsf D]\\
\widehat E\land\mathrm{C_REF}\land\operatorname{TREF}
&\Longrightarrow&\widehat{\mathrm{TRef}}&[\mathsf D]\\
\widehat{\mathrm{FallSel}}\land\widehat E\land\operatorname{PAT}_{VE}
&\Longrightarrow&\widehat{\mathrm{VE}}&[\mathsf B].
\end{array}
\tag{52}
\]

\[
\begin{array}{rcll}
\operatorname{NONSEED}\land G_1\land G_2\land G_3\land G_4\land
\operatorname{TE}\land\operatorname{EXT}\land\operatorname{NR}
&\Longrightarrow&\widehat{\mathrm{Core}}&[\mathsf D]\\
\widehat{\mathrm{Core}}\land\operatorname{FIRST\_PROBLEM}\land
\operatorname{TARGET\_EQ}\land\operatorname{PROMOTED\_ACCOUNT}\land
\operatorname{GOOD\_ACCOUNT}\land\operatorname{DISPLACEMENT\_SUCCESSOR}
&\Longrightarrow&\widehat{\mathrm{Exp}}&[\mathsf D]\\
\operatorname{FIN}\land W_1\land W_2\land W_3\land W_4\land W_5\land
\operatorname{COH}_5
&\Longrightarrow&\widehat{\mathrm{P56}}_\exists&[\mathsf P]\\
\widehat{\mathrm{P56}}_\exists\land\operatorname{KMAP\_BIND}\land\operatorname{PORT}
&\Longrightarrow&\widehat{\mathrm{Real}}_\exists&[\mathsf B\mid\varpi_{56,\theta}\downarrow]\\
\widehat{\mathrm{Real}}_\exists
&\Longrightarrow&\widehat{\mathrm{Real}}
\quad[\mathsf D\mid\varpi_{49,\theta}\downarrow]\\
\widehat{\mathrm{Core}}\land\widehat{\mathrm{Real}}\land
\operatorname{ID}_3\land\operatorname{ALIGN}\land W_0^{\rm term}\land
\operatorname{COH}_0\land\operatorname{PORT}
&\Longrightarrow&\widehat{\mathrm{RealCore}}&[\mathsf D]\\
J_{IR}\land J_{RE}\land J_{CE}\land\operatorname{JOIN}_{IRRE}
&\Longrightarrow&\widehat{\mathrm{Link}}&[\mathsf D]\\
\widehat{\mathrm{Exp}}\land\widehat{\mathrm{RealCore}}\land
\widehat E\land\widehat{\mathrm{Link}}\land\widehat{\mathrm{RK}}\land
\operatorname{PEALIGN}
&\Longrightarrow&\widehat{\mathrm{PhysExp}}&[\mathsf B]\\
\widehat{\mathrm{PhysExp}}\land\widehat{\mathrm{TRef}}
&\Longrightarrow&\widehat{\mathrm{PhysRefExp}}&[\mathsf B]\\
\operatorname{CAP}_{NS}\land\operatorname{CAP}_{CA}\land
\operatorname{CAP}_{A5}\land\operatorname{CAP}_{OET}\land\operatorname{CAP}_{JOIN}
&\Longrightarrow&\widehat{\mathrm{Cap}}&[\mathsf D].
\end{array}
\tag{53}
\]

The semantic targets are total:

\[
\begin{array}{rclcrcl}
\llbracket\widehat I\rrbracket&=&\operatorname{InfoVar}_\Phi(S_I,X_I;x_{I0}),&
\llbracket\widehat{\mathrm{PK}}\rrbracket&=&\operatorname{PK}^{\rm cur}_\eta(b,k;X_I,T),\\
\llbracket\widehat{\mathrm{RK}}\rrbracket&=&\operatorname{RecipeKnow}_\eta(p_{\rm code},T),&
\llbracket\widehat R_{\rm full}\rrbracket&=&\bigwedge R_{\rm full},\\
\llbracket\widehat H_{\rm src}\rrbracket&=&\operatorname{HRep}_\eta(F,T,\epsilon),&
\llbracket\widehat{\mathrm{Veh}}_\exists\rrbracket&=&\mathcal W_{30,\eta}(F,T,\epsilon)\ne\varnothing,\\
\llbracket\widehat{\mathrm{Veh}}\rrbracket&=&\varpi_{30,\theta}\downarrow\land
 w_\theta\in\mathcal W_{30,\eta}(F,T,\epsilon),&
\llbracket\widehat{\mathrm{DG}}\rrbracket&=&
 \operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e),\\
\llbracket\widehat H\rrbracket&=&\operatorname{HRep}_\eta(F,T,\epsilon)\land
 \operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e),&
\llbracket\widehat{\mathrm{Sel}}\rrbracket&=&\operatorname{Sel}_\eta(\lambda),\\
\llbracket\widehat{\mathrm{FallSel}}\rrbracket&=&\operatorname{FallSel}_\eta(\lambda),&
\llbracket\widehat C\rrbracket&=&\operatorname{CritPkg}_\eta(\chi),\\
\llbracket\widehat E\rrbracket&=&\operatorname{Epi}_{\eta,\theta},&
\llbracket\widehat{\mathrm{TRef}}\rrbracket&=&\operatorname{TRef}_{\eta,\theta},\\
\llbracket\widehat{\mathrm{VE}}\rrbracket&=&\operatorname{TypedVEEAnalogue}_{\eta,\theta},&
\llbracket\widehat{\mathrm{Core}}\rrbracket&=&\operatorname{Core}_{\eta,\theta},\\
\llbracket\widehat{\mathrm{Exp}}\rrbracket&=&\operatorname{Exp}_{\eta,\theta},&
\llbracket\widehat{\mathrm{P56}}_\exists\rrbracket&=&
\exists\mathcal R^\circ\,
\operatorname{P56Map}_\eta(\mathbb P_\Sigma,\mathcal K_{\le t},\Gamma,\mathcal R^\circ),\\
\llbracket\widehat{\mathrm{Real}}_\exists\rrbracket&=&
 \exists R\,\operatorname{Realized}_\eta(\tau;P_\Sigma,R),\\
\llbracket\widehat{\mathrm{Real}}\rrbracket&=&\varpi_{49,\theta}\downarrow\land
 R_\theta\in\mathcal W_{49,\eta}(\tau,P_\Sigma),&
\llbracket\widehat{\mathrm{RealCore}}\rrbracket&=&\operatorname{RealCore}_{\eta,\theta},\\
\llbracket\widehat{\mathrm{Link}}\rrbracket&=&\operatorname{Linked}_{\eta,\theta},&
\llbracket\widehat{\mathrm{PhysExp}}\rrbracket&=&\operatorname{PhysExpEpisode}_{\eta,\theta},\\
\llbracket\widehat{\mathrm{PhysRefExp}}\rrbracket&=&\operatorname{PhysRefExpEpisode}_{\eta,\theta},&
\llbracket\widehat{\mathrm{Cap}}\rrbracket&=&\operatorname{CreativeCap}_\eta(A,t).
\end{array}
\tag{54}
\]

Let
\[
D^\sharp(v)=\{\llbracket a\rrbracket_{\eta,\theta,\varpi}:a\in D(v)\}.
\tag{54a}
\]
Let \(\mathbb T_{\eta,\theta,\varpi}\) be the theory containing the
selected-witness definitions (8)–(10), source definitions (14)–(23),
(25)–(29), (31)–(46), the typed dictionary (12)–(13), imports
(24) and (39), bridge rules (36), (39a), (43)–(44), and the fixed witness
judgments (11).  Define the fixed model class by
\[
\mathfrak M_{\eta,\theta,\varpi}:=
\{M:\ M\text{ is sort-correct for }(\eta,\theta,\varpi)
\text{ and }M\models\mathbb T_{\eta,\theta,\varpi}\}.
\tag{54b}
\]
Thus the frame, boundary, selected witnesses, and raw-certificate meanings are
held fixed in every model comparison below.  Then the finite rule register satisfies

\[
q\in\mathcal F_{\eta,\theta}(v;\varpi)
\Longrightarrow
\mathbb T_{\eta,\theta,\varpi}\cup D^\sharp(v)\models
\llbracket q\rrbracket_{\eta,\theta,\varpi}.
\qquad[\mathsf T]
\tag{55}
\]

### 5.2 Exact supports, source cores, and provenance

For each target \(q\), \(S_q\) is its transitive **audit-route** support, and
\(\sigma_q\) is its inherited selected-witness condition.

\[
\begin{array}{c|l|c}
q&S_q&\sigma_q\\ \hline
\widehat I&\{\mathrm{I_APP}\}\cup I_0&\top\\
\widehat{\mathrm{PK}}&S_{\widehat I}\cup\{\mathrm{R_APP},J_{IR}\}\cup R_{\rm PK}&\top\\
\widehat{\mathrm{RK}}&S_{\widehat{\mathrm{PK}}}\cup
 \{\mathrm{K\_RECIPE\_CAUSAL\_ROLE,K\_HISTORY,A\_ARTIFACT\_ROLE},J_{KP}\}&\top\\
\widehat R_{\rm full}&\{\mathrm{R_APP,R\_EQ\_APP}\}\cup R_{\rm full}&\top\\
\widehat H_{\rm src}&\{\mathrm{H_APP,H\_BOUNDARY,H\_NO\_DESIGN,H\_ACCURACY}\}&\top\\
\widehat{\mathrm{Veh}}_\exists&S_{\widehat H_{\rm src}}&\top\\
\widehat{\mathrm{Veh}}&S_{\widehat H_{\rm src}}&\varpi_{30,\theta}\downarrow\\
\widehat{\mathrm{DG}}&S_{\widehat H_{\rm src}}\cup
 \{\mathrm{H\_RECIPE,H\_DIGITAL\_RECIPE,H\_ERROR\_CORRECTION},J_{p\Sigma C}&\varpi_{30,\theta}\downarrow\\
\widehat H&S_{\widehat{\mathrm{DG}}}&\varpi_{30,\theta}\downarrow\\
\widehat{\mathrm{Sel}}&V_0&\top\\
\widehat{\mathrm{FallSel}}&V_0\cup\{\mathrm{V\_FALLIBILITY}\}&\top\\
\widehat C&C_0&\top\\
\widehat E&C_0\cup E_0\cup\{J_{CE},\operatorname{JOIN}_{CE},\operatorname{CYCLE}\}&\top\\
\widehat{\mathrm{TRef}}&S_{\widehat E}\cup\{\mathrm{C_REF},\operatorname{TREF}\}&\top\\
\widehat{\mathrm{VE}}&S_{\widehat{\mathrm{FallSel}}}\cup S_{\widehat E}\cup\{\operatorname{PAT}_{VE}\}&\top\\
\widehat{\mathrm{Core}}&
 \{\operatorname{NONSEED},G_1,G_2,G_3,G_4,\operatorname{TE},\operatorname{EXT},\operatorname{NR}\}&\top\\
\widehat{\mathrm{Exp}}&S_{\widehat{\mathrm{Core}}}\cup
 \{\operatorname{FIRST\_PROBLEM},\operatorname{TARGET\_EQ},\operatorname{PROMOTED\_ACCOUNT},
 \operatorname{GOOD\_ACCOUNT},\operatorname{DISPLACEMENT\_SUCCESSOR}\}&\top\\
\widehat{\mathrm{P56}}_\exists&
 \{\operatorname{FIN},W_1,W_2,W_3,W_4,W_5,\operatorname{COH}_5\}&\top\\
\widehat{\mathrm{Real}}_\exists&
 S_{\widehat{\mathrm{P56}}_\exists}\cup\{\operatorname{KMAP\_BIND},\operatorname{PORT}\}&\varpi_{56,\theta}\downarrow\\
\widehat{\mathrm{Real}}&S_{\widehat{\mathrm{Real}}_\exists}&\varpi_{56,\theta}\downarrow\land\varpi_{49,\theta}\downarrow\\
\widehat{\mathrm{RealCore}}&S_{\widehat{\mathrm{Core}}}\cup S_{\widehat{\mathrm{Real}}_\exists}\cup
 \{\operatorname{ID}_3,\operatorname{ALIGN},W_0^{\rm term},\operatorname{COH}_0,\operatorname{PORT}\}&\varpi_{56,\theta}\downarrow\land\varpi_{49,\theta}\downarrow\\
\widehat{\mathrm{Link}}&\{J_{IR},J_{RE},J_{CE},\operatorname{JOIN}_{IRRE}\}&\top\\
\widehat{\mathrm{PhysExp}}&S_{\widehat{\mathrm{RK}}}\cup S_{\widehat E}\cup S_{\widehat{\mathrm{Exp}}}\cup
 S_{\widehat{\mathrm{RealCore}}}\cup S_{\widehat{\mathrm{Link}}}\cup\{\operatorname{PEALIGN}\}&\varpi_{56,\theta}\downarrow\land\varpi_{49,\theta}\downarrow\\
\widehat{\mathrm{PhysRefExp}}&S_{\widehat{\mathrm{PhysExp}}}\cup\{\mathrm{C_REF},\operatorname{TREF}\}&\varpi_{56,\theta}\downarrow\land\varpi_{49,\theta}\downarrow\\
\widehat{\mathrm{Cap}}&
 \{\operatorname{CAP}_{NS},\operatorname{CAP}_{CA},\operatorname{CAP}_{A5},\operatorname{CAP}_{OET},\operatorname{CAP}_{JOIN}\}&\top
\end{array}
\tag{56}
\]

For every row:

\[
q\in\mathcal F_{\eta,\theta}(v;\varpi)
\Longleftrightarrow S_q\subseteq D(v)\land\sigma_q(\varpi).
\qquad[\mathsf T]
\tag{57}
\]

This is a finite Horn-closure fact, proved by induction on the rule register.
It is the combinatorial engine: removing a supplied requirement deletes every
downstream head whose support contains it, while a missing requirement yields
non-establishment rather than a negative ontological conclusion.

The route supports are not automatically claimed to be semantically minimal
for the un-hatted source predicates.  They contain boundary, query, outcome,
and provenance certificates required for an **audit route**.  Let
\(S_q^{\rm src}\) denote the strictly source-semantic core of a route, with
all audit-only/context certificates removed.  A semantic-minimality result is
claimed only when the following separately labelled obligation is discharged:

\[
\begin{aligned}
\operatorname{Indep}_{\eta,\theta,\varpi}(q,S_q^{\rm src})
\Longleftrightarrow{}&
\sigma_q(\varpi)\land
\mathbb T_{\eta,\theta,\varpi}\cup
\{\llbracket a\rrbracket:a\in S_q^{\rm src}\}
\models\llbracket q\rrbracket\\
&\land\exists M\in\mathfrak M_{\eta,\theta,\varpi}\,
[M\models\mathbb T_{\eta,\theta,\varpi}\cup
\{\llbracket a\rrbracket:a\in S_q^{\rm src}\}]\\
&\land\forall a\in S_q^{\rm src}\ \exists M_a\in\mathfrak M_{\eta,\theta,\varpi}\,
[M_a\models\mathbb T_{\eta,\theta,\varpi}\cup
\{\llbracket b\rrbracket:b\in S_q^{\rm src}\setminus\{a\}\}
\cup\{\neg\llbracket q\rrbracket\}].
\end{aligned}
\qquad[\mathsf N]
\tag{58}
\]

The verification ledger records the exact closure support calculation for each
displayed target.  Source-semantic minimality is deliberately **unclaimed** in
this version unless a separate \(\operatorname{Indep}\) proof and model basis
are added.  This prevents an irrelevant audit precondition from being
misrepresented as a physical necessity.

The provenance set is

\[
\operatorname{Ann}(q_r)=\{g_r\}\cup
\bigcup_{\substack{a\in A_r\\a\in\mathcal Q_{\eta,\theta}}}
\operatorname{Ann}(a).
\tag{59}
\]

Thus, for example, \(\operatorname{Ann}(\widehat{\mathrm{PhysExp}})\)
contains \(\mathsf P\) from the realization route and \(\mathsf B\) from the
physical-explanatory attribution; it is never misreported as merely
\(\mathsf D\).

### 5.3 Status and full signed controls

For a hatted target \(q\), define

\[
\operatorname{Base}_q(v)=
\begin{cases}
\mathsf{NOT\_APPLICABLE},&\operatorname{NA}_q\in D(v),\\
\mathsf{MAY\_PASS},&q\in\mathcal F_{\eta,\theta}(v;\varpi),\\
\mathsf{NOT\_ESTABLISHED},&\text{otherwise}.
\end{cases}
\tag{60}
\]

Here
\[
\operatorname{NA}_{\widehat I}=\mathrm{I_NA},\qquad
\operatorname{NA}_{\widehat{\mathrm{PK}}}=
\operatorname{NA}_{\widehat{\mathrm{RK}}}=\mathrm{R_NA},\qquad
\operatorname{NA}_{\widehat R_{\rm full}}=\mathrm{R_EQ_NA},\qquad
\operatorname{NA}_{\widehat H}=\mathrm{H_NA},
\tag{61}
\]
and all other \(\operatorname{NA}_q\) are false.

The six reported coordinates are total functions:

\[
\begin{aligned}
\pi_I(v)&=\operatorname{Base}_{\widehat I}(v),\\
\pi_R(v)&=
 \begin{cases}
 \mathrm{EXTERNAL\_P\_NOT\_ATTRIBUTED},&\mathrm{EXT_P}\in D(v),\\
 \operatorname{Base}_{\widehat{\mathrm{RK}}}(v),&\text{otherwise},
 \end{cases}\\
\pi_H(v)&=\operatorname{Base}_{\widehat H}(v),\qquad
\pi_V(v)=\operatorname{Base}_{\widehat{\mathrm{Sel}}}(v),\\
\pi_C(v)&=
 \begin{cases}
 \mathrm{REFUTED\_CONJUNCTION},&\widehat C\in\mathcal F(v;\varpi)\land\mathrm{C_REF}\in D(v),\\
 \mathrm{SURVIVED\_DECLARED\_ATTEMPT},&\widehat C\in\mathcal F(v;\varpi)\land\mathrm{C_SURV}\in D(v),\\
 \mathrm{INTERPRETATION\_DISPUTED},&\widehat C\in\mathcal F(v;\varpi)\land\mathrm{C_DISP}\in D(v),\\
 \mathrm{INCONCLUSIVE},&\widehat C\in\mathcal F(v;\varpi)\land\mathrm{C_INC}\in D(v),\\
 \mathsf{NOT\_ESTABLISHED},&\text{otherwise},
 \end{cases}\\
\pi_E(v)&=
 \begin{cases}
 \mathrm{REFUTATION\_RECORDED\_ON\_DECLARED\_DOMAIN},
 &\widehat{\mathrm{TRef}}\in\mathcal F(v;\varpi)\land\mathrm{E_DOMAINREF}\in D(v),\\
 \mathrm{PROVENANCE\_UNRESOLVED},&\mathrm{E_PROVGAP}\in D(v),\\
 \mathrm{PHYSICALLY\_REALIZED\_REFUTATIONAL\_EPISODE},&
 \widehat{\mathrm{PhysRefExp}}\in\mathcal F(v;\varpi),\\
 \mathrm{PHYSICALLY\_REALIZED\_CRITICISABLE\_EPISODE},&
 \widehat{\mathrm{PhysExp}}\in\mathcal F(v;\varpi),\\
 \mathrm{CRITICISABLE\_TRACE\_AUDITED},&\widehat E\in\mathcal F(v;\varpi),\\
 \mathrm{UNRESOLVED\_NOT\_NON\_CREATIVE},&\mathrm{E_UNRES}\in D(v),\\
 \mathsf{NOT\_ESTABLISHED},&\text{otherwise}.
 \end{cases}\\
\operatorname{Display}(v)&=(\pi_I(v),\pi_R(v),\pi_H(v),\pi_V(v),\pi_C(v),\pi_E(v)).
\end{aligned}
\tag{62}
\]

The two conditional diagnostics are reported separately, so a claimed
composite medium or multiple realization cannot disappear inside a coarse
six-coordinate result:
\[
\begin{aligned}
\pi_{I^\otimes}(v_{12})&=
\begin{cases}
\mathsf{MAY\_PASS},&\mathrm{I_\otimes APP}\in D^\otimes(v_{12})\land
 \widehat I_\otimes\in\mathcal F^\otimes_{\eta,\theta_1,\theta_2}(v_{12}),\\
\mathsf{NOT\_ESTABLISHED},&\mathrm{I_\otimes APP}\in D^\otimes(v_{12}),\\
\mathsf{NOT\_APPLICABLE},&\text{otherwise},
\end{cases}\\
\pi_{R_{\rm eq}}(v)&=
\begin{cases}
\mathsf{MAY\_PASS},&\mathrm{R\_EQ\_APP}\in D(v)\land
 \widehat R_{\rm full}\in\mathcal F_{\eta,\theta}(v;\varpi),\\
\mathsf{NOT\_ESTABLISHED},&\mathrm{R\_EQ\_APP}\in D(v),\\
\mathsf{NOT\_APPLICABLE},&\text{otherwise},
\end{cases}\\
\operatorname{Display}^{+}(v,v_{12})&=
(\operatorname{Display}(v),\pi_{I^\otimes}(v_{12}),\pi_{R_{\rm eq}}(v)).
\end{aligned}
\tag{62a}
\]
\(\operatorname{Display}\) remains the frozen six-lattice vector;
\(\operatorname{Display}^{+}\) exposes only conditional diagnostics.

There is no \(\mathrm{CONFIRMED}\) or \(\mathrm{CREATIVITY\_PROVEN}\)
outcome.

For a control, \(\operatorname{Comp}(P^+,\Sigma^+;\Gamma^{\rm fix})\)
is the unique provision state that supplies \(P^+\cup\Sigma^+\), withholds
every other material certificate, and is evaluated relative to the named
typed model fixture \(\Gamma^{\rm fix}\).  Fixture facts are semantic
constraints on the model used to validate the named scenario; they are not
silently added as closure premises.

The fixture names in the control table are not prose labels.  They abbreviate
the following typed semantic constraints in the fixed model class:
\[
\begin{array}{rcl}
\mathsf{TransientRegister}&\Longleftrightarrow&
 \operatorname{InfoVar}_\Phi(S_I,X_I;x_{I0})\land
 \neg\operatorname{RetCover}_\eta(b,k;X_I,T,\Delta^\ast),\\
\mathsf{ExternalRoutine}&\Longleftrightarrow&
 \operatorname{RecipeKnow}_\eta(p_{\rm code},T)\land
 \neg\operatorname{Exp}_{\eta,\theta}\land
 \neg\operatorname{CreativeCap}_\eta(A,t),\\
\mathsf{LowFidelityLineage}&\Longleftrightarrow&
 \operatorname{Sel}_\eta(\lambda)\land\neg\operatorname{HRep}_\eta(F,T,\epsilon),\\
\mathsf{BlindSelection}&\Longleftrightarrow&
 \operatorname{Sel}_\eta(\lambda)\land\neg\operatorname{CritPkg}_\eta(\chi),\\
\mathsf{NonSelfReproducingCandidate}&\Longleftrightarrow&
 F=A\land\neg\operatorname{SelfReproduction}_B(A,T),\\
\mathsf{PossibleTaskOnly}&\Longleftrightarrow&
 \operatorname{Possible}_\Phi(T)\land
 \neg\exists b',k'\,\operatorname{PK}^{\rm cur}_\eta(b',k';X_I,T),\\
\mathsf{ExternalRecipeCarrier}&\Longleftrightarrow&
 \operatorname{ExternalRecipeCausalRole}_\eta(r,p_{\rm code},T,B_{\rm ext})
 \land\neg\operatorname{CandidateRecipeRole}_\eta(b,k,p_{\rm code},T,B),\\
\mathsf{BareScore}&\Longleftrightarrow&
 \operatorname{Record}(o_\chi)\land\neg\operatorname{CritPkg}_\eta(\chi),\\
\mathsf{CompleteAgreeingPackage}&\Longleftrightarrow&
 \operatorname{CritPkg}_\eta(\chi)\land\mathrm{C\_SURV}
 \land\neg\operatorname{Confirmed}(A^-_\chi),\\
\mathsf{FinalUncriticisableOutput}&\Longleftrightarrow&
 \operatorname{FinalOutput}_\eta(A)\land\operatorname{NoPossibleCritic}_\eta(A)
 \land\neg\operatorname{CritPkg}_\eta(\chi),\\
\mathsf{SameLabelDifferentTask}&\Longleftrightarrow&
 \exists b',k'\,\operatorname{SameLabelSwap}_{\eta,\theta}(b',k'),\\
\mathsf{OneCopyOnly}&\Longleftrightarrow&
 \operatorname{OneCopyOnly}_{\eta,\theta},\\
\mathsf{UninstantiatedRecipe}&\Longleftrightarrow&
 \operatorname{AbstractRecipe}(p_{\rm code})\land
 \neg\exists b',k'\,\operatorname{Inst}_{B,H}(b',k',t_0).
\end{array}
\tag{62b}
\]
They constrain only the semantic scenario used for the control; they are not
extra closure premises.
| control | \(P^+;\Sigma^+;\Gamma^{\rm fix}\) | \(\operatorname{Display}(\operatorname{Comp}(\cdot))\) |
|---|---|---|
| NC_INFORMATION_WITHOUT_RETENTION | \(I_0;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{TransientRegister}\) | \((\mathrm{MAY\_PASS},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_RETENTION_WITHOUT_EXPLANATION | \(S_{\widehat{\mathrm{RK}}};\{\mathrm{H_NA}\};\ \mathsf{ExternalRoutine}\) | \((\mathrm{MAY\_PASS},\mathrm{MAY\_PASS},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_NAKED_REPLICATOR | \(V_0;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{LowFidelityLineage}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{MAY\_PASS},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_SELECTION_WITHOUT_CRITICISM | \(V_0;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{BlindSelection}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{MAY\_PASS},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_CREATOR_WITHOUT_SELF_REPRODUCTION | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA,E_UNRES}\};\ \{\mathsf{NonSelfReproducingCandidate},
\neg\operatorname{SelfReproduction}_{B}(A,T)\}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{UNRESOLVED\_NOT\_NON\_CREATIVE})\) |
| NC_BARE_POSSIBILITY_WITHOUT_PRIOR_KNOWLEDGE | \(\varnothing;\{\mathrm{I_APP,R_NA,H_NA}\};\ \mathsf{PossibleTaskOnly}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_EXTERNAL_RECIPE_WITHOUT_CANDIDATE_ATTRIBUTION | \(\{\mathrm{EXT_P}\};\{\mathrm{I_APP,R_APP,H_NA}\};\ \{\mathsf{ExternalRecipeCarrier},
\operatorname{ExternalRecipeCausalRole}_\eta(r,p_{\rm code},T,B_{\rm ext}),
\neg\operatorname{CandidateRecipeRole}_\eta(b,k,p_{\rm code},T,B)\}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{EXTERNAL\_P\_NOT\_ATTRIBUTED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_BARE_SCORE_WITHOUT_CRITICAL_PACKAGE | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{BareScore}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_AGREEING_RESULT_NOT_CONFIRMATION | \(C_0\cup\{\mathrm{C_SURV}\};\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{CompleteAgreeingPackage}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{SURVIVED\_DECLARED\_ATTEMPT},\mathrm{NOT\_ESTABLISHED})\) |
| NC_UNREFUTABLE_OUTPUT | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{FinalUncriticisableOutput}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_UNCONSTRAINED_SUBSTRATE_SWAP | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{SameLabelDifferentTask}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_ONE_COPY_INSPECTION | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{OneCopyOnly}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |
| NC_NONPHYSICAL_RECIPE | \(\varnothing;\{\mathrm{I_APP,R_APP,H_NA}\};\ \mathsf{UninstantiatedRecipe}\) | \((\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_APPLICABLE},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED},\mathrm{NOT\_ESTABLISHED})\) |

By (51)–(62), each row is an exact finite closure calculation.  The
verification ledger records the six-coordinate output vectors for all thirteen
rows.

---

## 6. Countermodels, non-entailments, and limits

For a conservative extension \((\eta',\theta')\) define the closed
abbreviations

\[
\begin{aligned}
\operatorname{BoundaryMove}_{\eta,\theta}^{\eta',\theta'}&\Longleftrightarrow
B'\ne B\land\operatorname{SameObservableLabel}_{\eta,\eta'}(\theta,\theta')
\land\operatorname{MovedConstructorPort}_{\eta,\eta'}(\theta,\theta'),\\
\operatorname{FiniteTheorySuite}_{\eta,\theta}(L)&\Longleftrightarrow
L\subseteq\mathsf{Theory}_\eta\land |L|<\infty,\\
\operatorname{FiniteVariantSuite}_{\eta,\theta}(U)&\Longleftrightarrow
U\subseteq\mathcal V_\theta\times\mathcal E_\eta\land |U|<\infty,\\
\operatorname{SameLabelSwap}_{\eta,\theta}(b',k')&\Longleftrightarrow
\operatorname{SameSyntax}(b,k;b',k')\land
\neg\operatorname{RealizationEq}_\eta((b,k),(b',k');T,\mathcal E),\\
\operatorname{OneCopyOnly}_{\eta,\theta}&\Longleftrightarrow
\operatorname{OneObservedToken}(b,k)\land
\neg\operatorname{CounterfactualFamilyObserved}_\eta(b,k).
\end{aligned}
\tag{63}
\]

Each row below demands a model \(M_j\) in the indicated fixed or conservative
extension class satisfying its left-hand side and the displayed denials.
These are \(\mathsf N\) obligations: they prevent an invalid inference; they
are not forward rules.

| ID | typed countermodel requirement |
|---|---|
| NE_INFORMATION_NOT_KNOWLEDGE | \(M\models\operatorname{InfoVar}_\Phi(S_I,X_I;x_{I0})\land\neg\operatorname{PK}^{\rm cur}_\eta(b,k;X_I,T)\) |
| NE_INFORMATION_NOT_CREATIVITY | \(M\models\operatorname{InfoVar}_\Phi(S_I,X_I;x_{I0})\land\neg\operatorname{CreativeCap}_\eta(A,t)\) |
| NE_RETENTION_NOT_CREATIVITY | \(M\models(\operatorname{PK}^{\rm cur}_\eta(b,k;X_I,T)\lor\operatorname{RecipeKnow}_\eta(p_{\rm code},T))\land\neg\operatorname{Exp}_{\eta,\theta}\land\neg\operatorname{PhysExpEpisode}_{\eta,\theta}\land\neg\operatorname{CreativeCap}_\eta(A,t)\) |
| NE_SELECTION_NOT_HIGH_FIDELITY | \(M\models\operatorname{Sel}_\eta(\lambda)\land\neg\operatorname{HRep}_\eta(F,T,\epsilon)\land\neg\operatorname{DG}(\mathcal C_\Sigma,\Sigma;S_\Sigma,x_{\Sigma0},\mathbf e)\land\neg\operatorname{ErrorCorrect}(c,b_c;r,p_{\rm code},\Sigma)\land\neg\operatorname{VehPkg}(F;V_{\rm veh},r,S_\Sigma,p_{\rm code},\Sigma,c,b_c,\mathcal C_\Sigma)\) |
| NE_SELECTION_NOT_CRITICISM | \(M\models\operatorname{Sel}_\eta(\lambda)\land\neg\operatorname{CritPkg}_\eta(\chi)\land\neg\operatorname{TRef}_{\eta,\theta}\) |
| NE_WHOLE_CREATOR_NOT_CLONABLE | \(M\models F=A\land\operatorname{CreativeCap}_\eta(A,t)\land\neg\operatorname{WholeClone}_B(A)\land\neg\operatorname{WholeDigital}_B(A)\land\neg\operatorname{SelfReproduction}_B(A,T)\land\neg\operatorname{HRep}_\eta(A,T,\epsilon)\) |
| NE_BOUNDARY_IS_EVIDENCE | \(M'\models\operatorname{Linked}_{\eta,\theta}\land\operatorname{BoundaryMove}_{\eta,\theta}^{\eta',\theta'}\land\neg\operatorname{Linked}_{\eta',\theta'}\) |
| NE_FINITE_ENUMERATION_NOT_ALL_THEORIES | \(M\models\operatorname{FiniteTheorySuite}_{\eta,\theta}(L)\land\forall u\in L\,\operatorname{Pass}(u)\land\exists u^\ast\in\mathsf{Theory}_\eta\setminus L\,\neg\operatorname{Pass}(u^\ast)\) |
| NE_P1_TT_EE_P2_NOT_GENERATOR | \(M\models\operatorname{Epi}_{\eta,\theta}\land\neg\operatorname{CreativeCap}_\eta(A,t)\land\neg\operatorname{CreativeGenerator}_\eta(A)\) |
| NE_POSSIBILITY_NOT_PRIOR_KNOWLEDGE | \(M\models\operatorname{Possible}_\Phi(T)\land\neg\exists b,k\,\operatorname{PK}^{\rm cur}_\eta(b,k;X_I,T)\) |
| NE_RECIPE_NOT_CREATIVITY | \(M\models\operatorname{RecipeKnow}_\eta(p_{\rm code},T)\land\neg\operatorname{CreativeCap}_\eta(A,t)\land\neg\operatorname{PhysExpEpisode}_{\eta,\theta}\) |
| NE_ARTIFACT_NOT_RECIPE | \(M\models\operatorname{Artifact}(p_{\rm code})\land\neg\operatorname{RecipeKnow}_\eta(p_{\rm code},T)\land\neg\operatorname{Exp}_{\eta,\theta}\) |
| NE_BARE_RECORD_NOT_EVIDENCE | \(M\models(\operatorname{Record}(o_\chi)\lor\operatorname{Deduction}(d_\chi)\lor\operatorname{Prediction}(d_\chi))\land\neg\operatorname{CritPkg}_\eta(\chi)\) |
| NE_EVIDENCE_NOT_CONFIRMATION | \(M\models\operatorname{CritPkg}_\eta(\chi)\land\mathrm{C_SURV}\land\neg\operatorname{Confirmed}(A^-_\chi)\) |
| NE_VARIATION_NOT_CONJECTURE_IDENTITY | \(M\models\operatorname{TypedVEEAnalogue}_{\eta,\theta}\land\neg\operatorname{RepresentedConjecture}_\eta(\lambda)\land\neg\operatorname{TheoryMediatedCriticism}_\eta(\lambda)\) |
| NE_NONREFUTABLE_NOT_CREATIVE | \(M\models(\operatorname{NoPossibleCritic}_\eta(A)\lor\operatorname{FinalOutput}_\eta(A))\land\neg\operatorname{PhysExpEpisode}_{\eta,\theta}\) |
| NE_HIGH_LEVEL_NOT_EXTRA_SUBSTANCE | \(M\models\operatorname{RoleEq}_\eta(b,k)\land\neg\operatorname{SecondSubstance}(b,k)\land\neg\operatorname{CausalExemption}(b,k)\) |
| NE_SUBSTRATE_SWAP_NOT_AUTOMATIC | \(M\models\exists b',k'\,\operatorname{SameLabelSwap}_{\eta,\theta}(b',k')\) |
| NE_SINGLE_COPY_NOT_COUNTERFACTUAL_ROLE | \(M\models\operatorname{OneCopyOnly}_{\eta,\theta}\land\neg\operatorname{PK}^{\rm cur}_\eta(b,k;X_I,T)\land\neg\operatorname{Sel}_\eta(\lambda)\land\neg\operatorname{ReplicationRole}_\eta(b,k)\) |
| NE_FINITE_VARIANTS_NOT_ALL_ENVIRONMENTS | \(M'\models\operatorname{ConservativeExtension}_{\eta,\theta}^{\eta',\theta'}\land\operatorname{FiniteVariantSuite}_{\eta,\theta}(U)\land\exists(\nu^\ast,\mathcal E^\ast)\,[\,(\nu^\ast,\mathcal E^\ast)\in
(\mathcal V_{\theta'}\times\mathcal E_{\eta'})\setminus U\land\neg\operatorname{RetainsOrAdapts}_{\eta',\theta'}(\nu^\ast,\mathcal E^\ast)\,]\land\neg\operatorname{EverettianUniversalClaim}_{\eta',\theta'}(U)\) |

The two actual model classes are
\(\mathfrak M_{\eta,\theta,\varpi}\) for fixed-frame rows and
\(\mathfrak M_{\eta',\theta',\varpi'}\) for rows explicitly marked \(M'\).
No row treats a failed route as a proof that creativity is absent.



## 7. Authority and scope ledger

This is the immediate-source index for the \(\mathsf P\) and \(\mathsf B\)
edges used below. The [source register](PIECEMEAL_SOURCE_REGISTER.md) is the
complete bibliographic, quotation, licence, and frozen-ID crosswalk.

| item | grade | source IDs | permitted result | prohibited promotion |
|---|---|---|---|---|
| Information variable, retention, recipe knowledge | \(\mathsf D\) | CTI; CT_FOUNDATION; CTL | typed physical definitions | information medium \(\Rightarrow\) creativity |
| Binary CTI product/import route (7), (7d3) | \(\mathsf P\) | CTI, §§2–4 and §6 | a declared compatible pair of information media has the stated product-information consequence | whole-agent clonability, digitality, or interoperability |
| Pair-register soundness (7e) | \(\mathsf T\), inherits \(\mathsf P\) | local proof using (14) and (7d3) | the finite pair closure is sound for its declared semantic target | a new direct CTI theorem or an unscoped composite claim |
| Local digital guard (21) | \(\mathsf T\) | CTI; project kernel P3.1 | a well-formed correction task has an off-code recovery region | every system/agent is digital |
| HRep import (24) | \(\mathsf P\) | CTL | selected high/improvable no-design self-reproduction has the stated recipe/vehicle/error-correction package | selection or creativity \(\Rightarrow\) HRep |
| Finite-realization route (39) | \(\mathsf P\) | KERNEL_P5_6 | a finite witness ecology yields a typed realization map | all abstract traces are physical |
| Program-port realization bridge (39a) | \(\mathsf B\) | Poietic bridge; KERNEL_P5_6 prerequisite | bind a selected ecology map to a declared program port | the source theorem already mentions that port |
| Critical package and episode grammar | \(\mathsf D\) | POPPER_LSCD; POPPER_CNR; POPPER_OK; DEUTSCH | an audit distinguishes evidence channels, auxiliaries, and outcomes | a record confirms a theory |
| Variation–error-elimination analogue (36) | \(\mathsf B\) | DEUTSCH; POPPER_OK | a typed common transition pattern | conjecture \(=\) mutation; criticism \(=\) selection |
| Physical explanatory episode (43)–(44) | \(\mathsf B\) | Poietic bridge; KERNEL_P5_6; POPPER_OK | one scoped, port-aligned physical explanatory/refutational episode | creative capacity or creativity proven |
| Creative capacity (45) | \(\mathsf D\) | project kernel | a modal joint capability predicate | one historical episode establishes capacity |
| Non-entailment registry | \(\mathsf N\) | frozen plan; scoped countermodel families | named invalid inferences are blocked by countermodel requirements | absence of a route proves a negative claim |

The research governs the downstream calculus in three different ways:

\[
\begin{array}{rcl}
\text{source definition}&\rightsquigarrow&\text{model-class constraint},\\
\text{conditional source result}&\rightsquigarrow&\text{one-way imported rule},\\
\text{Poietic connection}&\rightsquigarrow&\text{labelled bridge}.
\end{array}
\tag{64}
\]

A definition remains load-bearing even if it is not a toggle in one proof
when removing it changes the typed domain, permits witness splicing, or
changes the countermodels relevant to an entailment.  It stays in the fixed
frame.  A condition becomes a toggle only when varying it is part of the
stated finite premise experiment.

The strongest affirmative output of this calculus is deliberately bounded:

\[
\operatorname{PhysRefExpEpisode}_{\eta,\theta}
\]

or its non-refutational predecessor, with its full provenance set
\(\operatorname{Ann}\).  This is a scoped audited attribution—not
\(\operatorname{CreativeCap}\), not \(\mathrm{CREATIVITY\_PROVEN}\), and not
a claim about every physically possible creative system.

## 8. Reproduction protocol

To inspect or repeat the calculation:

1. Fix \((\eta,\theta,\varpi)\), including a declared boundary, cut,
   environment/domain, task, evidence package, and provenance frame.
2. Choose a full provision state \(v\in\mathcal B_{\eta,\theta}\).
3. Compute \(\mathcal F_{\eta,\theta}(v;\varpi)\) by (51).
4. Compute \(\operatorname{Display}(v)\) by (60)–(62).
5. Check the relevant source grade and \(\operatorname{Ann}(q)\).
6. For a claimed necessity or non-entailment, provide the separately required
   model or countermodel from (58) or Section 6.

The accompanying verification ledger gives the frozen-plan hash check,
all thirteen control calculations, all twenty countermodel obligations,
independent formal-review checkpoints, and the separately dated final
qualification results recorded in the verification ledger.
