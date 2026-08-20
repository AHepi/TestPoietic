# Downstream Semantic Freeze v1 — Plain-language version

record_id: DSF-v1
version: 1.0
date: 2026-08-20
status: SEALED_DEPENDENCY_INVENTORY_TESTING_PROHIBITED
official_file: DOWNSTREAM_SEMANTIC_FREEZE_V1.md
plain_language_file: DOWNSTREAM_SEMANTIC_FREEZE_V1_PLAIN_LANGUAGE.md
digest_manifest: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json
sha256_official: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json#official_sha256
sha256_plain_language: DOWNSTREAM_SEMANTIC_FREEZE_V1_FREEZE.json#plain_language_sha256
parent_records: PIECEMEAL_PREMISE_CALCULUS.md; PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1); ADMISSIBILITY_GATE_AUDIT_V1.md (ADM-v1); TRANCHE_HANDOFF_V1.md (TH-v1); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1)
scope: complete dependency inventory for all 25 unary audit heads, the binary information head, eight report projections, and all 20 original N-rows
claims: freezes the current typed dependencies and pinning status; records newly discovered semantic defects; prohibits original-row testing while any transitive cone is PARTIAL or OPEN
non_claims: does not repair a definition, add a row bridge, construct a fixture, discharge an N-row, validate an imported principle or project bridge, or prove creativity or non-creativity

## The result in one sentence

We checked every meaning needed by every later result, and **none of the
original result paths is ready for a real meaning-level test yet**.

The rule-following calculator still works. What is not ready is the claim that
all the words fed into it have complete, matching meanings.

## What the three labels mean

We apply these labels in order, so they cannot overlap.

1. `PINNED`: every important word in the whole chain has a precise, correctly
   typed meaning in the named kind of small model, and every part that must
   refer to the same object really does.
2. `PARTIAL`: the item is not pinned, but an already frozen record explicitly
   connects a small-model version to that exact item. For one of the twenty
   rows, there must be a preregistered example or test aimed at that exact row;
   merely defining one word used by the row is not enough.
3. `OPEN`: neither of those conditions holds.

Wrong types, undefined words, missing identity links, missing full models,
and missing row bridges are listed separately as blockers. Any one of them
stops testing, but a blocker alone does not decide whether the label is
`PARTIAL` or `OPEN`.

A **head** is an audit result label such as “information route supplied” or
“physical explanatory episode supplied.” A **row** is one of the twenty
claims that one thing does not logically force another. A **bridge** is an
extra project rule connecting two kinds of description. A **row bridge**
would connect a small-model statement to one exact original row. No row
bridge exists yet.

## The counts

For the 25 ordinary audit heads, after following every dependency all the way
back:

- pinned: **0**;
- partial: **12**;
- open: **13**.

The separate two-medium information head is open too.

For the twenty original “does not imply” rows:

- pinned: **0**;
- partial: **2**;
- open: **18**.

All twenty rows are still only registered questions. Zero have been proved by
an accepted model. Therefore no original-row test may begin under this
version.

## The most important new problem

The small capacity model has a genuine type mistake.

It declares an update check that accepts:

1. one assessment;
2. one policy;
3. one selector; and
4. one state.

Later, two capacity checks give it an assessment, an entire policy table, an
entire selector table, and a state. A whole table is not one entry from that
table. It is like declaring a slot for one address and then pushing the whole
phone book into it.

This means two of the four small capacity checks are not valid formulas as
written. The combined small capacity claim is therefore not validly typed.
The positive example used by the earlier admissibility audit does not count
as a proper SPA-v1 model.

We are not quietly choosing a repair. That choice could change the later
results, so it must be frozen before any example is built.

## Correction to the earlier admissibility status

The earlier audit counted:

- bucket 1, proved from earlier rules: 0;
- bucket 2, chosen but independently shown not to decide the answer: 1;
- bucket 3, still open: 2.

Because the supposed bucket-2 proof used the ill-typed capacity formula, that
independence result is not established. The current valid count is:

- bucket 1: **0**;
- bucket 2: **0**;
- bucket 3: **3**.

The earlier ADM-v1 files are kept unchanged as the historical record. This
new record replaces only their current readiness claim. It does not rewrite
history and it does not repair any row.

The larger source-level word `Admissible` is also still undefined. It appears
inside the original capacity claim, but there is no rule saying that it means
the same thing as the small-model word `FAdmissible`.

## The second major problem

The small copying/replication route has a key naming a system and a task. The
route then checks a vehicle field and a copying-task field, but it never says
how those checked fields belong to the named system and task.

They might need equality, a “part of” relation, or an implementation map. We
have not picked one. Until that is frozen, a valid route for one object could
be used as if it belonged to another. The selection-versus-high-fidelity row
therefore stays partial and cannot be tested.

There is also no declared type for the route's allowed-error threshold, even
though the formula compares that threshold with rational-number error values.

## Other missing or weak meanings

The detailed official record freezes all of these problems:

- the task graph, copying route, and interface use separate task and code
  carriers without complete maps tying them together;
- the route's recovery/error-family list is not the same field as its
  environment, and neither the copying-task field nor that recovery list has
  the displayed embedding required by the task graph;
- an output and an error calculation are required to come from the same code
  family, but that check is only written in prose;
- several episode tables are used without complete input/output type
  declarations;
- several copying-route checks are bare yes/no tables with no declared
  signatures or deeper meaning;
- the selection equation table has no formal signature, and its agreement
  with the evaluation table is only prose;
- the interface key, display-label map, and identity-transport records are not
  completely typed;
- a selected edge is not formally required to have the source and target
  states supplied to the selection call;
- agent transitions are not formally required to move forward in time; and
- the “every next target is external” flag has no declared yes/no output type,
  so its proposed redundancy is not yet a formal result.

Several checks are also automatic because of how their types were already
declared. For example, the current small admissibility rule mostly says only
that a state is reachable. Such checks may still be useful reminders, but
they do not provide independent evidence.

## Three different layers

The project now keeps three things separate.

1. **The audit calculator.** Given supplied certificates, it calculates which
   labels appear and which report status wins. This part is exact.
2. **The original meanings.** These are the claims about information,
   knowledge, selection, explanation, physical realization, and capacity.
   Many of their basic terms are still not given working model meanings.
3. **The small-model meanings guide.** SPA-v1 gives useful finite versions of
   selection, copying, episodes, capacity, and interface matching. Its names
   begin with `F`. These are not automatically the original meanings.

To prove an original row later, one model must satisfy all original rules and
there must be a separately checked bridge connecting the small-model formula
to that exact original row. There are currently zero such full models and
zero such row bridges.

## What is fixed and what is not

The calculator's 44 input meanings, rule supports, result priorities, and
eight report functions are frozen exactly by the earlier calculus and its
file hash. The calculator is not allowed to turn a missing input into “false”
or “not creative.”

The finite task functions and the local digital-code lemma are precise inside
their own small tables. The finite selection, episode, copying-route,
capacity, and interface sections have useful pieces, but each still has at
least one missing type, free yes/no gate, missing identity, or missing bridge.

The source-only areas with no adequate small-model meanings include:

- information variables and physical knowledge;
- recipe knowledge and multiple realization;
- Spark core and explanatory growth;
- the full physical explanatory episode;
- whole-agent copying and whole-agent digitality;
- possible tasks versus actual knowledge;
- creative-generator role completeness;
- theory suites and passing a theory;
- records, deductions, predictions, and confirmation;
- represented conjectures and theory-guided criticism;
- final outputs and all possible critics;
- high-level role equality, extra substance, and causal exemption;
- same-syntax substrate swaps and counterfactual copying roles; and
- extension to new environments and universal claims.

## The four project bridges

The project has four explicit extra connecting rules:

1. a fallible-selection/critical-episode analogy;
2. a connection from the kernel realization map to the program port;
3. a connection from explanation, realization, episode, and alignment to a
   physical explanatory episode; and
4. a connection from that physical episode plus a tentative refutation to a
   physical refutational episode.

They remain bridges, not proved facts. None uses its own result as an input,
so there is no simple written circle. Their adequacy is still unproved. The
first bridge ends in a label that no later rule and no report uses.

## Status of all twenty rows

`PARTIAL` below means that SPA-v1 preregistered a small-model target for that
exact row. It still does not mean that the original denial is proved.

| No. | Plain statement | Status and essential blocker |
|---:|---|---|
| 1 | information does not by itself give current knowledge | OPEN: original information and retention meanings and their bridge are missing |
| 2 | information does not by itself give creative capacity | OPEN: information, capacity, and their bridge are not pinned |
| 3 | retention or recipe knowledge does not by itself give creativity | OPEN: knowledge, explanation, realization, capacity, and their joins are not all pinned |
| 4 | selection does not by itself give high-fidelity reproduction | PARTIAL: an exact finite proxy was preregistered, but source denials, key binding, threshold typing, and a row bridge are missing |
| 5 | selection is not automatically represented criticism | OPEN: finite selection and criticism pieces were not preregistered as this exact row |
| 6 | a creative agent is not automatically clonable, digital, or self-reproducing | OPEN: capacity and whole-agent copying meanings are missing |
| 7 | a valid link in one boundary followed by moving or extending that boundary does not guarantee a valid link in the extended boundary | OPEN: the interface fixtures test witness splicing, not the exact boundary-extension claim |
| 8 | a finite theory test does not cover every theory | OPEN: theory-suite, pass, and extension meanings are missing |
| 9 | one P1-to-TT-to-EE-to-P2 episode is not a lasting creative generator | PARTIAL: an exact finite target was preregistered, but capacity is ill-typed, generator meaning is missing, and no row bridge exists |
| 10 | a possible task does not imply prior current knowledge | OPEN: possibility and current-bearer knowledge meanings are missing |
| 11 | a recipe does not by itself give creativity | OPEN: recipe, capacity, physical explanation, and their joins are not pinned |
| 12 | an artifact does not by itself give recipe or explanatory knowledge | OPEN: artifact, recipe, and explanatory-growth meanings are missing |
| 13 | a bare record, deduction, or prediction is not yet critical evidence | OPEN: those source terms and the complete critical package are not pinned |
| 14 | surviving a test is not confirmation | OPEN: survival, confirmation, and the relevant model semantics are missing |
| 15 | variation is not literally a represented conjecture or criticism | OPEN: the analogy bridge and the represented-theory terms are not pinned |
| 16 | a final or unrefutable output is not automatically creative | OPEN: critic, final-output, and physical-explanation meanings are missing |
| 17 | a high-level role does not imply extra substance or causal exemption | OPEN: all three source-level meanings are missing |
| 18 | matching labels or syntax do not guarantee a valid substrate swap | OPEN: swap and realization-equivalence meanings are missing |
| 19 | one copy does not establish a counterfactual knowledge, selection, or replication role | OPEN: single-copy and role meanings are missing |
| 20 | finitely many variants and environments do not cover all environments | OPEN: extension, adaptation, and universal-claim meanings are missing |

All twenty remain `REGISTERED_SCHEMA [N]`; zero are discharged and none may
be tested as an original row in this version.

## Report labels do not change this result

The eight report calculations are exact: the six main columns plus the
two-medium-information and multiple-realization checks. Their “not
applicable,” “not established,” and priority rules are fixed.

But an exact report function cannot make an unpinned input meaningful. A
report can say that a certificate route passed; it cannot by itself say that
the corresponding source claim is true in the world.

Two audit heads are not reported anywhere at all: the variation/error-
elimination analogy head and the capacity head.

## Rules against mixing unrelated witnesses

A future model must show that the same actual tokens are used for:

- the information, retained knowledge, critical package, and episode arrows;
- the exact evidence belonging to that critical package;
- the episode trace and the physical realization trace;
- the retained information token and the final program/knowledge port;
- the target problem and promoted successor account;
- the task, environment, boundary, provenance frame, obligation frame,
  program, and whole scope; and
- the selected realization map and program port.

Matching display names are not enough. Two planned hostile examples,
`IC-SP-001` and `IC-SP-002`, must eventually test wrong joins. They have not
been run, so they prove nothing yet.

## What happens next

The next batch may only finish meanings. It must not build a row example.

In order:

1. choose and freeze a correctly typed update rule without designing it to
   force the wanted answer;
2. only then redo the “restriction does not contain the answer” check;
3. freeze how a copying-route witness belongs to its named system and task;
4. give complete types to the remaining primitive tables;
5. freeze the missing links between the five small-model domains;
6. pin the remaining open original terms; and
7. review every future bridge for its authority grade, adequacy, circularity,
   and protection against mixing witnesses.

Any change creates a new version. It must not overwrite this record or make
these failed readiness results disappear. No original-row testing starts
until the entire row's dependency chain contains no `PARTIAL` or `OPEN` item.
