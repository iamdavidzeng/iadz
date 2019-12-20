# -*- coding: utf-8 -*-

from decimal import Decimal

import pytest

from convert_dict_to_str import encode_line_items, decode_line_items



class TestEncode:

    @pytest.fixture
    def setup_line_items(self):
        return [
            {"description": "first_payment", "amount": Decimal(100), "processing": True},
            {"description": "second_payment", "amount": Decimal(200), "processing": True},
            {"description": "third_payment", "amount": Decimal(300), "processing": False},
        ]

    def test_encode_line_items(self, setup_line_items):

        result = encode_line_items(setup_line_items)

        assert result == "first_payment,100,True\r\nsecond_payment,200,True\r\nthird_payment,300,False\r\n"


class TestDecode:

    @pytest.fixture
    def setup_line_items(self):
        return "first_payment,300,True\r\nsecond_payment,100,True\r\nthird_payment,1,False\r\n"

    def test_decode_line_items(self, setup_line_items):

        result = decode_line_items(setup_line_items)

        assert result == [
            {"description": "first_payment", "amount": Decimal(300), "processing": True},
            {"description": "second_payment", "amount": Decimal(100), "processing": True},
            {"description": "third_payment", "amount": Decimal(1), "processing": False},
        ]