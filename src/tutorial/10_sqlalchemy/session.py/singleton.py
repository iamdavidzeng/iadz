# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
Answer Link: https://docs.sqlalchemy.org/en/13/faq/sessions.html#i-m-re-loading-data-with-my-session-but-it-isn-t-seeing-changes-that-i-committed-elsewhere
"""


DeclarativeBase = declarative_base()


class User(DeclarativeBase):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(String(8), nullable=False)


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo")
DeclarativeBase.metadata.create_all(engine)
connection = engine.connect()
DeclarativeBase.metadata.bind = engine
Session = sessionmaker(bind=connection)
