#!/usr/bin/python3
"""that writes a string to a text file"""


def write_file(filename="", text=""):
    """that writes a string to a text file"""
    with open(filename, mode="w") as f:
        return(f.write(text))
