# -*- coding: utf-8 -*-

import pytest
from mock import Mock, call
from marshmallow import Schema, fields

# service
class ModelX:
    name = None
    slug = None

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug


class SchemaX(Schema):
    name = fields.String()
    slug = fields.String()


class ServiceX:

    method_y = Mock()

    def method_x(self, data):
        data = SchemaX().load(data)
        result = self.method_y(data)
        return SchemaX().dump(result)


# testing
@pytest.fixture
def make_data():
    def _make(**overrides):
        data = {
            "name": "name",
            "slug": "slug",
        }
        data.update(**overrides)
        return data

    return _make


@pytest.fixture
def setup_data(make_data):
    def _setup(**overrides):
        instance = ModelX(**make_data(**overrides))
        # insert to db(not suggested here).
        return instance

    return _setup


class TestServiceX:
    @pytest.fixture
    def service(self):
        return ServiceX()

    def test_method_x(self, service, make_data, setup_data):
        instace = setup_data(name="foo", slug="foo")
        service.method_y.return_value = instace

        data = make_data(name="foo", slug="foo")
        result = service.method_x(data)

        assert result == {"name": "foo", "slug": "foo"}
        assert service.method_y.call_args == call(data)
