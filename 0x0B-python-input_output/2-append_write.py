#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""
    with open(filename, mode="a") as f:
        return(f.write(text))
