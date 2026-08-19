"""Deterministic source authentication and Markdown claim inventory."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import re
from pathlib import Path
from typing import Iterable

from .constants import DECLARED_PARENT_HASHES, PRIMARY_SHA256, PRIMARY_SUBJECT


GRADE_RE = re.compile(r"`\[([^\]]+)\]`")
BOLD_RE = re.compile(r"^\*\*(.+?)\*\*")
HEADING_CLAIM_RE = re.compile(
    r"^#{2,6}\s+(?P<kind>Theorem|Proposition|Lemma|Corollary)\s+"
    r"(?P<label>[A-Za-z0-9.]+)\b(?P<title>.*)$"
)

ALLOWED_GRADE_PREFIXES = {
    "axiom",
    "background",
    "background definition",
    "conditional",
    "conjecture",
    "countermodel",
    "elementary",
    "imported",
    "interface obligation",
    "interpretation",
    "optional axiom",
    "physical witness",
    "protocol",
    "residue",
}

CLAIM_WORDS = {
    "axiom",
    "background",
    "conjecture",
    "corollary",
    "lemma",
    "proposition",
    "residue",
    "separation",
    "theorem",
}


@dataclass(frozen=True)
class NamedClaim:
    label: str
    kind: str
    title: str
    line: int
    grade: str | None
    raw: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_subject_tree(repository_root: Path) -> dict[str, object]:
    primary_actual = sha256_file(PRIMARY_SUBJECT)
    parent_results: list[dict[str, object]] = []
    for name, expected in DECLARED_PARENT_HASHES.items():
        path = repository_root / "subject" / "provenance" / name
        actual = sha256_file(path)
        parent_results.append(
            {
                "path": str(path.relative_to(repository_root)),
                "expected": expected,
                "actual": actual,
                "match": actual == expected,
            }
        )
    return {
        "primary": {
            "path": str(PRIMARY_SUBJECT.relative_to(repository_root)),
            "expected": PRIMARY_SHA256,
            "actual": primary_actual,
            "match": primary_actual == PRIMARY_SHA256,
        },
        "parents": parent_results,
        "all_match": primary_actual == PRIMARY_SHA256
        and all(row["match"] for row in parent_results),
    }


def _first_label(text: str) -> str:
    without_grade = GRADE_RE.sub("", text).strip().rstrip(".")
    conjecture = re.match(r"Conjecture\s+([A-Za-z0-9]+)", without_grade)
    if conjecture:
        return conjecture.group(1)
    residue = re.match(r"Residue\s+(.+?)\s*\(", without_grade)
    if residue:
        return residue.group(1).strip()
    named = re.match(
        r"(?:Imported\s+)?(?:Theorem|Proposition|Lemma|Corollary|Separation)\s+"
        r"([A-Za-z0-9.]+)",
        without_grade,
    )
    if named:
        return named.group(1)
    token = without_grade.split(maxsplit=1)[0]
    return token.rstrip(",")


def _kind(text: str, grade: str | None) -> str:
    lower = text.lower()
    for word in (
        "imported theorem",
        "theorem",
        "proposition",
        "lemma",
        "corollary",
        "conjecture",
        "residue",
        "separation",
    ):
        if lower.startswith(word):
            return word
    if grade:
        return grade.split(" from ", 1)[0]
    return "named clause"


def extract_claims(path: Path = PRIMARY_SUBJECT) -> list[NamedClaim]:
    claims: list[NamedClaim] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        heading = HEADING_CLAIM_RE.match(line)
        if heading:
            claims.append(
                NamedClaim(
                    label=heading.group("label"),
                    kind=heading.group("kind").lower(),
                    title=heading.group("title").strip(" ."),
                    line=line_number,
                    grade=None,
                    raw=line,
                )
            )
            continue
        bold = BOLD_RE.match(line)
        if not bold:
            continue
        inside = bold.group(1).strip()
        lower_first = inside.split(maxsplit=1)[0].lower().rstrip(".,")
        grade_match = GRADE_RE.search(inside)
        grade = grade_match.group(1) if grade_match else None
        is_claim = (
            grade is not None
            or lower_first in CLAIM_WORDS
            or re.match(r"^(?:[ABCEFGJLRSTW]\d|A-NJ|B-Core|B-Universal|C2-P)", inside)
        )
        if not is_claim or inside.startswith("Proof."):
            continue
        claims.append(
            NamedClaim(
                label=_first_label(inside),
                kind=_kind(inside, grade),
                title=GRADE_RE.sub("", inside).strip().rstrip("."),
                line=line_number,
                grade=grade,
                raw=line,
            )
        )
    return claims


def grade_audit(claims: Iterable[NamedClaim]) -> dict[str, object]:
    claims = list(claims)
    unknown: list[dict[str, object]] = []
    ungraded_formal: list[dict[str, object]] = []
    for claim in claims:
        if claim.grade:
            prefix = claim.grade.split(" from ", 1)[0]
            prefix = prefix.split(",", 1)[0]
            if prefix not in ALLOWED_GRADE_PREFIXES:
                unknown.append(asdict(claim))
        elif claim.kind in {"theorem", "proposition", "lemma", "corollary"}:
            ungraded_formal.append(asdict(claim))
    return {
        "claim_count": len(claims),
        "unknown_grade_count": len(unknown),
        "unknown_grades": unknown,
        "ungraded_formal_count": len(ungraded_formal),
        "ungraded_formal_claims": ungraded_formal,
    }


def section_metrics(path: Path = PRIMARY_SUBJECT) -> dict[str, object]:
    """Measure a frozen, disclosed meta/theory partition without interpreting it."""

    lines = path.read_text(encoding="utf-8").splitlines()
    headings: list[tuple[int, str]] = [
        (index, line)
        for index, line in enumerate(lines, 1)
        if line.startswith("### ")
    ]

    meta_prefixes = (
        "### 0.",
        "### P0.",
        "### I5.",
        "### I6.",
        "### I7.",
        "### I11.",
    )
    category_by_line: dict[int, str] = {}
    current = "theory"
    for line_number, line in enumerate(lines, 1):
        if line.startswith("### "):
            current = "meta" if line.startswith(meta_prefixes) else "theory"
        if line_number <= 56:
            current = "meta"
        category_by_line[line_number] = current

    result: dict[str, dict[str, int]] = {
        "meta": {"lines": 0, "nonblank_lines": 0, "words": 0, "characters": 0},
        "theory": {"lines": 0, "nonblank_lines": 0, "words": 0, "characters": 0},
    }
    for number, line in enumerate(lines, 1):
        bucket = result[category_by_line[number]]
        bucket["lines"] += 1
        bucket["nonblank_lines"] += int(bool(line.strip()))
        bucket["words"] += len(line.split())
        bucket["characters"] += len(line) + 1

    total_words = result["meta"]["words"] + result["theory"]["words"]
    result["meta"]["word_fraction_ppm"] = round(
        1_000_000 * result["meta"]["words"] / total_words
    )
    return {
        "partition_rule": {
            "front_matter_lines": "1-56",
            "meta_section_prefixes": list(meta_prefixes),
            "all_other_lines": "theory",
        },
        "headings_seen": len(headings),
        "metrics": result,
    }
