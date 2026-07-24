# QA Report: KP_CL_005 — Batch 2 Extension (MS-13, mục 6 & Camorra, mục 7)

**Reviewer role:** Independent QA (fresh-eyes, did not author this extension), per `DOMAIN_QA/DOMAIN_QA_POLICY.md` Process section.
**Date:** 2026-07-24
**Files read in full:** `DOMAIN_GUIDE.md` (full, especially §8), `SOURCES/RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md` (full), `KNOWLEDGE_PACKETS/KP_CL_005_To_Chuc_Toi_Pham.md` (full — mục 6 and mục 7 read in full; mục 1-5 skimmed to confirm no alteration and to cross-check the Camorra↔Cosa Nostra compare/contrast against mục 1's actual text), `DOMAIN_QA/DOMAIN_QA_POLICY.md` (full), `GLOSSARY/DOMAIN_GLOSSARY.md` (terminology spot-check), prior `_QA_REPORT_KP_CL_005.md` (for precedent/format and to verify original 5-org figures are unchanged).

**Overall verdict: PASS**, with two non-blocking accuracy/completeness defects found and fixed. No §4/§6/§7/§8 boundary violation found anywhere in the batch-2 extension. The MS-13 "Cảnh báo chính trị hóa/giật gân" subsection survives completely intact and unsummarized, correctly separates the three required information layers, and contains no operational or reproducible-insignia detail. The Camorra section's Saviano/Gomorra and Spartacus Trial consequence beat is present, substantive, and correctly paired per the packet's "rise must pair with fall" pattern.

---

## (a) Checklist items that passed

### Task-specific checks

1. **Existing five organizations unaltered.** Skimmed all of sections 1-5 (Cosa Nostra, Yakuza, Triads, Năm Cam, Cartel Medellín). All figures match the original `_QA_REPORT_KP_CL_005.md`'s independently-recorded numbers verbatim (Maxi Trial 475 tried/338 convicted/2,665 years+19 life sentences; Yakuza 80,000→17,600-18,800; OSCO 185/3 days + 4,343 arrests; Năm Cam 155/24/21/17 đảng viên; Escobar Search Bloc ~600/2-12-1993/260,000 deaths+7M displaced). No drift, no rewording that changes meaning. **PASS.**

2. **MS-13 "Cảnh báo chính trị hóa/giật gân" present in full, not summarized/softened.** Compared line-by-line against research draft §1.6. All content is present: the framing paragraph (channel takes no side), the fact-check bullet (PolitiFact/AP — "gia tăng mạnh" claim contradicted by stable ~10,000 FBI estimate; "hầu hết là nhập cư bất hợp pháp" claim contradicted by US-born-citizen majority; "hàng nghìn bị trục xuất" rated Mostly False), the membership-scale bullet (8,000-10,000 in US / 30,000-70,000 global, always hedged as estimate), the 2025 FTO/SDGT designation bullet with the academic pushback (CNN/AULA/CFR — transnational criminal org vs. terrorism-definition mismatch, and the "strange timing" observation about MS-13's own decline in El Salvador), and all 5 numbered counter-framing directives for future scriptwriters. Nothing was cut; content was reformatted into denser paragraphs but no factual sub-claim was dropped. **PASS.**

3. **Three-layer separation held (verified facts / fact-checked-false claims / open 2025 debate).** These are structurally distinct, not collapsed:
   - (a) Verified facts live in Primary Concepts + Narrative detail (origin, IIRIRA mechanism, clique structure, RICO cases, mano dura security stats + human-rights stats — each with its own confidence label).
   - (b) Fact-checked-false claims are isolated in the dedicated "Fact-check đã xác nhận" bullet, explicitly framed as claims that were rated false/misleading — never repeated elsewhere as if true.
   - (c) The open FTO-designation debate is isolated in its own "Diễn biến chính trị hóa tiếp theo (2025)" bullet, explicitly labeled "tranh luận học thuật/chính sách đang mở, chưa có kết luận đồng thuận — phải trình bày như tranh luận đang diễn ra, nhiều phía, không chọn phe."
   Directive 1 of the counter-framing guidance additionally *instructs future scriptwriters* to keep these three layers separate ("Luôn phân biệt rõ ba tầng thông tin"), so the separation is enforced prescriptively, not just structurally in this document. **PASS.**

4. **No operational/recruitment detail in MS-13 section, even historically framed.** Checked every mention: clique structure, Palabrero role, Mexican Mafia/Sureños prison alliance (naming-only, no mechanics), IIRIRA policy mechanism (policy analysis, not evasion technique), RICO cases (legal outcome, not method). Explicitly self-restrained language throughout: "không đi sâu cơ chế vận hành nội bộ," "chỉ mô tả cấu trúc ở mức khái quát tổ chức học lịch sử-xã hội." **PASS.**

5. **No reproducible tattoo/symbol description.** Tattoos are mentioned exactly once, correctly, as an arrest pretext under mano dura ("nhiều trường hợp bị giam giữ chỉ vì hình xăm... không phải bằng chứng phạm tội cụ thể") — this is the permitted framing per the task instructions. Production cautions explicitly states the packet "chủ động không mô tả hình dạng/nội dung hình xăm cụ thể" despite MS-13 being commonly associated with tattoos in popular media. No description of appearance anywhere. **PASS.**

6. **Camorra compare/contrast with Cosa Nostra — cross-checked side-by-side against mục 1.** Found one inaccuracy (see Issue 1 below, fixed). Aside from that, the core contrast claim — Cosa Nostra's centralized "Ủy ban"/Commissione coordinating families with a dispute-resolution role vs. Camorra's 100+ decentralized, mutually unaccountable clans — is accurate to mục 1's actual content (mục 1's own text: "'Ủy ban' (Commissione) điều phối liên gia đình," and the original research draft's fuller version explicitly states the Commissione's dispute-resolution function). This is genuinely, per the packet's own framing, "one of the least contested points" in the source material, and it holds up. **PASS (after fix).**

7. **Saviano/Gomorra + Spartacus Trial consequence beat — present, substantive, not an afterthought.** Both beats get dedicated, full-paragraph treatment in Narrative detail, are each explicitly labeled mandatory ("Phần trọng tâm bắt buộc," "là điểm neo cảm xúc bắt buộc thứ hai của mục này"), and Production cautions reiterates they must stay paired ("không thể lược bỏ để 'dành thời lượng cho phần cấu trúc'"). The Saviano beat correctly notes the important asymmetry with Falcone/Borsellino (he is alive, the cost is ongoing, not a closed ending) rather than mechanically copying the mục-1 template. The section additionally handles Camorra's honest complication well — it does not force a false "fully dismantled" ending, explicitly restricting the "sụp đổ" framing to the Casalesi clan specifically, per §8's demand for consequence over adventure narrative without requiring the org to be literally finished. **PASS.**

8. **No glorification of Camorra's "social embeddedness."** The "ăn sâu xã hội" description (clans filling a state-void, "hòa trộn tính bất hợp pháp với vẻ ngoài của nghĩa vụ công dân") carries its own explicit anti-romanticization caveat in the same breath, consistent with how the packet already handles this pattern for the other five orgs. **PASS.**

### Full CL-QA-001 through CL-QA-012 pass (batch-2 sections only; 1-5 already covered by prior report)

| Check | Result | Note |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | No unconvicted individual named as guilty anywhere in mục 6/7. RICO defendants and Spartacus's 36 defendants are referenced only as counts, not by name, and only after final conviction is stated. El Salvador mano dura detainees are explicitly kept hedged ("phần lớn... chưa từng bị kết án," reviewed as a §4/§8 intersection point requiring extra caution). |
| CL-QA-002 (net-impression test) | PASS (as a knowledge asset) | No sensational title/hook exists yet at this stage; the packet's own guidance actively steers future scripts away from a net-impression failure on both the guilt-by-association axis (mass arrests) and the political-framing axis. |
| CL-QA-003 (source-backed org designation) | PASS | MS-13: tier-1 DOJ/RICO verdicts + Federal Register FTO designation. Camorra/Casalesi: tier-1 Spartacus Trial verdict (DIA). |
| CL-QA-004 (theory completeness) | PASS | Mano dura debate explicitly requires both the security-efficacy and human-rights-cost sides to appear; academic pushback on the FTO designation is presented as one side of an open debate, not the channel's conclusion. |
| CL-QA-005 (victim privacy) | PASS | No individual victim named or identified in either new section; MS-13's "9 nạn nhân" (Las Vegas RICO) referenced only in aggregate. |
| CL-QA-006 (no legal advice) | PASS | Nothing directed at a viewer's own situation. |
| CL-QA-007 (organized-crime non-glorification, highest severity) | PASS | See items 4, 5, 8 above. Scrutinized hardest per assignment; holds up. |
| CL-QA-008 (anti-sensationalism) | PASS | No shock-title language, no gore, no countdown framing. |
| CL-QA-009 (layered interpretation) | PASS | Both sections carry legal/procedural, narrative, and societal-reflective layers. |
| CL-QA-010 (jurisdiction clarity) | PASS | El Salvador (dân luật, chế độ ngoại lệ flagged as a special legal status) and US federal (RICO) both named explicitly; Italy (civil law) already established in Historical Background, applies to Camorra too. |
| CL-QA-011 (terminology consistency) | PASS | No new umbrella term is introduced outside `DOMAIN_GLOSSARY.md`'s existing "Tổ chức tội phạm" entry — consistent with how mục 1-5 already handle org-specific vocabulary (Yakuza's oyabun/kobun, Cosa Nostra's omertà, etc. are also not individually glossed). Not a batch-2-specific deviation. |
| CL-QA-012 (forbidden claims, §12) | PASS | No item on the §12 list appears anywhere in mục 6/7. |

---

## (b) Issues found

**Issue 1 — Camorra/Cosa Nostra compare/contrast misstated what mục 1 actually says (accuracy defect, not a §4/§6/§7/§8 boundary violation).**

Mục 7's Primary Concepts (Cấu trúc bullet) opened with: *"Cosa Nostra (mục 1) là kim tự tháp — soldati → capo-decina → gia đình (cosca/famiglia) → Ủy ban (Commissione/Cupola) điều phối liên gia đình, có cơ chế phân xử tranh chấp nội bộ,"* explicitly framed as restating what mục 1 "already described." But mục 1's actual text (line 157) is: *"Cấu trúc: 'gia đình' (cosche/famiglie) theo địa bàn, 'Ủy ban' (Commissione) điều phối liên gia đình, phân cấp nội bộ capo/sottocapo/consigliere/soldati/associates."* Mục 1 never uses the term "capo-decina," nor does it describe a `soldati → capo-decina → famiglia` chain — its actual hierarchy is `capo/sottocapo/consigliere/soldati/associates` *within* each family, with the Commissione coordinating *across* families. Traced the term back to `RESEARCH_DRAFT_TO_CHUC_TOI_PHAM_BATCH2.md` §2.2, which independently asserts "Cosa Nostra (đã mô tả trong KP_CL_005): cấu trúc kim tự tháp — soldati → capo-decina → gia đình..." — the research draft's own cross-reference claim was already slightly off from what mục 1 actually contains; the KP inherited it without checking against mục 1's real text. This is not a §8/§4 violation (no operational detail, no individual named), but it is exactly the kind of internal-cross-reference inaccuracy the task asked me to verify, since a scriptwriter relying on this line would describe Cosa Nostra using a rank never established elsewhere in the packet.

**Issue 2 — Camorra's mandatory Saviano+Spartacus pairing requirement was missing from the packet's top-level "Final Packet Use Boundary" enforceable list (completeness/parity gap, not a boundary violation).**

The 6-item "Mọi sản phẩm phái sinh phải giữ được các ranh giới sau" list gives MS-13's politicization-warning requirement explicit standing as boundary item 6 ("MS-13 (mục 6) luôn đi kèm nguyên vẹn tiểu mục..."). The equivalent requirement for Camorra — that the Spartacus Trial and Saviano consequence beats must stay paired and not be trimmed — is stated as mandatory in mục 7's own Production cautions and in the Retrieval Warnings section, but was never promoted to this top-level enforceable list, unlike every other section's core mandatory beat. This is an internal-consistency gap: a future agent skimming only the "Final Packet Use Boundary" section (the document's own designated enforcement summary) would not see this requirement flagged there.

## (c) Exact fixes applied

Both fixes made in `KP_CL_005_To_Chuc_Toi_Pham.md`.

**Fix 1 — mục 7, Primary Concepts, Cấu trúc bullet:**
- Before: `Cosa Nostra (mục 1) là kim tự tháp — soldati → capo-decina → gia đình (cosca/famiglia) → Ủy ban (Commissione/Cupola) điều phối liên gia đình, có cơ chế phân xử tranh chấp nội bộ.`
- After: `Cosa Nostra (mục 1) là kim tự tháp — mỗi "gia đình" (cosca/famiglia) theo địa bàn có phân cấp nội bộ capo/sottocapo/consigliere/soldati/associates, và "Ủy ban" (Commissione) điều phối liên gia đình, có vai trò giải quyết tranh chấp giữa các gia đình (đúng như đã mô tả ở mục 1).`
- This now uses exactly the hierarchy terms mục 1 actually uses, and the dispute-resolution claim is sourced accurately (mục 1's own text says the Commissione "điều phối liên gia đình"; the fuller dispute-resolution wording traces correctly to the original research draft's Cosa Nostra section, which does state the Commissione "có vai trò giải quyết tranh chấp giữa các gia đình" — so nothing invented, just correctly attributed). The rest of the compare/contrast paragraph (Camorra's 100+ decentralized clans, no equivalent coordinating body, the resulting inter-clan violence consequence) required no change — it was already accurate.

**Fix 2 — "Final Packet Use Boundary" list, added item 7:**
- Before (6 items, ending): `6. MS-13 (mục 6) luôn đi kèm nguyên vẹn tiểu mục "Cảnh báo chính trị hóa/giật gân"... / Nếu một sản phẩm đầu ra tương lai không thể giữ được sáu ranh giới này...`
- After (7 items): added `7. Camorra (mục 7) luôn giữ song song hai nhịp hậu quả bắt buộc — Phiên tòa Spartacus (clan Casalesi) và cái giá cá nhân thực tế của Roberto Saviano — không được lược bỏ một trong hai để rút gọn thời lượng; không khái quát hóa "Camorra đã bị dẹp bỏ" vượt quá phạm vi từng clan cụ thể đã bị xét xử.` and updated the closing sentence from "sáu ranh giới" to "bảy ranh giới."

No content in the "Cảnh báo chính trị hóa/giật gân" subsection, the Saviano/Gomorra narrative, the Spartacus Trial narrative, or any Production caution/confidence label was altered — only the one inaccurate cross-reference sentence and the one missing top-level boundary entry were fixed.

## (d) Anything unfixable requiring human judgment

1. **MS-13 membership-scale and deportation-count ranges remain genuinely wide** (8,000-10,000 US / 30,000-70,000 global; 20,000 vs. ~130,000 deportees) — already correctly hedged as dual/ranged estimates per source disagreement, not a defect, but a human editor will need to pick which figure(s) to actually voice in a script and should not silently collapse to one number.
2. **El Salvador prison-death count (261-517, source/date-dependent) and detention totals (84,000-118,000)** — same as above; correctly flagged as time-sensitive and source-dependent in both the research draft and the packet, not resolvable by a QA pass, and will need a "as of [date]" refresh whenever this packet is actually used for a script given how fast-moving the underlying situation is (chế độ ngoại lệ was still being renewed as of the 2026-07-24 research date).
3. **Saviano's protection-duration figure** ("tám năm" in some sources vs. ongoing in others) — already correctly left unresolved/flexible in the packet; a human fact-checker closer to production date should re-verify current status rather than trust either cited figure as final, since this is a living person's ongoing circumstance, not a historical fact.
4. **Whether to include the "capo-decina" rank concept in Camorra's compare/contrast at all** (rather than the corrected `capo/sottocapo/consigliere` terms) is now resolved for internal consistency, but if a future scriptwriter wants to use "capodecina" specifically (it is a real, if secondary, Cosa Nostra rank in broader literature — roughly a squad/ten-man leader), that would require adding it to mục 1 first with its own sourcing, not introducing it unilaterally from mục 7. Flagged for awareness, not blocking.

None of the above rise to a blocking issue under `DOMAIN_GUIDE.md` §4/§6/§7/§8 or `DOMAIN_QA_POLICY.md`'s blocking-check list; they are flagged for human awareness only, consistent with this domain's QA process requirement to surface unfixable items rather than silently drop them.
