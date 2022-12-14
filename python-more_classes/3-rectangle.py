#!/usr/bin/python3
""" Class that defines a rectangle """


class Rectangle:
    """
    class defined by width and height with public instance methods
    that return Rectangle's area and perimeter
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ setter and getter of height property """
    @property
    def height(self):
        """ Retrieves the instance's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ setter and getter of width property """
    @property
    def width(self):
        """ Retrieves the instance's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    Public instance method that returns the rectangle area
    """
    def area(self):
        area = self.width * self.height
        return area

    """
    Public instance method that returns the rectangle perimeter
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = (self.width + self.height) * 2
        return perimeter

    """
    Method that returns the rectangle as a string with the character "#"
    If width or height are equal to 0, returns an empty string
    """
    def __str__(self):
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle
        else:
            for x in range(self.height):
                if x != 0:
                    rectangle += "\n"
                for y in range(self.width):
                    rectangle += "#"
        return rectangle
