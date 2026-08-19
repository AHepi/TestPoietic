"""Deterministic source-anchored audits of protocol/claim alignment.

This module deliberately does not decide whether any field conjecture is true.
It checks whether the frozen prose supplies a refuter with the same quantifier
scope as its displayed claim and whether a named protocol is closed enough to
identify its experimental arms.  All checks are pure, standard-library-only,
and accept text explicitly so that repaired and mutation fixtures can be
evaluated without changing the pinned subject.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from pathlib import Path

from .constants import PRIMARY_SUBJECT


@dataclass(frozen=True)
class LineAnchor:
    """An exact UTF-8 source line expected at a one-based line number."""

    identifier: str
    line: int
    expected: str


LINE_ANCHORS = (
    LineAnchor(
        "conjecture-o",
        411,
        "**Conjecture O (Optimism). `[conjecture]`** Problems not forbidden by physical law admit explanatory resolutions or transformations that can in principle be created by enlarging the relevant repertoire. Existence is the conjectural burden; T10 keeps recognition fallible. A well-specified physically admissible problem for which no possible explanatory resolution or transforming knowledge exists refutes the conjecture.",
    ),
    LineAnchor(
        "fertility-conjecture",
        570,
        "**Fertility Conjecture. `[conjecture]`** Among matched-budget systems with A5-mediated promotion, universal reach, a content guard, and an unbounded evaluated problem source, policies that convert informative failure fringes into construction targets achieve greater long-run delivered content or lower assembly cost than library-local, promotion-shy, or directionless policies, except where the fringe carries no useful localization.",
    ),
    LineAnchor(
        "r-g-heading",
        825,
        "**Residue \\(R_G\\) (answer-generic jump construction). `[residue]`** For a declared scaling family and one preregistered success mode,",
    ),
    LineAnchor("r-g-exists", 830, "\\exists G\\;"),
    LineAnchor("r-g-forall", 831, "\\forall n\\in I\\;"),
    LineAnchor(
        "r-g-refuter-prose",
        843,
        "where \\(G\\Downarrow_n(\\mathcal M_n,\\alpha_n)\\) means that the fixed architecture constructs the stagewise acquisition model and its physical application witness inside the declared closed account. A cut with an invalid application witness, an answer-indexed specialist, target leakage, an omitted terminal-relevant cost, or a missed preregistered threshold refutes the universal claim on that declared family. Failure merely to nominate such a \\(G\\) is **INCONCLUSIVE** unless the architecture class is exhaustively reduced. No admissible F8-D run is supplied here, so \\(R_G\\) is **UNTESTED**. It is not a premise of the finite-prefix capstone unless an application explicitly adds it.",
    ),
    LineAnchor(
        "r-x-heading",
        1416,
        "**Residue \\(R_X^{\\Phi}\\) (protected physical extension). `[residue]`**",
    ),
    LineAnchor(
        "r-x-existential-consequent",
        1423,
        "\\text{some }[q]\\in W_t\\text{ has a Poietic extension-ready task }A_q",
    ),
    LineAnchor(
        "r-x-refuter-prose",
        1428,
        "This is the precise seam. Spark supplies the open good problem and A5 provenance. Poietic supplies physical executability, predecessor preservation or reconstruction, resources, coupling, persistence, and boundary closure. No theorem in either book proves this residue. A live problem with no extension-ready good resolution refutes it at that cut.",
    ),
    LineAnchor(
        "ledger-o-to-f6",
        1501,
        "| Conjecture O | source optimism and physical admissibility frame | stage-local solubility interpretation | a physically admissible problem with no possible resolution or transforming knowledge | F6 |",
    ),
    LineAnchor(
        "protocol-f3",
        1596,
        "**F3, failure-fringe policy tournament. `[protocol for the Fertility Conjecture]`** Compare failure-fringe targeting with library-local, promotion-shy, and directionless policies using the same seed, model architecture, target stream, available operators, appraisal battery, promotion constitution, and W4-closed budget. Predeclare either delivered content at fixed cost or cost to a fixed delivered-content target as the primary measure. Stratify cases in which the fringe contains no usable localization before the result is known. Matched-budget domination by a rival on the preregistered scaling family refutes the Fertility Conjecture on that family.",
    ),
    LineAnchor(
        "protocol-f6",
        1602,
        "**F6, residue stress test. `[protocol for the finite-prefix capstone]`** Before the base step, exhibit or fail \\(\\operatorname{CreativeCapacity}(\\mathcal K_0)\\) and \\(R_{P,0}\\) separately. At every successor cut, separately exhibit or fail \\(R_{P,+}\\), \\(R_S\\), and \\(R_X^{\\Phi}\\) on the accumulated predecessor cut. No residue may be inferred from the others, from Conjecture O, or from the boxed capstone. A missing witness blocks the next prefix and records exactly which residue failed; the composition theorem remains intact but inapplicable.",
    ),
    LineAnchor(
        "protocol-f8-d",
        1614,
        "**F8-D, answer-generic jump construction.** Freeze \\(G\\), its seed schema, the scaling family, answer boundary, matched answer-free whole-account benchmark, cost account, stopping rule, and exactly one success mode before target outcomes. At each cut require \\(G\\) itself to construct \\(\\mathcal M_n\\) and \\(\\alpha_n\\), then audit answer-freedom, W4 cost closure, W5 boundary closure, and the preregistered threshold. One hidden specialist, invalid application witness, omitted terminal-relevant cost, leakage event, or threshold miss refutes \\(R_G\\) on the declared family. Failure to discover a qualifying architecture is **INCONCLUSIVE** unless the architecture class is exhaustively reduced.",
    ),
)


F3_POLICY_TERMS = (
    "failure-fringe targeting",
    "library-local",
    "promotion-shy",
    "directionless",
)


def check_line_anchors(text: str) -> list[dict[str, object]]:
    """Return exact, stable line checks without hiding the observed source."""

    lines = text.splitlines()
    results: list[dict[str, object]] = []
    for anchor in LINE_ANCHORS:
        actual = lines[anchor.line - 1] if anchor.line <= len(lines) else None
        results.append(
            {
                **asdict(anchor),
                "actual": actual,
                "match": actual == anchor.expected,
            }
        )
    return results


def _between(text: str, start: str, end: str) -> str:
    start_at = text.find(start)
    if start_at < 0:
        return ""
    end_at = text.find(end, start_at + len(start))
    if end_at < 0:
        end_at = len(text)
    return text[start_at:end_at]


def rg_f8d_quantifier_audit(text: str) -> dict[str, object]:
    """Check the existential R_G witness against F8-D's one-witness verdict."""

    residue = _between(text, "**Residue \\(R_G\\)", "### S13.")
    protocol = _between(text, "**F8-D,", "The raw protocol traces")
    exists_at = residue.find("\\exists G")
    forall_at = residue.find("\\forall n\\in I")
    existential_outer_scope = 0 <= exists_at < forall_at
    one_witness_failure_claims_residue_refutation = (
        "One hidden specialist, invalid application witness, omitted terminal-relevant "
        "cost, leakage event, or threshold miss refutes \\(R_G\\) on the declared "
        "family."
        in protocol
    )

    # A finite truth table is a direct discriminator: the frozen witness can
    # fail while another witness keeps the existential residue true.
    cuts = (1, 2)
    architectures = {
        "G_frozen": {1: True, 2: False},
        "G_other": {1: True, 2: True},
    }
    frozen_g_fails = not all(architectures["G_frozen"][cut] for cut in cuts)
    residue_true = any(
        all(outcomes[cut] for cut in cuts)
        for outcomes in architectures.values()
    )
    mismatch = (
        existential_outer_scope
        and one_witness_failure_claims_residue_refutation
        and frozen_g_fails
        and residue_true
    )
    return {
        "id": "RG-F8D-QUANTIFIER-SCOPE",
        "source_lines": [825, 830, 831, 843, 1614],
        "outer_quantifier_is_existential": existential_outer_scope,
        "protocol_claims_one_frozen_witness_failure_refutes_residue": (
            one_witness_failure_claims_residue_refutation
        ),
        "finite_discriminator": {
            "cuts": list(cuts),
            "architectures": architectures,
            "frozen_G_fails": frozen_g_fails,
            "R_G_true": residue_true,
        },
        "mismatch": mismatch,
        "required_refuter": (
            "forall G in an exhaustive declared architecture class, exists n in I "
            "such that the success conjunction fails"
        ),
    }


def rx_refuter_scope_audit(text: str) -> dict[str, object]:
    """Check whether R_X prose negates its existential consequent completely."""

    residue = _between(
        text,
        "**Residue \\(R_X^{\\Phi}\\)",
        "All open-endedness in the capstone",
    )
    existential_consequent = "\\text{some }[q]\\in W_t" in residue
    single_bad_member_refuter = (
        "A live problem with no extension-ready good resolution refutes it at that cut."
        in residue
    )

    extension_ready = {"q_bad": False, "q_good": True}
    antecedent = bool(extension_ready)
    residue_true = (not antecedent) or any(extension_ready.values())
    prose_triggered = any(not ready for ready in extension_ready.values())
    mismatch = (
        existential_consequent
        and single_bad_member_refuter
        and residue_true
        and prose_triggered
    )
    return {
        "id": "RX-PROSE-REFUTER-SCOPE",
        "source_lines": [1416, 1419, 1423, 1428],
        "consequent_is_existential": existential_consequent,
        "prose_uses_single_bad_member_refuter": single_bad_member_refuter,
        "finite_discriminator": {
            "extension_ready": extension_ready,
            "prose_refuter_triggered": prose_triggered,
            "R_X_true": residue_true,
        },
        "mismatch": mismatch,
        "required_refuter": (
            "W_t is nonempty and every q in W_t lacks an extension-ready task "
            "for the same accumulated predecessor cut beta"
        ),
    }


def optimism_f6_address_audit(text: str) -> dict[str, object]:
    """Check whether the ledger's O -> F6 address has an O verdict rule."""

    conjecture = _between(text, "**Conjecture O", "### S8.")
    f6 = _between(text, "**F6,", "**F7,")
    ledger_routes_to_f6 = bool(
        re.search(r"^\| Conjecture O .*\| F6 \|$", text, flags=re.MULTILINE)
    )
    conjecture_has_refuter = all(
        phrase in conjecture
        for phrase in (
            "physically admissible problem",
            "no possible explanatory resolution or transforming knowledge exists",
            "refutes the conjecture",
        )
    )
    f6_excludes_inference_from_o = "from Conjecture O" in f6
    f6_has_o_verdict_rule = (
        "physically admissible problem" in f6
        and "no possible explanatory resolution or transforming knowledge exists" in f6
        and bool(re.search(r"refutes (?:Conjecture )?O\b", f6))
    )
    mismatch = (
        ledger_routes_to_f6
        and conjecture_has_refuter
        and f6_excludes_inference_from_o
        and not f6_has_o_verdict_rule
    )
    return {
        "id": "O-F6-MISSING-VERDICT-RULE",
        "source_lines": [411, 1501, 1602],
        "ledger_routes_O_to_F6": ledger_routes_to_f6,
        "O_declares_a_refuter": conjecture_has_refuter,
        "F6_excludes_inference_from_O": f6_excludes_inference_from_o,
        "F6_has_O_specific_verdict_rule": f6_has_o_verdict_rule,
        "mismatch": mismatch,
        "required_protocol_content": (
            "a preregistered physical-admissibility domain and a witness rule for a "
            "problem with no possible explanatory resolution or transforming knowledge"
        ),
    }


def _normal_form(line: str) -> str:
    return re.sub(r"[*_`]", "", line).casefold()


def _definition_lines(text: str, term: str) -> list[int]:
    escaped = re.escape(term.casefold())
    patterns = (
        re.compile(rf"\b{escaped}\b\s+(?:means|iff|is defined as)\b"),
        re.compile(rf"\bdefine(?:s|d)?\b.*\b{escaped}\b"),
        re.compile(
            rf"\b(?:a|the)\s+policy\s+is\s+{escaped}\b\s+"
            rf"(?:iff|when|exactly when)\b"
        ),
    )
    found: list[int] = []
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = _normal_form(raw)
        if term.casefold() in line and any(pattern.search(line) for pattern in patterns):
            found.append(line_number)
    return found


def f3_policy_closure_audit(text: str) -> dict[str, object]:
    """Inventory F3 arm definitions and an overlap-assignment rule."""

    f3 = _between(text, "**F3,", "**F4,")
    named_in_f3 = [term for term in F3_POLICY_TERMS if term in f3.casefold()]
    definitions = {term: _definition_lines(text, term) for term in F3_POLICY_TERMS}
    undefined = [term for term, lines in definitions.items() if not lines]
    normalized = _normal_form(text)
    mutually_exclusive = (
        "f3 policy classes are mutually exclusive" in normalized
        or "f3 policy classes are pairwise disjoint" in normalized
    )
    explicit_overlap_assignment = (
        "f3 policy classes" in normalized
        and "overlap" in normalized
        and ("assign" in normalized or "priority" in normalized)
    )
    arm_assignment_closed = (
        not undefined and (mutually_exclusive or explicit_overlap_assignment)
    )

    overlap_witness = {
        "policy": "local library repair chosen from retained failure traces; promotion delayed",
        "failure-fringe targeting": True,
        "library-local": True,
        "promotion-shy": True,
    }
    mismatch = (
        set(named_in_f3) == set(F3_POLICY_TERMS)
        and (bool(undefined) or not arm_assignment_closed)
    )
    return {
        "id": "F3-POLICY-ARMS-NONCLOSED",
        "source_lines": [570, 1596],
        "policy_terms_named_in_F3": named_in_f3,
        "definition_lines": definitions,
        "undefined_terms": undefined,
        "mutually_exclusive_rule": mutually_exclusive,
        "overlap_assignment_rule": explicit_overlap_assignment,
        "arm_assignment_closed": arm_assignment_closed,
        "overlap_witness_under_ordinary_reading": overlap_witness,
        "mismatch": mismatch,
        "required_protocol_content": (
            "outcome-independent membership predicates for all four arms plus either "
            "pairwise exclusivity or a preregistered overlap assignment rule"
        ),
    }


def audit_protocol_text(text: str) -> dict[str, object]:
    """Run every protocol audit and expose all intermediate observables."""

    anchors = check_line_anchors(text)
    findings = [
        rg_f8d_quantifier_audit(text),
        rx_refuter_scope_audit(text),
        optimism_f6_address_audit(text),
        f3_policy_closure_audit(text),
    ]
    return {
        "line_anchors": anchors,
        "all_line_anchors_match": all(row["match"] for row in anchors),
        "findings": findings,
        "mismatch_count": sum(bool(row["mismatch"]) for row in findings),
    }


def audit_protocol_file(path: Path = PRIMARY_SUBJECT) -> dict[str, object]:
    return audit_protocol_text(path.read_text(encoding="utf-8"))
