#!/usr/bin/python3
""" Script that uses a REST API """
import requests
from sys import argv


if __name__ == "__main__":
    """ main """
    args = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(args.text)))
    print("\t- content: {}".format(args.text))
