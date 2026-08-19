#!/usr/bin/env python3
"""Execute the frozen piecemeal campaign.

Usage:
    PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/run_piecemeal_campaign.py \
        [--plan evidence/frozen/piecemeal-plan-v1.json] \
        [--out evidence/runs/piecemeal-001]

Stdlib only.  Writes canonical artifacts and prints the manifest verdict.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from testpoietic.piecemeal import run_campaign  # noqa: E402

SUBJECT_SHA256 = "9c5d389afc1f334733604083710f6625638b8933825a6312c7403e7de08dafbc"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default=str(REPO_ROOT / "evidence" / "frozen" / "piecemeal-plan-v1.json"))
    parser.add_argument("--out", default=str(REPO_ROOT / "evidence" / "runs" / "piecemeal-001"))
    args = parser.parse_args()

    manifest = run_campaign(Path(args.plan), Path(args.out), SUBJECT_SHA256)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0 if manifest["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
