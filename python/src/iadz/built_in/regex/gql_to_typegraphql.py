# -*- coding: utf-8 -*-


import re
from sre_constants import GROUPREF

stream = """
type MsgCenterLandlordContact implements Node {
        id: ID!
        firstName: String!
        lastName: String!
        userUuid: NonEmptyString!
        liveChatEnabled: Boolean!
        online: Boolean
    }

type MsgCenterLandlordContact implements 123 {
        id: ID!
        firstName: String!
        lastName: String!
        userUuid: NonEmptyString!
        liveChatEnabled: Boolean!
        online: Boolean
    }
"""


def convert(match):
    for group in match.groups():
        print(group.split("\n"))
    return "1"


parser = re.compile(r"(\w+[\s\w]+\{[\s\w\n\:\!]+\})")
result = parser.sub(convert, stream)
print(f"result: {result}")
