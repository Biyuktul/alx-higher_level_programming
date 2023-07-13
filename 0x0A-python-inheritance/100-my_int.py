#!/usr/bin/python3
"""defines MyInt class"""


class MyInt(int):
    """represents integer object with -= and == operators reversed"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return super().__eq__(other)
