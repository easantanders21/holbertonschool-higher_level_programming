#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """function that prints list in order"""
        print(sorted(self))
