# Changelog

## [v0.1.0] - 2025-09-03
Initial bootstrap release of **NovaCore.AI.CustomAgent**

### ✨ Features
- **Kernel scaffolding**
  - Implemented core registry, lifecycle manager, plugin registry.
  - Event bus (broker + handlers) and basic security modules (auth manager, policy engine).
- **Capabilities**
  - Added modular capability stubs: reasoning, memory, execution, audit, communication.
  - Each capability exposes a standard `ping` contract with smoke tests.
- **Agents**
  - Introduced `research_agent` wired to reasoning capability.
  - Stubbed additional agents (`coding_agent`, `orchestrator_agent`, `guardian_agent`) with configs.
  - Shared base agent abstraction for consistent capability routing.
- **Infrastructure**
  - Providers: OpenAI, Anthropic, Google, Mistral, Local.
  - Storage: vector DB, blob, graph adapters.
  - Security: audit logger, encryption, key management.
  - Telemetry: OTEL config (logging receiver/exporter).
- **API Service**
  - Minimal FastAPI app with `/healthz` and `/ping` endpoints.
  - Dockerized with `uvicorn` entrypoint and dev image (`novacore-ai:dev`).

### 🧪 Testing & Quality
- Smoke tests for kernel, capabilities, and agent endpoints.
- Root-level `conftest.py` for import safety.
- **pre-commit** hooks (Black + Ruff).

### 🔐 Security & Compliance
- OPA policy stubs (`agent_admission.rego`, `capability_policies.rego`).
- CI `security-build.yml` generating SBOMs (Syft/Trivy) and signing with Cosign.

### 🚀 CI/CD & Release
- GitHub Actions:
  - `tests.yml` (pytest)
  - `security-build.yml` (SBOM + sign)
  - `deploy.yml` (Docker build & push → GHCR)
- Versioned release tagged as `v0.1.0`.

### 📦 Data/ML Tooling
- **DVC** initialized for dataset versioning.
- **MLflow** local tracking (`mlruns/`).

---

## Next Steps
- Expand agents beyond `ping` (reasoning pipelines).
- Wire telemetry to Prometheus/Grafana.
- Harden policies (deny-by-default).
- Extend CI/CD with integration tests & model jobs.

[Release tag v0.1.0](https://github.com/InfoLCA/NovaCore.AI.CustomAgent/releases/tag/v0.1.0)
