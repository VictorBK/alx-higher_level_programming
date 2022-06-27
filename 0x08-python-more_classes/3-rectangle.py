#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        @property(height) - retrieve value
        @height.setter - set value
        @property(width) - retrieve value
        @width.setter - set value
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle."""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__height == value

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
        if (self.__width == 0 or self.__height ==0):
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """print rectangle with str function having # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

