#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    roman_dictionary = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                             ('C', 100), ('D', 500), ('M', 1000)])
    res = 0
    for num_act, num_prox in zip(roman_string, roman_string[1:]):
        if roman_dictionary[num_act] < roman_dictionary[num_prox]:
            res -= roman_dictionary[num_act]
        else:
            res += roman_dictionary[num_act]
    res += roman_dictionary[roman_string[-1]]
    return res
