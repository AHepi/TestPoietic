### P1 - Record observation inside critical package

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e1}
  CritPkg = {pkg1}
  Record = {r1}
Relations (extensional):
  omega_chi: r1 -> Observation
  episode: r1 -> e1
  in_pkg: {(r1, pkg1)}
Classification: Record(o_chi); omega_chi = Observation; episode e1; inside CritPkg pkg1.
Admitted: yes.

### N1 - Deduction channel, not a Record (minimal pair with P1)

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e1}
  CritPkg = {pkg1}
  Record = {r1}
Relations (extensional):
  omega_chi: r1 -> Deduction
  episode: r1 -> e1
  in_pkg: {(r1, pkg1)}
Difference from P1: omega_chi(r1) = Deduction, not Observation.
Classification: Deduction(d_chi), not Record(o_chi).
Admitted: no -- wrong channel type.

### P2 - Bare record with channel typing, outside any CritPkg

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e2}
  CritPkg = {}
  Record = {r2}
Relations (extensional):
  omega_chi: r2 -> Observation
  episode: r2 -> e2
  in_pkg: {}
Classification: Record(o_chi); omega_chi = Observation; episode e2; NOT in any CritPkg (bare record).
Admitted: yes -- bare record is still a Record; evidence only inside typed package (POPPER_LSCD/POPPER_CNR), but the record itself exists.

### N2 - Bare mark with no episode binding (minimal pair with P2)

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {}
  CritPkg = {}
  Record = {r2}
Relations (extensional):
  omega_chi: r2 -> Observation
  episode: (unbound)
  in_pkg: {}
Difference from P2: episode(r2) is unbound -- no episode binding.
Classification: Bare mark with channel typing but no episode reference.
Admitted: no -- a Record must bind to an episode; a bare mark is not a record.

### P3 - Record with score value inside critical package

Sorts: Channel, Episode, CritPkg, Record, Score
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e3}
  CritPkg = {pkg2}
  Record = {r3}
  Score = {0.7}
Relations (extensional):
  omega_chi: r3 -> Observation
  episode: r3 -> e3
  in_pkg: {(r3, pkg2)}
  score: r3 -> 0.7
Classification: Record(o_chi); omega_chi = Observation; score 0.7; inside CritPkg pkg2.
Admitted: yes.

### N3 - Prediction channel with score, not a Record (minimal pair with P3)

Sorts: Channel, Episode, CritPkg, Record, Score
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e3}
  CritPkg = {pkg2}
  Record = {r3}
  Score = {0.7}
Relations (extensional):
  omega_chi: r3 -> Prediction
  episode: r3 -> e3
  in_pkg: {(r3, pkg2)}
  score: r3 -> 0.7
Difference from P3: omega_chi(r3) = Prediction, not Observation.
Classification: Prediction(d_chi), not Record(o_chi).
Admitted: no -- wrong channel type.

### P4 - TOO-STRONG WALL: bare episode record outside any CritPkg (BareScore fixture shape)

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e4}
  CritPkg = {}
  Record = {r4}
Relations (extensional):
  omega_chi: r4 -> Observation
  episode: r4 -> e4
  in_pkg: {}
Classification: BareScore = Record(o_chi) AND NOT CritPkg. Genuine bare episode record with channel typing, outside any critical package.
Admitted: yes -- this IS a Record; too-strong pinning (only package-internal FCritPkg-shaped tuples count) would WRONGLY EXCLUDE this.
Wall role: too-strong wall (positive that too-strong reading wrongly excludes).

### N4 - TOO-WEAK WALL: untyped artefact with no episode channel (minimal pair with P4)

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e4}
  CritPkg = {}
  Record = {r4}
Relations (extensional):
  omega_chi: (untyped -- no channel assignment)
  episode: r4 -> e4
  in_pkg: {}
Difference from P4: omega_chi(r4) is absent/untyped -- no episode channel.
Classification: Untyped artefact with episode binding but no channel typing. Not a Record.
Admitted: no -- too-weak pinning (any bare mark or score counts as a record regardless of typing) would WRONGLY ADMIT this.
Wall role: too-weak wall (near-miss that too-weak reading wrongly admits).

### B1 - OPEN: self-referential episode binding

Sorts: Channel, Episode, CritPkg, Record
Elements:
  Channel = {Observation, Deduction, Prediction}
  Episode = {e5}
  CritPkg = {pkg3}
  Record = {r5}
Relations (extensional):
  omega_chi: r5 -> Observation
  episode: r5 -> e5
  self_ref: e5 = r5 (the episode is the record itself)
  in_pkg: {(r5, pkg3)}
Classification: Record(o_chi) with omega_chi = Observation, but episode e5 is identical to record r5 (self-referential).
OPEN question: Does a Record require the episode to be distinct from the record itself, or is self-referential episode binding permitted? If episode must be distinct, this is a near-miss; if self-reference is allowed, this is a positive.

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | 9cb850bba0b2bdb4 |
| N1 | near-miss | P1 | 1279583f62a3b1a7 |
| P2 | positive | N2 | bcaa588e6b67aa71 |
| N2 | near-miss | P2 | a3e28dca53b6e907 |
| P3 | positive | N3 | 96e56ae1b06d6c3e |
| N3 | near-miss | P3 | d5edcf1170248ba5 |
| P4 | positive | N4 | 20c8e6d27f053b4b |
| N4 | near-miss | P4 | 7f1ef05be2fa0871 |
| B1 | boundary | - | e67ad05ed6973bde |
