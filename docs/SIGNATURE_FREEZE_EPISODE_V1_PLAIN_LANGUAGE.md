# Episode-Cluster Signature Freeze — Plain-Language Companion v1

This is the plain-language companion to SIGNATURE_FREEZE_EPISODE_V1.md. It
says the same things in everyday words. If the two disagree, the official
record wins.

## What this is

Several predicates in the project's episode machinery — Kind, Pkg, Evid,
FDerives, FInterprets, OutcomeSpace, FSuitable, FIncompatible, NonSeed —
were used in formulas without ever being given complete types. An earlier
inventory (DSF-v1) flagged this as a gap blocking future tests. This
record gives each of them an exact type, plus two rules: outcome spaces
must be nonempty, and an agent's own moves must strictly increase time.
It changes no existing sealed document.

## Why it matters

A formula whose parts have no types cannot be honestly tested — a checker
can pass or fail it for the wrong reasons. This is the same class of
defect as the capacity-table bug repaired earlier (CAP-v1), but for the
episode side of the fragment, which the planned episode fixtures will
depend on.

## One mistake caught and fixed

The first draft mistyped the package's discriminator field as a domain.
The independent reviewer caught it, because under that typing one of the
existing formulas (FIncompatible applied to the discriminator) would not
typecheck — the freeze would have been internally broken. The types now
match the source's own field order exactly: target account, auxiliaries,
domain, discriminator, protocol, interpretation graph, declared outcome.

## How we know the new types are not rigged

Types constrain shape, not content. The record shows that for each newly
typed table, both possible answers remain reachable: flipping a single
FDerives entry flips the package check while everything else stays fixed,
and the fallibility check can be made true or false by moving one external
revision edge in or out of the revision table, under time values that
satisfy the new time-increase rule. So the freeze decides nothing.

## What changed and what did not

Changed, in a new prospective fragment SIG-EPI-v1: the nine signatures and
two acceptance axioms, all classified. Explicitly not done here: the typing
of the H-route Boolean tables and of Eq, key, label, and Transport (next
record), and the identification of episode records with interface objects
(the identity record after that). Row readiness is unchanged: 0 pinned,
2 partial, 18 open, all 20 rows untestable, none discharged. The two
earlier witness structures (from the admissibility re-check) still work
under the new time rule, with an explicit time assignment now recorded.

## What happens next

The H-cluster signature record, then the cross-fragment identity freeze.
The owner seals this record when ready.
