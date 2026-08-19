#!/usr/bin/env python3
"""Replay the campaign independently and compare every deterministic byte."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import tempfile

from testpoietic.campaign import REPOSITORY_ROOT, compare_directories, write_campaign


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--evidence",
        type=Path,
        default=REPOSITORY_ROOT / "evidence" / "runs" / "campaign-001",
    )
    args = parser.parse_args()
    if not args.evidence.is_dir():
        print(json.dumps({"verified": False, "error": f"missing evidence directory: {args.evidence}"}))
        return 2
    with tempfile.TemporaryDirectory(prefix="testpoietic-replay-") as temp_name:
        replay = Path(temp_name) / "campaign-001"
        manifest = write_campaign(replay)
        comparison = compare_directories(args.evidence, replay)
    result = {
        "verified": bool(manifest["all_declared_checks_green"] and comparison["all_match"]),
        "replay_manifest_green": manifest["all_declared_checks_green"],
        "byte_comparison": comparison,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
