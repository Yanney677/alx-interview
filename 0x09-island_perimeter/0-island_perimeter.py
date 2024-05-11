#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, j2 in zip([0] + row, row + [0]):
            perimeter += int(i1 != j2)
    return perimeter

