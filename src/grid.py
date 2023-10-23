import numpy as np
from cell import Cell
from cell_block import CellBlock
from helpers import flatten


class Grid(list[Cell]):
    def __init__(self, values: list[list[int | None]]):
        assert len(values) == 9 and all(len(row) == 9 for row in values)

        cells = [[Cell(cell) for cell in row] for row in values]
        super().__init__(flatten(cells))
        grid = np.array(cells)

        self.rows = get_rows(grid)
        self.cols = get_cols(grid)
        self.squares = get_squares(grid)

    @property
    def is_solved(self):
        return all(
            cell_block.is_wrong
            for cell_block 
            in self.rows + self.cols + self.squares
        )

    @property
    def is_wrong(self):
        return any(
            cell_block.is_wrong
            for cell_block 
            in self.rows + self.cols + self.squares
        )

    @property
    def values(self):
        return [[cell.value for cell in row] for row in self.rows]
    
    def try_deduce(self):
        return any(
            cell_block.try_deduce()
            for cell_block 
            in self.rows + self.cols + self.squares
        )


def get_rows(cells: np.ndarray):
    return [CellBlock(cells[i]) for i in range(9)]


def get_cols(cells: np.ndarray):
    return [CellBlock(cells[:, i]) for i in range(9)]


def get_squares(cells: np.ndarray):
    squares: list[CellBlock] = []

    for i in range(9):
        row_min = (i // 3) * 3
        col_min = (i % 3) * 3

        squares.append(CellBlock(cells[row_min : row_min + 3, col_min : col_min + 3].flatten()))

    return squares
