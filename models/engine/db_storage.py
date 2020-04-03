#!/usr/bin/python3
"""this cmodule controls the database storage engine  """

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ the class that handles database storage """
    __engine = None
    __session = None

    def __init__(self):
        """ controls attributes of DBstorage instances"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ this module returns all instances of a Class"""
        classes = [State, City, User, Place, Review, Amenity]
        dictionary = {}

        if cls in classes:
            queries = self.__session.query(cls).all()
            for results in queries:
                key = "{}.{}".format(type(results), results.id)
                dictionary[key] = results
        else:
            for clss in classes:
                queries = self.__session.query(clss).all()
                for results in queries:
                    key = "{}.{}".format(type(results).__name__, results.id)
                    dictionary[key] = results
        return dictionary

    def new(self, obj):
        """ this adds a new instance to the session"""
        self.__session.add(obj)

    def save(self):
        """ this saves the instance into the database  """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an object from database  """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reloads an oject by loading from database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
