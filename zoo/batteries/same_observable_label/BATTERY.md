# Battery: SameObservableLabel

## Term

**SameObservableLabel(o1, o2)** - two observations bear the same observable label.

## Fragment language

Sorts: `Obs` (observations), `Label` (observable label strings), `Val` (measured values)

Functions:
- `labelOf : Obs -> Label`
- `valueOf : Obs -> Val`

Predicate under test: `SameObservableLabel(o1, o2)`

## Risk corridor (from terms inventory)

- **Too weak admits:** observations whose labels share a base concept but differ in unit qualifier (e.g. `temperature_C` vs `temperature_F`). These are *different* observables and must be excluded.
- **Too strong excludes:** observations whose labels are identical in local content but differ only in namespace prefix (e.g. `ns1:temp` vs `ns2:temp`). These are the *same* observable and must be included.

---

## Positive instances (must admit)

### P1 - identical label, identical value

```
Obs   = {o1, o2}
Label = {"temp"}
Val   = {23.0}
labelOf = {(o1,"temp"), (o2,"temp")}
valueOf = {(o1,23.0), (o2,23.0)}
```

SameObservableLabel(o1, o2) = **true**

### P2 - identical label, different values

```
Obs   = {o3, o4}
Label = {"pressure"}
Val   = {101.3, 99.8}
labelOf = {(o3,"pressure"), (o4,"pressure")}
valueOf = {(o3,101.3), (o4,99.8)}
```

SameObservableLabel(o3, o4) = **true**

### P3 - identical label, different measurement sessions

```
Obs   = {o5, o6}
Label = {"flow_rate"}
Val   = {4.2, 4.1}
labelOf = {(o5,"flow_rate"), (o6,"flow_rate")}
valueOf = {(o5,4.2), (o6,4.1)}
```

SameObservableLabel(o5, o6) = **true**

---

## Near-miss negatives (must exclude)

### N1 - minimal pair with P1: trailing character differs

```
Obs   = {o1, o7}
Label = {"temp", "temps"}
Val   = {23.0, 23.0}
labelOf = {(o1,"temp"), (o7,"temps")}
valueOf = {(o1,23.0), (o7,23.0)}
```

**Difference from P1:** label of second observation is `"temps"` instead of `"temp"` (extra trailing 's').

SameObservableLabel(o1, o7) = **false**

### N2 - minimal pair with P2: case differs

```
Obs   = {o3, o8}
Label = {"pressure", "Pressure"}
Val   = {101.3, 101.3}
labelOf = {(o3,"pressure"), (o8,"Pressure")}
valueOf = {(o3,101.3), (o8,101.3)}
```

**Difference from P2:** label of second observation is `"Pressure"` instead of `"pressure"` (capital 'P').

SameObservableLabel(o3, o8) = **false**

### N3 - minimal pair with P3: separator character differs

```
Obs   = {o5, o9}
Label = {"flow_rate", "flow-rate"}
Val   = {4.2, 4.2}
labelOf = {(o5,"flow_rate"), (o9,"flow-rate")}
valueOf = {(o5,4.2), (o9,4.2)}
```

**Difference from P3:** label of second observation is `"flow-rate"` instead of `"flow_rate"` (hyphen vs underscore).

SameObservableLabel(o5, o9) = **false**

---

## Risk corridor walls (mandatory)

### N4 - too-weak reading wrongly admits this

```
Obs   = {o12, o13}
Label = {"temperature_C", "temperature_F"}
Val   = {23.0, 73.4}
labelOf = {(o12,"temperature_C"), (o13,"temperature_F")}
valueOf = {(o12,23.0), (o13,73.4)}
```

**Why too-weak admits:** labels share base concept `temperature` but differ in unit qualifier (`_C` vs `_F`). A reading that compares only the base concept would wrongly return true.

**Correct classification:** SameObservableLabel(o12, o13) = **false**

### P4 - too-strong reading wrongly excludes this

```
Obs   = {o14, o15}
Label = {"ns1:temp", "ns2:temp"}
Val   = {23.0, 23.5}
labelOf = {(o14,"ns1:temp"), (o15,"ns2:temp")}
valueOf = {(o14,23.0), (o15,23.5)}
```

**Why too-strong excludes:** labels differ in namespace prefix (`ns1:` vs `ns2:`) but the local observable name `temp` is identical. A reading that requires full string equality including prefix would wrongly return false.

**Correct classification:** SameObservableLabel(o14, o15) = **true**

---

## Boundary case (OPEN)

### B1 - semantically equivalent labels, syntactically different

```
Obs   = {o10, o11}
Label = {"temperature", "temp"}
Val   = {23.0, 23.0}
labelOf = {(o10,"temperature"), (o11,"temp")}
valueOf = {(o10,23.0), (o11,23.0)}
```

**OPEN:** Does "same observable label" require exact string identity, or does it admit labels that are conventional abbreviations of the same observable? If the system maintains an alias table mapping `"temp"` -> `"temperature"`, these could be the same observable. Without such a table, they are distinct labels.

**Question to resolve:** Is SameObservableLabel defined over raw label strings, or over a canonicalized label equivalence class?

---

## Minimal-pair summary

| Positive | Negative | Single difference |
|----------|----------|-------------------|
| P1 | N1 | trailing 's' in label |
| P2 | N2 | capitalization of first letter |
| P3 | N3 | underscore vs hyphen separator |

---

## Registry

| id | kind | partner | digest |
|----|------|---------|--------|
| P1 | positive | N1 | 8851424d2e849204 |
| P2 | positive | N2 | 05d9a930a4e81e92 |
| P3 | positive | N3 | 56d66ed296949f3e |
| N1 | near-miss | P1 | b1ea656880378ff6 |
| N2 | near-miss | P2 | 51a10d90df463a42 |
| N3 | near-miss | P3 | 5759de906b47df62 |
| N4 | near-miss | - | d4b5f634fb74f295 |
| P4 | positive | - | b79fd7da428c2a49 |
| B1 | boundary | - | 5c3e0f002376b549 |
