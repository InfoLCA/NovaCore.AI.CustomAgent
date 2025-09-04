# Capabilities (Pluggable Skills)

Capabilities are isolated, composable “skills” that implement kernel interfaces. Agents compose these capabilities to form behaviors.

## Structure

capabilities/
├─ reasoning/
├─ memory/
├─ execution/
├─ communication/
└─ audit/
(each)
├─ lib/          # pure domain logic
├─ contracts/    # concrete impls of kernel.interfaces.Capability
├─ config/       # YAML schemas/defaults
└─ tests/        # co-located unit tests (+ fixtures/)

## Rules
- **Isolation:** no cross-capability imports from `lib/`. Share via `shared/` utils if needed.
- **Contracts implement Interfaces:** concrete class implements `Capability` with:
  - `name: str`
  - `supports(action: str) -> bool`
  - `run(action: str, payload: dict) -> dict`
- **Config-first:** place defaults and schema hints under `config/`.
- **Test-next-to-code:** smoke tests validate importability and `ping`.

## How to Add a New Capability
1. `mkdir -p capabilities/<name>/{lib,contracts,config,tests/fixtures}`
2. Implement `contracts/<name>_capability.py` (implements `Capability`).
3. Add `config/<name>_config.yaml`.
4. Add `tests/test_<name>.py` (copy one of the existing smoke tests).

## Example Contract (simplified)
```python
from novacore_ai.kernel.interfaces.capability_interface import Capability
from typing import Dict, Any

class Impl(Capability):
    name = "mycap"
    def supports(self, action: str) -> bool:
        return action in {"ping"}

    def run(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if action == "ping":
            return {"ok": True, "capability": self.name, "echo": payload}
        raise ValueError(f"unsupported action: {action}")

Testing

Run all capability tests:

Non-Goals
	•	No direct cloud/provider calls here — use infrastructure/ adapters.
