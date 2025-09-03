from typing import Any, Iterable


class LifecycleManager:
    """Start/stop lifecycle for plugins (no-op stubs for now)."""

    def start_all(self, plugins: Iterable[Any]) -> None:
        for _p in plugins:
            pass

    def stop_all(self, plugins: Iterable[Any]) -> None:
        for _p in plugins:
            pass
