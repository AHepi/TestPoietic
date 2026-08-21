# Battery: MovedConstructorPort

**Term:** MovedConstructorPort (inventory section 2, N7 row, D12 family)

**Intended meaning:** A structural configuration in which a constructor C,
originally hosted at port P_from, has been relocated to a different port
P_to (P_from != P_to), such that (i) C is now hosted at P_to, (ii) P_from
no longer hosts C, and (iii) an explicit move relation records the
relocation from P_from to P_to. The moved entity must be a constructor,
not a plain value or arbitrary function.

---

## Positive instances

### P1 - Simple move with explicit vacatur

```
sorts: Port = {p0, p1}; Constructor = {mk_A}
is_constructor: {mk_A}
hosts: {(p1, mk_A)}
moved: {(mk_A, p0, p1)}
vacated: {p0}
```

### P2 - Move with redirect from old port

```
sorts: Port = {q0, q2}; Constructor = {init_B}
is_constructor: {init_B}
hosts: {(q2, init_B)}
moved: {(init_B, q0, q2)}
vacated: {q0}
redirects: {(q0, q2)}
```

### P3 - Move with provenance record of origin

```
sorts: Port = {r1, r3}; Constructor = {build_C}
is_constructor: {build_C}
hosts: {(r3, build_C)}
moved: {(build_C, r1, r3)}
vacated: {r1}
provenance: {(build_C, r1)}
```

---

## Near-miss negatives (minimal pairs)

### N1 - Copy, not move (pair with P1)

```
sorts: Port = {p0, p1}; Constructor = {mk_A}
is_constructor: {mk_A}
hosts: {(p0, mk_A), (p1, mk_A)}
moved: {(mk_A, p0, p1)}
vacated: {}
```

**Single difference from P1:** `hosts(p0, mk_A)` is present and `vacated(p0)` is absent - the source port retains the constructor, so this is a copy, not a move.

### N2 - Different constructor at destination (pair with P2)

```
sorts: Port = {q0, q2}; Constructor = {init_B, init_B_prime}
is_constructor: {init_B, init_B_prime}
hosts: {(q2, init_B_prime)}
moved: {(init_B, q0, q2)}
vacated: {q0}
redirects: {(q0, q2)}
```

**Single difference from P2:** `hosts(q2, init_B_prime)` replaces `hosts(q2, init_B)` - the constructor at the destination is not the one recorded as moved.

### N3 - No move relation linking source and destination (pair with P3)

```
sorts: Port = {r1, r3}; Constructor = {build_C}
is_constructor: {build_C}
hosts: {(r3, build_C)}
moved: {}
vacated: {r1}
provenance: {(build_C, r1)}
```

**Single difference from P3:** `moved(build_C, r1, r3)` is absent - the constructor appears at r3 and r1 is vacated, but no explicit move relation connects them.

---

## Corridor walls

### W-WEAK - Too-weak reading wrongly admits: non-constructor moved between ports

```
sorts: Port = {s0, s1}; Constructor = {}; Value = {val_X}
is_constructor: {}
is_value: {val_X}
hosts: {(s1, val_X)}
moved: {(val_X, s0, s1)}
vacated: {s0}
```

**Why the too-weak reading admits it:** The weak reading only checks "something moved from one port to another with vacatur" and ignores the constructor requirement. `val_X` is a plain value, not a constructor, so the intended meaning must exclude this.

### W-STRONG - Too-strong reading wrongly excludes: implicit vacatur (no explicit vacated relation)

```
sorts: Port = {t0, t1}; Constructor = {mk_D}
is_constructor: {mk_D}
hosts: {(t1, mk_D)}
moved: {(mk_D, t0, t1)}
vacated: {}
```

**Why the too-strong reading excludes it:** The strong reading requires an explicit `vacated(t0)` relation. Here `hosts(t0, mk_D)` is absent, so t0 is implicitly vacated, but no explicit vacated relation is recorded. The intended meaning should admit this because the constructor is genuinely gone from t0.

---

## Boundary case

### B1 - OPEN: Destination port aliased back to source port

```
sorts: Port = {u0, u1}; Constructor = {mk_E}
is_constructor: {mk_E}
hosts: {(u1, mk_E)}
moved: {(mk_E, u0, u1)}
vacated: {u0}
alias: {(u0, u1)}
```

**Question:** If the destination port u1 is aliased back to the source port u0, does the move collapse to a no-op (the constructor is effectively still at the same logical port), or does the physical relocation to u1 still constitute a genuine MovedConstructorPort? The aliasing relation makes u0 and u1 referentially equivalent, but the `moved` and `hosts` relations distinguish them as distinct ports.

---

## Instance registry

| id | digest |
|----|--------|
| P1 | 2aef486d3494 |
| P2 | d9f075e5363a |
| P3 | 11e68ce004c3 |
| N1 | a80b0264b036 |
| N2 | c0de96c9fa2e |
| N3 | 756994d89d04 |
| W-WEAK | 929652f0415e |
| W-STRONG | 58b0d18b6dac |
| B1 | 6098f4792066 |
