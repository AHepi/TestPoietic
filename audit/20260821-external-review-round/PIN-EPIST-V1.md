# Independent review: PIN-EPIST-V1
reviewer_model: mistral-large-3:675b
date: 2026-08-21

VERDICT: REVISE

FINDINGS:

- **[MAJOR] PIN_EPIST_V1.md, Section 4 (PIN-EPIST-D7 / Confirmed):**
  The record claims to pin Confirmed via an acceptance axiom (PIN-EPIST-A1) that restates calculus (30) as a "negative guard-rail". However, the quoted anchor document (calculus (30)) explicitly states:
  > `CritPkg_η(χ) ∧ C_SURV ⊭ Confirmed(A⁻_χ). [𝖭]`
  This is a **non-implication obligation**, not a prohibition on deriving `Confirmed` from `C_SURV`. The record's PIN-EPIST-A1 ("no survived attempt or finite audit entails `Confirmed`") **overclaims** by converting a non-entailment into a universal prohibition. The anchor does not forbid a certificate from *declaring* `Confirmed` independently of `C_SURV`; it only blocks deriving it from `C_SURV`. This violates **Rule 3 (classification discipline)** and **Rule 5 (status discipline)**.

  Evidence:
  - Anchor: `PIECEMEAL_PREMISE_CALCULUS.md`, line 1050 (calculus (30)).
  - Record: `PIN_EPIST_V1.md`, Section 4 (PIN-EPIST-D7) and Section 5 (N14 check).

- **[MAJOR] PIN_EPIST_V1.md, Section 5 (N14 check):**
  The record claims that PIN-EPIST-A1 "GUARANTEES the denial limb survives any survival". This is **structurally unsound** per the above. The anchor only blocks deriving `Confirmed` from `C_SURV`; it does not block a certificate from declaring `Confirmed` independently (e.g., via a separate oracle). The two-sided check for N14 is thus **invalid**, as the "M-conf" case (adding `Confirmed` independently) is not prohibited by the anchor. This violates **Rule 4 (non-deciding claims)**.

- **[MINOR] PIN_EPIST_V1.md, Section 2 (anchors):**
  The record transcribes N-rows and calculus (30) in "display form" but does not use verbatim byte quotes. While the transcriptions appear accurate, this violates **Rule 2 (verbatim-anchor accuracy)**. The record should either:
  - Use exact byte quotes (preferred), or
  - Explicitly label transcriptions as "display-form paraphrases" and justify their fidelity.

  Evidence:
  - Record: "transcribed from math form" (Section 2).
  - Anchor: Exact byte sequences in `PIECEMEAL_PREMISE_CALCULUS.md` (e.g., calculus (30)).

- **[MINOR] PIN_EPIST_V1_PLAIN_LANGUAGE.md:**
  The plain-language version omits the **critical limitation** that PIN-EPIST-A1 is an overclaim (it converts a non-implication into a prohibition). This violates **Rule 6 (companion faithfulness)**. The plain-language file must retain the caveat that the "negative guard-rail" is **stronger than the anchor permits**.

  Evidence:
  - Official record: Section 4 (PIN-EPIST-D7) and Section 5 (N14 check).
  - Plain-language: No mention of the overclaim.

- **[MINOR] PIN_EPIST_V1_FREEZE.json:**
  The `verification.notes` field claims "SPA-v1 parent digest pinned per ERR-SPA-v1 to a9f62ebb...". However, the record header lists `PIECEMEAL_SEMANTIC_ANNEX_V1.md` with SHA `a9f62ebb...` directly, not via an erratum. This is **internally inconsistent** and violates **Rule 8 (hash/digest consistency)**.

---

NOTES:
1. **Primary attack vector**: The Confirmed pin (PIN-EPIST-D7/A1) is the most severe issue. It misrepresents a non-entailment obligation as a prohibition, which could silently pre-decide N14's truth value (violating **Rule 7 (steering check)**). The two-sided check for N14 is structurally unsound as a result.
2. **Held strong**: The CreativeGenerator/CreativeCap independence requirement (PIN-EPIST-D8) and the declared-space reading of NoPossibleCritic (PIN-EPIST-D9) are well-justified by the anchor rows (N9 and N16). The Artifact ambiguity (PIN-EPIST-OPEN-2) is correctly flagged as unresolved.
3. **Verification block**: The record's `verification.independent_mathematical_review` field discloses "NONE AVAILABLE", which is acceptable but should trigger heightened scrutiny of the orchestrator's claims. The Confirmed overclaim slipped through this gap.