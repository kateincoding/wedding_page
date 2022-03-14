#!/usr/bin/python3
"""db: file for DBStorage"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy import MetaData
from logging import info

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

user = getenv('WED_MYSQL_USER')
pssw = getenv('WED_MYSQL_PWD')
host = getenv('WED_MYSQL_HOST')
db = getenv('WED_MYSQL_DB')
sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, pssw, host, db)

classes = {"User": User}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """init"""
        self.__engine = create_engine(sql, pool_pre_ping=True)


    def all(self, cls=None):
        """sum"""
        dictionary = {}
        for x in classes:
            if cls is None or cls is classes[x] or cls is x:
                data = self.__session.query(classes[x]).all()
                for element in data:
                    key = element.__class__.__name__ + '.' + str(element.id)
                    new_dict[key] = element
        return(new_dict)


    def new(self, obj):
        """add an object"""
        if obj:
            self.__session.add(obj)


    def save(self):
        """commit all changes"""
        self.__session.commit()


    def delete(self, obj=None):
        """delete from current database"""
        if obj:
            info('DELETING...')
            self.__session.delete(obj)


    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = session()


    def close(self):
        """close session"""
        selkf.__session.close()
