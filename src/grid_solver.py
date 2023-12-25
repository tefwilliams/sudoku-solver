import csv
from helpers import null_value
from time import time
from grid import Grid
import numpy as np


def solve_grid(grid: Grid) -> Grid:
    start_time = time()

    while not grid.is_solved:
        if grid.is_wrong:
            raise ValueError("Failed to solve")

        if time() - start_time > 5:
            raise TimeoutError("Failed to solve in time")

        success = try_deduce(grid)

        if not success:
            return guess(grid)

    return grid


def try_deduce(grid: Grid):
    for row in range(9):
        for col in range(9):
            if grid.values[row, col] != null_value:
                continue

            grid.values[row, col] = (
                grid.get_single_possible_value(row, col) or
                grid.get_unique_possible_value(row, col)
            )

            if grid.values[row, col] != null_value:
                return True

    return False


def guess(grid: Grid) -> Grid:
    grid_copy = Grid(grid.values.copy())
    row, col = next(
        coords
        for coords, value
        in np.ndenumerate(grid_copy.values)
        if value == null_value
    )

    guess_value = grid.get_possible_values(row, col).pop()

    if (row, col) not in grid.guesses:
        grid.guesses[(row, col)] = set()

    grid.guesses[(row, col)].add(guess_value)
    grid_copy.values[row, col] = guess_value

    try:
        return solve_grid(grid_copy)

    except (ValueError, KeyError):
        if grid.is_wrong:
            raise ValueError("Grid is corrupted")

        return guess(grid)


def load_grid(path: str):
    with open(path, newline="") as file:
        grid = csv.reader(file, delimiter=",")

        return Grid(np.array([
            [
                int(col)
                if col != " "
                else null_value
                for col in row
            ]
            for row in grid
        ]))
