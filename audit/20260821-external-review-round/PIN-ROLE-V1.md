# Independent review: PIN-ROLE-V1
reviewer_model: kimi-k2.6
date: 2026-08-21

VERDICT: REVISE

FINDINGS:
- [MAJOR] PIN_ROLE_V1_PLAIN_LANGUAGE.md / caveat_crosswalk: The plain-language section "What did NOT change" omits two material non-claims from the official PIN_ROLE_V1.md Section 8 forbidden items: (i) "does not identify any original predicate with an F-prefixed fragment predicate" and (ii) "does not prove creativity or non-creativity". The caveat crosswalk marks PIN-ROLE-FORBIDDEN as checked in that section, but those limitations are not retained there. Per RPS-v1, a plain-language version must not remove a limitation, and the crosswalk must accurately reflect retention.

NOTES: I attacked companion faithfulness and the crosswalk hardest, finding that the plain-language file drops two explicit scope limitations while the freeze manifest falsely certifies them as retained. The non-deciding sketches (M-hi/M-lo, M-one/M-fam, M-ret/M-noret) are structurally sound: the proposed definitions leave each row antecedent satisfiable and falsifiable without rigging. Status discipline held—the record correctly preserves DSF-v1 readiness counts and does not overclaim under DRAFT_PENDING_REVIEW.