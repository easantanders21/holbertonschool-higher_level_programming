#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            jc = ord(i) - 32
        else:
            jc = ord(i)
        print("{:c}".format(jc), end="")
    print("")
