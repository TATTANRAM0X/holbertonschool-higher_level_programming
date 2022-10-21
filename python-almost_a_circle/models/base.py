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
