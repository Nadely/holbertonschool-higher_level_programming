#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """def in class"""

    def area(self):
        """that raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value, assuming name is always a string"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """def in class"""

    def __init__(self, width, height):
        """width and height must be positive integers,
        validated by integer_validator"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


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
