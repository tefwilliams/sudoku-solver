import csv
from time import time
from grid import Grid


def solve_grid(grid: Grid) -> Grid:
    start_time = time()

    while not grid.is_solved:
        if grid.is_wrong:
            raise ValueError("Failed to solve")

        if time() - start_time > 5:
            raise TimeoutError("Failed to solve in time")

        success = grid.try_deduce()

        if not success:
            return guess(grid)

    return grid


def guess(grid: Grid) -> Grid:
    grid_copy = Grid(grid.values)
    unsolved_cell, index = next(
        (cell, i) 
        for i, cell 
        in enumerate(grid_copy)
        if not cell.value
    )

    original_cell = grid[index]
    guess_value = original_cell.possible_values.pop()
    unsolved_cell.value = guess_value

    try:
        return solve_grid(grid_copy)

    except (ValueError, KeyError):
        if grid.is_wrong:
            raise ValueError("Grid is corrupted")
        
        return guess(grid)



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
