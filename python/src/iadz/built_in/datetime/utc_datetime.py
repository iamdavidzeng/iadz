# -*- coding: utf-8 -*-

import time

from datetime import datetime, timezone, timedelta


if __name__ == "__main__":

    utcnow = datetime.utcnow()
    print(f"UTC+00:00 now: {utcnow.isoformat()}")

    utc6_now = datetime.now(tz=timezone(offset=timedelta(hours=6)))
    print(f"UTC+06:00 now: {utc6_now.isoformat()}")
