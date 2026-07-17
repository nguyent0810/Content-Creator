# Migration Plan

## Current State Summary
Root-level documents combine a Buddhist content studio and operating-system conventions. Buddhism assets exist as root files with legacy names and IDs.

## Target State Summary
Core OS is generic. Buddhism is active domain BUD. Shared narrative and blueprint libraries are under SHARED_LIBRARIES. Planned domains FS, CL, TC, MUS, PSY have skeletons only.

## Phases Executed
0 baseline and backup; 1 audit; 2 plan; 3 schemas/contracts; 4 Core OS abstraction; 5 Buddhism domain copy migration; 6 planned-domain skeletons; 7 cross-domain layer; 8 compatibility mappings; 9 validation; 10 report.

## Movement Strategy
No original root files were deleted or overwritten. Existing canonical Buddhist assets were copied exactly to canonical domain paths and mapped through registries.

## Compatibility Strategy
Old paths are retained. New paths are canonical in registries. Old IDs map to new domain IDs in ID_MAPPING and ID_REGISTRY.

## Rollback Strategy
Remove generated top-level architecture folders and restore any modified file from backup. Existing root originals were not modified.

## Known Risks
Legacy root files still contain Buddhism-specific references for backward compatibility. Human review is required before removing or deprecating root files physically.
