#!/usr/bin/python3
"""defines class MyList"""


class MyList(list):
    def print_sorted(self):
        """prints a sorted version of given list"""
        for i in self:
            if not isinstance(i, int):
                raise TypeError()
        print(sorted(self))
