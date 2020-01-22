#!/usr/bin/python3
"""This is the state class for project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """ FileStorage relationship between State and City. """
            ret = []
            for city in list(models.storage.all)(City).values():
                if city.state_id == self.id:
                    ret.append(city)
            return ret
