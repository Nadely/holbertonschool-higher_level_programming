#!/usr/bin/python3
"""the first class Base"""


import json


class Base:
    """Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            if not isinstance(id, int):
                raise TypeError("id must be an integer")
            if id < 0:
                raise ValueError("id must be a non-negative integer")
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dict)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            if len(dictionary) > 0:
                if cls.__name__ == "Rectangle":
                    instance = cls(1, 1)
                if cls.__name__ == "Square":
                    instance = cls(1)
                instance.update(**dictionary)
                return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
