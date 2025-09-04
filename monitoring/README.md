# Monitoring

This folder contains observability tooling.

- **grafana/**: dashboards for system metrics and business KPIs  
- **prometheus/**: metrics collection and alerting rules  
- **jaeger/**: distributed tracing

## Purpose
Gives end-to-end visibility into NovaCore.AI agent activity, from infra health to request tracing.

## Next Steps
- Configure Grafana dashboards for kernel + agent metrics.
- Add Prometheus scrape configs for API and workers.
- Wire Jaeger with FastAPI/uvicorn for trace spans.

