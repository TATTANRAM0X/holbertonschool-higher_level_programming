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
        if cls.__name__ == "Rectangle":
            dummyInstance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummyInstance = cls(1)
        dummyInstance.update(**dictionary)
        return dummyInstance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l
