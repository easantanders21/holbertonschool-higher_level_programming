#!/usr/bin/python3
""" Write a Python script that fetches """
import urllib.request
from sys import argv

if __name__ == "__main__":
    """ main """
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
    print(response.getheader('X-Request-Id'))
