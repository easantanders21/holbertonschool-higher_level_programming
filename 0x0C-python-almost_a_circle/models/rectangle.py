#!/usr/bin/python3
"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter Returns: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter Returns: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter Returns: x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter Returns: y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area method"""
        return self.height * self.__width

    def display(self):
        """Display method"""
        for mov_y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """return information about rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args is None or not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            for n in range(len(args)):
                setattr(self, attr[n], args[n])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dicc = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return dicc
