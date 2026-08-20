# H/J-Cluster Signature Freeze — Plain-Language Companion v1

This is the plain-language companion to SIGNATURE_FREEZE_HJ_V1.md. It says
the same things in everyday words. If the two disagree, the official record
wins.

## What this is

Another batch of missing types, this time on the replication-route and
interface side: five Boolean tables the route check relies on (FPartOf,
FCarries, FBlindCopy, FErrorCorrect, FBuildWithResources), the population
fragment's Eq table, and the interface's key, label, and Transport maps.
All get exact types in a new prospective fragment called SIG-HJ-v1. One
thing gets more than a type: Eq is identified outright with the already
defined Eval table, which is what the source text always intended — this
removes a redundant primitive rather than adding anything.

## A real collision, recorded not resolved

The witness record's code field is read by one earlier record (HKEY-v1) as
a piece of code whose implemented task is computed by a map called tau,
while the route check feeds the same field into a task-graph predicate
that expects a task, not code. The two readings collide. This record picks
the disclosed reading that makes everything typecheck — the field is code,
and the task-graph predicate receives its implemented task via tau — and
writes down the leftover question (should error correction key on the code
or on the task?) as a named open item for the identity record. Nothing was
silently papered over.

The reviewer also caught this record initially typing the error-correction
table against the task carrier while its parent record had already typed
the same field as code — the write-up above is the fix.

## What else is in here

Transport gets its first real rule: any transported pair must agree on
every key field. The source prose was ambiguous between a weak and a
strong reading; the record takes the strong one and says so. Label
equality is still never identity. A pre-existing tension in the source
(tasks declared total in one section, called partial in the next) is
recorded as a second named open item, not resolved.

## How we know it is not rigged

Same argument as the episode record: the new types constrain shape, not
content, and the record shows each table can still take either value.
Eq's identification adds no freedom and removes none that was legitimately
present. The Transport rule is shown non-deciding: both an empty Transport
and an identity-only Transport satisfy it, and no existing clause uses
Transport at all.

## What changed and what did not

Changed in SIG-HJ-v1 only: the signatures, the Eq identification, and the
Transport rule. Unchanged: every prior record, every N-row, the readiness
counts (0 pinned, 2 partial, 18 open, none discharged, testing
prohibited). The mandatory interface fixtures IC-SP-001 and IC-SP-002 are
named as consumers of this schema but are not run — running anything is
still forbidden.

## What happens next

The cross-fragment identity record: which carriers across the task,
population, replication, agent, and interface fragments are the same
object, including the two open items named above. The owner seals this
record when ready.
