# -*- coding: utf-8 -*-

import pytest
from mock import call
from marshmallow import Schema, fields # 使用的是最新版本的，所以语法有变化
from nameko.rpc import ServiceRpc, rpc
from nameko.testing.services import worker_factory

# model
class ModelX:
    name = None
    slug = None

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug


# schema
class SchemaX(Schema):
    name = fields.String()
    slug = fields.String()


# service
class ServiceX:

    service_y = ServiceRpc("service_y")

    @rpc
    def method_x(self, data):
        // 验证输入值
        data = SchemaX().load(data)
        // 调用依赖处理逻辑
        result = self.service_y.method_y(data)
        // 序列化返回结果
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
        # 往数据库插入数据等操作，但是不建议在单元测试当中这样做，
        # 因为单元测试只会关注一个单元的逻辑，数据库操作不应该被考虑进来，
        # 而是应该有专门的封装的数据库操作单元测试。
        return instance

    return _setup


@pytest.fixture
def service_x():
    return worker_factory(ServiceX)


class TestServiceX:
    @pytest.fixture
    def service(self, service_x):
        return service_x

    def test_method_x(self, service, make_data, setup_data):
        instace = setup_data(name="foo", slug="foo")
        service.service_y.method_y.return_value = instace

        data = make_data(name="foo", slug="foo")
        result = service.method_x(data)

        # 断言返回结果
        assert result == {"name": "foo", "slug": "foo"}
        # 断言外部依赖的调用参数
        assert service.service_y.method_y.call_args == call(data)
