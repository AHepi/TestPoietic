# Episode-Cluster Signature Freeze — Record v1

record_id: SIG-EPI-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: SIGNATURE_FREEZE_EPISODE_V1.md
plain_language_file: SIGNATURE_FREEZE_EPISODE_V1_PLAIN_LANGUAGE.md
digest_manifest: SIGNATURE_FREEZE_EPISODE_V1_FREEZE.json
parent_records: DSF-v1 (Section 3.4(3), Section 3.4(7) second half, Section 13 item 4); SPA-v1 (Section 5.1, unchanged); CAP-v1 (SPA-CAP-v1); HKEY-v1
scope: complete displayed signatures for the episode-cluster primitives of SPA-v1 Section 5.1 (Kind, Pkg, Evid, FDerives, FInterprets, OutcomeSpace, FSuitable, FIncompatible, NonSeed) and the Time_A half of DSF-v1 3.4(7), implementing part of DSF-v1 Section 13 item 4
claims: freezes typed signatures and two acceptance axioms; classifies every addition; names affected cones; records a non-deciding argument
non_claims: does not edit SPA-v1 in place; does not interpret the predicates beyond their signatures; does not supply the episode-to-interface identification (reserved for the cross-fragment identity record); does not test or discharge an original N-row; does not prove creativity or non-creativity

Classification taxonomy: the four buckets of TH-v1/DSF-v1 Section 4
(definition, acceptance axiom, import, bridge). Check structures are record
artifacts, not semantic additions.

## 1. Defect addressed

DSF-v1 3.4(3): Kind, Pkg, Evid, FDerives, FInterprets, OutcomeSpace,
FSuitable, FIncompatible, and NonSeed lack complete displayed signatures,
and no episode carrier identifies an agent episode record with interface
carrier E. DSF-v1 3.4(7), second half: agent transitions are not required
to increase Time_A. This record completes the signatures and the Time_A
condition. The episode-to-E identification is explicitly deferred to the
cross-fragment identity record, because it is an identity condition, not a
signature.

## 2. Carrier inventory used (all from SPA-v1 5.1, read-only)

S (states), Edge, A (agents), Candidate, Assessment, Evidence, Outcome,
Promotion, Policy, Selector = Nodes(Prov), Tau (traces), Prov (finite
provenance DAG), Time_A: S -> N. New named carriers introduced below are
finite and part of the prospective fragment SIG-EPI-v1.

## 3. New carriers (classification: primitive data, finite carriers)

- Problem: carrier of problem tokens p1.
- Account: carrier of account tokens h and successor accounts p2.
- AuxIC: finite carrier of auxiliary/initial-condition tokens; a package's
  Xi is a finite subset of AuxIC.
- Domain: carrier of domain tokens; a package's D is an element.
- Discriminator: carrier of discriminator tokens.
- Protocol_C: carrier of criticism protocols rho (distinct from the
  H-fragment Protocol carrier; no identification is made here).
- InterpGraph: carrier of finite nonempty acyclic interpretation graphs
  I_chi.
- PkgRec: carrier of critical-package records
  chi = (h, Xi, D, d, rho, I_chi, o) with h in Account, Xi in
  P_fin(AuxIC), D in Domain, d in Discriminator, rho in Protocol_C,
  I_chi in InterpGraph, o in Outcome, matching SPA-v1's field gloss
  (target account; auxiliaries/initial conditions; domain; discriminator;
  protocol; interpretation graph; declared outcome). Target(chi) = h is
  its first field, as in SPA-v1.
- EpiRec: carrier of episode records e = (p1, h, chi, omega, p2, tau) with
  p1 in Problem, h in Account, chi in PkgRec, omega in Evidence, p2 in
  Account, tau = (s1,s2,s3,s4) in S^4.
- StateKind: tagged sum carrier
  P1(Problem) | TT(Problem, Account) | EE(Account, PkgRec, Evidence) |
  P2(Problem, Account, PkgRec, Account).

## 4. Completed signatures (classification: primitive data, typed tables)

    Kind:          S -> StateKind
    Pkg:           EpiRec -> PkgRec
    Evid:          EpiRec -> Evidence
    FDerives:      Account x P_fin(AuxIC) x Discriminator -> {0,1}
    FInterprets:   InterpGraph x Evidence x Outcome -> {0,1}
    OutcomeSpace:  Protocol_C -> P_fin(Outcome)
    FSuitable:     Protocol_C x Outcome -> {0,1}
    FIncompatible: Outcome x Discriminator -> {0,1}
    NonSeed:       Candidate -> {0,1}

NonSeed grounding: the Candidate typing is read off SPA-v1 5.2's
FCanConstructNonSeed clause, which applies NonSeed to c with
CandidateOutput(g)=c=Cand(s'), so c is a Candidate. (A provenance-node
reading was considered and rejected: SPA-v1's only occurrence binds a
candidate, not a provenance node.)

Note: SPA-v1 5.1 writes FDerives(h, Xi, d) with the conjunct "d in rho" in
FCritPkg. Under this freeze, d in Discriminator is the package's
discriminator field, and "d in rho" is read as membership of d in the
finite discriminator set declared by rho; Protocol_C records carry such a
set. This reading matches the field gloss (d is the discriminator; the
domain is the separate field D in Domain) and is the minimum reading that
makes the existing conjunct well-typed; it is recorded as a definition
reading, not a new constraint.

## 5. Acceptance axioms

    SIG-EPI-A1 (outcome spaces nonempty):
    for all rho in Protocol_C, OutcomeSpace(rho) is nonempty.
                                          (classification: acceptance axiom)
    Non-redundancy: SPA-v1 states FFallible using exists o' in
    OutcomeSpace(rho); without A1 an empty outcome space would make
    FFallible vacuously false and FCritPkg's o membership impossible.
    A1 excludes structures SPA-v1 does not exclude, so it is a real
    restriction; its non-deciding character is shown in Section 7.

    SIG-EPI-A2 (agent transitions increase time), the second half of
    DSF-v1 3.4(7):
    for all g in Edge and a in A, Owner(g) = a implies
    Time_A(tgt(g)) > Time_A(src(g)).
                                          (classification: acceptance axiom)
    Non-redundancy: SPA-v1 does not state this. Consequence recorded, not
    relied upon: under A2, owned action paths are strictly time-increasing,
    so no owned path cycles; this is intended (it makes owned constructions
    finite-history) and is disclosed because it rules out recurrent
    self-returning agent loops in the fragment.

## 6. Affected dependency cones

- Semantic families: D5 (CritPkg/outcomes/TRef fragment), D6 (episode
  fragment), D8 (CreativeGenerator — only via the episode carrier; its own
  semantics remain OPEN and outside this record).
- DSF-v1 Section 11 items: A-04 (episode/package records), A-05 (finite
  criticism/episode predicates); the FEpi/FCritPkg definitional cluster.
- Audit heads: C-hat, E-hat, TRef-hat, VE-hat (cone membership only).
- Original N-rows (cones only): N3, N5, N9, N11, N13, N14, N15, N16.
- Explicitly examined and unchanged: the H-fragment Boolean tables
  (FPartOf, FCarries, FBlindCopy, FErrorCorrect, FBuildWithResources —
  reserved for the next sweep record); Eq, key, label map, Transport
  (reserved); the episode-to-E identification (reserved for the identity
  record); DSF-F3; all four project bridges.
- ADM-RECHECK-v1's witness pair: unaffected — its reduct uses only Owner,
  Select, Update, and output tables, none of which this record modifies.
  SIG-EPI-A2 is satisfied in both witnesses under the explicit time
  assignment Time_A(s0)=0, Time_A(s1)=1, Time_A(s2)=Time_A(s2')=
  Time_A(s3)=Time_A(s4)=2: every agent-owned edge there moves 0->1 or
  1->2. That assignment is consistent with ADM-RECHECK-v1's stipulation
  (Time_A(s0)=0 strictly below all other states) and refines it; this
  record names that refinement so the dependency is visible.

## 7. Non-deciding argument

Signature completions assign types, not values: for every newly typed
table T and every structure M of SPA-v1 + SPA-CAP-v1, both value
assignments to any row of T remain admissible under SIG-EPI-v1, because no
clause in Sections 3--5 constrains any table entry. Representative check on
the FEpi predicate: fix the minimal episode skeleton of SPA-v1 5.1 (one
record e, one package chi, states s1..s4 with matching Kind values, linked
evidence, closed provenance). Structure M_yes sets the single relevant
FDerives row to 1 and M_no sets it to 0; all other rows and pins agree.
FCritPkg(chi) is true in M_yes and false in M_no, and both structures are
well-typed under SIG-EPI-v1. Therefore the signature freeze entails
neither FCritPkg nor its negation, and the same argument applies row by
row to FInterprets, FSuitable, FIncompatible, and NonSeed, and hence to
FEpi and any downstream head. For SIG-EPI-A1: in a skeleton with nonempty outcome space and time
assignment Time_A(s1)<Time_A(s2)<Time_A(s3)<Time_A(s4), take the
revision edge g_rev: s3->s4 with Owner(g_rev)=external, so SIG-EPI-A2 does
not constrain it. Structure M_fal places g_rev in Rev(tau,o') with
FSuitable(rho,o')=1 and FIncompatible(o',d)=1, making FFallible true;
M_nfal removes g_rev from Rev(tau,o') (leaving the edge itself in place),
making FFallible false; all other pins agree, and FProvenanceClosed is
untouched because g_rev is not an input-node carrier element. Therefore A1
does not decide FFallible; A1 only excludes the degenerate empty-space
structures in which FFallible is vacuously false, and that exclusion is
disclosed in Section 5. (The signature in Section 4 deliberately leaves
OutcomeSpace possibly empty; A1 is what excludes it, so A1 is a real
restriction, not a typing artifact.) For SIG-EPI-A2: both witnesses of ADM-RECHECK-v1 satisfy it, so
A2 does not decide FCreativeCap either.

Steering defense: rationale-based only; no comparative checks were run
against alternative signature choices because none were proposed — the
signatures are read off the existing SPA-v1 uses, and every reading choice
(the FCritPkg domain reading in Section 4) is stated explicitly.

## 8. Forbidden items

No original N-row change; no fixture construction or run; no source bridge
claim; no in-place SPA-v1 edit; no episode-to-interface identification; no
claim about creativity in any real system.

## 9. Residual status and next checkpoint

The episode cluster is now fully typed in the prospective fragment
SIG-EPI-v1. Row readiness is unchanged: PINNED=0, PARTIAL=2, OPEN=18; all
20 rows untestable; zero discharged. Next checkpoint: the H-cluster
signature record (FPartOf, FCarries, FBlindCopy, FErrorCorrect,
FBuildWithResources, Eq, key/label/Transport), then the cross-fragment
identity record (DSF-v1 Section 10 list, including the episode-to-E
identification and the rigid eta/theta/varpi conditions).
