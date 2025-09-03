from typing import Protocol, Any, Dict


class Provider(Protocol):
    """External provider adapter."""

    def invoke(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]: ...
