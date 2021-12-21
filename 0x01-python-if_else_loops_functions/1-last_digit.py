#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str2 = "and is less than 6 and not 0"

if number < 0:
    number2 = (number * - 1) % 10
    number2 = number2 * -1
else:
    number2 = number % 10
if number2 < 6 and number2 != 0:
    print("{} {:d} is {:d} {}".format(str, number, number2, str2))
elif number2 > 5 and number2 != 0:
    print("{} {:d} is {:d} and is greater than 5".format(str, number, number2))
elif number2 == 0:
    print("{} {:d} is {:d} and is 0".format(str, number, number2))
