#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
