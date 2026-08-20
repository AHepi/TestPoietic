# Record Publication Standard v1

record_id: RPS-v1
version: 1.0
date: 2026-08-20
status: SEALED_COMMUNICATION_REQUIREMENT
official_file: this file, section "Official version"
plain_language_file: this file, section "Plain-language version"
digest_manifest: RECORD_PUBLICATION_STANDARD_V1_FREEZE.json
sha256_official: RECORD_PUBLICATION_STANDARD_V1_FREEZE.json#official_sha256
sha256_plain_language: RECORD_PUBLICATION_STANDARD_V1_FREEZE.json#plain_language_sha256
parent_records: none
scope: substantive records created after this standard is sealed
claims: every substantive record has an official and faithful plain-language form
non_claims: this communication rule changes no mathematical, scientific, or philosophical result

## Official version

### Requirement

Every substantive project record issued after this standard is sealed must have two synchronized forms:

1. **Official version.** The precise version: definitions, equations, source references, identifiers, stated assumptions, scope, result status, and limitations.
2. **Plain-language version.** A faithful explanation for a reader without secondary-school completion or specialist training.

The two forms use the same record ID, version, date, status, parent records, scope, claims, and non-claims. They may be two files or two clearly marked sections of one container file.

- For two files, the ordered digest pair has one SHA-256 value for each file.
- For one container file, both digest fields name the same container SHA-256 value, and the manifest records separate official and plain-language section anchors.

Both headers point to this shared digest record in the freeze manifest. The external manifest avoids the impossible self-reference of placing a file's final hash inside the file being hashed. The project commit that contains the manifest is the freeze point.

The plain-language version may simplify wording and explain notation, but it must not:

- remove a limitation, uncertainty, condition, exception, or counterexample requirement;
- turn NOT_ESTABLISHED, REGISTERED_SCHEMA, a class-relative result, or a closure-blocked result into a positive conclusion;
- present an imported assumption or bridge as a proved fact;
- add a claim that is absent from the official version;
- treat an unsealed or pending digest as a completed freeze.

If a faithful plain-language explanation cannot yet be written, the official record must explicitly state PLAIN_LANGUAGE_VERSION_PENDING. It may not issue a misleading simplification instead.

### Required header and manifest

Every new substantive record begins with these fields:

    record_id:
    version:
    date:
    status:
    official_file:
    plain_language_file:
    digest_manifest:
    sha256_official:
    sha256_plain_language:
    parent_records:
    scope:
    claims:
    non_claims:

Before sealing, the two SHA fields may say PENDING_DIGEST, and the status must say UNSEALED or PENDING_DIGEST. A sealed record instead names a freeze manifest containing the actual ordered digest pair.

The freeze manifest must contain:

    schema
    record_id
    version
    date
    status
    official_file
    official_sha256
    plain_language_file
    plain_language_sha256
    shared_container
    official_anchor
    plain_language_anchor
    parent_records
    scope
    claims
    non_claims
    caveat_crosswalk

### Caveat crosswalk

A freeze manifest must include a caveat crosswalk. Each row identifies one official item and the plain-language location that retains it:

| Official item ID | Type | Official statement | Plain-language location | Checked |
|---|---|---|---|---|
| Example: NC-1 | non-claim | What the record does not establish | heading/paragraph | yes/no |

The required types are: claim, non-claim, condition, limitation, result status, and uncertainty. A record cannot be sealed until every official item has a plain-language location with equivalent scope.

### Verification gate

Before sealing a record:

1. both forms exist, or the pending status is explicit;
2. their IDs, version, date, status, parent records, scope, claims, and non-claims agree;
3. the manifest contains both actual SHA-256 values;
4. the caveat crosswalk covers every material claim, non-claim, condition, limitation, status, and uncertainty;
5. the plain-language text has been checked against the official text, not merely rewritten from memory.

This standard is a communication and traceability rule. It does not itself prove or change any mathematical, scientific, or philosophical claim.

## Plain-language version

Every important new record now comes in two matching copies.

- The **official copy** is the careful one. It has the exact rules, maths, sources, assumptions, and warnings.
- The **plain-language copy** says the same thing using everyday words. It is for people who have not finished high school or do not know the field.

The two copies can be separate files or two clearly marked sections of one file. If they are separate files, each has its own file hash. If they share one file, they share that container file hash and the freeze list names the two sections. In either case, a small separate freeze list records the hash information and both copies point to it. This makes it possible to check that the easy-to-read copy really belongs with the official one.

The easy-to-read copy is not allowed to hide the important warnings. If the official copy says “we have not proved this,” the easy-to-read copy must say that too. If the official copy says “this only works for a small named group of cases,” the easy-to-read copy must say that too.

Before we call a record frozen, we make a checklist. The checklist shows where every important claim, warning, condition, and limit in the official copy appears in the easy-to-read copy. If a warning is missing, the record is not ready. If a faithful easy-to-read copy cannot yet be written, the official copy must clearly say PLAIN_LANGUAGE_VERSION_PENDING instead of pretending the record is complete.

This rule does not make any idea true. It only makes the project clearer and easier to check.