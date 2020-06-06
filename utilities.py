from grid import print_grid

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
