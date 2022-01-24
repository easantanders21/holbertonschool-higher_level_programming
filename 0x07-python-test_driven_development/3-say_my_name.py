#!/usr/bin/python3
""" Write a function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ A function that print first name and last name """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if len(first_name) == 0:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
