#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_int = 0
    for v in a_dictionary.values():
        if v > max_int:
            max_int = v
    return max_int
