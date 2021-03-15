# -*- coding:utf-8 -*-

import os
import re

raw_value = """
"""


ENV_MATCHER = re.compile(
    r"""
    \$\{
    ([^}:\s]+)
    :?
    ([^}]+)?
    \}
    """,
    re.VERBOSE,
)


def _replace_env_var(match):
    env_var, default = match.groups()
    print(match.groups())
    value = os.environ.get(env_var, None)
    return value or default


def demo(raw_value):
    value = ENV_MATCHER.sub(_replace_env_var, raw_value)
    return value


def double(match):
    print(match.groups())
    return "1"


def demo1(value):
    MATCHER = re.compile(
        r"""
        (\w+)
        \s?
        loves
        \s?
        (\w+)
        """,
        re.VERBOSE,
    )
    value = MATCHER.sub(double, value)
    return value


if __name__ == "__main__":
    value = """DB_URIS:
    "payments:Base": mysql+mysqlconnector://${DB_USER:root}:${DB_PASS:}@${DB_SERVER:localhost}/${DB_NAME:payments}
"""
    # print(demo(value))

    s = ["Marry loves Tom", "Dasiy loves Smith"]
    for i in s:
        demo1(i)
