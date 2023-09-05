# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

from time import time
from errors import SolveError
import grid_solver

initial_grid = grid_solver.load_grid('grid')
start_time = time()

try:
    solved_grid = grid_solver.solve(initial_grid)
    
except SolveError as err:
    print('\n' + err.message)
    
else:
    run_time = time() - start_time
    grid_solver.display_result(solved_grid, run_time)

print('')
    