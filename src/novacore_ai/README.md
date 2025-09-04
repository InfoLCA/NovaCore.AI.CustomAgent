# NovaCore.AI — Source Overview

This directory contains the **main source code** for `NovaCore.AI.CustomAgent`.  
It is modular, testable, and follows state-of-the-art agent architecture.

---

## Folder Tree

src/novacore_ai/
├── init.py                  # Root package marker
├── api.py                       # FastAPI entrypoint (exposes REST API)
│
├── kernel/                      # Core agent kernel
│   ├── registry/                # Dependency resolver + lifecycle management
│   ├── interfaces/              # Base interfaces (Capability, Provider, Telemetry, etc.)
│   ├── event_bus/               # Message broker + event handlers
│   └── security/                # Auth manager + policy engine stubs
│
├── capabilities/                # Pluggable agent capabilities
│   ├── reasoning/               # Reasoning capability (ping + future LLM logic)
│   ├── memory/                  # Memory capability (vector DB adapters)
│   ├── execution/               # Execution capability (task orchestration)
│   ├── communication/           # Communication capability (messaging, I/O)
│   └── audit/                   # Audit/logging capability (OPA policies, attestations)
│
├── agents/                      # Agent wrappers around capabilities
│   ├── shared/                  # BaseAgent + shared adapters
│   ├── research_agent/          # Research agent (ping implemented)
│   ├── coding_agent/            # Future: code execution agent
│   ├── orchestrator_agent/      # Future: multi-agent orchestration
│   └── guardian_agent/          # Future: guardrails, safety checks
│
└── infrastructure/              # Infra adapters (external systems)
├── providers/               # LLM providers (OpenAI, Anthropic, Mistral, Google)
├── storage/                 # Storage adapters (vector, blob, graph DBs)
├── security/                # Audit + encryption + key management
└── telemetry/               # Observability (OpenTelemetry configs)

---

## Design Notes

- **Kernel** = “OS” for agents. Controls events, security, lifecycle.  
- **Capabilities** = pluggable “skills” that agents can use.  
- **Agents** = wrappers that compose capabilities for specific tasks.  
- **Infrastructure** = provider adapters, storage, telemetry, and security.  
- **API** = single FastAPI entrypoint exposing HTTP endpoints.  

---

## Next Steps

- Each capability and agent has its own `README.md` explaining internals.  
- Tests live alongside each module in `/tests`.  
- Observability dashboards (Grafana, Prometheus, Jaeger) will hook into `telemetry/`.  

---

📌 This is the **developer onboarding map**.  
Any engineer reading this can immediately understand the folder functions, without needing tribal knowledge.

---
