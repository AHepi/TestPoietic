# Admissibility Two-Sided Re-Check — Plain-Language Companion v1

This is the plain-language companion to ADM_RECHECK_V1.md. It says the
same things in everyday words. If the two disagree, the official record
wins.

## What this is

An earlier record (ADM-v1) proved that the project's admissibility gate —
the rule deciding which contexts count when capacity is tested — does not
rig the answer: it showed two small test worlds, one where capacity comes
out true and one where it comes out false, both satisfying the gate. A
later audit (DSF-v1) discovered that the positive world relied on a formula
that did not typecheck, so the proof was withdrawn and the gate's status
was downgraded. The capacity-typing record (CAP-v1) has now repaired that
formula. This record rebuilds the withdrawn proof on the repaired
foundation.

## The rebuilt proof

Two tiny test worlds again. Both have one agent, one possible policy, one
possible selector, one start state at time zero, and the same five arrows
between states. They differ only in who owns the arrows and what the
output tables say.

In the negative world, every arrow is externally owned. Each of the four
capacity checks needs at least one arrow owned by the agent, so all four
fail — and they fail for every admissible context, not just one, so no
loophole is hiding anywhere. Capacity comes out false.

In the positive world, the agent owns all five arrows, and the tables are
filled in so each capacity check passes: a fresh construction, a sustained
appraisal whose Update entry is set to yes, a promotion, and a draw-on
where the agent itself selects the target — which is also exactly what
makes the "everything selected is external" flag false, as required. All
four checks pass. Capacity comes out true.

Because both worlds satisfy the same admissibility gate and differ only in
things the gate does not look at, the gate decides neither answer. That is
the whole theorem.

## Honest limits

Three of them, all stated in the official record. First, this proof depends
on CAP-v1, which is still pending the owner's seal; if CAP-v1 changes, this
record must be re-checked. Second, the gate being tested is weak — in the
finite fragment its second condition is automatic, so what was proved
independent is essentially "the start state is reachable and contexts were
not filtered after the fact." That was true of the original proof too, and
the record repeats it so the restored status is not read as stronger than
it is. Third, this says nothing about the source-level theory: the five
original non-entailment rows that depend on real admissibility remain open,
and no row is discharged or testable.

## What changes

If the owner seals this record and CAP-v1: the finite admissibility gate
returns to bucket B2 (stipulated but shown not to decide the result), and
the counts go from 0/0/3 back to 0/1/2. Nothing else moves.

## What happens next

The frozen order continues with the signature and identity sweep: giving
complete types to the remaining primitive tables and freezing the
cross-fragment identity conditions, one bounded record at a time.
