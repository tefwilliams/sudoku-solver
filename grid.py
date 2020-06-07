# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

import numpy as np
from cell import Cell
from utilities import possible


class Grid:
    def __init__(self, grid_values):
        self.shape = grid_values.shape
        self.cells = generate_cells(grid_values)

    def get_values(self):
        grid_values = np.empty(self.shape, dtype='i')

        for y_coord in range(self.shape[0]):
            for x_coord in range(self.shape[1]):
                cell_coords = (y_coord, x_coord)

                grid_values[cell_coords] = self.cells[cell_coords].value

        return grid_values

    def get_unsolved_cell(self):
        for cell in self.cells.flatten():
            if not cell.is_solved():
                return cell

    def is_solved(self):
        for cell in self.cells.flatten():
            if not cell.is_solved():
                return False

        return True

    def is_wrong(self):
        for cell in self.cells.flatten():
            if (not cell.is_solved() and cell.has_no_potential_values() or
                    cell.is_solved() and not possible(self, cell.coords, cell.value)):
                return True

        return False

    def get_row(self, cell_coords):
        y_coord = cell_coords[0]
        return self.cells[y_coord]

    def get_column(self, cell_coords):
        x_coord = cell_coords[1]
        return self.cells[:, x_coord]

    def get_square(self, cell_coords):
        y_coord, x_coord = cell_coords

        y_coord_in_square = y_coord % 3
        x_coord_in_square = x_coord % 3

        square_y_start_coord = y_coord - y_coord_in_square
        square_x_start_coord = x_coord - x_coord_in_square

        square_y_end_coord = square_y_start_coord + 3
        square_x_end_coord = square_x_start_coord + 3

        return self.cells[square_y_start_coord: square_y_end_coord, square_x_start_coord: square_x_end_coord].flatten()


def load_grid(filename):
    grid_values = np.loadtxt('%s.csv' % filename, delimiter=',', dtype='U')
    grid_values[grid_values == ' '] = '0'
    grid_values = grid_values.astype('i')
    return Grid(grid_values)


def generate_cells(grid_values):
    grid_cells = np.ndarray(grid_values.shape, dtype='O')

    for y_coord in range(grid_values.shape[0]):
        for x_coord in range(grid_values.shape[1]):
            cell_coords = (y_coord, x_coord)

            cell_value = grid_values[cell_coords]
            grid_cells[cell_coords] = Cell(cell_value, cell_coords)

    return grid_cells


def print_grid(grid, run_time):
    grid_values = grid.get_values()

    if grid.is_wrong():
        print('\n' + 'Failed to solve')
        return

    if not grid.is_solved():
        print('\n' + 'Took too long to solve')
        return

    print('\n' + 'Solved in %ims' %(run_time * 1000) + '\n')

    for y_coord in range(grid.shape[0]):
        print('%s %s %s' % (grid_values[y_coord, : 3], grid_values[y_coord, 3: 6], grid_values[y_coord, 6: 9]))

        if y_coord % 3 == 2 and y_coord != 8:
            print('')
