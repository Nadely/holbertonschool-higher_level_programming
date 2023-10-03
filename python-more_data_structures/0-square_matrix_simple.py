#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            square = num ** 2
            new_row.append(square)
        new_matrix.append(new_row)
    return new_matrix


