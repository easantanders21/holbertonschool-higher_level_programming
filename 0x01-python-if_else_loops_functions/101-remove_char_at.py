#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    if n < 0 or n > len(str):
        str2 = str
    else:
        for i in range(n):
            str2 = str2 + str[i]
        for i in range(n + 1, len(str)):
            str2 = str2 + str[i]
    return (str2)
