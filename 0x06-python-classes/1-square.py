#!/usr/bin/python3


" A class Square that defines a sixe for a square "


class Square:
    """
    Square class

    Attributes:
        size (no type/value verification) : Private instance attribute
    """
    __size = None

    def __init__(self, size):
        self.__size = size
