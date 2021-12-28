#!/usr/bin/python3
from sys import *


def main():
    length = len(argv)
    suma = 0
    for i in range(1, len(argv)):
        suma += int(argv[i])
    print("{:d}".format(suma))


if __name__ == '__main__':
    main()
