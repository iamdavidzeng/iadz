# -*- coding: utf-8 -*-


from sqlalchemy import *
from sqlalchemy.orm import (
    scoped_session, sessionmaker, relationship, backref
)
from sqlalchemy.ext.declarative import declarative_base


# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo", convert_unicode=True)
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine
))


Base = declarative_base()
Base.query = session.query_property()


class Department(Base):

    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Employee(Base):

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship(
        Department,
        backref=backref(
            "employee",
            uselist=True,
            cascade="delete,all"
        )
    )
