# Battery: MovedConstructorPort

**Term:** MovedConstructorPort (inventory section 2, N7 row, D12 family)

**Intended meaning:** A structural configuration in which a constructor C,
originally hosted on port p of boundary B, is hosted on port p' of boundary
B' after a boundary move, with the move relation linking (B, p) to (B', p').

**BoundaryMove conjunction:** B'!=B AND SameObservableLabel AND MovedConstructorPort.

---

## Positive instances

### P1 - Simple move with explicit vacatur

```text
boundary B  : port p  hosts constructor C
boundary B' : port p' hosts constructor C
move M      : (B, p) -> (B', p')
vacated     : (B, p) after M
```

MovedConstructorPort holds: C moved from (B, p) to (B', p'), and the source
port is explicitly vacated.

### P2 - Move with redirect from old port

```text
boundary B  : port p  hosted constructor C
boundary B' : port p' hosts constructor C
move M      : (B, p) -> (B', p')
redirect    : requests to (B, p) forward to (B', p')
```

MovedConstructorPort holds even though (B, p) is not vacated; the redirect
is move-evidence, not continued hosting.

### P3 - Move with provenance record of origin

```text
boundary B' : port p' hosts constructor C
provenance  : C.origin = (B, p)
move M      : (B, p) -> (B', p') recorded at t
```

MovedConstructorPort holds on provenance alone; no live observation of the
source port is required.

---

## Near-miss minimal pairs

### N1 - Copy, not move (pair with P1)

```text
boundary B  : port p  hosts constructor C
boundary B' : port p' hosts constructor C
copy K      : (B, p) -> (B', p')
```

Differs from P1 only in the relation label: copy, not move. C is still
hosted at the source. MovedConstructorPort FAILS.

### N2 - Different constructor at destination (pair with P2)

```text
boundary B  : port p  hosted constructor C
boundary B' : port p' hosts constructor D
move M      : (B, p) -> (B', p')
redirect    : requests to (B, p) forward to (B', p')
```

Differs from P2 only in the destination constructor identity (D != C).
MovedConstructorPort FAILS: nothing moved.

### N3 - No move relation linking source and destination (pair with P3)

```text
boundary B  : port p  hosts constructor C
boundary B' : port p' hosts constructor C
```

Differs from P3 only in the absence of any move/provenance record. Two
ports hosting C with no linking move relation. MovedConstructorPort FAILS.

---

## Corridor walls

### W-WEAK - Too-weak reading wrongly admits: non-constructor moved between ports

```text
boundary B  : port p  holds value v
boundary B' : port p' holds value v
move M      : (B, p) -> (B', p') of value v
```

A too-weak reading (anything relocated between ports counts) wrongly admits
this. v is a value, not a constructor. MovedConstructorPort must FAIL here.

### W-STRONG - Too-strong reading wrongly excludes: implicit vacatur (no explicit vacated relation)

```text
boundary B  : port p  hosted constructor C
boundary B' : port p' hosts constructor C
move M      : (B, p) -> (B', p')
```

A too-strong reading (explicit vacatur required) wrongly excludes this.
Vacatur may be implicit in the move. MovedConstructorPort must HOLD here.

---

## Boundary questions

### B1 - OPEN: Destination port aliased back to source port

```text
boundary B  : port p  hosted constructor C
boundary B' : port p' hosts constructor C
move M      : (B, p) -> (B', p')
alias       : (B', p') resolves to (B, p)
```

If the destination port is aliased back to the source, did the constructor
port move? OPEN - needs an owner decision on whether alias-resolved identity
collapses the move.

---

## Instance registry

| id | digest |
|----|--------|
| P1 | 59b3835581b3 |
| P2 | 9ab4d08e1c6f |
| P3 | 92bfc3a503ba |
| N1 | 80cef63c387a |
| N2 | 762d194fa3a5 |
| N3 | e7e8769d3e16 |
| W-WEAK | d4bd04dd1b63 |
| W-STRONG | e7f0b4b5b598 |
| B1 | 15db59b249cd |
