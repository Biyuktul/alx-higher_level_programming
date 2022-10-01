#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Function to report only elements whic is unique to each set"""
    diff = set_2.difference(set_1)
    diff = diff.union(set_1.difference(set_2))
    return (diff)
