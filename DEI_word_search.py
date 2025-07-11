import random

def make_grid(grid_size: int):
    return [['' for _ in range(grid_size)] for _ in range(grid_size)]

print(make_grid(8))