#!/usr/bin/pyhton3
"""defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square instance"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if not args and len(args) == 0:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

    def to_dictionary(self):
        """
        method to represent the rectangle with dictionary
        :return: dictionary repr of the square
        """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
