#!/usr/bin/python3
"""
Function that generates Pascal's triangle of size n.
Returns a list of lists of integers representing the triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
