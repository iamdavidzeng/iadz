# -*- coding: utf-8 -*-
from time import sleep

from singleton import Session, User


session = Session()


def add_user():

    user = User(id=1, first_name="David", last_name="Zeng", gender="male")

    session.add(user)
    print(f"Add User[1]")
    sleep(30)
    session.commit()
    print(f"Commit User[1]")
    return


if __name__ == "__main__":
    print(f"session: {id(session)}")
    add_user()
