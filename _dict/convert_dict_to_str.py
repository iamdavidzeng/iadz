# -*- coding: utf-8 -*-

import io
import csv
from decimal import Decimal


noop = lambda value: value
bool_from_str = lambda value: value == "1" or value.lower() == "true"


DICT_MAPPING = (
    ("description", noop, noop),
    ("amount", str, Decimal),
    ("processing", str, bool_from_str),
)


def encode_line_items(line_items):

    def encode_line_item(line_item):
        return [
            encode(line_item.get(key)) for 
            key, encode, decode in DICT_MAPPING
        ]

    fp = io.StringIO()
    writer = csv.writer(fp)
    for line_item in line_items:
        writer.writerow(encode_line_item(line_item))
    output = fp.getvalue()
    fp.close()
    return output


def decode_line_items(line_items):

    def decode_line_item(line_item):
        decoded_line_item = {}
        for i, key, in enumerate(DICT_MAPPING):
            key, encode, decode = key
            if line_item[i] in ("None", ""):
                decoded_line_item[key] = None
            else:
                decoded_line_item[key] = decode(line_item[i])
        return decoded_line_item
    
    fp = io.StringIO(line_items)
    reader = csv.reader(fp)
    output = [decode_line_item(row) for row in reader]
    fp.close()
    return output


