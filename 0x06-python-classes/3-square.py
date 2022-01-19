#!/usr/bin/python3


" A class Square that defines a sixe for a square "


class Square:
    """
    Square class
    Attributes:
        size (no type/value verification) : Private instance attribute
    """
    __size = None

    def __init__(self, size=0):
        if type(size) is not int:
            raise NameError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    Public instance method that returns the square area
    """
    def area(self):
        return self.__size ** 2
