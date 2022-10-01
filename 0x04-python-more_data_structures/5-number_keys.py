#!/usr/bin/python3
def number_keys(a_dictionary):
    """Func to report number of keys in a dct"""
    keys = list(a_dictionary.keys())
    num = 0
    for i in range(len(keys)):
        num += 1
    return (num)
