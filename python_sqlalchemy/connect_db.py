# -*- coding: utf-8 -*-


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+mysqlconnector://root:12345678@locahost:3306/demo')
DBSession = sessionmaker(bind=engine)


if __name__ == '__main__':
    session = DBSession()
    new_user = User(name='david')
    session.add(new_user)
    session.commit()
    session.close()
