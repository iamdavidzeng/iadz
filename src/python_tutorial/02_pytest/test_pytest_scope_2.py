# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="class")
def fixture1():
    print("\ni am the first fixture")
    yield "iamdavidzeng"


class TestCase1:
    def test_case_1(self, fixture1):
        assert fixture1 == "iamdavidzeng"

    def test_case_2(self, fixture1):
        assert fixture1 == "iamdavidzeng"


if __name__ == "__main__":
    pytest.main(["-s", "test_pytest_scope_2.py"])
