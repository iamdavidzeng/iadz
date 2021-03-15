# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo")
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Balance(Base):

    __tablename__ = "balance"

    id = Column(Integer, primary_key=True)
    c = Column(Integer)


def update_table():

    session = Session()

    query = session.query(Balance).update({Balance.c: Balance.c + 1})

    print(query)


if __name__ == "__main__":
    update_table()
