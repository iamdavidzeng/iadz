# -*- coding: utf-8 -*-

import hashlib
import json

foo = {
    "installment_plans": [
        {
            "id": 1,
            "description": "1st installment",
            "amount": 100,
        },
        {"id": 2, "description": "2nd installment", "amount": 1000},
    ]
}


hash_value = hashlib.md5(json.dumps(foo).encode("utf-8")).hexdigest()

print(hash_value)
