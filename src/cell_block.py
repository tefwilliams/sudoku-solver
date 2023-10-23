from cell import Cell
from helpers import allowed_values


class CellBlock(list[Cell]):
    def __init__(self, value: list[Cell]):
        assert len(value) == 9
        super().__init__(value)

    @property
    def is_solved(self):
        return all(cell.is_solved for cell in self)

    @property
    def is_wrong(self):
        return len(set(self.__cell_values)) != len(self.__cell_values)

    @property
    def __cell_values(self):
        return [cell.value for cell in self if cell.value]
    
    def try_deduce(self):
        return (self.try_deduce_possible_values()
            or self.try_deduce_from_possible_values())
    
    def try_deduce_possible_values(self):
        values = self.__cell_values

        made_change = False

        for cell in self:
            for value in values:
                if value in cell.potential_values:
                    cell.potential_values.remove(value)
                    made_change = True
        
        return made_change
    
    def try_deduce_from_possible_values(self):
        made_change = False

        for cell in self:
            if len(cell.potential_values) == 1:
                [value] = cell.potential_values
                cell.value = value
                made_change = True
            
        return made_change
