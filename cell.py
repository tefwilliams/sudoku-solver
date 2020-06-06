import numpy as np

class Cell:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords
        
    def is_solved(self):
        return self.value != 0
    
def generate_cells(grid_values):
    grid_cells = np.ndarray(grid_values.shape, dtype='O')

    for y_coord in range(grid_values.shape[0]):
        for x_coord in range(grid_values.shape[1]):
            cell_coords = (y_coord, x_coord)
            
            cell_value = grid_values[cell_coords]
            grid_cells[cell_coords] = Cell(cell_value, cell_coords)

    return grid_cells
