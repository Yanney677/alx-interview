#!/usr/bin/python3
"""
Solving Pascal Triangle
"""
def pascal_triangle(n):
    """Pascal Triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        inner_numbers = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner_numbers.append(1)
            elif i > 0 and j > 0:
                outer_numbers = triangle[i - 1][j - 1] if j - 1 >= 0 else 0
                inner_numbers.append(outer_numbers + triangle[i - 1][j])
        triangle.append(inner_numbers)
    return triangle
