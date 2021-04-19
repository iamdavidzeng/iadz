# -*- coding: utf-8 -*-
import time

import eventlet
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


def update_without_yield_control(sleep: int = 0):
    """
    Output:
        >>> I got sleep duration: 5
        >>> 5
        >>> I got sleep duration: 0
        >>> 0
    """
    print(f"I got sleep duration: {sleep}")
    session = Session()

    # 1st way
    item = session.query(Balance).filter(Balance.id == 1).with_for_update().one()
    c = item.c + 1
    item.c = c

    # 2nd way
    # item = (
    #     session.query(Balance)
    #     .filter(Balance.id == 1)
    #     .update({Balance.c: Balance.c + 1})
    # )

    time.sleep(sleep)
    session.commit()
    return sleep


def update_with_yield_control(sleep: int = 0):
    """
    Output:
        >>> I got sleep duration: 5
        >>> I got sleep duration: 0
        >>> raise TimeoutError()
    """
    print(f"I got sleep duration: {sleep}")
    session = Session()

    # 1st way
    item = session.query(Balance).filter(Balance.id == 1).with_for_update().one()
    c = item.c + 1
    item.c = c

    # 2nd way
    # item = (
    #     session.query(Balance)
    #     .filter(Balance.id == 1)
    #     .update({Balance.c: Balance.c + 1})
    # )

    eventlet.sleep(sleep)
    session.commit()
    return sleep


if __name__ == "__main__":
    pool = eventlet.GreenPool(200)

    for result in pool.imap(update_without_yield_control, [5, 0]):
        print(result)
