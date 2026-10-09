#!/usr/bin/python3
"""
FileStorage Engine
Handles serialization and deserialization of instances to/from JSON.
"""
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects, optionally filtered by class."""
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            cls_dict = {}
            for k, v in FileStorage.__objects.items():
                if isinstance(v, cls):
                    cls_dict[k] = v
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        """
        Deserializes the JSON file to __objects if file exists.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for key, val in obj_dict.items():
                        cls_name = val.get("__class__")
                        if cls_name in classes:
                            FileStorage.__objects[key] = classes[cls_name](**val)
            except Exception:
                pass
