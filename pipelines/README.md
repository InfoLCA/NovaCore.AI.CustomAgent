# Pipelines

This module defines orchestration pipelines for training, inference, and data preparation.

## Structure

- **training_pipeline.py**  
  End-to-end model training using DVC/Prefect/Dagster.

- **inference_pipeline.py**  
  Inference orchestration and deployment flow.

- **scripts/**  
  Helper scripts for data preparation and pipeline execution.

## Purpose

- Automate **ML workflows** consistently across dev and prod.  
- Integrate with **DVC** for reproducibility and **orchestration engines** (e.g., Prefect).  
- Ensure observability and fault tolerance in pipeline execution.

## Notes

- Pipelines should be **idempotent** and re-runnable.  
- CI/CD hooks trigger training/inference pipelines as part of GitOps.
