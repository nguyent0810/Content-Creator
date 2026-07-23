# Independent Domain QA Report — KP_FS_001_Phong_Thuy.md

**Reviewer status:** Independent QA pass, first-ever for this domain/packet. This report was produced by a reviewer with no authorship role in the packet, per `DOMAIN_QA_POLICY.md` Process ("the agent/reviewer checking a script must not be the same context that wrote it").

**Reviewed against:** `DOMAIN_GUIDE.md` (full, §1-14), `DOMAIN_QA/DOMAIN_QA_POLICY.md` (FS-QA-001 to FS-QA-010), `GLOSSARY/DOMAIN_GLOSSARY.md`, and the three research drafts KP_FS_001 declares as dependencies: `RESEARCH_DRAFT_AM_DUONG_NGU_HANH.md`, `RESEARCH_DRAFT_BAT_QUAI_TRUONG_PHAI.md`, `RESEARCH_DRAFT_UNG_DUNG_NHA_O.md`.

**Verdict: PASS, with one blocking-adjacent sourcing defect found and fixed in place.** No violation of FS-QA-002 (individualized reading), FS-QA-004 (financial), FS-QA-005 (health), FS-QA-006 (lifespan — not applicable, no Tử Vi content in this packet), or FS-QA-007 (anti-fear-sales) was found anywhere in the packet's actual descriptive/applied text. The packet is unusually disciplined for a first-draft knowledge asset — nearly every risk area already carries its own explicit caution and a compliant required-language pattern. The one real defect found was a **sourcing-integrity problem in the Khí section**, which fabricated a tertiary source that contradicts the packet's own "Khoảng trống nguồn" (Known Gaps) disclosure. This has been rewritten in place (see §(c) below).

---

## (a) Checklist items that passed

| Check | Result | Notes |
|---|---|---|
| FS-QA-001 (source attribution) | **Pass, after fix** | See (b)/(c) — one violation found and corrected in the Khí section; everything else (Bát Quái Tiên Thiên/Hậu Thiên, Loan Đầu/Bát Trạch/Huyền Không attributions, historical-legend attributions) correctly names school/source or flags cross-school disagreement. |
| FS-QA-002 (no individualized reading) | **Pass** | Checked every "Chi tiết ứng dụng"/"Production cautions" pair in the Applied Section (hướng nhà, cửa, phòng khách, phòng ngủ, bàn thờ, bếp, cây, vật phẩm, văn phòng) and the Bát Trạch Kua-number formula. All instructive/formula content is paired with an explicit "not the viewer's house/chart" caution and a compliant required-language pattern (Rule 2). No line invites birth-year/floor-plan submission or narrates a specific implied viewer's situation. |
| FS-QA-003 (no certainty language) | **Pass** | Grepped the full packet for "sẽ" and "chắc chắn/đảm bảo/cam kết" — every occurrence outside a labeled Forbidden-pattern example is either (i) the Ngũ Hành Tương Sinh/Tương Khắc cycles, which `DOMAIN_GUIDE.md` §3 explicitly authorizes stating as settled fact, or (ii) a statement about internal logical consistency, not a future-outcome claim. |
| FS-QA-004 (financial boundary) | **Pass** | Every wealth-adjacent claim (hướng nhà, cây phong thủy, Tỳ Hưu, Thiềm Thừ, thác nước, bàn làm việc) carries an explicit "not a guaranteed financial mechanism" caution, matching `DOMAIN_GUIDE.md` §6's own worked example almost verbatim. No line asserts a guaranteed wealth outcome. |
| FS-QA-005 (health boundary) | **Pass** | Phòng ngủ section explicitly reframes "gây đau đầu, buồn nôn"-style source language as "được tin là ảnh hưởng tới giấc ngủ/tinh thần... không phải chẩn đoán y khoa." No diagnosis/cure claim anywhere. |
| FS-QA-006 (lifespan/crisis) | **N/A / Pass** | This packet is the Phong Thủy track only (`secondary_context` explicitly excludes deep Tử Vi content); no lifespan/Cung Tật Ách content appears here — correctly out of scope. |
| FS-QA-007 (anti-fear-sales) | **Pass** | Every vật phẩm subsection (gương bát quái, Tỳ Hưu, Thiềm Thừ, thác nước) and the bàn thờ/bếp/cửa sections explicitly name and forbid the "đại kỵ / sẽ gặp họa" fear pattern, and correctly ground this in the real Vietnamese spiritual-fraud press coverage (Applied §10) as an operational reason, not a style preference. Body/descriptive text itself (not just the cautions) stays neutral throughout — no residual dread-framing found in the descriptive prose. |
| FS-QA-008 (layered framework) | **Pass** | Cultural/historical, traditional-belief, and modern-reflective layers are all present and none erases another — clearest in the Khí section (ventilation/light as "phép loại suy," not proof) and Phòng ngủ (traditional layout logic run parallel to environmental psychology without claiming equivalence). |
| FS-QA-009 (terminology consistency) | **Pass** | Cross-checked Âm Dương, Ngũ Hành, Bát Quái, Khí, Loan Đầu, Bát Trạch, Huyền Không Phi Tinh definitions against `DOMAIN_GLOSSARY.md` — all consistent. The packet's own "Terminology" section transparently proposes glossary additions (Đông Tứ Mệnh, Sinh khí, etc.) rather than silently assuming them, which is the correct process per §11. |
| FS-QA-010 (forbidden claims) | **Pass, after fix** | No line claims scientific proof, authoritative personal reading, financial/medical advice via reading-frame, or mortality timing. The Khí section's "never scientifically proven" conclusion is correct and required by §12 — but see (b) for the sourcing defect that indirectly touched this claim's evidentiary basis, now fixed. |

## Attribution and cross-school checks (task items 2 and 3, in depth)

- **Bát Quái Tiên Thiên vs. Hậu Thiên:** Consistently distinguished everywhere (Historical Background, Core Concepts Map, Historical Debates #5). Hậu Thiên is correctly and consistently marked Tier 1/high-confidence for the home-application table; Tiên Thiên's detailed positions are consistently marked medium-confidence with the same caveat (Cấn/Đoài placement disagreement) repeated verbatim from `RESEARCH_DRAFT_BAT_QUAI_TRUONG_PHAI.md` §1.2/§1.4. No inflation found.
- **Bát Trạch vs. Huyền Không Phi Tinh:** Every specific rule in the Applied Section is explicitly prefixed "theo trường phái Bát Trạch" (Applied Section header, restated at point of use in §1 Hướng nhà, §6 Bếp's "Tọa Hung Hướng Cát"). Rule 1 and Rule 10 (School-Naming Rule, Cross-School Contradiction Disclosure Rule) both require this and both are followed in the body text, not just declared in the abstract. The "not cùng một gốc" quote from phongthuyhuyenkhong.vn is correctly attributed and under 15 words per the copyright constraint.
- **Khí across the three schools (Loan Đầu static/terrain, Bát Trạch static/person, Huyền Không dynamic/time):** consistently distinguished, never merged into one mechanism, and the Khí section explicitly cross-references every earlier use of "khí" in the packet (Âm Dương's Dương khí/Âm khí, Loan Đầu's tụ/tán, Bát Trạch's hướng-mệnh hài hòa, Huyền Không's khí vượng theo Vận, Applied Section's "miệng khí") — no contradiction found between the Khí section (added later) and any earlier usage.
- **Historical-legend attributions (Phục Hy, Văn Vương, Quách Phác, Dương Quân Tùng, Chu Đôn Di):** every instance checked uses "tương truyền"/"được cho là"/"quy gán truyền thuyết" — none is stated as verified historical fact, matching Rule 9 and `DOMAIN_GUIDE.md` §2's Trần Đoàn-analog standard.

---

## (b) Issue found

### Blocking-adjacent: fabricated tertiary sourcing in the Khí section (Core Concepts Map → Khí → Narrative detail and Production cautions)

**What was wrong:** The Khí section (packet's own text notes it was "added later than the rest of the packet") claimed its description of khí was cross-verified against three independent source tiers: Vietnamese popular practice, English popular practice, **and "nguồn học thuật/phê phán phong thủy" (an academic/critical-of-feng-shui source)**. It further attributed a specific claim to English-language sources — that they describe khí as "vital life force"/"transformative energy flow" — and asserted that an academic/critical source confirmed khí "chưa từng được đo lường hay xác nhận tồn tại qua bất kỳ thí nghiệm khoa học độc lập nào."

**Why this is a real defect:** None of this is traceable to the three research drafts this packet depends on. Worse, it is **directly contradicted by the packet's own "Khoảng trống nguồn" section** (Canonical Sources), which states in plain terms: *"Không có nguồn academic/dân tộc học độc lập nào được truy cập trong cả 3 research draft."* A packet cannot simultaneously say "no academic source was ever accessed" in one section and "an academic/critical source confirms X" in another. This is exactly the "do not invent a source" failure `DOMAIN_GUIDE.md` §3 prohibits, and it is doubly serious here because it sits underneath the domain's single most safety-critical claim — that Khí is not scientifically proven (§12) — which does not need a fabricated citation to be true, and is actually weakened by resting on one that doesn't exist (a hostile reviewer could otherwise correctly say "cite your academic source" and find none).

This does not cleanly map to FS-QA-004/005/006/007 (the formally "Blocking" checks), so it is nominally an FS-QA-001 (Advisory) finding. I am treating it as blocking-severity in effect and fixing it directly, because it undermines the evidentiary basis for an FS-QA-010/§12 claim and violates the domain's explicit anti-fabrication rule.

---

## (c) Exact fix applied

**File:** `DOMAINS/FENG_SHUI/KNOWLEDGE_PACKETS/KP_FS_001_Phong_Thuy.md`, Core Concepts Map → Khí section.

**Fix 1 — Narrative detail paragraph.**

Before:
> ...được xác nhận nhất quán qua đối chiếu nhiều nguồn thực hành phong thủy độc lập cả tiếng Việt (ví dụ nguồn dân gian phổ thông về "sinh khí/tà khí," về nguyên lý "khí gặp gió tán, gặp nước dừng") lẫn tiếng Anh (mô tả khí như "vital life force"/"transformative energy flow" gắn với địa hình và hướng la bàn). Điều này khác về bản chất với khái niệm "năng lượng" (energy) trong vật lý hiện đại... Đối chiếu thêm nguồn học thuật/phê phán phong thủy cho thấy khí chưa từng được đo lường hay xác nhận tồn tại qua bất kỳ thí nghiệm khoa học độc lập nào — đây là cơ sở cho khẳng định "chưa được khoa học chứng minh" mà `DOMAIN_GUIDE.md` §12 yêu cầu.

After (implemented):
> ...được xác nhận nhất quán qua đối chiếu các nguồn thực hành phong thủy độc lập **thực sự có trong 3 research draft nền tảng của packet này** — cả tiếng Việt (nguồn dân gian phổ thông về "sinh khí/tà khí"...) lẫn tiếng Anh (**các nguồn Loan Đầu/Form School đã khảo sát, ví dụ fengshui-expert.fr, jacquipepper.com** — mô tả khí như một luồng sức sống/năng lượng truyền thống gắn với địa hình và hướng la bàn, luôn ở mức ẩn dụ, không đại lượng nào được định nghĩa đo được)... **Lưu ý về nguồn (sửa sau QA...): cả 3 research draft nền tảng của packet này đều chưa tiếp cận được bất kỳ nguồn học thuật/phê phán phong thủy độc lập nào (xem "Khoảng trống nguồn"...) — bản nháp trước của mục này viện dẫn nhầm một "nguồn học thuật/phê phán phong thủy" như thể đã được xác minh cho packet, điều này không đúng và đã được sửa.** Khẳng định "khí chưa được khoa học chứng minh" trong packet này đứng vững không phải vì có một nguồn phê phán học thuật cụ thể đã bác bỏ nó, mà đơn giản vì **không một nguồn nào trong toàn bộ nguồn đã khảo sát (kể cả các nguồn ủng hộ/thực hành phong thủy) từng đưa ra bằng chứng đo lường hay thực nghiệm độc lập, lặp lại được cho khí** — sự vắng mặt hoàn toàn của bằng chứng đo lường, không phải một nguồn phản bác, là cơ sở cho yêu cầu `DOMAIN_GUIDE.md` §12.

**Fix 2 — Production cautions, confidence-tier line.**

Before:
> Nhãn độ tin cậy: cách truyền thống mô tả khí... đối chiếu nhất quán qua ≥3 nguồn độc lập (thực hành phổ thông tiếng Việt, thực hành phổ thông tiếng Anh, **nguồn học thuật/phê phán phong thủy**) — mức tin cậy trung bình-cao...

After (implemented):
> Nhãn độ tin cậy: cách truyền thống mô tả khí... đối chiếu nhất quán qua **2 nhóm nguồn độc lập thực sự có trong 3 research draft nền tảng của packet này** (thực hành phổ thông tiếng Việt; thực hành phổ thông tiếng Anh của nhánh Loan Đầu/Form School) — mức tin cậy **trung bình**... **Sửa sau QA: packet chưa từng tiếp cận một nguồn học thuật/phê phán phong thủy độc lập nào... không được đếm đó như một tầng nguồn thứ ba đã xác minh. Kết luận an toàn (khí không phải hiện tượng vật lý đã được khoa học xác nhận) vẫn đứng vững, vì nó dựa trên sự vắng mặt của bất kỳ nguồn nào — kể cả nguồn ủng hộ phong thủy — từng đưa ra bằng chứng đo lường được, không dựa trên một nguồn phản bác cụ thể.**

Net effect of both fixes: the safety-critical conclusion ("Khí is not a measured physical energy, not scientifically proven") is **preserved and, if anything, put on firmer footing** (absence-of-evidence framing instead of a phantom citation), while the fabricated three-source verification claim and the invented English-language quotes are removed. The confidence tier for "traditional description of khí" is correctly downgraded from the previously-claimed "trung bình-cao" (medium-high, resting on a fake third source) to the accurately-supported "trung bình" (medium, resting on the two source groups that actually exist in the dependency drafts).

---

## (d) Anything unfixable / requiring human judgment

1. **Domain QA / Research QA / Safety QA / Historical QA / Brand QA status.** This report constitutes the Domain QA pass referenced in the packet's `required_qa` list, but I cannot unilaterally flip `QA_status` in the frontmatter to "passed" — the packet also lists Research QA, Safety QA, Historical QA, and Brand QA as separately required, and those are outside this review's scope (this was specifically a Domain-QA-checklist pass against `DOMAIN_QA_POLICY.md`). A human/process owner should decide whether this report satisfies the "Domain QA (Phong Thủy)" line item specifically, and should still route the packet through the other four before flipping `status` away from `draft-pending-human-review`.
2. **Known Gaps already flagged by the packet itself remain genuinely open** and are outside what a QA pass can resolve by rewriting text: no ethnographic/academic source for bàn thờ gia tiên practice, no Kinh Dịch scholarly source to pin down the Tiên Thiên Bát Quái directional table, no lịch pháp source to confirm the lunar-calendar-conversion detail in the Kua number formula, and no unified explanation for the Ngũ Hành Cục numbering (2-3-4-5-6) in Tử Vi. These require new research, not editorial fixes, and the packet already labels them correctly as gaps rather than overclaiming — no action needed beyond what's already flagged.
3. **The Khí-section fabrication is a process finding, not just a content finding.** Whoever/whatever produced the Khí section (added later than the rest of the packet, per its own text) evidently drew on general world knowledge about qi/feng-shui criticism rather than strictly re-deriving from the three cited dependency drafts, then wrote it up as if it had been sourced the same disciplined way as the rest of the packet. Worth a human note for whatever process adds future "unify scattered mentions into one section" style updates to existing Knowledge Packets: re-verify against the actual dependency list before writing confidence-tier language, not just before writing content claims.

---

## Summary of severity

- **Blocking issues found and fixed: 1** (Khí section fabricated tertiary sourcing — fixed in place, see (c)).
- **Blocking issues found and NOT fixable by rewrite: 0.**
- **Advisory issues: 0** beyond the one item above (already counted).
- Everything else in the packet — school attribution, individualized-reading boundary, certainty language, financial/health/anti-fear-sales boundaries, layered framework, terminology — passed on direct inspection against the three cited research drafts and `DOMAIN_GUIDE.md`.
