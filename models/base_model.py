#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


'''This module represents the base model'''


class BaseModel():
    '''this represents the basemodel class'''

    def __init__(self, *args, **kwargs):
        '''this constructor is an updated version'''

        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs and kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'update_at':
                    v = datetime.strptime(v, time_format)
                    if k != "__class__":
                        setattr(self, k, v)

    def __str__(self):
        '''this method defines the string representation of the basemodel'''
        obj_dict = self.__dict__.copy()
        return "[{}] ({}) {}".format(type(self).__name__, self.id, obj_dict)

    def save(self):
        '''this method updates updated_at with current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''this method returns a dictionary containing all keys/values'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = str(type(self).__name__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return (obj_dict)
