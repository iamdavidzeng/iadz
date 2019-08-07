# -*- coding: utf-8 -*-


import json
import pytest

from mock import Mock

@pytest.fixture
def make_request():
    def make(data, headers=None):

        def json_():
            return json.dumps(data).encode("utf-8")

        headers = headers or {}
        request = Mock(
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            json=json_,
        )
        return request
    return make
