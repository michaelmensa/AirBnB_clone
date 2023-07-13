#!/usr/bin/python3


'''
Module represents review
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    This class inherits basemodel
    '''

    place_id = ""
    user_id = ""
    text = ""
