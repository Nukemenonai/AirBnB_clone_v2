#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
import models

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)


    cities = relationship("City", backref="state", cascade='all, delete')
    @property
    def cities(self):
        allcities = models.storage.all(City)
        return [n for n in allcities.values() if n.state_id == self.id]
