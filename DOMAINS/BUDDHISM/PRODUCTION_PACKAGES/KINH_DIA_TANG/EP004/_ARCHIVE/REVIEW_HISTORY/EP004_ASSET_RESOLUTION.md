# EP004 Asset Resolution

## Execution Context

| Field | Value |
|---|---|
| episode_id | EP_BUD_KDT_004 |
| primary_domain | BUD |
| domain_status | active |
| series_id | SB_BUD_001 |
| legacy_fallback_used | false |
| root_legacy_files_used_as_canonical_input | none |
| resolver_level | documented_mapping_only |
| runtime_resolution | not_implemented |

## Required Asset Resolution

| Asset role | Expected ID | Resolved ID | Canonical path | Asset version | Domain owner | Exists | Loaded successfully | Legacy fallback used | Dependency status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Buddhism Domain Manifest | BUD | BUD | DOMAINS/BUDDHISM/DOMAIN_MANIFEST.md | schema_version 1.0 | BUD | true | true | false | required | active manifest |
| Buddhist Guide | BUD_GUIDE | BUD_GUIDE | DOMAINS/BUDDHISM/BUDDHIST_GUIDE.md | migrated-20260714 | BUD | true | true | false | required | doctrinal and safety guide |
| Source Registry | BUD_SOURCE_REGISTRY | BUD_SOURCE_REGISTRY | DOMAINS/BUDDHISM/SOURCES/SOURCE_REGISTRY.md | migrated-20260714 | BUD | true | true | false | required | source metadata incomplete |
| Domain Glossary | BUD_GLOSSARY | BUD_GLOSSARY | DOMAINS/BUDDHISM/GLOSSARY/DOMAIN_GLOSSARY.md | migrated-20260714 | BUD | true | true | false | required | high-level glossary |
| Domain QA Policy | BUD_QA | BUD_QA | DOMAINS/BUDDHISM/DOMAIN_QA/DOMAIN_QA_POLICY.md | migrated-20260714 | BUD | true | true | false | required | high-risk Buddhist QA |
| Knowledge Packet | KP_BUD_001 | KP_BUD_001 | DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS/KP_BUD_001_Kinh_Dia_Tang.md | migrated-20260714 | BUD | true | true | false | required | primary packet |
| Creative Knowledge | CK_BUD_001 | CK_BUD_001 | DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE/CK_BUD_001_Kinh_Dia_Tang.md | migrated-20260714 | BUD | true | true | false | required for framing | not doctrinal evidence |
| Series Bible | SB_BUD_001 | SB_BUD_001 | DOMAINS/BUDDHISM/SERIES_BIBLES/SB_BUD_001_Kinh_Dia_Tang.md | migrated-20260714 | BUD | true | true | false | required | series continuity |
| Character Bible | CB_BUD_001 | CB_BUD_001 | DOMAINS/BUDDHISM/CHARACTER_BIBLES/CB_BUD_001_Dia_Tang_Bo_Tat.md | migrated-20260714 | BUD | true | true | false | required for Địa Tạng | no Buddha/Maya bible |
| Narrative Pattern Library | NPL_SHARED | NPL_SHARED | SHARED_LIBRARIES/NARRATIVE_PATTERN_LIBRARY.md | migrated-20260714 | CORE | true | true | false | shared | structure only |
| Episode Blueprint Library | EBL_SHARED | EBL_SHARED | SHARED_LIBRARIES/EPISODE_BLUEPRINT_LIBRARY.md | migrated-20260714 | CORE | true | true | false | shared | outline only |
| Core Research Engine | CORE_RESEARCH_ENGINE | CORE_RESEARCH_ENGINE | CORE_OS/RESEARCH_ENGINE.md | migrated-20260714 | CORE | true | true | false | required | research workflow |
| Core Content Engine | CORE_CONTENT_ENGINE | CORE_CONTENT_ENGINE | CORE_OS/CONTENT_ENGINE.md | migrated-20260714 | CORE | true | true | false | required | content workflow |
| Core QA Engine | CORE_QA_ENGINE | CORE_QA_ENGINE | CORE_OS/QA_ENGINE.md | migrated-20260714 | CORE | true | true | false | required | QA workflow |

## Source Assets

| Source asset ID | Canonical path | Exists | Metadata completeness | Planning use |
|---|---|---|---|---|
| SRC_BUD_001 | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-1.txt | true | INCOMPLETE | primary internal locator for Đao Lợi and hiếu framing |
| SRC_BUD_002 | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-2.txt | true | INCOMPLETE | optional reflective support, not canonical proof |
| SRC_BUD_003 | DOMAINS/BUDDHISM/SOURCES/kinh-dia-tang-3.txt | true | INCOMPLETE | optional vow context, not Episode 4 proof |

## Asset Gaps

| Gap | Status | Effect |
|---|---|---|
| Dedicated Character Bible for Đức Phật | CHARACTER_ASSET_GAP | Use only source-bound and guide-bound references. |
| Dedicated Character Bible for Ma-da/Ma Gia phu nhân | CHARACTER_ASSET_GAP | Use only name and relationship until approved. |
| Verified bibliographic source for Kinh Địa Tạng | HUMAN_REVIEW_REQUIRED | Scriptwriting remains closed. |

## Decision

`episode_status: PLANNING_ALLOWED_WITH_LIMITATIONS`
