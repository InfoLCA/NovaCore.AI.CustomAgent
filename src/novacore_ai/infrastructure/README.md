# Infrastructure (Adapters)

This layer adapts NovaCore to external systems: LLM providers, storage, security, and telemetry. It **implements** kernel interfaces (providers, telemetry) but keeps business logic out.

## Structure

infrastructure/
├─ providers/   # OpenAI/Anthropic/Mistral/Google + local stubs
├─ storage/     # vector, blob, graph adapters
├─ security/    # audit logger, encryption, key mgmt
└─ telemetry/   # OpenTelemetry config, exporters

## Responsibilities
- **Providers:** wrap vendor SDKs behind uniform methods (e.g., `.call()`).
- **Storage:** abstract persistence (vector stores, blob/object storage, graphs).
- **Security:** provide auditable logs, crypto helpers, future KMS integration.
- **Telemetry:** OTel config → Loki/Tempo/Jaeger/Grafana/Prometheus.

## Patterns
- Keep adapters **stateless** where possible; inject config via env or YAML.
- Never import from `capabilities/*/lib`; only from `kernel.interfaces.*`.
- Fail fast and return structured errors (machine-parseable).

## Local Dev Notes
- Minimal stubs are provided so `pytest` and container runs succeed offline.
- Production credentials belong in a secret manager (NOT this repo).

## Non-Goals
- No vendor lock-in logic; keep APIs thin and swappable.

(Optional) Commit & push once you’ve added all four

git add src/novacore_ai/*/README.md
git commit -m "docs: add module READMEs for kernel/capabilities/agents/infrastructure"
git push origin main
