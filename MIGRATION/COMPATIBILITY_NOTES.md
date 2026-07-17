# Compatibility Notes

1. Old IDs resolve via REGISTRIES/ID_REGISTRY.md and MIGRATION/ID_MAPPING.md.
2. Old paths are retained physically and mapped to canonical domain paths in MIGRATION/PATH_MAPPING.md.
3. Deprecated behavior is registry-based only; no original file was deleted.
4. Duplicate alias is prevented by canonical owner records in ASSET_REGISTRY.
5. Canonical owner is BUD for migrated Buddhist assets, CORE for shared/core abstractions.
6. Legacy root Buddhist assets remain accessible as compatibility aliases.
7. Current limitation: no runtime resolver code exists; compatibility is documented by registry and contract.
8. Future tools should load registries before resolving legacy IDs or paths.

# Cutover Verification Addendum

Timestamp: 2026-07-14T09:49:15.2278023+07:00

resolver_level: documented_mapping_only

runtime_resolution: not_implemented

Episode 004 dry run loaded canonical assets from new architecture with legacy_fallback_used: false. Runtime resolver remains future work because repository is documentation-only.

