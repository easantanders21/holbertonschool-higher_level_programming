#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        my_list2 = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                my_list2.append(True)
            else:
                my_list2.append(False)
        return(my_list2)
    else:
        return(None)
