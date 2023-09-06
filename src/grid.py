import numpy as np
from cell import Cell
from cell_block import CellBlock
from coords import Coords
from helpers import flatten


class Grid:
    cannot_deduce = False

    def __init__(self, values: list[list[int | None]]):
        assert len(values) == 9 and all(len(row) == 9 for row in values)

        grid = np.array([[Cell(cell) for cell in row] for row in values])
        self.cells: list[Cell] = list(grid.flatten())

        self.rows = get_rows(grid)
        self.cols = get_cols(grid)
        self.squares = get_squares(grid)

    @property
    def next_unsolved_cell(self):
        return next((cell for cell in self.cells if not cell.is_solved), None)

    @property
    def is_solved(self):
        return all(cell.is_solved for cell in self.cells)

    @property
    def is_wrong(self):
        return False
        return any(cell.is_wrong(self) for cell in flatten(self.cells))

    @property
    def values(self):
        return [[cell.value for cell in row] for row in self.cells]

    def possible(self, coords: Coords, potential_value: int) -> bool:
        row = self.__get_row(coords)
        column = self.__get_column(coords)
        square = self.__get_square(coords)

        def cell_has_potential_value(cell: Cell):
            return cell.value == potential_value and cell.coords != coords

        for cell_block in row, column, square:
            if any(cell_has_potential_value(cell) for cell in cell_block):
                return False

        return True


def get_rows(cells: np.ndarray):
    return [CellBlock(cells[i]) for i in range(9)]


def get_cols(cells: np.ndarray):
    return [CellBlock(cells[:, i]) for i in range(9)]


def get_squares(cells: np.ndarray):
    squares: list[CellBlock] = []

    for i in range(9):
        row_min = (i // 3) * 3
        col_min = (i % 3) * 3

        squares.append(CellBlock(cells[row_min : row_min + 3, col_min : col_min + 3]))

    return squares
