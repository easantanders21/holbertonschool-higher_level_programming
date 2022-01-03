#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        nmax = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > nmax:
                nmax = my_list[i]
        return(nmax)
    else:
        return(None)
