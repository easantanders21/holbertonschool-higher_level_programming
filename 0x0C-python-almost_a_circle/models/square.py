#!/usr/bin/python3
"""Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return information about square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter Return: width"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        super().__setattr__('width', value)
        super().__setattr__('heigth', value)

    def update(self, *args, **kwargs):
        """method that assigns attributes"""
        attr = ['id', 'size', 'x', 'y']
        if args is None or not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            for n in range(len(args)):
                setattr(self, attr[n], args[n])

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dicc = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dicc
