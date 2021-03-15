# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):

    __tablename__ = "person"

    id = Column(Integer, primary_key=True)

    nickname = Column(String(32), nullable=True)
    first_name = Column(String(32), nullable=True)
    last_name = Column(String(32), nullable=True)
