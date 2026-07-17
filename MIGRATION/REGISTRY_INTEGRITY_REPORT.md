# Registry Integrity Report

Timestamp: 2026-07-14T09:49:15.2278023+07:00

| Check | Method | Result count | Status | Evidence |
|---|---|---:|---|---|
| Duplicate asset IDs | Group Asset Registry IDs | 0 | PASS | Asset IDs scanned: 101 |
| Duplicate canonical paths | Group Asset Registry canonical paths | 0 | PASS | Paths scanned: 101 |
| Backup references in registries | Search BACKUP/CUTOVER_BACKUP | 0 | PASS | Asset Registry scan |
| Missing registry paths | Test-Path each canonical path | 0 | PASS | Missing:  |
| Old IDs as independent assets | Regex old legacy IDs in Asset ID column | 0 | PASS | Old IDs should be aliases only |
| Shared libraries domain ownership | Inspect NPL_SHARED/EBL_SHARED | 2 | PASS | Registered as shared, owner CORE |
| Old ID aliases | Inspect ID Registry | 4 | PASS | Legacy aliases mapped |

## Result

Registry integrity is PASS for structural checks. Semantic canonical-owner review remains HUMAN_REVIEW_REQUIRED before any root legacy path is deprecated physically.
