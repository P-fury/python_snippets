from abc import ABC

class ImmutableClass(ABC):
    __slots__ = ('__attrs__',)


