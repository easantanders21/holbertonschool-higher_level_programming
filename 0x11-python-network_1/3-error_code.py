#!/usr/bin/python3
""" Write a Python script that fetches """
import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
        html = html.decode('utf-8')
        print(html)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))
