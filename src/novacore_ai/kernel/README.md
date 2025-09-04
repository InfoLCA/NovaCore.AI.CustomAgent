# Kernel (Microkernel Core)

The kernel is the minimal “OS layer” of NovaCore. It hosts interfaces, lifecycle, eventing, and security so **capabilities** and **agents** stay clean and decoupled.

## Structure

kernel/
├─ registry/            # discovery, lifecycle, dependency graph
│  ├─ plugin_registry.py
│  ├─ lifecycle_manager.py
│  └─ dependency_resolver.py
├─ interfaces/          # contracts (ports) implemented elsewhere
│  ├─ capability_interface.py
│  ├─ provider_interface.py
│  ├─ telemetry_interface.py
│  └─ agent_protocol.py
├─ event_bus/           # async message/event primitives
│  ├─ message_broker.py
│  └─ event_handlers.py
└─ security/            # zero-trust stubs (OPA later)
├─ auth_manager.py
└─ policy_engine.py

## Responsibilities
- **Interfaces:** canonical contracts used by capabilities, agents, infra.
- **Lifecycle:** register/activate capabilities; wire dependencies.
- **Event Bus:** publish/subscribe, fan-out, backpressure (extensible).
- **Security:** central gatekeeper; later enforce OPA/Regula/ABAC.

## Extension Points
- Add a new interface under `interfaces/`.
- Register a new plugin via `registry/plugin_registry.py`.
- Add event handlers in `event_bus/event_handlers.py`.
- Enforce policies via `security/policy_engine.py`.

## Testing
- Unit tests live adjacent to modules (see capability tests for patterns).
- Kernel smoke test: import and create `MessageBroker()` and `PluginRegistry()`.

## Non-Goals
- No provider-specific logic.
- No direct network or storage calls.
