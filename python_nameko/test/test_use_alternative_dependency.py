# -*- coding: utf-8 -*-


import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from nameko.rpc import rpc
from nameko.testing.services import worker_factory

from nameko_sqlalchemy import DatabaseSession

Base = declarative_base()


class Result(Base):

    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    value = Column(String(64))


class Service:

    name = 'service'

    db = DatabaseSession(Base)

    @rpc
    def save(self, value):
        result = Result(value=value)
        self.db.add(result)
        self.db.commit()


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session_cls = sessionmaker(bind=engine)
    return session_cls()


def test_service(session):
    service = worker_factory(Service, db=session)

    service.save("hello, world!")
    assert session.query(Result.value).all() == [("hello, world!",)]
