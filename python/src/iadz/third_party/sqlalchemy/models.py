# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String


engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo", echo=True)
Session = sessionmaker(bind=engine)


Base = declarative_base()


class Foo(Base):

    __tablename__ = "foo"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=True)

    bazs = relationship("Baz", secondary="bar")

    def __repr__(self) -> str:
        return f"<Foo(name={self.name})>"


class Bar(Base):

    __tablename__ = "bar"
    id = Column(Integer, primary_key=True)
    foo_id = Column(Integer, ForeignKey("foo.id"))
    baz_slug = Column(String(16), ForeignKey("baz.slug"))

    bazs = relationship("Baz")

    def __repr__(self) -> str:
        return f"<Bar(foo_id={self.foo_id}, baz_slug={self.baz_slug})>"


class Baz(Base):

    __tablename__ = "baz"
    slug = Column(String(16), primary_key=True)

    def __repr__(self) -> str:
        return f"<Baz(slug={self.slug})>"


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


Base.metadata.create_all(engine)

session = Session()
