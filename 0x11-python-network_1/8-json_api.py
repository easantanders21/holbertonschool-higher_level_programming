#!/usr/bin/python3
""" script task 8 """
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ""}
    if len(argv) == 2:
        values['q'] = argv[1]
        res = requests.post(url, data=values)
    else:
        res = requests.post(url, data=values)
    try:
        user = response.json()
        if len(user) < 1:
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except ValueError:
        print("Not a valid JSON")
