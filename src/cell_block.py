from typing import Iterable
from cell import Cell


class CellBlock(list[Cell]):
    def __init__(self, value: Iterable[Cell]):
        super().__init__(list(value))

    @property
    def is_solved(self):
        return all(cell.is_solved for cell in self)

    @property
    def is_wrong(self):
        return len(set(self.__cell_values)) != len(self.__cell_values)

    @property
    def __cell_values(self):
        return [cell.value for cell in self if cell.value]

    @property
    def value(self):
        return self.__cell_values
