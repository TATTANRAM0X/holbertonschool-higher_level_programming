#!usr/bin/python3

from models.base import Base

class Rectangle(Base):
    ''' Rectangle class is created instruction of the task '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Inicialzes instance of Rectangle class '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

