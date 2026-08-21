---
name: example-battery
description: Build a battery of concrete instances BEFORE writing or evaluating any definition, pin, or semantic clause (Reed step 1). Use whenever a term needs a meaning, a pin is being drafted, or an existing pin is being retrofitted. Converts semantic mapping from unaided imagination into curation of juxtaposed structures.
---

# Example Battery (Reed 1)

<!-- PROMPT-CORE-BEGIN -->
Before any clause about a term's meaning is written, build its battery.

1. Construct, as small concrete structures in the fragment language:
   - >=3 POSITIVE instances the intended meaning must admit;
   - >=3 NEAR-MISS negatives, each a minimal pair with a positive -
     identical except in one respect, which the meaning must exclude;
   - >=1 BOUNDARY case whose classification is genuinely undecided,
     recorded as OPEN with the question stated.
2. Structures are explicit and tiny: name the sorts, list the elements,
   give every relevant relation extensionally. No instance is described
   only in prose.
3. Juxtapose everything in one file, positives beside their near-miss
   partners, with one line per pair naming the single difference.
4. If the term has a recorded risk corridor ("too weak admits X, too
   strong excludes Y"), X and Y are MANDATORY battery members: build the
   structure the too-weak reading wrongly admits and the structure the
   too-strong reading wrongly excludes. A corridor without its two walls
   built is not yet analyzed.
5. If you cannot construct three positives, the term is not understood
   well enough to pin: record what blocks each attempted instance and
   stop. That record is the deliverable.
6. Battery instances carry ids and content digests; they are proto-members
   of the model zoo and feed the denotation tests. You NEVER compute a
   digest yourself: write PENDING-DIGEST in the registry's digest column.
   Digests are computed and verified by scripts/battery_digest.py
   (sha256 over the instance's fenced structure blocks), which the task's
   acceptance command runs in --verify mode; a self-invented hash is a
   fabrication and fails acceptance. Never delete a battery
   instance a pin fails on; a failed instance is evidence, not clutter.
<!-- PROMPT-CORE-END -->
