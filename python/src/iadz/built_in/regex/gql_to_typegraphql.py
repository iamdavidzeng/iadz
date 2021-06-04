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
        lines = group.split("\n")
        for index, line in enumerate(lines):
            prefix = ""
            if index == 0:
                prefix = "@ObjectType()\n"
                line_list = line.split(" ")
                line = " ".join(["export class", line_list[1], line_list[-1], "\n"])
            
            if ":" in line:
                type_ = line.strip().split(" ")[1]
                prefix = f"@Field(() => {type_})\n"
                if "!" in line:
                    type_ = type_.replace("!", "")
                    nullable = "{ nullable: false }"
                    prefix = f"@Field(() => {type_}, {nullable})\n"

            new_line = prefix + line.strip().replace("!", "").replace("ID", "number").lower() + "\n"
            lines[index] = new_line
    return "\n".join(lines)


parser = re.compile(r"(\w+[\s\w]+\{[\s\w\n\:\!]+\})")
result = parser.sub(convert, stream)
print(f"result: {result}")
