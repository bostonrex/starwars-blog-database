import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(35), nullable=False, unique=True) 
    username = Column(String(35), nullable=False, unique=True) 
    password = Column(String(250), nullable=False)
    favorite = relationship("favorite")
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    birthyear = Column(String(15), nullable=False)
    height = Column(String(10), nullable=False) 
    eyecolor = Column(String(15), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True, nullable=False)
    climate = Column(String(250))
    population = Column(String(250))
    orbitalperiod = Column(String(250), nullable=False)  
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
