#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastn = (number * -1) % 10
    else:
        lastn = number % 10
    print("{:d}".format(lastn), end="")
    return(lastn)
