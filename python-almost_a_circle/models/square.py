#!/usr/bin/python3
"""Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes with arguments"""
        super().update(*args, **kwargs)
        if "size" in kwargs:
            self.width = kwargs["size"]
            self.height = kwargs["size"]

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
