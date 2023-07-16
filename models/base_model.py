#!/usr/bin/python3

import uuid
from datetime import datetime
import models


'''this module represents the base model'''

class BaseModel:
    '''this represents the basemodel class'''

    '''def __init__(self, id=None, created_at=None, updated_at=None):
        this method initializes the basemodel class
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()'''

    def __init__(self, *args, **kwargs):
        '''this constructor is an updated version'''
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            time_format = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(self.created_at, time_format)
            self.updated_at = datetime.strptime(self.updated_at, time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
	    models.storage.new(self)

    def __str__(self):
        '''this method defines the string representation of the basemodel'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''this method updates updated_at with current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''this method returns a dictionary containing all keys/values'''
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
