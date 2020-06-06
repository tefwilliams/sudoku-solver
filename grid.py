import numpy as np
from cell import Cell

class Grid:
    def __init__(self, grid_values):
        self.shape = grid_values.shape
        self.cells = generate_cells(grid_values)
    
    def get_values(self):
        grid_values = np.zeros(self.shape)
        
        for y_coord in range(self.shape[0]):
            for x_coord in range(self.shape[1]):
                cell_coords = (y_coord, x_coord)
                
                grid_values[cell_coords] = self.cells[cell_coords].value
                
        return grid_values
    
    def get_row(self, cell_coords):
        y_coord = cell_coords[0]
        return self.cells[y_coord]
        
    def get_column(self, cell_coords):
        x_coord = cell_coords[1]
        return self.cells[:, x_coord]
    
    def get_square(self, cell_coords):
        y_coord, x_coord = cell_coords
        
        y_coord_in_square = y_coord % 3
        x_coord_in_square = x_coord % 3
        
        square_y_start_coord = y_coord - y_coord_in_square
        square_x_start_coord = x_coord - x_coord_in_square
        
        square_y_end_coord = square_y_start_coord + 3
        square_x_end_coord = square_x_start_coord + 3
        
        return self.cells[square_y_start_coord : square_y_end_coord, square_x_start_coord : square_x_end_coord].flatten()
        
        
def generate_cells(grid_values):
    grid_cells = np.ndarray(grid_values.shape, dtype='O')

    for y_coord in range(grid_values.shape[0]):
        for x_coord in range(grid_values.shape[1]):
            cell_coords = (y_coord, x_coord)
            
            cell_value = grid_values[cell_coords]
            grid_cells[cell_coords] = Cell(cell_value, cell_coords)

    return grid_cells