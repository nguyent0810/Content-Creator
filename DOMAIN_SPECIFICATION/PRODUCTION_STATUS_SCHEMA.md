# Production Status Schema

## Deprecation Notice

`status.md` is deprecated for content production packages.

Current packages must use:

- `_INTERNAL/manifest.json` as the machine-readable source of truth;
- `README.md` as the human-readable root entry point;
- `_INTERNAL/REVIEW_SUMMARY.md` as the human-readable review summary.

Legacy `status.md` files must be moved to `_ARCHIVE/` and must not control package lifecycle decisions.

## Allowed Content Status Values

The active content-package status values are:

- `DRAFTING`
- `READY_FOR_CONTENT_REVIEW`
- `CONTENT_REVISION_REQUIRED`
- `CONTENT_APPROVED`
- `READY_FOR_TTS_HANDOFF`
- `CONTENT_PACKAGE_COMPLETE`
- `BLOCKED`

Renderer and publication states are outside content-package scope.
