# SPA-v1 Freeze-Pin Erratum — Record v1

record_id: ERR-SPA-v1
version: 1.0
date: 2026-08-20
status: SEALED_ERRATUM_DISCLOSURE
official_file: SPA_PIN_ERRATUM_V1.md
plain_language_file: SPA_PIN_ERRATUM_V1_PLAIN_LANGUAGE.md
digest_manifest: SPA_PIN_ERRATUM_V1_FREEZE.json
parent_records: PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1, subject of the defect); PIECEMEAL_SEMANTIC_ANNEX_V1_FREEZE.json (the defective seal, immutable history); RPS-v1 (publication standard)
scope: disclosure of a freeze-process integrity defect in the SPA-v1 digest manifest and prospective re-binding of SPA-v1 canonical bytes
claims: documents that the sealed SPA-v1 manifest pinned bytes that were never committed; re-binds SPA-v1 canonical bytes to the committed blob; corrects all downstream manifests prospectively
non_claims: no sealed record is edited; no semantic content of SPA-v1 is invalidated; no N-row, readiness count, or discharge count changes; no claim about how the wrong bytes were produced beyond the plausible explanation recorded below

## 1. The defect

The sealed freeze manifest docs/PIECEMEAL_SEMANTIC_ANNEX_V1_FREEZE.json pins

    official_sha256 = 40681e6cd79e207fc21cc85e2f698bc161807f42193c4e4bb9214dcb84dffdff

for docs/PIECEMEAL_SEMANTIC_ANNEX_V1.md (SPA-v1). This hash matches NO bytes
anywhere in retrievable repository history. The bytes that were actually
committed as SPA-v1 hash to

    sha256 = a9f62ebbd086a0499893f57a566f6b769a1b64fc27dfe15dd640a8c1f5e200a0
    (git blob 6b3b2faea4da707e0558f3f545379b3ee71796ef).

Verdict: freeze-process defect. The seal pinned bytes that were never
committed — plausibly a pre-commit local draft whose exact content is not
recoverable. This is a defect in the seal's binding, not in the document.

## 2. Evidence summary

- File history: docs/PIECEMEAL_SEMANTIC_ANNEX_V1.md was added in exactly one
  commit, 61ff58d6d4ee2a2558cb181cbeef24fd2dd25e4d (2026-08-20), and its
  bytes are identical at every later commit examined on branches
  agent/stress-test-continuation and agent/hkey-v1-binding. No post-freeze
  in-place edit occurred.
- Hash table:

  | bytes | sha256 |
  |---|---|
  | pinned by sealed manifest | 40681e6cd79e207fc21cc85e2f698bc161807f42193c4e4bb9214dcb84dffdff (matches nothing) |
  | committed SPA-v1 bytes (blob 6b3b2fae) | a9f62ebbd086a0499893f57a566f6b769a1b64fc27dfe15dd640a8c1f5e200a0 |

- Ruled-out normalizations: CRLF line endings, UTF-8 BOM, and
  trailing-newline variants of the committed bytes were hashed; none
  reproduces the pinned value. The pinned hash is not an encoding artifact
  of the committed file.
- Integrity of the rest of the seal: all other pins in the same manifest
  verify correctly (the plain-language file hash e2bea959... and all parent
  hashes match their committed bytes). The defect is isolated to the single
  official_file pin.

## 3. What is NOT affected

- The annex CONTENT reviewed by every subsequent record is the committed
  bytes a9f62ebb.... Every review of SPA-v1 — by DSF-v1, TH-v2, HKEY-v1,
  CAP-v1, ADM-RECHECK-v1, SIG-EPI-v1, and SIG-HJ-v1 — was a review of those
  committed bytes, because those are the only bytes that exist in history.
- No semantic content is invalidated. No definition, axiom, classification,
  cone trace, independence check, or review finding that cites SPA-v1
  changes meaning.
- No frozen calculus byte, N-row, readiness count (PINNED=0, PARTIAL=2,
  OPEN=18), or discharge count (0) is affected. Testing status remains
  PROHIBITED.
- The defective manifest itself is immutable history and is NOT edited.

## 4. Corrective binding

Henceforth the canonical bytes of SPA-v1 are the committed bytes at git blob
6b3b2faea4da707e0558f3f545379b3ee71796ef, sha256

    a9f62ebbd086a0499893f57a566f6b769a1b64fc27dfe15dd640a8c1f5e200a0.

All future records that pin SPA-v1 MUST pin that value. The value
40681e6c... is retired and must never be used as a pin for SPA-v1 again.

## 5. Affected downstream manifests and their disposition

The broken pin 40681e6c... for PIECEMEAL_SEMANTIC_ANNEX_V1.md is carried in
the parent_records of the following manifests:

- Sealed records — covered by this erratum (their seals stand; the corrected
  binding is supplied here, not by editing them): DSF-v1, TH-v2, HKEY-v1,
  and SPA-v1's own manifest.
- Pending-seal records — corrected prospectively (their manifests are
  amended to pin a9f62ebb... before owner seal): CAP-v1, SIG-EPI-v1,
  SIG-HJ-v1.

No sealed record is edited by this erratum or by any corrective action it
authorizes.

## 6. Process lesson and standing rule

The defect slipped through because the manifest was sealed against a local
working-tree draft rather than against the committed blob. Standing rule for
all future freezes: every pinned sha256 must be recomputed from the bytes
retrieved from the repository (e.g., via the contents API or a fresh clone)
at seal time, not from local files assumed to be identical. This erratum's
own pins were computed from the committed bytes.

## 7. Residual status

This is a disclosure of fact, sealed on publication per RPS-v1. It changes
no readiness or discharge count: PINNED=0, PARTIAL=2, OPEN=18; original
N-rows discharged: 0; testing status: PROHIBITED. The freeze process, not
the calculus, was the defective component, and the process is corrected by
the standing rule in Section 6.
