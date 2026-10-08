#!/usr/bin/python3
"""
BaseModel Module
Defines all common attributes/methods for other classes.
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    Class BaseModel that defines common attributes and methods
    for other classes in the project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        
        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs of attributes to initialize from dictionary.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates updated_at with current datetime and saves storage to JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance, adding '__class__' and converting timestamps
        to ISO formatted strings.
        """
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
