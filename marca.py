from enum import Enum

class Marca(Enum):
    VEJA = 1
    YPE = 2
    OMO = 3

    def __str__(self):
        return self.name 