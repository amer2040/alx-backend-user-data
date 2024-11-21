#!/usr/bin/env python3
"""user module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """user's class"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250))
    reset_token = Column(String(250))
