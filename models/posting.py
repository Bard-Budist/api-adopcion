#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel

Base = declarative_base()

class Posting(BaseModel, Base):
    """Representation of Posting """
    __tablename__ = 'posting'
    id = Column(Integer, primary_key=True)
    # Relacion aqui
    usuario = Column(Integer, nullable=False)
    #Relacion aqui
    info = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    estado = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)