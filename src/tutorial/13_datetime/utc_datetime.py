# -*- coding: utf-8 -*-

import time

from datetime import datetime


if __name__ == "__main__":

    utcnow = datetime.utcnow()
    print(f"second utcnow: {utcnow.isoformat()}")
