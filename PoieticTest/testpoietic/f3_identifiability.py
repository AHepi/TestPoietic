"""Exact finite discriminators for the wording of Protocol F3.

These models do not purport to test the unrestricted Fertility Conjecture.
They test whether the policy labels and decision rule in F3 identify the
claimed mechanism.  Arithmetic is integer-exact and the entire state is
returned for independent replay.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class PolicyResult:
    name: str
    n: int
    initial: str
    target: str
    terminal: str
    reads: int
    writes: int
    total_cost: int
    delivered_bits: int
    appraisals: int
    promotions: int
    uses_failure_fringe: bool
    library_local: bool
    promotion_shy: bool
    directionless: bool

    @property
    def delivered_fraction(self) -> float:
        return self.delivered_bits / self.n


def mismatch_indices(candidate: list[int], target: list[int]) -> tuple[int, ...]:
    """The resistant battery's complete localization output."""

    return tuple(index for index, pair in enumerate(zip(candidate, target)) if pair[0] != pair[1])


def serial_fringe_policy(n: int) -> PolicyResult:
    """Promote one localized repair and rerun the full battery each time."""

    if n < 1:
        raise ValueError("n must be positive")
    candidate = [0] * n
    target = [1] * n
    fringe = mismatch_indices(candidate, target)
    reads = n
    writes = 0
    appraisals = 1
    promotions = 0
    for index in fringe:
        candidate[index] = target[index]
        writes += 1
        promotions += 1
        # F3 leaves the appraisal schedule unspecified.  This arm embodies the
        # common serial interpretation: every promoted partial repair is tested
        # against the whole declared battery.
        mismatch_indices(candidate, target)
        reads += n
        appraisals += 1
    return PolicyResult(
        name="serial_fringe",
        n=n,
        initial="0" * n,
        target="1" * n,
        terminal="".join(map(str, candidate)),
        reads=reads,
        writes=writes,
        total_cost=reads + writes,
        delivered_bits=n - len(mismatch_indices(candidate, target)),
        appraisals=appraisals,
        promotions=promotions,
        uses_failure_fringe=True,
        library_local=False,
        promotion_shy=False,
        directionless=False,
    )


def library_batch_policy(n: int) -> PolicyResult:
    """Use the same fringe through a held generic batch-patch constructor."""

    if n < 1:
        raise ValueError("n must be positive")
    candidate = [0] * n
    target = [1] * n
    fringe = mismatch_indices(candidate, target)
    reads = n
    for index in fringe:
        candidate[index] = target[index]
    writes = len(fringe)
    final_fringe = mismatch_indices(candidate, target)
    reads += n
    return PolicyResult(
        name="library_batch",
        n=n,
        initial="0" * n,
        target="1" * n,
        terminal="".join(map(str, candidate)),
        reads=reads,
        writes=writes,
        total_cost=reads + writes,
        delivered_bits=n - len(final_fringe),
        appraisals=2,
        promotions=1,
        uses_failure_fringe=True,
        library_local=True,
        promotion_shy=True,
        directionless=False,
    )


def wrong_batch_cost_mutant(n: int) -> int:
    """A deliberate accounting mutant: it omits the final appraisal."""

    return 2 * n


def run_bitpatch_family(cuts: tuple[int, ...] = (4, 8, 16, 32, 64, 128)) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for n in cuts:
        serial = serial_fringe_policy(n)
        batch = library_batch_policy(n)
        rows.append(
            {
                "n": n,
                "serial": asdict(serial),
                "batch": asdict(batch),
                "serial_formula": n * n + 2 * n,
                "batch_formula": 3 * n,
                "both_deliver_all": serial.delivered_bits == batch.delivered_bits == n,
                "batch_strictly_cheaper": batch.total_cost < serial.total_cost,
                "policy_class_overlap": batch.uses_failure_fringe and batch.library_local,
                "serial_to_batch_cost_ratio": serial.total_cost / batch.total_cost,
                "mutant_omits_final_appraisal": wrong_batch_cost_mutant(n) != batch.total_cost,
            }
        )
    return {
        "experiment_id": "F3-ID-BITPATCH-001",
        "claim_tested": (
            "F3's named policy classes and failure-fringe conversion rule identify "
            "a policy contrast sufficient to determine the ranking"
        ),
        "subject_lines": [570, 1586, 1590, 1596],
        "scope": (
            "protocol identifiability on the declared finite bit-patch family; "
            "not a verdict on unrestricted Fertility"
        ),
        "cost_rule": "one unit for each bit read or written",
        "cuts": list(cuts),
        "rows": rows,
        "all_exact_formulas_match": all(
            row["serial"]["total_cost"] == row["serial_formula"]
            and row["batch"]["total_cost"] == row["batch_formula"]
            for row in rows
        ),
        "rival_dominates_every_cut": all(row["batch_strictly_cheaper"] for row in rows),
        "classes_overlap_every_cut": all(row["policy_class_overlap"] for row in rows),
        "all_mutants_killed": all(row["mutant_omits_final_appraisal"] for row in rows),
        "protocol_verdict": "NON-IDENTIFYING",
        "fertility_verdict": "UNTESTED",
    }
