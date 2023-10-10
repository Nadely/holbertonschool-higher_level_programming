#!/usr/bin/python3
""" function that prints a square with the character #
>>> print_square(1)
#
>>> print_square(-3)
size must be >= 0 """


def print_square(size):
    """ if size is less than 0, raise a ValueError exception with the message :
    size must be >= 0
    if size is a float and is less than 0, raise a TypeError exception
    with the message : size must be an integer """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            print("#" * size)
