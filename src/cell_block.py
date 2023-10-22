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
        return [cell.__value for cell in self if cell.__value]
    
    def try_deduce(self):
        return (self.try_deduce_from_values()
            or self.try_deduce_from_possible_values())

    def try_deduce_from_values(self):
        values = self.__cell_values

        if len(values) == len(allowed_values) - 1:
            [missing_value] = (value for value in allowed_values if value not in values)
            [cell] = (cell for cell in self if not cell.is_solved)

            cell.value = missing_value
            return True
        
        return False
    
    def try_deduce_from_possible_values(self):
        for cell in self:
            if len(cell.__potential_values) == 1:
                [value] = cell.__potential_values
                cell.value = value
                return True
            
        return False
    

    # @property
    # def value(self):
    #     return self.__cell_values
