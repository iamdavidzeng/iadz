# -*- coding: utf-8 -*-


from enum import Enum


class SendShortMessageType(Enum):

    bind = 'bind'
    auth = 'auth'
    login = 'login'
    signup = 'signup'


if __name__ == '__main__':
    print(*SendShortMessageType)
