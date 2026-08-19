#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from testpoietic.campaign import write_campaign


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    manifest = write_campaign(args.output_directory)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0 if manifest["all_declared_checks_green"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
