#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dict by ordered keys"""
    keys = list(sorted(a_dictionary.keys()))
    j = 0
    for i in sorted(keys):
        print("{}: {}".format(keys[j], a_dictionary[i]))
        j += 1


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
