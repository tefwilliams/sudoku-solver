# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

import csv
import numpy as np
from copy import deepcopy
from time import time
from grid import Grid
from cell import Cell
from helpers import flatten


def solve_grid(grid: Grid) -> Grid:
    start_time = time()

    while not grid.is_solved:
        if grid.is_wrong:
            print_grid(grid)
            raise ValueError("Failed to solve")

        if time() - start_time > 5:
            raise ValueError("Failed to solve in time")

        grid = deduce(grid)

        if grid.cannot_deduce:
            grid = guess(grid)

    return grid


def deduce(grid: Grid) -> Grid:
    grid.cannot_deduce = True

    for cell in flatten(grid.cells):
        cell.was_changed = False

        if cell.is_solved:
            continue

        cell = check_potential_values(grid, cell)

        if cell.was_changed:
            grid.cannot_deduce = False

    return grid


def guess(grid: Grid) -> Grid:
    grid_copy = deepcopy(grid)
    unsolved_cell = grid_copy.next_unsolved_cell

    assert unsolved_cell is not None

    number_of_potential_values = len(unsolved_cell.__potential_values)
    random_index = np.random.randint(number_of_potential_values)

    guess_value = unsolved_cell.__potential_values[random_index]
    unsolved_cell.set_value(guess_value)

    original_cell = grid.cells[unsolved_cell.coords.col][unsolved_cell.coords.row]
    original_cell.__potential_values.remove(guess_value)

    try:
        grid_copy = solve_grid(grid_copy)

    except ValueError:
        if not grid.is_wrong:
            return guess(grid)

    return grid_copy


def check_potential_values(grid: Grid, cell: Cell) -> Cell:
    if len(cell.__potential_values) == 1:
        only_potential_value = cell.__potential_values[0]

        if grid.possible(cell.coords, only_potential_value):
            cell.value = cell.__potential_values[0]

        cell.__potential_values.remove(only_potential_value)
        cell.was_changed = True

    for potential_value in cell.__potential_values:
        if not grid.possible(cell.coords, potential_value):
            cell.__potential_values.remove(potential_value)
            cell.was_changed = True

    return cell


def load_grid(path: str):
    with open(path, newline="") as file:
        grid = csv.reader(file, delimiter=",")

        return Grid([[int(col) if col != " " else None for col in row] for row in grid])


def print_grid(grid: Grid) -> None:
    for i, row in enumerate(grid.values):
        print(
            f"{row[:3]}  {row[3:6]}  {row[6:9]}".replace(",", "")
            .replace("None", "-")
            .replace("[", "")
            .replace("]", "")
        )

        if i in [2, 5]:
            print("")
