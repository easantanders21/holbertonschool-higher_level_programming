#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        new_tuple = (length, sentence[0])
        return(new_tuple)
    else:
        new_tuple = (0, None)
        return(new_tuple)
