---
schema_version: 1.0
asset_id: AST_CL_EP001_QA_REPORT
asset_type: qa_report
episode_id: EP001
package_id: PKG_CL_HS_EP001
domain_id: CL
reviewed_asset: 03_AUDIO_SCRIPT_MASTER.md (v0.1.0 as submitted → v0.1.1 as fixed)
reviewer_role: Independent Domain QA (Hình Sự) — CL-QA-001 through CL-QA-012
review_date: 2026-07-23
result: PASS (after 3 direct in-file transforms; no blocking issue remained unresolved)
---

# 06 QA Report — EP001, Giải Mã Hình Sự

## Result: PASS (post-transform)

This is the first script ever produced in the `CRIMINAL_LAW` domain (`risk_level: critical`). It was reviewed independently, in full, word-by-word, against `DOMAIN_GUIDE.md`, `DOMAIN_QA_POLICY.md` (CL-QA-001–012), `01_RESEARCH_BRIEF.md`, `02_EPISODE_PLANNER.md`, `KP_CL_001_Luat_Hinh_Su.md`, and `KP_CL_002_An_Da_Xu.md`. Three factual-precision issues were found and transformed directly in the script file per §14 (Transform First). No issue required refusal or a watered-down rewrite. No CL-QA-005 minor-victim-naming violation was found (the specific failure pattern this domain has repeated before) — this script gets that discipline right.

**Final word count (post-fix): 5,894** — within the 5,200–6,500 target band. **Original submitted word count: 5,761** (also in-band; the +133 words come from one added balancing sentence, see Issue 3).

## Checklist Table (CL-QA-001 through 012)

| Check ID | Verdict | Notes |
|---|---|---|
| CL-QA-001 (legal-status precision) | PASS | All four stations (bị tình nghi/bị can/bị cáo/đã bị kết án) defined correctly in Beat 1 and used consistently at every later occurrence. Beat 0's "kẻ giết người"/"tên sát nhân máu lạnh" are quoted as the *public's* wrong behavior, not the channel's claim — correctly framed. Lê Văn Luyện is named only after the effective-final-judgment reasoning is stated ("Chính vì vậy — và chỉ vì vậy —"). O.J. Simpson's criminal acquittal and civil liability are never merged into a guilt-asserting noun. |
| CL-QA-002 (net-impression test) | PASS | Verified sentence-by-sentence (see dedicated section below). The piece explicitly teaches and self-applies the test; no beat's structure, hook, or ending tips toward an unstated guilt conclusion. |
| CL-QA-003 (Format 2/3 sourcing) | N/A | No Format 2 (unsolved, named person-of-interest) or Format 3 (organized-crime designation) content in this episode — both illustrative cases are closed, Format 1. |
| CL-QA-004 (theory completeness) | N/A | No unsolved case discussed. |
| CL-QA-005 (victim privacy, incl. mandatory age sub-check) | PASS | Verified independently (see dedicated section below). Neither minor victim is named or given any identifying detail beyond age/role, anywhere in the file, including editorial notes/metadata. Ages (≈18 months, ≈8 years) independently checked against `KP_CL_002` and confirmed as minors — anonymization correctly triggered. |
| CL-QA-006 (no legal advice) | PASS | No line answers "what should I do about my/my acquaintance's situation." All procedural explanation stays general. |
| CL-QA-007 (organized-crime non-glorification) | PASS | Năm Cam is not used as a worked example (consistent with Episode Planner's "optional" framing); Beat 8's closing reference to organized crime ("một mạng lưới bảo trợ trong bộ máy nhà nước") stays generic, no name, no operational detail, no glamorization. |
| CL-QA-008 (anti-sensationalism) | PASS | Opening hook re-read specifically for sensationalism: uses a calm, analytical register ("dòng chữ đỏ báo 'nóng' ở góc màn hình") with no "SỰ THẬT RÙNG RỢN"/countdown-of-horror framing. Tone matches Series Bible throughout — documentary-guide voice, not tabloid or prosecutorial. |
| CL-QA-009 (layered interpretation) | PASS (post-fix) | **Found an issue and fixed it** — see Issue 2 below. The Lê Văn Luyện beat's societal-reflective layer was one-sided before the fix (only the "principle should hold firm" side), against `KP_CL_002`'s explicit Production Caution to present both sides of the age-cap debate. |
| CL-QA-010 (jurisdiction clarity) | PASS | O.J. Simpson's jurisdiction (California, USA) is stated in the very first sentence introducing that case, before any procedural claim. Double jeopardy and "bồi thẩm đoàn" (jury) are explicitly flagged as common-law/U.S. concepts, explicitly contrasted with Vietnam's hội đồng xét xử — no foreign-concept bleed into the Vietnamese-system description. |
| CL-QA-011 (terminology consistency) | PASS (advisory note) | All legal-status and procedural terms match `DOMAIN_GLOSSARY.md`. One advisory-only gap: "bồi thẩm đoàn" (jury) is used correctly in context but is not yet its own glossary entry (only "Common law vs. Civil law" covers it indirectly) — recommend adding it to Section C for future episodes that reuse it, not a script-blocking issue. |
| CL-QA-012 (forbidden claims / no invented facts) | PASS (post-fix) | **Found two issues and fixed them** — see Issues 1 and 3 below. No line matches any §12 forbidden-claim type after the fixes. |

## Issues Found and Fixes Applied (§14 Transform, all applied directly to `03_AUDIO_SCRIPT_MASTER.md`)

### Issue 1 — Overclaimed/self-contradicting procedural detail in the Lê Văn Luyện beat (CL-QA-012, factual precision)

**Problem:** The script stated the case "trải qua đầy đủ tám bước tố tụng" (went through the full eight procedural steps) and then listed only four (điều tra, truy tố, xét xử sơ thẩm, phúc thẩm). This directly contradicts the script's own Beat 3 explanation — established two beats earlier — that giám đốc thẩm/tái thẩm are rare, conditional special procedures, not steps every case automatically passes through. `KP_CL_002` explicitly states no giám đốc thẩm/tái thẩm was recorded for this case ("không ghi nhận kháng nghị giám đốc thẩm/tái thẩm nào"). Claiming "all eight steps" is an invented/unsupported procedural fact — the exact failure mode CL-QA-012 and this domain's §5 anti-invention rule exist to catch, even though the underlying case itself is safely Format 1.

**Before:**
> "...Vụ án trải qua đầy đủ tám bước tố tụng mà chúng ta vừa nói tới ở phần trước: điều tra, truy tố, xét xử sơ thẩm, rồi xét xử phúc thẩm. Cả hai cấp xét xử đều tuyên tổng hợp hình phạt 18 năm tù giam."

**After:**
> "...Vụ án đi qua các bước tố tụng chính mà chúng ta vừa nói tới ở phần trước: điều tra, truy tố, xét xử sơ thẩm, rồi xét xử phúc thẩm — không ghi nhận thủ tục đặc biệt giám đốc thẩm hay tái thẩm nào được áp dụng thêm sau đó. Cả hai cấp xét xử đều tuyên tổng hợp hình phạt 18 năm tù giam."

**Severity:** Treated as blocking-adjacent under CL-QA-012 (invented/inaccurate procedural claim) given this domain's zero-tolerance stance on unsupported facts. Transformed in place, no content lost.

### Issue 2 — Lê Văn Luyện societal-reflective layer presented only one side of the debate (CL-QA-009, advisory)

**Problem:** `KP_CL_002`'s Production Cautions for this case explicitly require: "phần tranh luận xã hội về mức án phải trình bày cả hai phía, không được chỉ chọn một phía để tạo cảm giác 'đúng/sai' rõ ràng." The submitted script only presented the "the humanitarian cap should hold firm regardless of public reaction" side (via the "fixed roof, unmoved by the storm" metaphor) and omitted the documented counter-view (that some legal opinion favors reconsidering the cap for extremely severe crimes) that `KP_CL_002`'s Narrative Detail section establishes as part of the real, sourced debate.

**Before:** (ended at) "...Đây là một nguyên tắc nhân đạo cứng — giống một mái nhà cố định, không di chuyển theo mức độ dữ dội của cơn bão bên dưới nó — chứ không phải một điểm có thể co giãn tùy theo phản ứng của dư luận."

**After (added sentence):** "...Vụ án cũng để lại một cuộc tranh luận công khai kéo dài, không có câu trả lời đơn giản: một số ý kiến, kể cả từ giới làm luật, cho rằng mức trần này nên được xem xét lại cho những trường hợp đặc biệt nghiêm trọng; nhiều ý kiến khác giữ quan điểm ngược lại, cho rằng nguyên tắc nhân đạo và khả năng cải tạo của người chưa thành niên cần được giữ vững bất kể mức độ nghiêm trọng của hành vi. Tập này không chọn phe trong cuộc tranh luận đó — chỉ ghi nhận rằng cả hai phía đều đang tồn tại thật, song song với nhau."

**Severity:** Advisory per the QA Policy's severity table (does not block in isolation), but fixed anyway per the Transform-First mandate since the source material (`KP_CL_002`) explicitly requires the balance and the fix was low-cost and lossless to the beat's intent.

### Issue 3 — Unsourced specific detail in the O.J. Simpson beat (CL-QA-012, minor)

**Problem:** The script stated the criminal jury was "mười hai người dân thường" (twelve laypeople). Neither `KP_CL_002` nor the pre-built passage this beat is explicitly modeled on (`CK_CL_001` §2.4) states a specific juror count. While a 12-person jury is generally true of the U.S. system, it is not a fact this domain's two governing knowledge packets actually contain, and the task's instruction is to treat any number beyond what `KP_CL_001`/`KP_CL_002` establish as unverified. Given this domain's "no invented fact" discipline, the specific figure was removed as an unnecessary risk with no loss of narrative value.

**Before:** "Bồi thẩm đoàn — mười hai người dân thường, không phải thẩm phán chuyên nghiệp — là một khái niệm của hệ thống thông luật..."

**After:** "Bồi thẩm đoàn — một nhóm người dân thường, không phải thẩm phán chuyên nghiệp — là một khái niệm của hệ thống thông luật..."

**Severity:** Minor/advisory, fixed as a precaution.

## Dedicated Re-Verification: Lê Văn Luyện Minor Victims (per task instruction 2)

Read every sentence of the beat again, specifically hunting for a name or a distinguishing identifying detail beyond age/role. Findings:

- The only victim-referencing sentences in the entire file are: "chủ tiệm vàng và vợ của ông đã thiệt mạng," "Con gái út của họ, khi đó khoảng mười tám tháng tuổi, cũng đã tử vong," and "Một người con gái khác trong gia đình, khoảng tám tuổi, bị thương rất nặng nhưng sống sót."
- No given name, family name, initial, school, physical description, or any other distinguishing detail appears for either minor victim, anywhere in the file (narration or editorial notes).
- The script includes an explicit, unprompted on-screen disclosure of the anonymization rule itself ("kênh này sẽ không nêu tên hai nạn nhân nhỏ tuổi nhất của vụ án này... dù chỉ là một câu nhắc thoáng qua"), which both matches `02_EPISODE_PLANNER.md` Beat 6's requirement and independently confirms the writer was aware of and actively applying the rule, not merely omitting names by accident.
- Ages independently checked against `KP_CL_002` ("một cháu bé khoảng 18 tháng tuổi tử vong, một cháu bé khoảng 8 tuổi bị thương") — both confirmed as minors; no risk of an adult being wrongly anonymized or a minor being wrongly treated as nameable.
- **No violation found.** This is the one specific failure pattern the QA Policy calls out as having occurred repeatedly elsewhere in this domain (CL-QA-005's mandatory sub-check preamble) — this script does not repeat it.

## Dedicated Re-Verification: O.J. Simpson Beat (per task instruction 3)

Read every sentence of the beat (script lines covering the introduction through the closing "hai cây thước" passage) in isolation, specifically checking for any sentence that states or implies a single unified guilt conclusion:

- "một bồi thẩm đoàn hình sự tại California tuyên bố O.J. Simpson trắng án cho hai tội danh giết người" — states acquittal, not guilt. Clean.
- "Đây là bản án hình sự cuối cùng" — factual, no guilt implication.
- "một bồi thẩm đoàn khác... đi đến một kết luận khác: Simpson phải chịu trách nhiệm dân sự cho cái chết của hai nạn nhân, và phải bồi thường 33,5 triệu đô la" — states civil liability specifically, not "ông đã giết người" — correctly scoped to the civil finding.
- "Đây không phải là tòa dân sự 'sửa sai' cho tòa hình sự... cả hai câu trả lời đều đúng" — explicitly blocks the "civil trial corrected the criminal one" reading that would tip toward guilt.
- The "hai cây thước đo" metaphor — neutral, does not favor either verdict.
- "Vậy: Simpson có tội hay không có tội?" followed by "nó phụ thuộc vào việc bạn đang hỏi tòa án nào. Về mặt hình sự... ông chưa từng bị kết án giết người. Về mặt dân sự, ông đã bị tuyên phải chịu trách nhiệm và bồi thường. Cả hai điều đó cùng tồn tại, không loại trừ nhau, không gộp lại thành một kết luận duy nhất." — **this is the beat's actual ending line**, and it explicitly refuses to resolve into a single conclusion, explicitly names both sides, and explicitly states they do not merge. This is the strongest possible compliant ending for this beat.
- The one sentence that comes closest to a risk — "để trích riêng câu kết luận của phiên tòa dân sự — rằng ông 'đã thực hiện' hành vi đó — và biến nó thành một tuyên bố tội hình sự mà nó không hề là" — is itself a warning against doing exactly that, not an instance of doing it. It does not present this as a quotation the episode itself uses; it explicitly frames it as the trap to avoid.
- **Verdict: no sentence, read in isolation or in sequence, resolves toward "guilty after all."** The beat ends cleanly in ambiguity, matching the mandatory `CK_CL_001` §2.4 template almost exactly. Only the unsourced "mười hai người" detail (Issue 3) needed a fix, and it was unrelated to the guilt-framing risk.

## Legal-Status Term Usage Audit (task instruction 4)

Traced every occurrence of bị tình nghi / bị can / bị cáo / đã bị kết án through the script in reading order:

1. Beat 1 defines all four in sequence, correctly, as sequential "stations," not synonyms.
2. Beat 3 reuses "bị can" → "bị cáo" transition correctly at the truy tố moment ("một 'bị can'... trở thành một 'bị cáo'").
3. Beat 4 (the sơ thẩm ≠ effective-verdict twist) correctly insists a person stays "bị cáo" through the appeal window and correctly reserves "người đã bị kết án" for post-effective-judgment only.
4. Beat 5's documentary example uses only "Nghi phạm"/"Bị cáo" as the clean-but-misleading dialogue, correctly never "hung thủ."
5. Beat 6 names Lê Văn Luyện and calls him "người đã bị kết án" only after stating the effective-final-judgment reasoning — correct placement, not premature.
6. Beat 7 never applies Vietnamese legal-status terms to Simpson (no "bị cáo"/"bị can" cross-contamination) and correctly uses jurisdiction-appropriate language ("trắng án," "chịu trách nhiệm dân sự") instead.

**No misuse found anywhere in the script.**

## Fact-Tracing Audit (task instruction 5): every number/date/name checked against KP_CL_001/KP_CL_002

| Claim in script | KP source | Match |
|---|---|---|
| Điều 13 BLTTHS near-verbatim quote | `KP_CL_001` Block 4 | Match (near-verbatim, "do luật quy định" paraphrases "do Bộ luật này quy định" — acceptable as "gần nguyên văn," not a blocking deviation) |
| Lê Văn Luyện born 18/10/1993, offense night 24/8/2011, ~54 days short of 18 | `KP_CL_002` | Exact match |
| Location: tiệm vàng, huyện Lục Nam, Bắc Giang | `KP_CL_002` | Exact match |
| Victims: parents deceased, daughter ~18 months deceased, other daughter ~8 years wounded/survived | `KP_CL_002` | Exact match, no names added |
| Motive: cướp tài sản / khó khăn tài chính cá nhân, hedged "theo hồ sơ vụ án" | `KP_CL_002` | Exact match, hedge preserved |
| Sentence: 18 years combined, both instances | `KP_CL_002` | Exact match |
| Điều 74 BLHS 1999 mechanism | `KP_CL_002` | Exact match |
| No specific arrest date or appeal date cited | `KP_CL_002` flags appeal date as single-sourced | Correctly omitted/hedged — script says only "vài ngày sau đó" and does not cite the flagged low-confidence appellate date |
| No 20-day / 15-30-day procedural windows cited as fixed numbers | `KP_CL_001` gap-flags | Correctly avoided everywhere — confirmed via full-text search, zero occurrences |
| O.J. Simpson: Oct 1995 criminal acquittal, 1997 civil verdict, $33.5M | `KP_CL_002` | Exact match |
| Double jeopardy flagged as U.S.-only concept | `KP_CL_002` Production Cautions | Exact match |
| 12-person jury (original) | Not in `KP_CL_001`/`KP_CL_002`/`CK_CL_001` §2.4 | **Fixed — see Issue 3** |
| "Đầy đủ tám bước tố tụng" for Lê Văn Luyện (original) | Contradicted by `KP_CL_002` (no giám đốc thẩm/tái thẩm recorded) | **Fixed — see Issue 1** |

No other invented statute numbers, dates, or sentencing details were found.

## Tone / Anti-Sensationalism Re-Check (task instruction 6)

Re-read Beat 0 in isolation as if it were the only thing a viewer saw. It opens on a deliberately mundane, realistic morning-news scenario (a generic placeholder headline, "vụ án X"), narrated in a measured, reflective register ("Không phải vì bạn ác ý...") rather than an alarmed or accusatory one. The only emotionally charged phrases ("kẻ giết người," "tên sát nhân máu lạnh") are explicitly attributed to hypothetical commenters, immediately followed by the corrective "Nhưng phiên tòa còn chưa bắt đầu" — the opposite of manufactured shock; it is a calm diagnosis of a familiar bad habit. This matches the Series Bible's "documentary guide" register and contains no countdown-of-horror framing, no all-caps dread language, and no real, identifiable case. **Confirmed clean.**

## Word Count / TTS-Cleanliness Check (task instruction 7)

- Final word count: **5,894** words between `<!-- NARRATION_START -->` and `<!-- NARRATION_END -->` — within the 5,200–6,500 target band (target derived from the ~260 wpm TTS calibration in `02_EPISODE_PLANNER.md`).
- Scanned the full narration block for stray markdown/headers/labels that would break a TTS derivation: none found. The block is pure prose paragraphs — no `#` headers, no bullet lists, no bracketed production notes, no beat labels — inside the markers. All structural/production commentary correctly lives in "Editorial Notes" outside the markers.

## Anything Requiring Human Judgment

1. **Confirm Điều 13 BLTTHS paraphrase.** The script renders the quote as "...cho đến khi được chứng minh theo đúng trình tự, thủ tục do luật quy định..." versus `KP_CL_001`'s "...do Bộ luật này quy định..." This is a minor paraphrase of a near-verbatim legal quote flagged by the Research Brief as needing eventual human legal review against the current statute text — recommend a human/legal reviewer confirm the exact statutory wording before this episode locks, per the Research Brief's own "cần rà soát nhân công" item (a).
2. **Confirm no real, currently-newsworthy case coincidentally matches the Beat 0 fictional hook** at time of publication — this was flagged in the Research Brief as item (b) requiring human review closer to publish date, and is outside what a script-text QA pass can verify (it depends on the news cycle at release time, not on the document).
3. **Glossary extension (non-blocking):** recommend adding "Bồi thẩm đoàn (jury)" as its own `DOMAIN_GLOSSARY.md` Section C entry before this term is reused in a future episode, since it currently rides on the general "Common law vs. Civil law" entry rather than having its own definition/rule.
4. This QA pass, `KP_CL_001`, and `KP_CL_002` are all still formally `draft-pending-human-review`/`draft-pending-human-review` status themselves — per the Research Brief's own gating language, official Domain QA/Research QA/Safety QA/Legal QA sign-off (plural reviewers, not just this one independent pass) is still required before this episode is cleared for publication, exactly as `01_RESEARCH_BRIEF.md`'s Research Confidence Summary item (c) states.
