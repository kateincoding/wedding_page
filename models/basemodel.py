#!/usr/bin/python3
"""Basemodel class for all models"""
from os import getenv
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models

Base = declarative_base()
date_format = "%d/%m/%YT%H:%M:%S"

class Basemodel:
    """Base class for all classes"""
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    upt_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instance a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__' and key != "_sa_instance_state":
                    setattr(self, key, value)
                if key == "created_at" or key == "upt_at":
                    value == datetime.strptime(value, date_format)
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "upt_at" not in kwargs:
                self.upt_at = datetime.now()


    def __str__(self):
        """str representation"""
        return "[{:s}] {}".format(
               self.__class__.__name__, self.__dict__)


    def save(self):
        """Guardar un nuevo objeto"""
        self.upt_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
