from abc import ABC
from dataclasses import dataclass


class ImmutableClass(ABC):
    #__slots__ OKRESLA DOPUSZCZALNE ATRYBUTY '__attrs__' - nazwa przestrzeni
    __slots__ = ('__attrs__',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__attrs__ = frozenset()

    # INICJALIZACJA LINI WYZEJ W CELU NADPISANIA
    def __setattr__(self, name, value):
        if name == '__attrs__':
            super().__setattr__(name, value)
            return

        if name in self.__attrs__:
            raise AttributeError(f'{name} is immutable')
        else:
            super().__setattr__(name, value)
            self.__attrs__ |= {name}

    def __delattr__(self, name):
        if name in self.__attrs__:
            raise AttributeError(f'{name} is immutable')
        else:
            raise AttributeError(name)



# EXAMPLE:
class PointOne(ImmutableClass):
    pass

p = PointOne()
p.x = 1
p.y = 2

# del p.y
# p.x = 3


#DATA CLASS dekorator blokujacy mutowanie klas
@dataclass(frozen=True)
class PointTwo:
    x: int
    y: int
    name: str

    def __post_init__(self):
        if self.name.strip() == '':
            raise ValueError(f'Name is empty')


# EXAMPLE:
p2 = PointTwo(x=1, y=2, name='a')
print(p2)
# p2.x = 42


