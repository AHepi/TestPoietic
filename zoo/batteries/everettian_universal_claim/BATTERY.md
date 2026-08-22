# Battery: EverettianUniversalClaim

Term pin (negative constraint): the Everettian universal claim ("all branches of the universal wavefunction are real") must remain unavailable from finite data. The explanatory discussion does not turn other universes into observed data, and no finite cohort is exhaustive.

Fragment language sorts: U (universes/branches), D (data points), C (claims).
Fragment language relations:
- observed subseteq D x U -- data point observes universe
- universal_claim(c) -- c asserts every u in U is real
- licenses subseteq D x C -- data point licenses claim
- exhaustive subseteq D -- data set declared exhaustive over U
- discussed subseteq U -- universe appears in Everettian explanatory discussion
- addressable(c) -- claim can be reasoned about (discussed, addressed) without being licensed

### P1 - single-branch observations do not license the multi-branch universal claim

Sorts:
- U = {u1, u2, u3}
- D = {d1, d2}
- C = {c}

Relations:
- observed = {(d1, u1), (d2, u1)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {u2, u3}
- addressable(c) = true

Classification: POSITIVE. Finite data D = {d1, d2} only observes u1. Claim c asserts all of {u1, u2, u3} are real. The claim is not licensed. Branches u2, u3 appear in Everettian discussion but are not observed. The denial holds: the universal claim is unavailable from finite data.

### N1 - minimal pair with P1: finite cohort declared exhaustive

Sorts:
- U = {u1, u2, u3}
- D = {d1, d2}
- C = {c}

Relations:
- observed = {(d1, u1), (d2, u1)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {d1, d2}
- discussed = {u2, u3}
- addressable(c) = true

Single difference from P1: exhaustive = {d1, d2} (was {}).

Classification: NEAR-MISS. Identical to P1 except the finite cohort is now declared exhaustive over U. If accepted, this declaration would make the finite data cover all universes and license the universal claim. The denial must exclude this: declaring a finite cohort exhaustive does not make it so.

### P2 - explanatory discussion of other branches does not create observational data

Sorts:
- U = {u1, u2}
- D = {d1}
- C = {c}

Relations:
- observed = {(d1, u1)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {u2}
- addressable(c) = true

Classification: POSITIVE. Data d1 observes only u1. Branch u2 is discussed in the Everettian explanation (discussed = {u2}) but discussion is not observation. The universal claim is not licensed by finite data. The denial holds.

### N2 - minimal pair with P2: other branch turned into observed data

Sorts:
- U = {u1, u2}
- D = {d1}
- C = {c}

Relations:
- observed = {(d1, u1), (d1, u2)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {u2}
- addressable(c) = true

Single difference from P2: observed adds (d1, u2).

Classification: NEAR-MISS. Identical to P2 except u2 is now also observed by d1. This turns the other branch into observed data -- exactly the move the guard-rail forbids. The Everettian explanatory discussion does not turn other universes into observed data. The denial must exclude this.

### P3 - larger finite cohort still does not cover all branches

Sorts:
- U = {u1, u2, u3, u4, u5}
- D = {d1, d2, d3}
- C = {c}

Relations:
- observed = {(d1, u1), (d2, u2), (d3, u1)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {u3, u4, u5}
- addressable(c) = true

Classification: POSITIVE. Finite data D = {d1, d2, d3} observes u1 and u2 but not u3, u4, u5. The cohort is not exhaustive. The universal claim is not licensed. Even a larger finite cohort does not cover all branches. The denial holds.

### N3 - minimal pair with P3: finite data directly licenses the claim

Sorts:
- U = {u1, u2, u3, u4, u5}
- D = {d1, d2, d3}
- C = {c}

Relations:
- observed = {(d1, u1), (d2, u2), (d3, u1)}
- universal_claim(c) = true
- licenses = {(d1, c)}
- exhaustive = {}
- discussed = {u3, u4, u5}
- addressable(c) = true

Single difference from P3: licenses = {(d1, c)} (was {}).

Classification: NEAR-MISS. Identical to P3 except a finite data point d1 now directly licenses the universal claim. The denial must exclude this: finite data cannot license the universal claim, regardless of cohort size.

### N4 - TOO-WEAK wall: weak reading admits finite-data licensing via declared exhaustiveness

Sorts:
- U = {u1, u2}
- D = {d1}
- C = {c}

Relations:
- observed = {(d1, u1)}
- universal_claim(c) = true
- licenses = {(d1, c)}
- exhaustive = {d1}
- discussed = {u2}
- addressable(c) = true

Classification: WALL (too-weak). The finite data d1 observes only u1, yet the cohort is declared exhaustive (exhaustive = {d1}) and the claim is licensed (licenses = {(d1, c)}). The too-weak reading checks only whether every universe is directly observed; since it sees exhaustive declared, it treats the cohort as covering all U and admits this structure. But the denial must exclude it: declaring a single-observation cohort exhaustive and licensing the universal claim from it is precisely what the guard-rail forbids. The weak reading wrongly admits this.

### P4 - TOO-STRONG wall: strong reading excludes a legitimate addressable positive

Sorts:
- U = {u1, u2}
- D = {d1}
- C = {c}

Relations:
- observed = {(d1, u1)}
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {u1, u2}
- addressable(c) = true

Classification: WALL (too-strong). The claim c is genuinely unavailable from finite data (licenses = {}, exhaustive = {}). The Everettian framework discusses both branches (discussed = {u1, u2}) and the claim is addressable (addressable(c) = true) -- one can reason about it. The too-strong reading says the universal claim can never be addressed at all, so it excludes this structure because addressable(c) = true. But this is a legitimate positive: the claim is addressable yet still unavailable from finite data. The strong reading wrongly excludes it.

### B1 - OPEN boundary: infinite universe set with infinite exhaustive observation

Sorts:
- U = {u1, u2, u3, ...} (countably infinite)
- D = {d1, d2, d3, ...} (countably infinite)
- C = {c}

Relations:
- observed = {(d1, u1), (d2, u2), (d3, u3), ...} (each di observes ui)
- universal_claim(c) = true
- licenses = {}
- exhaustive = {}
- discussed = {}
- addressable(c) = true

OPEN QUESTION: The denial constrains only finite data -- "the claim must stay unavailable from finite data." Here both U and D are countably infinite, and every universe is observed by some data point. Is the universal claim licensed in this case? The denial is silent on infinite data. If infinite exhaustive observation licenses the claim, the denial is specifically a finitude constraint, not a universal unavailability constraint. If even infinite observation does not license the claim (e.g., because the universal claim is metaphysical, not empirical), then the denial is stronger than finitude-limited. This boundary is genuinely undecided.

## Registry

| id | kind | partner | digest |
|---|---|---|---|
| P1 | positive | - | 9a1d791ffd865c16 |
| N1 | near-miss | P1 | 93ece40b7d5a649b |
| P2 | positive | - | b1306da64d164a11 |
| N2 | near-miss | P2 | 833ca27bfc1f659b |
| P3 | positive | - | c244cfbc074e5cc5 |
| N3 | near-miss | P3 | 18606c83525f2de7 |
| N4 | near-miss | P1 | 8dc81ad07379a044 |
| P4 | positive | P2 | 2d1060fe9511e599 |
| B1 | boundary | - | e9beac85c61a808b |
