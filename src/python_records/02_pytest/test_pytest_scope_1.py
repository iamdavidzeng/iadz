# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def first_fixture():
    print("\ni am the first fixture")
    username = "iamdavidzeng"
    yield username


def test_case_1(first_fixture):
    assert first_fixture == "iamdavidzeng"


def test_case_2(first_fixture):
    assert first_fixture == "iamdavidzeng"


if __name__ == "__main__":
    pytest.main(["-s", "test_pytest_scope_1.py"])
