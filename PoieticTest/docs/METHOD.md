# Verification method

## Boundary and evidence grades

The audited subject is the exact 1,805-line file pinned in `subject/` by
SHA-256. The three predecessor/criticism artifacts named by its provenance
ledger are also present and byte-checked. Prior evidence is retained as prior
evidence; it is not silently regenerated or rewritten.

This campaign separates source authentication, source/protocol linting,
formal finite models, bounded theorem checks, empirical replay, and
interpretation. A result can therefore be reproduced without treating every
green checker as support for the theory. Each report row names the mechanism,
the exact lines reached, the outcome, and the scope that cannot be crossed.

Commit `d04bd2273121427166cd4fe9442ff595db959fbd` is the
content-addressed semantic/preregistration freeze. The remote branch
`freeze/stress-plan-v1` retains that commit; the branch pointer is not itself
immutable, while the commit and tree identities are. The local tag
`stress-plan-v1` names the same commit. `evidence/frozen/stress-plan-v1.json`
contains the exact expected populations and outcomes.

The checkpoint's direct launcher failed before test discovery. Commit
`71fae96d7103e695a4c955ad7c46c8b19afc6a5a` repaired imports in exactly three
launcher files without changing model semantics, populations, predictions, or
decision rules: `scripts/run_campaign.py`, `scripts/verify_repository.py`, and
`experiments/F3-ID-BITPATCH-001/run.py`. Campaign output is deterministic JSON.
The repository verifier reruns every test in a temporary directory and
compares every stored evidence file by SHA-256. This is a disclosed semantic
freeze plus launcher repair, not an unchanged executable freeze.

## Independent mechanisms

| Campaign | What it can decide | What it cannot decide |
|---|---|---|
| Source authentication | exact bytes, parent hashes, line anchors | semantic validity |
| Protocol linter | quantifier/refuter alignment and whether F3 arms are closed | truth of any conjecture |
| Formal models | validity of a universal implication under the encoded definitions when the source antecedent is premise-closed | omitted source premises, alternative semantic readings, or actual physical possibility |
| Finite exhaustion | all models inside the disclosed bounded population | cases outside the population |
| Mutation controls | whether a checker distinguishes a named defect from its repair | completeness against all possible defects |
| F1 replay | exact prior verdict on its Boolean domain | C1 outside that domain |
| F3 discriminator | whether F3's present labels identify a contrast | the repaired Fertility Conjecture |

## False-green controls

Every critical executable attack has a nearby negative or mutation control.
The W3 structural projection is repaired by supplying candidate/occupant
identity, current-criterion licensing, and open permission. That control shows
the reduced classifier discriminates those facts; it does not establish that
the failing rows satisfy P5.3's full identification-map antecedent. P3.1 is
enumerated both with its full identity-protection hypothesis and with the
historical weakened mutant.
The acquisition checker compares the displayed worst-case Bellman recurrence
with a deliberately wrong best-case recurrence. F3 accounting includes a
mutant that omits the terminal full appraisal. Protocol-source mismatches are
tested against text mutations that repair the exact quantifier or verdict
rule. A checker that passes both the broken and repaired candidate fails this
campaign.

## F1 preservation and replay

The prior `F1-AR-BOOL4-001` directory is copied to a temporary directory.
Sidecar hashes are checked first. The row-level verifier then recalculates all
saved rows, while the structurally separate full-domain verifier independently
enumerates the Boolean functions, reconstructs the target population, and
recomputes the association and verdict. No verifier writes into the retained
prior-evidence directory.

## Execution

From the repository root, the frozen campaign is materialized with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/run_campaign.py /tmp/testpoietic-campaign
```

After the authenticated output is stored under `evidence/runs/campaign-001`,
the full replay is:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify_repository.py
```

The verifier succeeds only when subject authentication, unit/mutation tests,
both F1 verifiers, and the byte-for-byte evidence replay all succeed. This
green state means the documentation is reproducible. The substantive claim
statuses are reported separately. `PREMISE_CLOSURE.md` is the mandatory bridge
between a raw reduced-model Boolean and any source-level claim verdict.
