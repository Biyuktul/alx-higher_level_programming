#!/usr/bin/python3
"""define a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new instance of the Rectangle class.
    - area(self): Calculates the area of the rectangle.
    - integer_validator(self): Validates width and height of the rectangle
    """
    def __init__(self, width, height):
        try:
            super().integer_validator(width)
            self.__width = width
        except (ValueError, TypeError):
            pass
        try:
            super().integer_validator(height)
            self.__height = height
        except (ValueError, TypeError):
            pass

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
