#!/usr/bin/python3


" A class Square that defines a size for a square and print this"


class Square:
    """
    Square class
    Attributes:
        size (int) : Private instance attribute
        position (tuple): Private instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if ((isinstance(value, tuple)) and len(value) == 2 and
            (value[0] >= 0 and value[1] >= 0) and
            (isinstance(value[0], int)) and (isinstance(value[1], int))):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    """
    Public instance method that returns the current square area

    """
    def area(self):
        return self.size ** 2
    """
    Public instance method that print square with "#" with spaces

    """
    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")
