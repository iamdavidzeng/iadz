# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import joinedload, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo", echo=True)
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Foo(Base):

    __tablename__ = "foo"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=True)

    bazs = relationship("Baz", secondary="bar")


class Bar(Base):

    __tablename__ = "bar"
    id = Column(Integer, primary_key=True)
    foo_id = Column(Integer, ForeignKey("foo.id"))
    baz_slug = Column(String(16), ForeignKey("baz.slug"))

    bazs = relationship("Baz")


class Baz(Base):

    __tablename__ = "baz"
    slug = Column(String(16), primary_key=True)


class Storage:
    def __init__(self, session: Session(), model: any) -> None:
        self.session = session
        self.model = model

    @property
    def query(self):
        return self.session.query(self.model)

    def insert(self, data: dict) -> object:
        data = self.model(**data)
        resource = self.session.add(data)
        return resource

    def get(self, id_: int) -> object:
        resource = self.query.filter(self.model.id == id_).one()
        return resource

    def list(
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

    session = Session()

    storage = Storage(session, Foo)

    query = storage.query.join(Foo.bazs).with_entities(Foo.id, Baz.slug)

    print(query.all())
