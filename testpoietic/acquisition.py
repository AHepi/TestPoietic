"""Exact finite checkers for the acquisition results in Spark section S12.

The finite-model core uses :class:`fractions.Fraction` throughout.  In
particular, Bellman costs, contraction ratios, efficiency ordering, and the
two inequalities in Imported Theorem 12.1 are decided without floating-point
tolerances.  Decimal logarithms are produced only as human-readable evidence.

The independent-noise checker for Imported Proposition 12.3 additionally
computes the worst i.i.d. binomial majority tail exactly for rational ``nu``.
The displayed Hoeffding threshold is transcendental, so its presentation and
the convenience calculation of the least qualifying odd integer use a
high-precision Decimal context; the exact binomial check is kept separate.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction
from functools import cmp_to_key, lru_cache
from itertools import product
from math import comb
from typing import Hashable, Iterable, Mapping


State = frozenset[str]


def _as_fraction(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _decimal_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


@dataclass(frozen=True)
class ExactQuery:
    """One deterministic finite response map with a positive base cost.

    ``outcomes`` is positionally aligned with the containing model's
    ``hypotheses`` tuple.  Outcomes need only be hashable; their labels carry
    no ordering or metric meaning.
    """

    name: str
    outcomes: tuple[Hashable, ...]
    cost: Fraction = Fraction(1)


@dataclass
class FiniteAcquisitionModel:
    """Executable form of the finite exact model in S12, lines 664--735.

    With ``availability=None``, every declared query is available at every
    state.  With an explicit map, an omitted state has no available query.
    ``state_costs`` can override a query's base cost at an exact version space.
    """

    hypotheses: tuple[str, ...]
    queries: tuple[ExactQuery, ...]
    availability: Mapping[State, tuple[str, ...]] | None = None
    state_costs: Mapping[tuple[str, State], Fraction] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.hypotheses:
            raise ValueError("the hypothesis class must be non-empty")
        if len(set(self.hypotheses)) != len(self.hypotheses):
            raise ValueError("hypothesis labels must be unique")
        query_names = [query.name for query in self.queries]
        if len(set(query_names)) != len(query_names):
            raise ValueError("query names must be unique")
        for query in self.queries:
            if len(query.outcomes) != len(self.hypotheses):
                raise ValueError(f"query {query.name!r} has the wrong response-map size")
            try:
                set(query.outcomes)
            except TypeError as error:
                raise ValueError(f"query {query.name!r} has an unhashable outcome") from error
            if _as_fraction(query.cost) <= 0:
                raise ValueError(f"query {query.name!r} must have positive cost")

        known_hypotheses = set(self.hypotheses)
        known_queries = set(query_names)
        if self.availability is not None:
            for state, names in self.availability.items():
                if not state or not state.issubset(known_hypotheses):
                    raise ValueError("availability keys must be non-empty model states")
                if not set(names).issubset(known_queries):
                    raise ValueError("availability names must denote declared queries")
                if len(set(names)) != len(names):
                    raise ValueError("a query may occur only once in an availability row")
        for (name, state), cost in self.state_costs.items():
            if name not in known_queries:
                raise ValueError("a state-cost override names an unknown query")
            if not state or not state.issubset(known_hypotheses):
                raise ValueError("state-cost keys must contain a non-empty model state")
            if _as_fraction(cost) <= 0:
                raise ValueError("all state-specific costs must be positive")

    @property
    def initial_state(self) -> State:
        return frozenset(self.hypotheses)

    def available_queries(self, state: State) -> tuple[ExactQuery, ...]:
        by_name = {query.name: query for query in self.queries}
        if self.availability is None:
            return self.queries
        return tuple(by_name[name] for name in self.availability.get(state, ()))

    def cost(self, query: ExactQuery, state: State) -> Fraction:
        return _as_fraction(self.state_costs.get((query.name, state), query.cost))

    def cells(self, query: ExactQuery, state: State) -> tuple[State, ...]:
        index = {hypothesis: position for position, hypothesis in enumerate(self.hypotheses)}
        grouped: dict[Hashable, set[str]] = {}
        for hypothesis in state:
            outcome = query.outcomes[index[hypothesis]]
            grouped.setdefault(outcome, set()).add(hypothesis)
        return tuple(
            sorted(
                (frozenset(cell) for cell in grouped.values()),
                key=lambda cell: (len(cell), tuple(sorted(cell))),
            )
        )


@dataclass(frozen=True)
class Efficiency:
    """The exact symbolic value ``log2(ratio) / cost``."""

    ratio: Fraction
    cost: Fraction
    state: State
    query: str

    def decimal(self, precision: int = 50) -> Decimal:
        with localcontext() as context:
            context.prec = precision
            if self.ratio == 1:
                return Decimal(0)
            return _decimal_fraction(self.ratio).ln() / Decimal(2).ln() / _decimal_fraction(self.cost)


def _compare_efficiency(left: Efficiency, right: Efficiency) -> int:
    """Compare logarithmic efficiencies using integer powers only.

    For positive rational costs ``a_i / b_i``, comparing
    ``ln(r_1)/c_1`` with ``ln(r_2)/c_2`` is equivalent to comparing
    ``r_1 ** (b_1*a_2)`` with ``r_2 ** (b_2*a_1)``.
    """

    left_power = left.ratio ** (left.cost.denominator * right.cost.numerator)
    right_power = right.ratio ** (right.cost.denominator * left.cost.numerator)
    return (left_power > right_power) - (left_power < right_power)


def _maximum_efficiency(rows: Iterable[Efficiency]) -> Efficiency | None:
    rows = tuple(rows)
    if not rows:
        return None
    return max(rows, key=cmp_to_key(_compare_efficiency))


def _minimum_efficiency(rows: Iterable[Efficiency]) -> Efficiency | None:
    rows = tuple(rows)
    if not rows:
        return None
    return min(rows, key=cmp_to_key(_compare_efficiency))


def query_efficiency(
    model: FiniteAcquisitionModel,
    query: ExactQuery,
    state: State,
) -> Efficiency:
    cells = model.cells(query, state)
    largest_cell = max(len(cell) for cell in cells)
    return Efficiency(
        ratio=Fraction(len(state), largest_cell),
        cost=model.cost(query, state),
        state=state,
        query=query.name,
    )


def reachable_states(model: FiniteAcquisitionModel) -> tuple[State, ...]:
    """Return the full closure under every available query and non-empty cell."""

    seen = {model.initial_state}
    queue = deque([model.initial_state])
    while queue:
        state = queue.popleft()
        if len(state) == 1:
            continue
        for query in model.available_queries(state):
            for cell in model.cells(query, state):
                if cell not in seen:
                    seen.add(cell)
                    queue.append(cell)
    return tuple(sorted(seen, key=lambda state: (-len(state), tuple(sorted(state)))))


def optimal_worst_cost(model: FiniteAcquisitionModel) -> Fraction | None:
    """Evaluate the exact Bellman recurrence; ``None`` denotes infinity."""

    @lru_cache(maxsize=None)
    def solve(state: State) -> Fraction | None:
        if len(state) == 1:
            return Fraction(0)
        candidates: list[Fraction] = []
        for query in model.available_queries(state):
            cells = model.cells(query, state)
            if max(len(cell) for cell in cells) == len(state):
                continue
            child_costs = [solve(cell) for cell in cells]
            if any(cost is None for cost in child_costs):
                continue
            finite_children = [cost for cost in child_costs if cost is not None]
            candidates.append(model.cost(query, state) + max(finite_children))
        return min(candidates) if candidates else None

    return solve(model.initial_state)


def mutant_best_case_cost(model: FiniteAcquisitionModel) -> Fraction | None:
    """Deliberately wrong Bellman evaluator retained for mutation evidence.

    The mutant lets the learner choose the most favourable outcome cell by
    replacing the theorem's ``max_y`` with ``min_y``.  A discriminating test
    must kill it; this function must never be used as an oracle.
    """

    @lru_cache(maxsize=None)
    def solve(state: State) -> Fraction | None:
        if len(state) == 1:
            return Fraction(0)
        candidates: list[Fraction] = []
        for query in model.available_queries(state):
            cells = model.cells(query, state)
            if max(len(cell) for cell in cells) == len(state):
                continue
            child_costs = [solve(cell) for cell in cells]
            finite_children = [cost for cost in child_costs if cost is not None]
            if finite_children:
                candidates.append(model.cost(query, state) + min(finite_children))
        return min(candidates) if candidates else None

    return solve(model.initial_state)


def _cost_vs_log_bound(
    total_cost: Fraction,
    efficiency: Efficiency,
    hypothesis_count: int,
) -> int:
    """Compare cost with ``log2(N)/efficiency`` exactly.

    The return value is negative, zero, or positive according as ``total_cost``
    is below, equal to, or above the logarithmic bound.
    """

    if efficiency.ratio <= 1:
        raise ValueError("a positive efficiency is required")
    scaled = total_cost / efficiency.cost
    left = efficiency.ratio ** scaled.numerator
    right = Fraction(hypothesis_count) ** scaled.denominator
    return (left > right) - (left < right)


def _bound_decimal(
    hypothesis_count: int,
    efficiency: Efficiency,
    precision: int = 50,
) -> str:
    with localcontext() as context:
        context.prec = precision
        numerator = Decimal(hypothesis_count).ln() * _decimal_fraction(efficiency.cost)
        denominator = _decimal_fraction(efficiency.ratio).ln()
        return str(numerator / denominator)


def theorem_12_1_certificate(model: FiniteAcquisitionModel) -> dict[str, object]:
    """Return an independently checkable certificate for Theorem 12.1."""

    states = reachable_states(model)
    live_states = tuple(state for state in states if len(state) > 1)
    best_by_state: list[Efficiency] = []
    every_efficiency: list[Efficiency] = []
    missing_availability: list[list[str]] = []
    for state in live_states:
        rows = [query_efficiency(model, query, state) for query in model.available_queries(state)]
        every_efficiency.extend(rows)
        best = _maximum_efficiency(rows)
        if best is None:
            missing_availability.append(sorted(state))
        else:
            best_by_state.append(best)

    lower_efficiency = _minimum_efficiency(best_by_state)
    upper_efficiency = _maximum_efficiency(every_efficiency)
    exact_cost = optimal_worst_cost(model)
    assumptions = (
        len(model.hypotheses) > 1
        and not missing_availability
        and len(best_by_state) == len(live_states)
        and lower_efficiency is not None
        and upper_efficiency is not None
        and lower_efficiency.ratio > 1
        and upper_efficiency.ratio > 1
    )

    result: dict[str, object] = {
        "theorem": "Imported Theorem 12.1",
        "subject_lines": [737, 761],
        "scope": (
            "The displayed Bellman recurrence over all available queries; the declared "
            "policy family Pi is not an argument of that recurrence and is therefore not "
            "an independently enforced restriction here."
        ),
        "hypothesis_count": len(model.hypotheses),
        "reachable_state_count": len(states),
        "reachable_live_state_count": len(live_states),
        "states_with_no_available_query": missing_availability,
        "assumptions_satisfied": assumptions,
        "optimal_worst_cost": None if exact_cost is None else _fraction_text(exact_cost),
    }
    if not assumptions or lower_efficiency is None or upper_efficiency is None:
        result.update(
            {
                "lower_bound": None,
                "upper_bound": None,
                "lower_bound_holds_exactly": None,
                "upper_bound_holds_exactly": None,
                "theorem_holds": None,
            }
        )
        return result

    if exact_cost is None:
        result.update(
            {
                "lower_bound": _bound_decimal(len(model.hypotheses), upper_efficiency),
                "upper_bound": _bound_decimal(len(model.hypotheses), lower_efficiency),
                "lower_bound_holds_exactly": True,
                "upper_bound_holds_exactly": False,
                "theorem_holds": False,
            }
        )
        return result

    lower_comparison = _cost_vs_log_bound(exact_cost, upper_efficiency, len(model.hypotheses))
    upper_comparison = _cost_vs_log_bound(exact_cost, lower_efficiency, len(model.hypotheses))
    lower_holds = lower_comparison >= 0
    upper_holds = upper_comparison <= 0
    result.update(
        {
            "lower_efficiency": {
                "ratio": _fraction_text(lower_efficiency.ratio),
                "cost": _fraction_text(lower_efficiency.cost),
                "state": sorted(lower_efficiency.state),
                "query": lower_efficiency.query,
                "decimal": str(lower_efficiency.decimal()),
            },
            "upper_efficiency": {
                "ratio": _fraction_text(upper_efficiency.ratio),
                "cost": _fraction_text(upper_efficiency.cost),
                "state": sorted(upper_efficiency.state),
                "query": upper_efficiency.query,
                "decimal": str(upper_efficiency.decimal()),
            },
            "lower_bound": _bound_decimal(len(model.hypotheses), upper_efficiency),
            "upper_bound": _bound_decimal(len(model.hypotheses), lower_efficiency),
            "lower_bound_holds_exactly": lower_holds,
            "upper_bound_holds_exactly": upper_holds,
            "theorem_holds": lower_holds and upper_holds,
        }
    )
    return result


def _contraction_step_limit(hypothesis_count: int, contraction: Fraction) -> int:
    if hypothesis_count <= 1:
        raise ValueError("N must be greater than one")
    if not 0 < contraction < 1:
        raise ValueError("lambda must lie strictly between zero and one")
    steps = 0
    remaining_bound = Fraction(hypothesis_count)
    while remaining_bound > 1:
        remaining_bound *= contraction
        steps += 1
    return steps


def corollary_12_2_certificate(
    model: FiniteAcquisitionModel,
    contraction: Fraction,
    cost_limit: Fraction,
) -> dict[str, object]:
    """Check separability and construct the policy promised by Corollary 12.2."""

    contraction = _as_fraction(contraction)
    cost_limit = _as_fraction(cost_limit)
    if len(model.hypotheses) <= 1:
        raise ValueError("Corollary 12.2 assumes N > 1")
    if not 0 < contraction < 1:
        raise ValueError("lambda must lie strictly between zero and one")
    if cost_limit <= 0:
        raise ValueError("c0 must be positive")

    live_states = tuple(state for state in reachable_states(model) if len(state) > 1)
    witnesses: dict[State, ExactQuery] = {}
    failures: list[list[str]] = []
    for state in live_states:
        qualifying = []
        for query in model.available_queries(state):
            largest = max(len(cell) for cell in model.cells(query, state))
            sigma = Fraction(largest, len(state))
            if sigma <= contraction and model.cost(query, state) <= cost_limit:
                qualifying.append(query)
        if not qualifying:
            failures.append(sorted(state))
        else:
            witnesses[state] = min(
                qualifying,
                key=lambda query: (model.cost(query, state), query.name),
            )

    query_limit = _contraction_step_limit(len(model.hypotheses), contraction)
    if failures:
        return {
            "corollary": "Corollary 12.2",
            "subject_lines": [763, 773],
            "scope": "Finite exact response maps, explicit availability, and closed rational costs.",
            "separability_satisfied": False,
            "states_without_witness": failures,
            "query_limit": query_limit,
            "closed_cost_limit": _fraction_text(cost_limit * query_limit),
            "conclusion_checked": None,
        }

    @lru_cache(maxsize=None)
    def policy_cost(state: State) -> tuple[int, Fraction]:
        if len(state) == 1:
            return (0, Fraction(0))
        query = witnesses[state]
        children = [policy_cost(cell) for cell in model.cells(query, state)]
        return (
            1 + max(depth for depth, _ in children),
            model.cost(query, state) + max(cost for _, cost in children),
        )

    actual_queries, actual_cost = policy_cost(model.initial_state)
    conclusion = actual_queries <= query_limit and actual_cost <= cost_limit * query_limit
    return {
        "corollary": "Corollary 12.2",
        "subject_lines": [763, 773],
        "scope": "Finite exact response maps, explicit availability, and closed rational costs.",
        "separability_satisfied": True,
        "states_without_witness": [],
        "query_limit": query_limit,
        "closed_cost_limit": _fraction_text(cost_limit * query_limit),
        "constructed_policy_worst_queries": actual_queries,
        "constructed_policy_worst_cost": _fraction_text(actual_cost),
        "conclusion_checked": conclusion,
    }


def canonical_binary_queries(hypothesis_count: int) -> tuple[ExactQuery, ...]:
    """Enumerate every nonconstant binary partition once, up to label swap."""

    if hypothesis_count < 2:
        raise ValueError("at least two hypotheses are required")
    rows: list[ExactQuery] = []
    for mask in range(1, 2 ** (hypothesis_count - 1)):
        outcomes = (0,) + tuple(
            1 if mask & (1 << (index - 1)) else 0
            for index in range(1, hypothesis_count)
        )
        rows.append(ExactQuery(name=f"q{mask:0{hypothesis_count - 1}b}", outcomes=outcomes))
    return tuple(rows)


def exhaustive_binary_campaign(max_hypotheses: int = 4) -> dict[str, object]:
    """Exhaust every binary-query family with per-query cost one or two.

    A query has exactly three statuses: absent, present at cost one, or present
    at cost two.  For ``N=2,3,4`` this is exactly 2,214 non-empty finite models.
    Each theorem-applicable model is also checked against Corollary 12.2 with
    ``lambda=(N-1)/N`` and ``c0=2``.
    """

    if not 2 <= max_hypotheses <= 4:
        raise ValueError("the frozen exhaustive campaign supports 2 <= N <= 4")
    enumerated = 0
    theorem_applicable = 0
    theorem_failures: list[dict[str, object]] = []
    corollary_applicable = 0
    corollary_failures: list[dict[str, object]] = []
    by_size: dict[str, int] = {}
    for hypothesis_count in range(2, max_hypotheses + 1):
        hypotheses = tuple(f"h{index}" for index in range(hypothesis_count))
        universe = canonical_binary_queries(hypothesis_count)
        size_count = 0
        for statuses in product((0, 1, 2), repeat=len(universe)):
            if not any(statuses):
                continue
            queries = tuple(
                ExactQuery(query.name, query.outcomes, Fraction(status))
                for query, status in zip(universe, statuses)
                if status
            )
            model = FiniteAcquisitionModel(hypotheses=hypotheses, queries=queries)
            enumerated += 1
            size_count += 1
            theorem = theorem_12_1_certificate(model)
            if theorem["assumptions_satisfied"]:
                theorem_applicable += 1
                if theorem["theorem_holds"] is not True:
                    theorem_failures.append(
                        {"N": hypothesis_count, "statuses": list(statuses), "certificate": theorem}
                    )
                corollary = corollary_12_2_certificate(
                    model,
                    Fraction(hypothesis_count - 1, hypothesis_count),
                    Fraction(2),
                )
                corollary_applicable += 1
                if corollary["conclusion_checked"] is not True:
                    corollary_failures.append(
                        {"N": hypothesis_count, "statuses": list(statuses), "certificate": corollary}
                    )
        by_size[str(hypothesis_count)] = size_count
    return {
        "campaign": "S12-EXHAUSTIVE-BINARY-N4",
        "enumerated_models": enumerated,
        "models_by_hypothesis_count": by_size,
        "theorem_applicable_models": theorem_applicable,
        "theorem_failures": theorem_failures,
        "corollary_applicable_models": corollary_applicable,
        "corollary_failures": corollary_failures,
        "all_applicable_claims_hold": not theorem_failures and not corollary_failures,
    }


def required_odd_repetitions(
    logical_steps: int,
    failure_tolerance: Fraction,
    noise_rate: Fraction,
    precision: int = 100,
) -> tuple[int, Decimal]:
    """Return the least odd integer above Proposition 12.3's threshold."""

    failure_tolerance = _as_fraction(failure_tolerance)
    noise_rate = _as_fraction(noise_rate)
    if logical_steps < 1:
        raise ValueError("m must be positive")
    if not 0 < failure_tolerance < 1:
        raise ValueError("delta must lie strictly between zero and one")
    if not 0 <= noise_rate < Fraction(1, 2):
        raise ValueError("nu must lie between zero inclusive and one half exclusive")
    with localcontext() as context:
        context.prec = precision
        ratio = Decimal(logical_steps) / _decimal_fraction(failure_tolerance)
        gap = Decimal(1) - Decimal(2) * _decimal_fraction(noise_rate)
        threshold = Decimal(2) * ratio.ln() / (gap * gap)
        integer = int(threshold.to_integral_value(rounding=ROUND_CEILING))
    if integer % 2 == 0:
        integer += 1
    return integer, threshold


def exact_majority_error(repetitions: int, noise_rate: Fraction) -> Fraction:
    """Exact worst rational majority tail for independent errors ``p_i <= nu``.

    The majority-error event is coordinatewise increasing, so its maximum over
    independent (not necessarily identical) error probabilities bounded by
    ``nu`` occurs when every probability equals ``nu``.
    """

    noise_rate = _as_fraction(noise_rate)
    if repetitions < 1 or repetitions % 2 == 0:
        raise ValueError("majority decoding requires a positive odd repetition count")
    if not 0 <= noise_rate < Fraction(1, 2):
        raise ValueError("nu must lie between zero inclusive and one half exclusive")
    threshold = repetitions // 2 + 1
    return sum(
        Fraction(comb(repetitions, errors))
        * noise_rate**errors
        * (1 - noise_rate) ** (repetitions - errors)
        for errors in range(threshold, repetitions + 1)
    )


def proposition_12_3_certificate(
    hypothesis_count: int,
    contraction: Fraction,
    failure_tolerance: Fraction,
    noise_rate: Fraction,
    repetition_cost: Fraction,
    majority_cost: Fraction,
    repetitions: int | None = None,
) -> dict[str, object]:
    """Check the displayed noise lift and its exact rational binomial tail."""

    contraction = _as_fraction(contraction)
    failure_tolerance = _as_fraction(failure_tolerance)
    noise_rate = _as_fraction(noise_rate)
    repetition_cost = _as_fraction(repetition_cost)
    majority_cost = _as_fraction(majority_cost)
    if repetition_cost < 0 or majority_cost < 0:
        raise ValueError("physical cost bounds must be non-negative")
    logical_steps = _contraction_step_limit(hypothesis_count, contraction)
    required, threshold = required_odd_repetitions(
        logical_steps,
        failure_tolerance,
        noise_rate,
    )
    selected = required if repetitions is None else repetitions
    odd = selected > 0 and selected % 2 == 1
    threshold_met = Decimal(selected) >= threshold
    exact_tail = exact_majority_error(selected, noise_rate) if odd else None
    exact_union = None if exact_tail is None else logical_steps * exact_tail

    with localcontext() as context:
        context.prec = 100
        gap = Decimal(1) - Decimal(2) * _decimal_fraction(noise_rate)
        one_step_hoeffding = (-Decimal(selected) * gap * gap / Decimal(2)).exp()
        union_hoeffding = Decimal(logical_steps) * one_step_hoeffding

    guarantee = odd and threshold_met
    exact_within_tolerance = (
        None if exact_union is None else exact_union <= failure_tolerance
    )
    cost_bound = logical_steps * (selected * repetition_cost + majority_cost)
    return {
        "proposition": "Imported Proposition 12.3",
        "subject_lines": [777, 795],
        "scope": (
            "Numerical consequence conditional on binary repeatability, conditional "
            "independence, and the per-repeat error bound; those physical assumptions "
            "are inputs, not established by this checker."
        ),
        "logical_steps_m": logical_steps,
        "required_odd_repetitions": required,
        "selected_repetitions": selected,
        "threshold_decimal": str(threshold),
        "odd_repetition_count": odd,
        "displayed_threshold_met": threshold_met,
        "theorem_guarantee_applies": guarantee,
        "exact_worst_iid_majority_error": (
            None if exact_tail is None else _fraction_text(exact_tail)
        ),
        "exact_union_upper_bound": (
            None if exact_union is None else _fraction_text(exact_union)
        ),
        "exact_union_within_delta": exact_within_tolerance,
        "hoeffding_union_bound_decimal": str(union_hoeffding),
        "closed_cost_bound": _fraction_text(cost_bound),
    }


def all_acquisition_checks() -> dict[str, object]:
    """Return the frozen exact campaign observables without hiding assumptions."""

    exhaustive = exhaustive_binary_campaign(max_hypotheses=4)
    whole = frozenset(("a", "b", "c"))
    tail = frozenset(("b", "c"))
    mutant_fixture = FiniteAcquisitionModel(
        hypotheses=("a", "b", "c"),
        queries=(
            ExactQuery("first", (0, 1, 1), Fraction(1)),
            ExactQuery("tail", (0, 0, 1), Fraction(10)),
        ),
        availability={whole: ("first",), tail: ("tail",)},
    )
    correct = optimal_worst_cost(mutant_fixture)
    mutant = mutant_best_case_cost(mutant_fixture)
    grid_points = 0
    grid_failures: list[dict[str, object]] = []
    for hypotheses, contraction, delta, noise in product(
        (2, 3, 8, 17),
        (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)),
        (Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)),
        (Fraction(0), Fraction(1, 10), Fraction(1, 4), Fraction(2, 5)),
    ):
        grid_points += 1
        certificate = proposition_12_3_certificate(
            hypotheses,
            contraction,
            delta,
            noise,
            Fraction(1),
            Fraction(0),
        )
        if not (
            certificate["theorem_guarantee_applies"]
            and certificate["exact_union_within_delta"]
        ):
            grid_failures.append(
                {
                    "N": hypotheses,
                    "lambda": _fraction_text(contraction),
                    "delta": _fraction_text(delta),
                    "nu": _fraction_text(noise),
                    "certificate": certificate,
                }
            )
    return {
        "theorem_12_1_and_corollary_12_2": exhaustive,
        "bellman_mutation_control": {
            "correct_worst_case_cost": None if correct is None else _fraction_text(correct),
            "mutant_best_case_cost": None if mutant is None else _fraction_text(mutant),
            "mutant_killed": correct != mutant,
        },
        "proposition_12_3_grid": {
            "points": grid_points,
            "failures": grid_failures,
            "all_exact_binomial_tails_within_delta": not grid_failures,
        },
        "limitations": [
            "The displayed Bellman recurrence does not use Pi, so this checker does not silently add it.",
            "Finite acquisition arithmetic does not establish physical test availability or W4 cost closure.",
            "The noise result is conditional on repeatability, independence, and per-repeat error bounds.",
        ],
    }
