#!/usr/bin/python3
"""This is the place class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import environ
from sqlalchemy.ext.declarative import declarative_base

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter property that retrieves a list of places instances
            based in the id of a place and the review place id"""
            reviews = models.storage.all(Review)
            return [n for n in reviews.values() if n.place_id == self.id]

        @property
        def amenities(self):
            """ getter attribute that returns a list of all amenities ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """setter attribute which will fill the amenity_ids list with
            the intended content"""
            if (isinstance(obj, Amenity) and obj not in self.amenity_ids):
                self.amenities.append(obj.id)
