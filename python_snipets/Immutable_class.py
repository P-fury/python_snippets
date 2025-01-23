from abc import ABC


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
class Pointer(ImmutableClass):
    pass

p = Pointer()
p.x = 1
p.y = 2

# del p.y
p.x = 3