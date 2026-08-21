# .swarm/

Coordination state for the swarm orchestrator protocol (scripts/swarm_gate.py).

- board.json — task board (WIP limit 2, require_remote auto).
- map.md — regenerated locally with `python3 scripts/swarm_gate.py map`; intentionally not committed (a generated map goes stale on every push; regenerate on your own checkout).
- log.jsonl — the gate's own hash-chained log, created by `swarm_gate.py init` on your checkout.
- manual-log-rule9.jsonl — the orchestrator's manual rule-9 log from the 2026-08-20/21 session, before the gate was installed. It is NOT hash-chained and must not be renamed to log.jsonl.
