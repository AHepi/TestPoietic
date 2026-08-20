# Cross-Fragment Identity Freeze — Plain-Language Companion v1

This is the plain-language companion to IDENTITY_FREEZE_V1.md. It says the
same things in everyday words. If the two disagree, the official record
wins.

## What this is

The earlier records gave every table and map an exact type, but they
deliberately left one question untouched: when the task fragment, the
population fragment, the replication fragment, the agent fragment, and the
interface fragment all talk about "the task" or "the environment" or "the
episode," are they talking about the SAME thing? This record answers that,
one identity at a time, in a new prospective fragment called SPA-IDENT-v1.
Nothing already sealed is edited, and matching labels never count as
identity — these are real carrier identifications, not name-matching.

## The identifications, in plain terms

- One task carrier. The three fragments' three "task" notions are declared
  to be one carrier. No quotient, no translation map — one thing with three
  old names.
- Code families live in task states. Each replication-route code family is
  embedded as a family of disjoint cell subsets of the task-graph state
  set, which is exactly what the digital-guard check always assumed.
- One boundary carrier and one environment carrier, shared by the
  population fragment, the replication fragment's environment field, and
  the interface. This closes a gap the H/J record explicitly left open.
- Lineage meets the route. A partial map assigns a checked vehicle to a
  population member, and a new axiom says: any certificate that claims both
  "selection happened" and "the high-fidelity route failed" must be talking
  about one and the same vehicle. The axiom applies even when the route
  claim is a FAILURE claim (the negative case): a certificate saying
  "selection happened AND the route failed" is still one certificate about
  both, so it too must be about one vehicle. The looser alternative — tying
  only certificates where both claims are positive — was considered and
  rejected, because it would leave exactly the failure-row claims untied.
  This is the one place where the record
  could actually force something — it rules out pairing a selection story
  about one system with a route story about an unrelated system — and the
  official record flags that prominently instead of hiding it.
- Episodes are interface tokens. The interface's episode, package,
  evidence, trace, problem, and account carriers ARE the agent fragment's
  episode/package/evidence/trace/problem/account records, field by field.
  This is the identification the episode record deferred. Four repairs are
  disclosed inside it. First, the typing of "the episode's target is its
  account" was wrong (targets live in the problem carrier, accounts in the
  account carrier); the fix declares an explicit embedding of accounts into
  problems, so the interface's target equality now reads "problem part =
  embedded account = the realization's target" — one well-typed equality in
  one carrier. Second, the package-to-evidence map is NOT read off a
  package field (packages have no evidence field); it is reclassified as
  primitive data plus a new axiom saying it agrees with the episode's own
  evidence field wherever both exist. Third, provenance frames, which the
  episode record has no field for, are supplied as a frame record over the
  provenance DAG with the episode-to-frame map declared as primitive data
  rather than pretended to be a field lookup. Fourth (added this cycle):
  the clause "the interface's trace of an episode is the episode's trace"
  was left untyped — the episode record types its trace as a four-state
  tuple, while the interface's trace map lands in the trace carrier. The
  record now declares explicitly, as a named definition, that the
  episode's trace IS an element of the trace carrier — a typing the annex
  already assumed by feeding the trace straight into trace-carrier maps.
- Realizations are witnesses. A plain map sends each interface-level
  realization to a replication witness. The earlier draft required the
  map to be injective (no two realizations sharing a witness); that
  requirement was removed on review, because nothing anywhere in the
  annex or this record ever needs it — every use of the map is
  point-by-point. The alternative of keeping injectivity as an explicit
  axiom was considered and rejected as an unforced strengthening. A
  realization's "program" is defined to be its witness's protocol chain,
  so the interface's program-equality check is a real equality, not a
  label comparison.
- Obligation frames: half decided, half refused. The interface's key
  value for an obligation field IS an obligation frame, exactly equal to
  what the existing frameLower/frameUpper maps return — that equality,
  stated by the interface record, is kept word for word. What this record
  adds is internal structure only: an obligation frame is declared to be
  a two-field record (lower, upper) with its own NEW projection names
  that read the fields out AFTER the fact. An earlier draft had wrongly
  inserted a field projection into the middle of the interface's
  equation, which was a type error and misquoted the interface record;
  that equation is withdrawn. But identifying those
  frames with the ORIGINAL theory and
  obligation levels of the frozen calculus is refused and left open: that
  is bridge territory, and this tranche is forbidden from claiming bridges.
- Rigid frame. One fixed triple (eta, theta, varpi) per certificate, set
  before any model is built, never reindexed mid-argument. This stops the
  trick of satisfying one half of a claim under one frame and the other
  half under another.
- Transport. No new rule beyond the H/J record's field-preservation axiom;
  now that the carriers are identified, that axiom simply means more. It is
  still not required to be an equivalence, and label equality is still
  never identity.

## The two inherited open items, decided

- Code versus task (SIG-HJ-OPEN-1): error correction keys on the CODE, not
  on the implemented task. Keying on the task would let a key-admissibility
  problem silently change an error-correction verdict — the same determinacy
  defect an earlier record rejected elsewhere. Both readings were written
  down; the choice is load-bearing because the readings disagree exactly at
  the boundary of key admissibility, and the record says so. (The task
  reading was in any case unavailable: the H/J record's frozen
  error-correction signature already keys on the code, and changing that
  would have required bumping a sealed-pending record.)
- Total versus partial tasks (SIG-HJ-OPEN-2): every task is total ON ITS
  DECLARED DOMAIN, which may be a proper subset of all states; the source's
  word "partial" is read as "not defined outside that domain." Correction
  of attribution: the requirement that an error-correction task's declared
  domain cover its error sets was ALREADY imposed by the digital-guard
  condition under both readings — it is not new with this decision. What
  this decision settles is only that tasks are total on their declared
  domain, so no definedness guards need to be added anywhere.

## How we know it is not rigged

For each cluster of decisions the record shows a small two-structure check:
two models that agree on every new pin but still disagree on the predicate
in question (a critical package that passes in one and fails in the other;
a route that meets its error bound in one and misses it in the other; a
selection predicate flipped by its own tables only). One scope restriction
is now stated honestly: the invariance argument for the code-family
embedding covers only structures whose state set is big enough to hold
the required number of pairwise disjoint nonempty cells — that size
condition is the whole restriction. An earlier draft additionally
demanded that the error sets sit outside all cells; that was too strong
and mixed up two different things, because wherever the digital-guard
check holds, "each error set has a point outside every cell" is PROVED by
the annex's own lemma, not something we may assume — and where the check
fails, the structures are preserved anyway. Smaller
structures are simply outside the argument. So the identifications
decide no existing fragment predicate and no negation. The single exception
— the lineage-to-route axiom excluding mixed, unrelated-vehicle
certificates — is flagged in the official record as a deliberate,
load-bearing restriction, not discovered later. The defense against
outcome-steering is rationale-based only, as in the earlier records.

## What changed and what did not

Changed in SPA-IDENT-v1 only: the carrier identifications, the embeddings,
the vehicle tie, the rigidity axiom, the new evidence-agreement axiom, the
account-into-problem embedding, the provenance-frame data, and the two
disclosed readings. The dependency-cone list now also names K-02 (the
digital-guard condition, via the domain-coverage discussion) and P-05
(selection, via the lineage tie). One wording repaired: saying the
rigidity-and-transport requirement now has "both halves pinned" means only
that both halves have named fragment-level pins; that requirement's row
stays PARTIAL because the interface fixtures it rests on are still unrun.
Unchanged: every prior record, every bridge grade, every N-row,
and the readiness counts — 0 pinned, 2 partial, 18 open, none discharged,
testing still prohibited. The mandatory interface fixtures IC-SP-001 and
IC-SP-002 are named as consumers of this freeze but are not run; running
anything remains forbidden. The cone list in the official record is a
manual trace and carries that caveat.

## What happens next

The remaining open original terms get pinned (next tranche), then every
bridge gets its grade/adequacy review. The one refused identification —
obligation frames to the original theory levels — travels with that bridge
tranche as named open item IDENT-OPEN-1. The owner seals this record when
ready.
