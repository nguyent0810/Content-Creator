# QA Report — KP_CL_002_An_Da_Xu.md

**Reviewer:** Independent QA pass (fresh review, did not author the packet)
**Date:** 2026-07-23
**Domain:** CRIMINAL_LAW (Hình Sự) — `risk_level: critical`
**Documents read in full before review:** `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `KNOWLEDGE_PACKETS/KP_CL_002_An_Da_Xu.md`, `SOURCES/RESEARCH_DRAFT_AN_DA_XU.md`. Cross-checked against `GLOSSARY/DOMAIN_GLOSSARY.md`, `SOURCES/SOURCE_REGISTRY.md`, and the sibling packet `KP_CL_004_Chan_Dung_Sat_Nhan.md` (to understand the prior minor-naming violation pattern this review was asked to check against with extra suspicion).

## Verdict: PASS — no blocking issues found

This is unusual for a first independent QA pass on a critical-risk asset, so the review was deliberately adversarial: every claim in the packet was traced back to the research draft, and the four flagged risk areas were checked against the raw prose, not just the "Production cautions" bullets. No fixes were required or applied to the packet file itself.

---

## (a) Checklist items that passed

Mapped to `DOMAIN_QA_POLICY.md`'s CL-QA-001 through CL-QA-012:

| Check | Result | Evidence |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | All four cases correctly use Format 1 (finally-convicted) factual language. Năm Cam: stated as executed 3/6/2004, not "accused." Lê Văn Luyện: stated as convicted (18 years, final). Cát Tường: Nguyễn Mạnh Tường and Đào Quang Khánh both stated as finally convicted. O.J. Simpson: correctly stated as criminally acquitted (never "guilty," never "hung thủ") and separately as civilly liable. |
| CL-QA-002 (net-impression test) | PASS, verified against actual prose not just cautions | See item 2 below — checked sentence-by-sentence. |
| CL-QA-003 (Format 2/3 source-backed ID) | N/A | No unsolved-case suspect-naming or Format-2/3 content in this packet; all four cases are Format 1. |
| CL-QA-004 (theory completeness) | N/A | No unsolved-case theories in this packet. |
| CL-QA-005 (victim privacy/dignity) | PASS | See item 1 below. No addresses/contact info anywhere; adult victim Lê Thị Thanh Huyền named only because research confirms she is a publicly self-identified adult victim (permitted under §6); no graphic/exploitative dramatization of any death. |
| CL-QA-006 (no legal advice) | PASS | Entire packet is descriptive/historical/comparative-law; no line tells a viewer what to do about their own situation. |
| CL-QA-007 (organized-crime non-glorification) | PASS | See item 3 below. |
| CL-QA-008 (anti-sensationalism) | PASS | No manufactured-shock language, no gore, no countdown-of-horror framing. Clinical, factual register throughout (e.g., Cát Tường's death and body-disposal are stated factually, not sensationally). |
| CL-QA-009 (layered interpretation intact) | PASS | Every case carries legal/narrative/societal-reflective layers (e.g., Lê Văn Luyện's juvenile-sentencing debate presents both sides; Năm Cam's state-corruption angle; O.J.'s comparative-law layer). |
| CL-QA-010 (jurisdiction clarity) | PASS | O.J. Simpson section explicitly and repeatedly flags US/California jurisdiction, jury trial, "double jeopardy" as a foreign concept not to be equated with Vietnamese procedure. |
| CL-QA-011 (terminology consistency) | PASS | Terms used (bị cáo, bản án có hiệu lực pháp luật, kháng cáo, giám đốc thẩm/tái thẩm, etc.) match `DOMAIN_GLOSSARY.md`; no invented terminology. |
| CL-QA-012 (forbidden claims, §12) | PASS | No item in §12's never-use list is present anywhere in the packet. |

Additional independent verification performed (per QA Policy's instruction to re-verify citations, not just check they exist): cross-checked every date, sentence figure, and case-status claim in KP_CL_002 against `RESEARCH_DRAFT_AN_DA_XU.md` line-by-line. No fabricated fact, invented quote, or upgraded-confidence claim was found — every number (155 bị can/24 tội danh, 140 ngày xét xử, 18 năm tù, 19 năm tù, 33,5 triệu USD, etc.) traces directly to the research draft's stated confidence level, unchanged.

---

## (b) Issues found / (c) fixes applied

**None. No blocking or non-blocking issues were found requiring a fix to the packet file.**

Detail on the four specifically-flagged risk areas, checked with the requested extra suspicion:

### 1. Lê Văn Luyện section — minor victim naming (checked with real suspicion, not a skim)

Read every sentence referencing the two minor victims across all five subsections (Primary concepts, Narrative detail, Script-ready material, Production cautions, and the whole-document §6 note at the top). Confirmed:
- The infant victim is referred to only as "con gái út của họ (khoảng 18 tháng tuổi)" / "cháu bé út khoảng 18 tháng tuổi" — age and family role only, never a name.
- The surviving injured child is referred to only as "một người con gái khác của gia đình (khoảng 8 tuổi)" / "cháu bé khoảng 8 tuổi bị thương" — age and family role only, never a name.
- No partial names, initials, school, or other identifying detail appears anywhere for either child, in any of the four case sections or the editor's summary notes.
- The packet explicitly states (and follows through on) the rule that this holds even though the children's names were reportedly public in 2011 press coverage — this is the correct, stricter-than-source-record application of §6's no-exception rule.
- As a bonus check: the two adult parent-victims (chủ tiệm and vợ) are also left unnamed throughout, even though naming adult victims within public-record bounds is normally permitted under §6. This is more conservative than required — not a violation, just a stricter editorial choice than strictly necessary. Noted for (d) below as something the writer may want revisited (not a QA problem either way).

**No violation found. No fix needed.** This is a clean pass, distinct from the KP_CL_004 case where names had been present and had to be removed.

### 2. O.J. Simpson section — net-impression test checked against the actual narrative prose

Re-read the full "Narrative detail," "Primary concepts," and "Script-ready material" prose (not just "Production cautions") sentence by sentence for any blending of the criminal acquittal and civil liability into a single guilt conclusion. Confirmed:
- Every paragraph that states the civil-liability outcome is immediately and explicitly qualified as civil-standard ("chịu trách nhiệm dân sự," "preponderance of the evidence," "trong khuôn khổ phán quyết dân sự") in the same breath, not deferred to a separate caution paragraph.
- The single riskiest quote in the whole packet — the civil appellate court's language that the jury "in effect found that Simpson committed two deliberate, vicious murders" — is never presented standalone; every occurrence (Primary concepts and Production cautions) is immediately wrapped in "đây là nhận định trong khuôn khổ phán quyết dân sự, không phải một bản án hình sự."
- No sentence anywhere states or implies "Simpson đã giết người" or "Simpson là hung thủ" as the packet's own conclusion — those exact phrases appear only inside an explicit prohibition ("không được nói hoặc ngụ ý...").
- The "Trạng thái pháp lý kép" paragraph is a model of the required discipline: it explicitly says the historical/deceased-perpetrator exception in §4 does not apply here because there is no final *conviction* (only an acquittal), and states the two-track outcome must be preserved "không đơn giản hóa theo hướng nào."

**One advisory-level observation (not blocking):** the Script-ready material line "giải thích vì sao trắng án không đồng nghĩa 'vô tội tuyệt đối' theo mọi nghĩa pháp lý" is legally accurate (acquittal = reasonable-doubt standard not met, not a formal declaration of innocence) and is standard comparative-law content, but it is the single phrase in this packet closest to the net-impression line. It is correctly framed as an explanation of legal standards, not a guilt claim, so it passes as written — but flagging it explicitly here so a future scriptwriter handles it with the same care the packet itself models, rather than compressing it into something that reads as "so he's actually guilty."

**No violation found. No fix needed.**

### 3. Năm Cam section — operational/glorifying detail (§8) and legal-status language

- **Legal status:** Confirmed the packet correctly states Năm Cam was finally convicted (bản án có hiệu lực from 30/10/2003) and executed (thi hành án 3/6/2004) — stated as settled historical fact under Format 1, never downgraded to "bị cáo" or "accused" language anywhere in the packet.
- **Operational/glorifying detail:** Checked the "Cấu trúc tổ chức" content that made it into KP_CL_002 against the (deeper) version in the research draft. Confirmed the packet deliberately did *not* carry over the research draft's more granular organizational detail (e.g., the draft's specific ~$3,000 bribe figure to Phạm Sỹ Chiến, the four-tier operational breakdown) — it explicitly defers that depth to the future `KP_CL_005` organized-crime packet. What remains in KP_CL_002 is historical/consequence-framed narrative (arrest, trial, execution) with no laundering mechanics, no specific bribery/extortion technique, and explicit "Production cautions" language forbidding "cool"/admirable framing.

**No violation found. No fix needed.**

### 4. Cát Tường section — flagged single-sourced details still marked as such

Checked whether Đào Quang Khánh's sentence breakdown (24 + 9 = 33 months) and the exact/early-release-date details had been silently upgraded to settled fact anywhere in the packet's Primary concepts or Narrative detail sections. Confirmed:
- Primary concepts states the total (33 tháng) as fact but explicitly defers the charge-by-charge breakdown with "xem lưu ý độ tin cậy bên dưới" rather than asserting the 24/9 split as settled.
- Production cautions repeats the single-sourced flag clearly: "chỉ được xác nhận qua 1-2 nguồn báo chí (single-sourced/lower-confidence theo `DOMAIN_GUIDE.md` §3)," with an explicit instruction not to state the breakdown as fact without further verification.
- The "ra tù trước hạn (khoảng 2017)" detail does not even appear in Primary Concepts/Narrative detail — it exists only inside the Production-cautions hedge, which is more conservative than the research draft required.
- The Lê Văn Luyện appellate date ("30/3") is likewise correctly kept out of Primary Concepts and confined to a hedged Production-cautions note, matching the research draft's own confidence label.

**No violation found. No fix needed.**

---

## (d) Anything unfixable / requiring human judgment

1. **Not a defect, but worth flagging to a human editor:** the packet chose to anonymize the two adult parent-victims in the Lê Văn Luyện case (no names given) even though §6 would permit naming adult victims within public-record bounds. This is a legitimate editorial choice (more protective than the floor requires), but if a future scriptwriter wants to restore the adults' names for narrative specificity, that would require a fresh public-record check — not something this QA pass can authorize or perform.
2. **The O.J. Simpson "acquittal ≠ absolute innocence" phrasing** (see item 2 above) is correct as written but is the packet's highest-risk single sentence for downstream drift. Recommend any script derived from this packet keep that sentence's exact qualification intact rather than paraphrasing it looser.
3. This QA pass reviewed the Knowledge Packet only, not a produced script. Per the packet's own status field, a full Domain QA / Research QA / Safety QA / Legal-accuracy QA / Brand QA cycle is still required before any script derived from this packet is published — this report satisfies the Domain QA (Hình Sự) pass specifically, not the other listed required-QA gates.
4. No Tier-1 primary source (an actual bản án/verdict document) was directly consulted by this reviewer or by the underlying research draft for any of the four cases — all confidence labels rely on Tier 1-2 journalism reporting on official records, not the records themselves. This is already correctly disclosed in the packet and registry; flagging only as a standing gap for whoever eventually sources original court documents.
