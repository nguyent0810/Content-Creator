# Current State Audit

Repository root: D:\Media\TTS\Kinh địa tạng

Files before migration: 22. Domain-specific Buddhist content was hardcoded in root-level operating documents. No Git repository was detected or initialized.

| Current path | Detected role | Target layer | Target domain | Canonical status | Recommended action | Dependency risk | Migration risk | Human review required |
|---|---|---|---|---|---|---|---|---|
| PROJECT_PRD.md | legacy Buddhist PRD | DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/LEGACY_GOVERNANCE | BUD | legacy-retained | compatibility-copy | high | medium | yes: core/domain split |
| 01_BRAND_BIBLE.md | legacy Buddhist brand bible | DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/LEGACY_GOVERNANCE | BUD | legacy-retained | compatibility-copy | high | medium | yes: domain-specific brand |
| 02_BUDDHIST_GUIDE.md | Buddhist domain guide | DOMAINS/BUDDHISM | BUD | canonical | compatibility-copy | high | low | no |
| 03_CONTENT_ARCHITECTURE.md..11_KNOWLEDGE_MODEL.md | legacy Buddhist operating docs | DOMAINS/BUDDHISM/PRODUCTION_PACKAGES/LEGACY_GOVERNANCE and generic CORE_OS replacements | BUD/Core split | legacy-retained | compatibility-copy + new abstraction | high | medium | yes: legacy docs mention Buddhism |
| NARRATIVE_PATTERN_LIBRARY.md | shared narrative library | SHARED_LIBRARIES | shared | canonical shared | compatibility-copy | medium | low | no |
| EPISODE_BLUEPRINT_LIBRARY.md | shared episode blueprint library | SHARED_LIBRARIES | shared | canonical shared | compatibility-copy | medium | low | no |
| KP_001_Kinh_Dia_Tang.md | Buddhist knowledge packet | DOMAINS/BUDDHISM/KNOWLEDGE_PACKETS | BUD | canonical | compatibility-copy to KP_BUD_001 | high | low | no |
| CK_001_Kinh_Dia_Tang.md | Buddhist creative knowledge | DOMAINS/BUDDHISM/CREATIVE_KNOWLEDGE | BUD | canonical | compatibility-copy to CK_BUD_001 | high | low | no |
| SERIES_BIBLE_Kinh_Dia_Tang.md | Buddhist series bible | DOMAINS/BUDDHISM/SERIES_BIBLES | BUD | canonical | compatibility-copy to SB_BUD_001 | high | low | no |
| CHARACTER_BIBLE_Dia_Tang_Bo_Tat.md | Buddhist character bible | DOMAINS/BUDDHISM/CHARACTER_BIBLES | BUD | canonical | compatibility-copy to CB_BUD_001 | high | low | no |
| kinh-dia-tang-*.txt | source files | DOMAINS/BUDDHISM/SOURCES | BUD | source | compatibility-copy | medium | low | human review: source metadata incomplete |
| request.txt | user instruction file | root | none | non-canonical | retained | low | low | no |

## Findings

- Core OS and Buddhism were mixed in the legacy root documents.
- Buddhism is the only active researched domain.
- No production binary assets were found in the initial root inventory.
- Source files have been copied into DOMAINS/BUDDHISM/SOURCES and require human review for detailed source metadata.
- Planned domains contain only skeletons and no fake Knowledge Packets.

