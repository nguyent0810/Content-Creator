# Domain Manifest Schema

Required YAML fields: schema_version, domain_id, domain_name, status, domain_guide, default_language, source_registry, glossary, qa_policy, knowledge_packet_prefix, creative_packet_prefix, character_bible_prefix, series_bible_prefix, risk_level.

Allowed status: active, planned, deprecated, blocked.

Planned domains must use TODO_RESEARCH_REQUIRED or HUMAN_REVIEW_REQUIRED for unknown data and must not include fake knowledge assets.
