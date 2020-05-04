# -*- coding: utf-8 -*-


from enum import Enum


class SendShortMessageType(Enum):

    bind = "bind"
    auth = "auth"
    login = "login"
    sign_up = "sign_up"


if __name__ == "__main__":
    print(*SendShortMessageType)
