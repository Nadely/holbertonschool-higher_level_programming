#!/usr/bin/python3
"""a class Student that defines a studen"""


class Student:
    """Public instance attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list)) and (all((type(x) is str)
                                              for x in attrs)):
            return {name: getattr(self, name) for name in attrs
                    if hasattr(self, name)}
        return self.__dict__

    def reload_from_json(self, json):
        for x in json:
            self.__dict__[x] = json[x]
