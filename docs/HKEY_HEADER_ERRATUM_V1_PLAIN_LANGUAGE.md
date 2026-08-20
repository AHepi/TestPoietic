# HKEY-v1 Header-Line Erratum — Plain-Language Companion v1

This is the plain-language companion to HKEY_HEADER_ERRATUM_V1.md. It says
the same things in everyday words. If the two disagree, the official record
wins.

## What this is about

Each project record starts with a small header block. One pair of lines in
that block points to the record's "seal" file, which stores the
fingerprints (sha256 hashes) of the record's exact bytes. An outside audit
noticed that the sealed key-binding record, HKEY-v1, is missing those two
pointer lines, even though other sealed records have them.

## Why it does not matter much

The pointer lines are only a convenience. The real, authoritative
fingerprints live in HKEY-v1's seal file, and they are correct: the
official record's fingerprint is 01a5bf4f... and the plain-language
companion's is b31c5e74.... Both match the files actually stored in the
repository. Every later record that refers to HKEY-v1 uses the correct
fingerprint. Nothing about the record's content, its checks, or any count
changes.

## What is being done

HKEY-v1 is sealed, and sealed records are never edited, so the missing
lines are not added to it. Instead, this erratum records the omission and
confirms that the seal file's fingerprints are authoritative. The five
newer records that had the same omission were not yet sealed, so their
headers were fixed directly and their seal files re-pinned. No sealed
bytes change anywhere.

## What happens next

This erratum is published for owner review; it is not sealed by this act.
The counts stand unchanged: 0 rows pinned, 2 partial, 18 open; 0 rows
discharged; testing remains prohibited.
