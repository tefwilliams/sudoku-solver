"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwi
"""

import numpy as np
from cell import Cell
from utilities import possible

class Grid:
    def __init__(self, grid_values):
        self.shape = grid_values.shape
        self.cells = self.generate_cells(grid_values)
        self.cannot_deduce = False
    
    def get_values(self):
        grid_values = np.zeros(self.shape)
        
        for y_coord in range(self.shape[0]):
            for x_coord in range(self.shape[1]):
                cell_coords = (y_coord, x_coord)
                
                grid_values[cell_coords] = self.cells[cell_coords].value
                
        return grid_values
    
    def generate_cells(self, grid_values):
        grid_cells = np.ndarray(grid_values.shape, dtype='O')
    
        for y_coord in range(grid_values.shape[0]):
            for x_coord in range(grid_values.shape[1]):
                cell_coords = (y_coord, x_coord)
                
                cell_value = grid_values[cell_coords]
                grid_cells[cell_coords] = Cell(cell_value, cell_coords)
    
        return grid_cells

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
        
        return self.cells[square_y_start_coord : square_y_end_coord, square_x_start_coord : square_x_end_coord].flatten()