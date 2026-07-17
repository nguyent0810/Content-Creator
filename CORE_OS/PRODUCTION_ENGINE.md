# Core Production Engine

The Production Engine coordinates content production packages without owning domain facts. It binds each package to a domain manifest, approved source assets, QA policy, and compatibility records. Production must stop when required domain assets are missing, planned-only, or doctrinally unvalidated.

## Production Package Lifecycle Standard

The Production Engine manages each episode as a lifecycle-controlled content package, not as disconnected documents and not as a media rendering workspace.

`_INTERNAL/manifest.json` is the machine-readable source of truth for package identity, content status, active asset inventory, derivation lineage, dependency tracking, QA status, and external handoff state.

`README.md` is the human entry point. It must point users to `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` as the only user-facing output.

Legacy `status.md` files are not active lifecycle projections and must be archived.

## Canonical Production Flow

Research -> Episode Planner -> Master Script -> Content QA -> TTS-clean output -> External handoff.

The Production Engine must not generate, require, or approve voice renders, video renders, final subtitles, visual briefs, metadata packages, publication summaries, or platform-publishing states as part of the default content package.

## Canonical Package Layout

| Location | Rule |
|---|---|
| `README.md` | The only root file. Explains the package and where to find the TTS handoff. |
| `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` | The only user-facing active output. Plain text only. |
| `_INTERNAL/` | Active manifest, research, planner, master script, QA, review summary, and source support files. |
| `_ARCHIVE/` | Superseded, unused, migrated, or review-history files with an archive manifest. |

No active asset should exist as a peer file at package root.

## Asset Classes

| Class | Rule |
|---|---|
| canonical editorial asset | Owns editorial source content and may be used as a source of truth. Must live in `_INTERNAL/`. |
| derived handoff asset | Generated from canonical narration and must never become an independent canonical source. Must live in `OUTPUT/`. |
| internal review asset | Supports review, QA, and source traceability. Must live in `_INTERNAL/`. |
| archive asset | Retained for auditability but not active. Must live in `_ARCHIVE/`. |
| external process | Voice, video, publishing, subtitle alignment, and metadata finalization are outside package scope. |

## Allowed Content Status Values

The only allowed package content statuses are:

- `DRAFTING`
- `READY_FOR_CONTENT_REVIEW`
- `CONTENT_REVISION_REQUIRED`
- `CONTENT_APPROVED`
- `READY_FOR_TTS_HANDOFF`
- `CONTENT_PACKAGE_COMPLETE`
- `BLOCKED`

Renderer or publisher states must not be used for content packages.

## Required Tracking

Every production package must track:

- package identity;
- domain and series ownership;
- canonical master path;
- TTS output path;
- word count;
- QA status;
- master-to-TTS coverage;
- active internal assets;
- archived assets;
- external processes explicitly marked `OUT_OF_SCOPE`;
- dependency paths for governing domain assets.

If the canonical master changes, `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` becomes stale until regenerated or revalidated.

## Gate Review Requirement

Package review is required before advancing to `READY_FOR_TTS_HANDOFF` or `CONTENT_PACKAGE_COMPLETE`.

Review must evaluate only content-package assets. It must not fail a package because downstream voice, subtitle, video, visual, metadata, or publishing assets do not exist.

## Handoff Rule

The final handoff is `OUTPUT/03_AUDIO_SCRIPT_TTS.txt`. This file is consumed by external TTS or production systems. The Production Engine must not mark external voice, video, or publishing work complete.
