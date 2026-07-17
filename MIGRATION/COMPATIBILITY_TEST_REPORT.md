# Compatibility Test Report

Timestamp: 2026-07-14T09:52:52.5167734+07:00

resolver_level: documented_mapping_only

runtime_resolution: not_implemented

| Type | Old value | New value | Mapping exists | Destination exists | Canonical destination | Resolver behavior documented | Ambiguous mapping | Validation status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| old-path | 02_BUDDHIST_GUIDE.md | DOMAINS/BUDDHISM/BUDDHIST_GUIDE.md | yes | True | DOMAINS/BUDDHISM/BUDDHIST_GUIDE.md | documented_mapping_only | no | PASS | canonical_owner=BUD_GUIDE; old_path_retained=true |
| old-path | KP_001_Kinh_Dia_Tang.md | DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS/KP_BUD_001_Kinh_Dia_Tang.md | yes | True | DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS/KP_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_owner=KP_BUD_001; old_path_retained=true |
| old-path | CK_001_Kinh_Dia_Tang.md | DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE/CK_BUD_001_Kinh_Dia_Tang.md | yes | True | DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE/CK_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_owner=CK_BUD_001; old_path_retained=true |
| old-path | SERIES_BIBLE_Kinh_Dia_Tang.md | DOMAINS/BUDDHISM/SERIES_BIBLES/SB_BUD_001_Kinh_Dia_Tang.md | yes | True | DOMAINS/BUDDHISM/SERIES_BIBLES/SB_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_owner=SB_BUD_001; old_path_retained=true |
| old-path | CHARACTER_BIBLE_Dia_Tang_Bo_Tat.md | DOMAINS/BUDDHISM/CHARACTER_BIBLES/CB_BUD_001_Dia_Tang_Bo_Tat.md | yes | True | DOMAINS/BUDDHISM/CHARACTER_BIBLES/CB_BUD_001_Dia_Tang_Bo_Tat.md | documented_mapping_only | no | PASS | canonical_owner=CB_BUD_001; old_path_retained=true |
| old-path | NARRATIVE_PATTERN_LIBRARY.md | SHARED_LIBRARIES/NARRATIVE_PATTERN_LIBRARY.md | yes | True | SHARED_LIBRARIES/NARRATIVE_PATTERN_LIBRARY.md | documented_mapping_only | no | PASS | canonical_owner=NPL_SHARED; old_path_retained=true |
| old-path | EPISODE_BLUEPRINT_LIBRARY.md | SHARED_LIBRARIES/EPISODE_BLUEPRINT_LIBRARY.md | yes | True | SHARED_LIBRARIES/EPISODE_BLUEPRINT_LIBRARY.md | documented_mapping_only | no | PASS | canonical_owner=EBL_SHARED; old_path_retained=true |
| old-path | kinh-dia-tang-1.txt | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-1.txt | yes | True | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-1.txt | documented_mapping_only | no | PASS | canonical_owner=SRC_BUD_001; old_path_retained=true |
| old-path | kinh-dia-tang-2.txt | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-2.txt | yes | True | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-2.txt | documented_mapping_only | no | PASS | canonical_owner=SRC_BUD_002; old_path_retained=true |
| old-path | kinh-dia-tang-3.txt | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-3.txt | yes | True | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-3.txt | documented_mapping_only | no | PASS | canonical_owner=SRC_BUD_003; old_path_retained=true |
| old-id | KP_001_Kinh_Dia_Tang | KP_BUD_001 | yes | True | DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS/KP_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_path=DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS/KP_BUD_001_Kinh_Dia_Tang.md |
| old-id | CK_001_Kinh_Dia_Tang | CK_BUD_001 | yes | True | DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE/CK_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_path=DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE/CK_BUD_001_Kinh_Dia_Tang.md |
| old-id | SERIES_BIBLE_Kinh_Dia_Tang | SB_BUD_001 | yes | True | DOMAINS/BUDDHISM/SERIES_BIBLES/SB_BUD_001_Kinh_Dia_Tang.md | documented_mapping_only | no | PASS | canonical_path=DOMAINS/BUDDHISM/SERIES_BIBLES/SB_BUD_001_Kinh_Dia_Tang.md |
| old-id | CHARACTER_BIBLE_Dia_Tang_Bo_Tat | CB_BUD_001 | yes | True | DOMAINS/BUDDHISM/CHARACTER_BIBLES/CB_BUD_001_Dia_Tang_Bo_Tat.md | documented_mapping_only | no | PASS | canonical_path=DOMAINS/BUDDHISM/CHARACTER_BIBLES/CB_BUD_001_Dia_Tang_Bo_Tat.md |

## Validation Evidence

| Validation name | Method | Files scanned | Result count | Evidence | Status |
|---|---|---|---:|---|---|
| Old path mapping validation | Parsed PATH_MAPPING.md and tested each destination with Test-Path | MIGRATION/PATH_MAPPING.md | 10 | backup destination references checked; old paths retained as compatibility copies | PASS |
| Old ID mapping validation | Parsed ID_MAPPING.md and tested each new canonical path with Test-Path | MIGRATION/ID_MAPPING.md | 4 | aliases resolve to canonical new IDs and paths | PASS |
| Ambiguity check | Counted ambiguous mapping markers | PATH_MAPPING.md; ID_MAPPING.md | 0 | expected 0 ambiguous mappings | PASS |
| Failure check | Counted non-PASS validation rows | PATH_MAPPING.md; ID_MAPPING.md | 0 | expected 0 failed rows | PASS |

## Result

Compatibility mapping is documented and structurally valid for old paths and old IDs. Runtime resolution is not implemented because this repository has documentation assets only.
