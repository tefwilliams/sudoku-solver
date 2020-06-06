import numpy as np
from cell import generate_cells

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
    
def generate_grid(filename):
    grid_values = np.loadtxt('%s.csv' %filename, delimiter=',', dtype='U')
    grid_values[grid_values == ' '] = '0'
    grid_values = grid_values.astype('i')
    return Grid(grid_values)

def print_grid(grid):
    grid_values = grid.get_values()
    
    print('')
    for y_coord in range(grid.shape[0]):
        print('%s %s %s' %(grid_values[y_coord, : 3], grid_values[y_coord, 3 : 6], grid_values[y_coord, 6 : 9]))
        
        if y_coord % 3 == 2 and y_coord != 8:
            print('')