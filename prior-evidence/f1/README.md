# Spark–Poietic F1-AR-BOOL4-001 companion package

This package contains the first executed protocol associated with Spark–Poietic revision 1.3. Read `F1-AR-BOOL4-001-report.md` first. The frozen protocol is in the preregistration and two pre-execution amendments. `run_f1_ar_bool4_001.py` is the frozen execution program. `run-001/` contains the raw target table, summary, verdict, runtime record, and clean-process verification. `verify_f1_ar_bool4_001.py` independently recalculates every saved row. `verify_f1_ar_bool4_001_full_domain.py` separately re-enumerates the entire minimum-expression domain, checks that no target was omitted or added, and reproduces the verdict. `replay-comparison.txt` records the exact-hash match from a complete second execution.

The verdict is **REFUTED ON THIS DECLARED DOMAIN**. This package is an experimental criticism, not part of the theory’s premises and not a gate on later revisions.
