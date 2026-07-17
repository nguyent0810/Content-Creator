# 04I — Limited Test Generation & Output Review (Phase I, EP004)

## Status: GENERATION NOT YET PERFORMED — this document is a ready-to-use generation package and evaluation template, not a results report

**Why:** Phase I requires actually calling a video-generation model to produce 12 `.mp4` files and then inspecting the real frames for anatomy stability, temporal stability, camera compliance, and Tier 1/Tier 4 domain safety. No video-generation tool or API (Runway, Veo, Sora, Pika, ComfyUI, or similar) is available in this session. Writing PASS/FAIL judgments, seeds, actual durations, or frame-level observations without a real video to inspect would be fabricated QA — exactly the "false PASS from an unverified process" failure this project's Phase 1 audit exists to eliminate. This document does not do that.

**What this document is instead:** (1) the exact, verbatim, execution-ordered generation package for the 12 Phase H shots, ready to hand to any video-generation tool; (2) the complete per-shot evaluation template — every field the task requires — left as `PENDING` for a human (or a future session with real tool access) to fill in against actual generated output; (3) the acceptance-gate logic, unevaluated until real data exists.

**Next step:** generate the 12 clips with the prompts below (same model/version/aspect ratio/settings across the whole batch, in the execution order given), save them to `_INTERNAL/LIMITED_TEST_GENERATION/EP004/` using the exact filenames specified, then return so each clip can be reviewed against the rubric and this document updated with real findings.

**Output directory (created, currently empty):** `_INTERNAL/LIMITED_TEST_GENERATION/EP004/`

---

## 1. Generation Package (12 shots, execution order)

Rules for whoever runs the generator:
- Use the prompt text **exactly as written below** — copied verbatim from `04E_FINAL_VIDEO_PROMPTS.md`; do not edit before this first attempt.
- Use the **same model, model version, aspect ratio, and generation settings** for all 12 clips.
- Record the actual model/version/settings/seed used (if the tool exposes a seed) — needed for the evaluation table in Section 2.
- **One attempt per shot** for this first pass — do not regenerate on sight of a flaw; that judgment call belongs to the evaluation step (Section 3), not the generation step.
- If the tool cannot produce the shot's full target duration, generate the maximum duration the tool supports and record that limitation explicitly — do not claim the full duration was tested if it wasn't.
- **Stop the batch early** if any of the following appears during generation: a `PIPELINE_BLOCKER`-level result, a serious Tier 1 violation, a serious Tier 4 violation, a prompt that is truncated or passed incorrectly by the tool, or output that doesn't correspond to the intended Shot ID.
- Filename convention: `<ShotID>_attempt01.mp4` (e.g. `S084_attempt01.mp4`), saved into `_INTERNAL/LIMITED_TEST_GENERATION/EP004/`.

| # | Shot ID | Target timeline (from 04D) | Target duration | Expected output filename |
|---|---|---|---:|---|
| 1 | S084 | 00:34:41.077 → 00:35:18.000 | 36.92s | `S084_attempt01.mp4` |
| 2 | S088 | 00:35:57.692 → 00:36:10.154 | 12.46s | `S088_attempt01.mp4` |
| 3 | S089 | 00:36:10.154 → 00:36:35.539 | 25.38s | `S089_attempt01.mp4` |
| 4 | S060 | 00:24:12.000 → 00:24:45.692 | 33.69s | `S060_attempt01.mp4` |
| 5 | S014 | 00:04:52.154 → 00:05:25.846 | 33.69s | `S014_attempt01.mp4` |
| 6 | S046 | 00:18:37.385 → 00:19:10.154 | 32.77s | `S046_attempt01.mp4` |
| 7 | S083 | 00:34:06.923 → 00:34:41.077 | 34.15s | `S083_attempt01.mp4` |
| 8 | S042 | 00:17:11.077 → 00:17:48.000 | 36.92s | `S042_attempt01.mp4` |
| 9 | S074 | 00:29:21.231 → 00:29:36.369 | 15.14s | `S074_attempt01.mp4` |
| 10 | S078 | 00:31:12.462 → 00:31:48.923 | 36.46s | `S078_attempt01.mp4` |
| 11 | S001 | 00:00:00.000 → 00:00:07.846 | 7.85s | `S001_attempt01.mp4` |
| 12 | S095 | 00:38:04.616 → 00:38:18.203 | 13.59s | `S095_attempt01.mp4` |

Note: these target durations (2410.154s total across the full episode) are `ESTIMATED_FROM_NARRATION`, not audio-aligned — treat them as pacing guidance for the test clip, not a hard technical requirement if the generator's native clip-length options don't line up exactly.

### 1.1 — S084 (Tier 4, high risk)

> Inside an ordinary home, several family members sit apart in their own corners of the room, none of them looking at one another. A slow, static wide shot of the house takes in the distance between each person. Flat, cool interior light fills the space, giving no warmth. The mood is heavy with quiet estrangement, entirely human and domestic, the ordinary house simply grown cold.

### 1.2 — S088 (Tier 4, high risk)

> A fixed, unmoving shot rests on soft, undefined light, pausing quietly between one idea and its opposite. Nothing else enters the frame — only this plain, wordless visual pause.

### 1.3 — S089 (Tier 4, high risk + scene-pool differentiation check)

> A person's whole posture stiffens for a moment, shoulders and hands drawing inward as if catching themselves right before a harsh word or gesture, then easing back to stillness. A static, medium shot takes in the full figure through this moment of restraint. Soft, even light fills the frame. The harsh act itself is never shown — only the visible choice to stop before it happens.

### 1.4 — S060 (Tier 1)

> The same hall continues to hold, unchanged, the camera static and undisturbed. The gold-white light remains steady and even. The frame stays exactly as reverent and calm as it was before, nothing new entering the composition.

### 1.5 — S014 (Tier 1 + long-shot progression check)

> The gesture continues to hold, the teaching figure's hand still extended toward the indistinct maternal presence. The camera's slow push from the previous shot settles to a close, complete framing on the gesture, coming to rest just short of any facial detail. The gold-white light deepens slightly around the two figures. The composition remains reverent and unhurried, without introducing any new symbol to illustrate the surrounding teaching.

### 1.6 — S046 (Tier 3, triple-fix / scene-pool)

> An unnamed figure sits in a plain room, one hand stopping mid-motion in a small, private moment of restraint, the corner of a modest home altar visible but out of focus in the far background. A steady, wide observational frame takes in the person and the quiet room together. Warm, low light fills the space. The stillness carries a general sense of catching oneself before a habitual moment, ordinary and unremarkable rather than tied to any single story.

### 1.7 — S083 (scene-pool differentiation + long shot)

> A parent's shoulders rise and fall in one slow, deliberate breath, their expression easing from tight to calm just before a sharp gesture would have followed. A close, unmoving shot stays on the parent's face and shoulders as they exhale slowly. Even, quiet light fills the frame. The moment is entirely about the visible release of tension, not about what almost happened.

### 1.8 — S042 (Continuity Thread T3, opening shot)

> A father raises his voice sharply at his young child in the plain front room of a modest home, the words landing hard. The child flinches and lowers their face. In the same breath, something shifts in the father's own expression — a flicker of recognition, as though he has heard this voice before. A subtle, handheld documentary movement stays close, feeling the tension without exaggerating it. Warm but uneasy lamp light fills the room. Neither figure is named, and no other image is inserted into the frame beyond this single moment between them.

### 1.9 — S074 (caregiver)

> A caregiver administers medicine to their mother with practiced, tired hands, evening light through the window marking the hour. A still, observational frame takes in the scene. Warm but weary domestic light fills the room. Fatigue sits plainly in the caregiver's tired, careful movements.

### 1.10 — S078 (modern life)

> A person stiffens and glances away as a nearby phone starts ringing, their body drawing inward. A static, close composition stays on the visible tension. Even, cool light fills the room. No specific words are shown, and no other figure is shown speaking the phrase running through their mind.

### 1.11 — S001 (chair motif, short shot, unrevised baseline)

> A single wooden chair stands empty in a modest Vietnamese home, positioned near a window. No one is seated, and no one has just left. The shot is still and unhurried, contemplative in its quiet. Warm late-afternoon light falls softly across the chair, casting a gentle amber tone through the room. The mood is quiet and unresolved, neither sad nor comforting. No text, no logos, no watermarks, no photographs or flowers added near the chair.

### 1.12 — S095 (chair continuity + ritual/lamp, unrevised baseline)

> A person sits down before the same familiar wooden chair and lights a small lamp beside it. Static and unhurried, the shot settles close on the small flame catching. Warm, gentle light spreads from the lamp across the room. The mood is quiet and resolved, neither performative nor elaborate. No incense or altar is added to the scene.

---

## 2. Batch Generation Log — PENDING

| Field | Value |
|---|---|
| Model / version | *PENDING — fill in after generation* |
| Aspect ratio | *PENDING* |
| Other generation settings (resolution, guidance scale, etc.) | *PENDING* |
| Seed(s) (if supported/recorded per clip) | *PENDING* |
| Shots attempted | *PENDING (target: 12)* |
| Shots completed | *PENDING* |
| Batch stopped early? | *PENDING — record which early-stop condition triggered, if any* |
| Any duration limitation encountered | *PENDING — record per-shot if the generator could not reach the target duration* |

---

## 3. Per-Shot Evaluation — PENDING (template; all fields to be completed against real output)

For each shot, once its `.mp4` exists in `_INTERNAL/LIMITED_TEST_GENERATION/EP004/`, complete this block by direct frame-by-frame inspection of the actual video — not by re-reading the prompt.

Fields per shot (repeat for all 12, in execution order S084, S088, S089, S060, S014, S046, S083, S042, S074, S078, S001, S095):

```
Shot ID:
Output file:
Model/settings:
Generation attempt:
Actual generated duration:
Narration–visual alignment:
Subject/action accuracy:
Single-action readability:
Natural motion:
Camera compliance:
Character continuity:
Object continuity:
Setting continuity:
Anatomy stability:
Temporal stability:
Domain safety:
Overall usability:
Final status: [PASS | PASS_WITH_PROMPT_POLISH | REGENERATE_SAME_PROMPT | PROMPT_REVISION_REQUIRED | PIPELINE_BLOCKER]
Evidence: [specific timestamp(s)/frame description(s) in the actual clip supporting the status]
Root-cause classification: [MODEL_RANDOMNESS | PROMPT_AMBIGUITY | PROMPT_CONFLICT | CONTINUITY_FAILURE | DOMAIN_SAFETY_FAILURE | GENERATION_PIPELINE_FAILURE | UNKNOWN]
```

**Status/root-cause decision rules (from the governing instructions, for whoever completes this):**
- `REGENERATE_SAME_PROMPT` — prompt is clear and correctly sourced; the defect is anatomy/flicker/motion/composition randomness; no similar pattern across multiple shots.
- `PROMPT_REVISION_REQUIRED` — the model visibly misread a genuinely ambiguous part of the prompt; the prompt has competing subjects/actions; a camera instruction is self-contradictory; or the same failure pattern recurs across multiple shots of the same type.
- Do not regenerate to paper over a real prompt defect — a repeated pattern must be logged as `PROMPT_REVISION_REQUIRED`, not silently retried away.
- Any confirmed Tier 1 or Tier 4 forbidden depiction is always `PIPELINE_BLOCKER`, never `MODEL_RANDOMNESS`/`REGENERATE_SAME_PROMPT`, regardless of how it looks in a single frame.

### 3.1 Tier 1 Gate (S060, S014) — PENDING, must be checked directly against actual frames

| Check | S060 | S014 |
|---|---|---|
| Respectful medium/wide framing maintained | PENDING | PENDING |
| Sacred figure not shown in frontal close-up | PENDING | PENDING |
| No invented dialogue or visible text | PENDING | PENDING |
| Restrained, non-spectacular celestial environment | PENDING | PENDING |
| No excessive fantasy spectacle | PENDING | PENDING |
| **Tier 1 gate result** | PENDING | PENDING |

### 3.2 Tier 4 Gate (S084, S088, S089) — PENDING, must be checked directly against actual frames

| Check | S084 | S088 | S089 |
|---|---|---|---|
| Ordinary, realistic domestic setting | PENDING | PENDING | PENDING |
| Human distance / psychological tension only | PENDING | PENDING | PENDING |
| No supernatural interpretation | PENDING | PENDING | PENDING |
| No religious/punishment imagery | PENDING | PENDING | PENDING |
| No sensational horror tone | PENDING | PENDING | PENDING |
| **Tier 4 gate result** | PENDING | PENDING | PENDING |

---

## 4. Acceptance Gate — CANNOT BE EVALUATED YET

The gate requires real per-shot results:

```
PIPELINE_BLOCKER: 0
Tier 1 violations: 0
Tier 4 violations: 0
semantic mismatches: 0
≥10/12 shots at PASS or PASS_WITH_PROMPT_POLISH
PROMPT_REVISION_REQUIRED: ≤2
```

Until Section 3 is filled in with real evaluations, the conclusion must remain **PENDING** — reporting `PASS_READY_FOR_EXPANDED_TEST_GENERATION` (or any of the fallback conclusions `TARGETED_PROMPT_REVISION_REQUIRED` / `GENERATOR_RETRY_REQUIRED` / `PIPELINE_FIX_REQUIRED`) without real data would be an unverified claim.

---

## 5. Final Report — PENDING

```
shots attempted: PENDING
shots completed: PENDING
PASS: PENDING
PASS_WITH_PROMPT_POLISH: PENDING
REGENERATE_SAME_PROMPT: PENDING
PROMPT_REVISION_REQUIRED: PENDING
PIPELINE_BLOCKER: PENDING
Tier 1 results: PENDING
Tier 4 results: PENDING
semantic mismatches: PENDING
continuity failures: PENDING
generator-specific failures: PENDING
acceptance-gate result: PENDING
recommended next action: PENDING
```

## 6. Constraints Honored

`04A`–`04H`, narration, TTS, and the final prompt text in `04E_FINAL_VIDEO_PROMPTS.md` were not modified. No video was rendered by this session (no tool available). No full 100-shot batch was attempted. This is the only report created in this phase. No Git command was used.
