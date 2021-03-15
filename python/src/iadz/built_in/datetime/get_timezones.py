#!/usr/bin/env python
from datetime import datetime, timedelta
import pytz  # $ pip install pytz

utc_offset = timedelta(hours=14, minutes=30)
now = datetime.now(pytz.utc)  # current time
print(
    {
        tz.zone
        for tz in map(pytz.timezone, pytz.all_timezones_set)
        if now.astimezone(tz).utcoffset() == utc_offset
    }
)

