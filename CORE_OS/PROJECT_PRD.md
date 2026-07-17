# Core OS PRD

## Purpose
This Core OS defines the domain-neutral operating layer for the AI Content Studio. It must route all subject-matter work through an explicit DOMAIN_CONTEXT and never assume Buddhism or any other domain by default.

## Core Contract
Core OS may manage workflow, asset structure, lineage, validation, registries, orchestration, production stages, and retrieval contracts. Core OS must not own domain doctrine, law, case facts, musicology, psychology claims, feng shui schools, or domain-specific evidence rules.

## Required Domain Context
Every content or knowledge operation must resolve: DOMAIN_CONTEXT, DOMAIN_MANIFEST, DOMAIN_GUIDE, DOMAIN_SOURCE_POLICY, DOMAIN_GLOSSARY, DOMAIN_QA_POLICY, and DOMAIN_ASSET_REGISTRY.

## Unresolved Domain Behavior
If no domain can be resolved, set domain_status: unresolved and action: require_domain_resolution. Do not fallback to BUD.

## Planned Domain Behavior
If a domain has status: planned, block content generation and return setup requirements. Do not invent knowledge.
