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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs t"""
        filename = cls.__name__ + ".json"
        lista = []
        with open(cls.__name__ + ".json", mode="w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    lista.append(cls.to_dictionary(obj))
            f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return (json.loads(json_string))
