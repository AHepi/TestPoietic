# PoieticTest Tranche Handoff v1 — Plain-language version

record_id: TH-v1
version: 1.0
date: 2026-08-20
status: SEALED_REPOSITORY_HANDOFF_SEMANTICS_FIRST
official_file: TRANCHE_HANDOFF_V1.md
plain_language_file: TRANCHE_HANDOFF_V1_PLAIN_LANGUAGE.md
digest_manifest: TRANCHE_HANDOFF_V1_FREEZE.json
sha256_official: TRANCHE_HANDOFF_V1_FREEZE.json#official_sha256
sha256_plain_language: TRANCHE_HANDOFF_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; PIECEMEAL_SEMANTIC_ANNEX_V1.md; ADMISSIBILITY_GATE_AUDIT_V1.md; RECORD_PUBLICATION_STANDARD_V1.md
scope: PoieticTest repository checkpoint and the protocol for future bounded tranches
claims: records the current project state, unresolved obligations, and ordered next tranches
non_claims: does not back up the whole computer, discharge an original N-row, prove creativity, expose private key material, or claim that an SSH agent is available

## Where the project is now

This file tells the next worker where to restart.

Only the PoieticTest project is being uploaded. Personal files, passwords,
browser information, Windows files, and unrelated things elsewhere on the
computer are not part of the project and are not being uploaded.

The two ZIP files were checked before removal. Everything inside them was
already in the project. Every ZIP entry was either an exact copy of a current project file or an
older copy of a document that now has a current version in `docs/`. Nothing
unique was lost. The project will keep the real files in their proper folders instead
of keeping duplicate ZIP bundles. Future workers must not make new ZIP bundles
unless the user asks for them.

The project is on branch `agent/stress-test-continuation`. The Git commit that
contains this handoff file is the checkpoint a future worker should use.

## About the SSH key you supplied

The text you supplied is not a file checksum. It is the fingerprint of the
public half of the local `PoieticTest` SSH key. A direct check matched it
exactly, so we know which key you meant.

The private half is encrypted. Its password must never be printed, stored in
this project, or sent through chat. During the latest check, this Codex task
could not see a running SSH key helper, so GitHub refused the SSH login. That
does not mean the key is the wrong key. It means this task could not use the
encrypted private half at that moment. A successful push must still be proved
by the actual push result and by matching the remote commit.
## What has actually been achieved

The project now has a careful rulebook for testing combinations of premises.
It keeps six different kinds of question separate, records 44 requirements,
and refuses several common shortcuts.

It also has a new meanings guide called `SPA-v1`. That guide says what words
such as selection, copying, one episode, lasting capacity, and a valid join
mean inside small test models. This stops a future example from winning by
simply declaring the wanted sentences true.
It now also has `ADM-v1`, an admissibility check. That check found three places
where an "allowed case" rule is used later: none were proved from earlier
rules, one small-model use was chosen but shown not to contain the answer, and
two larger uses are still not defined well enough. The rows that depend on the
two larger uses stay open.

The last checks passed:

- the frozen record manifests replayed correctly;
- the frozen plan was reproduced correctly;
- all 20 focused tests passed;
- the mathematical review accepted the meanings guide; and
- the easy-to-read version kept the important warnings from the official one.
The final wider check ran all 121 current tests, and all 121 passed. An older
campaign replay was not a full match: 8 of its 11 files matched exactly, while
authentication.json, unit_tests.json, and manifest.json differed. The replay's own internal manifest checks were green, and the repository
formatting check passed. Those old evidence files were not rewritten just to
make the check green. The project
must understand that difference before claiming that the whole old campaign
can still be reproduced byte for byte.

## What has not been proved

No original non-entailment claim has yet been proved with a real model. No
actual person or machine has been proved creative or non-creative. The project
has built and checked the rulebook and the meanings needed for the next tests;
it has not yet run those model tests.

There are 20 registered non-entailment claims and zero fully discharged ones.
For the three later uses of the named admissibility rule, the counts are:
zero proved from earlier rules, one chosen rule that does not decide the
answer, and two still-open uses. Five original rows carry the clear label
`OPEN_ADMISSIBILITY_B3`; none was repaired or proved.
A small example will count only as a checked small example unless it is also
connected back to every relevant full rule, checked independently, and
reported only for the exact small class and scope that was tested.

## The next batches of work

### Batch 2 — Freeze every meaning used later

No small example or row test may start yet. First make one complete list of
every meaning used on the path to any reported answer or any of the 20
non-entailment rows. This includes what objects the words apply to, which
systems and times must be the same, which outside assumptions are borrowed,
and exactly how records from different parts may be joined.

For every item, the official record must give the exact rule, say where it
came from, name everything that uses it later, and mark it `PINNED`, `PARTIAL`,
or `OPEN`. Every meaning the project adds itself must have a number and must be labelled
honestly as a definition, an acceptance rule, or a bridge between domains.
Only a rule restricting which test cases are allowed needs the two examples
with the same restriction but opposite tested answers. That shows the
restriction did not hide the wanted answer. A bridge instead needs its added
assumption, authority grade, limits, and circularity check written out.

If any meaning needed by a row is `PARTIAL` or `OPEN`, testing that row is not
allowed. Finding a missing meaning does not give permission to repair the row.
The missing meaning is recorded and remains open.

Two missing pieces are already known. The larger capacity rule uses an
undefined idea of an allowed context. The high-accuracy-copying route names a
system and task without yet proving that they are the ones used by its actual
route witness.

### Batch 3 — Build the small examples

Only after Batch 2 is frozen and independently accepted, build these examples
using exactly the frozen meanings:

1. a population where selection happens but the named high-accuracy copying
   route does not;
2. one problem–idea–test–revision episode that does not show a lasting ability
   to do this independently; and
3. two examples showing that records from different systems or times cannot be
   joined merely because their labels look alike. One must test a broken join;
   the other must allow the first join but reject a later mismatch in the
   physical port or history being used.

Before any example is built, its plan and hash must be locked. A separate
checker must replay it. Even a successful result may be called only a
`VERIFIED_FIXTURE` for that named small class. It does not prove the original
physical claim or a universal claim.

### Batch 4 — Connect a small example to the full rulebook

Start with the selection-versus-high-accuracy-copying claim. Check every
meaning and every link needed by the full frozen rule. Then do the
one-episode-versus-lasting-capacity claim.

Keep every meanings version and the model class fixed during each test. Give a
separate reason why the small-model facts really match the exact full claim,
and have an independent checker inspect the complete model and that link. The
honest outcomes are: discharged only for the named class, unclear or
under-specified, meanings made too strong, or a counterexample to the proposed
link.

If a link fails, record the failure. Do not quietly rewrite the meanings until
the wanted answer appears. A changed meaning needs a new version, and the old
result must remain available.

### Batch 5 — Test against material that did not build the rulebook

Before reading any comparison passage, freeze the calculus, every meanings
record, the rules for mapping source statements into project terms, the
complete list of allowed outside sources, and the rule for choosing from that
list. Then have one person or process state what the chosen passages say in
neutral terms and another map that statement into the frozen project rulebook.

Also test deliberately broken rulebooks. Catching those broken versions shows
only that the checker can catch those named mistakes. It does not prove the
real rulebook is perfect. Agreement with outside source material is only
evidence that the frozen rulebook handled an unseen source consistently. It
does not prove that the outside authority is true and does not show that a
real system is creative.

### Batch 6 — Test a real system only with separate permission

A real-system test needs clear boundaries, evidence, and a full record of
prompts, training, tools, seeds, scores, and human help. Even then, the result
must stay limited and open to criticism. It cannot simply announce
`CREATIVITY_PROVEN`.
## How every future batch must work

Before doing a test, write down one exact job and the exact files it may
change. Record the branch, commit, and whether any files were already changed.
Freeze both the official and easy-to-read plans before starting. Then do only
that job, check it through a separate path, and have a separate read-only
reviewer inspect it. Record a bad or unclear result before changing the rules.

Every new important result must again have an official copy, an easy-to-read
copy, and a hash list joining the two. Commit only the named project files.
Push only after the user clearly asks, then compare the commit on the remote
with the local commit to prove the push reached the intended branch.

Missing evidence must stay “not established”; it cannot be changed into
“false.” A result for one small class cannot be changed into a universal
claim. A borrowed source rule or a project bridge cannot be presented as a
proved fact.

The very next job is to make and freeze the complete downstream meaning list,
then pin one dependency path at a time. No small example, row repair, or row
test may begin while anything needed on that path is still partial or open.
