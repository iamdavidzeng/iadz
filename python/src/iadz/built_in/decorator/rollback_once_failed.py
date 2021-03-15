# -*- coding: utf-8 -*-

"""
在涉及到session的部分，
为了保证数据的一致性，在raise的时候进行session.rollback()
"""
import inspect
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def rollback_once_failed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        default_kws = get_default_args(func)
        kwargs.update(default_kws)

        commit = kwargs.get("commit")
        try:
            func(self, *args, **kwargs)
        except Exception as exc:
            self.session.rollback()
            print("commit failed, rollback")
            raise exc
        else:
            if commit:
                self.session.commit()
                print("commit successfully")
            print("func can't commit when commit is False")
    return wrapper


class InsertError(Exception):
    pass


class BillingService(object):
    def __init__(self, session):
        self.session = session

    @rollback_once_failed
    def create_item(self, commit=True):
        self.session.execute(
            """
            INSERT INTO `user` (`email`, `password`, `email_verified`, `email_token`, `newsletter_accepted`, `forgot_password_token`, `forgot_password_token_issued_at`, `password_set_by_user`, `create_password_token`, `osl_password_key_pair`, `uuid`, `created_at`, `updated_at`, `facebook_id`, `wechat_id`, `phone`, `enabled`, `role_data`)
VALUES
	('hui.zhao2@student.com', NULL, 0, NULL, 0, NULL, NULL, 0, NULL, NULL, 'd5d93672-2947-9207-cd44-c7e7e8ba4f72', '2018-02-06 10:00:00', '2018-02-06 10:00:00', NULL, NULL, NULL, 1, NULL);

            """
        )
        raise InsertError("Whoops, Error!")


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/test")
    Session = sessionmaker(bind=engine)

    session = Session()

    billing = BillingService(session=session)
    billing.create_item(commit=False)
