# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="module")
def fixture1():
    print("\ni am the first fixture")
    yield "1"


def test_case_1(fixture1):
    assert fixture1 == "1"


class TestCase2:
    def test_case_2(self, fixture1):
        assert fixture1 == "1"


if __name__ == "__main__":
    pytest.main(["-s", "test_scope_3.py"])
