# Core Content Architecture

Content architecture is layered: Core OS -> Shared Libraries -> Domain Specification -> Domain Assets -> Cross-domain Relations -> Registries -> Migration/Compatibility.

Core architecture defines asset types and dependency resolution. It does not define subject-specific truth. Each asset must declare domain, owner, status, dependencies, lineage, QA policy, and compatibility aliases when applicable.
