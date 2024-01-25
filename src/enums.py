import enum
from typing import TypeVar, Generic, Any, Type

from common import BaseConversionDescriptor, NOTHING

E = TypeVar("E", bound=enum.Enum)


class StrEnumField(Generic[E], BaseConversionDescriptor):
    def __init__(self, enum_type, default: Any = NOTHING):
        self.enum_type = enum_type
        super().__init__(default)

    def on_set(self, value):
        assert isinstance(value, (str, self.enum_type))


if __name__ == "__main__":
    e = enum.Enum("e", "one two")
    s = StrEnumField(e)
    s.on_set(e.one)
