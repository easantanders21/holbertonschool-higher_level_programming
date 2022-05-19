#!/usr/bin/python3
""" Write a Python script that fetches """
import urllib.request

if __name__ == "__main__":
    """ main """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode("utf-8")))
