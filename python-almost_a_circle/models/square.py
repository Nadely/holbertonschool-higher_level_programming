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
        if args:
            if len(args) > 0:
                super().update(*args[:4])
                self.size = args[0]
        else:
            super().update(**kwargs)
            if "size" in kwargs:
                self.size = kwargs["size"]
