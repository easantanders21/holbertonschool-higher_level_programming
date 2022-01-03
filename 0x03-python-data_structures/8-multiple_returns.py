#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == None:
        new_tuple = (0, None)
    new_tuple = (length, sentence[0])
    return(new_tuple)
