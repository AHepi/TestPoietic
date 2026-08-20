# Admissibility Gate Audit v1 — Plain-language version

record_id: ADM-v1
version: 1.0
date: 2026-08-20
status: SEALED_ADMISSIBILITY_CLASSIFICATION_NO_N_DISCHARGE
official_file: ADMISSIBILITY_GATE_AUDIT_V1.md
plain_language_file: ADMISSIBILITY_GATE_AUDIT_V1_PLAIN_LANGUAGE.md
digest_manifest: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json
sha256_official: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json#official_sha256
sha256_plain_language: ADMISSIBILITY_GATE_AUDIT_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: the three downstream formula sites that invoke Admissible_eta or FAdmissible
claims: classifies all three sites; makes the one bucket-2 restriction explicit; proves local two-sided independence of that restriction
non_claims: does not define source-level admissibility, discharge an original N-row, prove an annex-to-source bridge, validate creativity, or establish adequacy of the finite fragment

## The question

The worry was: did we quietly define an "allowed" test case so that it already
contains the answer we wanted?

We counted only places where the maths actually uses the named admissibility
test to open or close a later step. We did not count every ordinary sentence
that happens to use the word "admissible."
Here, an **allowed context** is one candidate situation the test is permitted
to inspect. A **policy table** says which action rule is in use. A **selector
table** says which target is chosen. A **provenance record** is the small table
showing where that target came from. A **fixture** is a deliberately small test
example. **Source-level** means the larger original calculus; **small-model**
means only the finite meanings guide. **A5** is the calculus's full
four-stage promotion check. `widehat Cap` is only an audit label saying five
required records were supplied; it is not a finding of real capacity.

There are exactly three such uses:

- bucket 1, proved from earlier rules: **0**;
- bucket 2, chosen as a rule but shown not to decide the answer: **1**;
- bucket 3, not pinned down well enough yet: **2**.

The one bucket-2 use is the small-model rule called `FAdmissible`. The two
bucket-3 uses are both the larger source-level rule called
`Admissible_eta(A, mu)`.

## The numbered rules for bucket 2

The official record calls the existing meaning ADM-D1 and the new numbered
acceptance rule ADM-A2.

**ADM-D1 — what the small meanings guide calls an allowed context.** A small policy context is
allowed when its state can be reached from the starting state and its target
selector points into the provenance record.

There is an important weakness. In the current small model, every selector is
already defined to be a provenance node. That part of the check is therefore
automatic. Right now ADM-D1 does little more than require a reachable state.
We are stating that openly. We are not claiming this is a complete or
real-world meaning of admissibility.

**ADM-A2 — no choosing the test set after seeing the answer.** This is a new,
numbered rule for accepting future fixtures; it was not already part of
SPA-v1. A test of lasting capacity must use every well-typed context that
passes ADM-D1. There must be at least one and only finitely many such
contexts. The tester is not allowed to remove a
context because it gives an unwanted capacity result, because it belongs to a
particular episode, or because one of the four capacity checks passes or
fails.

This stops a negative result from winning merely by saying, "There were no
allowed cases to inspect."

## Why those rules do not contain the answer

We can keep the allowed-context part exactly the same and build two different
small systems.

Both systems have the same agent, starting point, reachable states, state
clock values, action-rule table, target-choice table, and origin-record node. Both therefore
have the same single allowed context and obey ADM-D1 and ADM-A2.

In the first system, every action edge is owned by an outside party. The agent
has no owned route that makes a new candidate not copied from the starting
seed, judges it using evidence, changes its future action rule, and awards it. The small lasting-capacity claim is false.

In the second system, the same edges are owned by the agent. Their output
tables record a new candidate not copied from the starting seed, a judgment
using evidence, a working change to the future action rule, a full four-stage
promotion, and an evaluated target selected by the agent rather than supplied
from outside. The
small lasting-capacity claim is true.

Because the two systems obey the same admissibility rules but give opposite
capacity answers, those rules do not already say "creative capacity" and do
not already say "no creative capacity." That is the result called ADM-T1 in
the official record.

This is only a check of the small meanings guide. It is not the promised
episode-versus-capacity example, not a full model of the source theory, not a
bridge back to the source-level words, and not a proof of any original
non-entailment row.

## What remains open in bucket 3

The larger calculus uses `Admissible_eta(A, mu)` twice, but never tells us
exactly what that term means and never proves that it is the same as the small
ADM-D1 definition.

That matters both ways. Someone could make a negative capacity example too
easy by declaring every context inadmissible. Someone could also make the
positive audit gate too easy by simply declaring the needed context
admissible.

For that reason:

- the `widehat Cap` paperwork label has status `OPEN_ADMISSIBILITY_B3` at the
  meaning level, although its paper rule path still exists;
- the "not creative capacity" part of the `ExternalRoutine` small example,
  used by `NC_RETENTION_WITHOUT_EXPLANATION`, also has status
  `OPEN_ADMISSIBILITY_B3`, although its six-part rulebook output does not
  change; and
- these five original rows are explicitly open:

  1. `NE_INFORMATION_NOT_CREATIVITY`;
  2. `NE_RETENTION_NOT_CREATIVITY`;
  3. `NE_WHOLE_CREATOR_NOT_CLONABLE`;
  4. `NE_P1_TT_EE_P2_NOT_GENERATOR`;
  5. `NE_RECIPE_NOT_CREATIVITY`.

They were not previously proved and then taken away. The project had zero
fully discharged rows before this check and still has zero. The new label
`OPEN_ADMISSIBILITY_B3` simply tells a future reader exactly why these five
cannot yet be claimed. Closing that label requires all of the following: give
the larger calculus's allowed-context term an exact meaning; show that meaning
does not contain the wanted answer; build a complete model of the larger
rules; justify the exact link from the small meaning to the original row; and
pass a separate independent review.

## Two other open problems found during this check

These are not included in the three-use count, but they matter for later work.

First, the small high-accuracy-copying route names a system and task without
yet proving that they are the same system and task used by its actual route
witness. The selection-versus-high-accuracy row therefore remains open for a
separate reason.

Second, the physical connection rules are project-added bridge assumptions,
not conclusions proved by the sources. The V-E comparison label, the H-route
label, and the capacity paperwork label also stop without feeding a later
semantic rule. They must not be described as source-derived physical
conclusions.

This record only reports those problems. It does not quietly repair them or
add new bridge assumptions.

## Bottom line

The small allowed-context meaning was chosen, not derived. Its use in future
tests is now controlled by a numbered acceptance rule, and the two-system
example shows that the restriction does not contain the capacity answer. The
two larger uses are still under-defined, so the five named rows and two named
audit items above stay open.

Nothing here proves creativity, non-creativity, or an original physical
non-entailment.
