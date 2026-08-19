# Independent review record and resolution

An independent read-only review examined evidence/report candidate
`f0680881d0ca7411a4f15dc447c2800052f6e567`. Its disposition was `FAIL`: one P0
and three P1 findings. All four findings are accepted in the corrected
documentation. The reviewer did not edit the repository.

## Authenticated subject

| Identity | Independently recomputed value |
|---|---|
| Candidate commit | `f0680881d0ca7411a4f15dc447c2800052f6e567` |
| Candidate tree | `9c3c514185e22a57292a08b1cac7e55159cccd09` |
| Candidate parent | `71fae96d7103e695a4c955ad7c46c8b19afc6a5a` |
| Semantic freeze commit | `d04bd2273121427166cd4fe9442ff595db959fbd` |
| Semantic freeze tree | `5e317432fcb00ba4b5ea106cc6845fe63c13e425` |
| Subject SHA-256 | `9c5d389afc1f334733604083710f6625638b8933825a6312c7403e7de08dafbc` |
| Subject manifest SHA-256 | `f33e00824ef06e8990b869ca056795b97e5456db3e606ce222100f69fcc33832` |
| Disposable review archive SHA-256 | `3f3c545646d783adfd60e6becea6788a4344a8cae3d9f890be9c2fc58dc7ff89` |

The reviewer recomputed candidate/tree/parent identity, checkpoint/tree,
ancestry, subject bytes, all three provenance hashes, 64 tests, and byte
identity for all 11 campaign files. Exact replay reproduced the F1 statistics,
all bounded population counts, F3 costs, and the four protocol mismatches.

## Findings and resolutions

| Review ID | Original disposition | Finding | Accepted correction |
|---|---|---|---|
| `IR-01` | P0, refuted | `w3_to_a5` satisfies a weakened structural projection, not P5.3's full identification-map antecedent; the 32-row table hard-codes structural W3. | Downgraded to `UNDERDETERMINED structural-adequacy criticism`. |
| `IR-02` | P1, underdetermined | The finite-prefix empty-edge witness does not interpret P7.1 or join extension-readiness to selection. | Downgraded to a quantifier/selection ambiguity, not a countermodel. |
| `IR-03` | P1, refuted | The d04 checkpoint launcher failed; three executable launchers changed before the successful run. | Replaced “unchanged executable freeze” with the exact d04 semantic freeze → 71fa launcher repair → f068 evidence history. |
| `IR-04` | P1, unverified | The purpose checker counts non-empty cells but performs no semantic v1.0/v1.1 transport comparison. | Verdict changed to `SURFACE PCOV=12 RECOMPUTED; RETROACTIVE TRANSPORT UNVERIFIED`; removal is labelled editorial advice. |

The three repaired launchers were `scripts/run_campaign.py`,
`scripts/verify_repository.py`, and
`experiments/F3-ID-BITPATCH-001/run.py`. Their exact d04-to-71fa diff is
recoverable from the two named commits.

The review also classified the P3.5, T7, and TRef witnesses as plausible textual
defects whose complete premise closure was unverified. The corrected
[`PREMISE_CLOSURE.md`](PREMISE_CLOSURE.md) now records that boundary for every
object emitted by `all_formal_models()`.

## Replay commands

The reviewer materialized a disposable archive and used the repository's Git
database only to authenticate the candidate identity:

```bash
review_root="$(mktemp -d /tmp/testpoietic-review.XXXXXX)"
git archive --format=tar \
  --output="$review_root/candidate.tar" \
  f0680881d0ca7411a4f15dc447c2800052f6e567
mkdir "$review_root/tree"
tar -xf "$review_root/candidate.tar" -C "$review_root/tree"
cd "$review_root/tree"

env PYTHONDONTWRITEBYTECODE=1 \
  GIT_DIR=/workspace/scratch/c0eabe6f773f/TestPoietic/.git \
  GIT_WORK_TREE="$review_root/tree" \
  python3 -B scripts/run_campaign.py \
  "$review_root/replay"

env PYTHONDONTWRITEBYTECODE=1 \
  GIT_DIR=/workspace/scratch/c0eabe6f773f/TestPoietic/.git \
  GIT_WORK_TREE="$review_root/tree" \
  python3 -B scripts/verify_repository.py \
  --evidence "$review_root/tree/evidence/runs/campaign-001"
```

This was a small in-thread review rather than a separately authenticated
lifecycle run. No gate-capsule, lease, compiled-prompt identity, or lifecycle
hook was supplied, so that orchestration assurance is explicitly outside the
review claim.
