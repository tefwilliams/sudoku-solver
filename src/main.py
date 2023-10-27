from time import time
from grid_solver import load_grid, solve_grid

initial_grid = load_grid("./data/grid.csv")

try:
    start_time = time()
    solved_grid = solve_grid(initial_grid)
    end_time = time()

except ValueError as err:
    print(f"""
{err}

{initial_grid}
""")

else:
    run_time_ms = (end_time - start_time) * 1000
    print(f"""
Solved in {run_time_ms:.3g}ms

{solved_grid}
""")
