# 04F — Independent Human-Style Prompt Audit (Phase E, EP004)

**Scope:** Direct, read-only quality audit of the 100 final video prompts produced in Phase E. This audit does not trust the `PASS_READY_FOR_HUMAN_PROMPT_REVIEW` status or QA counts recorded in `06_QA_REPORT.md` — every claim below was independently re-derived from the source files on disk (`04C_SHOT_PLAN.md`, `04D_SHOT_TIMING_AND_PRODUCTION_FILL.md`, `04E_FINAL_VIDEO_PROMPTS.md`, `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt`, `04_VIDEO_PROMPT_TIMELINE.json`). No prompt, and no 04A–04E file, was modified in the course of this audit. No video was rendered.

**Method:** Section 1 (mapping/consistency) was verified by parsing all five source files fresh from disk with an independent script and diffing them field-by-field. Section 2 (per-prompt audit) was performed by four independent reviewers working from the raw Shot Plan ground truth with no access to each other's conclusions, each auditing 25 prompts sentence-by-sentence; a fifth independent pass then re-checked their combined output against the source files, added several findings the four reviewers missed, and reversed one reviewer flag that did not survive verification. Sections 3–7 (diversity, camera language, duration, domain, English) were audited holistically across all 100 prompts using direct text extraction and manual sentence-level reading, not string-hash comparison.

---

## 1. Mapping and Consistency

| Check | Result |
|---|---|
| 100 prompts ↔ S001–S100 | **PASS** — 100/100, no gaps |
| Prompt-number sequencing (S001→001 … S100→100) | **PASS** — 0 mapping errors |
| Timeline matches 04D (per-shot start/end) | **PASS** — 0 mismatches across all 100 shots |
| Timeline gaps | **PASS** — 0 |
| Timeline overlaps | **PASS** — 0 |
| Covered Beats / Covered Obligations match 04C | **PASS** — 0 mismatches |
| 04E vs OUTPUT.txt (video prompt text, narration, timeline) | **PASS** — byte-identical across all 100 blocks |
| 04E vs `04_VIDEO_PROMPT_TIMELINE.json` (video prompt text, shot order) | **PASS** — identical across all 100 entries |
| Missing Shot IDs | **0** |
| Duplicate Shot IDs | **0** |
| Reordered Shot IDs | **0** |

**Conclusion: Section 1 is fully clean.** The mechanical scaffolding of Phase E (mapping, timing inheritance, cross-file consistency) is correct and independently verified — this part of the prior QA's claim holds up.

---

## 2. Per-Prompt Audit (all 100)

Aggregate result:

| Status | Count |
|---|---:|
| PASS | 68 |
| PASS_WITH_MINOR_POLISH | 17 |
| REVISION_REQUIRED | 15 |
| CRITICAL_BLOCKER | 0 |

**0 CRITICAL_BLOCKER** — no prompt depicts forbidden religious content, no prompt contains an unrenderable instruction that would simply fail, and no prompt asserts a fabricated fact as source evidence with no basis at all. The defects found are real but narrower: unauthorized micro-details, hedged/ambiguous staging, self-contradiction, non-renderable meta-commentary, and a prompt-craft risk pattern (naming forbidden content even while negating it) concentrated in the religiously-sensitive tiers.

### REVISION_REQUIRED (15)

| Prompt | Shot | Problem | Evidence from 04C/04D | Why it matters | Recommended direction |
|---|---|---|---|---|---|
| 002 | S002 | Mother described as "elderly" — an unconfirmed age/appearance detail. | `productionFills`: only clothing/vegetable-type/lighting; `forbiddenAdditions`: "không đặc tả... ngoại hình cụ thể của mẹ." | Locks in a specific trait for a character the plan intends to keep a universal, unspecified archetype. | Drop "elderly"; stay within licensed fills only. |
| 003 | S003 | Father described as "elderly" — same issue as S002. | `productionFills`/`forbiddenAdditions` as above, mirrored for the father. | Same as S002. | Drop "elderly." |
| 011 | S011 | Stillness is framed as "grief," which reads as the bereaved-child group specifically. | `forbiddenAdditions`: must use one neutral fatigue signal representing 5 groups, "không chọn thiên vị một nhóm." | Biases the image toward one of five groups the plan explicitly says must not be favored. | Replace "grief" with a neutral fatigue/stillness description. |
| 013 | S013 | Invents a "veiled" maternal figure — an unlicensed costume detail on a Tier-1 sacred-adjacent figure. | `productionFills`: "không có mới ngoài Production Fill đã dùng ở S009," which authorizes only architecture/assembly, not a veil. | Adds an invented visual attribute to a religiously-sensitive figure with no source basis. | Keep the mother's presence indistinct; drop "veiled." |
| 026 | S026 | Adds an invented hand-raise gesture stacked onto the sourced action; this gesture is also the authorized action of a different shot (S050). | `oneAction`: "lùi lại một bước" (step back) only. S050's own action is the hand-raise. | Adds an unconfirmed second action and blurs two shots meant to show different boundary behaviors. | Keep only the step-back; remove the hand-raise. |
| 042 | S042 | Names and negates "physical strike" in an already-tense staged scene. | `forbiddenAdditions`: "không mô tả hành vi bạo lực thể chất" — one of the strictest per-shot bans in the plan. | Naming the exact forbidden act, even negated, in a physically tense scene is a real risk of the prohibited content appearing on render. | Describe only the raised voice and the child's flinch; remove the "no physical strike" sentence rather than stating it. |
| 054 | S054 | Names "statue, shrine architecture, temple exterior" while negating them. | `forbiddenAdditions`: "không mô tả không gian 'chùa' cụ thể" (Tier 3, domain-gated). | Text-to-video models often attend to named nouns regardless of negation; this raises the odds of rendering the excluded temple imagery. | Describe only the plain room and the practice; never name the excluded architecture. |
| 056 | S056 | Names "large shrine, abundance of offerings" while negating them. | `forbiddenAdditions`: "không dựng bàn thờ lớn." | Same risk as S054, for the shot whose entire point is contrast with an ornate altar. | Describe only the humble single incense stick without naming shrine imagery. |
| 060 | S060 | Names "suffering or torment" while negating them, directly beside the Buddha/Đao Lợi assembly. | `forbiddenAdditions`: "không tự vẽ hình ảnh địa ngục ở beat này" — the project's single strictest religious-safety boundary. | This is the highest-risk prompt-craft choice in the whole document: naming hell-adjacent imagery, even negated, next to a sacred figure. | Describe only the calm, unchanged hall; never introduce the concept of suffering/torment, positive or negative. |
| 069 | S069 | Visualizes the mother's kitchen fluency, which is explicitly narration-only per the shot design; also self-contradictory ("unseen" + a described visible action). | `oneAction`: father fixes a bulb (visible); "mẹ biết bếp còn gì mang bằng giọng đọc" (mother's fact is voice-only). | Shows more than the design authorizes, and a video model cannot resolve "unseen ... moves through the kitchen." | Omit the mother's visible action, or keep her as indistinct non-active background only. |
| 071 | S071 | Names "clock or countdown imagery" while negating it. | `forbiddenAdditions`: "không dựng hình ảnh 'cuộc đua'/đồng hồ đếm ngược." | Risks the model literally placing a clock/countdown — the exact anxious imagery the shot exists to avoid. | Describe the warm, unhurried meal directly; never reference clocks/countdowns. |
| 074 | S074 | Action hedged as "bandage or medicine" (not one concrete action); also shows "a quiet trace of guilt," which is explicitly reserved for the next shot's REVEAL. | `oneAction`: "thay thuốc cho mẹ" (medicine only); S075 is the dedicated REVEAL shot for the inner feeling. | A model can't render two unrelated actions as one instruction; showing the guilt early flattens the two-shot reveal structure. | Specify medicine only; remove the guilt cue, reserving it for S075. |
| 081 | S081 | Father "speaks an apology" — adds audible speech to evidence that is gesture-only. | `requiredEvidence`: "cử chỉ cha xin lỗi con" (gesture); `oneAction`: "cúi đầu" (bows head). | This documentary format has no dialogue track; sibling shots (S078, S096) deliberately avoid voicing unconfirmed words for the same reason. | Restrict to the physical gesture; remove implied speech. |
| 088 | S088 | Two consecutive sentences both state the camera is static: "The camera holds a fixed position, resting..." immediately followed by "The camera stays static." | Direct read of the deployed text — a leftover artifact of the automated banned-phrase substitution pass applied during Phase E polish. | Redundant back-to-back camera-stillness statements read as an unedited mechanical splice, in one of the highest-stakes Tier 4 shots. | Delete the second, redundant sentence. |
| 094 | S094 | Offers two alternative stagings joined by "or" ("held in an open palm or resting on a plain surface") instead of one concrete scene. | `productionFills`: palm/surface are two options to choose *between* at composition time, not to leave unresolved in the final text. | A single generation call needs one unambiguous scene; "or" risks an inconsistent or blended render. | Commit to exactly one placement. |

### PASS_WITH_MINOR_POLISH (17)

| Prompt | Shot | Problem (brief) |
|---|---|---|
| 009 | S009 | Rising crane move risks ending in a look-down angle over the Buddha figure — should explicitly stay level/medium-wide (Tier 1). |
| 018 | S018 | Calls a 31.85s hold "briefly" — a minor internal contradiction with its actual duration. |
| 021 | S021 | "Almost theatrical" lighting pre-empts the "stage/performance" metaphor that belongs to the next shot (S022)'s narration. |
| 028 | S028 | Names "whip" even while negating it (Tier 4-adjacent metaphor risk, lower severity than the REVISION_REQUIRED cases). |
| 030 | S030 | Drops the confirmed "labored breathing" detail in favor of generic weakness; adds unconfirmed "elderly." |
| 035 | S035 | "Unconnected to any earlier figures" is a non-renderable meta/continuity annotation. |
| 043 | S043 | "The camera holds in a slow, quiet push" is internally contradictory (holds = static, push = movement). |
| 046 | S046 | "Not the father seen earlier" is a non-renderable meta/continuity annotation. |
| 052 | S052 | "Trace of old grief" should be "remorse/regret" per source; "the two remain unnamed" is non-renderable meta text. |
| 055 | S055 | Negates abstract states ("urgency, fear, a promise of guaranteed results") instead of describing the scene positively. |
| 057 | S057 | "A separate person from the one seen lighting incense" is a non-renderable meta/continuity annotation. |
| 059 | S059 | "This is a return to reflect on what has already been shown" is non-renderable editorial commentary. |
| 061 | S061 | "As one section of the film prepares to shift" is non-renderable filler describing documentary structure. |
| 068 | S068 | Same template filler as S061 ("as one section gives way to the next"). |
| 075 | S075 | "The praise from outside belongs to a different time" is non-renderable editorial commentary. |
| 083 | S083 | "Frames the hand and the breath" treats breath as a directly framable subject without a concrete visual proxy. |
| 085 | S085 | "Visibly holding some private anger" is vague emotional shorthand without a concrete physical anchor. |

### PASS (68)

All remaining prompts (S001, S004–S008, S010, S012, S014–S017, S019, S020, S022–S025, S027, S029, S031–S034, S036–S041, S044, S045, S047–S051, S053, S058, S062–S067, S070, S072, S073, S076–S080, S082, S084, S086, S087, S089–S093, S095–S100) were checked sentence-by-sentence against `requiredEvidence`, `productionFills`, `forbiddenAdditions`, and `continuityIn/Out` and found free of defects at the per-prompt level.

### Cross-cutting pattern found in Section 2: naming forbidden content even while negating it

Beyond the individual REVISION_REQUIRED cases above, a broader pattern was found: **24 of the 100 prompts** contain a "No X, no Y..." sentence that names the specific excluded noun rather than simply omitting it. Most of these are low-risk (e.g., S001 "no photographs or flowers," S094 "no soil, no planting hands"), but a subset sits directly on the project's highest-stakes religious-safety boundaries: **S060** ("suffering or torment," beside Buddha/Đao Lợi), **S054/S056** (temple/shrine architecture), **S084/S088** ("fire, demonic imagery, punishment," the Tier 4 hell-metaphor core), **S028/S042** (whip, physical strike). Naming a forbidden concept and then negating it is a known real risk for text-to-video generation, since these models frequently attend to the named noun regardless of the negation. This is not a semantic error in what the prompt *says* — every one of these sentences is factually compliant — but it is a legitimate rendering-risk finding a grammar/keyword QA pass cannot catch, and it concentrates precisely where the project's own Domain Approval Gate says the risk must be lowest.

---

## 3. Visual Diversity / Scene-Pool Audit

Semantic comparison (subject / action / setting / narrative function only, ignoring camera, lighting, emotion, continuity boilerplate, and negative constraints) across all 100 shots:

**Legitimate, Shot-Plan-required continuity (not scene-pool reuse):**
- **Chair (Thread T1)** — 13 shots (S001, S005–S008, S033, S038, S067, S095–S097, S099–S100). Every recurrence has a `continuityIn`/`continuityOut` tag citing T1 and a distinct narrative function (establish → passage of time → hold → dissolve → callback/anchor → resolution → final fade). This is the show's designed spine motif, not a fallback.
- **Đao Lợi celestial hall (Thread T2)** — 11 shots (S009, S010, S012–S017, S034, S059, S060), all Domain-Gate Tier 1, each with a distinct function (establish, hold, gesture, hold, exact callback, hold, summary callback, hold). Legitimate per-design reuse.
- **Father story (Thread T3)** — S042–S047, each carrying the sequence forward (outburst → stillness → apology → hold → generic-representative variant explicitly marked as NOT the same person). Legitimate.

**No hits found** on the literal banned motifs "blank note," "closed door," "phone hesitation" (as a fallback filler — see below), "temple courtyard," "celestial assembly" (used only for the legitimate T2 thread), "caregiver bedside" (each caregiving shot has a distinct character/context, correctly marked "not linked to" earlier caregiver figures per 04C).

**Real finding — hidden scene-pool reuse not covered by any declared continuity thread:**

A "hand stops mid-motion before a negative gesture, then relents" visual is used **three separate times** with no continuity thread linking them and no cross-reference to each other in 04C: **S046** (representative "stopping" gesture, CONTRAST, ~19 min mark), **S083** (parent restraining anger, DEVELOP, ~34 min mark), **S089** (restraint before one of "5 negative behaviors," DEVELOP, ~36 min mark). Each is independently justified by its own beat's narration, and 04C explicitly marks each as a *new*, unconnected subject — so this is not a false-continuity violation. But visually, a viewer would see the same close-up "hand freezes, then eases back" shot three times within roughly 20 minutes of runtime with no narrative acknowledgment that it is a repeated device. This is exactly the "different wording, same visual meaning" pattern the audit was asked to catch. **Severity: moderate** — no forbidden content, no false continuity claim, but a genuine visual-distinctiveness gap that the per-shot Domain/Forbidden-Addition checks (which operate shot-by-shot) cannot catch on their own.

**Minor, lower-severity observation:** two "lone generic seated figure, quiet unspecified room" shots (S011 — five-groups abstract representative; S039 — compassion's origin) share a similar setup (single seated figure, muted room, no named identity). This is likely acceptable, since both are deliberately abstract, representative visualizations for non-visualizable narration content (per the System Spec's Abstract/Symbolic visualization allowance) — flagged here only as a borderline case, not a defect.

**Phone-related shots (S019, S049, S062, S072, S078)** were checked individually: each has a distinct narrative function (avoidant call-ending / texting-instead-of-calling / calm resolved practice / attentive long-distance listening / tensing at a ringing phone) and distinct staging. Not scene-pool reuse.

---

## 4. Camera-Language Audit ("The camera holds")

29 prompts contain the literal string "The camera holds." Classification:

| Class | Count | Shots |
|---|---:|---|
| Natural and necessary (tied to shot function — CALLBACK exact-echo, or explicitly justified by content) | 9 | S008, S016, S059 (CALLBACK exact-echo, camera must not move by design), S004, S026, S030, S037, S084, S086 (static choice explicitly tied to described content/composition) |
| Acceptable but repetitive (generic, but not wrong) | 17 | S022, S032, S035, S046, S049, S054, S063, S065, S067, S070, S072, S075, S078, S081, S092, S094, S096, S099 |
| Mechanical template (genuine defect) | 3 | S043 (self-contradictory "holds in a ... push"), S088 (redundant double camera-stillness statement, see Section 2), and the exact 8-word clause **"The camera holds in a static, observational frame."** reused byte-for-byte across S022, S032, and S046 — three unrelated shots (a performative-grief memorial shot, an empty hospital corridor, and a hand-stop restraint shot) with zero content-specific variation in the camera clause |

**Additional finding beyond the literal 29:** a broader "camera stays static" pattern (not caught by a search for "camera holds" alone) affects 5 of the 6 abstract TRANSITION filler shots (S018, S061, S068, S077, S088; S098 was already fixed in an earlier polish pass and is clean). Each pairs a first sentence describing the visual content holding still with a second, largely redundant sentence stating "The camera stays static." Because these six shots are legitimately near-content-free bridging shots (04C confirms `—` for all content fields), some family resemblance between them is expected and acceptable; but the *internal* two-sentence redundancy within each individual prompt is a real, fixable natural-English defect, most severe in S088 (already listed as REVISION_REQUIRED in Section 2) where both redundant sentences literally use the word "camera."

**Conclusion:** the 29→ reduction done in the prior polish pass was real progress (verified: 0 of the 29 are byte-identical to each other), but "not identical" is not the same as "not mechanical" — the audit found 3 genuinely mechanical instances (S022/S032/S046's identical clause, S043's contradiction, S088's redundancy) that a full-string-duplicate check would never surface, plus a lower-severity structural echo across the 6 TRANSITION filler shots.

---

## 5. Duration Suitability

`04D`'s own Duration Review (section 3.2) checked and confirmed no *single* shot exceeds 60s. That check is correct on its own terms but does not catch **consecutive shots holding the identical unchanging visual** — which is exactly what this audit was asked to check ("prompt không yêu cầu giữ một hình ảnh gần như tĩnh quá lâu"). Two such chains were found:

| Chain | Total duration | Content held static throughout | Narration spoken during the hold |
|---|---:|---|---|
| **S039 → S040 → S041** | **121.4s** (48.92 + 41.54 + 30.92) | A single seated figure with a distant, tender gaze — explicitly "unchanged," "extending the earlier stillness," "no new action" in all three prompts | Three substantively different ideas: compassion's origin in personal grief; a critique of filial piety that doesn't extend to others; self-reflective questions about repeating generational harm |
| **S013 → S014 → S015** | **98.8s** (28.62 + 33.69 + 36.46) | The Buddha's gesture toward the mother, held motionless — Tier 1 sensitive | Three distinct philosophical passages: enlightenment doesn't mean coldness; the distinction between attachment and love; four separate definitions (attachment/gratitude/repayment/compassion) |

Both are marked `DURATION_VISUAL_MISMATCH`. Over 2 minutes of a single frozen portrait, and nearly 100 seconds of a frozen Tier-1 gesture, while substantially different ideas are narrated, exceeds what a "hold" can reasonably carry — a viewer would be watching a still image for that entire span. This is a shot-plan/timing-methodology consequence (word-count-proportional timing applied to dense philosophical narration mapped onto a HOLD shot function), not a Phase E prompt-composition error — the prompts accurately and honestly describe what the shot plan specifies (they even correctly refuse to invent new visual content to fill the time, which is the right compositional choice given the constraint). The mismatch is upstream in 04C/04D's shot-boundary decisions for these two passages, surfaced here for visibility since Phase E is expressly forbidden from silently altering 04A–04D. **This is reported as a blocker to flag, not as a Phase E authoring defect.**

**Milder, lower-severity observation:** S005–S006–S007 (chair silence, 61.4s combined, of which 54.9s is explicitly "unchanged") is a comparable but less severe case — softened by being the opening emotional beat of the whole episode and by S005 containing a genuine subtle visual change (dust settling).

**Short shots reviewed:** the shortest shots (S063 at 2.77s, S043 at 3.23s, S035/S065 at 4.15s, S062/S064 at 5.08s) were each checked for a readable single action within their duration; all pass — each is a single, simple, instantly-legible gesture (sitting to eat, a stopped body, a brief presence, a phone call posture, an apology gesture), consistent with 04D's own justification for keeping them short (the rapid "6 small practices" sequence's designed pacing).

**No multi-action-stacking-for-duration issues** were found beyond what's already listed in Section 2 (S026, S069, S074 — flagged there for other reasons that also touch duration/action-count).

---

## 6. Domain Audit (Tier 1 and Tier 4, full manual review)

### Tier 1 — Đức Phật, thân mẫu, Cung Trời Đao Lợi (11 shots: S009, S010, S012–S017, S034, S059, S060)

All 11 read directly. Compliant on: no frontal close-up (all explicitly "no facial close-up," "no frontal close-up of the face"), no invented dialogue (all explicitly "no dialogue is implied/suggested"), no claim of historical/architectural accuracy (S009: "architecture is rendered as softly symbolic rather than a claim of historical accuracy"), no fantasy spectacle, respectful medium-wide/silhouette framing throughout.

Two findings already listed in Section 2 apply here: **S009**'s ascending crane risks ending in a disrespectful look-down angle (PASS_WITH_MINOR_POLISH); **S013**'s invented "veiled" maternal-figure detail is unlicensed (REVISION_REQUIRED); **S060** names "suffering or torment" in negation immediately beside the sacred assembly — the single highest religious-safety risk found in this audit (REVISION_REQUIRED).

### Tier 4 — "Địa ngục" as psychological metaphor (6 shots: S084–S089)

All 6 read directly, word-for-word. This is the strongest-complying block in the whole document: every shot explicitly and correctly frames the content as ordinary domestic estrangement ("an ordinary house grown cold, not any otherworldly place," "entirely domestic and human," "a strained, ordinary meal," "only the quiet failure to reach out," "the harsh act itself is never shown") and every shot that touches the absolute ban explicitly negates supernatural imagery (S084: "no fire, no demonic imagery, no punishment of any kind"; S088: "no fire, darkness-as-punishment, or symbolic afterlife imagery"). No supernatural hell, no demons, no fire-as-punishment, no chains, no torture, no gore, no religious-judgment spectacle found anywhere in this block — **0 forbidden depictions**.

The one defect found in this block is **S088**'s redundant double camera-stillness sentence (Section 2/4) — an English/mechanical-template defect, not a religious-safety defect. The "naming forbidden imagery in negation" risk pattern (Section 2) does apply to S084 and S088 specifically, since they are the two shots that explicitly name "fire," "demonic," "punishment," "torment" — even though every occurrence is grammatically a negation, this is flagged as the highest-priority item for human re-check before any test render, given this tier's zero-tolerance status.

### Tier 2, 3, 5 (spot-checked, not the audit's mandatory focus but reviewed for completeness)

Tier 2 (Địa Tạng Bồ Tát named but never shown — S038, S061): both compliant, no form/costume/symbol depicted. Tier 3 (generic ritual — S021, S046, S047, S054, S056): S054 and S056 flagged in Section 2 for naming forbidden shrine imagery; S021 and S047 clean. Tier 5 (closing lamp/joined-palms — S095, S096): both compliant, no extra ritual gesture added, inner words not shown as on-screen text.

**Tier 1 violations: 0. Tier 4 violations: 0.** (Both tiers pass on literal content; the naming-in-negation risk pattern is reported as a prompt-craft risk factor, not a confirmed violation, per the distinction drawn in Section 2.)

---

## 7. English Audit

Beyond grammar (which was already clean per the prior QA pass), this audit looked specifically for: awkward-but-grammatical phrasing, template-fragment splicing, unclear subject/action, redundant meaning, non-renderable production instructions, over-clausal sentences, and vague wording.

- **Vague wording** ("ordinary object," "visible action," "symbolic space" used without being made concrete): **0 literal hits** — the composer avoided these specific phrases entirely.
- **Non-renderable meta/editorial commentary** (sentences that describe the prompt's own structural role rather than anything a camera could see): **9 instances** — S035, S046, S052 (partial), S057, S059, S061, S068, S075, and implicitly S018's duration-description mismatch. All already listed individually in Section 2 as PASS_WITH_MINOR_POLISH. Pattern: sentences like "This is a return to reflect on what has already been shown," "the two remain unnamed," "not the father seen earlier" try to enforce a Forbidden-Addition or Continuity constraint by *narrating* the constraint rather than achieving it through concrete visual description — a real technique problem, low individual severity, but recurring enough to be worth a systemic fix pass.
- **Redundant meaning** (two sentences saying the same thing): 1 clear case, **S088** (Section 2/4), plus the milder structural echo across the 5 other TRANSITION filler shots (Section 4).
- **Internally contradictory phrasing**: **S043** ("holds in a ... push" — Section 2/4).
- **Unclear subject/action needing a concrete visual proxy**: **S083** ("frames ... the breath"), **S085** ("visibly holding some private anger") — both listed in Section 2.
- **Hedged/unresolved either-or staging** (not one concrete scene): **S074** ("bandage or medicine"), **S094** ("palm or surface") — both REVISION_REQUIRED in Section 2.
- **Over-clausal sentences**: not found as a distinct problem — sentence structure throughout stays within one or two clauses per idea.

---

## 8. Conclusion

| Metric | Value |
|---|---:|
| total prompts reviewed | 100 |
| PASS | 68 |
| PASS_WITH_MINOR_POLISH | 17 |
| REVISION_REQUIRED | 15 |
| CRITICAL_BLOCKER | 0 |
| semantic mismatches (narration visualizes something unrelated to source) | 0 |
| hidden scene-pool reuse (motif repeated with no continuity-thread justification) | 1 pattern, 3 shots (S046, S083, S089 — "hand-stop restraint" visual) |
| unnatural-English prompts (redundant meaning, contradiction, non-renderable meta text, unresolved either-or) | 13 (S035, S043, S046, S052, S057, S059, S061, S068, S074, S075, S083, S085, S088 — some already counted under REVISION_REQUIRED above) |
| camera-template issues (mechanical, not just repetitive) | 3 (S022/S032/S046 identical clause as one pattern, S043, S088) |
| duration-visual mismatches | 2 chains (S013–S015, S039–S041), 1 milder observation (S005–S007) |
| continuity violations (false or broken continuity claims) | 0 |
| unsupported additions (invented detail beyond licensed Production Fill) | 6 (S002, S003, S011, S013, S026, S081) |
| Tier 1 violations (confirmed, literal) | 0 |
| Tier 4 violations (confirmed, literal) | 0 |

**Note on the PASS-gate arithmetic:** the user-specified gate for `READY_FOR_LIMITED_TEST_GENERATION` requires `CRITICAL_BLOCKER: 0` (met), `semantic mismatch: 0` (met), `domain violation: 0` (met on literal content), `unsupported addition: 0` (**not met — 6 found**), and `scene-pool reuse nghiêm trọng: 0` (**not met — 1 pattern, 3 shots found, of moderate-not-severe severity**). Since two of the five gate conditions are not satisfied, the top verdict is not available regardless of the otherwise-strong 68% clean-PASS rate.

At the same time, none of the findings amount to an architectural failure: mapping/timeline/traceability is perfect (Section 1), the domain-safety literal content is clean (Section 6), and every defect found is narrow, specific, and independently listable against a named shot and a named Shot-Plan field — exactly the shape of a targeted revision list, not a sign that the composition approach itself is broken.

## FINAL STATUS: `TARGETED_PROMPT_REVISION_REQUIRED`

**Priority order for the targeted revision pass:**
1. **S060, S084, S088** — highest priority. Remove or rephrase the "naming forbidden imagery in negation" sentences on the episode's single strictest religious-safety boundary (Tier 4 hell-metaphor / Tier 1 adjacency), and fix S088's redundant double camera-sentence.
2. **S054, S056, S071, S028, S042** — same "naming forbidden imagery in negation" pattern on Tier 3 and other strict-forbidden-addition shots.
3. **S013, S026, S069, S074, S081, S094** — unauthorized invented detail, stacked/hedged actions, or narration-only content shown visually.
4. **S002, S003, S011** — unlicensed generic-character descriptors (age, emotion-bias).
5. **S046, S083, S089** — resolve the hidden "hand-stop restraint" scene-pool reuse by differentiating at least one of the three visually (different framing, body part emphasis, or setting detail) so they read as distinct moments rather than the same shot recurring.
6. **S035, S046, S052, S057, S059, S061, S068, S075** — replace non-renderable meta/continuity commentary with concrete visual differentiation.
7. **S009, S018, S021, S030, S043, S055** — minor polish items as individually described in Section 2.
8. Report to a human, but do not silently fix: the two duration-visual mismatch chains (S013–S015, S039–S041), since correcting them may require a 04C/04D shot-boundary change outside Phase E's authority.

Even after this revision pass, per the user's own instruction, only a small representative test batch should be generated next — not all 100 shots — with priority given to one shot from each of the five Domain Approval Gate tiers plus a sample of the revised shots above.
