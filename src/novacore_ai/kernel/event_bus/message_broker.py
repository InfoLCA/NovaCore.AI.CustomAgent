from dataclasses import dataclass
from typing import Callable, Dict, List, Any


@dataclass(frozen=True)
class Event:
    name: str
    data: Dict[str, Any]


class MessageBroker:
    def __init__(self) -> None:
        self._subs: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[Event], None]) -> None:
        self._subs.setdefault(topic, []).append(handler)

    def publish(self, topic: str, event: Event) -> None:
        for h in self._subs.get(topic, []):
            h(event)
