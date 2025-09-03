from ..shared.base_agent import BaseAgent
from ...capabilities.reasoning.contracts.reasoning_capability import Impl as ReasoningImpl


def build() -> BaseAgent:
    # Expose a simple 'ping' using the reasoning capability stub
    return BaseAgent("research_agent", {"ping": ReasoningImpl()})
