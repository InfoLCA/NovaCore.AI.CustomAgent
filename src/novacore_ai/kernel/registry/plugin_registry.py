from typing import Dict, Any


class PluginRegistry:
    """Simple in-memory registry for capabilities/providers."""

    def __init__(self) -> None:
        self._items: Dict[str, Any] = {}

    def register(self, name: str, obj: Any) -> None:
        if name in self._items:
            raise ValueError(f"Plugin already registered: {name}")
        self._items[name] = obj

    def get(self, name: str) -> Any:
        if name not in self._items:
            raise KeyError(name)
        return self._items[name]

    def all(self) -> Dict[str, Any]:
        return dict(self._items)
