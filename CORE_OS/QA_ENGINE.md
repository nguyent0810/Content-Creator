# Core QA Engine

QA composition model:

Core QA + Domain QA + Asset-specific QA + Risk-specific QA.

Core QA checks structure, clarity, internal consistency, source presence, citation completeness, lineage, unsupported generalization, format, registry coverage, manifest validity, and asset integrity.

Domain QA is loaded from `DOMAIN_MANIFEST.qa_policy`. Core QA must not embed all domain policy details.

## Content Package QA Standard

QA validates the content package through TTS handoff only. A package cannot advance to `READY_FOR_TTS_HANDOFF` or `CONTENT_PACKAGE_COMPLETE` until required checks pass or receive explicit advisory status.

QA must not require or validate downstream voice rendering, video rendering, final subtitles, visual briefs, metadata exports, publication summaries, or upload state as part of the default content package.

## Content QA

Content QA checks research accuracy, claim-to-source integrity, doctrinal accuracy, narrative quality, safety, attribution, terminology, and internal consistency.

## Structure QA

Structure QA checks that package root contains only:

- `README.md`;
- `OUTPUT/`;
- `_INTERNAL/`;
- `_ARCHIVE/`.

Structure QA must fail if active package files remain at root or if obsolete files are left unarchived.

## Asset QA

Asset QA checks that required files exist, filenames and extensions are correct, files are UTF-8 and non-empty, JSON parses, declared paths exist, asset IDs are unique, and required content-package assets are present.

Required active files are:

- `OUTPUT/03_AUDIO_SCRIPT_TTS.txt`;
- `_INTERNAL/manifest.json`;
- `_INTERNAL/01_RESEARCH_BRIEF.md`;
- `_INTERNAL/02_EPISODE_PLANNER.md`;
- `_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`;
- `_INTERNAL/06_QA_REPORT.md`;
- `_INTERNAL/REVIEW_SUMMARY.md`;
- `_ARCHIVE/ARCHIVE_MANIFEST.md`.

## Derivation QA

Derivation QA checks MASTER-to-TTS coverage, absence of missing narration, absence of unsupported narration additions, no editorial notes in TTS, no metadata in TTS, no Markdown in TTS, no comments in TTS, and no production directions in TTS.

Subtitle coverage and subtitle alignment are outside default content-package QA unless a separate downstream subtitle package is explicitly created.

## Manifest QA

Manifest QA checks:

- `_INTERNAL/manifest.json` parses as valid JSON;
- `schema_version` is `2.0`;
- `content_status` uses an allowed content-package status;
- `canonical_master` is `_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`;
- `tts_output` is `OUTPUT/03_AUDIO_SCRIPT_TTS.txt`;
- external processes are marked `OUT_OF_SCOPE`;
- archived assets do not remain active dependencies;
- active internal assets point only into `_INTERNAL/`.

## Registry QA

Registry QA checks that active registry entries point to the current `OUTPUT/` and `_INTERNAL/` paths, do not point to archived package files as active dependencies, do not reference backup directories, and do not duplicate IDs.

## Failure Conditions

Audit must fail if:

- manifest JSON is invalid;
- `schema_version` is not `2.0`;
- content status is not allowed;
- Master Script is missing;
- TTS output is missing or empty;
- TTS contains Markdown, metadata, comments, labels, or production notes;
- TTS omits or invents spoken content;
- master-to-TTS coverage is below 100 percent without explicit human approval;
- external voice, video, or publish states are claimed as complete;
- obsolete root files remain outside `_ARCHIVE/`;
- active registry paths point to archived files, missing files, or old root paths;
- a ready package contains failed QA.
