import csv
import numpy as np
from copy import deepcopy
from time import time
from grid import Grid


def solve_grid(grid: Grid) -> Grid:
    start_time = time()

    while not grid.is_solved:
        if grid.is_wrong:
            print_grid(grid)
            raise ValueError("Failed to solve")

        if time() - start_time > 5:
            raise ValueError("Failed to solve in time")

        success = grid.try_deduce()

        if not success:
            pass

    return grid


def guess(grid: Grid) -> Grid:
    grid_copy = deepcopy(grid)
    unsolved_cell, index = next(
        (cell, i) 
        for i, cell 
        in enumerate(grid_copy)
        if not cell.value
    )

    number_of_potential_values = len(unsolved_cell.__potential_values)
    random_index = np.random.randint(number_of_potential_values)

    guess_value = unsolved_cell.__potential_values[random_index]
    unsolved_cell.value = guess_value

    original_cell = grid[index]
    original_cell.__potential_values.remove(guess_value)

    try:
        grid_copy = solve_grid(grid_copy)

    except ValueError:
        if not grid.is_wrong:
            return guess(grid)

    return grid_copy


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
