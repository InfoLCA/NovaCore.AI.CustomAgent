# Tests

NovaCore’s test suite follows a layered strategy for fast feedback and clear ownership.

## Layout
- **unit/** – Small, isolated tests for a single function/class (no I/O or network)
- **integration/** – Cross-module flows (e.g., agent ↔ capability)
- **e2e/** – Black-box API checks (spin up app, hit HTTP endpoints)
- **security/** – Guardrails, policy, and permission checks
- **performance/** – Simple latency/throughput smoke (non-binding)

## Conventions
- Naming: `test_*.py` with pytest.
- One behavior per test; use descriptive names.
- Prefer pure functions and dependency injection for testability.

## Running
```bash
# all tests (quiet)
pytest -q

# a folder or file
pytest src/novacore_ai/capabilities/reasoning/tests -q
pytest src/novacore_ai/agents/research_agent/tests/test_research_agent.py::test_smoke -q

Markers (optional)

Use markers to slice the suite:

import pytest

@pytest.mark.integration
def test_cross_module_flow(): ...

Then:

pytest -m "integration" -q

Fixtures
	•	Shared path/PYTHONPATH is set in repo-root conftest.py.
	•	Add module-local fixtures in tests/fixtures/ subfolders where needed.

Coverage (optional)

pip install coverage
coverage run -m pytest -q
coverage html  # see htmlcov/index.html

Adding a new test
	1.	Pick the correct layer folder.
	2.	Create test_<feature>.py.
	3.	Import the SUT (System Under Test) from src/….
	4.	Keep assertions focused; mock at boundaries only.

Goal: fast, deterministic, minimal mocks, and clear split between unit/integration/e2e.

---

### (Optional) Step 2 — Add common markers to `pytest.ini`
If you want to predeclare markers (avoids warnings):
```bash
printf '\nmarkers =\n    integration: cross-module tests\n    e2e: end-to-end API tests\n    security: policy/guardrail tests\n    performance: basic perf smoke\n' >> pytest.ini
