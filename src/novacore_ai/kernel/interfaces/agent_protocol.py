from typing import Protocol, Any, Dict


class AgentProtocol(Protocol):
    """Contract for agent-to-agent or app-to-agent calls."""

    def handle(self, message: Dict[str, Any]) -> Dict[str, Any]: ...
