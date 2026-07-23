# QA Report — EP015_016_CASE_STUDY_HOUSE.md (First Independent Domain QA Pass)

| Field | Value |
|---|---|
| File reviewed | `DOMAINS/FENG_SHUI/CREATIVE_KNOWLEDGE/EP015_016_CASE_STUDY_HOUSE.md` |
| Domain | FENG_SHUI (`risk_level: high`) |
| Reviewer | Independent QA agent (did not author the file) |
| Reviewed against | `DOMAIN_GUIDE.md` (full), `DOMAIN_QA/DOMAIN_QA_POLICY.md`, `KNOWLEDGE_PACKETS/KP_FS_001_Phong_Thuy.md` |
| Verdict | **PASS — no blocking (FS-QA-002/004/005/006/007/010) issues found.** Three word-choice/framing tightenings applied for defense-in-depth (see below). |

---

## (a) Checklist items that passed

1. **Fictional-declaration airtightness (Task 1 / DOMAIN_GUIDE §4, §4a).**
   - Mandatory disclaimer block is present at the very top of the file, before any content, and is explicit: house, characters, birth years, and surrounding terrain are "hoàn toàn hư cấu và tổng hợp," not tied to any real address, family, or real consultation record.
   - The disclaimer explicitly instructs that any script derived from this asset must open with "Đây là một ví dụ minh họa hoàn toàn hư cấu — không phải nhà của bạn." — this satisfies the requirement that the fictional framing survive being placed at the start of a produced script.
   - Checked every section (house profile, floor plan, owner bios, surrounding terrain) for anything that could be read as a real address, real family, or real consultation: none found. No city/district/street/ward is named; the alley/terrain description is generic ("hẻm nhỏ hình chữ L") with no identifying detail. Owner names ("ông Phúc," "bà Lan") are generic placeholders explicitly tagged `(hư cấu, tạm gọi ...)`.
   - Section 4 (mandatory editorial boundaries) independently reinforces this a second time ("Không mời khán giả gửi năm sinh hoặc mặt bằng nhà thật để 'xem giúp'"), so the constraint is redundant/defense-in-depth, not single-point-of-failure.

2. **No school declared "winner" (Task 2 / DOMAIN_GUIDE §2, §10).**
   - Section 2's preamble and Section 4 point 1 both explicitly forbid a "trường phái X đúng hơn" conclusion, and the document never states an overall verdict on the house ("nhà này tốt hay xấu" is explicitly named as the wrong question to end on, Section 4 point 6).
   - The comparison table (Section 3) presents the Bát Trạch/Huyền Không kitchen disagreement as arising from two different questions each school asks, not from one school being wrong — this is the correct non-reductive framing required by §10.
   - Grep-verified: every occurrence of "đúng hơn" in the file appears only inside a sentence *forbidding* that framing — none is used to assert it.

3. **Method-consistency against KP_FS_001 (Task 3).**
   - **Bát Trạch Kua calculation** for ông Phúc (b. 1978): 7+8=15→1+5=6→x=6; pre-2000 male formula `10−x`=4; Kua 4 → Tốn → Đông Tứ Mệnh. Matches KP_FS_001's formula and Kua-group table exactly. The parenthetical cross-check for bà Lan (b. 1982, pre-2000 female formula `5+x`, x=1 → Kua 6 → Càn → Tây Tứ Mệnh) is also arithmetically and structurally correct per the packet.
   - Bát Trạch's "Tọa Hung, Hướng Cát" kitchen rule is applied exactly as KP_FS_001 Applied §6 describes it (bad-direction placement desired, good-direction facing desired), and the case study correctly evaluates the fictional kitchen's position (SW — a bad direction for Đông Tứ Mệnh, correctly praised as "đúng chỗ") separately from its facing (NW — also a bad direction, correctly flagged as not meeting the "Hướng Cát" requirement).
   - **Huyền Không** correctly uses construction/move-in year (2015) + facing, not birth year, to derive Vận 8 (2004–2023) per KP_FS_001's own Vận table, and correctly frames itself as dynamic ("theo Vận") versus Bát Trạch's static, person-bound logic — matching KP_FS_001's own Bát Trạch-vs-Huyền Không contrast table.
   - The "Nhị Hắc tại Tây Nam" flying-star reading is explicitly and correctly labeled a *stipulated illustrative assumption*, not a verified full 24-mountain chart result — this mirrors KP_FS_001's own admission that it lacks sourcing for a complete flying-star table and flags this school as the packet's "highest oversimplification risk." The case study inherits that caution faithfully rather than overclaiming precision it doesn't have.
   - **Loan Đầu** correctly uses only physical terrain (no birth year, no construction year), and correctly applies the Tứ Tượng principle (Thanh Long/left should be sturdier than Bạch Hổ/right) from KP_FS_001's Loan Đầu section, including reproducing KP's own caution that this principle "không nên bị đơn giản hóa thành quy tắc cứng."

4. **No certainty language (Task 4 / DOMAIN_GUIDE §5).**
   - Grep swept the file for certainty markers ("bạn sẽ," "chắc chắn," "thực sự," "sẽ [outcome]," "đúng hơn," "tốt hơn," "chính xác nhất"). Every hit is either (a) part of a forbidden-pattern instruction telling future scriptwriters *not* to use that phrasing, or (b) not present at all. All school verdicts are framed as "được Loan Đầu/Bát Trạch/Huyền Không khen/lưu ý," i.e. attributed to the school's own framework, never asserted as objective fact about the house.

5. **Financial/health/lifespan claim-type check (Task 5 / DOMAIN_GUIDE §6-§8).**
   - No line predicts a financial outcome for the fictional owners; the one place a wealth-adjacent classical principle appears ("thủy tụ thì tài tụ," water/wealth), the case study explicitly declines to reach a verdict ("chưa đủ rõ để kết luận") rather than asserting a financial effect.
   - No death/lifespan/crisis-timing content anywhere in the file.
   - The one health-adjacent term ("Nhị Hắc" traditionally associated with "bệnh tật") does not diagnose or predict an illness for the fictional occupants — see Issue 1 below for the tightening applied anyway.
   - Section 4 point 5 already pre-emptively instructs future scriptwriters never to extrapolate a specific health/financial consequence from any "lưu ý" note in the case study — a correct, built-in §14-style guardrail.

6. **Terminology (FS-QA-009).** All terms used (Quái Mệnh, Đông Tứ Mệnh/Tây Tứ Mệnh, Tọa Hung Hướng Cát, Vận, Nhị Hắc, Tứ Tượng/Thanh Long/Bạch Hổ, Minh đường) trace to KP_FS_001's own Core Concepts Map / Terminology list, or are a directly implied member of a named sequence in it (Nhị Hắc as the 2nd of the "Nhất Bạch đến Cửu Tử" nine flying stars). No invented terminology found.

---

## (b) Issues found and (c) exact fixes applied

All three issues below are **word-choice/framing asymmetries**, not hard claim-type violations — they were caught under the adversarial instruction in Task 2 ("does word choice or ordering subtly favor one school's verdict, even if it claims neutrality") and Task 5 (health-adjacency). None of them independently rose to a blocking FS-QA-002/004/005/006/007/010 violation on its own, but all three point the same direction (making Bát Trạch read as the "good news" school and Huyền Không as the "bad news" school), so they were fixed to remove even the appearance of a thumb on the scale, consistent with the §14 "transform, don't just flag" posture.

### Issue 1 — Severity-escalated word choice for Huyền Không's kitchen verdict

**Location:** Section 2.3 body, Section 3 comparison table, Section 3 closing paragraph.

**Problem:** Loan Đầu's negative observation used the neutral word "lưu ý" (note). Huyền Không's negative observation on the same kitchen used the compound "lưu ý/cảnh báo" (note/**warning**) three times — a more severe word than any used for Loan Đầu's or Bát Trạch's points, even though Huyền Không's point rests on an explicitly-stipulated, unverified illustrative assumption (weaker evidentiary footing, not stronger). This created an unintended asymmetry where the least-certain of the three readings was given the most alarming label.

**Fix applied (3 locations):**
- Before: `bị Huyền Không **lưu ý/cảnh báo**` → After: `bị Huyền Không **lưu ý**`
- Before (table): `**Lưu ý/cảnh báo vị trí** (trùng cung mang sao bất lợi của Vận 8 theo giả định minh họa)` → After: `**Lưu ý vị trí** (trùng cung mang sao bất lợi của Vận 8 theo giả định minh họa)`
- Before (closing para): `**Huyền Không lưu ý/cảnh báo** (vì trùng cung mang sao bất lợi của Vận nhà)` → After: `**Huyền Không lưu ý** (vì trùng cung mang sao bất lợi của Vận nhà)`

### Issue 2 — Intensifier attached only to Bát Trạch's praise

**Location:** Section 2.2, hướng nhà paragraph.

**Problem:** Bát Trạch's praise of the house's overall facing was written as "được Bát Trạch **khen rõ ràng**" ("clearly praised") — the only instance of an intensifier anywhere in Section 2's three school write-ups. Loan Đầu's and Bát Trạch's other praised points use plain "khen" with no intensifier. Leaving this in place would make Bát Trạch's single strongest verdict read as more emphatic/definitive than any equivalent verdict from the other two schools, undercutting the "ba góc đọc... bình đẳng" (three readings presented as equal) claim in the file's own stated purpose.

**Fix applied:** `được Bát Trạch **khen** rõ ràng` → `được Bát Trạch **khen**` (intensifier removed; verdict register now matches Loan Đầu's and Bát Trạch's own other praised points).

### Issue 3 — Health-adjacent term ("Nhị Hắc" / "bệnh tật") lacked an inline scope clarifier at its point of use

**Location:** Section 2.3, "Nhận định minh họa" paragraph.

**Problem:** Not a blocking §7 violation (no diagnosis or health-event prediction for the fictional owners was made — see checklist item 5 above), but the sentence introduced the star's traditional "bệnh tật" (illness) association and then said the bad star gets "vượng thêm" (strengthened) without an inline reminder, at the exact point of highest risk, that this is symbolic/traditional-belief content about a star's name, not a claim about ông Phúc/bà Lan's health. The file's only such reminder previously lived in Section 4 point 5, several paragraphs away — safe, but not defense-in-depth at the point of use, which is where a future scriptwriter copying a single sentence out of context would be most likely to over-read it.

**Fix applied:** Inserted an inline clarifying clause at first use, explicitly naming §7 and stating this is the star's traditional symbolic name/meaning, not a diagnosis or prediction for the fictional family; and added a second inline clarifier after "vượng thêm" restating that this describes a symbolic reading getting stronger, not a claim that the family will fall ill. Full before/after:

**Before:**
> cung Tây Nam mang một sao thuộc nhóm "Nhị Hắc" (sao gắn với ý nghĩa bệnh tật, hành Thổ theo nhiều nguồn Huyền Không phổ thông khảo sát — Tier 3, chưa xác minh sâu qua nguồn học thuật). Theo logic ngũ hành phổ biến trong giới thực hành Huyền Không, đặt bếp (hành Hỏa) ngay tại cung này bị một số thầy xem là "Hỏa sinh Thổ" — vô tình làm sao xấu **vượng thêm** thay vì suy yếu.

**After:**
> cung Tây Nam mang một sao thuộc nhóm "Nhị Hắc" (tên gọi truyền thống của sao này trong nhiều nguồn Huyền Không phổ thông khảo sát gắn liền với ý nghĩa biểu tượng "bệnh tật", hành Thổ — Tier 3, chưa xác minh sâu qua nguồn học thuật; đây là ý nghĩa biểu tượng truyền thống gắn với *tên gọi* của sao, không phải một chẩn đoán hay dự đoán bệnh tật cụ thể cho gia đình hư cấu ông Phúc/bà Lan — đúng ranh giới §7 domain guide). Theo logic ngũ hành phổ biến trong giới thực hành Huyền Không, đặt bếp (hành Hỏa) ngay tại cung này bị một số thầy xem là "Hỏa sinh Thổ" — vô tình làm sao xấu **vượng thêm** thay vì suy yếu (nghĩa là, theo cách diễn giải riêng của Huyền Không, ý nghĩa biểu tượng bất lợi của cung này được xem là mạnh lên chứ không yếu đi — không phải một tuyên bố rằng gia đình sẽ ốm đau).

---

## (d) Anything unfixable requiring human judgment

Nothing found requires escalation or human judgment beyond the fixes already applied. Two lower-priority observations for whoever produces the actual EP015/016 script (not requiring a change to this creative-knowledge asset itself):

1. **Structural imbalance in "screen time," not tone.** Bát Trạch evaluates three house elements (facing, bedroom, kitchen) in this case study; Huyền Không, due to the packet's own honestly-disclosed sourcing gap on full flying-star charts, only evaluates one (kitchen). This is a defensible, honestly-disclosed limitation (the file explains why in both Section 2.3 and Section 3), not a bias — but when this asset is turned into an actual script, the writer should keep Section 4 point 1's "thời lượng và giọng điệu ngang nhau" (equal runtime and tone) instruction in mind and may want to consciously balance runtime even though Huyền Không has structurally less to say in this particular illustrative example.
2. **Kua-formula lunar/solar year conversion caveat.** KP_FS_001 itself flags (Khoảng trống nguồn) that some sources require lunar-year conversion for people born near Tết, which this case study's Kua calculation does not address. This is inherited uncertainty from the knowledge packet, not an error introduced by the case study, and does not need a fix here — flagging only so a future, more detailed script doesn't accidentally present the Gregorian-year shortcut as definitively correct.

No blocking issue required a refusal or an unresolved §14 escalation.
