# Piecemeal Premise Calculus

## Mathematical reconstruction, draft 0

### Status

This is a reconstruction of a rule system from the pinned Spark–Poietic kernel,
constructor-theoretic sources, and the frozen piecemeal requirements.  It is
not a recovered source theorem.  Every rule is labelled:

\[
\mathsf D=\text{definition},\qquad
\mathsf P=\text{physical principle/import},\qquad
\mathsf T=\text{conditional theorem},\qquad
\mathsf B=\text{bridge conjecture},\qquad
\mathsf N=\text{non-entailment/countermodel obligation}.
\]

The object of study is not a Boolean predicate \(\operatorname{Creative}(A)\).
It is a family of scoped derivations and countermodels.

---

## 1. Frames, formulae, and derivability

Fix a frame

\[
\sigma=
(\Phi,B,\mathcal E,\Delta,\mathcal Q,\mathcal I,\mathsf{Prov},t),
\]

where \(\Phi\) is a law-relative physical background, \(B\) an attribution
boundary, \(\mathcal E\) an environment class, \(\Delta\) an admissible
intervention family, \(\mathcal Q\) a task portfolio, \(\mathcal I\) an
interpretive apparatus, \(\mathsf{Prov}\) a causal/provenance history, and
\(t\) a cut.  Every atomic formula is indexed by \(\sigma\).

The many-sorted language has at least the sorts

\[
\mathsf{Attr},\mathsf{Var},\mathsf{Task},\mathsf{Constr},
\mathsf{Bearer},\mathsf{Record},\mathsf{Problem},\mathsf{Account},
\mathsf{Variant},\mathsf{CritPkg},\mathsf{Outcome},\mathsf{Trace}.
\]

A judgement has the form

\[
\Gamma;\sigma\vdash^{\ell}_{\pi}\varphi,
\tag{1}
\]

where \(\Gamma\) is a finite set of premises, \(\pi\) is a finite derivation,
and \(\ell\in\{\mathsf D,\mathsf P,\mathsf T,\mathsf B\}\) is its weakest
rule label.  A rule has the form

\[
\frac{p_1(\bar x_1;\sigma),\ldots,p_n(\bar x_n;\sigma)}
     {q(\bar y;\sigma)}\;[r,\ell].
\tag{2}
\]

The variables in the premises must have a single common assignment.  Thus

\[
\frac{I(i,p,b;\sigma)\qquad R(p,e,b;\sigma)\qquad C(c,e,q;\sigma)}
     {Q(i,p,e,c,q,b;\sigma)}
\tag{3}
\]

is admissible only when the displayed \(p,e,b,q,\sigma\) are literally the
same objects in all three premises.  Independently witnessed objects cannot
be substituted into one derivation merely because their labels are similar.

For a rule set \(\mathcal R\), define

\[
\begin{aligned}
C_0(D)&=D,\\
C_{n+1}(D)&=C_n(D)\cup
\left\{q\theta:
\frac{P}{q}\in\mathcal R,\ P\theta\subseteq C_n(D),
\ \theta\text{ is type-correct in }\sigma\right\},\\
\operatorname{Cn}^{\sigma}_{\mathcal R}(D)&=igcup_{n<\omega}C_n(D).
\end{aligned}
\tag{4}
\]

Hence

\[
D;\sigma\vdash_{\mathcal R}\varphi
\iff
\varphi\in\operatorname{Cn}^{\sigma}_{\mathcal R}(D).
\tag{5}
\]

For a conclusion \(\varphi\), its minimal supports are

\[
\operatorname{MinSupp}_{\sigma}(\varphi)=
\min_{\subseteq}
\left\{D:D;\sigma\vdash_{\mathcal R}\varphi\right\}.
\tag{6}
\]

A premise \(p\in D\) is necessary for \(\varphi\), relative to \(D\), when

\[
D\vdash_{\mathcal R}^{\sigma}\varphi
\quad\text{and}\quad
D\setminus\{p\}\nvdash_{\mathcal R}^{\sigma}\varphi.
\tag{7}
\]

A claimed implication fails on a model class \(\mathfrak M_\sigma\) when

\[
D\nvDash_{\mathfrak M_\sigma}\varphi
\iff
\exists M\in\mathfrak M_\sigma
\left(M\models D\land M\models\neg\varphi\right).
\tag{8}
\]

Equations (6)–(8) are the piecemeal procedure: vary premise bundles, derive
exact consequences, and exhibit countermodels for every denied implication.

---

## 2. Constructor-theoretic task and information rules

For pairwise disjoint attributes \(X=\{x_i:i\in I\}\), let

\[
\mathfrak A=\bigcup_{i\in I}\{x_i\mapsto y_i\}
\tag{9}
\]

be a task.  Write \(\Diamond_\Phi\mathfrak A\) for its law-relative
possibility.  Possibility is modal/counterfactual; it does not assert that a
task token occurred.

\[
\Diamond_\Phi\mathfrak A
\not\Rightarrow
\operatorname{Tok}_{\mathsf{Prov}}(\mathfrak A,t).
\tag{10}
\]

For a variable \(X\), let

\[
\operatorname{Clone}_{X}=
\bigcup_{x\in X}\{(x,x_0)\mapsto(x,x)\},
\tag{11}
\]

where \(x_0\) is one fixed receptive attribute, independent of \(x\).  Then

\[
\frac{
|X|\ge 2\qquad
\displaystyle\bigwedge_{\pi\in\operatorname{Sym}(X)}
\Diamond_\Phi\operatorname{Perm}_\pi(X)
\qquad
\Diamond_\Phi\operatorname{Clone}_{X}
}
{operatorname{InfoVar}_{\sigma}(X)}\;[\mathsf D\text{-}I].
\tag{12}
\]

The interoperability principle is recorded separately:

\[
\operatorname{InfoVar}_{\sigma}(X_1)\land
\operatorname{InfoVar}_{\sigma}(X_2)
\Longrightarrow
\operatorname{InfoVar}_{\sigma}(X_1\times X_2)
\quad[\mathsf P\text{-}I].
\tag{13}
\]

No rule has either of the forms

\[
\operatorname{InfoVar}_{\sigma}(X)Longrightarrow
operatorname{Know}_{\sigma}(k),
\qquad
\operatorname{InfoVar}_{\sigma}(X)Longrightarrow
operatorname{Creative}_{\sigma}(A).
\tag{14}
\]

A countermodel for the first formula is a clonable, permutable register whose
payload is erased after one use and has no value-dependent retention route.

---

## 3. Instantiated, causally active knowledge

Let \(k\in X\) be an information attribute carried by a bearer \(b\).  Define

\[
\operatorname{Ret}_{\sigma}(b,k)
\iff
\forall\delta\in\Delta\;\exists r_\delta\;
\left[
\operatorname{Tok}_{\mathsf{Prov}}(r_\delta)
\land
r_\delta:k\leadsto k_\delta
\land
k_\delta\simeq_{\mathrm{Info}} k
\right].
\tag{15}
\]

Let \(\operatorname{Prof}_{\sigma}(k)\) denote the non-copy causal profile
of those retention routes.  Then

\[
\operatorname{CSRet}_{\sigma}(b,k)
\iff
\exists\widetilde{k}\ne k\;
\left[
\operatorname{Prof}_{\sigma}(k)
\not\cong_{\mathrm{copy}}
\operatorname{Prof}_{\sigma}(\widetilde{k})
\right].
\tag{16}
\]

The strengthened physical knowledge predicate is

\[
\frac{
 k\in X\qquad
 \operatorname{InfoVar}_{\sigma}(X)qquad
 \operatorname{Inst}_{B,t}(b,k)qquad
 \operatorname{Ret}_{\sigma}(b,k)qquad
 \operatorname{CSRet}_{\sigma}(b,k)
}
{operatorname{PoiKnow}_{\sigma}(b,k)}
\;[\mathsf D\text{-}K].
\tag{17}
\]

Thus the valid implication is

\[
\operatorname{PoiKnow}_{\sigma}(b,k)Longrightarrow
operatorname{InfoVar}_{\sigma}(X)
\land
operatorname{Inst}_{B,t}(b,k),
\tag{18}
\]

but neither

\[
\operatorname{PoiKnow}_{\sigma}(b,k)Longrightarrow
operatorname{GoodExplanation}(k)
\tag{19}
\]

nor

\[
\operatorname{PoiKnow}_{\sigma}(b,k)Longrightarrow
operatorname{Creative}_{\sigma}(A)
\tag{20}
\]

is licensed.

For a declared task family \(\mathcal Q\), define physical-realizer
identity by

\[
b\sim_{\mathcal Q,\sigma}b'
\iff
\forall T\in\mathcal Q\;
\left[
operatorname{Role}_{\sigma}(b,k,T)
=
operatorname{Role}_{\sigma}(b',k',T)
\right]
\tag{21}
\]

including the declared side effects, form constraints, and environment class.
The abstraction \([b,k]_{\sim_{\mathcal Q,\sigma}}\) is an equivalence class
of physical realizers.  It adds no second physical substance.  Equation (21)
does not license unrestricted substrate replacement:

\[
\operatorname{Role}_{\sigma}(b,k,T)
\not\Rightarrow
\operatorname{Role}_{\sigma'}(b',k',T')
\quad\text{when }\sigma'\ne\sigma.
\tag{22}
\]

The creative-capacity premise is an explicit bridge conjecture:

\[
operatorname{CreativeCap}_{\sigma}(A)
Longrightarrow
\exists b,k\;\operatorname{PoiKnow}_{\sigma}(b,k)
\quad[\mathsf B\text{-}K].
\tag{23}
\]

It does not assert that \(b=A\), that every component is clonable, or that
knowledge generated later was present at an earlier cut.

---

## 4. Conditional high-fidelity replication

Let \(H_\sigma(F,T)\) abbreviate the conjunction of: no-design laws, generic
resources, a non-elementary task \(T\), and a claim of high or indefinitely
improvable accuracy for \(F\).  The conditional constructor-theoretic result
is represented as

\[
H_\sigma(F,T)
\Longrightarrow
\exists(V,P,\Sigma)
\left[
operatorname{ProgConstr}_{\sigma}(V,P,T)
\land
operatorname{Modular}_{\sigma}(P)
\land
operatorname{BlindCopy}_{\sigma}(P)
\land
operatorname{ErrorCorrect}_{\sigma}(P)
\land
operatorname{Digital}_{\sigma}(\Sigma)
ight]
\quad[\mathsf C\text{-}H].
\tag{24}
\]

At a protected code interface, the more exact digital-guard statement is

\[
\frac{
\displaystyle\bigwedge_{j\in I}(x_j\mapsto x_j)
\qquad
\displaystyle\bigwedge_{i\in I}(e_i\mapsto x_i)
\qquad
\forall i\;e_i\setminus x_i\ne\varnothing
}
{displaystyle\bigwedge_{i\in I}e_i\setminus\bigcup_{j\in I}x_j\ne\varnothing}
\;[\mathsf T\text{-}H].
\tag{25}
\]

Hence error correction at that interface entails a discrete/digital guard
structure.  Its scope is the recipe/code variable, not an entire agent:

\[
H_\sigma(F,T)\not\Rightarrowoperatorname{Digital}_{\sigma}(F),
\qquad
\neg H_\sigma(F,T)\not\Rightarrow\negoperatorname{Creative}_{\sigma}(A).
\tag{26}
\]

---

## 5. Variation, selection, conjecture, and criticism

A fallible generative–eliminative trace has the form

\[
\mathfrak F_\tau=
\langle Q_\tau,W_\tau,G_\tau,\Xi_\tau,U_\tau,K_\tau\rangle,
\tag{27}
\]

where \(Q_\tau\) is a candidate family, \(W_\tau\) a problem or environment,
\(G_\tau\) a non-guaranteeing generation relation, \(\Xi_\tau\) an exposure
to consequences, \(U_\tau\) elimination/revision/differential continuation,
and \(K_\tau\) the retained causal structure after the transition.

The explanatory and evolutionary instances are

\[
\begin{array}{c|ccccc}
\tau & Q_\tau & G_\tau & \Xi_\tau & U_\tau & K_\tau\\ \hline
\mathrm{exp} & \text{accounts} & \text{conjecture} & \text{criticism} & \text{revision} & \text{explanatory knowledge}\\
\mathrm{evo} & \text{heritable variants} & \text{variation} & \text{environmental exposure} & \text{differential continuation} & \text{adaptive knowledge}
\end{array}
\tag{28}
\]

The common-form conjecture is

\[
U(\mathfrak F_{\mathrm{exp}})
\cong
U(\mathfrak F_{\mathrm{evo}})
\quad[\mathsf B\text{-}F],
\tag{29}
\]

where \(U\) retains only generation, exposure, elimination, and retention.
Equation (29) does not imply identity of the unprojected structures:

\[
\mathfrak F_{\mathrm{evo}}
\not\Rightarrow
\operatorname{RepresentedConjecture},
\qquad
\mathfrak F_{\mathrm{evo}}
\not\Rightarrow
\operatorname{TheoryMediatedCriticism}.
\tag{30}
\]

For variants \(v_i\), selection requires

\[
\frac{
operatorname{Population}(V)quad
operatorname{Inheritance}(V)quad
operatorname{Variation}(V)quad
operatorname{Constraint}_{\sigma}(V)quad
operatorname{DifferentialContinuation}_{\sigma}(V)quad
operatorname{Reinstantiation}_{\sigma}(V^+)
}
{operatorname{SelectionTrace}_{\sigma}(V)}
\;[\mathsf D\text{-}V].
\tag{31}
\]

A blind population satisfies (31) while satisfying neither conclusion in
(30), so it is a countermodel to both proposed implications.

A critical package is

\[
\chi=(h,A,I,S,O,d,\rho,D),
\tag{32}
\]

with target account \(h\), auxiliaries \(A\), instrument \(I\),
software/data-reduction \(S\), observer or inferential stage \(O\),
deduction \(d\), protocol \(\rho\), and declared domain \(D\).  A record
\(r\) becomes an interpreted outcome only through

\[
o=\operatorname{Int}_{A,I,S,O}(r).
\tag{33}
\]

The basic adverse-result rule is

\[
\frac{
(h\land A)\vdash d
\qquad
\operatorname{Int}_{A,I,S,O}(r)\vdash\neg d
\qquad
\rho\text{ predeclares }d\text{ as adverse}
}
{operatorname{Problem}_{D}(h\land A)}
\;[\mathsf D\text{-}C].
\tag{34}
\]

Equation (34) yields a problem in the displayed conjunction, not \(\neg h\).
Tentative refutation is the stronger relation

\[
\frac{
operatorname{Problem}(h^-)qquad
\negoperatorname{Good}(h^-)qquad
operatorname{Good}(h^+)qquad
h^+\succeq_{\mathrm{succ}}h^-
}
{operatorname{TRef}(h^-;h^+)}
\;[\mathsf D\text{-}TRef].
\tag{35}
\]

There is no rule

\[
operatorname{SurvivedAttempt}_{D}(h)\Longrightarrow
operatorname{Confirmed}(h).
\tag{36}
\]

The fallibility requirement is recorded as a bridge premise:

\[
operatorname{CreativeProcess}_{\sigma}(\tau)
\Longrightarrow
operatorname{Criticisable}_{\sigma}(\tau)
\quad[\mathsf B\text{-}Fall].
\tag{37}
\]

---

## 6. Spark growth and physical realization

Let \(G_1,G_2,G_3,G_4\) denote, respectively, construction provenance,
consequential exposure, mediated award, and no direct answer insertion.  Put

\[
A5(\tau)\iff G_1(\tau)\land G_2(\tau)\land G_3(\tau)\land G_4(\tau).
\tag{38}
\]

Core growth is

\[
\operatorname{Core}_{\sigma}(\tau)
\iff
A5(\tau)
\land
operatorname{TargetEssential}(\tau)
\land
operatorname{CumulativeExtension}(\tau)
\land
\negoperatorname{SilentObligationRetreat}(\tau).
\tag{39}
\]

Explanatory growth is

\[
\operatorname{Exp}_{\sigma}(\tau)
\iff
operatorname{Core}_{\sigma}(\tau)
\land
operatorname{FirstClassProblem}(\tau)
\land
operatorname{GoodAccount}(\tau)
\land
operatorname{SuccessorRecovery}(\tau).
\tag{40}
\]

The realization witnesses \(W_i\) discharge the corresponding interface
obligations \(R_i\):

\[
W_i(\tau;\sigma)\Longrightarrow R_i(\tau;\sigma)
\qquad(i=1,\ldots,5).
\tag{41}
\]

Their joint use requires coherence:

\[
\frac{
A5(\tau)qquad
W_1(\tau)\land\cdots\land W_5(\tau)qquad
\operatorname{Coh}_{\sigma}(W_1,\ldots,W_5)
}
{operatorname{Realized}_{\sigma}(\tau)}
\;[\mathsf T\text{-}R].
\tag{42}
\]

\(W_0\) is the role-coupled physical knowledge anchor.  Thus

\[
\frac{
operatorname{Core}_{\sigma}(\tau)qquad
operatorname{Realized}_{\sigma}(\tau)qquad
W_0(\tau;\sigma)
}
{operatorname{RealizedCoreGrowth}_{\sigma}(\tau)}
\;[\mathsf T\text{-}RG].
\tag{43}
\]

A physically identified knowledge-bearing extension does not automatically
produce (39).  The converse direction is the bridge conjecture

\[
operatorname{PoiExtension}_{\sigma}(\tau)
\Longrightarrow
\exists\sigma'\;\operatorname{Core}_{\sigma'}(\tau)
\quad[\mathsf B\text{-}Core].
\tag{44}
\]

For explanatory attribution, (40), (42), (43), the critical package in (32),
and boundary-closed provenance must all be present.  The resulting conclusion
is only

\[
operatorname{CriticisableRealizedExpTrace}_{\sigma}(\tau),
\tag{45}
\]

not a truth certificate or a general capacity theorem.

Creative capacity and a creative episode are distinct:

\[
\operatorname{CreativeCap}_{\sigma}(A)
\iff
operatorname{NonSeedConstruction}(A)
\land
operatorname{ConsequentialAppraisal}(A)
\land
operatorname{A5Promotion}(A)
\land
operatorname{OwnedEvaluatedTarget}(A),
\tag{46}
\]

while

\[
operatorname{CriticisableRealizedExpTrace}_{\sigma}(\tau)
\not\Rightarrow
operatorname{CreativeCap}_{\sigma}(A).
\tag{47}
\]

A finite input-output sample cannot establish (46):

\[
\left(\forall x\in F\;f_A(x)=f_C(x)\right)
\not\Rightarrow
operatorname{CreativeCap}_{\sigma}(A)
\qquad(F\text{ finite}).
\tag{48}
\]

---

## 7. Premise-combination tests

For any conclusion \(q\), choose a finite, closed support cone
\(\mathcal P_q\).  The declared test space is

\[
\mathfrak B_q=
\left\{D\subseteq\mathcal P_q:
D\text{ is type-correct and coherent in }\sigma\right\}.
\tag{49}
\]

The task is to compute \(\operatorname{Cn}^{\sigma}_{\mathcal R}(D)\) for
each \(D\in\mathfrak B_q\), not to enumerate all possible theories or
physical systems.

The central target bundles are:

\[
\begin{array}{c|c|c}
q & \text{minimal support form} & \text{required countermodel when a premise is removed}\\ \hline
\operatorname{InfoVar}(X) & (12) & \text{missing permutation or cloning task}\\
\operatorname{PoiKnow}(b,k) & (17) & \text{clonable value without retention or content sensitivity}\\
\operatorname{DigitalGuard}(X) & (25) & \text{remove one identity/recovery premise}\\
\operatorname{SelectionTrace}(V) & (31) & \text{remove inheritance or differential continuation}\\
\operatorname{Problem}_{D}(h\land A) & (32)\text{--}(34) & \text{bare record or undeclared interpretation}\\
\operatorname{TRef}(h^-;h^+) & (35) & \text{adverse result without a good successor}\\
\operatorname{Realized}(\tau) & (42) & \text{remove one }W_i\text{ or coherence}\\
\operatorname{RealizedCoreGrowth}(\tau) & (39),(42),(43) & \text{remove }W_0\text{ or target-essential A5 gain}\\
\operatorname{CriticisableRealizedExpTrace}(\tau) & (40)\text{--}(45) & \text{remove provenance, criticism, or successor recovery}
\end{array}
\tag{50}
\]

For example,

\[
D_R=\{A5,W_1,W_2,W_3,W_4,W_5,\operatorname{Coh}\}
\tag{51}
\]

satisfies

\[
D_R\vdash\operatorname{Realized}(\tau),
\tag{52}
\]

while, for each \(i\),

\[
D_R\setminus\{W_i\}\nvdash\operatorname{Realized}(\tau).
\tag{53}
\]

The latter requires a model in which all remaining witnesses hold but the
corresponding realization face fails.

The required non-entailments include

\[
\begin{aligned}
\operatorname{InfoVar}&\nRightarrow\operatorname{PoiKnow},\\
\operatorname{PoiKnow}&\nRightarrow\operatorname{Exp},\\
\operatorname{SelectionTrace}&\nRightarrow\operatorname{TheoryMediatedCriticism},\\
\operatorname{SelectionTrace}&\nRightarrow H_\sigma,\\
\operatorname{SurvivedAttempt}&\nRightarrow\operatorname{Confirmed},\\
\operatorname{FiniteTest}&\nRightarrow\operatorname{AllTheories},\\
\forall n<\omega\;\exists P_n&\nRightarrow\exists P_\omega.
\end{aligned}
\tag{54}
\]

The final line is especially important: arbitrarily long finite prefixes do
not alone give one infinite compatible history.

---

## 8. Open formulae

The adequacy of any proposed definition of a creator must remain external to
its definition.  For an independently specified case predicate \(J\) on a
declared domain \(\mathcal D\), the characterization claim is

\[
R_{\mathrm{CG}}:
\forall x\in\mathcal D\;
\left[
J(x)\iff
\exists\tau\;\operatorname{CriticisableRealizedExpTrace}_{\sigma_x}(\tau)
\right].
\tag{55}
\]

Equation (55) is a conjecture to be tested with positive cases, matched
negative cases, and declared boundary/frame families.  It is not derivable
from definitions (12)–(46).

No finite \(D\in\mathfrak B_q\) gives any of the following without an
additional theorem about the model class:

\[
\operatorname{CreativeCap}(A),qquad
\operatorname{OpenEndedCreativeCareer}(A),qquad
\operatorname{Confirmed}(h),qquad
\operatorname{AllSubstrates},qquad
\operatorname{AllEnvironments}.
\tag{56}
\]

The mathematical work remaining is therefore precise: complete the rule
register, give a model class and a countermodel for every intended
non-entailment, and prove the stated closure/dependency results.  A program
may later check finite derivation certificates; it is not the calculus itself.