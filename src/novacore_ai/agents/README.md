# Agents (Composition Layer)

Agents wire **capabilities** into task-oriented personas (research, coding, orchestrator, guardian). They are thin wrappers that route actions to capabilities.

## Structure

agents/
├─ shared/
│  ├─ base_agent.py      # tiny router w/ handle()
│  └─ common_adapters.py # helper adapters (optional)
├─ research_agent/
│  ├─ agent.py           # build() returns a BaseAgent w/ capabilities
│  ├─ agent_config.yaml
│  └─ tests/
├─ coding_agent/
├─ orchestrator_agent/
└─ guardian_agent/

## Responsibilities
- **Compose**: select capabilities and expose actions.
- **Route**: `BaseAgent.handle(action, payload)` → underlying capability.
- **Config**: `agent_config.yaml` describes which capabilities are active.

## Example
```python
from ..shared.base_agent import BaseAgent
from ...capabilities.reasoning.contracts.reasoning_capability import Impl as Reasoning

def build() -> BaseAgent:
    return BaseAgent("research_agent", {"ping": Reasoning()})

API Integration

The HTTP surface is in novacore_ai/api.py (FastAPI):
	•	/healthz
	•	/ping → proxies to agent

Next Additions
	•	orchestrator_agent for multi-agent flows.
	•	guardian_agent to gate high-risk actions with policies.

Non-Goals
	•	No cloud/provider specifics here (use infrastructure/).
