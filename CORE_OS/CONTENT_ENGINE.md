# Core Content Engine

The Content Engine composes domain-aware production flows. It must load domain context before selecting knowledge packets, character bibles, series bibles, narrative patterns, episode blueprints, or QA policies.

Content generation is blocked when domain_status is unresolved or planned. Core may provide setup instructions but must not fabricate domain knowledge.
