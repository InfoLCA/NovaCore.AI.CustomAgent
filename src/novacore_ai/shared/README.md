# Shared Module

This package centralizes cross-cutting concerns and common utilities used throughout **NovaCore AI**.

## Structure

- **constants/**  
  Fixed values, error codes, and system-wide limits.

- **exceptions/**  
  Custom exception types for agent and capability error handling.

- **schemas/**  
  Pydantic-style data models for agents, messages, and configuration contracts.

- **utils/**  
  Helper utilities (config loading, serialization, validation).

## Purpose

- Provide **reusable primitives** across kernel, capabilities, and agents.
- Reduce code duplication and enforce consistent standards.
- Act as the **foundation layer** of the system, imported by nearly every component.

## Notes

- Avoid introducing business logic here.  
- Keep this strictly as a **support library** for higher-level modules.
