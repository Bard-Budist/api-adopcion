#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from .municipio import Municipio
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel
from sqlalchemy.orm import relationship

Base = declarative_base()

class Departamento(BaseModel, Base):
    """Representation of Departamento """
    __tablename__ = 'departamento'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)