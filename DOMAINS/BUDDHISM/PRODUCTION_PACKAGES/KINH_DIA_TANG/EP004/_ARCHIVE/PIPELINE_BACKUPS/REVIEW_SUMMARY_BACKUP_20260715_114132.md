# Package Overview

EP004 is a minimal content package for the Kinh Địa Tạng episode Cung Trời Đao Lợi - Khi Đức Phật Giảng Kinh Vì Mẹ, Và Bài Học Hiếu Đạo Bị Lãng Quên.

# Current Status

READY_FOR_TTS_HANDOFF

The app-scope content package is complete. Voice render, video render, forced alignment, upload, and publish are external processes.

# Output

Active user-facing output:

OUTPUT/03_AUDIO_SCRIPT_TTS.txt

Video prompt output:

OUTPUT/04_VIDEO_CREATE_PROMPTS.txt

# Canonical Master

Canonical narration source:

_INTERNAL/03_AUDIO_SCRIPT_MASTER.md

The TTS file must be regenerated from this Master if narration changes.

# Research Summary

Research and content decisions are in _INTERNAL/01_RESEARCH_BRIEF.md. The episode uses qualified Buddhist/traditional language, avoids unsupported direct quotations, and keeps filial piety trauma-aware.

# Planner Summary

Planning is in _INTERNAL/02_EPISODE_PLANNER.md. The episode uses a parallel timeline pattern, filial-piety blueprint, and empty-chair motif.

# QA Summary

QA is in _INTERNAL/06_QA_REPORT.md. Content QA passed with human-review advisories for citation/copyright and visual representation if later used.

Video Prompt QA passed for estimated timeline coverage, continuous six-second prompt numbering, visual-mode labeling, continuity, and Buddhist representation safety.

# Video Prompt Handoff Summary

| Item | Value |
|---|---|
| Video prompt output path | OUTPUT/04_VIDEO_CREATE_PROMPTS.txt |
| Timeline mapping path | _INTERNAL/04_VIDEO_PROMPT_TIMELINE.json |
| Prompt count | 402 |
| Semantic beat count | 130 |
| Duration per prompt | 6 seconds |
| Timeline type | ESTIMATED |
| Segmentation type | SEMANTIC_BEAT_FIRST |
| Visual pipeline | SEMANTIC_BEAT_FIRST -> VISUAL_BEAT_DECOMPOSITION -> DISTINCT_VISUAL_OBLIGATION_PER_CLIP -> VIDEO_PROMPT |
| Estimated total duration | 2410.154 seconds |
| Rounded visual duration | 2412 seconds |
| Global visual style | Cinematic sacred-documentary realism with Vietnamese Buddhist restraint, symbolic transitions, and human domestic detail |
| Continuity policy | Scene sequences preserve character appearance, environment, lighting, palette, props, and Buddhist representation constraints; each prompt remains standalone |
| Narration context policy | Complete semantic beats are prioritized over exact six-second word slicing; adjacent clips may reuse the same complete sentence or idea for continuity |
| Visual obligation policy | Each six-second clip has a distinct content obligation tied to narration details, not merely a new camera angle |
| QA result | PASS |
| Known limitations | Timeline is estimated from 5222 words at 130 words per minute; it is not actual audio alignment. Future rendered audio may require retiming. |

## Video Prompt Revision QA

| Metric | Result |
|---|---:|
| Total prompts | 402 |
| Semantic beats | 130 |
| Visual obligations | 402 |
| Concrete-detail coverage | 100% |
| Prompts reviewed | 402 |
| Prompts retained | 31 |
| Prompts rewritten | 371 |
| Generic obligation count | 0 |
| Placeholder prompt count | 0 |
| Global repeated-template count | 0 |
| Unjustified template reuse count | 0 |
| Visual-narration mismatch count | 0 |
| Missing concrete-detail count | 0 |
| Meaning-polarity mismatch count | 0 |
| Obligation-without-source count | 0 |
| Timeline gaps | 0 |
| Timeline overlaps | 0 |
| Narration coverage | 100% |

# Approved Decisions

- _INTERNAL/03_AUDIO_SCRIPT_MASTER.md is canonical.
- OUTPUT/03_AUDIO_SCRIPT_TTS.txt is the only active deliverable.
- OUTPUT/04_VIDEO_CREATE_PROMPTS.txt is the active video-prompt handoff output.
- Voice, video, subtitle timing, upload, and publish are out of scope.
- Optional visual, metadata, subtitle, audit, and production handoff files are archived.

# Outstanding Issues

No blocker exists inside the app's scope. External processes still need their own tools and review.

# Human Review Required

- Final citation/copyright review before public publication.
- Human review if any visual, metadata, subtitle, or publication package is revived from archive.

# Regeneration Instructions

1. Edit _INTERNAL/03_AUDIO_SCRIPT_MASTER.md only.
2. Keep narration inside <!-- NARRATION_START --> and <!-- NARRATION_END -->.
3. Regenerate OUTPUT/03_AUDIO_SCRIPT_TTS.txt from the narration block.
4. Re-run Master-to-TTS coverage QA.
5. Update _INTERNAL/manifest.json and _INTERNAL/06_QA_REPORT.md.
6. If TTS timing changes, regenerate OUTPUT/04_VIDEO_CREATE_PROMPTS.txt and _INTERNAL/04_VIDEO_PROMPT_TIMELINE.json from the updated narration.

# Archived Files

See _ARCHIVE/ARCHIVE_MANIFEST.md.


## Safe Rollback Video Prompt QA

| Metric | Result |
|---|---:|
| Prompts reviewed | 402 |
| Prompts retained | 0 |
| Prompts rewritten | 402 |
| Max batch size | 30 |
| Batch gate status | PASS |
| Meta-template count | 0 |
| Mixed-language prompt count | 0 |
| Source-visual mismatch count | 0 |
| Meaning-polarity mismatch count | 0 |
| Missing concrete-detail count | 0 |
| Unjustified scene-template reuse count | 0 |
| Timeline gaps | 0 |
| Timeline overlaps | 0 |
| Narration coverage | 100% |


## No Random Continuity Video Prompt QA

| Metric | Result |
|---|---:|
| Prompts reviewed | 402 |
| Prompts retained | 0 |
| Prompts rewritten | 402 |
| Max batch size | 25 |
| Batch gate status | PASS |
| Random continuity-detail count | 0 |
| Unjustified scene-template reuse count | 0 |
| Narration-visual mismatch count | 0 |
| Anachronistic object count | 0 |
| English grammar issue count | 0 |
| Timeline gaps | 0 |
| Timeline overlaps | 0 |
| Narration coverage | 100% |

## Remove Meta Template Video Prompt QA

| Metric | Result |
|---|---:|
| prompts reviewed | 402 |
| prompts retained | 11 |
| prompts rewritten | 391 |
| max batch size | 25 |
| batch gate status | PASS |
| meta-template count | 0 |
| Vietnamese-fragment-in-English count | 0 |
| unnatural-English count | 0 |
| unjustified scene reuse count | 0 |
| narration-visual mismatch count | 0 |
| multi-action-in-six-seconds count | 0 |
| timeline gaps | 0 |
| timeline overlaps | 0 |
| narration coverage | 100% |
| decision | PASS |

Backup created before revision: `D:\Media\TTS\Kinh ??a t?ng_EP004_REMOVE_META_TEMPLATE_BACKUP_20260714_152410`
