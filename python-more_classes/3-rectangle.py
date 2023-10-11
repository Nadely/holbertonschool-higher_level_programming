#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
>>> my_rectangle = Rectangle(2, 4)
{'_Rectangle__height': 2, '_Rectangle__width': 4}
>>> my_rectangle = Rectangle(3, 10)
{'_Rectangle__width': 10, '_Rectangle__height': 3}
"""


class Rectangle:
    """ Private instance attribute: width and height"""

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    """ width must be an integer, otherwise raise a TypeError exception with
    the message : width must be an integer
    if width is less than 0, raise a ValueError exception with the message :
    width must be >= 0 """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ height must be an integer, otherwise raise a TypeError exception
    with the message : height must be an integer
    if height is less than 0, raise a ValueError exception with the message :
    height must be >= 0 """

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """ that returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        else:
            for _ in range(self.__height):
                result += "#" * self.__width + "\n"
            return result[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
