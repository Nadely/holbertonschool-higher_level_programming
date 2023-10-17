#!/usr/bin/python3
"""A class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """def in class"""

    def __init__(self, size):
        """size must be a positive integer, validated by integer_validator"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
