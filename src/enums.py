import enum
from typing import TypeVar, Generic, Any, Type

from common import BaseConversionDescriptor, NOTHING

E = TypeVar("E", bound=enum.EnumMeta)


class StrEnumField(Generic[E], BaseConversionDescriptor):
    def __init__(self, enum_type: type(E), default: Any = NOTHING):
        self.enum_type = enum_type
        super().__init__(default)

    def on_set(self, value: str | E) -> str:
        if isinstance(value, str):
            if not hasattr(self.enum_type, value):
                raise ValueError(f"{value} is not the name of a {self.enum_type}")
            return value
        if isinstance(value, self.enum_type):
            return value.name
        raise ValueError()


if __name__ == "__main__":
    e = enum.Enum("e", "one two")
    s = StrEnumField(e)
    assert s.on_set(e.one) == "one"
    assert s.on_set("one") == "one"
    # assert s.on_set("three")  "three is not the name of a <enum 'e'>
