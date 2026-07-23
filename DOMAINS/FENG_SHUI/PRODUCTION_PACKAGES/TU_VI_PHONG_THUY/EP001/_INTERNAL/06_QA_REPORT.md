# 06 QA Report — EP001 Audio Script Master (First Independent Domain QA Pass)

| Field | Value |
|---|---|
| File reviewed | `DOMAINS/FENG_SHUI/PRODUCTION_PACKAGES/TU_VI_PHONG_THUY/EP001/_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` |
| Domain | FENG_SHUI (`risk_level: high`) — first production script ever produced for this domain |
| Reviewer | Independent QA agent (did not author the script) |
| Reviewed against | `DOMAIN_GUIDE.md` (full, esp. §4/§4a), `DOMAIN_QA/DOMAIN_QA_POLICY.md` (FS-QA-001–010), `01_RESEARCH_BRIEF.md`, `02_EPISODE_PLANNER.md`, `KP_FS_001_Phong_Thuy.md` (current, post-Khí-correction version), `KP_FS_002_Tu_Vi.md`, `GLOSSARY/DOMAIN_GLOSSARY.md` |
| Full narration read | Yes, word-by-word, between `<!-- NARRATION_START -->` / `<!-- NARRATION_END -->` (lines 37–184) |
| Verdict | **PASS — no blocking issues found (FS-QA-002/004/005/006/007/010 all clear).** One administrative metadata correction applied (see Fixes). No content transform was required. |

---

## Checklist Table (FS-QA-001 through FS-QA-010)

| ID | Category | Result | Notes |
|---|---|---|---|
| FS-QA-001 | Source/school attribution | **PASS** | Loan Đầu, Lý Khí, Bát Trạch, Huyền Không Phi Tinh, Tiên Thiên/Hậu Thiên Bát Quái are each named explicitly and stated as independent systems that "có thể cho khuyến nghị khác nhau, thậm chí trái ngược nhau" — matches `KP_FS_001` Schools section almost verbatim. No claim is presented as universal consensus where schools disagree. |
| FS-QA-002 | No individualized reading (§4/§4a) | **PASS — central check, verified line by line** | No worked chart/floor-plan example is given anywhere in the script (Beat 5 states the promise but supplies zero example, so there is nothing to mistake for a real reading). No "hãy tính," no "nhà bạn," no second-person chart outcome. The one quoted phrase "với ngày sinh của bạn, cuộc đời bạn sẽ..." (line 117) is explicitly quoted as the *forbidden* pattern being warned against, not asserted. §4a's two exempt formats (zodiac-cohort, retrospective deceased/public figure) are correctly previewed (line 125) as future formats, correctly distinguished from a live private reading. The two "bình luận" (comment-section) mentions are both refusals ("kênh sẽ không bao giờ... kể cả khi bạn để lại ngày sinh... trong bình luận"), never invitations. |
| FS-QA-003 | No certainty language (§5) | **PASS** | Grepped all 4 instances of "bạn sẽ" — all are meta-narrative about the viewing experience ("bạn sẽ nghe," "bạn sẽ hiểu," "bạn sẽ có chìa khóa") or the one quoted-as-forbidden example above. No line predicts a specific future outcome for the viewer. |
| FS-QA-004 | Financial boundary (§6) | **PASS** | Cung Tài Bạch is named only descriptively ("nói về chủ đề tiền bạc"), no investment/purchase advice tied to a reading. "Chắc chắn giàu" appears once, quoted as an example of the ad language the mocker figure is reacting against, not asserted by the narrator. |
| FS-QA-005 | Health boundary (§7) | **PASS** | Cung Tật Ách is named only descriptively ("nói về chủ đề sức khỏe"), no diagnosis or health-event claim anywhere. |
| FS-QA-006 | Lifespan/serious-event boundary (§8) | **PASS** | No death/lifespan/crisis-timing content anywhere in the script (searched "qua đời," "chết," "mất năm," "tuổi thọ" — the only hit is the historical-figure case-study reference at line 125, used correctly per §4a Format 2, past tense, no timing claim). |
| FS-QA-007 | Anti-fear-sales (§9) | **PASS** | The scam-model description (Beat 6) is written in a calm, analytical register, explicitly attributed to a real reported pattern ("được báo chí chính thống ghi nhận rộng rãi," no invented statistics), and is followed immediately by the channel's refusal of that model. The closing CTA (line 183) is soft ("Nếu bạn thấy con đường thứ ba này đáng để đi tiếp, series sẽ ở đây") with no urgency/threat framing, and the script explicitly states the channel will never build even its own follow/share request on fear (lines 133, 171). |
| FS-QA-008 | Layered interpretation (§10) | **PASS** | Beat 7 explicitly names and applies all three layers (cultural/historical, traditional-belief, modern-reflective) to both Phong Thủy and Tử Vi, and explicitly refuses to let either layer erase the others ("không có nghĩa khoa học 'chứng minh' truyền thống, và cũng không có nghĩa truyền thống chỉ là 'thật ra chỉ là' tâm lý học"). |
| FS-QA-009 | Terminology consistency | **PASS** | Every FS-specific term used (Âm Dương, Ngũ Hành, Bát Quái, Tiên Thiên/Hậu Thiên, Loan Đầu, Lý Khí, Bát Trạch, Huyền Không Phi Tinh, Tử Vi Đẩu Số, Cung, Mệnh, Tài Bạch, Tật Ách, chính tinh/phụ tinh) is a controlled term already present in `GLOSSARY/DOMAIN_GLOSSARY.md`. No invented terminology found. |
| FS-QA-010 | Forbidden claims (§12) | **PASS** | Both halves of the central misconception are stated and then explicitly negated in the narrator's own voice ("Không phải 'chỉ là mê tín.' Không phải 'đã được khoa học chứng minh.'"). No mockery of the tradition anywhere (Beat 8 explicitly states neither opening figure was mocked, "một lựa chọn có chủ đích"). No school named as "more correct." No named historical-founder attribution (Trần Đoàn, Phục Hy, Văn Vương, Quách Phác, Dương Quân Tùng) appears at all — the script correctly stays at the "nhiều truyền thuyết, chưa xác thực" generality level required for Episode 1, deferring specifics to later seasons. |

---

## §4/§4a Individualized-Reading Deep Check (task-specific re-verification)

Read every example/illustration in the script individually:

- **Beat 1/8 opening figures** — generic, unnamed, explicitly composite ("Cùng một con phố... hai người"), never addressed as "you," never tied to a real identifiable person. Beat 8 explicitly confirms neither is mocked.
- **Bát Trạch/Huyền Không school description (Beat 3)** — describes the *existence* of the two systems and that they can disagree; no Kua-number formula, no worked calculation, no invitation to self-apply either method to the listener's own house.
- **12 Cung mention (Beat 4)** — names only 3 of 12 cung (Mệnh, Tài Bạch, Tật Ách) at the concept level, and immediately, explicitly disclaims individualized use: "những cái tên vừa được nhắc tới... hoàn toàn không phải là để bạn tự tính lá số của mình theo... không bao giờ tính toán chúng cho một người cụ thể nào đang xem tập này" (line 103).
- **Core boundary statement (Beat 5)** — uses only absolute language ("sẽ không bao giờ," "không bao giờ," "kể cả khi... yêu cầu trực tiếp," "kể cả khi bạn để lại ngày sinh, giờ sinh, hay sơ đồ căn nhà... trong bình luận"). No hedge, no softened phrasing, no implied exception.
- **§4a format previews (Beat 5, line 125)** — the zodiac-cohort format is described at cohort level ("xu hướng chung của một nhóm mười hai con giáp, theo mùa hay theo năm") with no individual precision claimed; the retrospective case-study format is described as analysis of "một nhân vật lịch sử đã qua đời từ rất lâu... đã có đầy đủ tư liệu lịch sử" — correctly gated to documented/deceased figures, and the script explicitly reaffirms the core boundary "vẫn nguyên vẹn, không có ngoại lệ nào" for any living viewer.

**Conclusion: no line in this script performs, simulates, or invites an individualized reading.** This is the strongest section of the script and it holds up under adversarial re-reading.

---

## School Attribution Deep Check (task-specific re-verification)

- Loan Đầu vs. Lý Khí: named separately, correctly described (terrain-reading vs. compass/time-based).
- Bát Trạch vs. Huyền Không Phi Tinh: named separately, correctly described as having different bases (birth year vs. construction period/facing), correctly stated as capable of disagreeing on the same house, correctly framed as "không phải hai bước của cùng một quy trình" (matches `KP_FS_001`'s "không cùng một gốc" warning almost exactly).
- Tiên Thiên vs. Hậu Thiên Bát Quái: named separately, correctly stated as "không phải một bảng đúng, một bảng sai," deferred to a future dedicated episode rather than explained in technical depth (correctly avoids the over-depth risk flagged in `02_EPISODE_PLANNER.md`).
- No claim in the script presents any one school's method as universally agreed where the source packets record disagreement.

---

## Khí Passage Check (task-specific re-verification)

The word "khí" appears **exactly once** in the narration, inside the compound "thoáng khí" (well-ventilated/airy), used as a modern-reflective analogy for traditional space-quality intuition (line 153: "nguyên lý truyền thống về một không gian 'thoáng khí, có ánh sáng, có chỗ dựa vững chắc phía sau lưng' nghe rất gần với trực giác hiện đại của chúng ta"). This is consistent with the corrected `KP_FS_001` Khí section's own guidance that ventilation/light is a permitted modern-reflective analogy, explicitly not a claim that ventilation science "proves" Khí or that Khí "is" airflow. The script does not otherwise define, name-check, or dive into Khí as a concept — correct for Episode 1, since Khí's full treatment is reserved for Episode 4 per the production plan. **No claim that Khí is a measured physical energy anywhere in the script.**

---

## Scientific-Proof / "Pure Superstition" Binary Check (task-specific re-verification)

Both halves of the central misconception are explicitly stated as the two things being corrected, then explicitly negated in the narrator's own voice, back to back:

> "Phong Thủy không phải là một điều đã được khoa học chứng minh... Nhưng Phong Thủy cũng không phải là một mớ niềm tin tùy tiện, không có cấu trúc, không có logic nội tại nào cả." (Beat 3)
> "Không phải 'chỉ là mê tín.' Không phải 'đã được khoa học chứng minh.'" (Beat 7 closing)

Both directions are corrected, not just one — this satisfies Task 5 of this review precisely (many first drafts in this kind of content over-correct only the "it's just superstition" half and accidentally under-correct the "science has proven it" half, or vice versa; this script does not have that asymmetry).

---

## Fear-Sales / CTA Check (task-specific re-verification)

- Scam-market description (Beat 6): qualitative only, no invented figures, calm/analytical register, immediately followed by explicit refusal of the model.
- Warning-sign guidance (Beat 6): framed as self-protection ("để tự bảo vệ mình"), not accusation of any named party, and not itself alarmist.
- Closing CTA (Beat 8, line 183): soft invitation to continue the series, no urgency, no threat, no "like/subscribe or miss out" framing. The script additionally makes an explicit meta-commitment that the channel's own CTAs will never be built on fear (lines 133, 171) — this is a stronger-than-required compliance, not just a passing one.

---

## Word Count / TTS-Derivation Check

- Target band per `02_EPISODE_PLANNER.md`: 6,000–6,500 words (mid-point of the 5,200–7,300 overall range).
- Narration-only text (between markers) word count, verified independently via Python tokenization and via `tr -s ' \n' '\n' | grep -c .` (both methods agree): **6,173 words** — inside the target band.
- Note: the file's frontmatter previously declared `word_count: 6456`, computed with a tool that (in this environment) miscounts Vietnamese UTF-8 text via `wc -w` (verified: `wc -w` on the identical extracted text returns 6455 while byte-literal-delimiter tokenization and Python's `.split()` both independently return 6173 — a locale/tooling artifact, not a real discrepancy in the text). **Fix applied:** corrected `word_count` in the script's frontmatter from `6456` to `6173` to reflect the verified count. This did not require a content transform, only a metadata correction. Both the old and new figures are within the 6,000–6,500 target band, so this had no bearing on the PASS verdict.
- No stray markdown headers, bullet lists, tables, or bracketed production labels found between `NARRATION_START`/`NARRATION_END` — the narration text is clean prose throughout and safe for direct TTS derivation.

---

## Issues Found and Fixes Applied

### Fix 1 — Frontmatter word-count metadata correction (administrative, non-content)

**Location:** Line 14, YAML frontmatter.

**Before:** `word_count: 6456`

**After:** `word_count: 6173`

**Reason:** The declared count did not match the actual narration word count under verified tokenization (see Word Count check above). This is a metadata-accuracy fix, not a §14 content transform — no narration text was altered.

**No other fixes were required.** No blocking claim-type violation (FS-QA-002/004/005/006/007/010) was found anywhere in the script, so no §14 transform was needed.

---

## Anything Requiring Human Judgment

1. **Both source Knowledge Packets remain `draft-pending-human-review`.** Per `01_RESEARCH_BRIEF.md`'s own instruction, this script should be re-checked once `KP_FS_001` and `KP_FS_002` formally clear Domain QA/Research QA/Safety QA/Historical QA — this QA pass confirms the script is faithful to the *current* content of both packets (including the corrected Khí section) but cannot substitute for that packet-level sign-off, which is a human/process gate outside this script review's scope.
2. **Stylistic, not compliance, observation:** the script leans on the Buddhism-domain comparison ("Kinh Phật có một bộ kinh gốc...", line 77) as a rhetorical device to explain FS's lack of a single canonical text. This is accurate and low-risk, but a human editor may want to confirm it reads naturally in the finished cut rather than as a cross-domain aside — this is a taste call, not a QA failure.
3. No other item requires escalation. This script is unusually disciplined for a first-ever domain script: the core boundary (§4/§4a) is stated twice (an early preview plus the full Beat 5 declaration) with no softening in either instance, and the writer appears to have actively self-audited against the forbidden-pattern list (e.g., explicitly quoting the "bạn sẽ..." pattern only to label it as what must never be said).
