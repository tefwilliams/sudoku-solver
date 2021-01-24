# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

import numpy as np
from copy import deepcopy
from time import time
from errors import SolveError
from grid import print_grid

def solve(grid):
    start_time = time()
    while not grid.is_solved():
        if grid.is_wrong():
             raise SolveError("Failed to solve")
             break
            
        if time() - start_time > 5:
            raise SolveError("Failed to solve in time")
            break
            
        grid = deduce(grid)

        if grid.cannot_deduce:
            grid = guess(grid)

    return grid


def deduce(grid):
    grid.cannot_deduce = True

    for cell in grid.cells.flatten():
        cell.was_changed = False

        if cell.is_solved():
            continue

        cell = check_potential_values(grid, cell)

        if cell.was_changed:
            grid.cannot_deduce = False

    return grid


def guess(grid):
    grid_copy = deepcopy(grid)
    unsolved_cell = grid_copy.get_unsolved_cell()

    number_of_potential_values = len(unsolved_cell.potential_values)
    random_index = np.random.randint(number_of_potential_values)

    guess_value = unsolved_cell.potential_values[random_index]
    unsolved_cell.value = guess_value

    original_cell = grid.cells[unsolved_cell.coords]
    original_cell.potential_values.remove(guess_value)

    try:
        grid_copy = solve(grid_copy)

    except SolveError:
        if not grid.is_wrong():
            return guess(grid)

    return grid_copy


def check_potential_values(grid, cell):
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

    return cell


def possible(grid, cell_coords, potential_value):
    row = grid.get_row(cell_coords)
    column = grid.get_column(cell_coords)
    square = grid.get_square(cell_coords)

    for cell_block in row, column, square:
        for cell in cell_block:
            if cell.value == potential_value and cell.coords != cell_coords:
                return False

    return True

def display_result(grid, run_time):
    print('\n' + 'Solved in %ims' %(run_time * 1000) + '\n')
    print_grid(grid)