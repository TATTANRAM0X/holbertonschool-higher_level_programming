#!/usr/bin/python3
''' File for class Square '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class is created instruction of the task '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Inicialzes instance of Square class '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """Returns the size of the object"""
        self.width = value
        self.height = value
