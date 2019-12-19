#!/usr/bin/python3
""" New engine for the program with alchemy and env variables mysql. """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Class for the new engine. """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializer for the instances of the class. """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Query on the current session all objects by class. """
        if cls is not None:
            res = self.__session.query(cls)
        else:
            res = self.__session.query(City).all()
            res += self.__session.query(State).all()
        output = {}
        for elem in res:
            key = '{}.{}'.format(type(elem).__name__, elem.id)
            output[key] = elem
        return output

    def new(self, obj):
        """ Add the object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session. """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and the session. """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
