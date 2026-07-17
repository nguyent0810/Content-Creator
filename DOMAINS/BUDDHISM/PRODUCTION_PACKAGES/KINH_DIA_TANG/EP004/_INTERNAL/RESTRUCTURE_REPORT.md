# Previous Structure

EP004 previously had production, research, audit, subtitle, visual, metadata, migration, and compatibility files as peer files at package root.

# New Structure

Package root now contains only OUTPUT/, _INTERNAL/, _ARCHIVE/, and README.md.

# Files Moved to OUTPUT

- OUTPUT/03_AUDIO_SCRIPT_TTS.txt

# Files Moved to INTERNAL

- _INTERNAL/01_RESEARCH_BRIEF.md
- _INTERNAL/02_EPISODE_PLANNER.md
- _INTERNAL/03_AUDIO_SCRIPT_MASTER.md
- _INTERNAL/06_QA_REPORT.md
- _INTERNAL/CHARACTER_USAGE_PLAN.md
- _INTERNAL/manifest.json
- _INTERNAL/RESEARCH_GAPS.md
- _INTERNAL/REVIEW_SUMMARY.md
- _INTERNAL/SOURCE_CLAIM_MATRIX.md
- _INTERNAL/TERMINOLOGY_MAP.md

# Files Moved to ARCHIVE

- _ARCHIVE/ARCHIVE_MANIFEST.md
- _ARCHIVE/MIGRATION_HISTORY/EP004_BACKUP_MANIFEST.md
- _ARCHIVE/MIGRATION_HISTORY/EP004_MANIFEST.md
- _ARCHIVE/MIGRATION_HISTORY/PRODUCTION_MIGRATION_BACKUP_MANIFEST.md
- _ARCHIVE/MIGRATION_HISTORY/PRODUCTION_MIGRATION_REPORT.md
- _ARCHIVE/REVIEW_HISTORY/EP004_ASSET_RESOLUTION.md
- _ARCHIVE/REVIEW_HISTORY/EP004_EPISODE_PLAN.md
- _ARCHIVE/REVIEW_HISTORY/EP004_QA_PLAN.md
- _ARCHIVE/REVIEW_HISTORY/EP004_READINESS_REPORT.md
- _ARCHIVE/REVIEW_HISTORY/EP004_RESEARCH_BRIEF.md
- _ARCHIVE/REVIEW_HISTORY/EP004_VISUAL_RESEARCH_REQUIREMENTS.md
- _ARCHIVE/SUPERSEDED_FILES/03_AUDIO_SCRIPT.md
- _ARCHIVE/SUPERSEDED_FILES/manifest.v1.json
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/03_SUBTITLE_SEGMENTS.json
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/04_VISUAL_BRIEF.md
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/05_METADATA.md
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/05_METADATA_DRAFT.md
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/07_PRODUCTION_SUMMARY.md
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/PACKAGE_AUDIT_REPORT.md
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/PACKAGE_AUDIT_RESULT.json
- _ARCHIVE/UNUSED_PRODUCTION_ASSETS/status.md

# Files Retained at Root

- README.md: human entry point and output path pointer.

# References Updated

- _INTERNAL/manifest.json now points to _INTERNAL/03_AUDIO_SCRIPT_MASTER.md and OUTPUT/03_AUDIO_SCRIPT_TTS.txt.
- README points ordinary users to OUTPUT/03_AUDIO_SCRIPT_TTS.txt.
- Review Summary gives regeneration instructions from Master to TTS.

# Registry Updates

Registry paths were updated to active minimal paths and archived files are no longer active dependencies.

# Compatibility Notes

Old root-level 03_AUDIO_SCRIPT_TTS.txt was moved to OUTPUT/03_AUDIO_SCRIPT_TTS.txt. No compatibility copy is kept because no active consumer was identified. Use the new path going forward.

# QA Results

- Output QA: PASS.
- Internal QA: PASS.
- Structure QA: PASS.
- Manifest QA: PASS.
- Master-to-TTS coverage: PASS, 100%.
- Registry integrity: PASS.
- Broken active references: 0.

# Remaining Human Review

Human review remains required before publication for citation/copyright and any future visual/metadata/subtitle package revived from archive.

# Final Status

COMPLETED. EP004 is now a minimal content package scoped to Research -> Planning -> Writing -> Content QA -> clean TTS export.
