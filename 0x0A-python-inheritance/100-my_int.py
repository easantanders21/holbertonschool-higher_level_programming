#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class MyInt"""
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return(False)

    def __ne__(self, other):
        return(True)
