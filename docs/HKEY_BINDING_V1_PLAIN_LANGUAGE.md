# H Witness-Key Binding — Plain-Language Companion v1

This is the plain-language companion to HKEY_BINDING_V1.md. It says the same
things in everyday words. If the two disagree, the official record wins.

## What problem this solves

The test machinery checks a "key" that names a system, a task, and a
protocol, written (F, T, R). But nothing in the rules said the named system
F has to be the actual vehicle being checked, or that the named task T has
to be the task the checked code actually performs. A witness could pass
while its key pointed at something else entirely. This record adds the
missing connections — for the finite test models only, not for the original
theory.

## What was added

Three new pieces, each labeled by what kind of thing it is.

A lookup table called SysBind that says, for each system name and each
vehicle, whether they belong together. A rule called HKEY-A1 says one system
name may be tied to at most one vehicle. We considered two other ways to do
this — pretending names simply are vehicles, or allowing unlimited
"implements" links — and rejected both: the first claims more than the
source text says, and the second would let one passing vehicle speak for
other vehicles that fail, a mistake the project has seen before under the
label F8-D.

A partial map called tau that says which task a piece of code performs.
"Partial" means some code may perform no task at all; we deliberately did
not assume every code is meaningful. A rule called HKEY-A2 says that if a
witness's key is accepted, tau must cover that witness's code. We rejected a
looser matching relation because it could match the same code to two
different tasks, leaving the key ambiguous about what the code does.

A revised definition of when a key counts as acceptable: the system name
must be tied to the checked vehicle, tau must cover the checked code, and
the task tau gives must equal the named task T. This is a change to a
definition in a new prospective fragment called SPA-HKEY-v1. No existing
frozen document was edited.

## How we know the new pieces are not rigged

The project's own rules require proof that a new restriction does not
secretly decide the outcome of the test it will be used in. Using the same
tiny test model as the earlier threshold fix, we showed three things.

First, with the new connections switched on, the route test still passes
when the error is 1/4 and still fails when the error is 3/4. So the new
pieces do not decide the answer either way.

Second, switching only the new connection off — while everything old,
including the error check, still passes — makes the test fail. So the new
pieces are doing real work; they are not redundant.

Third, we are honest that the choice among design options is defended by
the written reasons above, not by an experiment. An earlier draft claimed
more than that; the independent reviewer caught it, and the claim was
corrected.

## What changed and what did not

Changed, in the prospective fragment only: the definition of an acceptable
key. Affected downstream: the five H-family audit heads, original
non-entailment rows N4 and N6 (as dependency cones only — the rows
themselves are untouched), and one of the cross-fragment identity gaps. A
side benefit is that tau also fills a missing link that an earlier audit
flagged for the task graph, and the record names both users of it.

Not changed: SPA-v1, the calculus, the earlier threshold record, any
original N-row, and the overall readiness counts. No row is any closer to
being testable: the count stays 0 pinned, 2 partial, 18 open, with all 20
rows untestable and none discharged. The finite test proxy still does not
connect to the source-level claim HRep, and the known capacity-typing and
admissibility problems are untouched.

## What happens next

The owner reviewed and sealed this record on 2026-08-20. The remaining
frozen order continues: missing primitive signatures, cross-domain
identities, remaining source terms, and only then any thought of testing.
