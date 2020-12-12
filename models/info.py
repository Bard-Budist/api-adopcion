#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel
from sqlalchemy.orm import relationship

Base = declarative_base()

class Info(BaseModel, Base):
    """Representation of Info """
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    descripcion = Column(String(150), nullable=False)
    # Relacion aqui
    animal = Column(Integer, nullable=False)
    imagen = Column(LargeBinary(), nullable=False)
    raza = Column(String(100), nullable=False)
    # Relacion aqui
    genero = Column(Integer,nullable=False)
    edad = Column(String(30), nullable=False)
    cantidad = Column(Integer, nullable=False)
    # Relacion aqui
    vacunas = Column(Integer, nullable=False)
    requisitos = Column(String(100), nullable=False)
    # Relacion aqui
    operado = vacunas = Column(Integer, nullable=True)



    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)