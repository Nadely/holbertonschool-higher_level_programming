#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle():
    def __init__(self, height=0, width=0):
        self._Rectangle__height = height
        self._Rectangle__width = width

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
        self._Rectangle__width = value

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
            raise TypeError("height must be an intege")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
