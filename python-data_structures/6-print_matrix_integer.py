#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_row = len(matrix)
    for row in matrix:
        for idx, num in enumerate(row):
            print("{:d}".format(num), end='')
            if idx < len(row) - 1:
                print(' ', end='')
        if len_row > 1:
            print()
    if not matrix:
        print()
