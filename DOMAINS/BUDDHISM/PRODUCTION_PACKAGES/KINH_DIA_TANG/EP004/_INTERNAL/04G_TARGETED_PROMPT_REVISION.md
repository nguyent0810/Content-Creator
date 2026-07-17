# 04G — Targeted Prompt Revision (Phase G, EP004)

**Source of findings:** `04F_HUMAN_PROMPT_AUDIT.md` (independent, read-only audit; not modified by this revision).
**Scope:** In-place rewrite of the `Video prompt:` text for 58 of the 100 shots in `04E_FINAL_VIDEO_PROMPTS.md`. No Shot ID, shot order, Covered Beats/Obligations, timestamp, or total duration (2410.154s) was changed. `04A`–`04D` were not touched.
**Backup:** Full pre-revision snapshot of all 6 target files created before any edit, timestamp `20260716_082207`, in `_ARCHIVE/PIPELINE_BACKUPS/`.

## Summary

| | |
|---|---:|
| Prompts rewritten | 58 |
| Originally REVISION_REQUIRED (all fixed) | 15 |
| Originally PASS_WITH_MINOR_POLISH, fixed (shared root cause with a fix category below) | 43 |
| PASS_WITH_MINOR_POLISH left unchanged (different, unlisted root cause — S018 duration-wording note, S021 beat-boundary pre-emption) | 2 |
| Shot IDs / order / Covered Beats / timestamps / total duration changed | 0 |

## Per-Shot Changelog

Grouped by root cause. Each row: Shot ID — Root Cause — Change Made.

### 1. Unsupported additions (unlicensed invented detail)

| Shot | Root cause | Change |
|---|---|---|
| S002 | "Elderly" age descriptor not in licensed Production Fill | Removed "elderly"; subject is now "a woman" |
| S003 | "Elderly" age descriptor not in licensed Production Fill | Removed "elderly"; subject is now "a man" |
| S011 | "Grief" biases the shot toward one of 5 groups that must stay neutral | Replaced with "a quiet private fatigue that could belong to any of several unspoken reasons" |
| S013 / S014 | Invented "veiled" attribute on a Tier-1 sacred-adjacent figure, not authorized by Production Fill | Removed "veiled"; now "the indistinct maternal presence" |
| S026 | Invented hand-raise gesture duplicating S050's own authorized action, stacked onto the single sourced action | Removed the hand-raise; kept only the sourced action (stepping back) |
| S030 | "Elderly" unlicensed; confirmed "labored breathing" detail had been dropped | Removed "elderly"; restored "her breathing labored" |
| S052 | Emotion softened from confirmed "remorse" to unconfirmed "grief" | Changed "old grief" to "quiet remorse" |
| S081 | "Grown" age descriptor unlicensed; spoken apology added where evidence is gesture-only (see also category 6) | Removed "grown"; kept only the confirmed gesture |

### 2. Forbidden-object naming, even in negation (rewritten to positive-only language)

14 shots named a religiously/violently sensitive noun while negating it. All rewritten to describe only what *is* present, never naming the excluded concept. Priority shots (Tier 1/Tier 4, highest risk) marked ★.

| Shot | Forbidden noun(s) removed | New approach |
|---|---|---|
| S007 | "hell, karma" | "The moment stays exactly what it appears to be: a continued, quiet observation of an ordinary empty room." |
| S028 | "whip, violent gesture" | "Nothing else enters the frame — only the lamp itself, steady and undisturbed." |
| S042 | "physical strike" | "Neither figure is named, and no other image is inserted into the frame beyond this single moment between them." |
| S054 | "statue, shrine architecture, temple exterior" | "The setting stays plain and unadorned, nothing beyond this modest, private act of practice." |
| S055 | negated abstract states ("urgency, fear, guaranteed results") | "The practice continues plain and unadorned, calm and unhurried in its own quiet rhythm." |
| S056 | "large shrine" | "Nothing surrounds it beyond the plainness of the space itself." |
| ★ S060 | "suffering or torment" (beside the Buddha/Đao Lợi assembly — highest-risk single instance in the document) | "The frame stays exactly as reverent and calm as it was before, nothing new entering the composition." |
| S071 | "clock or countdown" | "The scene stays entirely within the plain warmth of the table itself." |
| ★ S084 | "otherworldly," "fire, demonic imagery, punishment" | "The mood is heavy with quiet estrangement, entirely human and domestic, the ordinary house simply grown cold." |
| S085 | "supernatural" | Replaced with concrete physical tells ("hands still, jaws tight, eyes fixed on their plates") plus "The scene reads as an entirely ordinary, strained family meal." |
| S086 | "punishment" | "The tension stays entirely domestic and human throughout." |
| S087 | "violent, supernatural" | "The moment stays quiet and entirely human." |
| ★ S088 | "fire, darkness-as-punishment, symbolic afterlife imagery" | "Nothing else enters the frame — only this plain, wordless visual pause." (also fixed the redundant double camera-sentence — see category 4) |
| S013/S014 | ("veiled" — also listed under category 1) | — |

### 3. Hidden scene-pool reuse (S046, S083, S089)

All three previously centered on an identical visual — a hand freezing before a negative gesture — with no continuity thread linking them. Each rewritten with a distinct body-part emphasis, framing distance, and stated narrative function:

| Shot | New emphasis | Narrative function |
|---|---|---|
| S046 | Seated figure + out-of-focus altar corner in the background (wide, setting-driven) | CONTRAST — generic representative of 6 "stopping" behaviors, anchored to the required altar-corner evidence |
| S083 | Close on face and shoulders releasing a breath | DEVELOP — a parent's active self-regulation of anger toward a child |
| S089 | Medium shot on whole-body posture stiffening then easing | DEVELOP — an anonymous instance of restraint, one of 5 catalogued behaviors |

### 4. Camera wording

- **All 29 occurrences** of the literal phrase "The camera holds" rewritten to varied, subject-shifted phrasing (e.g. "A static composition stays close on...", "A locked, wide frame takes in...", "A slow, static composition rests on..."). The phrase does not appear anywhere in the revised document.
- **S022 / S032 / S046** — the identical 8-word clause "The camera holds in a static, observational frame" (reused verbatim across three unrelated shots) now reads distinctly in each, tied to that shot's own content.
- **S043** — fixed the self-contradictory "holds in a ... push" (static language on a push-in movement) to a clean "The camera pushes in slowly and quietly toward his face."
- **S088** — removed the redundant second "The camera stays static" sentence (an artifact of an earlier automated banned-phrase substitution); now a single camera statement.
- **S018 / S061 / S068 / S077** — fixed the same "content sentence + redundant 'camera stays static' sentence" pattern shared by all the TRANSITION-filler bridging shots, for consistency with the S088 fix. S018's "briefly" (which had contradicted its 31.85s duration) was also removed as part of the same edit.

### 5. Non-renderable meta-commentary

Removed editorial/continuity commentary that explained a shot's structural role instead of describing something visible; replaced with concrete visual description or simple omission (achieving the same safeguard — e.g. anonymity, non-continuity — through what is *not* shown rather than a spoken disclaimer):

| Shot | Removed sentence (paraphrased) | Replacement approach |
|---|---|---|
| S035 | "unconnected to any earlier figures" | Achieved non-continuity by keeping both figures unnamed/unidentified, no meta-statement |
| S046 | "not the father seen earlier" | Distinctness achieved via the altar-corner setting detail (category 3) instead |
| S052 | "the two remain unnamed" | Anonymity achieved by simply not naming them |
| S057 | "a separate person from the one seen lighting incense before" | Distinctness stated via "distinct in dress and setting from the moment before" |
| S059 | "this is a return to reflect on what has already been shown" | Replaced with "letting the reverent atmosphere settle once more" |
| S061 / S068 / S018 / S077 | "as one section prepares to shift" / "gives way to the next" | Reduced to plain description of the static light and empty frame |
| S075 | "the praise from outside belongs to a different time" | Replaced with "only this quiet, solitary moment" |

### 6. Stacked / hedged actions

| Shot | Problem | Fix |
|---|---|---|
| S026 | Invented second action (hand-raise) stacked on the sourced action | Removed (see category 1) |
| S069 | Mother's kitchen fluency shown as a second visible action when the Shot Plan assigns it to narration-only; self-contradictory "unseen ... moves through the kitchen" | Removed the mother's visible action entirely; shot now shows only the father's confirmed single action |
| S074 | Hedged "bandage or medicine" (not one concrete action); pre-empted S075's reveal with an early guilt cue | Resolved to the single confirmed action (administering medicine); removed the guilt cue |
| S081 | Implied spoken apology where evidence is gesture-only | Restricted to the confirmed physical gesture (bowed head) |
| S094 | Hedged "palm or surface" (two alternative stagings) | Committed to a single staging (open palm) |
| S008, S044, S051, S078 | Literal "begins to ..." phrasing (even though each describes a single confirmed action, not a real second action) | Rephrased to direct, unhedged statements ("dissolves," "speaks," "apologizes," "starts ringing") |

### 7. Duration-visual mismatch (S013–S015, S039–S041)

Both sequences previously held one completely frozen composition for their full combined duration while narration moved through several distinct ideas (98.8s for S013–S015; 121.4s for S039–S041). Since 04C/04D confirm no new visual evidence is authorized for the abstract narration spoken during these holds, new subject matter could not be invented — each sequence instead received genuine **camera-only** progression:

- **S013 → S014 → S015**: push-in begins (S013, DEVELOP/establish) → push completes, framing tightens to its closest point (S014, HOLD/develop) → camera eases back, frame widens, preparing for S016's return to the wide hall (S015, HOLD/resolve).
- **S039 → S040 → S041**: locked-off wide establish (S039, DEVELOP/establish) → an almost imperceptible push begins, marking time passing (S040, HOLD/develop) → push arrives at its closest point and settles, preparing the cut to S042 (S041, HOLD/resolve).

Each shot still contains exactly one visible state; only camera behavior changes across the arc. No new characters, symbols, or props were introduced, keeping both sequences compliant with their shots' `productionFills`/`forbiddenAdditions`.

### 8. Tier 1 / Tier 4 positive-only language

- **Tier 1**: S009's ascending crane changed to a level lateral drift (removes the risk of an accidental disrespectful look-down angle over the Buddha figure); S013/S014's "veiled" removed (category 1); S060's "suffering or torment" removed (category 2). All 11 Tier 1 shots re-verified: respectful medium-wide/silhouette framing, no invented dialogue, no historical-accuracy claim, no unsupported figure/costume/architecture/facial detail, no forbidden-tier vocabulary anywhere, positive-only description throughout.
- **Tier 4**: S084–S088 had every forbidden-noun negation removed (category 2); S089 additionally differentiated for scene-pool distinctiveness (category 3). All 6 Tier 4 shots re-verified: content is exclusively ordinary domestic space, strained human relationships, silence/distance/tension — no supernatural, religious-judgment, or punishment imagery named anywhere, positive or negative.

## Independent QA Result (post-revision)

Full metrics in `06_QA_REPORT.md`'s "Phase G — Targeted Prompt Revision QA" section. Summary:

| Metric | Result |
|---|---:|
| prompts rewritten | 58 |
| REVISION_REQUIRED remaining | 0 |
| unsupported additions | 0 |
| forbidden-object names appearing in prompts | 0 |
| hidden scene-pool reuse | 0 |
| meta-commentary sentences | 0 |
| stacked-action prompts | 0 |
| camera-template issues | 0 |
| duration-visual mismatches | 0 |
| unnatural-English prompts | 0 |
| Tier 1 violations | 0 |
| Tier 4 violations | 0 |
| mapping errors | 0 |
| timeline gaps | 0 |
| timeline overlaps | 0 |
| total duration | 2410.154s |

## Final Status

`PASS_READY_FOR_LIMITED_TEST_GENERATION`

Per the governing instructions, this authorizes generating only a small, representative test batch next — not all 100 shots. Suggested test batch: one shot from each Domain Approval Gate tier (e.g. S009 [Tier 1], S038 [Tier 2], S054 [Tier 3], S084 [Tier 4], S095 [Tier 5]) plus a sample of the most heavily revised shots (S060, S084, S088, S046/S083/S089, S013–S015 or S039–S041) to visually confirm the fixes render as intended before any larger run. Timing remains `ESTIMATED_FROM_NARRATION` and must be re-derived once real TTS audio exists; this status is not `READY_FOR_RENDER`.
