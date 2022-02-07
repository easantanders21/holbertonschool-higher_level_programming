#!/usr/bin/python3
"""Class base"""


import json


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            lista = []
        filename = cls.__name__ + ".json"
        lista = []
        with open(filename, mode="w") as f:
            for obj in list_objs:
                lista.append(cls.to_dictionary(obj))
            f.write(cls.to_json_string(lista))
