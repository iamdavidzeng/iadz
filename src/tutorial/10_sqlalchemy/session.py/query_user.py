# -*- coding: utf-8 -*-
from time import sleep

from singleton import User
from add_user import session


def get_user(id_):

    query = session.query(User)

    resource = query.filter(User.id == id_).first()

    return resource

if __name__ == "__main__":
    print(f"session: {id(session)}")
    while True:

        user = get_user(1)

        if user:
            print(f"Find User[1] {user}")
            break
        else:
            print(f"Can't find User[1] now.")
            session.expire_all()
            sleep(5)
            
