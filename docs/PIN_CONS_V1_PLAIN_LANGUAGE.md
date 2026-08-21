# PIN-CONS-v1 in Plain Language

record: PIN-CONS-v1 (official file: PIN_CONS_V1.md)
status: REVIEWED_PENDING_OWNER_SEAL — two independent review rounds are
complete (first REVISE with six findings, all repaired; second REVISE with
five findings, all confirmed by an independent arbiter, all repaired)

## What this is

The frozen calculus uses some words it never defined — they are "leaves"
with no meaning attached yet. This record proposes fixed meanings for the
first small cluster of them: the words used when the calculus talks about
MOVING A BOUNDARY while keeping the situation comparable. That cluster
feeds two frozen "you cannot infer this" rows: N7 (a boundary move is not
automatically evidence) and N20 (testing a finite list of variants is not
testing all environments).

We are only PINNING candidate meanings — choosing definitions and writing
down why. Nothing is tested, nothing is proved, and no row's status
changes.

## What was decided

- PIN-CONS-D1 — ConservativeExtension. When we move from one context to a
  bigger one, everything sayable in the OLD language keeps its old truth
  value; only genuinely new things may differ. (The textbook notion of
  "conservative extension" is about not proving new theorems in the old
  language; what we pin here is the model-level version — old-language
  truths are preserved exactly under the named embeddings — and the record
  says so explicitly instead of calling it the standard reading.) We rejected a weaker
  version (only a chosen list of facts is preserved — it would tangle the
  definitions together) and a stronger one (everything must stay
  identical — it would forbid exactly the difference row N7 needs).
- PIN-CONS-D2 — SameObservableLabel. The labels you can observe stay the
  same across the move — but this is about LABELS ONLY. Because the frozen
  calculus never actually declared such labels anywhere, this record first
  DECLARES them as new basic data (a per-context "observable-label map",
  item PIN-CONS-D2a, classified as primitive data / definition bucket) and
  then builds the pin on that declared data — the dependency is explicit,
  not hidden. Matching labels
  never means the underlying things are identical. We rejected reading it
  as real identity (too strong, and against the calculus's own rules) and
  as free string-matching (too loose — anyone could fake it).
- PIN-CONS-D3 — MovedConstructorPort. The declared "program port" (the
  named recipe/program attachment point) is tracked across the boundary
  move with its program intact — but whether it still DOES its job in the
  new context is a separate question the pin leaves open. We rejected a
  vacuous version (would delete the limb) and a version that also
  preserves the job. The second rejection does NOT rest on the claim that
  it would pre-decide row N7 — that stronger claim was checked and is
  unproven, because row N7's linkage test never mentions the port's job.
  The rejection stands on the weakest-meaning rule alone: pick the weakest
  reading that works, and preserving the job is strictly stronger.
- PIN-CONS-D5 — FiniteVariantSuite. Already defined in the calculus as
  "a finite sub-list"; we confirm that is ALL it means — being finite
  says nothing about whether the variants actually work elsewhere.
- PIN-CONS-A2 — EverettianUniversalClaim, guard-rail only. A claim about
  ALL environments/universes can never be established from a finite list.
  This is classified as an ACCEPTANCE AXIOM (a rule about which derivations
  are allowed), not a definition, because it does not say what the words
  mean — it only forbids deriving the claim from finite data. What WOULD
  establish it is left undefined, because no frozen row needs that — the
  word only ever appears denied.
- PIN-CONS-A1 — no mixing of witnesses. The same named embedding must be
  used for every part of a boundary-move claim; you cannot prove one part
  with one mapping and another part with a different mapping.

## What was left open, on purpose

- PIN-CONS-OPEN-1 — RetainsOrAdapts. Whether a variant "still works" in a
  new environment needs a bridge to the source literature that we cannot
  yet justify. Pinning it either way would rig row N20 (make its
  counterexample impossible, or guarantee it). So it stays open for the
  next record in this cluster.
- PIN-CONS-OPEN-2 — the positive meaning of EverettianUniversalClaim (see
  A2 above).

## How we know it is not rigged

For the most important pin (D1) we built two concrete example structures
that both satisfy every pin in this record — but in one the boundary move
destroys the linkage (N7's counterexample shape) and in the other it does
not. So the pin itself does not decide the row either way. Similar
flip-two-structures checks cover the label and port pins. Every choice
was made for a stated structural reason; no choice was tested against the
outcome we might want (steering defense: rationale-based only).

## What did NOT change

No N-row was tested, discharged, or reclassified. The readiness counts
stand: 0 pinned rows, 2 partial, 18 open; zero rows discharged; testing
remains PROHIBITED. D0 (the requirement of a total expansion plus a row
bridge before any row can be discharged) is untouched — zero expansions
and zero bridges exist. The frozen calculus, the semantic annex SPA-v1,
and every sealed record are unedited. The SPA-v1 digest is pinned to the
corrected value a9f62ebb... per the sealed erratum. The term catalog this
record cites (ORIGINAL_TERMS_INVENTORY.md) is now pinned too: it has been
committed to the repository and its digest is recorded in this record's
manifest.

## What happens next

The rest of the boundary/substrate cluster (the N17, N18, N19 leaves,
including the delicate SameSyntax/RealizationEq pair that must be pinned
together — this deferral is also logged in the manifest) and the open
RetainsOrAdapts pin go to the next records in this tranche, per the frozen
step order. For transparency: the record whose format this one follows
(IDF-v1) is currently reviewed but awaiting the owner's seal
(REVIEWED_PENDING_OWNER_SEAL).
