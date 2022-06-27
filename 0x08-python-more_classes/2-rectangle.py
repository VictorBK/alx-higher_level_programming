#!/usr/bin/python3

"""
Create two privte instances attributes of
width and height
and public area and perimeter methods
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Initializes rectangles """
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__width = value

    def area(self):
        """return the rectangle area"""
        return(self.__height * self.__width)
    
    def perimeter(self):
        """return the rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2 + self.__height *2)
