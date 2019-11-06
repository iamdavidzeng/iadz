# -*- coding: utf-8 -*-


from graphene import relay, ObjectType, Schema
from graphene_sqlalchemy import (
    SQLAlchemyConnectionField, SQLAlchemyObjectType
)

from models import (
    Department as DepartmentModel,
    Employee as EmployeeModel
)


class Department(SQLAlchemyObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentConnections(relay.Connection):

    class Meta:
        node = Department


class Employee(SQLAlchemyObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class EmployeeConnections(relay.Connection):

    class Meta:
        node = Employee


class Query(ObjectType):

    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(EmployeeConnections)
    all_departments = SQLAlchemyConnectionField(DepartmentConnections, sort=None)


schema = Schema(query=Query)
