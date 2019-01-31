# -*- coding: utf-8 -*-


import json

def test_will_return_expected_value(make_request):
    headers = {'User-Agent': 'Mozilla'}
    data = {'name': 'david', 'gender': 'male'}

    result = make_request(data, headers).json()

    assert result == json.dumps(data).encode('utf-8')
