# TestPoietic

This repository is an auditable stress-test package for the exact attachment
`subject/spark-poietic-layered-kernel-v1.2-purpose-guarded.md`.

The primary subject is byte-pinned by SHA-256:

```text
9c5d389afc1f334733604083710f6625638b8933825a6312c7403e7de08dafbc
```

The repository separates four things that the kernel itself says must not be
collapsed: source authentication, proof/model criticism, executable field
protocols, and interpretation. A green verifier means only that the recorded
evidence reproduces; it is not a truth or support grade for the theory.

## Frozen-before-run campaign

The first repository commit freezes the subject, the prior F1 evidence, the
F3 identifiability discriminator, the formal countermodel population, and the
expected observables before the new campaign is executed. Later commits add
raw outputs and the final report without rewriting the frozen files.

Run the complete verifier from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify_repository.py
```

The verifier uses only the Python standard library. Generated files are
written to a caller-selected external directory, never silently into the
authenticated source tree.

## Layout

| Path | Purpose |
|---|---|
| `subject/` | Exact primary attachment and authenticated parent artifacts |
| `prior-evidence/f1/` | Previously frozen F1 experiment, raw table, and independent verifiers |
| `experiments/F3-ID-BITPATCH-001/` | Frozen F3 protocol-identifiability discriminator |
| `testpoietic/` | Reusable parsers, model checkers, and evidence generators |
| `tests/` | Unit and mutation tests for the checkers themselves |
| `evidence/frozen/` | Predicted observables and campaign boundary fixed before execution |
| `evidence/runs/` | Added only after execution |
| `docs/` | Method, findings, limitations, and independent review |

## Evidence rule

Every reported verdict must name its exact subject hash, executable boundary,
input population, predicted observable, raw output, and scope. Failure of a
witness blocks the application that needs it; it is not silently counted as a
refutation of an unrelated theorem.
