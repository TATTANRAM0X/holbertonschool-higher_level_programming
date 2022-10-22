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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string representation of list_objs '''
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))

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
            with open(filename, 'r') as file:
                list = cls.from_json_string(file.read())
            for i, e in enumerate(list):
                list[i] = cls.create(**list[i])
        except:
            pass
        return list
