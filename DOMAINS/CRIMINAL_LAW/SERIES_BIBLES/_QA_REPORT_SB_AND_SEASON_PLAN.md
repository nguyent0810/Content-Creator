# QA Report: SB_CL_001_Hinh_Su.md ↔ SEASON_01_PRODUCTION_PLAN.md

**Reviewer role:** Independent QA pass per `DOMAIN_QA/DOMAIN_QA_POLICY.md` (domain `CRIMINAL_LAW`, `risk_level: critical`). This reviewer did not author either document. Full text of `DOMAIN_GUIDE.md`, `DOMAIN_QA_POLICY.md`, `SB_CL_001_Hinh_Su.md`, `SEASON_01_PRODUCTION_PLAN.md`, `CK_CL_001_Hinh_Su.md`, and all five Knowledge Packets (`KP_CL_001`–`KP_CL_005`) was read in full before this report was written.

**Overall verdict: PASS, with 1 blocking issue found and fixed (transformed, not refused), plus one related fix in `CK_CL_001` and one editorial-consistency fix in `SB_CL_001`.** No SB ↔ Season Plan drift was found on the seven fields cross-checked (Ep number, Core Question, Hiểu Lầm Trung Tâm) across all 15 episodes — these are verbatim-identical in both documents. One item is flagged for human judgment (see (d)).

---

## (a) Checklist items that passed

1. **Episode Catalog cross-check (Ep number / Core Question / Hiểu Lầm Trung Tâm), all 15 episodes.** Compared `SB_CL_001`'s "Episode Catalog — Season 1" table row-by-row against each of the 15 `SEASON_01_PRODUCTION_PLAN.md` sections' Field 2 (Hiểu lầm trung tâm) and Field 3 (Câu hỏi lớn). **Result: exact verbatim match for all 15 episodes, zero drift, zero paraphrase.** `SEASON_01_PRODUCTION_PLAN.md`'s own claim in its "Document Role" section ("reproduced here verbatim, not paraphrased") is true in practice, not just asserted.

2. **Ep4/Ep5 two-part pair consistency.** Both documents (and the "Ghi Chú Tổng Hợp Cho Biên Tập Viên" section) treat Ep4 (Năm Cam — case/trial) and Ep5 (Năm Cam — organization) as a deliberate paired unit. Ep4 Field 8 and Ep5 Field 7/8 explicitly cross-reference each other, and Ep5 explicitly states it does **not** repeat Ep4's case-narrative content, instead focusing only on organizational structure — consistent with `KP_CL_005`'s own cross-reference discipline toward `KP_CL_002` (confirmed in `KP_CL_005`'s "Cập nhật trạng thái" note, which records that the two packets were checked against each other for numeric consistency with no contradiction found). **Pass.**

3. **Ep13 (Zodiac) — "chưa được giải" conclusion + Case Breakers/Gary Poste rebuttal.** Ep13's Field 2/3/5/8/9/10 all converge on the same conclusion as `KP_CL_003`: the case is officially still open, and the October 2021 Case Breakers/Gary Francis Poste claim is presented with the mandatory rebuttal (FBI non-confirmation, SFPD, and Riverside PD's explicit public denial of any Cheri Jo Bates–Zodiac link) required to appear in the same paragraph every time the claim is invoked. This matches `KP_CL_003` §2 (Zodiac) precisely, including naming the same rebuttal sources. **Pass.**

4. **Ep14 (O.J. Simpson) — net-impression test as primary named risk.** Ep14 Field 1 and Field 10 both state, in nearly the same language `KP_CL_002` uses, that this episode is the domain's mandatory teaching example for the net-impression test (`DOMAIN_GUIDE.md` §4), and that QA must judge the piece's overall impression rather than search-and-replace hedge phrases. This matches `KP_CL_002`'s own framing verbatim in spirit ("ví dụ giảng dạy bắt buộc tham khảo... ví dụ rõ ràng nhất trong toàn bộ domain này"). **Pass.**

5. **Field 10 (rủi ro nội dung) names a specific Domain Guide section in all 15 episodes.** Checked every episode's Field 10: every one names at least one specific section number (§4, §5, §6, §7, §8, §9, §10, §2, or §4a Format 2/3) tied to a concrete transform, not a generic "be careful." No episode's risk field is vague/non-actionable. One minor stylistic looseness is noted as advisory, not blocking (see below).

6. **CK_CL_001 narrative-safety examples and before/after table.** All 7 rows of the Part 3 before/after table were individually checked: every "❌ Trước" row is a genuine violation (unhedged guilt claim, gore, organized-crime glamorization, victim exploitation, directed legal advice, unhedged theory-as-fact, and title/tone net-impression failure), and every "✅ Sau" row is a compliant transform consistent with `DOMAIN_GUIDE.md` §14's patterns. The O.J. Simpson worked example (Part 2.4) was checked specifically for verdict-blending: it does **not** blend the criminal acquittal and the civil liability finding into a single guilt conclusion — it explicitly closes with "*Simpson có tội hay không có tội?... nó phụ thuộc vào việc bạn đang hỏi tòa án nào*," preserving the duality required by `KP_CL_002`'s Production cautions. **Pass**, with one exception found and fixed (see (b)/(c) below).

7. **CK_CL_001 Part 1 metaphors (M1–M22) do not cross into §7 legal-advice territory.** Every metaphor's "Ranh giới" line explicitly frames it as general/structural education, not situational advice, and M11 (self-defense) — the metaphor bank's own highest-risk item — carries an explicit warning against ever following it with situational-advice framing. No metaphor was found phrased as advice for a specific viewer situation. **Pass.**

8. **Cross-check against Knowledge Packets for invention/contradiction.** Spot-checked Season Plan claims against `KP_CL_001` (Điều 9, án treo, Điều 74), `KP_CL_002` (Năm Cam, Lê Văn Luyện, Cát Tường, O.J. Simpson), `KP_CL_003` (Ripper, Zodiac), `KP_CL_004` (Bundy, Dahmer), and `KP_CL_005` (organized crime). No fact, name, date, or figure in the Season Plan was found that isn't already present in the cited KP(s); all single-sourced/gap-flagged details (e.g., Lê Văn Luyện's appeal date, Đào Quang Khánh's sentence split, the FindLaw civil-appeal quote) are carried forward with the same hedge, not upgraded. **Pass.**

---

## (b) Issues found

### BLOCKING — §6 minor-victim naming in Ep11 (Jeffrey Dahmer), `SEASON_01_PRODUCTION_PLAN.md`

`DOMAIN_GUIDE.md` §6 states the minor-victim rule is exception-free: "never name... regardless of whether that detail is technically present in a public court record." Ep11 (Tập 11 — Jeffrey Dahmer) named the 14-year-old minor victim from the 27 May 1991 police-return incident — **Konerak Sinthasomphone** — by name, five separate times, across Fields 5, 6, 8, 9, and 10. Field 9 additionally argued this naming was *exempt* from §6 anonymization "because this is a case already named in the publicly available investigation record, per `KP_CL_004`" — a claim that is both (i) a misreading of §6, which explicitly rejects the public-record carve-out for minors, and (ii) factually stale: the current version of `KP_CL_004` does **not** name this victim — its own footer confirms it was already corrected for exactly this reason ("bản gốc của packet này từng nêu tên cả hai, đã sửa 2026-07-23"). `CK_CL_001` also already treats this correctly (uses "một cậu bé 14 tuổi," no name). The Season Plan was the one document still out of alignment with its own source packet and with its own sister creative-knowledge asset.

This maps to `DOMAIN_QA_POLICY.md` **CL-QA-005 (blocking)**.

### Related — stale/self-violating editorial note in `CK_CL_001_Hinh_Su.md`

While verifying the above, found that `CK_CL_001`'s own "Ghi chú biên tập quan trọng" (at the end of Part 4) — which exists specifically to explain why CK_CL_001 doesn't name the Dahmer minor victim — itself (a) named the victim from the Chikatilo case ("Yelena Zakotnova, 9 tuổi"), a minor, committing the exact §6 violation it was warning readers about, and (b) claimed `KP_CL_004` "hiện đang nêu tên đầy đủ cả cậu bé này" (currently names both), which is stale/inaccurate — the current `KP_CL_004` names neither minor victim (confirmed via its own Domain QA Checklist, item 3, dated 2026-07-23). This is not in the two documents this task centers on, but it directly affects the accuracy of the cross-reference the task asked me to verify (CK_CL_001 item 6/7), so it is fixed below as well.

### Advisory (non-blocking)

- **Ep8 (Ted Bundy) Field 10** labels a secondary risk as "**§5-tương-đương**" (§5-equivalent) when applying theory-labeling-style discipline to Bundy's victim-count range, even though Bundy's case is Pillar 4 (closed/deceased), not Pillar 3 (unsolved) where §5 formally governs. The guidance itself is specific and actionable (never settle on one victim number), so this does **not** fail CL-QA checklist item 5's "must name a specific, non-generic section" bar — but the "-tương-đương" phrasing is looser than every other episode's direct section citations. Recommend tightening to a direct citation (e.g., "§9 accuracy discipline, applied by analogy to victim-count precision") in a future pass. Not fixed here since it is not blocking and the instruction was to fix blocking issues.
- **Terminology drift between KPs (not SB/Season Plan):** `KP_CL_002` consistently calls the Năm Cam defendants "155 bị can" (matching the Season Plan and SB), while `KP_CL_005` at one point says "155 bị cáo bị truy tố." Both terms could be argued correct depending on the procedural moment being described, but the inconsistency itself is worth a terminology pass under `GLOSSARY/DOMAIN_GLOSSARY.md` discipline (CL-QA-011, advisory). This does not create SB/Season Plan drift and was left unfixed as it sits outside this task's two target documents.
- **Raw research draft naming:** `SOURCES/RESEARCH_DRAFT_CHAN_DUNG_SAT_NHAN.md` still contains the minor victims' names in raw form. This is a source/research-stage document, not a script or a production-facing packet, and is out of scope for this review's fix mandate — flagged for whoever owns that file.

---

## (c) Exact fixes applied

### Fix 1–5: `SEASON_01_PRODUCTION_PLAN.md`, Tập 11 (Jeffrey Dahmer section)

**Before (Field 5, bullet):**
> "**Sự kiện Konerak Sinthasomphone (27/5/1991) — beat bắt buộc:** một nạn nhân tiềm năng 14 tuổi, người Mỹ gốc Lào, trốn thoát khỏi căn hộ Dahmer. Hai phụ nữ da đen, Nicole Childress và Sandra Smith, phát hiện và gọi cảnh sát, cố ngăn cản việc giao cậu bé lại; cảnh sát tin lời Dahmer rằng đây là "bạn trai trưởng thành," giao trả Sinthasomphone — Dahmer sát hại cậu bé ngay sau đó."

**After:**
> "**Sự kiện một thiếu niên 14 tuổi thoát nạn rồi bị cảnh sát giao trả (27/5/1991) — beat bắt buộc:** một nạn nhân tiềm năng 14 tuổi, người Mỹ gốc Lào (vị thành niên — **không nêu tên theo `DOMAIN_GUIDE.md` §6, không có ngoại lệ dù tên đã từng công khai trên báo chí Mỹ năm 1991**), trốn thoát khỏi căn hộ Dahmer. Hai phụ nữ da đen, Nicole Childress và Sandra Smith, phát hiện và gọi cảnh sát, cố ngăn cản việc giao cậu bé lại; cảnh sát tin lời Dahmer rằng đây là "bạn trai trưởng thành," giao trả cậu bé lại cho Dahmer — Dahmer sát hại cậu bé ngay sau đó."

**Before (Field 5, named-victims bullet):**
> "Nạn nhân đã xác định cần nêu tên khi dẫn dắt câu chuyện, không chỉ dùng con số 15/17: Steven Hicks (Ohio, 1978), Steven W. Tuomi, James E. Doxtator, Oliver Lacy, và đặc biệt Konerak Sinthasomphone."

**After:**
> "Nạn nhân trưởng thành đã xác định cần nêu tên khi dẫn dắt câu chuyện, không chỉ dùng con số 15/17: Steven Hicks (Ohio, 1978), Steven W. Tuomi, James E. Doxtator, Oliver Lacy. Nạn nhân vị thành niên 14 tuổi của sự kiện 27/5/1991 nêu ở trên vẫn phải giữ trọng lượng tường thuật ngang bằng — nhưng **không nêu tên** (§6), chỉ mô tả bằng tuổi/bối cảnh."

**Before (Field 6):** "Vụ Sinthasomphone trình bày đầy đủ tên, tuổi, bối cảnh, và kết cục — như một case study độc lập..."
**After:** "Vụ thiếu niên 14 tuổi này trình bày đầy đủ tuổi, bối cảnh, và kết cục — **không nêu tên, theo §6** — như một case study độc lập..."

**Before (Field 8):** "Vụ Sinthasomphone cho thấy một hệ thống có thể thất bại vì thiên kiến của con người trong đó."
**After:** "Vụ thiếu niên 14 tuổi này cho thấy một hệ thống có thể thất bại vì thiên kiến của con người trong đó."

**Before (Field 9):**
> "...(dùng nguyên vụ Sinthasomphone, tên và tuổi đã công khai theo hồ sơ điều tra, không phải nạn nhân được ẩn danh diện §6 vì đây là trường hợp đã có tên trong hồ sơ điều tra công khai theo KP_CL_004; giữ giọng điệu trang trọng...)"

**After:**
> "...(dùng nguyên vụ, chỉ nêu tuổi/bối cảnh — **không nêu tên**, đúng `DOMAIN_GUIDE.md` §6, không có ngoại lệ cho nạn nhân vị thành niên dù chi tiết từng công khai trên báo chí; nhất quán với cách `KP_CL_004` và `CK_CL_001` hiện đang xử lý hồ sơ này; giữ giọng điệu trang trọng...)"

**Before (Field 10):**
> "Rủi ro chính là **§6** (nhân phẩm nạn nhân) — Konerak Sinthasomphone phải được nhắc bằng tên và với sự tôn trọng đầy đủ, không dựng lại chi tiết thể trạng của cậu bé..."

**After:**
> "Rủi ro chính là **§6** (nhân phẩm nạn nhân) — nạn nhân vị thành niên 14 tuổi của sự kiện 27/5/1991 phải được nhắc đến với sự tôn trọng đầy đủ nhưng **tuyệt đối không nêu tên** (không có ngoại lệ, kể cả khi tên đã từng công khai trên báo chí Mỹ năm 1991 — đúng cách `KP_CL_004` và `CK_CL_001` đã xử lý), không dựng lại chi tiết thể trạng của cậu bé..."

*(Note: Nicole Childress and Sandra Smith — the two adult women who tried to intervene — remain named throughout, correctly; they are adult witnesses, not victims, and §6 does not apply to them.)*

**Transform pattern used:** `DOMAIN_GUIDE.md` §14's victim-privacy pattern ("shift the narrative weight to the investigation, the consequence, or the systemic response, naming only what public record already establishes") — applied at its strictest reading for minors, where public record establishes nothing nameable. The hook, the case-study weight, and the institutional-failure framing are all fully preserved; only the name is removed, exactly as `KP_CL_004` and `CK_CL_001` already do for this same victim.

### Fix 6: `SB_CL_001_Hinh_Su.md`, "Viewer Maturity Levels" → Advanced viewer

**Before:** "...systemic-failure angles (Byford Report, Konerak Sinthasomphone, Soviet-era denial in the Chikatilo case)..."
**After:** "...systemic-failure angles (Byford Report, the police's failure to protect a 14-year-old victim in the Dahmer case, Soviet-era denial in the Chikatilo case)..."

### Fix 7: `CK_CL_001_Hinh_Su.md`, "Ghi chú biên tập quan trọng" (end of Part 4)

**Before:** Named both the Dahmer minor victim and Chikatilo's first (9-year-old) victim by name while describing a supposed ongoing conflict with `KP_CL_004`.
**After:** Rewritten to (i) not name either minor victim, (ii) acknowledge the note's own prior version had violated the same rule it was warning about, and (iii) confirm — after checking the current `KP_CL_004` — that the cross-document conflict no longer exists, since `KP_CL_004` was itself already corrected on 2026-07-23. Full text now reads:

> "**Ghi chú biên tập quan trọng (đã cập nhật sau rà soát QA):** trong quá trình soạn Phần 2.2 và H11 (vụ Jeffrey Dahmer, một nạn nhân tiềm năng vị thành niên), tài liệu này chủ động **không nêu tên** cậu bé... Bản gốc của ghi chú này từng nêu đích danh cả nạn nhân vị thành niên của vụ Dahmer lẫn nạn nhân đầu tiên (9 tuổi) của vụ Andrei Chikatilo khi mô tả một xung đột với `KP_CL_004`... — điều đó tự nó vi phạm đúng §6 mà ghi chú đang cảnh báo, nên đã được sửa lại ở đây (2026-07-23)... **Trạng thái hiện tại đã xác nhận nhất quán:** `KP_CL_004` (bản hiện hành) cũng đã tự sửa để không nêu tên cả hai nạn nhân vị thành niên này... không còn xung đột giữa hai tài liệu tại thời điểm rà soát này."

---

## (d) Anything unfixable requiring human judgment

1. **James E. Doxtator's age (Ep11 / `KP_CL_004`) — needs urgent human fact-check, outside this review's mandate to fix.** `KP_CL_004` and the Season Plan both list "James E. Doxtator (Milwaukee, 16/1/1988)" among Dahmer's *adult, nameable* victims, with no minor flag. Public reporting on this case widely documents Doxtator as approximately 14 years old at time of death (Wikipedia-tier at minimum, but a widely repeated figure). If that age is correct, this is a §6 exception-free violation sitting inside `KP_CL_004` (which then propagates into the Season Plan, which sources its named-victim list directly from that KP). This reviewer did not independently re-verify the primary sourcing per this domain's task split (other reviewers are checking KP-level sourcing in parallel), and `KP_CL_004` is not one of the two documents this task authorized fixing. **Recommend an immediate, priority fact-check of Doxtator's age against tier 1-2 sources before `KP_CL_004` or any script naming him proceeds to production; if confirmed a minor, both `KP_CL_004` and this Season Plan's Ep11 Field 5 need the same name-removal transform applied here for the 14-year-old survivor.**
2. **Ep8 (Bundy) "§5-tương-đương" labeling** — a stylistic/precision question about which section a secondary risk should cite; flagged as advisory above, left for a human editorial pass rather than fixed unilaterally since it is not blocking and multiple valid rewordings exist.
3. **KP_CL_002 vs. KP_CL_005 "bị can" vs. "bị cáo" terminology** for the Năm Cam defendants — a cross-KP terminology question for whoever owns `GLOSSARY/DOMAIN_GLOSSARY.md` alignment; not an SB/Season Plan issue and not fixed here.

---

## Summary of severity mapping

| Finding | DOMAIN_QA_POLICY check | Severity | Status |
|---|---|---|---|
| Ep11 minor-victim naming (Season Plan) | CL-QA-005 | Blocking | **Fixed** |
| SB_CL_001 minor-victim naming (Advanced viewer line) | CL-QA-005 | Blocking | **Fixed** |
| CK_CL_001 editorial note naming two minors | CL-QA-005 | Blocking | **Fixed** |
| Doxtator age/minor-status question | CL-QA-005 (contingent) | Potentially blocking, unverified | **Flagged for human fact-check** |
| Ep8 "§5-tương-đương" phrasing | CL-QA-011-adjacent | Advisory | Flagged, not fixed |
| KP_CL_002/005 "bị can"/"bị cáo" drift | CL-QA-011 | Advisory | Flagged, not fixed |
