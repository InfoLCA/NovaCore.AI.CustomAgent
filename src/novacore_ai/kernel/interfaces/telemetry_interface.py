from typing import Protocol, Mapping, Any


class Telemetry(Protocol):
    """Minimal telemetry contract; wire to OTel later."""

    def event(self, name: str, attrs: Mapping[str, Any] | None = None) -> None: ...
    def metric(self, name: str, value: float, attrs: Mapping[str, Any] | None = None) -> None: ...
