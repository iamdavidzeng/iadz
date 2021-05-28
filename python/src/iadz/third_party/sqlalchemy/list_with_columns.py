# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
import logging


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo")
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Booking(Base):

    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)


class Balance(Base):

    __tablename__ = "balances"
    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Integer, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    booking = relationship(
        "Booking",
        backref="balances",
        primaryjoin="and_(Balance.booking_id == Booking.id, Balance.deleted_at == None)",
    )


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

    Base.metadata.create_all(engine)

    dummy = DummyService()

    query = (
        dummy.session.query(Booking)
        .join(Balance)
        .with_entities(Booking.id, Balance.id, Balance.amount)
    )

    for b in query.all():
        print(b)
