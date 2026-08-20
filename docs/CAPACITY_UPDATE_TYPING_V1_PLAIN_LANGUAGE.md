# Capacity Update Typing — Plain-Language Companion v1

This is the plain-language companion to CAPACITY_UPDATE_TYPING_V1.md. It
says the same things in everyday words. If the two disagree, the official
record wins.

## What problem this solves

The rulebook defines an operation called Update that takes one assessment,
one policy, one selector, and one state, and answers yes or no. But two of
the capacity rules call it with entire lookup tables of policies and
selectors instead of single entries. That is like feeding a whole
spreadsheet into a formula that expects one cell: the expression does not
parse, so four capacity checks and everything built on them were never
actually well-defined. An earlier audit (DSF-F1) caught this and stripped
a result called ADM-T1 that had relied on it. This record repairs the
typing. It does not re-prove ADM-T1.

## The repair

Both call sites now evaluate the tables at the specific state the rule is
talking about: Update(x, policy-at-s'', selector-at-s'', s''). The
operation's own definition is untouched.

One extra piece was needed. The tables only cover states reachable from the
start state, and in one of the two rules the state s'' is introduced by a
selection step that the old text never required to be a real transition
between those endpoints. A new rule, CAP-A1, says a selection result must
actually be an edge from the selected-from state to the selected-to state.
Without it, the repaired formula could still be undefined. This also fixes
half of a different recorded gap (DSF-v1 3.4(7)), and the record says so.

We considered two other repairs and rejected them: re-typing Update to
accept whole tables (moves the defect into the definition and invites
spurious dependencies), and evaluating the tables at the earlier state s'
instead of s''. The second alternative is not obviously wrong — for one of
the two rules it is even arguably natural — so the record states plainly
that the choice is ours, explains it per rule, and shows with an explicit
example that the two choices can give different answers. Nothing was hidden.

## How we know the repair is not rigged

We built the smallest possible test world in which all four capacity
checks can be satisfied: one agent, a handful of states, and — this is the
important part — exactly one possible policy and one possible selector, so
there is only one possible context for the rules to quantify over. Then we
flipped a single Update entry. With the entry set to yes, all four clauses
hold and the capacity predicate is true. With it set to no, one clause
fails, no other context can rescue it, and the predicate is false. So the
repaired typing does not decide the answer either way.

An earlier draft of this record claimed the same thing without the
single-policy device; the independent reviewer showed the claim failed
without it, because a different context could have consulted a different
table entry. The construction above is the fix.

As with the previous record, the defense of the design choice itself is by
written reasons, not by experiment, and the record labels it that way.

## What changed and what did not

Changed, in a new prospective fragment called SPA-CAP-v1: the bodies of
the two capacity rules, plus the new CAP-A1 selection-coherence rule. Not
changed: SPA-v1, the earlier threshold and key-binding records, any
original N-row, the admissibility counts (still 0 / 0 / 3, because ADM-T1
has not been re-derived), and the overall readiness counts — still 0
pinned, 2 partial, 18 open, all 20 rows untestable, none discharged. The
repair by itself makes nothing true or false; both outcomes remain
reachable, as the test world shows.

## What happens next

The owner reviews and seals this record. After that, the frozen order
continues with item 2: re-attempting the ADM-T1 independence result under
the repaired typing. A failure there is a result, not permission to keep
editing.
