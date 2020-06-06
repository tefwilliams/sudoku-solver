import numpy as np

class Cell:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords
        self.potential_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    def is_solved(self):
        return self.value != 0
    
    def has_no_potential_values(self):
        return len(self.potential_values) == 0

    
def generate_cells(grid_values):
    grid_cells = np.ndarray(grid_values.shape, dtype='O')

    for y_coord in range(grid_values.shape[0]):
        for x_coord in range(grid_values.shape[1]):
            cell_coords = (y_coord, x_coord)
            
            cell_value = grid_values[cell_coords]
            grid_cells[cell_coords] = Cell(cell_value, cell_coords)

    return grid_cells

def get_unsolved_cell(grid):
    for cell in grid.cells.flatten():
        if not cell.is_solved():
            return cell
