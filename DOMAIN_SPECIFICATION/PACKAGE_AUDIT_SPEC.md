# Package Audit Specification

Package Audit is a quality gate for content production packages through TTS handoff. It is not a media-rendering, subtitle-finalization, metadata-publication, upload, or publishing audit.

## Audit Groups

1. Schema validation: `_INTERNAL/manifest.json` parses, required fields exist, schema version is `2.0`, and content status values are valid.
2. Required asset validation: required content-package assets exist and are non-empty.
3. Dependency validation: dependency paths and IDs resolve, no backup path is used, and archived files are not active dependencies.
4. Canonical/derived validation: `_INTERNAL/03_AUDIO_SCRIPT_MASTER.md` is the canonical master narration source and `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` is derived from it.
5. TTS validation: plain text only, no metadata, no Markdown, no labels, no comments, no production notes, and 100 percent narration coverage unless explicit human approval states otherwise.
6. Structure validation: package root contains only `README.md`, `OUTPUT/`, `_INTERNAL/`, and `_ARCHIVE/`.
7. Archive validation: superseded, unused, migrated, or out-of-scope files are in `_ARCHIVE/` and listed in `_ARCHIVE/ARCHIVE_MANIFEST.md`.
8. Registry validation: active registries point only to current active paths or governing system paths; no active registry row points to old root-level package assets.
9. External-scope validation: `voice_render`, `video_render`, and `publish` remain `OUT_OF_SCOPE`.

## Out-of-Scope Checks

The default package audit must not require:

- voice render files;
- video render files;
- final SRT files;
- subtitle segment JSON;
- visual brief files;
- metadata publication files;
- production-summary files;
- upload or publish evidence.

If a downstream workflow needs those assets, it must create a separate governed package or revive archived material through human review.

## Audit Result

Audit results may be recorded in `_INTERNAL/06_QA_REPORT.md`, `_INTERNAL/REVIEW_SUMMARY.md`, and `_INTERNAL/manifest.json`.

`PACKAGE_AUDIT_RESULT.json` is optional and must be archived when it is not part of the active content-package scope.

Check status values: `PASS`, `PASS_WITH_ADVISORY`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`.

Severity values: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
