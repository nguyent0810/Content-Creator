# Production Package Specification

## Purpose

A Production Package is the lifecycle-managed unit for an episode content package. It is not a loose folder of peer Markdown files and it is not a renderer, publisher, or media-production workspace.

The canonical package scope is:

1. Research source material.
2. Episode planning.
3. Canonical master narration.
4. Content and derivation QA.
5. Plain-text TTS handoff output.
6. Archive records for superseded or unused files.

Voice rendering, video rendering, subtitle alignment, visual production, metadata finalization, publishing, and platform upload are external processes. They may consume the TTS handoff output, but they must not be represented as completed inside the content package unless a separate downstream system creates its own governed package.

## Canonical Folder Layout

Each package root must contain only:

| Path | Required | Purpose |
|---|---:|---|
| `README.md` | yes | Human entry point and usage instructions. |
| `OUTPUT/` | yes | User-facing handoff output. |
| `_INTERNAL/` | yes | Active editorial, QA, manifest, review, and source files. |
| `_ARCHIVE/` | yes | Superseded, unused, migrated, or review-history files. |

No active production file should remain as a peer of these folders at package root.

## Source Of Truth

`_INTERNAL/manifest.json` is the machine-readable source of truth for package identity, active assets, status, derivation coverage, QA state, and out-of-scope external processes.

`README.md` is a human-readable entry point. If `README.md` contradicts `_INTERNAL/manifest.json`, the package must fail review until corrected.

`status.md` is not part of the active canonical package structure. Legacy `status.md` files must be archived under `_ARCHIVE/` and must not be used for current lifecycle decisions.

## Asset Classes

| Class | Definition | Active location | Examples |
|---|---|---|---|
| canonical editorial asset | Asset that owns editorial source content for a package | `_INTERNAL/` | Research Brief, Episode Planner, Audio Script Master |
| derived handoff asset | Asset generated from a canonical source without independent editorial authority | `OUTPUT/` | `03_AUDIO_SCRIPT_TTS.txt` |
| internal review asset | Supporting review, QA, or source-control record | `_INTERNAL/` | QA Report, Review Summary, Source Claim Matrix |
| archive asset | Superseded, unused, legacy, or historical file retained for auditability | `_ARCHIVE/` | Legacy visual brief, metadata draft, superseded manifest |
| external process | Work intentionally outside content-package scope | none | voice render, video render, publish |

Rendered assets and publication exports are not active asset classes in this content-package specification.

## Required Content Package Profile

The canonical production profile is `CONTENT_PACKAGE`.

`CONTENT_PACKAGE` always evaluates only the assets required to reach TTS handoff. It must not fail because downstream voice, subtitle, video, metadata, or publishing assets do not exist.

## Required Active Assets

| Path | Required | Role |
|---|---:|---|
| `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` | yes | Plain-text TTS handoff file. |
| `_INTERNAL/manifest.json` | yes | Machine-readable package source of truth. |
| `_INTERNAL/01_RESEARCH_BRIEF.md` | yes | Research foundation. |
| `_INTERNAL/02_EPISODE_PLANNER.md` | yes | Editorial and structural plan. |
| `_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` | yes | Canonical narration source. |
| `_INTERNAL/06_QA_REPORT.md` | yes | Content and derivation QA record. |
| `_INTERNAL/REVIEW_SUMMARY.md` | yes | Human-readable current package review summary. |
| `_ARCHIVE/ARCHIVE_MANIFEST.md` | yes | Record of archived files and retention state. |

Optional active internal assets such as `SOURCE_CLAIM_MATRIX.md`, `RESEARCH_GAPS.md`, `TERMINOLOGY_MAP.md`, and `CHARACTER_USAGE_PLAN.md` may exist in `_INTERNAL/` when they are needed for research traceability or editorial review.

## Allowed Content Status Values

| Status | Meaning |
|---|---|
| `DRAFTING` | Package content is being drafted and is not ready for review. |
| `READY_FOR_CONTENT_REVIEW` | Research, planner, and master script are ready for content review. |
| `CONTENT_REVISION_REQUIRED` | Content review found issues requiring revision. |
| `CONTENT_APPROVED` | Canonical content has passed content review. |
| `READY_FOR_TTS_HANDOFF` | Clean TTS text has been derived and validated from the canonical master. |
| `CONTENT_PACKAGE_COMPLETE` | Package is structurally complete for content handoff. |
| `BLOCKED` | Work cannot progress because a required upstream dependency is missing or invalid. |

No package may use renderer or publication states such as `READY_FOR_VIDEO`, `READY_TO_PUBLISH`, `PUBLISHED`, `VOICE_RENDERED`, or `VIDEO_RENDERED` under this specification.

## Required Production Flow

Research -> Episode Planner -> Master Script -> Content QA -> TTS-clean output -> External handoff.

The system must stop at external handoff. Downstream tools may consume `OUTPUT/03_AUDIO_SCRIPT_TTS.txt`, but this package must not fabricate or imply completion of downstream work.

## Canonical Narration Rule

`_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` is the canonical narration asset. It must contain stable narration markers:

```text
<!-- NARRATION_START -->
...
<!-- NARRATION_END -->
```

`OUTPUT/03_AUDIO_SCRIPT_TTS.txt` is a derived handoff asset and must never become the canonical narration source.

## TTS Output Rule

`OUTPUT/03_AUDIO_SCRIPT_TTS.txt` must contain only spoken narration intended for TTS.

It must not contain:

- Markdown headings.
- YAML front matter.
- HTML comments.
- Speaker labels.
- Editorial notes.
- QA notes.
- Source citations.
- Metadata.
- Subtitle timing.
- Visual direction.
- Production instructions.

## Archive Rule

Files that are superseded, unused, deprecated, or outside current content-package scope must be moved to `_ARCHIVE/`, not deleted.

Every archived file must be listed in `_ARCHIVE/ARCHIVE_MANIFEST.md` with:

- original path;
- archive path;
- asset type;
- archive reason;
- superseded-by value when applicable;
- active dependency remaining;
- safe-to-delete-later status;
- human-review-required status.

Archived files must not remain active dependencies in registries or current manifests.
