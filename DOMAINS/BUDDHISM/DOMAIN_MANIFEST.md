---
schema_version: 1.0
domain_id: BUD
domain_name: Buddhism
status: active
domain_guide: BUDDHIST_GUIDE.md
default_language: vi
source_registry: SOURCES/SOURCE_REGISTRY.md
glossary: GLOSSARY/DOMAIN_GLOSSARY.md
qa_policy: DOMAIN_QA/DOMAIN_QA_POLICY.md
knowledge_packet_prefix: KP_BUD
creative_packet_prefix: CK_BUD
character_bible_prefix: CB_BUD
series_bible_prefix: SB_BUD
risk_level: high
---

# Buddhism Domain Manifest

Buddhism is the first active domain. Canonical Buddhist assets migrated from the legacy root are preserved by checksum and mapped through registries. Domain generation must use this manifest, BUDDHIST_GUIDE.md, SOURCE_REGISTRY.md, DOMAIN_GLOSSARY.md, and DOMAIN_QA_POLICY.md.

**Domain expansion beyond Kinh Địa Tạng (2026-07-24):** per explicit channel-owner direction that this domain should eventually cover "mọi khía cạnh của Phật giáo" (all aspects of Buddhism), not just one sutra, two new foundational Knowledge Packets were added: `KP_BUD_002_Bat_Nha_Tam_Kinh.md` (Bát Nhã Tâm Kinh / Heart Sutra) and `KP_BUD_003_Kinh_A_Di_Da_Tinh_Do.md` (Kinh A Di Đà / Pure Land — activates the previously-unused `CB_BUD_004`/`CB_BUD_005` character bibles). Both `status: draft-pending-human-review`, not yet through independent QA. `SB_BUD_001` remains scoped to Kinh Địa Tạng production; a new Series Bible or season would be needed before these two new Knowledge Packets can drive actual episode production.
