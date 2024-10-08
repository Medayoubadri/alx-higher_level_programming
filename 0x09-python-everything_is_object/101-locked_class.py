#!/usr/bin/python3
class LockedClass:
    '''
    Prevents the user from creating new instance attributes
    but attributes called "first_name".
    '''
    __slots__ = ['first_name']