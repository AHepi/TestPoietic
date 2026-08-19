# F1-AR-BOOL4-001 Preregistration Amendment 01

**Frozen before execution:** 2026-08-19, Australia/Brisbane  
**Reason:** remove an implementation ambiguity in the phrase “repeated SHA-256 blocks.”  
**Outcome access before amendment:** none; the experiment code had not been run.

For battery generation, let `seed` be the ASCII byte string `SPARK-F1-AR-BOOL4-001-BATTERY`. For counters `c = 0,1,2,...`, compute SHA-256 over `seed || b":" || ASCII_decimal(c)`. Read each 32-byte digest from left to right. Reduce each byte modulo 16, append an index only if it has not appeared before, and stop after eight distinct indices.

This amendment changes no domain, statistic, threshold, exclusion, or verdict rule.
