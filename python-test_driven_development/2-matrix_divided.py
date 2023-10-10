#!/usr/bin/python3
""" function that divides all elements of a matrix, example :
>>> matrix_divided([[1, 2, 3], [4, 5, 6]] / 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]] / 0)
division by zero """


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError
    div can’t be equal to 0, otherwise raise a ZeroDivisionError """

    Invalid = "Each row of the matrix must have the same size"
    Invalid_type = "matrix must be a matrix (list of lists) of integers/floats"
    Invalid_type_2 = "All elements of the matrix must be integers or floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(Invalid_type)
    elif any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError(Invalid)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(Invalid_type_2)
            result_item = round(item / div, 2)
            new_row.append(result_item)
        result.append(new_row)
    return result
