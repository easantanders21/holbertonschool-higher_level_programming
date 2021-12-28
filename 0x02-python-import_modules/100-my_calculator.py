#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    argv = sys.argv[1:]
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        exit(0)
    elif sys.argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        exit(0)
    elif sys.argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        exit(0)
    elif sys.argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == '__main__':
    main()
