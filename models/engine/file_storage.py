#!/usr/bin/python3
"""Serialization and Deserialization of JSON files"""

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """A class for Serializing and Deserializing JSON files"""
    __file_path = 'file.json'
    __objects = {}
    allclasses = {"BaseModel": BaseModel, "User": User}

    def __init__(self):
        """Default initializing"""
        pass

    def all(self):
        """Returns a dictionary with all the objects of the program"""
        return self.__objects

    def path(self):
        """Returns the path of the JSON file"""
        return self.__file_path

    def new(self, obj):
        """Creates a new object for the program, or updates an older object"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj   

    def save(self):
        """Serialization:
            Saves all dictionaries from the objects to 'file.json'
        """
        dct = self.__objects.copy()
        for k, o in dct.items():
            dct[k] = o.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(dct, fp)

    def reload(self):
        """Deserialization:
        If 'file.json' exists, extracts all its dicts and converts them in
        objects to be read for the program
        """
        try:
            if os.stat(self.__file_path).st_size == 0:
                raise EOFError()
            with open(self.__file_path, 'r', encoding='UTF-8') as fp:
                obj = json.load(fp)
            for k, v in obj.items():
                """Creates a instance of an object class from the dictionary
                Example:
                    ex = self.__allclasses[v['__class__']](**v)
                        -> ex = BaseModel({'id': '98',
                                'created_at': '15-05-2019T17:30:46.15623',
                                ...})
                        -> ex = User(**kwargs)
                        -> ...etc
                """
                self.__objects[k] = self.allclasses[v['__class__']](**v)
        except FileNotFoundError:
            pass
        except EOFError:
            pass
