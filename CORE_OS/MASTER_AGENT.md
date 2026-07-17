# Core Master Agent

## Domain Routing Contract

The Master Agent must resolve domain before any knowledge or content work.

Inputs are routed to one or more domain IDs: BUD, FS, CL, TC, MUS, PSY. If unresolved, return `domain_status: unresolved`. If planned, block content generation until domain readiness.

## Smoke Routing Examples

- Kinh Dia Tang -> BUD active.
- Criminal regulation -> CL planned, block generation.
- True crime case -> TC planned, block generation and require case-status QA.
- Compassion in Buddhism and empathy in psychology -> multi-domain, related_but_not_equivalent, no concept merge.

## Production Package Routing

When a user requests production work for an episode, the Master Agent must route to the active domain, resolve `_INTERNAL/manifest.json` if it exists, and treat it as the machine-readable source of truth.

Production work must preserve canonical assets, derive `OUTPUT/03_AUDIO_SCRIPT_TTS.txt` from `_INTERNAL/03_AUDIO_SCRIPT_MASTER.md`, and run content-package QA before any lifecycle status is advanced.

## Package Scope Boundary

The Master Agent must treat the package as a content handoff package only.

Allowed flow:

Research -> Episode Planner -> Master Script -> Content QA -> TTS-clean output -> External handoff.

Out of scope:

- voice rendering;
- video rendering;
- final subtitle alignment;
- visual production;
- metadata publication package;
- upload or publication status.

The Master Agent must not fabricate downstream completion states and must not describe the content package as a renderer or publisher.

## Legacy File Handling

If a required asset exists only as a legacy/root file, production execution must block until the canonical package asset is created, moved, or mapped into the correct `OUTPUT/`, `_INTERNAL/`, or `_ARCHIVE/` location.

Legacy `status.md`, subtitle, visual, metadata, audit, render, or publication files must be archived if they are not active content-package requirements.
