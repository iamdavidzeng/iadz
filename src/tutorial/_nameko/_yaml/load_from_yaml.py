# -*- coding: utf-8 -*-

import yaml

with open("payment_items.yaml") as f:

    data = yaml.unsafe_load(f)
    print(data)
