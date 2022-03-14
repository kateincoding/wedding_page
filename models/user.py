#!/usr/bin/python3
"""Module for User"""
from models.basemodel import Basemodel, Basemodel
from sqlalchemy import DateTime
from sqlalchemy.sql.schema import Column ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer

from sqlalchemy.orm import relationship, backref
from os import getenv

class User(Basemodel, Base):
    """class for users"""
    __tablename__ = 'users'
    first_name = Column(String(30))
    last_name = Column(String(30))
    whatsapp = Column(Integer(15), nullable=False)
    email = Column(String(30))
    num_entradas = COlumn(Integer(2), default=1)
    confirmation = Column(Integer(2), default=0)
