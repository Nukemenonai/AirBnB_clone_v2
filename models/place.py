#!/usr/bin/python3
"""This is the place class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import environ

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
)

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
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if environ.get('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review",
                               backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)

    @property
    def reviews(self):
        """getter property for reviews"""
        reviews = models.storage.all(Review)
        return [n for n in reviews.values() if n.place_id == self.id]

    @property
    def amenities(self):
        """ getter attribute """
        amidlist = []
        amenity_dic = models.storage.all(models.Amenity)
        for key, value in amenity_dic.items():
            if value.id in self.amenity_ids:
                amidlist.append(value.id)
        return amidlist

    @amenities.setter
    def amenities(self, comodidad):
        if isinstance(comodidad, models.Amenity):
            self.amenity_ids.append(comodidad.id)
        else:
            pass
