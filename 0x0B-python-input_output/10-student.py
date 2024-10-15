#!/usr/bin/python3
"""
Defines a Student class with attributes first_name, last_name, and age.
Includes a method to retrieve the dictionary representation of the instance
with an optional filter for specific attributes.
"""


class Student:
    """
    Defines a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
