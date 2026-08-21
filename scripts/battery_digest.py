#!/usr/bin/env python3
"""Compute and verify per-instance content digests in a battery file.

Battery instances are '### <ID> — <title>' sections each containing at
least one fenced code block (the explicit structure). The digest of an
instance is sha256 over the concatenated contents of its fenced blocks
(in the order they appear), UTF-8, with trailing whitespace stripped per
line. Models never compute these: they write PENDING-DIGEST (or anything)
in the registry's digest column; this script fills or verifies it.

Usage:
    battery_digest.py FILE --write    # rewrite registry digests in place
    battery_digest.py FILE --verify   # exit 1 if any digest is wrong/missing
    battery_digest.py FILE --print    # print ID<TAB>digest lines
"""
from __future__ import annotations

import hashlib
import re
import sys

HEAD = re.compile(r"^###\s+([A-Za-z0-9_-]+)\s+[—\-]")
FENCE = re.compile(r"^```")
ROW = re.compile(r"^(\|\s*([A-Za-z0-9_-]+)\s*\|[^|]*\|)\s*[^|]*\|")
PENDING = "PENDING-DIGEST"


def instance_digests(text: str) -> dict[str, str]:
    digests: dict[str, str] = {}
    current: str | None = None
    in_fence = False
    buf: list[str] = []
    blocks: list[str] = []

    def flush() -> None:
        if current is None or not blocks:
            return
        payload = "\n".join(blocks)
        digests[current] = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    for line in text.splitlines():
        m = HEAD.match(line)
        if m and not in_fence:
            flush()
            current = m.group(1)
            blocks = []
            continue
        if FENCE.match(line):
            if in_fence:
                blocks.append("\n".join(x.rstrip() for x in buf))
                buf = []
                in_fence = False
            else:
                in_fence = True
            continue
        if in_fence:
            buf.append(line)
        elif line.startswith("## ") and current is not None:
            flush()
            current = None
            blocks = []
    flush()
    return digests


def rewrite(text: str, digests: dict[str, str]) -> tuple[str, list[str]]:
    out = []
    missing = []
    in_registry = False
    for line in text.splitlines():
        if line.strip().lower().startswith("## instance registry"):
            in_registry = True
        elif line.startswith("## ") and in_registry:
            in_registry = False
        if in_registry:
            m = ROW.match(line)
            if m and m.group(2) in digests:
                line = f"{m.group(1)} {digests[m.group(2)][:12]} |"
        out.append(line)
    for iid in digests:
        if not any(f"| {iid} " in l or f"|{iid} " in l or f"| {iid} " in l
                   for l in out if l.startswith("|")):
            # instance has no registry row
            missing.append(iid)
    return "\n".join(out) + "\n", missing


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[2] not in ("--write", "--verify", "--print"):
        print(__doc__)
        return 2
    path, mode = sys.argv[1], sys.argv[2]
    text = open(path, encoding="utf-8").read()
    digests = instance_digests(text)
    if not digests:
        print(f"FAIL: no instances found in {path}")
        return 1
    new_text, missing = rewrite(text, digests)
    if mode == "--print":
        for iid, d in digests.items():
            print(f"{iid}\t{d[:12]}")
        return 0
    if missing:
        print(f"FAIL: instances without registry rows: {', '.join(missing)}")
        return 1
    if mode == "--write":
        open(path, "w", encoding="utf-8").write(new_text)
        print(f"OK: wrote {len(digests)} digests into {path}")
        return 0
    # --verify
    if new_text != text:
        bad = [iid for iid, d in digests.items()
               if f"| {d[:12]} |" not in text]
        print(f"FAIL: stale or placeholder digests for: {', '.join(bad) or 'registry'}")
        return 1
    print(f"OK: {len(digests)} instance digests verified in {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
