#!/usr/bin/python3
"""
0-pascal_triangle task
"""


def pascal_triangle(n):
    """
    function that returns a list of integers
    representing the Pascal Triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        outer_number = [1]
        for j in range(len(triangle[i - 1]) - 1):
            inner_number = triangle[i - 1]
            outer_number.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        outer_number.append(1)
        triangle.append(outer_number)
    return triangle
