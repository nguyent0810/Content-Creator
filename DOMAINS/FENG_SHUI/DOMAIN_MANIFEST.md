---
schema_version: 1.0
domain_id: FS
domain_name: Feng Shui
status: active
domain_guide: DOMAIN_GUIDE.md
default_language: vi
source_registry: SOURCES/SOURCE_REGISTRY.md
glossary: GLOSSARY/DOMAIN_GLOSSARY.md
qa_policy: DOMAIN_QA/DOMAIN_QA_POLICY.md
knowledge_packet_prefix: KP_FS
creative_packet_prefix: CK_FS
character_bible_prefix: CB_FS
series_bible_prefix: SB_FS
risk_level: high
---

# Feng Shui Domain Manifest (Tử Vi & Phong Thủy)

Status: active (updated 2026-07-24). Full foundation complete: `DOMAIN_GUIDE.md`, `SOURCES/SOURCE_REGISTRY.md`, `GLOSSARY/DOMAIN_GLOSSARY.md`, `DOMAIN_QA/DOMAIN_QA_POLICY.md`, two foundational Knowledge Packets (`KP_FS_001_Phong_Thuy.md`, `KP_FS_002_Tu_Vi.md`), one Creative Knowledge packet (`CK_FS_001_Tu_Vi_Phong_Thuy.md`), one Series Bible (`SB_FS_001_Tu_Vi_Phong_Thuy.md`, series name "Giải Mã Tử Vi Phong Thủy"), and a 17-episode Season 1 production plan (`SERIES_BIBLES/SEASON_01_PRODUCTION_PLAN.md`, locked 2026-07-20). All content packets are marked `draft-pending-human-review` — a solid production-ready foundation with explicitly flagged lower-confidence details (see each packet's gap notes and `SOURCE_REGISTRY.md`'s "Known Gaps"), not a fully closed-out reference. Character Bibles have not been built (this domain has no deity/character-figure equivalent the way Buddhism does — legendary figures like Trần Đoàn are covered inside `KP_FS_002` instead). **First independent QA pass completed 2026-07-24** across all foundational assets (KP_FS_001/002, CK_FS_001, SB_FS_001, Season Plan, EP015_016 case study) — found and fixed a fabricated-source claim in KP_FS_001's Khí section plus several smaller consistency issues; see each asset's `_QA_REPORT_*.md`. **First production package (2026-07-24):** `PRODUCTION_PACKAGES/TU_VI_PHONG_THUY/EP001/` (Season 1 Episode 1) validated the full pipeline end-to-end — `TOOLS/package_audit.py` result: PASS, 0 blocking, 0 warnings. This is a pipeline-validation test, not a publish-ready package; human sign-off is still required before real use.

