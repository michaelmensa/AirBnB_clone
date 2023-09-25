#!/usr/bin/python3


'''
Module for file storage
'''


import json

class FileStorage():
    '''
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' public instance method that returns dictionary __objects
        '''

        return self.__objects

    def new(self, obj):
        ''' this public instance method sets in __objects the obj with key
        <obj class name>.id
        '''
        key = f'{type(obj).__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        ''' this public instance method serializes __objects to a JSON
        file(path:__file_path)
        '''

        filename = self.__file_path
        with open(filename, 'w') as json_file:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, json_file)

    def reload(self):

        '''
        this public instance method deserializes the JSON file to __objects
        '''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        filename = self.__file_path
        class_map = {'BaseModel': BaseModel, 'User': User,
                     'Place': Place, 'State': State,
                     'City': City, 'Amenity': Amenity, 
                     'Review': Review}
        try:
            with open(filename, 'r') as json_file:
                for obj in json.load(json_file).values():
                    self.new(class_map[obj['__class__']](**obj))
        except FileNotFoundError:
            pass
