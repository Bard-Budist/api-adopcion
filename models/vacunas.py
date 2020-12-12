#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel

Base = declarative_base()

class Vacunas(BaseModel, Base):
    """Representation of Vacunas """
    __tablename__ = 'vacunas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)