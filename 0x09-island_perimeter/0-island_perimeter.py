#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """Function that returns the perimeter of the given island"""
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for i, j in zip([0] + row, row + [0]):
            perimeter += int(i != j)
    return perimeter

