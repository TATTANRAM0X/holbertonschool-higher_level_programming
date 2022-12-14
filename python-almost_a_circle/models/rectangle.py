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

    @height.setter
    def height(self, value):
        ''' height setter method validation '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        ''' width getter method validation '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter method validation '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        ''' x getter method validation '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter method validation '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y getter method validation '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter method validation '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Returns the value of the area of the Rectangle instance '''
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the instance with the character #"""
        if self.__y > 0:
            for _ in range(self.__y):
                print()

        for row in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        ''' Returns a string representation of a Rectangle '''
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        ''' Assigns an argument to each attribute '''
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return format of dictionary"""
        return {
            'id': self.id, 'x': self.x, 'y': self.y,
            'width': self.width, 'height': self.height
        }
