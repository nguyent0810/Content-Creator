# QA Report — KP_CL_001_Luat_Hinh_Su.md

**Reviewer:** Independent QA pass (fresh review, not the authoring context), per `DOMAIN_QA/DOMAIN_QA_POLICY.md` Process section.
**Date:** 2026-07-23
**Scope:** Full read of `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `KNOWLEDGE_PACKETS/KP_CL_001_Luat_Hinh_Su.md` (586 lines, full text), `SOURCES/RESEARCH_DRAFT_LUAT_HINH_SU.md` (full text), `GLOSSARY/DOMAIN_GLOSSARY.md`, and `SOURCES/SOURCE_REGISTRY.md`. Every numeric/factual claim in KP_CL_001 was cross-checked line-by-line against the corresponding claim in the research draft.

**Overall verdict: PASS, with 3 advisory fixes applied. No blocking issue found.**

This packet is unusually disciplined. Every sentencing bracket, confidence label, and "gap/unverified" flag in the research draft survived into the Knowledge Packet without being upgraded into a stated-as-fact claim. The one specific item the review brief asked me to re-verify by name — the Điều 141 "05–10 năm cho bị hại 16–18 tuổi" bracket anomaly — is still correctly flagged as unverified/do-not-use in four separate places in the packet (§3.3 body, the Phần 5 table, the Phần 5 production cautions, and the Retrieval Warnings), never presented as settled.

---

## (a) Checklist items checked and passed

| Check | Result |
|---|---|
| CL-QA-001 (legal-status precision) | **Pass.** Packet is abstract legal-education content with no real persons named; it correctly requires bị tình nghi/bị can/bị cáo language even for hypothetical/general discussion (Rule 1, §4 production cautions throughout). |
| CL-QA-002 (net-impression) | **Pass.** No case narrative exists in this packet to fail the test on; suggested hooks/titles (e.g. §6.6's "Tòa đã tuyên án — vậy đã được gọi là 'tội phạm' chưa?") are neutral questions, not guilt-implying titles. Rule 6 explicitly codifies the requirement for downstream scripts. |
| CL-QA-003 (source-backed identification, Format 2/3) | **N/A / Pass.** No suspect or organization is named in this packet. |
| CL-QA-004 (theory completeness) | **N/A / Pass.** Not an unsolved-case asset. |
| CL-QA-005 (victim privacy) | **Pass.** Điều 141/142 (rape/child rape) content stays at legal-definition altitude only, no graphic behavioral detail, no real victims. Rule 5 codifies this explicitly for downstream scripts. |
| CL-QA-006 (no legal advice) | **Pass.** I specifically grepped every second-person ("bạn") passage in the file (13 hits) — every one is either a rhetorical hook or an explicit **Forbidden**-language example warning against advice; none is itself an instance of directed advice. Every knowledge block carries its own §7 production-caution reminder. |
| CL-QA-007 (organized-crime non-glorification) | **N/A / Pass.** No organized-crime content in this packet (Pillar 5 material). |
| CL-QA-008 (anti-sensationalism) | **Pass.** No shock-title language; Rule 7 explicitly bans it for downstream use. |
| CL-QA-009 (layered interpretation) | **Pass.** Production cautions correctly separate legal/procedural fact from societal-reflective commentary (e.g. §3's caution on án tử hình/án treo: state the sentence, don't editorialize on its justice at the legal layer). |
| CL-QA-010 (jurisdiction clarity) | **Pass.** Jurisdiction (Vietnam, BLHS 2015/sửa đổi 2017 + BLTTHS 2015) is stated up front and repeated at multiple structural points. The Miranda/"quyền im lặng" foreign-concept risk is the single most-repeated caution in the whole packet (§2 recap, Block 4, Mythbust 6.4, Rule 4) and is handled correctly every time: never claimed to exist in Vietnam, always given the correct analogous principle (nguyên tắc suy đoán vô tội + Điều 60/61) instead. |
| CL-QA-011 (terminology consistency) | **Advisory issue found and fixed** — see (b)/(c) below. |
| CL-QA-012 (forbidden claims, §12) | **Pass.** No premature-guilt language, no directed advice, no operational crime/evasion detail (the money-laundering/drug-trafficking/bribery entries in the 13-crime table stay at legal-definition altitude, not mechanism-level how-to), no minor-victim identification, no unsolved-case-as-settled framing, no shock framing, no glamorization. |

## Source-fidelity check (the review's primary focus)

I compared every one of the 13 crime-category brackets, all sentencing-system facts (Điều 32/39/40/65/22), the age-of-responsibility rule (Điều 12), the aggravating/mitigating framework (Điều 51/52), the 8-stage procedure, and the rights-of-the-accused block against the research draft sentence-by-sentence. Result: **no hedge was dropped, no "single-sourced/trung bình/thấp/chưa xác minh" label was silently upgraded to a stated-as-fact claim.** Specifically re-verified per the review brief:

- **Điều 141 bracket anomaly:** still flagged "không dùng chi tiết này cho đến khi xác minh lại" in the Knowledge Packet, in every location the research draft flagged it. Not silently settled anywhere.
- **Điều 251 (ma túy) 01/07/2025 effective-date gap:** still flagged as unresolved (statutory amendment vs. implementing-guidance date) in the Khoảng trống nguồn list, the Phần 5 table, and Retrieval Warnings.
- **Điều 168/134/169/175 mid-tier brackets, Điều 12 khoản 2 article list, the 20-day tin báo window, Điều 60/61 article numbers, the 15/30-day kháng cáo/kháng nghị windows, the death-penalty-to-life-sentence commutation mechanism, and the Part-2 article-count arithmetic quirk:** all 10 items from the research draft's own gap list (Phần 5, mục 2) are individually reproduced in the Knowledge Packet's "Khoảng trống nguồn" section with the same hedge strength, none upgraded.

## (b) Issues found

1. **(Advisory, CL-QA-011)** The packet's front matter claims it "không đề xuất thuật ngữ mới nào chưa có trong glossary" (proposes no new terminology not already in the glossary), but Block 4 builds an entire concept around **"Người bị buộc tội"** (Điều 4 BLTTHS — the umbrella term covering người bị bắt/tạm giữ/bị can/bị cáo) as a foundational term, and that term was not actually present in `GLOSSARY/DOMAIN_GLOSSARY.md` (nor in `DOMAIN_GUIDE.md` §11's core-term list). This is exactly the kind of term §11 requires be registered before use, since it sits inside this domain's single highest-risk vocabulary area (legal-status precision).

2. **(Advisory, precision/confidence-tiering accuracy)** In two places (the front-matter `source_lineage` field and the "Canonical Sources" table), the packet stated the overall legal-framework claims were cross-verified via "**≥3 nguồn độc lập mỗi mục**" as a blanket figure covering the sentencing system (Điều 32/39/40/65) along with everything else. The research draft's own §1.5 confidence note for that specific section states the sentencing-system points were each confirmed via "**≥2 nguồn độc lập**," not ≥3. This is a small but real instance of the packet's own summary metadata rounding a source's stated confidence upward — precisely the failure mode the review brief asked me to hunt for, even though it did not appear anywhere in the substantive body text (every in-body confidence label I checked was accurate).

3. **(Process/cross-file finding, not a defect in KP_CL_001 itself)** `SOURCES/SOURCE_REGISTRY.md` had not been updated to reflect that `RESEARCH_DRAFT_LUAT_HINH_SU.md` (dated 2026-07-23, the same date as this packet) exists. Its "Canonical Legal Text (Pillar 1)" section still read "Not yet added as a research draft; required before any Pillar 1 Knowledge Packet is written," and its "Known Gaps" section still listed "Pillars 1, 4, and 5 have not had a dedicated research pass yet" — both contradicted by the fact that KP_CL_001 (built on that research draft) now exists. This is a registry-maintenance gap, not a claim-accuracy problem inside KP_CL_001, but it directly affects whether a future agent correctly locates and re-uses Pillar 1's existing research instead of duplicating it.

No blocking (CL-QA-001/002/003/005/006/007/008/012) issue was found anywhere in the packet.

## (c) Exact fixes applied

### Fix 1 — Glossary gap for "Người bị buộc tội" (CL-QA-011)

File: `DOMAINS/CRIMINAL_LAW/GLOSSARY/DOMAIN_GLOSSARY.md`

**Before:** No entry existed for "Người bị buộc tội" anywhere in the glossary.

**After** (new entry added to Section A, immediately after "Bị hại"):
> **Người bị buộc tội (person accused)** — The umbrella term (Điều 4, Bộ luật Tố tụng Hình sự 2015) covering everyone from a person just arrested (người bị bắt) through người bị tạm giữ, bị can, and bị cáo. *Rule:* same presumption-of-innocence requirement as its narrower sub-terms; used when explaining rights/principles that apply across all these stages at once (e.g., nguyên tắc suy đoán vô tội, quyền bào chữa) — added per `DOMAIN_GUIDE.md` §11's extension workflow when `KNOWLEDGE_PACKETS/KP_CL_001_Luat_Hinh_Su.md` made this term foundational to Pillar 1.

This closes the gap between the packet's front-matter claim of full glossary compliance and its actual content, and gives the term the same rule-bound treatment as its sub-terms per §11's extension workflow.

### Fix 2 — Confidence-count overstatement in front matter (`source_lineage`)

File: `DOMAINS/CRIMINAL_LAW/KNOWLEDGE_PACKETS/KP_CL_001_Luat_Hinh_Su.md`, line 34

**Before:**
> ...Độ tin cậy cao cho khung pháp lý tổng thể (cấu trúc BLHS, phân loại Điều 9, hệ thống hình phạt, quy trình tố tụng tổng quát, nguyên tắc suy đoán vô tội) — xác minh chéo ≥3 nguồn độc lập mỗi mục.

**After:**
> ...Độ tin cậy cao cho khung pháp lý tổng thể (cấu trúc BLHS, phân loại Điều 9, hệ thống hình phạt, quy trình tố tụng tổng quát, nguyên tắc suy đoán vô tội) — xác minh chéo ≥2-3 nguồn độc lập tùy mục (theo đúng số nguồn research draft tự ghi nhận cho từng mục cụ thể, không làm tròn lên thành một con số duy nhất).

### Fix 3 — Same overstatement in the "Canonical Sources" table

File: same, line 100

**Before:**
> Tier 1 cho khung pháp lý tổng thể (cấu trúc luật, Điều 9, hệ thống hình phạt, nguyên tắc suy đoán vô tội — xác minh ≥3 nguồn độc lập); Tier 3-tương-đương...

**After:**
> Tier 1 cho khung pháp lý tổng thể (cấu trúc luật, Điều 9, quy trình tố tụng, nguyên tắc suy đoán vô tội — xác minh ≥3 nguồn độc lập; riêng hệ thống hình phạt/Điều 65/39/40 ở mục 1.5 research draft tự ghi nhận ≥2 nguồn độc lập mỗi điểm, không phải ≥3 — giữ đúng mức này); Tier 3-tương-đương...

### Fix 4 — Cross-file registry staleness (SOURCE_REGISTRY.md)

File: `DOMAINS/CRIMINAL_LAW/SOURCES/SOURCE_REGISTRY.md`

- Added a full table row for `RESEARCH_DRAFT_LUAT_HINH_SU.md` under "Research draft entries," matching the format of the existing Pillar 2/3 rows (topics covered, sources cross-referenced, and a notes column that reproduces the tier-1-primary-text gap and the ≥2-vs-≥3-sources nuance from Fix 2/3 above).
- Updated "Canonical Legal Text (Pillar 1 — Luật Hình Sự)" from "Not yet added as a research draft; required before any Pillar 1 Knowledge Packet is written" to reflect that the research draft and `KP_CL_001` now exist, while preserving the still-true fact that neither has directly verified the primary statutory text at vbpl.vn.
- Updated "Known Gaps" from "Pillars 1, 4, and 5 have not had a dedicated research pass yet" to "Pillars 4 and 5 have not had a dedicated research pass yet," and added an explicit gap entry for Pillar 1's still-open tier-1-primary-text verification need.

This is not a change to KP_CL_001 itself — it is a supporting-file correction so the domain's own source-tracking file stops contradicting a fact the reviewed packet establishes. Flagging it seemed more useful to the domain than leaving it silently stale.

## (d) Issues not fixed / requiring human judgment

None found that rise to "cannot be fixed by an editor" — every issue identified above had a direct, in-scope transform and was applied. Two items are worth a human's attention going forward, not because the packet is unsafe, but because they are the packet's own stated precondition for use:

1. **The packet is explicitly `status: draft-pending-human-review` and `QA_status: draft`,** and this review does not substitute for the packet's own required Legal QA ("nếu có luật sư/cố vấn pháp lý cộng tác trước khi phát hành"). Nothing in this review should be read as clearing that requirement — it only confirms the packet does not currently contain a blocking safety-boundary violation and faithfully preserves its source's hedges.
2. **The single largest substantive gap is structural, not a QA defect:** neither the research draft nor this packet has directly read the primary statutory text at vbpl.vn for any article cited. This is called out repeatedly and correctly by the packet itself (never hidden), but it means no sentencing-bracket figure in Phần 5 should be locked into a production script without the direct vbpl.vn/thuvienphapluat.vn cross-check the packet already recommends. This is a research-completeness question for a human/future research pass to close, not something a QA rewrite can fix in place.
