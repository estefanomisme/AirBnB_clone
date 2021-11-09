#!/usr/bin/python3
"""A module for a generic BaseModel class"""

import uuid
import datetime

"""ftm = format of current time"""
ftm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes a BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of all the atributes of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """Records the last changes made to the object"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of an
        object instance
        """
        dct = self.__dict__.copy()
        if "created_at" in dct:
            dct["created_at"] = dct["created_at"].strftime(ftm)
        if "updated_at" in dct:
            dct["updated_at"] = dct["updated_at"].strftime(ftm)
        dct["__class__"] = "{}".format(self.__class__.__name__)
        return dct
