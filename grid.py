# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

import numpy as np
from nptyping import NDArray
from cell import Cell
from typing import Optional


class Grid:
    cannot_deduce = False

    def __init__(self, grid_values: NDArray):
        self.shape = grid_values.shape
        self.cells = generate_cells(grid_values)

    def get_values(self) -> NDArray:
        grid_values = np.empty(self.shape, dtype='i')

        for y_coord in range(self.shape[0]):
            for x_coord in range(self.shape[1]):
                cell_coords = (y_coord, x_coord)

                grid_values[cell_coords] = self.cells[cell_coords].value

        return grid_values

    def get_unsolved_cell(self) -> Optional[Cell]:
        for cell in self.cells.flatten():
            if not cell.is_solved():
                return cell

    def is_solved(self) -> bool:
        for cell in self.cells.flatten():
            if not cell.is_solved():
                return False

        return True

    def is_wrong(self) -> bool:
        for cell in self.cells.flatten():
            if cell.is_wrong(self):
                return True

        return False

    def get_row(self, cell_coords: tuple[int, int]) -> NDArray:
        y_coord = cell_coords[0]
        return self.cells[y_coord]

    def get_column(self, cell_coords: tuple[int, int]) -> NDArray:
        x_coord = cell_coords[1]
        return self.cells[:, x_coord]

    def get_square(self, cell_coords: tuple[int, int]) -> NDArray:
        y_coord, x_coord = cell_coords

        y_coord_in_square = y_coord % 3
        x_coord_in_square = x_coord % 3

        square_y_start_coord = y_coord - y_coord_in_square
        square_x_start_coord = x_coord - x_coord_in_square

        square_y_end_coord = square_y_start_coord + 3
        square_x_end_coord = square_x_start_coord + 3

        return self.cells[square_y_start_coord: square_y_end_coord, square_x_start_coord: square_x_end_coord].flatten()
    
    def possible(self, cell_coords: tuple[int, int], potential_value: int) -> bool:
        row = self.get_row(cell_coords)
        column = self.get_column(cell_coords)
        square = self.get_square(cell_coords)
    
        for cell_block in row, column, square:
            for cell in cell_block:
                if cell.value == potential_value and cell.coords != cell_coords:
                    return False
    
        return True


def generate_cells(grid_values: NDArray) -> NDArray:
    grid_cells = np.ndarray(grid_values.shape, dtype='O')

    for y_coord in range(grid_values.shape[0]):
        for x_coord in range(grid_values.shape[1]):
            cell_coords = (y_coord, x_coord)

            cell_value = grid_values[cell_coords]
            grid_cells[cell_coords] = Cell(cell_value, cell_coords)

    return grid_cells
