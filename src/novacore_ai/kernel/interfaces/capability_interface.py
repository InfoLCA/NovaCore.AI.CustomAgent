from typing import Protocol, Any, Dict


class Capability(Protocol):
    """Pluggable capability contract."""

    name: str

    def supports(self, action: str) -> bool: ...
    def run(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]: ...
