from copy import deepcopy
from cell import get_unsolved_cell
import numpy as np
from time import time

def solve(grid):
    start_time = time()
    while not grid.is_solved() and not grid.is_wrong():
        grid = deduce(grid)
            
        if grid.cannot_deduce:
            grid = guess(grid)
            
        if time() - start_time > 5:
            break

    return grid

def deduce(grid):
    grid.cannot_deduce = True
    
    for cell in grid.cells.flatten():
        if cell.is_solved():
            continue
        
        cell.was_changed = False
        
        if len(cell.potential_values) == 1:
            only_potential_value = cell.potential_values[0]
            
            if possible(grid, cell.coords, only_potential_value):
                cell.value = cell.potential_values[0]
                
            cell.potential_values.remove(only_potential_value)
            cell.was_changed = True
        
        for potential_value in cell.potential_values:
            if not possible(grid, cell.coords, potential_value):
                cell.potential_values.remove(potential_value)
                cell.was_changed = True
                    
        if cell.was_changed:
            grid.cannot_deduce = False
            
    return grid
            
def guess(grid):
    grid_copy = deepcopy(grid)
    unsolved_cell = get_unsolved_cell(grid_copy)
    
    number_of_potential_values = len(unsolved_cell.potential_values)
    random_index = np.random.randint(number_of_potential_values)

    guess_value = unsolved_cell.potential_values[random_index]
    unsolved_cell.value = guess_value
    
    original_cell = grid.cells[unsolved_cell.coords]
    original_cell.potential_values.remove(guess_value)
    
    grid_copy = solve(grid_copy)
    
    if grid_copy.is_wrong():
        if not grid.is_wrong():
            return guess(grid)
    
        return grid
    
    return grid_copy
        
                        
def possible(grid, cell_coords, potential_value):
    row = grid.get_row(cell_coords)
    column = grid.get_column(cell_coords)
    square = grid.get_square(cell_coords)
    
    for cell in row:
        if cell.value == potential_value and cell.coords != cell_coords:
            return False
        
    for cell in column:
        if cell.value == potential_value and cell.coords != cell_coords:
            return False
        
    for cell in square:
        if cell.value == potential_value and cell.coords != cell_coords:
            return False
        
    return True
