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
    amount = Column(Integer)


class DummyService:
    def __init__(self) -> None:
        self.session = Session()
        self.model = Balance

    @property
    def query(self):
        return self.session.query(self.model)

    def add_balance(self, data: dict):
        resource = self.session.add(self.model(**data))
        self.session.commit()
        return resource

    def get_balance(self, id_: int):

        balance = self.query.filter(self.model.id == id_)

        return balance.one()

    def list_balances(
        self,
        filters: dict,
        order_by: dict = None,
        offset: int = None,
        limit: int = None,
        columns: list = None,
    ):
        query = self.query.filter_by(**filters)
        if order_by:
            query = query.order_by(**order_by)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if columns:
            query = query.with_entities(*columns)

        return query.all()


if __name__ == "__main__":

    dummy = DummyService()

    balances = dummy.list_balances({"id": 10}, columns=["id"])

    for b in balances:
        print(type(b))
