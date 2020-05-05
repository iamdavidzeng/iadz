# -*- coding: utf-8 -*-

"""
在涉及到session的部分，
为了保证数据的一致性，在raise的时候进行session.rollback()
"""

from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def rollback_once_failed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as exc:
            self.session.rollback()
            print("commit failed, rollback")
            raise exc
        else:
            self.session.commit()
            print("commit successfully")
    return wrapper


class InsertError(Exception):
    pass


class BillingService(object):
    def __init__(self, session):
        self.session = session

    @rollback_once_failed
    def create_item(self):
        self.session.execute(
            """
            INSERT INTO `user_role` (`user_id`, `role`)
            VALUES
                (1, 'partner');
            """
        )
        raise InsertError("Whoops, Error!")


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/test")
    Session = sessionmaker(bind=engine)

    session = Session()

    billing = BillingService(session=session)
    billing.create_item()
