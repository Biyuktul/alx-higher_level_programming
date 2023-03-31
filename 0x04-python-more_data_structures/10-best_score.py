#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = ''
    max_int = 0
    for k, v in a_dictionary.items():
        if v > max_int:
            max_int = v
            max_key = k
    return max_key
