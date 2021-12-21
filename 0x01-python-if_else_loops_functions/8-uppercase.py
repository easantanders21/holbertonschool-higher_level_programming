#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            j = ord(i) - 32
        else:
            j = ord(i)
        print("{}".format(chr(j)), end="")
    print()
