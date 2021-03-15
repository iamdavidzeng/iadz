# -*- coding: utf-8 -*-

from datetime import datetime


class InvalidUpdateSince(Exception):
    pass


def str_to_time(time_str: str):

    try:
        converted_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        datetime_now = datetime.now()

        datetime_diff = datetime_now - converted_time
        if datetime_diff.days > 7:
            raise InvalidUpdateSince(
                f"Interval between {datetime_now} and {converted_time} cannot be grater than 7 days"
            )

        print(f"time: {datetime_diff}")
    except ValueError as e:
        print(e.args[0])


if __name__ == "__main__":

    str_to_time("2021-05-01 00:00:00")
