#!/usr/bin/python3
"""
Defines a Student class with attributes first_name, last_name, and age.
Includes methods to serialize to JSON and reload attributes from a JSON dict.
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
        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
