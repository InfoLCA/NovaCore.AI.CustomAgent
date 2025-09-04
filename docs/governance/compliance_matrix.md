# Compliance Matrix (Starter)

| Control           | Where Implemented                      |
|-------------------|----------------------------------------|
| SBOM & Signing    | `scripts/sbom-sign.sh`, CI workflow    |
| Policy Enforcement| `security/policies/*.rego`             |
| Audit Logging     | `infrastructure/security/audit_logger` |
| Observability     | `monitoring/*`                         |
