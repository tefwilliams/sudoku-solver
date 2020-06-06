import numpy as np
from grid import Grid

def get_grid(filename):
    grid_values = np.loadtxt('%s.csv' %filename, delimiter=',', dtype='U')
    grid_values[grid_values == ' '] = '0'
    grid_values = grid_values.astype('i')
    return Grid(grid_values)

def solve(grid):
    for y_coord in range(grid.shape[0]):
        for x_coord in range(grid.shape[1]):
            cell_coords = (y_coord, x_coord)
            
            if not grid.cells[cell_coords].is_solved():
                for potential_value in range(1, 10):
                    if possible(grid, cell_coords, potential_value):
                        grid.cells[cell_coords].value = potential_value
                        solve(grid)
                        
                        grid.cells[cell_coords].value = 0
                        
                return
    
    print_grid(grid)
    input('Press Enter to find more solutions')
                        
def possible(grid, cell_coords, potential_value):
    row = grid.get_row(cell_coords)
    column = grid.get_column(cell_coords)
    square = grid.get_square(cell_coords)
    
    for cell in row:
        if cell.value == potential_value:
            return False
        
    for cell in column:
        if cell.value == potential_value:
            return False
        
    for cell in square:
        if cell.value == potential_value:
            return False
        
    return True

def print_grid(grid):
    grid_values = grid.get_values()
    
    print('')
    for y_coord in range(grid.shape[0]):
        print('%s %s %s' %(grid_values[y_coord, : 3], grid_values[y_coord, 3 : 6], grid_values[y_coord, 6 : 9]))
        
        if y_coord % 3 == 2 and y_coord != 8:
            print('')
