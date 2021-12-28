#!/usr/bin/python3
from sys import *


def main():
    if len(argv) <= 1:
        print("0 arguments.")
        return()
    print("{} argument:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == '__main__':
    main()
