#!/usr/bin/python3
"""class Square that defines a square
this class is empty
"""


class Square():
    """Private instance attribute: size"""

    def __init__(self, _Square__size=0, position=(0, 0)):
        """Instantiation with size and position"""
        self._Square__size = _Square__size
        self.position = position

    """Public instance method"""

    def area(self):
        """Compute the area of the square"""
        return self._Square__size ** 2

    """property getter"""

    @property
    def size(self):
        """return getter"""
        return self._Square__size

    """property setter"""

    @size.setter
    def size(self, value):
        """Instantiation with optional size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
        """Change name"""
        self._Square__size = value

        """Printing a square"""

    def my_print(self):
        """print function"""
        if self._Square__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self._Square__size):
                print(" " * self.position[0] + "#" * self._Square__size)

        """property getter"""

    @property
    def position(self):
        """return getter"""
        return self.__position

    """property setter"""

    @position.setter
    def position(self, value):
        """Instantiation with optional position"""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")
