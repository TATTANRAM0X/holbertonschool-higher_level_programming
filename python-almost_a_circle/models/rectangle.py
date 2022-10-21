#!/usr/bin/python3

''' File for class Rectangle '''

from models.base import Base


class Rectangle(Base):
    ''' Rectangle class is created instruction of the task '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Inicialzes instance of Rectangle class '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        '''height getter method validation'''
        return self.__height

    @property
    def width(self):
        ''' width getter method validation '''
        return self.__width

    @property
    def x(self):
        ''' x getter method validation '''
        return self.__x

    @property
    def y(self):
        ''' y getter method validation '''
        return self.__y

    @height.setter
    def height(self, value):
        ''' height setter method validation '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        ''' width setter method validation '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        ''' x setter method validation '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter method validation '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

