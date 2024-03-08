#!/usr/bin/python3
"""
0-pascal_triangle task
"""


def pascal_triangle(n):
    """
    function that returns a list of integers
    representing the Pascal Triangle of n
    """
    t = []
    if n <= 0:
        return t
    t = [[1]]
    for i in range(1, n):
        tri = [1]
        for j in range(len(t[i - 1]) - 1):
            curs = t[i - 1]
            tri.append(t[i - 1][j] + t[i - 1][j + 1])
        tri.append(1)
        t.append(tri)
    return t
