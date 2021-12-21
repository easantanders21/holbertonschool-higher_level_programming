#!/usr/bin/python3
for i in range(97, 123):
    if i == 101:
        number = 1
    elif i == 113:
        number = 2
    else:
        print("{:c}".format(i), end="")
