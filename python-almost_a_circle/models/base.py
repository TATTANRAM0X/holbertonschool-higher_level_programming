#!/usr/bin/python3
''' File for class Base '''

class Base:
    ''' Base class task instruction '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Inicialezes an instance '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
