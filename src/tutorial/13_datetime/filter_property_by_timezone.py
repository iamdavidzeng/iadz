# -*- coding: utf-8 -*-


from datetime import date, datetime, time

import pytz

# Refer: https://stackoverflow.com/questions/35085289/getting-timezone-name-from-utc-offset

properties = [
    {"property_id": 1, "timezone": "America/Bahia"},
    {"property_id": 2, "timezone": "Europe/Dublin"},
    {"property_id": 3, "timezone": "America/Belize"},
    {"property_id": 4, "timezone": "UTC"},
    {"property_id": 5, "timezone": "Asia/Shanghai"},
    {"property_id": 6, "timezone": "Iceland"},
]

min_time = time(0, 0, 0)
max_time = time(0, 30, 0)

property_ids = list(
    property_["property_id"]
    for property_ in properties
    if min_time
    # <= datetime.now(pytz.utc).astimezone(pytz.timezone(property_["timezone"])).time()
    <= pytz.utc.localize(datetime(2020, 9, 23, 16, 20, 0))
    .astimezone(pytz.timezone(property_["timezone"]))
    .time()
    < max_time
)

print(property_ids)

property_with_max_datetime = list(
    (
        property_["property_id"],
        datetime.combine(
            datetime.now(pytz.utc).astimezone(pytz.timezone(property_["timezone"])),
            datetime.max.time(),
        ).astimezone(pytz.utc),
    )
    for property_ in properties
    if property_["property_id"] in property_ids
)

print(property_with_max_datetime)
