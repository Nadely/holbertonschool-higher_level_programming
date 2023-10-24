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
            """that assigns an argument to each attribute"""
            if args:
                arg = 0
                attributs = ["id", "width", "height", "x", "y"]
                for i in args:
                    setattr(self, attributs[arg], i)
                    arg += 1
                return
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
