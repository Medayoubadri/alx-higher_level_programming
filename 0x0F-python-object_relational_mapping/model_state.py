#!/usr/bin/python3
"""
Contains the class definition of a Stateand
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:
    - inherits from Base
    - links to the MySQL table states
    - class attribute id that represents a column of an auto-generated,
      unique integer, can't be null and is a primary key
    - class attribute name that represents a column of a string
      with maximum 128 characters and can't be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
