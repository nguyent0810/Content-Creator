# SEO Engine

## Document Role

This document governs how discovery metadata (titles, descriptions, tags, hashtags, thumbnails) is written for this channel across YouTube Long-form, YouTube Shorts, and TikTok. It is the SEO-specific counterpart to `SHORTS_ENGINE.md` (which governs the Short *script* itself) and `GROWTH_ENGINE.md` (`08_GROWTH_ENGINE.md`) — it does not override either, or `BRAND_BIBLE.md`, or any Domain's `DOMAIN_QA_POLICY.md`. It exists because SEO work was previously done ad hoc, per-episode, inside one-off agent prompts with no persistent record — EP006 was produced with zero SEO metadata as a direct consequence, discovered only when auditing readiness for EP007. Treat this file the same way `SHORTS_ENGINE.md` is treated: read before every SEO pass, and an episode is not "done" until its `SEO/` folder exists and matches this spec.

## The One Rule That Overrides Every Tactic Below

`08_GROWTH_ENGINE.md`'s **Anti-Keyword-Chasing Standard** applies in full to SEO metadata, not just to topic selection: "The studio must never chase keywords blindly... If a keyword cannot be served truthfully and compassionately, it must be rejected or reframed." A title, thumbnail-text suggestion, or hashtag that is technically higher-CTR but sensational, fear-based, or overclaiming is rejected regardless of expected performance — the same standard `SHORTS_ENGINE.md` applies to Short hooks. This is not a soft preference; it is the reason this Engine exists as a companion to, not a replacement for, general SEO best practice.

**Concretely, for a channel that will keep covering karma, hell realms, death, and grief:** never title or caption content with fear-bait framing ("ĐỊA NGỤC CÓ THẬT KHÔNG?! Sự thật KINH HOÀNG...", "Cái giá bạn phải trả nếu...", "Nếu bạn KHÔNG xem video này..."). The correcting-a-misconception angle (which this channel uses constantly and effectively — see EP001, EP006) is not the same as fear-bait; "X không phải là Y — sự thật là Z" is an honest curiosity hook, "điều KINH HOÀNG sẽ xảy ra nếu..." is not. If a title needs a threat or a countdown-to-doom framing to feel compelling, the title is wrong, not the topic.

## What Gets Produced, Per Episode

```
EP0XX/SEO/
  Youtube Long/<N>_<Title>.txt         — 1 file, metadata for the Long-form video
  Youtube Short/<N>_<Title>_Short.csv  — 1 file, 30 rows (one per Short), bulk-upload CSV format
  Tiktok/<N>_<Title>_Tiktok.txt        — 1 file, 30 entries, description-only (see format below)
```

An episode's production is not complete until this folder exists alongside `Long/` and `Short/`.

## YouTube Long-form

Source research (2026, industry consensus): the algorithm weights watch time, retention, and CTR; titles should carry the primary keyword naturally, stay under ~60 characters ideally and never exceed 100 (mobile truncation); descriptions are indexable content — the primary keyword must appear in the first ~125 characters (the preview window) and 2 sentences, with 200-300 words of contextual explanation; chapters/timestamps aid both navigation and search visibility when the episode's beat structure supports them.

Format (plain text file):
```
TITLE:
<one title, ideally <60 chars, hard max 100, primary keyword natural, not keyword-stuffed>

DESCRIPTION:
<200-300 words. Primary keyword in the first 2 sentences / first 125 characters. Cover: what the episode corrects or explores, 3-5 bullet content points, one sentence naming the series and its editorial character ("chậm rãi, có căn cứ, không giật gân"). End with chapter timestamps if the episode planner's beat structure supports reasonable estimates (label them as estimates pending final edit — see EP005 precedent), then 3-5 hashtags.>

TAGS:
<10-15 comma-separated keyword phrases, not hashtags — broad-to-specific, include the series name, the episode's core figures/concepts, and 2-3 audience-intent phrases (e.g. "Phật giáo cho người mới bắt đầu")>

CATEGORY:
Education (27)

PLAYLIST:
Giải Mã Kinh Địa Tạng

SUGGESTED THUMBNAIL TEXT:
<3-6 words, honest curiosity hook, no threat/countdown framing — this is the text that would appear ON the thumbnail image, not the video title restated>
```

## YouTube Shorts (30 per episode, one CSV)

Source research (2026): Shorts titles cap at 100 characters, stay under ~70 for full mobile display; descriptions cap at 5000 characters but only the first ~125 are shown before "more" — put the keyword there; hashtags belong in the description (not the title) — 3-5 total, lead with `#Shorts`, add 1-2 niche-specific tags, optionally 1 trend/branded tag; never use empty viral tags (`#Viral`, `#FYP`, `#ForYou`, `#Trending`) — they carry no discovery signal and read as try-hard.

CSV header (must match exactly, this project's `bulk_upload_template.csv` convention):
```
"filename","title","description","tags","privacy","playlist","categoryId","scheduleTime","thumbnail"
```

Per-row rules:
- `filename`: `<N>_Short_<NN>.mp4` placeholder (no rendered video exists yet — rename to match the real export filename when one exists).
- `title`: ≤70 chars, keyword-natural, pulled from that Short's actual hook/claim — never generic, never fabricated beyond what that Short's script says.
- `description`: keyword + context in the first 125 chars, ends with hashtags per the rule above.
- `tags`: 5-8 comma-separated keyword phrases (distinct field from hashtags-in-description).
- `privacy`: `public`.
- `playlist`: `Giải Mã Kinh Địa Tạng - Shorts`.
- `categoryId`: `27`.
- `scheduleTime`: a default suggested cadence (commonly 1 Short/day starting a few days out), explicitly flagged in the delivery message as a placeholder the user must adjust to their real calendar — never presented as a committed schedule.
- `thumbnail`: `<N>_Short_<NN>_thumb.jpg` placeholder.

Validate the CSV with a real parser (Python `csv` module) before delivery — check row count (30), header match, no empty fields, no duplicate filenames, no title over 100 chars. This has caught zero errors so far but the check is cheap and the failure mode (a broken bulk-upload file) is expensive for the user.

## TikTok (30 per episode, one file)

Source research (2026): TikTok shows only the first ~100-150 characters of a caption before truncating — lead with the primary keyword phrase, not a teaser; the algorithm reads spoken audio (ASR) and on-screen text (OCR) for search indexing, so the *spoken* keyword-first opening matters as much as the caption; ideal hashtag count is 3-5, one broad + 2-3 niche, "less is more."

**Format decision (per explicit user correction — do not revert):** TikTok has one field that matters for copy-paste — the description. Do not produce separate CAPTION / ON-SCREEN TEXT / HASHTAGS / SUGGESTED SOUND fields; those were tried and explicitly rejected as harder to use. The file is 30 entries, each just:

```
*** 1

<one flowing line: the caption text, keyword-first, ending with 3-5 hashtags inline — nothing else, no field label>

*** 2

<...>
```

The caption text should closely track (not necessarily duplicate word-for-word) that Short's own hook/opening line, since the same underlying claim is what's being surfaced on both platforms — but it does not need to be identical, and TikTok's harder ~150-char truncation may require a tighter opening than the Short's full audio hook.

## Consistency Checks Before Delivery

1. Does `EP0XX/SEO/` contain all three subfolders with exactly one file each (Long: 1 file; Short: 1 CSV; TikTok: 1 file with 30 entries)?
2. Does the Long-form title stay under 100 characters, and the description's first 125 characters carry the primary keyword?
3. Does every Shorts CSV row's title stay under 100 characters (ideally 70), and does the CSV parse cleanly with Python's `csv` module (30 rows, correct header, no empty fields)?
4. Does every TikTok entry read as one flowing description line with no leftover field labels?
5. Would any title, caption, or thumbnail-text suggestion read as fear-bait, a threat, or a countdown-to-doom framing if seen out of context? If yes, rewrite — see "The One Rule That Overrides Every Tactic Below."
6. Are hashtags free of empty-signal tags (`#Viral`, `#FYP`, `#ForYou`, `#Trending`)?
7. Does the content of every title/description/caption trace back to something actually present in the Long-form script or that specific Short's script — no claims invented for the sake of a punchier title?

## Known Gaps (as of this Engine's creation, 2026-07-17)

- EP001 and EP005 have SEO produced under the ad-hoc prompts that preceded this Engine — their content matches this spec closely (checked retroactively) but were not produced *from* this file, so a full re-check against the "Consistency Checks" list above has not been run on them.
- EP006 had no SEO at all until this Engine's first production pass — see `CONTINUITY_REGISTRY.md` for the broader pattern of production steps silently skipped without a persistent Engine doc forcing them.
- There is currently no automated audit gate (unlike `TOOLS/package_audit.py` for Long/Short packages) that checks an episode's `SEO/` folder exists or validates its contents. A future improvement could extend that tool or add a sibling script.
