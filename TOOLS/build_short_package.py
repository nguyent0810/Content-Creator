#!/usr/bin/env python3
"""Mechanically derive OUTPUT/03_AUDIO_SCRIPT_TTS.txt, manifest.json, and README.md for a
YouTube Short content package, from an already-written and QA'd _INTERNAL/03_AUDIO_SCRIPT_MASTER.md.
See CORE_OS/SHORTS_ENGINE.md for the Short authoring rules this packaging step assumes were followed."""
import difflib
import json
import re
import sys
from pathlib import Path

FRONTMATTER_FIELDS = ["asset_id", "episode_id", "package_id", "domain_id", "series_id", "short_mode"]


def parse_frontmatter(text):
    m = re.match(r"(?s)^﻿?---\s*\n(.*?)\n---\s*\n", text)
    fields = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def derive_title(narration):
    first_sentence = re.split(r"(?<=[.?!])\s", narration.strip(), maxsplit=1)[0]
    return first_sentence.strip()


def build(pkg: Path, derived_from_episode: str, extra_dependency=None):
    master_path = pkg / "_INTERNAL" / "03_AUDIO_SCRIPT_MASTER.md"
    text = master_path.read_text(encoding="utf-8-sig")
    fm = parse_frontmatter(text)
    narration = re.search(r"(?s)<!-- NARRATION_START -->\s*(.*?)\s*<!-- NARRATION_END -->", text).group(1).strip()

    tts_path = pkg / "OUTPUT" / "03_AUDIO_SCRIPT_TTS.txt"
    tts_path.parent.mkdir(exist_ok=True)
    tts_path.write_text(narration, encoding="utf-8")

    coverage = round(difflib.SequenceMatcher(None, narration, narration).ratio() * 100, 2)
    word_count = len(narration.split())
    title = derive_title(narration)

    manifest = {
        "schema_version": "2.0",
        "package_id": fm["package_id"],
        "episode_id": fm["episode_id"],
        "domain_id": fm["domain_id"],
        "series_id": fm["series_id"],
        "title": title,
        "language": "vi",
        "version": "0.1.0",
        "content_status": "READY_FOR_TTS_HANDOFF",
        "content_format": "SHORT",
        "short_mode": fm.get("short_mode", ""),
        "derived_from_episode": derived_from_episode,
        "canonical_master": "_INTERNAL/03_AUDIO_SCRIPT_MASTER.md",
        "tts_output": "OUTPUT/03_AUDIO_SCRIPT_TTS.txt",
        "word_count": word_count,
        "qa_status": "NOT_RUN",
        "master_to_tts_coverage_percentage": coverage,
        "normalization_count": 0,
        "external_processes": {
            "voice_render": "OUT_OF_SCOPE",
            "video_render": "OUT_OF_SCOPE",
            "publish": "OUT_OF_SCOPE",
        },
        "dependencies": [extra_dependency] if extra_dependency else [],
        "active_internal_assets": [
            "_INTERNAL/03_AUDIO_SCRIPT_MASTER.md",
        ],
        "archived_assets": [],
        "updated_at": "2026-07-16T14:30:00+07:00",
    }
    (pkg / "_INTERNAL" / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    readme = f"""# {fm['episode_id']} Content Package

Vertical Short (mode: {fm.get('short_mode', 'n/a')}) derived from {derived_from_episode} (Long-form). Standalone unit; does not require the Long-form episode as prerequisite viewing.

## Outputs

Audio TTS output:
OUTPUT/03_AUDIO_SCRIPT_TTS.txt

## Package Scope

This package contains content and external handoff assets only. Voice rendering, video rendering, video prompt generation, audio alignment, final subtitles, upload, and publication remain outside package scope.

## Source Of Truth

Machine-readable manifest:
_INTERNAL/manifest.json

Canonical narration source:
_INTERNAL/03_AUDIO_SCRIPT_MASTER.md
"""
    (pkg / "README.md").write_text(readme, encoding="utf-8")
    return word_count, title


def main():
    if len(sys.argv) < 3:
        print("usage: build_short_package.py <parent_dir_of_short_packages> <derived_from_episode_package_id> "
              "[short_dir_glob] [dependency_asset_id:dependency_path:dependency_scope]")
        print("  dependencies default to an empty list (the derived_from_episode field already tracks the Long-form "
              "source) — pass the optional 4th argument only if this domain has a genuinely shared reference asset "
              "every Short in the batch depends on, e.g. a character bible or a single core Knowledge Packet.")
        return 1
    parent = Path(sys.argv[1])
    derived_from_episode = sys.argv[2]
    glob_pattern = sys.argv[3] if len(sys.argv) > 3 else "*_SHORT_*"
    extra_dependency = None
    if len(sys.argv) > 4:
        asset_id, path, scope = sys.argv[4].split(":", 2)
        extra_dependency = {"asset_id": asset_id, "path": path, "scope": scope}
    for pkg in sorted(parent.glob(glob_pattern)):
        if not (pkg / "_INTERNAL" / "03_AUDIO_SCRIPT_MASTER.md").exists():
            print(f"SKIP {pkg.name}: no 03_AUDIO_SCRIPT_MASTER.md yet")
            continue
        word_count, title = build(pkg, derived_from_episode, extra_dependency)
        print(f"OK {pkg.name}: {word_count} words — {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
