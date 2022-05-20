#!/usr/bin/python3
""" Script that uses a REST API """
import requests
from sys import argv


if __name__ == "__main__":
    """ main """
    args = requests.get(argv[1]).headers.get('X-Request-Id')
    print(args)
