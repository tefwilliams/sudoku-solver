# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""

from utilities import solve
from grid import load_grid, print_grid
from time import time

grid = load_grid('grid')
start_time = time()
grid = solve(grid)
run_time = time() - start_time
print_grid(grid, run_time)