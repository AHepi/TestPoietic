# SPA-v1 Freeze-Pin Erratum — Plain-Language Companion v1

This is the plain-language companion to SPA_PIN_ERRATUM_V1.md. It says the
same things in everyday words. If the two disagree, the official record
wins.

## What went wrong

When the project froze the annex document called SPA-v1, it published a
"seal" file that records the fingerprint (a sha256 hash) of the exact bytes
being frozen. The idea is: anyone can later recompute the fingerprint of the
file and check it against the seal, proving the file was never changed.

The problem: the fingerprint written into the seal does not match the file
that was actually saved into the repository. It does not match any version
of the file that ever existed there. In short, the seal was made against
some other bytes — most likely a local draft from just before the file was
committed — and those bytes are lost.

## How we know

- The annex file was committed exactly once, on 2026-08-20, and its bytes
  never changed afterwards on either working branch. So nobody edited the
  file after freezing it.
- The real committed file's fingerprint is a9f62ebb.... The seal says
  40681e6c.... They are simply different.
- We checked the usual innocent explanations — Windows-style line endings,
  a byte-order mark, an extra newline at the end. None of them turns the
  committed file's fingerprint into the sealed one. The sealed fingerprint
  is not the committed file in disguise.
- Everything else in the same seal checks out: the plain-language file's
  fingerprint and all the parent-document fingerprints match their real
  bytes. Only this one pin is broken.

## What this does NOT mean

- It does not mean the annex was tampered with. The file everyone reviewed
  is the file in the repository, and that file is unchanged since the day
  it was committed.
- Every review that cited SPA-v1 — the downstream freeze, the threshold
  fix, the key binding, the capacity repair, and both signature freezes —
  reviewed the real committed bytes. No conclusion, definition, or check
  based on SPA-v1 is invalidated. The document is fine; the seal's label
  on the document was wrong.
- No test status, row count, or discharge count changes. Nothing was being
  tested before and nothing is being tested now.

## What happens now

From now on, the official fingerprint of SPA-v1 is a9f62ebb... (the real
committed bytes). Every future record that refers to SPA-v1 must use that
fingerprint. The wrong value, 40681e6c..., is retired.

The wrong pin also appears inside the seal files of seven other records.
Four of those are already sealed (DSF-v1, TH-v2, HKEY-v1, and SPA-v1's own
seal); they are never edited, so this erratum serves as the standing
correction for them. Three are still awaiting their owner's seal (CAP-v1,
SIG-EPI-v1, SIG-HJ-v1); their seal files are fixed to use the correct
fingerprint before they are sealed. No sealed record is edited.

## The lesson

The seal was computed against a local file instead of against the bytes
actually stored in the repository. The new standing rule: before sealing,
recompute every fingerprint from bytes fetched fresh from the repository.
This erratum's own fingerprints were computed that way.

## What happens next

This record is a disclosure of a fact, sealed when published, under the
project's publication standard. The counts stand unchanged: 0 rows pinned,
2 partial, 18 open; 0 rows discharged; testing remains prohibited.
