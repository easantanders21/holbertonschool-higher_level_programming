#!/usr/bin/python3
""" script task 8 """
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        values = {'q': argv[1]}
    else:
        values = {'q': ""}
    res = requests.post(url, values)
    try:
        if (len(res.json()) > 0):
            print('[{}] {}'.format(res.json()['id'], res.json()['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
