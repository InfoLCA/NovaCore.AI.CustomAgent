# NovaCore AI — Docs Index

This directory is the entry point for technical documentation. It orients new contributors and CI bots to where canonical specs live.

## Structure
- **architecture/**  
  High-level and deep-dive design docs:
  - `README.md`: map of the architecture docs
  - `clean_architecture.md`: layering, boundaries, dependencies
  - `capability_design.md`: capability contracts, lifecycle, testing
  - `microkernel_pattern.md`: kernel + plugin model and rationale

- **deployment/**  
  How to run locally and in production:
  - `local_setup.md`: dev environment, Docker/Nix, env vars
  - `cloud_deployment.md`: container build, registry, GitOps
  - `security_hardening.md`: network policies, secrets, SBOM gates

- **governance/**  
  Security and compliance guidance:
  - `security_policy.md`: org/project security rules
  - `compliance_matrix.md`: control mapping (e.g., CIS/SOC2 cues)

- **api/**  
  Auto-generated API surface (e.g., FastAPI docs build):  
  - `index.html` is a placeholder for generated output; do not edit manually.

## Authoritative References
- Runtime code: `src/novacore_ai/` (kernel, capabilities, agents, infrastructure, shared)
- CI/CD: `.github/workflows/`
- Observability: `monitoring/`
- Security artifacts: `security/` (policies, SBOMs, attestations)
- Data/Models: `data/`, `models/` (DVC-ready)

## Conventions
- All documents are Markdown unless explicitly generated (e.g., `api/index.html`).
- Treat docs as code: update docs in the same PR as the change.
- Prefer diagrams-as-code (Mermaid/PlantUML) committed alongside text.

## Keeping Docs Fresh (Checklist)
- [ ] Added/changed capability? Update `architecture/capability_design.md`.
- [ ] Touched kernel contracts? Note the change in `architecture/README.md`.
- [ ] New deployment knob? Update `deployment/local_setup.md` and `cloud_deployment.md`.
- [ ] New security control? Reflect in `governance/*` and link from `SECURITY.md`.

