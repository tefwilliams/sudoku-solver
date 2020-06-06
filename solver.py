from grid import generate_grid, print_grid
from time import time
from utilities import  solve

grid = generate_grid('grid')
start_time = time()
grid = solve(grid)
run_time = time() - start_time
print_grid(grid, run_time)