#!/usr/bin/python3
"""defines MyInt class"""


class MyInt(int):
    """defines MyInt to represent int object"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)
