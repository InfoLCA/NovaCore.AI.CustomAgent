from typing import Dict, Any, Protocol


class Capability(Protocol):
    def supports(self, action: str) -> bool: ...
    def run(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]: ...


class BaseAgent:
    def __init__(self, name: str, capabilities: Dict[str, Capability]):
        self.name = name
        self.capabilities = capabilities

    def handle(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        cap = self.capabilities.get(action) or next(
            (c for c in self.capabilities.values() if c.supports(action)), None
        )
        if not cap:
            return {"ok": False, "error": f"No capability for action: {action}"}
        out = cap.run(action, payload)
        out.setdefault("agent", self.name)
        return out
