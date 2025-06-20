#!/usr/bin/python3
""" Pascal Triangle Function"""


def pascal_triangle(n):
    """Pascal Triangle using 2 for loops"""
    if n <= 0:
        return []

    triangle = [[1]]

    for num_row in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])

        row.append(1)
        triangle.append(row)

    return triangle
