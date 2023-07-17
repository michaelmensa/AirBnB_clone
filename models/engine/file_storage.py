#!/usr/bin/python3


'''
Module for file storage
'''

import models
from models.base_model import BaseModel
import json


class FileStorage():
    '''
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' public instance method that returns dictionary __objects
        '''

        return self.__objects

    def new(self, obj):
        ''' this public instance method sets in __objects the obj with key
        <obj class name>.id
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' this public instance method serializes __objects to a JSON
        file(path:__file_path)
        '''

        new_dict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
                json.dump(new_dict, f)

    def reload(self):
        '''
        this public instance method deserializes the JSON file to __objects
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                new_objects = json.load(f)
                for key, value in new_objects.items():
                    reloaded_obj = eval('{}(**value)'.format(value['__class__']))
                    self.__objects[key] = reloaded_obj
        except (IOError, json.JSONDecodeError):
            pass
