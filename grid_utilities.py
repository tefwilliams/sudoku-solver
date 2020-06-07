# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwi
"""

import numpy as np
from grid import Grid

def load_grid(filename):
    grid_values = np.loadtxt('%s.csv' %filename, delimiter=',', dtype='U')
    grid_values[grid_values == ' '] = '0'
    grid_values = grid_values.astype('i')
    return Grid(grid_values)

def print_grid(grid, run_time):
    grid_values = grid.get_values()
    
    if grid.is_wrong():
        print('\n' + 'Failed to solve')
        return
    
    if not grid.is_solved():
        print('\n' + 'Took too long to solve')
        return
        
    print('\n' + 'Solved in %.2f seconds' %(run_time) + '\n')

    for y_coord in range(grid.shape[0]):
        print('%s %s %s' %(grid_values[y_coord, : 3], grid_values[y_coord, 3 : 6], grid_values[y_coord, 6 : 9]))
        
        if y_coord % 3 == 2 and y_coord != 8:
            print('')
