# Core Research Engine

## Dynamic Source Policy
The Research Engine loads source hierarchy from the active domain manifest and source registry. It validates source type, confidence, date, jurisdiction where relevant, domain attribution, and rejection rules.

## Core Duties
1. Load DOMAIN_SOURCE_POLICY.
2. Validate sources against the domain hierarchy.
3. Record confidence and source type.
4. Reject disallowed sources.
5. Escalate source conflict or missing source to human review.

Domain-specific hierarchies belong in DOMAINS/<DOMAIN>/SOURCES/SOURCE_REGISTRY.md and DOMAIN_QA policy, not in Core.
