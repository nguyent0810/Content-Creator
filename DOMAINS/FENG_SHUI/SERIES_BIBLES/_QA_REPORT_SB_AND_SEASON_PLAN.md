# Independent QA Report — SB_FS_001, SEASON_01_PRODUCTION_PLAN, CK_FS_001

**Domain:** FENG_SHUI (`FS`) — risk_level: high
**Reviewer:** Independent QA pass (did not author any reviewed document)
**Date:** 2026-07-23
**Documents in scope:** `SB_FS_001_Tu_Vi_Phong_Thuy.md`, `SEASON_01_PRODUCTION_PLAN.md`, `CK_FS_001_Tu_Vi_Phong_Thuy.md`, cross-checked against `DOMAIN_GUIDE.md`, `DOMAIN_QA_POLICY.md`, and skimmed against `KP_FS_001_Phong_Thuy.md` / `KP_FS_002_Tu_Vi.md`.
**Overall verdict: PASS, with 6 issues found and fixed directly (blocking-adjacent editorial/accuracy issues, not §6/7/8 hard-boundary violations) and 1 item flagged for human/production follow-up.**

No violation of `DOMAIN_GUIDE.md` §6 (financial), §7 (health), or §8 (lifespan/death) claim-type locks was found in either binding document. No individualized-reading (§4) violation was found in SB_FS_001 or SEASON_01_PRODUCTION_PLAN.md. One CK_FS_001 metaphor and five CK_FS_001 hook lines were adjusted as a precaution (see below) — none were confirmed hard violations, but all sat closer to the line than they needed to given the source material's own stated rules.

---

## (a) Checklist items that PASSED

1. **Episode Catalog cross-check (Task 1).** All 17 rows of SB_FS_001's Episode Catalog table (Ep, Core Question, Hiểu Lầm Trung Tâm) were compared word-for-word against the corresponding 17 sections of `SEASON_01_PRODUCTION_PLAN.md`. Core Question fields match exactly in all 17 episodes. Hiểu Lầm Trung Tâm fields match exactly or (in Ep001, Ep002) the catalog table carries a verbatim first sentence of the Season Plan's fuller field with an elaboration clause dropped — this is intentional table-summarization, not drift, since the retained sentence is character-for-character identical. No renumbering, retitling, or reassignment found.
2. **Episode 4 (Khí) and Episode 15/16 cross-references (Task 2).** SB_FS_001's Season Architecture text ("no dedicated episode defined Khí... now Episode 4," "no episode demonstrated the whole system... now Episode 16, paired with Episode 15") matches the Season Plan's Tập 4 "vai trò" field (which names Tập 6, 9, 11, and the 15-16 pair as the five episodes that reference Khí forward) and the Season Plan's own "Cross-Episode Continuity Notes" (which independently lists the same five: Tập 6, 9, 11, 15, 16). The Episode 16 Ground Rule (fictional/composite house only) is stated identically in both SB_FS_001 (Season Architecture) and the Season Plan (Tập 16, field 4). Bridge language between Ep15→Ep16 and the "do not produce Ep16 without reading Ep15's finished script first" instruction is internally consistent.
3. **Rủi ro nội dung — specific-section requirement (Task 3), 14 of 17 episodes on first pass.** Episodes 1–13 and 17 all name a specific `DOMAIN_GUIDE.md` section number (§3, §4, §5, §6, §6-7, §9, §10, §12, or a combination) alongside a concrete, written-out transformed sentence — none of these are vague "be careful" placeholders. (Episodes 14–16 required a fix; see part (b)/(c) below.)
4. **Rhythm Rule — the two three-episode Nền tảng runs themselves (Task 4).** The claim "two runs of three consecutive Nền tảng episodes exist... Ep002-004 and Ep010-012... no run exceeds three" is factually correct against the actual 17-episode rhythm sequence (verified episode-by-episode: 001 Mở đầu, 002-004 Nền tảng ×3, 005 Mở đầu, 006 Ứng dụng, 007-008 Nền tảng ×2, 009 Ứng dụng, 010-012 Nền tảng ×3, 013 Ứng dụng/Myth-bust, 014 Đào sâu, 015 Tranh luận, 016 Case-study, 017 Kết mùa). No run of Nền tảng exceeds three anywhere in the sequence. (The "immediately followed by" clause required a fix; see below.)
5. **CK_FS_001 claim-type locks (Task 5), broad pass.** Across ~250 metaphors (M001-M132), ~250 story hooks, ~120 story angles, and the "Forbidden Creative Patterns" section, the overwhelming majority of financial (Cung Tài Bạch, wealth-corner, vật phẩm) and health/lifespan-adjacent (Cung Tật Ách, Cục, Vận) material stays firmly on the illustrative/non-guarantee side of §6-8 — e.g. M042 ("Cung Tật Ách as a smoke detector, not a death sentence"), M098 ("Cung Tài Bạch as a garden bed, not a vending machine"), M058-059 (direction as tailwind/headwind, "not a guarantee"), and an explicit "Guaranteed-Outcome Bait" forbidden-patterns section that independently bans exactly this failure mode. Only one metaphor (M050) needed a wording fix (below).
6. **Individualized-reading drift (Task 6), broad pass.** SB_FS_001 and SEASON_01_PRODUCTION_PLAN.md hooks consistently use fictional couples, generic/hypothetical "if someone told you..." framing (e.g. Ep3, Ep7's rhetorical "bạn"), or explicitly-labeled fictional/historical chart examples — never a calculated real chart framed as "your chart." CK_FS_001's own "Individualized-Reading Bait" forbidden-patterns section explicitly bans "framing any illustrative example as 'your chart' or 'nhà của bạn.'" Five hook lines in CK_FS_001's Story Hooks library (H101-H105) used exactly that "your chart / your Cục / your direction" phrasing and were corrected (below) to bring them in line with the packet's own rule.
7. Terminology, school-naming discipline (§2-3), and the three-layer interpretation framework (§10) are consistently present and were not found violated anywhere in the two binding documents.

---

## (b) Issues found and (c) exact fixes applied

### Issue 1 — Rhythm Rule's "immediately followed by" claim was inaccurate (Task 4)
**File:** `SB_FS_001_Tu_Vi_Phong_Thuy.md`, Season 1 Rhythm Rule.
**Problem:** The Rhythm Rule states each 3-episode Nền tảng run "is immediately followed by a change of mode (Ứng dụng, Đào sâu, or Tranh luận)." That is true for the second run (Ep012 → Ep013 Ứng dụng/Myth-bust), but **false** for the first run: Ep004 is immediately followed by **Ep005, which is rhythm type "Mở đầu"** (opening the Tử Vi track) — not Ứng dụng, Đào sâu, or Tranh luận. Ep006 (Ứng dụng) only arrives one episode later. This looks like a leftover from before Ep004 ("Khí") was inserted into the season during the 15→17 revision, and was not re-verified against the final sequence. This is precisely the class of error the task asked me to check for ("was this broken by a later edit").
**Before:** *"...each run is immediately followed by a change of mode (Ứng dụng, Đào sâu, or Tranh luận), so no run exceeds three..."*
**After:** *"...each run is immediately followed by a change of mode: Ep004 gives way to Ep005's Mở đầu (opening the Tử Vi track) and then Ep006's Ứng dụng, while Ep012 gives way directly to Ep013's Ứng dụng/Myth-bust beat — so no run exceeds three..."*
**Status:** Fixed directly in `SB_FS_001_Tu_Vi_Phong_Thuy.md`.

### Issue 2 — Episodes 14, 15, 16 "rủi ro nội dung" fields lacked a specific Domain Guide section citation (Task 3)
**File:** `SEASON_01_PRODUCTION_PLAN.md`.
**Problem:** Unlike every other episode, Episodes 14 (Cung Mệnh/Thân), 15 (Bát Trạch vs. Huyền Không), and 16 (case-study) had a concrete transform sentence but named no specific `DOMAIN_GUIDE.md` §-number — a real (if narrow) miss against the task's explicit requirement that every risk field "name a SPECIFIC Domain Guide section."
**Fixes applied (before → after, abbreviated):**
- **Ep014:** *"Rủi ro là trình bày Cung Thân như một công thức tính chắc chắn..."* → added *"— vi phạm nguyên tắc nguồn/độ tin cậy của `DOMAIN_GUIDE.md` §3 và ngôn ngữ chắc chắn bị cấm ở §5."*
- **Ep015:** *"Rủi ro là ngầm chọn phe hoặc gợi ý một trong hai chuyên gia đang 'lừa đảo'..."* → added *"— vi phạm yêu cầu không trình bày một trường phái là 'đúng duy nhất' của `DOMAIN_GUIDE.md` §2-3 và nguyên tắc giữ cả ba lớp đọc của §10."*
- **Ep016:** *"Rủi ro cao nhất là vô tình khiến ví dụ trông giống một nhà thật..."* → added *"(vi phạm ranh giới ví dụ-hư-cấu-bắt buộc của `DOMAIN_GUIDE.md` §4 và Episode 16 Ground Rule của `SB_FS_001`)"* and *"(vi phạm §2-3/§10 về đa trường phái và ba lớp đọc)"* at the relevant clauses.
**Status:** Fixed directly in `SEASON_01_PRODUCTION_PLAN.md`.

**Advisory (not fixed, not blocking):** Ep008 and Ep009's risk fields cite `§14` (the transform-process section) but not the specific substantive lock (§7/§8 for Ep008's Cung Tật Ách, §9 for Ep009's fear-tone risk) even though those locks are unambiguous from the surrounding text. The transform in both is already concrete and correct in substance — this is a minor completeness/cross-reference style gap, not a missing transform, so it was left as an observation rather than an edit.

### Issue 3 — Knowledge Dependencies section (Long-term Knowledge Roadmap) used stale, pre-revision episode numbers and one claim directly contradicted the document's own Continuity Notes
**File:** `SB_FS_001_Tu_Vi_Phong_Thuy.md`, "Long-term Knowledge Roadmap → Knowledge Dependencies" (this is a distinct section from the Episode Catalog table, found while tracing Task 1/2's cross-references).
**Problem:** Three paragraphs referenced episode numbers that predate the 15→17 revision (which inserted Ep004 "Khí" and Ep016's case-study) and were never updated:
- *"Tử Vi cung/sao episodes (EP007, EP009, EP012)... depend on... Thiên Can/Địa Chi (EP006)... lá số... established in EP004"* — EP006 is actually "Hướng Nhà" (Phong Thủy) and EP004 is "Khí," neither of which is what the sentence meant; EP009 ("Bàn Thờ, Bếp, Cửa Chính") is Phong Thủy, not a "Tử Vi cung/sao" episode.
- *"Phong Thủy school-comparison episodes (EP010)... depend on... Bát Quái (EP005)"* — EP010 **is** the Bát Quái episode itself, not a school-comparison episode; the actual school-comparison episodes are EP015-016.
- *"Applied home-Phong-Thủy episodes (EP011, EP013, EP014)... depend on... Bát Quái (EP005), for EP011 specifically"* — EP014 is a **Tử Vi** episode (Cung Mệnh/Thân), not Phong Thủy, and the claim that EP011 (Loan Đầu) depends on Bát Quái **directly contradicts** this same document's own Cross-Episode Continuity Notes, which state Loan Đầu is "độc lập với la bàn/Bát Quái về mặt lịch sử — không ngụ ý Tập 11 phụ thuộc Tập 10."
**Status:** Fixed directly — all three paragraphs corrected to current canonical numbering (EP008/EP012 for Tử Vi cung/sao; EP015-016 for school-comparison depending on EP010; EP006/EP009/EP013 for applied home-Phong-Thủy), with the EP011-does-not-depend-on-Bát-Quái correction made explicit and cross-referenced to the Continuity Notes it was contradicting. Each corrected paragraph carries an inline dated note explaining what was wrong and why, for traceability.

### Issue 4 — Season Plan's supplementary research note for Tập 4 (Khí) was stale relative to KP_FS_001
**File:** `SEASON_01_PRODUCTION_PLAN.md`, "Ghi Chú Nghiên Cứu Bổ Sung."
**Problem:** This note claims "`KP_FS_001` không có một mục 'Khái niệm nền tảng' riêng cho Khí theo đúng định dạng... đã dùng cho Âm Dương, Ngũ Hành, Bát Quái, Loan Đầu, Bát Trạch, Huyền Không." A direct read of `KP_FS_001_Phong_Thuy.md` (lines 310-345) shows it now **does** contain a full "## Khí (Qi/Chi — Traditional Environmental Flow, Not Physics Energy)" section in exactly that Knowledge function/Primary concepts/Narrative detail/Script-ready material/Production cautions format — the gap this note flagged has already been closed at the Knowledge Packet level, but the Season Plan's coordination note was never updated to match, and would have misled a future writer into thinking they needed to commission new research that already exists.
**Status:** Fixed directly — note rewritten to point writers at `KP_FS_001`'s existing Khí section instead of recommending redundant research.

### Issue 5 — CK_FS_001 metaphor M050 used "true medicine" language adjacent to a §7 health-cure claim
**File:** `CK_FS_001_Tu_Vi_Phong_Thuy.md`, Metaphor Library.
**Problem:** *"a 'cure' that is really just decluttering as a placebo that happens to also be true medicine"* — the phrase "true medicine" risks reading as an actual medical-efficacy claim for a Phong Thủy-adjacent practice, which is the exact claim type §7 and the packet's own "Guaranteed-Outcome Bait" section prohibit (a metaphor illustrating a concept is fine; one that implies decluttering is literally medicine is not).
**Before:** *"M050. a 'cure' that is really just decluttering as a placebo that happens to also be true medicine."*
**After:** *"M050. a 'cure' that is really just decluttering as a placebo whose side effect happens to be real calm (not a medical claim — the calm is real, the 'cure' framing is not)."*
**Status:** Fixed directly in `CK_FS_001_Tu_Vi_Phong_Thuy.md`.

### Issue 6 — CK_FS_001 Story Hooks H101-H105 used "your chart"/"your Cục"/"your direction" framing that the same packet's own rule forbids (Task 6)
**File:** `CK_FS_001_Tu_Vi_Phong_Thuy.md`, Story Hooks.
**Problem:** The packet's own "Forbidden Creative Patterns → Individualized-Reading Bait" section bans "Framing any illustrative example as 'your chart' or 'nhà của bạn.'" Five hook lines did exactly that:
**Before:**
> H101. What if your "bad Cục" year was actually just a hard year?
> H102. What if your unlucky direction is asking for a rearranged room, not a new house?
> H103. What if your chart's flattering line is the one to question hardest?
> H104. What if your family's rule is asking for a source, not obedience?
> H105. What if your anxiety about money is asking for a budget, not a charm?

**After (hook energy preserved, second-person specific-chart framing removed):**
> H101. What if a "bad Cục" year is usually just a hard year?
> H102. What if an unlucky direction is asking for a rearranged room, not a new house?
> H103. What if a chart's flattering line is the one worth questioning hardest?
> H104. What if a family's rule is asking for a source, not obedience?
> H105. What if anxiety about money is asking for a budget, not a charm?

**Status:** Fixed directly in `CK_FS_001_Tu_Vi_Phong_Thuy.md`. Note: these were graded as a precautionary fix, not a confirmed §4 violation — the hooks were phrased as open questions, not asserted outcomes, and Reflection Questions elsewhere in the same packet legitimately use first-person "my chart" framing for private self-reflection (explicitly scoped by CTA003 as a "private exercise," never performed on-screen). But Story Hooks are written to be spoken on-screen, where "your chart" reads differently than a private reflection prompt, and the packet's own forbidden-patterns list singles out exactly this phrase — so the inconsistency was real and worth closing.

---

## (d) Items requiring human judgment (not fixed by this QA pass)

1. **CK_FS_001 has no dedicated Episode 16 section, despite SB_FS_001 claiming both Ep004 and Ep016 "draw on CK_FS_001 sections added specifically for them."** Verified via full-text search: CK_FS_001 contains a clearly-labeled "Khí — Metaphor & Hook Extension (Episode 4)" block (M121-M132) but no equivalent "Nhà số 7" / Episode 16 block anywhere in the packet. This is a genuine content gap, not just a documentation error — closing it means a human writer or the creative-knowledge author needs to actually draft a dedicated Episode 16 metaphor/hook set (mirroring the Ep004 pattern), which is production work outside a QA reviewer's remit. As an interim fix, I corrected SB_FS_001's claim so it no longer overstates what currently exists (see Issue in SB_FS_001's Episode Catalog intro note) and flagged the outstanding gap there for whoever produces Episode 16's script.
2. **Ep008/Ep009 risk-field citation completeness** (noted as advisory above) — left as a judgment call for the production team on whether to tighten every field to cite the exact §-number versus accepting §14-plus-context as sufficient, since the transforms themselves are already correct and concrete.
3. **KP_FS_001 / KP_FS_002 sourcing itself** was only skimmed per the task's scope (other reviewers cover KP-level sourcing in parallel) — this report does not certify KP-level source discipline, only that the Season Plan's and Series Bible's *references* to KP content were internally consistent with what a skim found.
