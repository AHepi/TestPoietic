# Arbiter adjudication: PIN-SUB-V1
arbiter_model: deepseek-v4-pro:0813
date: 2026-08-21

ADJUDICATION:
- FINDING 1: CONFIRM — The record states “Section 12 lists SameSyntax and RealizationEq among the uninterpreted N-only leaves, and RealizationEq among the open load-bearing originals.” DSF-v1 Section 12’s “Uninterpreted N-only leaves” list includes “SameSyntax” but not “RealizationEq”; RealizationEq appears only in the separate “Also open and load-bearing” list. Thus the phrasing misattributes RealizationEq to the first list.
- FINDING 2: CONFIRM — Official header scope includes “feeding N-row N18 (NE_SUBSTRATE_SWAP_NOT_AUTOMATIC) and the K_REALIZATION_EQUIVALENCE certificate row…”, while the manifest scope says “feeding N-row N18 and the K_REALIZATION_EQUIVALENCE certificate row…”, omitting the parenthetical. RPS-v1 requires scope fields to agree.
- FINDING 3: CONFIRM — The official non_claims include “does not prove creativity or non-creativity”, but the manifest caveat_crosswalk has no row with that official_item_id or statement; the only non-claim row is PIN-SUB-NO-TEST about N18 do-not-test. RPS-v1 requires every non-claim to have a plain-language location.

SUMMARY: 3/3 confirmed; all three findings are accurate minor documentation mismatches.