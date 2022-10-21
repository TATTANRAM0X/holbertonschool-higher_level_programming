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

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return format of dictionary"""
        dictionary = {'id': self.id, 'x': self.x, 'y': self.y,
                        'size': self.size}
        return dictionary
