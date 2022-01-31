#!/usr/bin/python3
"""function that return false or true if arg 1 is ins instance of argument 2"""


def is_same_class(obj, a_class):
    """object is exactly an instance of a_class?"""
    return type(obj) is a_class
