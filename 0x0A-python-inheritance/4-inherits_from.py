#!/usr/bin/python3
"""function that return false or true if arg 1 is subclass of argument 2"""


def inherits_from(obj, a_class):
    """object is sub class of a_class?"""
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
