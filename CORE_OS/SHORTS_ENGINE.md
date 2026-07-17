# Shorts Engine

## Document Role

This document governs how YouTube Shorts (vertical, ≤75s) are written for this channel. It is the Shorts-specific counterpart to `CONTENT_ENGINE.md` and `PRODUCTION_ENGINE.md`, and it does not override `BRAND_BIBLE.md`, any Series Bible's Canonical Boundaries, or a Domain's `DOMAIN_QA_POLICY.md` — it specializes them for short-form. Every Short produced under this Engine is a derivative asset of an already-QA'd Long-form `audio_script_master`; a Short must never introduce doctrinal content, names, or claims that do not already exist in its source Long-form script.

## Why Retention Craft Is Not the Same As Manipulation

The channel's Non-exploitation value (`BRAND_BIBLE.md`) forbids exploiting fear, guilt, or false urgency for engagement. This Engine treats that as a hard constraint, not a suggestion to be balanced against performance. The good news: the retention techniques that actually work on Shorts in 2026 are structural, not deceptive — a strong hook, a single idea, tight pacing, and an ending that loops back to the beginning. None of that requires clickbait, fear-baiting, or a promise the content doesn't deliver on. The rule for every Short: **the hook's question must be honestly answered inside the Short itself.** If a hook creates curiosity the Short doesn't resolve, the Short is rejected regardless of how well it performs.

Retention data (industry sources, 2026) that shapes the rules below:
- 50-60% of Shorts viewers who drop off do so in the first 3 seconds — the opening line/image is the single highest-leverage sentence in the whole script.
- **"Hook Drop Delta":** if a Short loses more than 25% of viewers within the first 3 seconds, the platform tends to throttle further reach; Shorts that retain 60%+ of viewers past the 3-second mark are meaningfully more likely to get pushed to the discovery feed. There is no way to measure this internally before publishing, but it is the reason the hook gets more editorial scrutiny than any other single line in this Engine.
- A stop-scroll hook works through four fast stages, not one clever line: **Pattern Interrupt** (the opening image/line breaks the expected feed pattern), **Micro-Commitment** (something makes the viewer's thumb pause), **Relevance Proof** (a cue that this is for them, specifically), **Payoff Promise** (a reason to keep watching to the end). Mode-specific hook templates below should be checked against this four-stage shape, not just against the self-sufficiency rule.
- Replays are weighted heavily by the algorithm; a Short whose last line flows naturally back into its first line earns more replays than one that just "ends."
- Most mobile viewers watch with sound off some of the time — a Short's opening line must land even without narration, which for an audio-only asset means the FIRST sentence must be self-sufficient and concrete (no pronoun that depends on prior context, no "và" continuing a thought that isn't there).

Sources: [OpusClip — YouTube Shorts Hook Formulas](https://www.opus.pro/blog/youtube-shorts-hook-formulas), [OpusClip — Ideal Shorts Length & Format](https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention), [Conbersa — Best Shorts Hooks 2026](https://www.conbersa.ai/learn/best-youtube-shorts-hooks), [Virvid — The First 3 Seconds: Hook Structures That Stop Scroll](https://virvid.ai/blog/first-3-seconds-hook-faceless-shorts-2026), [Joyspace — Pattern Interrupts](https://joyspace.ai/pattern-interrupt-reset-attention-span), [FluxNote — Text-On-Screen Shorts Format](https://fluxnote.io/guides/youtube-shorts-text-on-screen-format-2026)

## Open Question: Narration Pace May Be Faster Than Optimal For Comprehension

General 2026 faceless-Shorts guidance converges on **~150-170 wpm** as the "conversational, not rushed" ideal voiceover pace for comprehension and retention. This channel's measured real TTS pace (see `CONTINUITY_REGISTRY.md`, "Calibrated production parameters") is **~260 wpm at the tool's default speed** — roughly 60% faster than that external benchmark. This Engine's word-count targets (below) are still built around the 260 wpm figure because that is what the production pipeline actually measures against, but the gap itself is worth surfacing: a Short scripted to 110-195 words will read in the intended 25-45 seconds only if narrated at 260 wpm; narrated at the "ideal" 150-170 wpm instead, the same script would run 40-78 seconds — long for a Short. If comprehension/retention ever underperforms expectations, check the TTS playback speed setting before assuming the script itself is the problem; slowing default TTS speed for Shorts specifically (independent of Long-form) is a lever this Engine does not currently take a position on.

## Universal Short Anatomy

Every Short, regardless of mode (below), follows this shape:

1. **Hook (0-3s, ~8-15 words).** Drops the listener into a concrete image, a question, or a stated misconception — never a greeting, never "hôm nay chúng ta sẽ nói về...", never a throat-clear. Must be fully self-contained (see sound-off rule above) and should satisfy the four-stage Pattern Interrupt → Micro-Commitment → Relevance Proof → Payoff Promise shape described above, compressed into one or two sentences.
2. **Single idea (rest of the body).** One claim, one image, one story-beat, or one contrast. If a script needs "và ngoài ra" to fit in a second idea, split it into two Shorts instead.
3. **Micro-pacing.** A new concrete detail, turn, or emotional beat at least every 3-4 seconds of read time (~7-10 words). No unbroken abstract exposition longer than two sentences.
4. **Loop-close ending.** The final line should echo, answer, or rhyme with the opening line/image closely enough that replaying the Short from the top feels intentional rather than jarring. This is a craft technique, not a trick — it rewards a viewer who watches twice, it doesn't deceive a viewer who watches once.
5. **Reflective close, not a directive CTA.** Ends on a question or a resonant statement inviting inner reflection, matching the channel's existing Long-form ending style. No "nhấn theo dõi", no manufactured urgency.

Target length: 25-45 seconds (~110-195 words at the measured ~260 wpm real TTS pace — see `CONTINUITY_REGISTRY.md`, "Calibrated production parameters"; this supersedes any earlier ~150 wpm estimate) for most modes; Quote/Reflection Shorts may run as short as 15-20s (~65-85 words). Do not pad a thin idea to hit a length target — a strong 20-second Short outperforms a padded 45-second one. Always re-check this pace figure against a real TTS render before relying on it for a new batch; update both this line and the registry entry if a new measurement differs.

## The Six Short Modes

A single Long-form episode is mined for Shorts using six distinct modes, not by chopping the transcript into 30 sequential slices (that produces redundant, low-quality Shorts — the exact complaint that triggered this Engine). Each mode extracts a different *kind* of unit from the Long-form, so a 30-Short batch feels like 30 different entry points into the episode, not 30 fragments of the same walk-through.

1. **Myth-Bust.** Structure: "Nhiều người nghĩ [hiểu lầm phổ biến]. Nhưng thực ra [sự thật]." Source: any misconception the Research Brief's Risk Flags/Things Not To Claim section explicitly names, or any place the Long-form corrects a common assumption. Strongest mode for cold-audience discovery because it creates immediate, honest tension.
2. **Symbol Decode.** Structure: isolate one visual/symbolic detail (an object, a gesture, a color, a setting) and unpack what it means. Source: any named symbol, object, or setting in the Long-form (tích trượng, minh châu, khói hương, tòa sen, etc.). One symbol per Short.
3. **Story Beat.** Structure: a single self-contained moment from a narrative the Long-form tells, rewritten so it doesn't require the surrounding story to land emotionally — needs its own micro-setup, its own turn, its own close. Source: any story/parable in the Long-form; a rich story can yield 2-3 Story Beat Shorts (setup-beat, turning-point-beat, resolution-beat) as long as each still stands alone.
4. **Quote/Reflection.** Structure: take (or tightly paraphrase, per the same verbatim-quoting Risk Flags as the Long-form) the single most quotable line the Long-form produced, give it 1-2 sentences of context, end on the reflective question it implies. Shortest mode, text-forward, minimal narration.
5. **Compare/Contrast.** Structure: "Người ta hay nhầm [X] với [Y]. Khác nhau ở chỗ..." Source: any distinction the Character Bible or Research Brief draws (e.g., Địa Tạng vs. Diêm Vương, vow vs. transaction, remorse vs. guilt). Directly reuses the channel's existing "correcting misunderstanding" mission — never invent a contrast the source material doesn't already make.
6. **Modern Application.** Structure: connect one teaching/image from the Long-form to a concrete modern emotional situation (grief, loneliness, guilt, caregiving fatigue — see `PROJECT_PRD.md` Target Audience) in one sentence, then return to the teaching. Source: the Long-form's own theme, reframed toward daily life — must not introduce a modern scenario the Research Brief didn't already sanction as in-bounds for the series.

## Mining a Long-form Into 30 Shorts

1. Re-read the finished, QA-passed Long-form `03_AUDIO_SCRIPT_MASTER.md` and the Research Brief together.
2. For each of the 6 modes, list every distinct unit the Long-form actually supports (a symbol, a misconception, a story beat, a quotable line, a contrast, an application). Do not force a mode to produce units the source doesn't contain — an episode with 3 strong symbols yields 3 Symbol Decode Shorts, not 5 padded ones.
3. If the combined list is short of 30, prioritize splitting rich Story Beats into multiple stand-alone moments and drawing more Modern Application angles (this mode scales best) before ever repeating an angle.
4. Deduplicate: no two Shorts in the batch may share the same hook image or the same core claim. A reviewer reading all 30 hooks in a row should see 30 different opening images/questions.
5. Sequence the batch for release (not for narrative order) by alternating modes — do not release 5 Myth-Bust Shorts in a row.
6. Cross-check the source line/passage each concept cites against every other concept's citation. Two Shorts drawing on the *same* Long-form line/passage are high-risk for claim duplication even when their planned modes differ (this has happened in production — a Story Beat and a Quote/Reflection mode both anchored to the same line ended up making the same core claim). Flag any shared-citation pairs explicitly in the plan and verify at write time that they truly diverge, or reassign one to a different passage.

## Shorts-Specific QA Checklist

In addition to the standard checks in `QA_ENGINE.md` and the domain's `DOMAIN_QA_POLICY.md`, every Short batch is checked for:

- **Standalone comprehension:** could a viewer who has never seen the Long-form or any other Short in the batch understand and feel this Short? (This caught a real defect in the first EP001 Shorts batch — a Short about "the vow" never named who was making it.)
- **Hook self-sufficiency:** does the first sentence work with zero prior context and zero visual, i.e. read on its own?
- **Loop-close fit:** does the last line plausibly flow back into the first line?
- **No manufactured curiosity gap:** is every question the hook raises actually answered inside the same Short?
- **Batch-level de-duplication:** no repeated hook image/claim across the batch (checked across the whole batch at once, not Short-by-Short).
- **Fidelity to Long-form:** no claim, name, or detail absent from the source Long-form script (same standard as the Long-form's own Risk Flags).

## What Not To Do

- Do not open with a greeting, a preamble, or a restatement of the episode title.
- Do not promise a payoff ("đợi đến cuối video sẽ biết") the Short doesn't deliver inside itself.
- Do not use fear, guilt, or urgency as the hook mechanism, even softened — use genuine curiosity or a genuine misconception instead.
- Do not pad length to hit a target duration.
- Do not let two Shorts in the same batch answer the same question.
