from typing import Dict, Any
from ....kernel.interfaces.capability_interface import Capability


class Impl(Capability):
    name = __name__.split(".")[-2]  # folder name (reasoning/memory/...)

    def supports(self, action: str) -> bool:
        return action in {"ping"}

    def run(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if action == "ping":
            return {"ok": True, "capability": self.name, "echo": payload}
        raise ValueError(f"unsupported action: {action}")
