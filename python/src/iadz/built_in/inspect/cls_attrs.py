# -*- coding: utf-8 -*-
from enum import Enum

from sqlalchemy import String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy_utils import ChoiceType


Base = declarative_base()


def wrap_enum(attr, value):
    """Try to wrap enum types

    Works with `sqlalchemy_utils.types.choice.ChoiceType` if the choices are
    represented as Python's built-in Enum. Note that this does NOT wrap
    built-in enum column types of newer version of SQLAlchemy (yet).
    """
    column_type = attr.columns[0].type
    if hasattr(column_type, "choices") and issubclass(
        type(column_type.choices[0]), Enum
    ):
        return type(column_type.choices[0])(value)
    return value


class City(Base):
    class Statuses(Enum):
        published = "published"
        unpublished = "unpublished"

    __tablename__ = "cities"
    slug = Column(String(length=100), primary_key=True)
    status = Column(ChoiceType(Statuses, impl=String(32)), nullable=True)

    @classmethod
    def from_dict(cls, data):
        """Return model instance created out of passed dictionary

        Keys not representing model fields are omitted. Override this factory
        method for customisation.
        """
        attrs = inspect(cls).mapper.attrs
        return cls(
            **{
                key: wrap_enum(attrs[key], value)
                for key, value in data.items()
                if key in attrs
            }
        )


if __name__ == "__main__":

    city = City.from_dict({"slug": "david", "status": "published"})

    print(city.status)
