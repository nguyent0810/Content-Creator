# QA Report: KP_CL_005 — Tổ Chức Tội Phạm

**Reviewer role:** Independent QA (fresh-eyes, did not author this packet), per `DOMAIN_QA/DOMAIN_QA_POLICY.md` Process section.
**Date:** 2026-07-23
**Files read in full:** `DOMAIN_GUIDE.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `KNOWLEDGE_PACKETS/KP_CL_005_To_Chuc_Toi_Pham.md`, `SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md`, `KNOWLEDGE_PACKETS/KP_CL_002_An_Da_Xu.md`, `GLOSSARY/DOMAIN_GLOSSARY.md` (for legal-status term precision).

**Overall verdict: PASS**, with one governance/documentation defect found and fixed (stale cross-reference status text), and two items flagged for human judgment (not blocking). No operational-detail, glamorization, insignia, or defamation-boundary violation was found anywhere in the packet — this is the highest-severity check for this domain (§8 / CL-QA-007) and it holds up under adversarial re-reading.

---

## (a) Checklist items that passed

### Task-specific checks (per assignment)

1. **Rise/scale paired with substantive consequence beat, in all 5 sections** — PASS.
   - Cosa Nostra: Maxi Trial (475 tried, 338 convicted, 2,665 years + 19 life sentences) *and* the Falcone/Borsellino assassinations (23/5/1992, 19/7/1992) are both present and given roughly equal narrative weight to the "gabellotto/weak state" origin story. Explicitly labeled "phần trọng tâm bắt buộc, không phải màu sắc phụ."
   - Yakuza: Bōtaihō 1992 + 2008 amendment + prefectural exclusion ordinances + the 80,000→17,600-18,800 membership collapse (20 consecutive years of decline) are all present, framed as the mandatory "khung diễn giải," not an afterthought.
   - Triads: OSCO 1994/1995 + Societies Ordinance + concrete raid numbers (185/3 days, 4,343 arrests) + City University of Hong Kong research on declining triad visibility post-1997 — substantive.
   - Năm Cam: 2003-2004 trial outcome (death sentence, corrupt officials also tried and imprisoned) is present, deliberately minimized in *volume* only (by design, to defer to KP_CL_002) but not reduced to an afterthought — it still carries the section's narrative weight.
   - Cartel Medellín: Search Bloc (1989, ~600 officers, DEA/US military support) + Escobar's death (2/12/1993) + immediate cartel collapse — explicitly required to carry "trọng lượng tường thuật tương đương hoặc lớn hơn phần 'trỗi dậy.'" This is the strongest-enforced consequence beat in the packet, appropriately so given the glamorization risk.
   - No section reads as an afterthought; all five have dedicated "Narrative detail" and "Production cautions" language making the consequence beat structurally mandatory, not optional color.

2. **No operational detail anywhere** — PASS, checked line-by-line against §8's forbidden list (recruitment scripts/targeting, money-laundering mechanics, weapon/drug-sourcing logistics, evasion techniques, coded communication). Findings:
   - Cosa Nostra: gabellotto, omertà, pentiti, capo/consigliere/soldati hierarchy — all conceptual/historical, no "how it worked in practice" mechanics.
   - Yakuza: oyabun-kobun relationship described only as a loyalty/hierarchy concept, no initiation ritual or fee-collection mechanics given.
   - Triads: explicitly refuses to describe initiation rites, sign systems, or badges beyond naming them.
   - Năm Cam: the "bảo kê → front businesses → laundering/evasion" description stays at the level of "a protection racket funneled proceeds into legitimate-looking businesses" — a widely known generic pattern, not a specific mechanic (no named laundering technique, no step-by-step). This is the closest any section comes to the line, and it holds because it is self-labeled "mô tả ở mức khái quát lịch sử, không đủ chi tiết để làm theo" and gives no actionable specificity.
   - Cartel Medellín: violence/bribery/smuggling scale are stated only as historical facts ("chỉ nêu như sự kiện lịch sử, không mô tả chi tiết kỹ thuật"); Escobar's capture-by-phone-tracing detail describes a law-enforcement success, not an evasion technique, so it is correctly on the safe side of the line.
   - No section anywhere provides anything a reader could use as an actual recruitment, laundering, smuggling, evasion, or coded-communication method.

3. **No reproducible gang/triad insignia** — PASS. The only insignia reference is naming "phù hiệu 14K" as an example of a symbol name (not a description of its appearance) to illustrate what *is* permitted (naming) versus what is not (rendering/describing for recognition). No visual, verbal, or structural description of any symbol appears anywhere in the file.

4. **Escobar/Medellín "Cảnh báo lãng mạn hóa" subsection substantive** — PASS, strongly. It is a dedicated subsection (not folded into Production cautions), cites the Narcos criticism, the bin Laden comparison, the Escobar family's own contested reactions, and gives four concrete, actionable counter-framing directives for future scriptwriters — most importantly directive 1, which mandates that every wealth/power figure be paired *in the same narrative beat* with the ~260,000 deaths / ~7,000,000 displaced toll, not just mentioned once and dropped. This requirement is reinforced a second time in "Script-ready material" ("Cấu trúc hai vế cân xứng bắt buộc"), so the pairing requirement is redundant/hard to miss, not a token line.

5. **Hội Tam Hoàng anti-Qing origin flagged as disputed folklore** — PASS. The "phản Thanh phục Minh" narrative is explicitly labeled "Cờ đỏ cảnh báo bắt buộc," "truyền thuyết dân gian," "không phải sự kiện lịch sử đã kiểm chứng hoàn toàn," with an instruction to always use hedged language ("tương truyền"/"theo truyền thuyết dân gian") — never presented as settled history. Confirmed in three places (Historical Background intro, section 3's own Primary Concepts, and Production cautions).

6. **Năm Cam section stays structural, doesn't duplicate KP_CL_002, numbers cross-check** — PASS.
   - The section explicitly states its scope is organizational structure + corrupt-official network, explicitly defers "diễn biến đầy đủ của quá trình điều tra, hai phiên xét xử... narrative vụ án" to KP_CL_002, and does not narrate the investigation timeline, courtroom scenes, or individual case detail that KP_CL_002 covers (Z5.01 investigation unit, specific trial dates 25/2-5/6/2003 and 15/9-30/10/2003, Năm Cam's personal backstory via Huỳnh Tỳ/Đại Cathay, the three named corrupt officials) — none of that appears in KP_CL_005. Good separation of concerns.
   - **Numbers independently verified against KP_CL_002:**
     | Metric | KP_CL_005 | KP_CL_002 | Match? |
     |---|---|---|---|
     | Defendant/charged count | 155 bị cáo | 155 bị can | ✅ same number (see note below on bị can/bị cáo terminology) |
     | Charges | 24 tội danh | 24 tội danh | ✅ |
     | Corrupt officials | 21 người là cán bộ nhà nước/lực lượng chức năng | 21 cán bộ, công chức nhà nước bị xử lý | ✅ |
   - No numeric mismatch found. The packet's own internal "Cập nhật trạng thái" note (added 2026-07-23) already claimed this cross-check had been done and found no conflict — I independently re-derived the same result from both source files rather than trusting that claim at face value, and it holds.
   - **Minor terminology note (not blocking):** KP_CL_005 labels the 155 as "bị cáo" (charged-and-on-trial stage per glossary) while KP_CL_002 labels the same 155 as "bị can" (charged-and-under-investigation stage). Per `DOMAIN_GLOSSARY.md` these are distinct procedural stages, not interchangeable synonyms — but since the same 155 people who were `bị can` at indictment became `bị cáo` once the case reached trial, both labels can be simultaneously true of the same headcount and this is not an actual contradiction. Flagged as an advisory only.
   - **Additional stat not cross-verified (not blocking):** KP_CL_005 states "17 đảng viên" (17 Party members) among the defendants — this figure comes from the same research draft (`RESEARCH_DRAFT_TO_CHUC_TOI_PHAM.md`) but does not appear anywhere in KP_CL_002 or its underlying research draft. This is not a contradiction (KP_CL_002 simply doesn't mention this figure one way or the other), but it means the "17 đảng viên" figure is currently single-packet-sourced. Recommend carrying this figure into KP_CL_002 the next time that packet is revised, purely for completeness, not because of any conflict.

### Full CL-QA-001 through CL-QA-012 pass

| Check | Result | Note |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | Only finally-convicted/deceased-with-public-record individuals are named factually (Falcone/Borsellino as victims, Escobar/Ochoa brothers, Năm Cam and executed co-defendants). No unconvicted individual is named as guilty. |
| CL-QA-002 (net-impression test) | PASS | Framing throughout centers consequence/dismantling, not admiration; no title/hook implies unproven guilt. |
| CL-QA-003 (source-backed org designation) | PASS | Every org's "tổ chức tội phạm" designation is sourced to a tier-1/2 origin (Italian judicial ruling, Japanese statute, Hong Kong ordinance, Vietnamese verdict, US/Colombian law enforcement + investigative journalism). |
| CL-QA-004 (theory completeness) | PASS | Los Pepes/Cartel Cali connection is explicitly hedged as contested/unconfirmed rather than asserted; folklore origin of Triads presents itself as folklore, not the only theory. |
| CL-QA-005 (victim privacy) | PASS | Colombian victims of the Medellín conflict are referenced only in aggregate (260,000 deaths, 7M displaced) — no individual victim identification anywhere in this packet. |
| CL-QA-006 (no legal advice) | PASS | Nothing directed at a viewer's own situation. |
| CL-QA-007 (organized-crime non-glorification, highest severity) | PASS | See detailed operational-detail and glamorization analysis above; this is the check I scrutinized hardest and found no violation. |
| CL-QA-008 (anti-sensationalism) | PASS | No shock-title language, no gore, no countdown-of-horror framing. |
| CL-QA-009 (layered interpretation) | PASS | Legal/procedural (verdicts, laws), narrative (case color), and societal-reflective (why the org emerged, what dismantled it) layers are all present in each of the 5 sections. |
| CL-QA-010 (jurisdiction clarity) | PASS | Italy, Japan, Hong Kong, Vietnam, Colombia/US jurisdictions and legal-system types are all named explicitly (Historical Background + each section). |
| CL-QA-011 (terminology consistency) | PASS (minor note above on bị can/bị cáo) | Matches `DOMAIN_GLOSSARY.md` definitions; "tổ chức tội phạm," "Hội Tam Hoàng" used per glossary. |
| CL-QA-012 (forbidden claims, §12) | PASS | No item on the §12 list is present anywhere in this packet. |

---

## (b) Issues found

**Issue 1 — Stale cross-reference/dependency status text (governance/documentation defect, not a content-safety violation).**

The packet was originally drafted before `KP_CL_002_An_Da_Xu.md` existed, and correctly flagged that dependency as missing in five separate places (YAML frontmatter dependencies list, Packet Control cross-reference row, Canonical Sources table, "Khoảng trống nguồn" bullet, Retrieval Warnings bullet, and Packet Completion Notes item 2). A later "Cập nhật trạng thái (2026-07-23, sau khi soạn)" note was added under Packet Control stating `KP_CL_002` now exists and the Năm Cam numbers were cross-checked and matched — but the five other locations were never updated to match, leaving the packet self-contradictory: one paragraph says the dependency is resolved, while five other locations still assert it doesn't exist / is pending. A future agent skimming only the frontmatter, the Canonical Sources table, or the Retrieval Warnings block (rather than the full Packet Control prose) would wrongly conclude the cross-reference still needs to be done, or would not know it had already been verified.

This is not a content-safety (§4/§6/§7/§8) violation, but it is a real accuracy defect in a governed knowledge asset, and directly bears on the assignment's instruction to "verify the cross-reference is accurate."

## (c) Exact fixes applied

All fixes were made in `KP_CL_005_To_Chuc_Toi_Pham.md`.

**Fix 1 — YAML frontmatter, `dependencies` list:**
- Before: `KP_CL_002_An_Da_Xu.md (cross-reference cho case Năm Cam — CHƯA TỒN TẠI tại thời điểm soạn packet này, xem "Khoảng trống phụ thuộc" bên dưới)`
- After: `KP_CL_002_An_Da_Xu.md (cross-reference cho case Năm Cam — ĐÃ TỒN TẠI kể từ 2026-07-23; số liệu 155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước đã được đối chiếu và khớp, xem "Cập nhật trạng thái" ở Packet Control và _QA_REPORT_KP_CL_005.md)`

**Fix 2 — Canonical Sources table row for KP_CL_002:**
- Before: `| KP_CL_002_An_Da_Xu.md (dự kiến, hiện chưa tồn tại) | Sẽ chứa tường thuật case/phiên tòa... | N/A — placeholder | ...xác nhận link khi KP_CL_002 được viết |`
- After: `| KP_CL_002_An_Da_Xu.md (đã tồn tại kể từ 2026-07-23) | Chứa tường thuật case/phiên tòa... đầy đủ (Pillar 2) | Tier 1-2 cho số liệu tố tụng cốt lõi, kế thừa từ RESEARCH_DRAFT_AN_DA_XU.md | ...đã đối chiếu số liệu 155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước — khớp, không mâu thuẫn |`

**Fix 3 — "Khoảng trống nguồn" (Known Gaps) bullet:**
- Before: `**KP_CL_002 chưa tồn tại** — xem "Lưu ý trạng thái"...; mục Năm Cam dưới đây cần rà soát lại khi packet đó được soạn.`
- After: `~~KP_CL_002 chưa tồn tại~~ — **đã giải quyết 2026-07-23:** KP_CL_002_An_Da_Xu.md nay đã được soạn xong; mục Năm Cam dưới đây đã được rà soát và đối chiếu số liệu, khớp hoàn toàn...`

**Fix 4 — Retrieval Warnings bullet:**
- Before: `...thuộc KP_CL_002_An_Da_Xu.md — packet đó hiện **chưa tồn tại**, cần rà soát cross-reference khi được soạn.`
- After: `...thuộc KP_CL_002_An_Da_Xu.md — packet đó **đã tồn tại** (kể từ 2026-07-23) và cross-reference số liệu đã được xác nhận khớp (155 bị can/bị cáo, 24 tội danh, 21 cán bộ nhà nước).`

**Fix 5 — Packet Completion Notes, item (2) of the pre-`active` requirements list:**
- Before: `(2) KP_CL_002_An_Da_Xu.md được soạn và cross-reference ở mục Năm Cam được xác nhận/khớp;`
- After: `(2) ~~KP_CL_002_An_Da_Xu.md được soạn và cross-reference ở mục Năm Cam được xác nhận/khớp~~ — **hoàn tất 2026-07-23:** đã soạn xong và số liệu đã đối chiếu khớp...`
- Item (1) in the same list was also annotated to note that independent Domain QA has now been performed (this report) and is pending only final human sign-off; item (3) was annotated as still open, requiring human judgment (see below).

No content (Primary concepts, Narrative detail, Script-ready material, Production cautions, Cảnh báo lãng mạn hóa) was altered — only the stale dependency-status metadata was corrected. No transform under §14 was required because no locked-claim-type violation was found.

## (d) Anything unfixable requiring human judgment

1. **Los Pepes / Cartel Cali connection (Cartel Medellín section).** The packet already hedges this appropriately ("độ tin cậy trung bình-cao nhưng còn tranh cãi," "không khẳng định dứt khoát"), but whether this contested detail should appear in a produced script at all — versus being cut entirely to reduce legal/factual risk — is an editorial call for a human producer, not something a QA pass can resolve by rewriting.
2. **Cartel Medellín scale estimates (80% cocaine share, ~15 tons/day, ~$100M/day, ~96% market share at peak).** These are already correctly labeled as law-enforcement-era estimates rather than audited figures, per the packet's own confidence notes. Whether to soften these further, drop the most extreme figure (96%), or keep all of them as-is for narrative impact is a production judgment call, not a compliance defect — flagging for human awareness per the packet's own "Khoảng trống nguồn" list, unchanged from the original draft.
3. **"17 đảng viên" single-packet sourcing** (see item 6 above) — recommend the next revision of KP_CL_002 incorporate this figure for full cross-packet symmetry, but this is a completeness enhancement, not a defect requiring a fix in this pass.

None of the above rise to a blocking issue under `DOMAIN_GUIDE.md` §4/§6/§7/§8 or `DOMAIN_QA_POLICY.md`'s blocking-check list; they are flagged for human awareness only, per this domain's QA process requirement to surface unfixable items rather than silently drop them.
