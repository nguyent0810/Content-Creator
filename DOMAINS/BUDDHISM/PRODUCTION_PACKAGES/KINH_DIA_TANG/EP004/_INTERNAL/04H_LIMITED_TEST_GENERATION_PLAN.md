# 04H — Limited Test Generation Plan (Phase H, EP004)

**Purpose:** Select and sequence a small, representative subset of the 100 Phase E/G prompts for actual test video generation, so that real model output can be evaluated before any larger render is authorized. This document is a **plan only** — no video is generated here, no prompt text is altered, and `04A`–`04G` are unmodified.

**Sources read:** `04C_SHOT_PLAN.md`, `04D_SHOT_TIMING_AND_PRODUCTION_FILL.md`, `04E_FINAL_VIDEO_PROMPTS.md`, `04F_HUMAN_PROMPT_AUDIT.md`, `04G_TARGETED_PROMPT_REVISION.md`, `OUTPUT/04_VIDEO_CREATE_PROMPTS.txt`.

**Gate this plan operates under:** Phase G ended at `PASS_READY_FOR_LIMITED_TEST_GENERATION`, which explicitly authorizes only a small representative test batch, not a full 100-shot render. This document defines that batch.

---

## 1. Selected Shots (12) and Coverage Matrix

| Shot ID | Prompt # | Duration | Domain Tier | Chair motif | Modern life | Caregiver | Father continuity (T3) | Ritual/altar/lamp | Short shot | Long shot w/ progression | Prior scene-pool reuse | Phase G revised? |
|---|---|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| S084 | 084 | 36.92s | Tier 4 | | | | | | | | | ✅ |
| S088 | 088 | 12.46s | Tier 4 | | | | | | | | | ✅ |
| S089 | 089 | 25.38s | Tier 4 | | | | | | | | ✅ | ✅ |
| S060 | 060 | 33.69s | Tier 1 | | | | | | | | | ✅ |
| S014 | 014 | 33.69s | Tier 1 | | | | | | | ✅ | | ✅ |
| S046 | 046 | 32.77s | Tier 3 | | | | | ✅ | | | ✅ | ✅ |
| S083 | 083 | 34.15s | — | | | | | | | ✅ | ✅ | ✅ |
| S042 | 042 | 36.92s | — | | | | ✅ | | | | | ✅ |
| S074 | 074 | 15.14s | — | | | ✅ | | | | | | ✅ |
| S078 | 078 | 36.46s | — | | ✅ | | | | | | | ✅ |
| S001 | 001 | 7.85s | — | ✅ | | | | | ✅ | | | (baseline, unrevised) |
| S095 | 095 | 13.59s | Tier 5 | ✅ | | | | ✅ | | | | (baseline, unrevised) |

**Coverage check against the required list:**

| Required category | Satisfied by |
|---|---|
| Motif chiếc ghế | S001 (establish), S095 (T1 continuity, 6th callback) |
| Đời sống hiện đại | S078 (phone call triggers a stress response) |
| Caregiver | S074 |
| Continuity người cha (T3) | S042 (opens Thread T3) |
| 2 shot Tier 1 — Đức Phật/Đao Lợi | S060, S014 |
| 2 shot Tier 4 — "địa ngục" tâm lý | S084, S088 (S089 is a 3rd Tier 4 shot, included for its scene-pool role) |
| Nghi lễ/bàn thờ/ngọn đèn | S095 (lamp, primary), S046 (altar corner, background evidence) |
| Shot ngắn | S001 (7.85s) |
| Shot dài có progression | S014 (part of the Phase G camera-only progression fix for the S013–S015 sequence) |
| Shot từng bị scene-pool reuse | S046, S083, S089 (all three shots the 04F audit found sharing one "hand freezes before a negative gesture" visual, since differentiated in Phase G) |

**Mandatory priority shots from the task instruction** (S046, S060, S083, S084, S088, S089): all 6 present in the selection above.

Two shots (S001, S095) were deliberately kept as **unrevised baselines** — they passed Phase F's audit without any Phase G change — so the test batch also confirms the pipeline produces good output on prompts that never needed fixing, not only on the repaired ones.

---

## 2. Execution Order

Ordered to surface a pipeline blocker as early as possible, per the required sequence (Tier 4 → Tier 1 → heavily revised → continuity/motif → short/long → remaining life scenes). Categories 5 and 6 are folded into the shots already placed above where a shot satisfies more than one role; no shot is generated twice.

| Order | Shot ID | Group | Rationale for this position |
|---|---|---|---|
| 1 | S084 | Tier 4, high risk | Establishes the "domestic hell" metaphor (CONTRAST); first and most content-bearing of the Tier 4 block; if this fails, the whole Tier 4 approach needs rework before continuing |
| 2 | S088 | Tier 4, high risk | The single highest-risk instance identified in 04G (★) — a near-content-free TRANSITION shot whose only job is to hold a plain visual pause with zero forbidden-tier imagery; tests the positive-only rewrite under the least forgiving conditions (almost nothing else to look at) |
| 3 | S089 | Tier 4, high risk + scene-pool | Closes the Tier 4 block; also the third scene-pool-differentiation case, so a failure here signals either a Tier 4 problem or a scene-pool problem — the evaluator must determine which (see rubric) |
| 4 | S060 | Tier 1 | The single highest religious-safety-risk fix outside Tier 4 (removed "suffering or torment" beside the Buddha/Đao Lợi assembly) |
| 5 | S014 | Tier 1 + long-shot progression | Tests both Tier 1 compliance (removed invented "veiled" attribute) and the camera-only progression fix for the S013–S015 duration sequence in one shot |
| 6 | S046 | Heavily revised (triple fix) + ritual/altar + scene-pool | Tests scene-pool differentiation, camera-clause de-duplication, and meta-commentary removal simultaneously — the most structurally complex fix in the whole revision |
| 7 | S083 | Heavily revised + scene-pool + long shot | Second scene-pool-differentiation case; also the clearest single-shot test of sustained one-action progression (hand stops → breathes → lowers) |
| 8 | S042 | Heavily revised — continuity/motif (T3) | Opens Continuity Thread T3 (father); tests the "physical strike" removal on emotionally charged content |
| 9 | S074 | Heavily revised — continuity/motif (caregiver) | Tests the hedged-action fix (bandage-or-medicine → medicine only) and the removed pre-empted-emotion cue |
| 10 | S078 | Heavily revised — modern life | Tests the "begins to ring" → "starts ringing" hedge fix on an everyday contemporary scene |
| 11 | S001 | Short shot + chair motif (baseline) | Shortest-duration test case; also confirms the episode's opening shot (never revised) renders cleanly |
| 12 | S095 | Chair continuity + ritual/lamp (baseline) | Last — a resolution-tier shot (Tier 5) that closes both the chair thread and the ritual category; also unrevised, so it closes the batch on a confirmed-clean baseline |

---

## 3. Test Cases

Each `Video prompt` below is copied **verbatim** from `04E_FINAL_VIDEO_PROMPTS.md` — no wording was changed for this document.

### Test 1 — S084

- **Shot ID:** S084
- **Timeline:** 00:34:41.077 → 00:35:18.000 (36.92s)
- **Category/domain tier:** Tier 4 — "địa ngục" tâm lý (psychological-metaphor hell)
- **Reason selected:** Mandatory priority shot; establishes the Tier 4 metaphor for the first time in the sequence (CONTRAST); the 04F audit found the original text named "otherworldly" and "fire, demonic imagery, punishment" even while negating them — the single riskiest phrase pattern for this tier.
- **Primary risk:** A text-to-video model renders literal fire, demonic imagery, or a supernatural/punishment scene despite the prompt's intent, because the underlying training data statistically associates "estrangement/cold house" scenes with dramatic lighting or genre cues that could drift toward horror framing if the model over-interprets "heavy," "cold," or "grown cold."
- **Expected visible result:** An ordinary, realistically lit domestic interior; several people seated apart in different corners of one room; flat, cool, unremarkable lighting; no one making eye contact; nothing supernatural, no unusual color grading, no genre-horror visual language.
- **Continuity requirements:** None (topic-linked only to S085, not a formal continuity thread); the setting must read as a plain, contemporary home, not connected to any earlier "chair" or "hall" motif.
- **Failure indicators:** Any fire, smoke, glowing/red lighting, monstrous or demonic figures, ritual punishment imagery, unnatural color grading suggesting the supernatural, or an interior that reads as a stage/temple/otherworldly space rather than an ordinary home.
- **Final prompt (verbatim from 04E):** "Inside an ordinary home, several family members sit apart in their own corners of the room, none of them looking at one another. A slow, static wide shot of the house takes in the distance between each person. Flat, cool interior light fills the space, giving no warmth. The mood is heavy with quiet estrangement, entirely human and domestic, the ordinary house simply grown cold."

### Test 2 — S088

- **Shot ID:** S088
- **Timeline:** 00:35:57.692 → 00:36:10.154 (12.46s)
- **Category/domain tier:** Tier 4 — "địa ngục" tâm lý
- **Reason selected:** Mandatory priority shot; 04G's single ★ highest-priority fix — this TRANSITION shot originally contained "fire, darkness-as-punishment, symbolic afterlife imagery" named directly beside the episode's strictest constraint, plus a redundant double camera-stillness sentence.
- **Primary risk:** Because the prompt is deliberately near-content-free (a plain visual pause, no confirmed subject), the model has the least grounding of any shot in the batch and may fall back on generic "transition" visual tropes (light flares, particle effects, abstract fire-like textures) that could be misread as the very afterlife/punishment imagery this shot must avoid.
- **Expected visible result:** A static or near-static frame of soft, undefined, neutral light with no discernible figure, object, or symbol — a plain visual pause, nothing more.
- **Continuity requirements:** Follows S087, precedes S089; no figure or object should carry over from either neighboring shot; must not resemble the Đao Lợi hall (Tier 1) or the chair motif (Thread T1).
- **Failure indicators:** Any flame, ember, red/orange glow, silhouette suggestive of a figure or demon, religious iconography, or any visual element that could read as "afterlife" or "punishment" — even abstractly (e.g., a glowing threshold, a descending light with ominous connotation).
- **Final prompt (verbatim from 04E):** "A fixed, unmoving shot rests on soft, undefined light, pausing quietly between one idea and its opposite. Nothing else enters the frame — only this plain, wordless visual pause."

### Test 3 — S089

- **Shot ID:** S089
- **Timeline:** 00:36:10.154 → 00:36:35.539 (25.38s)
- **Category/domain tier:** Tier 4 — "địa ngục" tâm lý; also a scene-pool-differentiation case
- **Reason selected:** Mandatory priority shot; closes the Tier 4 block; also one of three shots (with S046, S083) that previously shared one "hand freezes before a negative gesture" visual with no continuity thread — now rewritten with a whole-body-posture emphasis instead of a hand close-up.
- **Primary risk:** Two overlapping risks must be distinguished on review: (a) a Tier 4 risk — the model showing the "harsh word or gesture" itself instead of only the moment before it; (b) a scene-pool risk — the model rendering this shot so similarly to S046 or S083 that the intended visual differentiation collapses (i.e., the fix reads correctly in text but not in the generated frame).
- **Expected visible result:** A generic, unnamed person shown at medium shot distance, whole body visible, posture and shoulders stiffening inward for a moment and then easing back to stillness — no hand close-up, no depiction of any actual slap, insult, or comparison being carried out.
- **Continuity requirements:** New subject, no link to S046 or S083's figures; must not reuse their close-hand or face/shoulders framing verbatim.
- **Failure indicators:** The harmful act itself becoming visible (a raised hand actually striking, a mouth shaping an insult); framing that is a close-up on a single hand (would collapse the scene-pool fix back toward S046/S083); any religious/supernatural symbolism.
- **Final prompt (verbatim from 04E):** "A person's whole posture stiffens for a moment, shoulders and hands drawing inward as if catching themselves right before a harsh word or gesture, then easing back to stillness. A static, medium shot takes in the full figure through this moment of restraint. Soft, even light fills the frame. The harsh act itself is never shown — only the visible choice to stop before it happens."

### Test 4 — S060

- **Shot ID:** S060
- **Timeline:** 00:24:12.000 → 00:24:45.692 (33.69s)
- **Category/domain tier:** Tier 1 — Đức Phật / thân mẫu / Cung Trời Đao Lợi
- **Reason selected:** Mandatory priority shot; 04G's other ★ highest-priority fix — originally named "suffering or torment" directly beside the sacred assembly, the single highest-risk phrase pattern found anywhere in the document.
- **Primary risk:** The model introducing any visual suggestion of suffering, hell imagery, or a "dark" contrast within or adjacent to the reverent hall, given that the surrounding narration (not shown to the model, but potentially inferred from training-data associations with "Buddhist sutra" content) concerns hell/karma themes.
- **Expected visible result:** The identical gold-lit hall from the preceding shot, held static and unchanged — same distant assembly, same even gold-white light, nothing new entering the frame, calm and reverent throughout.
- **Continuity requirements:** Must exactly match S059's established framing, architecture-level, and lighting (Thread T2 HOLD); no new figure, symbol, or architectural element.
- **Failure indicators:** Any darkening, flame, shadow figure, or symbolic "underworld" element entering the frame; any drift away from the calm, evenly-lit composition already established in S009/S012/S016/S059.
- **Final prompt (verbatim from 04E):** "The same hall continues to hold, unchanged, the camera static and undisturbed. The gold-white light remains steady and even. The frame stays exactly as reverent and calm as it was before, nothing new entering the composition."

### Test 5 — S014

- **Shot ID:** S014
- **Timeline:** 00:04:52.154 → 00:05:25.846 (33.69s)
- **Category/domain tier:** Tier 1 — Đức Phật / thân mẫu / Cung Trời Đao Lợi; also the "long shot with progression" test case
- **Reason selected:** Tests two fixes in one shot: the removal of the invented "veiled" attribute on the maternal figure (unlicensed Production Fill on a sacred-adjacent figure), and the camera-only progression design built for the S013–S015 sequence (this is the middle shot: push completes, framing tightens to its closest point).
- **Primary risk:** (a) Domain risk — the model inventing a specific costume/veil detail despite it no longer being named in the prompt, or resolving facial detail on the sacred figure or the mother despite the explicit constraint; (b) progression risk — the model treating this as a flat, static repeat of S013 with no perceptible camera movement, which would mean the duration-mismatch fix failed to translate into an actual visual difference.
- **Expected visible result:** The same gesture as the previous shot (a hand extended toward an indistinct figure at the frame's edge), now framed slightly closer than before, gold-white light slightly deeper/warmer, still no facial detail resolved on either figure, no dialogue implied.
- **Continuity requirements:** Must visibly continue directly from S013's composition and lighting, one step closer; must set up S015's slight widen-back.
- **Failure indicators:** A resolved, detailed face on either figure; any veil, headdress, or costume detail invented; identical, motionless framing indistinguishable from S013 (would indicate the progression fix did not translate to visible camera movement); any dialogue/text overlay.
- **Final prompt (verbatim from 04E):** "The gesture continues to hold, the teaching figure's hand still extended toward the indistinct maternal presence. The camera's slow push from the previous shot settles to a close, complete framing on the gesture, coming to rest just short of any facial detail. The gold-white light deepens slightly around the two figures. The composition remains reverent and unhurried, without introducing any new symbol to illustrate the surrounding teaching."

### Test 6 — S046

- **Shot ID:** S046
- **Timeline:** 00:18:37.385 → 00:19:10.154 (32.77s)
- **Category/domain tier:** Tier 3 — Nghi lễ/kinh điển/bàn thờ/nén hương generic; also a scene-pool-differentiation case and the most structurally complex fix in the revision
- **Reason selected:** Mandatory priority shot; this single prompt combines three separate Phase G fixes (scene-pool differentiation via a wide setting-driven frame, de-duplication of a camera clause reused verbatim in S022/S032, and removal of a "not the father seen earlier" meta-commentary sentence) — the highest-complexity single test case in the batch.
- **Primary risk:** The model failing to render the required background altar-corner evidence at all (since it is explicitly meant to be soft/out-of-focus/non-central, a model may drop it entirely, under-satisfying the shot's Required Source Evidence), or conversely making it too prominent (turning a background reference into a focal altar, risking a return to the same "shrine" visual this fix was meant to avoid naming).
- **Expected visible result:** An unnamed person seated in a plain room, one hand stopping mid-motion in a small gesture of restraint; the corner of a modest home altar visible but clearly out of focus in the far background, not the visual focus of the shot; warm, low light; a wide, steady observational frame.
- **Continuity requirements:** New, unconnected subject — must not resemble or be mistaken for the father figure from S042–S045 (Thread T3); must not connect to S021's ornate memorial altar.
- **Failure indicators:** No altar/background evidence at all; an altar rendered as the shot's central focus (too prominent); a figure that visually resembles the S042 father (age, clothing, framing); a close-up on the hand alone (would collapse the scene-pool differentiation back toward S083/S089).
- **Final prompt (verbatim from 04E):** "An unnamed figure sits in a plain room, one hand stopping mid-motion in a small, private moment of restraint, the corner of a modest home altar visible but out of focus in the far background. A steady, wide observational frame takes in the person and the quiet room together. Warm, low light fills the space. The stillness carries a general sense of catching oneself before a habitual moment, ordinary and unremarkable rather than tied to any single story."

### Test 7 — S083

- **Shot ID:** S083
- **Timeline:** 00:34:06.923 → 00:34:41.077 (34.15s)
- **Category/domain tier:** — (no Domain Approval Gate tier); scene-pool-differentiation case; long-shot-with-progression case
- **Reason selected:** Mandatory priority shot; second of the three scene-pool-differentiation cases (face/shoulders emphasis, distinct from S046's wide-with-background-altar and S089's whole-body-posture); also the clearest single-shot test of a sustained one-action progression (breath in, hold, release) within a single continuous gesture.
- **Primary risk:** The model defaulting back to a hand-close-up framing (the original, now-removed shared visual with S046/S089), since "restraint before anger" is a common enough concept that training data may bias toward showing a clenched or stopping hand rather than the face/shoulders/breath the revised prompt specifies.
- **Expected visible result:** Close, unmoving framing on a parent's face and shoulders; a single visible exhale — shoulders/chest rising and falling once, expression easing from tense to calm; no hand shown prominently; even, quiet lighting.
- **Continuity requirements:** None (new, unconnected subject); must read as visually distinct from S046 and S089 despite sharing the same underlying "restraint" narrative concept.
- **Failure indicators:** A hand-focused close-up (collapses the scene-pool fix); an actual angry gesture completing instead of being caught and released; multiple breaths or repeated motion (should be one continuous single action, not a looping/stacked gesture).
- **Final prompt (verbatim from 04E):** "A parent's shoulders rise and fall in one slow, deliberate breath, their expression easing from tight to calm just before a sharp gesture would have followed. A close, unmoving shot stays on the parent's face and shoulders as they exhale slowly. Even, quiet light fills the frame. The moment is entirely about the visible release of tension, not about what almost happened."

### Test 8 — S042

- **Shot ID:** S042
- **Timeline:** 00:17:11.077 → 00:17:48.000 (36.92s)
- **Category/domain tier:** — (no Domain Approval Gate tier); Continuity Thread T3 (father) — opening shot
- **Reason selected:** Opens Continuity Thread T3, which every subsequent father-story shot (S043–S047) depends on; the original prompt named "physical strike" while negating it, on emotionally charged content (a parent raising their voice at a child) where the risk of the model rendering the named-but-negated act is highest in the whole batch outside the two Domain Gate tiers.
- **Primary risk:** The model depicting an actual physical strike/hit despite the source evidence being strictly vocal (raised voice only); or depicting the child as visibly injured/frightened beyond the confirmed "flinches and lowers face."
- **Expected visible result:** A father, visibly raising his voice (open mouth, tense posture, no physical contact), in a plain, modest front room; the child flinching and lowering their face; a brief, subtle shift in the father's own expression (recognition) within the same continuous moment; warm but uneasy lamp lighting; a close, handheld-feeling but restrained camera movement.
- **Continuity requirements:** Establishes Thread T3 — the specific father and child figures here must be visually consistent enough to be recognizable as the same pair in S043 (stillness), S044 (kneeling apology), and S045 (hold).
- **Failure indicators:** Any physical contact/strike; a named/labeled character; a second, separate image of "the father as a child" appearing in the same frame (explicitly forbidden); a circular/loop symbol rendered anywhere in the frame.
- **Final prompt (verbatim from 04E):** "A father raises his voice sharply at his young child in the plain front room of a modest home, the words landing hard. The child flinches and lowers their face. In the same breath, something shifts in the father's own expression — a flicker of recognition, as though he has heard this voice before. A subtle, handheld documentary movement stays close, feeling the tension without exaggerating it. Warm but uneasy lamp light fills the room. Neither figure is named, and no other image is inserted into the frame beyond this single moment between them."

### Test 9 — S074

- **Shot ID:** S074
- **Timeline:** 00:29:21.231 → 00:29:36.369 (15.14s)
- **Category/domain tier:** — (no Domain Approval Gate tier); caregiver category
- **Reason selected:** Represents the caregiver thread; the original prompt hedged the single action ("bandage or medicine") and pre-empted the next shot's emotional reveal with an early guilt cue — both fixed in Phase G, both testable only by checking whether the model now renders exactly one clear, confident action.
- **Primary risk:** The model rendering an ambiguous or composite action (e.g., unclear whether the caregiver is applying medicine or a bandage) if the prompt's now-single "administers medicine" instruction is not concrete enough about what "medicine" looks like being administered; or the model injecting a visibly sad/guilty expression that belongs to the next shot (S075).
- **Expected visible result:** A caregiver, at home, administering medicine to their mother with practiced, tired hands; evening light through a window; warm but weary domestic lighting; the caregiver's tiredness visible in their movements, but no strong emotional expression (guilt/crying reserved for S075).
- **Continuity requirements:** Same caregiver character must carry into S075 (bathroom scene, same person, different room).
- **Failure indicators:** An ambiguous or two-part action (bandaging AND medicating); a visible crying/guilt expression (belongs to S075, not here); a named character; a specifically depicted illness/diagnosis.
- **Final prompt (verbatim from 04E):** "A caregiver administers medicine to their mother with practiced, tired hands, evening light through the window marking the hour. A still, observational frame takes in the scene. Warm but weary domestic light fills the room. Fatigue sits plainly in the caregiver's tired, careful movements."

### Test 10 — S078

- **Shot ID:** S078
- **Timeline:** 00:31:12.462 → 00:31:48.923 (36.46s)
- **Category/domain tier:** — (no Domain Approval Gate tier); "đời sống hiện đại" (modern life) category
- **Reason selected:** Represents contemporary, technology-mediated life (a ringing phone as a stress trigger); the original prompt used a "begins to ring" hedge, revised to "starts ringing"; tests whether this minor wording change affects the model's ability to render a single, clear cause-and-effect reaction.
- **Primary risk:** The model failing to convey that the phone ringing is the *cause* of the person's stiffening (rendering the two as unrelated/simultaneous events rather than a clear reaction), or inventing a visible phone screen with legible content.
- **Expected visible result:** A person's body visibly tensing and glancing away in direct response to a nearby phone that has just started ringing; even, cool lighting; no visible screen text; no second figure present.
- **Continuity requirements:** New, unconnected subject; no link to any other phone-related shot (S004, S019, S049, S062, S072) since none of these form an official continuity thread.
- **Failure indicators:** A legible phone screen or caller ID; a second figure appearing to voice the "hãy về đi, cha mẹ mà" line; the stiffening reaction reading as unrelated to the phone (poor cause-and-effect clarity).
- **Final prompt (verbatim from 04E):** "A person stiffens and glances away as a nearby phone starts ringing, their body drawing inward. A static, close composition stays on the visible tension. Even, cool light fills the room. No specific words are shown, and no other figure is shown speaking the phrase running through their mind."

### Test 11 — S001

- **Shot ID:** S001
- **Timeline:** 00:00:00.000 → 00:00:07.846 (7.85s)
- **Category/domain tier:** — (no Domain Approval Gate tier); chair motif (Thread T1, opening shot); shortest-duration test case; unrevised baseline
- **Reason selected:** The episode's opening shot and the first link in Continuity Thread T1 (the chair, which recurs 13 times across the episode); the shortest duration in the selected batch, testing whether a very brief shot (7.85s) can still read as a complete, legible single composition; also a baseline check since this prompt was never touched in Phase G (it passed Phase F's audit cleanly).
- **Primary risk:** At under 8 seconds, the model may not have time to establish the scene clearly before the clip ends, or may compress/rush the intended "quiet and unresolved" mood into something that reads as abrupt rather than contemplative.
- **Expected visible result:** A single wooden chair, empty, in a modest home near a window; warm late-afternoon light; no person seated or nearby; a still, unhurried, contemplative visual mood established within the first couple of seconds.
- **Continuity requirements:** Establishes the chair's exact appearance (wood, size, placement) that S002–S008, S033, S038, S067, S095, S099, S100 must all visually match going forward — this is the reference frame for the entire T1 thread.
- **Failure indicators:** Any person seated in or near the chair; any photograph, flower, or extra prop near the chair; any on-screen text/logo/watermark; a chair design too generic or too distinctive to be recognizably "the same chair" in later callbacks.
- **Final prompt (verbatim from 04E):** "A single wooden chair stands empty in a modest Vietnamese home, positioned near a window. No one is seated, and no one has just left. The shot is still and unhurried, contemplative in its quiet. Warm late-afternoon light falls softly across the chair, casting a gentle amber tone through the room. The mood is quiet and unresolved, neither sad nor comforting. No text, no logos, no watermarks, no photographs or flowers added near the chair."

### Test 12 — S095

- **Shot ID:** S095
- **Timeline:** 00:38:04.616 → 00:38:18.203 (13.59s)
- **Category/domain tier:** Tier 5 — Nghi thức cá nhân khép phim (ngọn đèn, chắp tay); chair continuity (T1, 6th/final callback before the closing fade); ritual/lamp category; unrevised baseline
- **Reason selected:** Closes both the chair motif and the ritual/lamp category in one shot — the person finally sits before the long-established chair and lights a lamp, the episode's central visual resolution; also unrevised in Phase G (passed Phase F cleanly), serving as a second baseline confirmation.
- **Primary risk:** The model adding unauthorized ritual elements (incense, a larger altar, kneeling/prayer gestures) beyond the two confirmed actions (sitting, lighting a lamp), since "person + chair + flame" is visually close to a devotional/altar scene in common training data.
- **Expected visible result:** A person sitting down in front of the same wooden chair established in S001 and continued throughout the episode, lighting a small lamp beside it; warm, gentle lamp light spreading across the room; a quiet, resolved, unperformed mood; no incense, no additional altar objects.
- **Continuity requirements:** Must visually match the chair's established appearance from S001/S033/S067/etc. exactly; the lamp itself is a new, independent prop (not connected to S028's earlier lamp) per 04B/04C's explicit non-continuity note.
- **Failure indicators:** Incense, a shrine/altar setup, kneeling or prayer gestures beyond joined palms (which belongs to the next shot, S096), a chair that doesn't match the established T1 design, any on-screen text for the internal words.
- **Final prompt (verbatim from 04E):** "A person sits down before the same familiar wooden chair and lights a small lamp beside it. Static and unhurried, the shot settles close on the small flame catching. Warm, gentle light spreads from the lamp across the room. The mood is quiet and resolved, neither performative nor elaborate. No incense or altar is added to the scene."

---

## 4. Evaluation Rubric

Each generated test clip is scored across all 10 dimensions, then assigned one overall status.

### Dimensions

1. **Narration–visual alignment** — does the generated clip visualize what the shot's Required Source Evidence actually describes?
2. **Subject/action accuracy** — is the correct subject shown performing the correct single action, with no invented or missing elements?
3. **Single-action readability** — is exactly one action legible within the clip, without drift into a second action or an ambiguous blend?
4. **Natural motion** — does movement (camera or subject) look physically plausible, without warping, jitter, or unnatural physics?
5. **Camera compliance** — does the camera behavior match the prompt's stated instruction (static / push-in / lateral drift / etc.), with no unintended movement or a movement that contradicts the stated one?
6. **Character/object/setting continuity** — for shots with a continuity requirement (chair, Đao Lợi hall, Thread T3 father), does the rendered subject/object/setting plausibly match its established appearance?
7. **Anatomy stability** — are hands, faces, and bodies anatomically coherent throughout the clip (no extra/missing limbs, distorted faces, morphing)?
8. **Temporal stability** — does the subject/setting stay visually consistent frame-to-frame (no flickering, no identity drift mid-clip)?
9. **Domain safety** — for Tier 1/Tier 3/Tier 4/Tier 5 shots, does the output avoid every forbidden depiction listed in that shot's Domain Approval Gate entry?
10. **Overall usability** — could this clip be used in the final episode as-is, or does it need further work?

### Status Options

- **PASS** — meets all 10 dimensions; usable as-is.
- **PASS_WITH_PROMPT_POLISH** — core content and safety are correct; a minor prompt wording tweak (not a re-render) would improve quality (e.g. clarify a single ambiguous word).
- **REGENERATE_SAME_PROMPT** — the prompt itself is judged correct and safe, but this particular generation has a model-side defect (anatomy glitch, unnatural motion, a one-off rendering artifact) — evaluator's job is to distinguish this from a prompt problem by checking whether the defect is something the exact same prompt text would plausibly avoid on a second attempt.
- **PROMPT_REVISION_REQUIRED** — the defect is systematic and traceable to the prompt's own wording (ambiguity, missing constraint, an instruction the model could not have satisfied as written) — regenerating with the same prompt would likely reproduce the same problem.
- **PIPELINE_BLOCKER** — a Tier 1 or Tier 4 domain-safety violation appears in the output (forbidden depiction actually rendered, not just risked), or a shot's mapping/continuity is structurally broken — this halts any further batch expansion regardless of the other 11 shots' results.

**Distinguishing random model error from prompt error (required by the task):** if a defect is isolated to anatomy/motion glitches typical of generative video (flickering fingers, a brief warped frame, a stutter in camera motion) with no clear textual cause in the prompt, classify as `REGENERATE_SAME_PROMPT`. If the same defect recurs in a way traceable to genuine prompt ambiguity (e.g., "the seed rests in an open palm" rendered with an anatomically extra hand because the prompt never specifies whose palm), or if a forbidden-tier element appears that the prompt's positive-only language should have prevented, classify as `PROMPT_REVISION_REQUIRED` or `PIPELINE_BLOCKER` (domain-safety failures are always the latter, never treated as "random").

---

## 5. Acceptance Gate for a Larger Render Batch

A larger batch may only be proposed when **all** of the following hold across the 12 test results:

| Condition | Threshold |
|---|---|
| PIPELINE_BLOCKER count | 0 |
| Tier 1 violations (S060, S014) | 0 |
| Tier 4 violations (S084, S088, S089) | 0 |
| Semantic mismatches (narration–visual alignment failures) | 0 |
| Shots reaching PASS or PASS_WITH_PROMPT_POLISH | ≥ 10 of 12 |

If these hold, the next step is a larger — but still not full-100 — batch, prioritized toward whichever categories in Section 1's coverage matrix are not yet represented (e.g. more caregiver shots, more of the six "small practices" S062–S067 sequence). If any condition fails, the appropriate response is either targeted prompt revision (if the failure is `PROMPT_REVISION_REQUIRED`) or a full stop pending human review (if any result is `PIPELINE_BLOCKER`) — this document does not itself authorize or perform either action.

---

## 6. Kết quả trả về (Return Summary)

**Selected Shot IDs (12, execution order):** S084, S088, S089, S060, S014, S046, S083, S042, S074, S078, S001, S095

**Coverage matrix:** see Section 1.

**Execution order:** see Section 2 (1. Tier 4 high-risk → 2. Tier 1 → 3. heavily-revised structural fixes → 4–5. continuity/motif and short/long, folded into the same 12 shots where a shot serves a dual role → 6. no separate "remaining life scenes" shots needed, since caregiver/modern-life/father-continuity already appear in positions 8–10).

**Risk tested per shot:** documented individually in each Test Case's "Primary risk" and "Failure indicators" fields in Section 3.

**Evaluation checklist:** the 10-dimension rubric and 5-status classification in Section 4.

**Acceptance gate:** Section 5 — 0 PIPELINE_BLOCKER, 0 Tier 1 violations, 0 Tier 4 violations, 0 semantic mismatches, ≥10/12 at PASS or PASS_WITH_PROMPT_POLISH.

**File created:** `_INTERNAL/04H_LIMITED_TEST_GENERATION_PLAN.md` (this file). No other file was created or modified; `04A`–`04G`, narration, TTS, and final prompt text are all unchanged; no video was generated; no Git command was used.

**Remaining risks (for the human reviewer, not resolved by this plan):**
- This plan cannot verify actual model behavior — every "expected result" and "failure indicator" above is a prediction to be checked against real output once generation is actually run (by a human, with a specific video-generation tool, outside this task's scope).
- The two duration-progression sequences (S013–S015, S039–S041) are only partially covered: S014 tests the middle shot of one sequence, but the other sequence (S039–S041) and the bookend shots of the tested sequence (S013, S015) are not in this 12-shot batch — a full check of both sequences' visual continuity would need a follow-up batch.
- Timing remains `ESTIMATED_FROM_NARRATION`; even a fully passing test batch does not make timing audio-aligned, and clip durations generated here are illustrative of pacing, not a substitute for real TTS-driven retiming.
- Tier 2 (Địa Tạng Bồ Tát, never depicted) and Tier 3's other four shots (S021, S047, S054, S056) are not represented in this batch and would need their own check before a full-episode render.
