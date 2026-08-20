# HKEY-v1 Header-Line Erratum — Record v1

record_id: ERR-HKEY-HDR-v1
version: 1.0
date: 2026-08-20
status: REVIEWED_PENDING_OWNER_SEAL
official_file: HKEY_HEADER_ERRATUM_V1.md
plain_language_file: HKEY_HEADER_ERRATUM_V1_PLAIN_LANGUAGE.md
digest_manifest: HKEY_HEADER_ERRATUM_V1_FREEZE.json
sha256_official: HKEY_HEADER_ERRATUM_V1_FREEZE.json#official_sha256
sha256_plain_language: HKEY_HEADER_ERRATUM_V1_FREEZE.json#plain_language_sha256
parent_records: HKEY_BINDING_V1.md (HKEY-v1, subject of the erratum); RECORD_PUBLICATION_STANDARD_V1.md (RPS-v1, publication standard)
scope: disclosure that the sealed HKEY-v1 official bytes omit the sha256_official/sha256_plain_language header pointer lines carried by the other sealed records, and confirmation that the omission is cosmetic
claims: documents the missing header pointer lines in the sealed HKEY-v1 official file; confirms the sealed manifest carries the authoritative hashes; confirms the sealed bytes are unchanged
non_claims: does not edit HKEY-v1 or any sealed record; does not change any hash, pin, N-row, readiness count, or discharge count; does not seal this erratum; does not prove creativity or non-creativity

## 1. The observation

External audit (shuttle, RPS-v1 profile) noted that the sealed record
docs/HKEY_BINDING_V1.md (HKEY-v1) does not carry the two conventional
header pointer lines

    sha256_official: <manifest>#official_sha256
    sha256_plain_language: <manifest>#plain_language_sha256

that sealed records such as TRANCHE_HANDOFF_V2.md carry between the
digest_manifest line and the parent_records line. The five
pending-seal records of this tranche had the same omission and are
corrected in place (they are not yet sealed); HKEY-v1 is sealed and
therefore is NOT edited. This erratum is the standing correction for
HKEY-v1, in the same posture as ERR-SPA-v1.

## 2. Authoritative hashes

HKEY-v1's sealed digest manifest, docs/HKEY_BINDING_V1_FREEZE.json,
carries the authoritative hashes of the sealed bytes:

    official_sha256       = 01a5bf4f8f6a84d5cd7d67554ed1e1aededafced4a7a767728445f40a504d57f
    plain_language_sha256 = b31c5e74fa4d88f2803faa4125655c326ed6cf511e7fbce72af0bd9e4531c362

Both values verify correctly against the committed bytes of
HKEY_BINDING_V1.md and HKEY_BINDING_V1_PLAIN_LANGUAGE.md. The manifest,
not the record header, is the authoritative pin location under RPS-v1;
the header pointer lines are a convenience pointer to it.

## 3. Assessment

The omission is cosmetic. It affects no hash, no pin, no parent_record
entry, and no semantic content of HKEY-v1. Every downstream manifest that
pins HKEY-v1 (CAP-v1, SIG-EPI-v1, SIG-HJ-v1, IDF-v1) pins the correct
sealed bytes 01a5bf4f.... No readiness count changes: PINNED=0,
PARTIAL=2, OPEN=18; original N-rows discharged: 0; testing status:
PROHIBITED.

## 4. Disposition

The sealed bytes of HKEY-v1 are unchanged and remain the canonical bytes.
Future records that quote or re-issue HKEY-v1's header should include the
two pointer lines; no retroactive edit of the sealed file is authorized
or needed.
