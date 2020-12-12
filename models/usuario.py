#!/usr/bin/python
""" holds class animal"""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel

Base = declarative_base()

class Usuario(BaseModel, Base):
    """Representation of Usuario """
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    edad = Column(Integer, nullable=False)
    correo = Column(String(100), nullable=False)
    contraseña = Column(String(30), nullable=False)
    imagen = Column(LargeBinary(), nullable=True)
    telefono = Column(String(30), nullable=True)
    celular = Column(String(30), nullable=True)
    facebook = Column(String(100), nullable=True)
    whatsapp = Column(String(100), nullable=True)
    # Relacion aqui
    municipio = Column(Integer,nullable=False)
    direccion = Column(String(150), nullable=True)
    

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)