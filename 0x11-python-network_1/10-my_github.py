#!/usr/bin/python3
""" script task 9 """
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    s = requests.Session()
    s.auth = (argv[1], argv[2])
    req = s.get(url)
    try:
        print('{}'.format(req.json()['id']))
    except:
        print("None")
