#!/usr/bin/python3
"""defines class MyList"""


class MyList(list):
    def print_sorted(self):
        """prints a sorted version of given list"""
        print(sorted(self))