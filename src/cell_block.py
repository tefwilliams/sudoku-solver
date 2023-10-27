from cell import Cell
from helpers import allowed_values


class CellBlock(list[Cell]):
    def __init__(self, value: list[Cell]):
        assert len(value) == 9
        super().__init__(value)

    @property
    def is_solved(self):
        return len(self.__unsolved_cells) == 0

    @property
    def is_wrong(self):
        return len(set(self.__cell_values)) != len(self.__cell_values)
    
    @property
    def __unsolved_cells(self):
        return [cell for cell in self if not cell.value]

    @property
    def __cell_values(self):
        return [cell.value for cell in self if cell.value]
    
    def try_deduce(self):
        return (
            self.check_cell_has_single_possible_value()
            or self.check_cell_has_unique_possible_value()
        )
    
    def update_possible_values(self):
        for cell in self.__unsolved_cells:
            for value in self.__cell_values:
                if value in cell.possible_values:
                    cell.possible_values.remove(value)


    def check_cell_has_single_possible_value(self):
        for cell in self.__unsolved_cells:
            if len(cell.possible_values) == 1:
                [value] = cell.possible_values

                if value not in self.__cell_values:
                    cell.value = value
                    return True

        return False
    
    def check_cell_has_unique_possible_value(self):
        '''
        Check if any value is only possible for one cell
        '''

        # TODO - Maybe some sort of 'reduce' function
        possible_value_counts = { value : 0 for value in allowed_values }

        for cell in self.__unsolved_cells:
            for value in cell.possible_values:
                if value not in self.__cell_values:
                    possible_value_counts[value] += 1

        unique_possible_values = set(
            value
            for value, count
            in possible_value_counts.items() 
            if count == 1
        )

        for cell in self.__unsolved_cells:
            for value in cell.possible_values:
                if value in unique_possible_values:
                    cell.value = value
                    return True
            
        return False
