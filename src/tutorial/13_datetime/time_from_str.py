# -*- coding: utf-8 -*-

from datetime import datetime


def str_to_time(time_str: str):

    converted_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    print(f"time: {converted_time}")


if __name__ == "__main__":

    str_to_time("2020-01-01 00:00:00")
