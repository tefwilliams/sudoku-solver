# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

import numpy as np
from copy import deepcopy
from time import time
from errors import SolveError
from grid import Grid
from cell import Cell


def solve(grid: Grid) -> Grid:
    start_time = time()

    while not grid.is_solved():
        if grid.is_wrong():
            raise SolveError("Failed to solve")

        if time() - start_time > 5:
            raise SolveError("Failed to solve in time")

        grid = deduce(grid)

        if grid.cannot_deduce:
            grid = guess(grid)

    return grid


def deduce(grid: Grid) -> Grid:
    grid.cannot_deduce = True

    for cell in grid.cells.flatten():
        cell.was_changed = False

        if cell.is_solved():
            continue

        cell = check_potential_values(grid, cell)

        if cell.was_changed:
            grid.cannot_deduce = False

    return grid


def guess(grid: Grid) -> Grid:
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


def check_potential_values(grid: Grid, cell: Cell) -> Cell:
    if len(cell.potential_values) == 1:
        only_potential_value = cell.potential_values[0]

        if grid.possible(cell.coords, only_potential_value):
            cell.value = cell.potential_values[0]

        cell.potential_values.remove(only_potential_value)
        cell.was_changed = True

    for potential_value in cell.potential_values:
        if not grid.possible(cell.coords, potential_value):
            cell.potential_values.remove(potential_value)
            cell.was_changed = True

    return cell


def display_result(grid: Grid, run_time: float) -> None:
    print("\n" + "Solved in %ims" % (run_time * 1000) + "\n")
    print_grid(grid)


def load_grid(filename: str) -> Grid:
    grid_values = np.loadtxt(f"./data/{filename}.csv", delimiter=",", dtype="U")
    grid_values[grid_values == " "] = "0"
    grid_values = grid_values.astype("i")
    return Grid(grid_values)


def print_grid(grid: Grid) -> None:
    grid_values = grid.get_values()

    for y_coord in range(grid.shape[0]):
        print(
            "%s  %s  %s"
            % (
                grid_values[y_coord, :3],
                grid_values[y_coord, 3:6],
                grid_values[y_coord, 6:9],
            )
        )

        if y_coord % 3 == 2 and y_coord != 8:
            print("")
