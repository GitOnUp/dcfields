from abc import ABC, abstractmethod
from typing import Any

NOTHING = object()


class BaseConversionDescriptor(ABC):
    def __init__(self, default=NOTHING):
        self._default = default

    def __set_name__(self, _, name: str) -> None:
        self._name = "_" + name

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            if self._default is NOTHING:
                raise AttributeError()
            return self._default

        return getattr(instance, self._name, self._default)

    def __set__(self, instance: Any, value: Any) -> None:
        setattr(instance, self._name, self.on_set(value))

    @abstractmethod
    def on_set(self, value):
        raise NotImplementedError()
