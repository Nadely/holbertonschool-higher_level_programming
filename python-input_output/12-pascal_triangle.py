#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """You can assume n will be always an integer"""

    if n <= 0:
        return []

    pascal = [[1]]

    for x in range(1, n):
        line = [1]

        for y in range(len(pascal)):
            if y+1 < len(pascal):
                line.append(pascal[x-1][y] + pascal[x-1][y+1])

        line.append(1)
        pascal.append(line)

    return pascal
