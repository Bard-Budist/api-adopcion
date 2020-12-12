#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from .usuario import Usuario
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base_model import BaseModel

Base = declarative_base()

class Municipio(BaseModel, Base):
    """Representation of Municipio """
    __tablename__ = 'municipio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    # Relacion aqui
    departamento = Column(Integer, nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)