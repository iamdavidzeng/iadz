# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo", echo=True)
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Foo(Base):

    __tablename__ = "foo"
    id = Column(Integer, primary_key=True)


class Bar(Base):

    __tablename__ = "bar"
    id = Column(Integer, primary_key=True)
    foo_id = Column(Integer, ForeignKey("foo.id"))
    amount = Column(Integer, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    foo = relationship(
        "Foo",
        backref="bars",
        primaryjoin="and_(Bar.foo_id == Bar.id, Bar.deleted_at == None)",
    )


class DummyService:
    def __init__(self) -> None:
        self.session = Session()
        self.model = Bar

    @property
    def query(self):
        return self.session.query(self.model)

    def add_bar(self, data: dict):
        resource = self.session.add(self.model(**data))
        self.session.commit()
        return resource

    def get_bar(self, id_: int):

        Bar = self.query.filter(self.model.id == id_)

        return Bar.one()

    def list_bars(
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

    query = dummy.session.query(Foo).join(Bar).with_entities(Foo.id, Bar.id, Bar.amount)

    for foo_id, bar_id, bar_amount in query.all():
        print(foo_id, bar_id, bar_amount)
