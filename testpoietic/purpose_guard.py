"""Mechanical audit of the purpose-coverage guard's reproducibility."""

from __future__ import annotations

from pathlib import Path
import re

from .constants import PRIMARY_SUBJECT


def _guard_section(text: str) -> str:
    start = text.find("#### Purpose-coverage guard")
    end = text.find("### I6.", start)
    return text[start:end] if start >= 0 and end > start else ""


def _purpose_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw in section.splitlines():
        if not raw.startswith("| ") or raw.startswith("| ---"):
            continue
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        if cells and cells[0] in {
            "What creativity is",
            "What a creator must be",
            "How attribution and refutation proceed",
        }:
            rows.append(cells)
    return rows


def validate_transport_manifest(manifest: dict[str, object] | None) -> dict[str, object]:
    required_rows = {
        "what_creativity_is",
        "what_a_creator_must_be",
        "how_attribution_and_refutation_proceed",
    }
    required_faces = {"K", "S", "F", "M"}
    if not isinstance(manifest, dict) or not isinstance(manifest.get("rows"), dict):
        return {"valid": False, "reason": "no typed transport manifest", "mapped_faces": 0}
    rows = manifest["rows"]
    if set(rows) != required_rows:
        return {"valid": False, "reason": "row identity mismatch", "mapped_faces": 0}
    mapped = 0
    for row in required_rows:
        faces = rows[row]
        if not isinstance(faces, dict) or set(faces) != required_faces:
            return {"valid": False, "reason": f"face identity mismatch in {row}", "mapped_faces": mapped}
        for face in required_faces:
            record = faces[face]
            if not isinstance(record, dict):
                return {"valid": False, "reason": "untyped face record", "mapped_faces": mapped}
            if not all(record.get(field) for field in ("source_nodes", "target_nodes", "grade", "refuter")):
                return {"valid": False, "reason": "incomplete face witness", "mapped_faces": mapped}
            mapped += 1
    return {"valid": mapped == 12, "reason": None, "mapped_faces": mapped}


def audit_purpose_guard(
    text: str,
    transport_manifest: dict[str, object] | None = None,
) -> dict[str, object]:
    section = _guard_section(text)
    rows = _purpose_rows(section)
    nonempty_face_cells = sum(
        bool(cell.strip())
        for row in rows
        for cell in row[1:5]
    )
    displayed_score = bool(re.search(r"pcov.*=12", section, flags=re.DOTALL))
    mapping = validate_transport_manifest(transport_manifest)
    decision_language = any(
        phrase in section.casefold()
        for phrase in ("decision procedure", "machine-readable grammar", "canonical syntax")
    )
    standing_inheritance = (
        "inherited by the next revision" in section
        and "changing either is first scored" in section
    )
    retroactive_verdict_asserted = "FAIL: UNPRICED PURPOSE RETREAT" in section
    return {
        "subject_lines": [1543, 1582, 1805],
        "table_rows": len(rows),
        "nonempty_face_cells": nonempty_face_cells,
        "surface_pcov_12_reproduced": displayed_score and nonempty_face_cells == 12,
        "transport_manifest": mapping,
        "face_membership_decision_procedure_declared": decision_language,
        "retroactive_pret_verdict_asserted": retroactive_verdict_asserted,
        "retroactive_pret_verdict_recomputable": bool(mapping["valid"]),
        "standing_inheritance_gate": standing_inheritance,
        "declared_inferential_force": "none" if "creates no inference" in section else "not found",
        "audit_verdict": (
            "REPRODUCIBLE"
            if displayed_score and nonempty_face_cells == 12 and mapping["valid"] and decision_language
            else "SURFACE SCORE REPRODUCES; SEMANTIC TRANSPORT DOES NOT"
        ),
    }


def audit_primary_purpose_guard() -> dict[str, object]:
    return audit_purpose_guard(PRIMARY_SUBJECT.read_text(encoding="utf-8"))
