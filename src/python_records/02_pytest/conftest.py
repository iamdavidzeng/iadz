# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="session")
def fixture1():
    print("\ni am the first fixture")
    yield "iamdavidzeng"
