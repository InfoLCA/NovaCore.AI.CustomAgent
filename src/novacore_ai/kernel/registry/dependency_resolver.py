from typing import Dict, List


class DependencyResolver:
    """Very light dependency resolver (placeholder)."""

    def order(self, deps: Dict[str, List[str]]) -> List[str]:
        # naive topo-like: list keys with no deps first, then the rest
        roots = [k for k, v in deps.items() if not v]
        others = [k for k, v in deps.items() if v]
        return roots + others
