#!/usr/bin/python3


'''
This module represents the user class
'''


from models.base_model import BaseModel


class User(BaseModel):
    '''
    This class inherits from Basemodel
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
