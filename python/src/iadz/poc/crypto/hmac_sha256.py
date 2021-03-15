#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hmac
import json
import hashlib
import getopt
import sys


def hmac_sha256(unsigned_data, secret):
    unsigned_data = json.dumps(unsigned_data)
    print(unsigned_data)
    signature = hmac.new(
        secret.encode("utf-8"), unsigned_data.encode("utf-8"), digestmod=hashlib.sha256
    ).hexdigest()
    return signature.upper()


if __name__ == "__main__":
    auto_barn_au = (
        {
            "method": "step2",
            "vehiclecategorytypeid": "0",
            "pickuplocationid": 7,
            "pickupdate": "20/10/2018",
            "pickuptime": "10:00",
            "dropofflocationid": 7,
            "dropoffdate": "30/10/2018",
            "dropofftime": "10:00",
            "ageid": 1,
        },
        "123456",
    )
    auto_barn_au_detail = (
        {
            "method": "step3",
            "vehiclecategorytypeid": "0",
            "pickuplocationid": 7,
            "pickupdate": "20/10/2018",
            "pickuptime": "10:00",
            "dropofflocationid": 7,
            "dropoffdate": "30/10/2018",
            "dropofftime": "10:00",
            "ageid": 1,
            "vehiclecategoryid": 19,
        },
        "123456",
    )
    auto_barn_nz = (
        {
            "method": "step2",
            "vehiclecategorytypeid": "0",
            "pickuplocationid": 1,
            "pickupdate": "20/10/2018",
            "pickuptime": "10:00",
            "dropofflocationid": 1,
            "dropoffdate": "30/10/2019",
            "dropofftime": "10:00",
            "ageid": 1,
        },
        "123456",
    )
    auto_barn_nz_detail = (
        {
            "method": "step3",
            "vehiclecategorytypeid": "0",
            "pickuplocationid": 1,
            "pickupdate": "20/10/2018",
            "pickuptime": "10:00",
            "dropofflocationid": 1,
            "dropoffdate": "30/10/2019",
            "dropofftime": "10:00",
            "ageid": 1,
            "vehiclecategoryid": 9,
        },
        "123456",
    )
    print(hmac_sha256(*auto_barn_nz_detail))
