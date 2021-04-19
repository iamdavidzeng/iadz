# -*- coding: utf-8 -*-
import sys
import time
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

    # 1st way
    item = session.query(Balance).filter(Balance.id == 1).with_for_update().one()

    c = item.c + int(sys.argv[2])
    item.c = c

    # 2nd way
    # item = (
    #     session.query(Balance)
    #     .filter(Balance.id == 1)
    #     .update({Balance.c: Balance.c + 1})
    # )

    time.sleep(int(sys.argv[1]))

    session.commit()

    print(item)


if __name__ == "__main__":
    update_table()
