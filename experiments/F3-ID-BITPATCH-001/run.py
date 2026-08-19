#!/usr/bin/env python3
"""Materialize the frozen F3 discriminator to a caller-selected directory."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY_ROOT))
from testpoietic.f3_identifiability import run_bitpatch_family


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    result = run_bitpatch_family()
    summary_path = args.output_directory / "summary.json"
    summary_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    rows_path = args.output_directory / "results.csv"
    with rows_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "n",
                "serial_cost",
                "batch_cost",
                "delivered_bits",
                "batch_uses_fringe",
                "batch_library_local",
                "batch_strictly_cheaper",
                "mutant_killed",
            ),
        )
        writer.writeheader()
        for row in result["rows"]:
            writer.writerow(
                {
                    "n": row["n"],
                    "serial_cost": row["serial"]["total_cost"],
                    "batch_cost": row["batch"]["total_cost"],
                    "delivered_bits": row["batch"]["delivered_bits"],
                    "batch_uses_fringe": row["batch"]["uses_failure_fringe"],
                    "batch_library_local": row["batch"]["library_local"],
                    "batch_strictly_cheaper": row["batch_strictly_cheaper"],
                    "mutant_killed": row["mutant_omits_final_appraisal"],
                }
            )
    print(json.dumps({"summary": str(summary_path), "rows": str(rows_path)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
