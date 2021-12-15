# -*- coding: utf-8 -*-

import pytest
from mock import call, Mock
from marshmallow import Schema, fields  # 使用的是最新版本的，所以语法有变化
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
        # 验证输入值
        data = SchemaX().load(data).data
        # 调用依赖处理逻辑
        result = self.service_y.method_y(data)
        # 调用复杂函数
        self.complicated_method(data["name"], data["slug"])
        # 调用辅助函数
        self.simple_helper_method(data["name"], data["slug"])
        # 序列化返回结果
        return SchemaX().dump(result).data

    @rpc
    def complicated_method(self, args1, args2):
        # 作为一个单独的业务功能单元，包含复杂的业务逻辑
        # 容易随着业务改变发生变化
        pass

    def simple_helper_method(self, args1, args2):
        # 作为一个辅助函数被创建，简单的计算逻辑
        pass


# testing
@pytest.fixture
def db_session():
    # 使用本地测试数据库，模拟数据库连接
    return Mock()


@pytest.fixture
def storage(db_session):
    return Mock()


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
def setup_data(db_session, make_data):
    def _setup(**overrides):
        instance = ModelX(**make_data(**overrides))
        # 理想情况：
        #   往数据库插入数据等操作，但是不建议在单元测试当中这样做，
        #   因为单元测试只会关注一个单元的逻辑，数据库操作不应该被考虑进来，
        #   而是应该有专门的封装的数据库操作单元测试。

        # 更新：
        #   为了方便开发去完成测试，在对测试速度影响不大的情况下，
        #   我们在单元测试当中使用真实数据库连接来模拟数据库操作，
        #   不然每一次的storage模拟对于单元测试编写效率影响太大了。
        db_session.add(instance)
        db_session.commit()
        return instance

    return _setup


@pytest.fixture
def service_x(db_session, storage):
    service = worker_factory(ServiceX)
    service.db_session = db_session
    service.storage = storage
    return service


class TestServiceX:
    @pytest.fixture
    def service(self, service_x):
        return service_x

    def test_method_x(self, service, make_data, setup_data):
        instace = setup_data(name="foo", slug="foo")
        # 对于外部依赖会使用Mock来模拟，这样可以更好的模拟外部依赖的行为
        service.service_y.method_y.return_value = instace
        # 对于复杂的业务逻辑单元，使用Mock模拟，入参和出参不变的情况下，
        # 对被调用逻辑单元内部的逻辑不关心，由它自己维护。
        service.complicated_method = Mock(return_value=[])

        data = make_data(name="foo", slug="foo")
        result = service.method_x(data)

        # 断言返回结果
        assert result == {"name": "foo", "slug": "foo"}
        # 断言外部依赖的调用参数
        assert service.service_y.method_y.call_args == call(data)
        # 断言内部复杂逻辑单元的入参符合预期
        assert service.complicated_method.call_args == call("foo", "foo")
        # 不再断言辅助函数，因为辅助函数大概率不会随着业务发生改变
