# Cross-Fragment Identity Freeze — Record v1

record_id: IDF-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: IDENTITY_FREEZE_V1.md
plain_language_file: IDENTITY_FREEZE_V1_PLAIN_LANGUAGE.md
digest_manifest: IDENTITY_FREEZE_V1_FREEZE.json
parent_records: DSF-v1 (Section 10, Section 13 item 4); SPA-v1 (Sections 3--6, unchanged; pinned per ERR-SPA-v1 to the committed bytes a9f62ebb..., the defective pin 40681e6c... retired); ERR-SPA-v1 (governing re-binding erratum); HKEY-v1; CAP-v1; SIG-EPI-v1; SIG-HJ-v1; RPS-v1
scope: named, classified cross-fragment identity decisions for the still-open identity list of DSF-v1 Section 10, the episode-to-E identification deferred from SIG-EPI-v1, and the two named open items SIG-HJ-OPEN-1 and SIG-HJ-OPEN-2
claims: freezes carrier identifications and typed embeddings with per-decision classifications; resolves SIG-HJ-OPEN-1 and SIG-HJ-OPEN-2 as disclosed definition readings; records per-cluster non-deciding arguments; names affected dependency cones
non_claims: does not edit SPA-v1 or any sealed record in place; does not test, discharge, or change any original N-row; does not construct or run a fixture (IC-SP-001/002 remain unrun); does not claim any source-level bridge; does not identify any J obligation frame with an original T, Lambda, or Lambda-prime; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4
(definition, acceptance axiom, import, bridge). Check structures are record
artifacts, not semantic additions. Label equality is never identity:
throughout, an identification is an actual carrier identification or a typed
embedding, never a matching of display labels or of the label map ell.

## 1. Scope and method

DSF-v1 Section 10 froze the requirement that future models preserve, in one
typed context, the shared endpoint/key structure of the IR/RE/CE arrows, the
critical package and evidence token, the episode/realization trace complex,
and the selected realization map and program port. It left nine
cross-fragment identities open. SIG-HJ-v1 added two named open items
(SIG-HJ-OPEN-1, SIG-HJ-OPEN-2) and reserved every cross-fragment carrier
identification for this record. SIG-EPI-v1 deferred the episode-to-interface
identification here.

Method rule (inherited): each identification is the WEAKEST one that makes
the existing SPA-v1 uses well-typed. Where two readings are possible, both
are stated, one is chosen, and the choice is recorded as load-bearing. Every
decision is named IDENT-D<n> and classified; new constraints are named
IDENT-A<n> and classified as acceptance axioms.

All identifications live in a prospective additive fragment, SPA-IDENT-v1,
which supersedes nothing and edits nothing: SPA-v1, SPA-H-THRESH-v1,
SPA-HKEY-v1, SPA-CAP-v1, SIG-EPI-v1, and SIG-HJ-v1 remain as written.

## 2. IDENT-D1: one task carrier across K, H, and J (definition)

SPA-v1 uses three task notions: K's task indices C with f_C: D_C -> Q
(Section 3), H's Task carrier ranged over by T in hkey(w)=(F,T,R) (Section
4.2), and J's Task carrier, the codomain of frameTask and scopeTask and the
key field D_T (Section 6.1). DSF-v1 Section 10 lists "common task carrier
across K/H/J" as open.

Decision: there is ONE finite task carrier, denoted Task, and

    Task  =  K's task index carrier Ccal  =  H's Task  =  J's Task.

K's per-task data (D_C, f_C) become dependent data over Task. HKEY-v1's
tau: Code -> Task and the SIG-HJ-v1 collision reading (FDG_K receives
tau(w.C_Sigma)) are already typed against this carrier and are unchanged.

Weakest-identification note: no map, quotient, or equivalence relation is
introduced; the three names denote one carrier. The rejected stronger
alternative (a task-isomorphism relation between three kept-distinct
carriers) adds structure no SPA-v1 use requires and invites the label-style
confusion this record exists to exclude.

## 3. IDENT-D2: H code families embedded into K states (definition, typed embedding)

DSF-v1 3.4(1): FDG_K expects a task in the task-graph carrier and code/error
subsets of its state carrier Q, while FRouteData supplies w.Sigma and
w.E-bold without displayed embeddings. SPA-v1 3.2 already treats Sigma as a
tuple of pairwise disjoint nonempty subsets of Q.

Decision: a typed embedding

    iota: CodeFamily -> P_fin(Q)-families,
    iota(Sigma) = (sigma_1,...,sigma_n), pairwise disjoint nonempty subsets
    of Q,  with  n = |Sigma|-declared cell index count,

and every cell sigma in Cells_Sigma(p) is read through iota as a subset of
Q. The error/recovery family w.E-bold is likewise a family of subsets of Q
(declared per witness, not an element of CodeFamily). FDG_K's code and error
arguments are exactly iota(w.Sigma) and w.E-bold; its task argument remains
tau(w.C_Sigma) per SIG-HJ-v1.

Classification: definition (typed embedding). The word/output fibres
Word_Sigma, Output_Sigma stay inside H; only the cell structure is embedded
into Q. The rejected stronger alternative (identifying code words with K
states) is overcommitment of the same kind as HKEY-v1's rejected S1.

## 4. IDENT-D3 and IDENT-D4: population boundary and environment tied to J (definitions)

IDENT-D3 (definition): P's Boundary carrier IS J's Boundary carrier; a
lineage's boundary field B = pi_B(lambda) is an element of it, and J's
scopeBoundary: Scope -> Boundary is typed against the same carrier.

IDENT-D4 (definition): there is ONE environment carrier, denoted
Environment, and

    Environment  =  P's Env  =  SIG-HJ-v1's EnvH  =  J's Environment.

A lineage's environment field E = pi_E(lambda), a witness's w.E, and J's
environment_E and scopeEnvironment all range over it. This closes the
EnvH/Environment distinction that SIG-HJ-v1 recorded explicitly as not an
identification; the identification is made here, in the record reserved for
it. FBuildWithResources(w, w.Vveh, w.E) and viable(xi, E, u) now share one
environment type, which is what SPA-v1's joint use in FRouteData and the
population fragment already presumed.

Rejected alternative (three carriers plus coercion maps): rejected as
non-weakest; no SPA-v1 clause distinguishes the three environment roles, and
coercions would reintroduce exactly the untyped gap DSF-v1 3.4(1) flagged.

## 5. IDENT-D5: lineage tied to the H route (primitive data plus acceptance axiom)

The selection/H row shape (FSel_P(lambda) and not FPT-HRoute(F,T;R)) is
meaningless as one model claim unless the lineage's population and the
route's checked vehicle are tied. HKEY-v1 named this cone "lineage tied to
H route" and left the identity portion here.

Decision, two parts:

    IDENT-D5a (primitive data): a partial map
        veh: U -> Vehicle
    assigning a checked vehicle to a population member. Partiality matches
    HKEY-v1's Q1/Q2 discipline: totality would stipulate checkability of
    arbitrary population members.

    IDENT-A1 (acceptance axiom, joint-certificate tie):
    any certificate invoking both FSel_P(lambda) and FPT-HRoute(F,T;R)
    with witness w must exhibit u in pi_V(lambda) with veh(u) defined,
    veh(u) = w.Vveh, and SysBind(F, w.Vveh) = 1.

A1 constrains only JOINT certificates; it says nothing about FSel alone or
FPT-HRoute alone. NEGATION SCOPE, pinned explicitly (repair): A1 applies to
every joint invocation regardless of polarity — including the negative
invocation in the N4 row shape (FSel_P(lambda) AND NOT FPT-HRoute(F,T;R)),
i.e. counter-witness/failure invocations count as invocations. Justification:
a certificate asserting the N4 row shape is still one certificate invoking
BOTH predicates; exempting the negative case would readmit exactly the
mixed pairing (a satisfying selection lineage over one population with a
FAILING route over an SysBind-unrelated vehicle) that the tie exists to
exclude, and would do so precisely in the failure rows. The weaker
per-positive-application alternative (A1 binds only when both predicates
are invoked positively) was considered and rejected for that reason: it
would leave the N4-shaped joint claims untied, which is the primary case
DSF-v1 Section 10's selection/route pairing cares about. It is the weakest
tie that makes the row shape a single
claim about one system rather than two claims about unrelated carriers.
This is recorded as the one decision in this record that could conceivably
force an outcome — a certificate that pairs a satisfying selection lineage
with a failing route over an UNRELATED vehicle is excluded by A1 — and it
is flagged prominently for exactly that reason. Its non-deciding character
for each conjunct separately is shown in Section 13.

## 6. IDENT-D6: agent episode/package/trace tied to J, including the episode-to-E identification (definitions)

This discharges the identification deferred from SIG-EPI-v1. Decisions
(D6a--D6e carrier identifications and embeddings, definition; the omega
reading reclassified as primitive data plus acceptance axiom IDENT-A3):

    IDENT-D6a: J's E  =  SIG-EPI-v1's EpiRec. An interface episode token IS
        an agent episode record e = (p1, h, chi, omega, p2, tau).
    IDENT-D6b: J's Chi  =  SIG-EPI-v1's PkgRec; J's Omega  =  A's Evidence
        carrier; J's Tau  =  A's Tau trace carrier; J's Problem  =
        SIG-EPI-v1's Problem; J's Account  =  SIG-EPI-v1's Account.
    IDENT-D6c (field coherence, definitional equalities, not new axioms,
        except where reclassified below):
        PkgOf(e) = Pkg(e) = chi;  EvidOf(e) = Evid(e) = omega;
        trace_E(e) = the episode trace tau of e;
        p1_E(e) = p1;  target_E(e) = acc2prob(h)  (see IDENT-D6d);
        hplus_E(e) = h;  succ_E(e) = p2;
        prov_E(e) = the provenance frame of e  (see IDENT-D6e).

    IDENT-D6c' (definition; REPAIR supplying the missing Tau typing, new
        in this cycle): the clause "trace_E(e) = the episode trace tau of
        e" was previously ungrounded in type: SIG-EPI-v1 types the episode
        record's tau field in S^4 (tau = (s1,s2,s3,s4) with ordered
        transitions), while SPA-v1 6.1 declares trace_E: E -> Tau, so
        the equality as first drafted related elements of different
        carriers. Explicit typed identification, classified as definition
        (typing repair, not a new constraint): the episode trace tau of e
        is DECLARED an element of Tau, J's trace carrier, and trace_E(e)
        IS that element. Grounding note: SPA-v1 5.1 already implicitly
        treats tau as a Tau element — FProvenanceClosed applies
        InputNodes: Tau -> P_fin(Nodes(Prov)) directly to tau, and
        FFallible applies Rev: Tau x Outcome -> P_fin(Edge) to it — so
        this declaration makes explicit a typing the annex already uses;
        it does not re-type the S^4 presentation, which stands as the
        concrete tuple form of a Tau element. Non-deciding for this axis
        by typing-repair reasoning: assigning denotation to tau inside
        Tau adds no constraint on any table entry.

    IDENT-D6d (definition, Problem/Account relationship decision;
        REPAIR of the D6c carrier typing): SIG-EPI-v1 types h in Account
        with Problem and Account distinct carriers, while SPA-v1 6.1
        declares target_E: E -> Problem and FPEALIGN requires
        p1_E(e) = target_E(e) = target_R(r). An unmediated
        target_E(e) = h is therefore ill-typed. Decision (weakest coherent
        option, classified as definition): Account is embedded into Problem
        by a declared typed embedding
            acc2prob: Account -> Problem,
        and the D6c clauses read hplus_E(e) = h (in Account) and
        target_E(e) = acc2prob(h) (in Problem). Consequences traced for
        FPEALIGN: its equality chain now reads
            p1_E(e) = target_E(e) = target_R(r)
            i.e.  p1 = acc2prob(h) = target_R(r),
        a well-typed equality in the single carrier Problem, with p1_E and
        target_R unchanged. The rejected alternatives were (i) re-typing
        target_E's codomain to Account, which would require an in-place
        edit of SPA-v1 6.1 (forbidden by this record's non-claims) and
        would break FPEALIGN's other conjuncts typed in Problem; and (ii)
        identifying Account = Problem outright, a stronger carrier
        identification no SPA-v1 use requires.

    IDENT-D6e (primitive data; REPAIR supplying the missing ProvFrame):
        SIG-EPI-v1's EpiRec has no Prov field, so J's ProvFrame and prov_E
        were left ungrounded. Decision (weakest complete option): J's
        ProvFrame is identified with a frame-record carrier over
        SIG-EPI-v1's provenance-DAG carrier (the carrier over which
        FDerives is defined), and
            prov_E: E -> ProvFrame
        is declared as primitive data assigning each episode its provenance
        frame over that DAG. No definitional equality into EpiRec fields is
        claimed, because no such field exists; classifying prov_E as
        primitive data (not a definition) is the honest typing.

    IDENT-A3 (acceptance axiom; RECLASSIFICATION of the omega clause):
        the earlier draft's "omega(chi) = the package's evidence field"
        clause is ill-founded: PkgRec has no evidence field, so that
        clause defined a map out of a nonexistent field. Corrected
        classification, stated explicitly: the episode-level reading
            omega: Chi -> Omega
        is PRIMITIVE DATA (load-bearing in FJOIN_CE), not a definitional
        equality, and IDENT-A3 ties it to the episode record: for every
        episode e = (p1, h, chi, omega, p2, tau), omega(chi) = omega —
        i.e. the package-level evidence map agrees with the episode's
        Evid field wherever both are present. FJOIN_CE's EvidOf agreement
        conjunct is thereby well-typed via EvidOf(e) = omega (D6c) plus
        IDENT-A3.

Under D6 (with D6d/D6e/IDENT-A3), SPA-v1 6.1's FJOIN_CE condition
(PkgOf(tgt_CE(gamma)) = src_CE(gamma), EvidOf agreement) is exactly the
interface reading of FEvidenceLinked, and DSF-v1 Section 10's preserved
item "critical package and exact evidence token" is a field equality in
one record, not label matching. The rejected weaker alternative (E and
EpiRec kept distinct with a correspondence map) was considered and
rejected: it leaves the FEpi/FLinked relationship unexpressed, which is
precisely the gap DSF-v1 3.4(3) recorded.

## 7. IDENT-D7: H witnesses tied to J realization/program (primitive data plus definition)

J's alignment clause FPEALIGN quantifies over e in E, r in R, p in P with
uses(r,p)=1 and program(p) = program_R(r). The H side supplies witnesses w
with protocol chains w.c = (c_0,...,c_{N_R}).

    IDENT-D7a (primitive data; REPAIRED, second cycle): a plain map
        rho: R -> W
    sending each J-level realization to an H witness. NO injectivity is
    required or claimed, and surjectivity is not claimed either (not every
    witness need be a J-level realization). Justification (one paragraph,
    per the review): no SPA-v1 clause anywhere requires rho to be
    injective — every use of rho in this record (D7b's definition of
    program_R(r) as the chain of rho(r), and FPEALIGN's program equality
    read through it) is pointwise in r and never quantifies over pairs of
    realizations sharing a witness, so injectivity was an unforced
    strengthening. The choice between the two repairs offered by the
    review — downgrading rho to a plain map versus keeping injectivity as
    an acceptance axiom with its own exclusion check — is resolved in
    favour of the downgrade because it is the weakest typing consistent
    with all uses: keeping an injectivity axiom would exclude structures
    (two realizations sharing one witness) that no fragment use needs
    excluded, and this record's standing method rule is to choose the
    weakest identification that makes the existing SPA-v1 uses well-typed.
    The rejected alternative (injectivity reclassified as an acceptance
    axiom) is recorded as rejected for exactly that reason. Non-deciding:
    see Section 13, Cluster 3, where the witness argument is unchanged —
    a plain map adds no table constraint, and the exhibited pair of
    structures satisfies the downgraded D7a and still flips the tested
    predicate.

    IDENT-D7b (definition): the Program carrier is the carrier of finite
    protocol-chain records (R, c_0,...,c_{N_R}); program_R(r) is DEFINED as
    the chain of rho(r) under its hkey protocol, and program: P -> Program
    remains primitive data over that carrier. The FPEALIGN conjunct
    program(p) = program_R(r) is thereby a well-typed equality of chain
    records, not a label comparison.

This supplies DSF-v1 Section 10's "selected realization map and program
port" preservation at the fragment level. It is not the original-row bridge
DSF-B2; that bridge keeps its B grade and is untouched.

## 8. IDENT-D8: J obligation frames — internal structure decided, original tie refused (definition; one open sub-item)

    IDENT-D8 (definition; REPAIRED typing, second repair cycle): SPA-v1
    6.1 declares D_Lambda = D_Lambda' = ObligationFrame and FPEALIGN
    states the equalities
        val(key(a),Lambda)  = frameLower(frame(e,r,p))
        val(key(a),Lambda') = frameUpper(frame(e,r,p))
    directly IN ObligationFrame. Those equalities are KEPT verbatim and
    unmodified; the earlier draft's displayed equation, which interposed
    obLower between frameLower(frame(...)) and val(key(a),Lambda), was
    ill-typed under SPA-v1 (frameLower lands in ObligationFrame, not in a
    lower-field carrier) and misquoted FPEALIGN; it is withdrawn. What
    this record decides is INTERNAL STRUCTURE of ObligationFrame elements
    only: ObligationFrame is declared a two-field record carrier with NEW
    projection names
        obLower, obUpper: ObligationFrame -> (lower/upper field carriers),
    projecting OUT of ObligationFrame; they are never interposed in the
    FPEALIGN equation. Equivalently: the key's Lambda value IS an
    obligation frame (equal, by FPEALIGN, to frameLower(frame(e,r,p))),
    and obLower/obUpper read its two fields after the fact. D_Lambda and
    D_Lambda' are NOT re-typed; frameLower/frameUpper keep their declared
    types AlignFrame -> ObligationFrame. Non-deciding for this axis by
    typing-repair reasoning: declaring internal field structure and
    projections assigns denotation to ObligationFrame elements and adds no
    constraint on any table entry — no fragment predicate mentions
    obLower/obUpper. The rejected alternative (typing ObligationFrame
    abstractly with no internal structure) was not needed: the record
    structure with fresh projection names is weaker than withdrawing the
    structure and resolves the direction contradiction at zero cost to
    SPA-v1.

REFUSED AND LEFT OPEN — IDENT-OPEN-1: identifying J's obligation frames
with the ORIGINAL T, Lambda, Lambda-prime of the frozen calculus is not
decided here. Reason: that identification is row-bridge content — it is
part of what DSF-B3/DSF-B4 and any Expand certificate must establish in a
total expansion Mhat — and this tranche's governing rules forbid any source
bridge claim. Recording it as a definition would smuggle a bridge into an
identity record. IDENT-OPEN-1 is assigned to the future expansion/row-bridge
tranche (DSF-v1 Section 13 items 3--6 sequence), not to a signature or
identity sweep.

## 9. IDENT-D9: rigid eta/theta/varpi across all fragments (acceptance axiom)

    IDENT-A2 (acceptance axiom): eta, theta, varpi are ONE rigid triple of
    declared constants per certificate. The eta in FPEALIGN_eta, in
    scope(e,r,p) = eta, and in DSF-D1's class index is one and the same
    element; theta and varpi (including the selected-witness conditions
    varpi30, varpi56, varpi49 of DSF-v1 Section 9) are fixed before model
    construction and may not be reindexed between antecedent and
    conclusion, between fragments, or between Mflat and any expansion
    Mhat.

This restates SPA-v1 Section 2's "rigid declared constants" as a numbered
axiom and supplies the rigid-frame half of DSF-A6; the transport half is
SIG-HJ-A1. Non-redundancy: without A2, a structure could satisfy the
selection conjunct under eta and the route denial under eta' with
ell-equal displays; A2 excludes exactly that. Scope typing: eta in Scope,
with scopeBoundary/scopeTask/scopeEnvironment projecting into the
IDENT-D1/D3/D4 carriers.

## 10. IDENT-D10: complete Transport signature interaction (definition reading; no new constraint)

SIG-HJ-v1 typed Transport as a subset of KeyRec x KeyRec with SIG-HJ-A1
(field preservation). After IDENT-D1--D7, every field carrier D_f of KeyRec
is identified across fragments, so SIG-HJ-A1's quantification over Fld is
now a cross-fragment identity condition rather than an intra-J one.

Decision (definition reading, disclosed): no further axiom is added.
Transport is still not required to be reflexive, symmetric, or transitive;
ell may still be non-injective; label equality is still never identity. The
"interaction" the DSF-v1 list asked for is fully supplied by the carrier
identifications themselves. The rejected stronger alternative (requiring
Transport to be an equivalence, or to exist on all FKeyMatch pairs) is
recorded as rejected: it would add a global constraint SPA-v1 states
nowhere, and SPA-v1's no-splicing guard is explicitly local.

## 11. IDENT-D11: SIG-HJ-OPEN-1 resolved — error correction keys on the code (definition reading; LOAD-BEARING)

The collision: HKEY-v1 and SIG-HJ-v1 read w.C_Sigma as an element of Code
with FDG_K receiving tau(w.C_Sigma); the residual question was whether the
error-CORRECTION claim keys on the code or on the implemented task.

Two readings stated:
- R-code (SELECTED): FErrorCorrect(w, w.C_Sigma, w.p, w.Sigma) keys on the
  code element w.C_Sigma in Code, exactly as SIG-HJ-v1 typed it.
- R-task: error correction keys on the task tau(w.C_Sigma) in Task.

Rationale for R-code: the finite route check is about blind copying and
error correction of the ACTUAL code word w.p against its cells; R-task
would route the check through tau, coupling an error-correction verdict to
tau's definedness and letting an inadmissible-key situation silently change
FErrorCorrect values — the determinacy defect HKEY-v1 rejected as T2, one
level down. R-code is also the weakest reading: it is what the existing
FRouteData text supplies, and it keeps key inadmissibility and
error-correction failure as separate, visible failure modes. Availability
note: the R-task alternative was in any case foreclosed by SIG-HJ-v1's
frozen FErrorCorrect signature, which types the keyed argument in Code;
only R-code was available to this record without a version bump of a
sealed-pending record, which this tranche's rules forbid.

Load-bearing disclosure: the readings diverge whenever tau is undefined on
w.C_Sigma but FErrorCorrect would hold of the code (R-code: the conjunct
can be true while the key is inadmissible; R-task: the conjunct is
ill-typed or false). The choice therefore changes which structures satisfy
FRouteData and is recorded as load-bearing, not absorbed silently.

## 12. IDENT-D12: SIG-HJ-OPEN-2 resolved — total on the declared domain (definition reading; LOAD-BEARING)

The tension: SPA-v1 Section 3 declares every task a TOTAL function
f_C: D_C -> Q with D_C a subset of Q, while Section 3.2's proof says "the
one partial function f_{C_Sigma}".

Two readings stated:
- R-total-on-domain (SELECTED): f_C is total on its declared domain D_C,
  which may be a proper subset of Q; Section 3.2's "partial" is prose for
  "defined only on D_C, hence partial over Q". No formula text changes.
- R-genuinely-partial: tasks are partial maps Q -/> Q; FFace's U subset D_C
  clause becomes a definedness side condition everywhere.

Rationale for R-total-on-domain: it is the weakest reading that makes both
sections true as written, and it preserves SPA-v1 3.1's state-level
single-valuedness argument verbatim. R-genuinely-partial would require
restating every FFace use with a definedness guard — a larger change for no
typed gain.

Disclosed consequence, correctly attributed (repair): the coverage
requirement E_i subset D_{C_Sigma} follows from FFace ALONE (FFace
requires U subset D_C, applied with U = E_i), under BOTH readings; it is
not a restriction introduced by D12. What D12's R-total-on-domain reading
itself decides is only that f_C is total ON D_C (so no definedness guards
are added anywhere) — it retains FFace's pre-existing coverage requirement
verbatim rather than converting it into a definedness side condition.
Structures in which an error state lies outside the declared domain were
ALREADY excluded by FFace under both readings; this is the "common core"
of Cluster 5, and the earlier draft's attribution of that exclusion to D12
is corrected here. The requirement is intended (error correction undefined
on an error state should not count as recovery), and Section 13 shows the
reading choice decides no fragment predicate.

## 13. Non-deciding arguments

Cluster 1 (IDENT-D1, D2, D3, D4, D6, D7b, D10 — pure carrier
identifications and embeddings). Each decision equates names or embeds
carriers; none constrains any table entry. For any structure M of the prior
fragment stack, the identified structure M' (same tables, carriers renamed
per the identifications) satisfies SPA-IDENT-v1 and preserves every
fragment predicate's truth value, because every fragment predicate's
definition is invariant under the renamings. SCOPE RESTRICTION for
IDENT-D2 (repair, corrected in the second cycle): this invariance
argument applies only to structures ADMITTING the embedding iota — i.e.
whose state carrier Q satisfies the single cardinality side condition
that Q accommodates n pairwise disjoint nonempty cell subsets
(n = the declared cell index count of Sigma). That is the whole
condition: whether iota exists at a given Q depends only on Q's
cardinality accommodating the n cells. The earlier draft's additional
requirement that the error sets of w.E-bold lie outside all cells is
withdrawn: it was over-strong and conflated two distinct conditions,
because for structures where FDG_K(FRecover) holds, each
E_i \ union_j sigma_j being nonempty is not a hypothesis on the
structure at all but is DERIVED by SPA-v1 3.2's finite lemma from
FRecover itself — and structures where FDG_K fails are preserved
trivially since the predicate's falsehood is invariant under the
renamings. Structures whose Q is too small to
admit such a family are not claimed to be preserved; the argument is
vacuous for them and is disclosed as such rather than overgeneralized.
Small structure: take the
SIG-EPI-v1 Section 7 skeleton (one episode e, one package chi, s1..s4 with
matching Kind) and set the single relevant FDerives row to 1 (M_yes) or 0
(M_no); after applying D1--D6 both structures remain well-typed, FCritPkg
is still true in one and false in the other. The identifications decide
neither FCritPkg nor its negation; the same holds predicate-wise for FSel,
FDG_K, FPT-HRoute, FLinked, and FCompOK.

Cluster 2 (IDENT-D5/IDENT-A1 — lineage tie). A1 restricts only joint
certificates. Non-deciding per conjunct: fix the HKEY-v1 Check 1 reduct
(FRouteData(w), FImplements(c0,w), epsilon=1/2) together with a one-lineage
population structure with pi_V(lambda)={u}, veh(u)=w.Vveh, SysBind(F,
w.Vveh)=1. M_pass (err=1/4) makes FPT-HRoute true; M_fail (err=3/4) makes
it false; FSel_P(lambda) is held false in both (e.g. |V|=1 defeats the
|V|>=2 clause), and a second pair with |V|=2 and the selection tables
flipped makes FSel true in both while the route pair is unchanged. All four
structures satisfy A1. Therefore A1 decides neither FSel, nor FPT-HRoute,
nor either negation. FORCED-OUTCOME FLAG (prominent, per the governing
rule): A1 DOES exclude the mixed structure that pairs a selection lineage
over one population with a route witness over an SysBind-unrelated vehicle;
that exclusion is the point of the tie, and it is disclosed rather than
hidden. No existing fragment predicate or its negation is forced by it.

Cluster 3 (IDENT-D7a — the rho map; extended to the D6 repair's
primitive data). A plain map adds no table
constraint: take Transport empty, R a singleton {r}, W = {w}, rho(r)=w.
FPEALIGN's program equality holds or fails solely by the program table
entries, which D7b defines but does not constrain; flipping
FImplements(c0,w) between two otherwise identical structures flips
FProtocolChain while every IDENT pin holds. The same argument covers the
repair's new primitive data: omega: Chi -> Omega, prov_E, and acc2prob are
primitive data/maps whose values no fragment predicate table entry depends
on, and IDENT-A3 constrains only the mutual coherence of two pieces of
primitive data (the package-level evidence map and the episode's Evid
field), not any table entry — FEvidenceLinked, FCritPkg, and FJOIN_CE
verdicts can still be flipped between otherwise identical structures
satisfying A3. Non-deciding.

Cluster 4 (IDENT-D9/IDENT-A2 — rigidity). A2 excludes cross-eta reindexing
structures only. Within one rigid triple, the Cluster 1 and Cluster 2
witnesses above already satisfy A2 and still realize both truth values of
the relevant predicates. Non-deciding; the excluded structures are exactly
the splicing structures DSF-v1 Section 10 exists to forbid.

Cluster 5 (IDENT-D11, D12 — the two disclosed readings). Each is a reading
of existing text, not a new constraint on values. For D11: with tau defined
on w.C_Sigma (admissible key), R-code and R-task coincide pointwise on
every FRouteData conjunct, so no predicate value changes in the admissible
fragment; they differ only where the key is already inadmissible, hence
already outside FPT-HRoute's witness. For D12: in the SPA-v1 3.2 skeleton
with E_i subset D_{C_Sigma} declared, FRecover's truth is untouched by the
reading choice; the E_i-not-covered structures are excluded by FFace
itself under both readings' common core (FFace requires U subset D_C), not
by D12 — the reading choice changes only whether totality is stated per
declared domain or per Q. Neither reading decides any fragment predicate or its
negation; both are recorded as load-bearing because they change WHICH
STRUCTURES ARE WELL-TYPED at the margin, not because they change a verdict.

Steering defense: rationale-based only, per the HKEY-v1 downgrade. The
selections (weakest identification; R-code over R-task; R-total-on-domain
over R-genuinely-partial; refusal of the obligation-frame original tie)
rest on the documented structural objections in Sections 2--12
(overcommitment, determinacy, minimality, bridge-scope discipline). No
comparative non-deciding checks were run for rejected alternatives; none is
claimed.

## 14. Affected dependency cones

- Semantic families (DSF-v1 Section 6): D3 (Sel/FSel; via D3/D4/D5 ties),
  D4 (H family; via D1, D2, D5, D7, D11), D5 (CritPkg; via D6), D6 (Epi;
  via D6), D9 (physical route; via D7, D10), D10 (Linked/PEALIGN; via D6,
  D7, D9, D10). D7 (capacity) untouched; DSF-F1/F3 untouched.
- DSF-v1 Section 11 items: K-01/K-03 (task carrier, FDG_K arguments),
  K-02 (FFace, implicated by D12's domain-coverage discussion), P-01
  (Boundary/Env identifications), P-05 (FSel, implicated by D5/IDENT-A1),
  H-01/H-04/H-06 (witness ties, D11), A-04
  (episode-to-E, closing the DSF 3.4(3) residue), J-01/J-02/J-03/J-05
  (carriers and alignment under the identifications), J-07 (IC-SP-001/002
  are consumers of the Transport/key interaction; named, unrun, no run
  obligation created).
- DSF-v1 acceptance items: DSF-A6 (both halves now have named fragment-level
  pins: rigid frame = IDENT-A2, transport = SIG-HJ-A1; this pinning of the
  halves does NOT change DSF-A6's readiness, which remains PARTIAL, resting
  on the unrun fixtures IC-SP-001/002); DSF-A1 unchanged.
- Audit heads (cone membership only): Hsrc-hat through H-hat; Sel-hat,
  FallSel-hat; C-hat, E-hat, TRef-hat, VE-hat; Link-hat, PhysExp-hat,
  PhysRefExp-hat (via D7/D9/D10); Veh-hat, DG-hat (via D2/D11).
- Original N-rows (cones only, rows untouched): N3, N4, N5, N6, N7, N11,
  N15, N16, N19; N9, N13, N14 via the episode carrier only.
- Explicitly unchanged: HKEY-v1's SysBind/tau; CAP-v1; SIG-EPI-v1's
  signatures and A1/A2; SIG-HJ-v1's signatures and A1; all four project
  bridges (DSF-B1..B4 keep grade B, unclaimed); the original T,
  Lambda, Lambda-prime (IDENT-OPEN-1); ADM-v1's counts (B1=0, B2=0, B3=3).

Cone completeness is a MANUAL TRACE over DSF-v1 Sections 6, 10, and 11 with
the exclusions stated explicitly; it should be re-derived mechanically in a
later tranche, subject to the same caveat as HKEY-v1, CAP-v1, SIG-EPI-v1,
and SIG-HJ-v1.

## 15. Forbidden items

No original N-row change; no fixture construction or run (IC-SP-001/002
remain mandatory-but-unrun); no source bridge claim (in particular
IDENT-OPEN-1 refuses the obligation-frame-to-original tie); no in-place
edit of SPA-v1 or any sealed record; no semantic choice justified by a
desired separation; no claim about creativity or non-creativity in any real
system.

## 16. Residual status and next checkpoint

Every still-open cross-fragment identity on the DSF-v1 Section 10 list is
now decided at the fragment level in the prospective fragment SPA-IDENT-v1,
with two exceptions recorded honestly: IDENT-OPEN-1 (obligation frames to
original T, Lambda, Lambda-prime — deferred as bridge content) and the
continuing OPEN status of IC-SP-001/002 (fixture obligations, unrun). Row
readiness is unchanged: PINNED=0, PARTIAL=2, OPEN=18; all 20 rows
untestable; zero discharged; testing remains prohibited. Next checkpoint
per DSF-v1 Section 13: item 5 (pin remaining open original terms), then
item 6 (bridge review), with IDENT-OPEN-1 carried into the expansion/bridge
tranche.
