#!/usr/bin/python3
def multiple_returns(sentence):
    if not(len(sentence)):
        first_char = None
    else:
        first_char = sentence[0]
    new_tuple = (len(sentence), first_char)
    return new_tuple
