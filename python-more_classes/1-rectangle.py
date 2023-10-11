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

    def __init__(self, height=0, width=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width

    """ width must be an integer, otherwise raise a TypeError exception with
    the message : width must be an integer
    if width is less than 0, raise a ValueError exception with the message :
    width must be >= 0 """

    @property
    def width(self):
        return self.width

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
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
