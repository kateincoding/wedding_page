#!/usr/bin/python3
"""Module for User"""
from models.basemodel import Basemodel, Base
from sqlalchemy import DateTime
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer

from sqlalchemy.orm import relationship, backref
from os import getenv

class User(Basemodel, Base):
    """class for users"""
    __tablename__ = 'users'
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    whatsapp = Column(Integer, nullable=False)
    email = Column(String(30))
    num_entradas = Column(Integer, default=1)
    confirmation = Column(Integer, default=0)
    password = Column(String(60), nullable=False)
