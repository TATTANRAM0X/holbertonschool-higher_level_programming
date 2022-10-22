#!/usr/bin/python3
''' File for class Base '''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of a list of dict '''
        if list_dictionaries is None:
            list_dictionaries = []
        dictJson = json.dumps(list_dictionaries)
        return dictJson

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation json_string '''
        if json_string is None or len(json_string) == 0:
            return []
        strJson = json.loads(json_string)
        return strJson

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set '''

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummyInstance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummyInstance = cls(1)
        dummyInstance.update(**dictionary)
        return dummyInstance

    @classmethod
    def load_from_file(cls):
        '''  Returns a list of instances '''
        filename = cls.__name__ + ".json"
        list = []
        try:
            with open(filename, 'r') as f:
                list = cls.from_json_string(f.read())
            for i, e in enumerate(list):
                list[i] = cls.create(**list[i])
        except:
            pass
        return list
