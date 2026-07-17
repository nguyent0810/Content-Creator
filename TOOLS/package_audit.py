#!/usr/bin/env python3
"""Package audit for content production packages, per DOMAIN_SPECIFICATION/PACKAGE_AUDIT_SPEC.md
and the schema_version 2.0 manifest (DOMAIN_SPECIFICATION/PRODUCTION_PACKAGE_MANIFEST_SCHEMA.json)."""
import difflib
import json
import re
import sys
from pathlib import Path

CONTENT_STATUS = {
    "DRAFTING", "READY_FOR_CONTENT_REVIEW", "CONTENT_REVISION_REQUIRED",
    "CONTENT_APPROVED", "READY_FOR_TTS_HANDOFF", "CONTENT_PACKAGE_COMPLETE", "BLOCKED",
}
QA_STATUS = {"NOT_RUN", "PASS", "PASS_WITH_ADVISORIES", "FAIL", "BLOCKED"}
REQUIRED_FIELDS = [
    "schema_version", "package_id", "episode_id", "domain_id", "series_id",
    "title", "language", "version", "content_status", "canonical_master",
    "tts_output", "word_count", "qa_status", "master_to_tts_coverage_percentage",
    "normalization_count", "external_processes", "dependencies",
    "active_internal_assets", "archived_assets", "updated_at",
]
CANONICAL_MASTER_PATH = "_INTERNAL/03_AUDIO_SCRIPT_MASTER.md"
TTS_OUTPUT_PATH = "OUTPUT/03_AUDIO_SCRIPT_TTS.txt"
ALLOWED_ROOT_ENTRIES = {"README.md", "OUTPUT", "_INTERNAL", "_ARCHIVE"}


def check(checks, check_id, category, name, status, severity, evidence, remediation=""):
    checks.append({
        "check_id": check_id,
        "category": category,
        "name": name,
        "status": status,
        "severity": severity,
        "evidence": evidence,
        "remediation": remediation,
    })


def fail_count(checks):
    return sum(1 for c in checks if c["status"] in {"FAIL", "BLOCKED"} and c["severity"] in {"CRITICAL", "HIGH"})


def warn_count(checks):
    return sum(1 for c in checks if c["status"] == "PASS_WITH_ADVISORY")


def find_project_root(pkg: Path) -> Path:
    for candidate in [pkg.resolve(), *pkg.resolve().parents]:
        if (candidate / "REGISTRIES" / "ASSET_REGISTRY.md").exists():
            return candidate
    return Path.cwd()


def parse_pipe_table(text: str, min_cols: int):
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < min_cols:
            continue
        if all(set(c) <= {"-"} for c in cells if c):
            continue
        if cells[0] in {"Asset ID", "Original path"}:
            continue
        rows.append(cells)
    return rows


def parse_asset_registry(root: Path):
    path = root / "REGISTRIES" / "ASSET_REGISTRY.md"
    registry = {}
    if not path.exists():
        return registry
    for cells in parse_pipe_table(path.read_text(encoding="utf-8-sig"), min_cols=6):
        asset_id, _asset_type, _domain, canonical_path, _owner, status = cells[:6]
        registry[asset_id] = {"path": canonical_path, "status": status}
    return registry


def parse_archive_manifest(pkg: Path):
    path = pkg / "_ARCHIVE" / "ARCHIVE_MANIFEST.md"
    entries = {}
    if not path.exists():
        return entries
    for cells in parse_pipe_table(path.read_text(encoding="utf-8-sig"), min_cols=8):
        _original_path, archive_path, _asset_type, _reason, _superseded_by, active_dep = cells[:6]
        entries[archive_path] = {"active_dependency_remaining": active_dep}
    return entries


def write_result(pkg, checks, package_id, content_status):
    blocking = fail_count(checks)
    warnings = warn_count(checks)
    result_status = "FAIL" if blocking else ("PASS_WITH_ADVISORIES" if warnings else "PASS")
    result = {
        "schema_version": "2.0",
        "package_id": package_id,
        "audit_timestamp": __import__("datetime").datetime.now().isoformat(),
        "audit_mode": "automated",
        "result": result_status,
        "content_status": content_status,
        "blocking_errors": blocking,
        "warnings": warnings,
        "checks": checks,
    }
    internal = pkg / "_INTERNAL"
    internal.mkdir(exist_ok=True)
    (internal / "PACKAGE_AUDIT_RESULT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Package Audit Report", "",
        f"Result: {result_status}", f"Content status: {content_status}",
        f"Blocking errors: {blocking}", f"Warnings: {warnings}", "",
        "| Check ID | Category | Status | Severity | Evidence |", "|---|---|---|---|---|",
    ]
    for c in checks:
        lines.append(f"| {c['check_id']} | {c['category']} | {c['status']} | {c['severity']} | {c['evidence']} |")
    (internal / "PACKAGE_AUDIT_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if blocking == 0 else 2


def main() -> int:
    pkg = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    root = find_project_root(pkg)
    manifest_path = pkg / "_INTERNAL" / "manifest.json"
    checks = []

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        check(checks, "PKG-SCHEMA-001", "schema", "manifest.json parses", "PASS", "CRITICAL", str(manifest_path))
    except Exception as exc:
        check(checks, "PKG-SCHEMA-001", "schema", "manifest.json parses", "FAIL", "CRITICAL", str(exc), "Fix manifest JSON.")
        return write_result(pkg, checks, package_id="UNKNOWN", content_status="UNKNOWN")

    # 1. Schema validation
    missing = [k for k in REQUIRED_FIELDS if k not in manifest]
    check(checks, "PKG-SCHEMA-002", "schema", "required manifest fields", "PASS" if not missing else "FAIL", "CRITICAL", f"missing={missing}", "Add required fields per PRODUCTION_PACKAGE_MANIFEST_SCHEMA.json.")
    check(checks, "PKG-SCHEMA-003", "schema", "schema_version is 2.0", "PASS" if manifest.get("schema_version") == "2.0" else "FAIL", "CRITICAL", str(manifest.get("schema_version")), "Migrate manifest to schema_version 2.0.")
    check(checks, "PKG-SCHEMA-004", "schema", "content_status valid", "PASS" if manifest.get("content_status") in CONTENT_STATUS else "FAIL", "CRITICAL", str(manifest.get("content_status")), "Use a supported content_status value.")
    check(checks, "PKG-SCHEMA-005", "schema", "qa_status valid", "PASS" if manifest.get("qa_status") in QA_STATUS else "FAIL", "CRITICAL", str(manifest.get("qa_status")), "Use a supported qa_status value.")
    check(checks, "PKG-SCHEMA-006", "schema", "canonical_master is the fixed contract path", "PASS" if manifest.get("canonical_master") == CANONICAL_MASTER_PATH else "FAIL", "CRITICAL", str(manifest.get("canonical_master")), f"canonical_master must be {CANONICAL_MASTER_PATH}.")
    check(checks, "PKG-SCHEMA-007", "schema", "tts_output is the fixed contract path", "PASS" if manifest.get("tts_output") == TTS_OUTPUT_PATH else "FAIL", "CRITICAL", str(manifest.get("tts_output")), f"tts_output must be {TTS_OUTPUT_PATH}.")

    # 2. Required asset validation
    required_assets = {manifest.get("canonical_master"), manifest.get("tts_output"), *manifest.get("active_internal_assets", [])}
    required_assets.discard(None)
    missing_assets = sorted(rel for rel in required_assets if not (pkg / rel).exists())
    empty_assets = sorted(rel for rel in required_assets if (pkg / rel).exists() and (pkg / rel).stat().st_size == 0)
    check(checks, "PKG-ASSET-001", "asset", "required assets exist", "PASS" if not missing_assets else "FAIL", "CRITICAL", f"missing={missing_assets}", "Create the asset or remove it from the manifest.")
    check(checks, "PKG-ASSET-002", "asset", "required assets non-empty", "PASS" if not empty_assets else "FAIL", "HIGH", f"empty={empty_assets}", "Populate empty assets.")

    # 3. Dependency validation
    dependencies = manifest.get("dependencies", [])
    dep_missing = sorted(d.get("path", "") for d in dependencies if not (root / d.get("path", "")).exists())
    dep_in_archive = sorted(d.get("path", "") for d in dependencies if "_ARCHIVE/" in d.get("path", "") or "BACKUP" in d.get("path", "").upper())
    check(checks, "PKG-DEP-001", "dependency", "dependency paths exist", "PASS" if not dep_missing else "FAIL", "HIGH", f"missing={dep_missing}", "Fix dependency paths.")
    check(checks, "PKG-DEP-002", "dependency", "no dependency points at an archive/backup path", "PASS" if not dep_in_archive else "FAIL", "CRITICAL", f"archived={dep_in_archive}", "Point dependencies at active canonical paths, not archived/backup copies.")

    # 4/8. Registry validation
    registry = parse_asset_registry(root)
    registry_unknown = sorted(d.get("asset_id") for d in dependencies if d.get("asset_id") not in registry)
    registry_mismatches = sorted(d.get("asset_id") for d in dependencies if d.get("asset_id") in registry and registry[d["asset_id"]]["path"] != d.get("path"))
    registry_inactive = sorted(d.get("asset_id") for d in dependencies if d.get("asset_id") in registry and registry[d["asset_id"]]["status"] != "active")
    check(checks, "PKG-REG-001", "registry", "dependency asset_id known in ASSET_REGISTRY", "PASS" if not registry_unknown else "FAIL", "HIGH", f"unknown={registry_unknown}", "Register the asset in REGISTRIES/ASSET_REGISTRY.md or fix the asset_id.")
    check(checks, "PKG-REG-002", "registry", "dependency path matches registry canonical path", "PASS" if not registry_mismatches else "FAIL", "HIGH", f"mismatched={registry_mismatches}", "Update the dependency path to match the registry's canonical path.")
    check(checks, "PKG-REG-003", "registry", "dependency asset is active in registry", "PASS" if not registry_inactive else "FAIL", "MEDIUM", f"inactive={registry_inactive}", "Do not depend on non-active registry assets.")

    # 5. Canonical/derived + TTS validation
    master_rel = manifest.get("canonical_master")
    master_text = ""
    has_markers = False
    if master_rel and (pkg / master_rel).exists():
        master_text = (pkg / master_rel).read_text(encoding="utf-8-sig")
        has_markers = "<!-- NARRATION_START -->" in master_text and "<!-- NARRATION_END -->" in master_text
    check(checks, "PKG-TTS-001", "tts", "master narration markers exist", "PASS" if has_markers else "FAIL", "CRITICAL", master_rel, "Wrap narration in <!-- NARRATION_START/END --> markers.")

    tts_rel = manifest.get("tts_output")
    if has_markers and tts_rel and (pkg / tts_rel).exists():
        narration = re.search(r"(?s)<!-- NARRATION_START -->\s*(.*?)\s*<!-- NARRATION_END -->", master_text).group(1).strip()
        tts = (pkg / tts_rel).read_text(encoding="utf-8-sig")
        clean = not re.search(r"^#|^---|<!--|^\|---|\[[A-Z_ ]+\]|Episode ID|Package ID", tts, re.M)
        check(checks, "PKG-TTS-002", "tts", "TTS plain text cleanliness", "PASS" if clean else "FAIL", "CRITICAL", tts_rel, "Remove metadata/Markdown from the TTS output.")

        coverage = round(difflib.SequenceMatcher(None, narration.strip(), tts.strip()).ratio() * 100, 2)
        declared = manifest.get("master_to_tts_coverage_percentage")
        coverage_ok = coverage >= 99.5
        declared_honest = isinstance(declared, (int, float)) and abs(declared - coverage) <= 1.0
        check(checks, "PKG-DERIVE-001", "derivation", "MASTER-to-TTS coverage >= 99.5%", "PASS" if coverage_ok else "FAIL", "CRITICAL", f"measured={coverage}%", "Regenerate the TTS output from the master narration.")
        check(checks, "PKG-DERIVE-002", "derivation", "declared coverage percentage is honest", "PASS" if declared_honest else "PASS_WITH_ADVISORY", "MEDIUM", f"declared={declared}%, measured={coverage}%", "Recompute master_to_tts_coverage_percentage after edits.")
    else:
        check(checks, "PKG-TTS-002", "tts", "TTS output exists", "FAIL", "CRITICAL", "missing tts_output or narration markers", "Create the TTS output derived from the master.")

    # 6. Structure validation
    extra_root = sorted(e.name for e in pkg.iterdir() if e.name not in ALLOWED_ROOT_ENTRIES)
    check(checks, "PKG-STRUCT-001", "structure", "package root contains only README.md, OUTPUT/, _INTERNAL/, _ARCHIVE/", "PASS" if not extra_root else "FAIL", "MEDIUM", f"extra={extra_root}", "Move stray files into _INTERNAL/, OUTPUT/, or _ARCHIVE/.")

    # 7. Archive validation
    archive_dir = pkg / "_ARCHIVE"
    archive_entries = parse_archive_manifest(pkg)
    unlisted, dangling_active_dep = [], []
    if archive_dir.exists():
        for f in archive_dir.rglob("*"):
            if f.is_file() and f.name != "ARCHIVE_MANIFEST.md":
                rel = f.relative_to(pkg).as_posix()
                if rel not in archive_entries:
                    unlisted.append(rel)
        dangling_active_dep = sorted(rel for rel, e in archive_entries.items() if e["active_dependency_remaining"].lower() == "true")
    check(checks, "PKG-ARCHIVE-001", "archive", "archived files listed in ARCHIVE_MANIFEST.md", "PASS" if not unlisted else "FAIL", "MEDIUM", f"unlisted={sorted(unlisted)}", "Add missing rows to _ARCHIVE/ARCHIVE_MANIFEST.md.")
    check(checks, "PKG-ARCHIVE-002", "archive", "no archived file still marked as an active dependency", "PASS" if not dangling_active_dep else "FAIL", "HIGH", f"active_dependency_remaining={dangling_active_dep}", "Resolve or remove the active dependency before archiving the file.")

    # 9. External-scope validation
    ext = manifest.get("external_processes", {})
    out_of_scope_ok = all(ext.get(k) == "OUT_OF_SCOPE" for k in ("voice_render", "video_render", "publish"))
    check(checks, "PKG-SCOPE-001", "scope", "voice_render/video_render/publish remain OUT_OF_SCOPE", "PASS" if out_of_scope_ok else "FAIL", "HIGH", str(ext), "This audit only covers packages through TTS handoff; do not mark render/publish stages complete here.")

    return write_result(pkg, checks, package_id=manifest.get("package_id"), content_status=manifest.get("content_status"))


if __name__ == "__main__":
    raise SystemExit(main())
