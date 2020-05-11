# -*- coding: utf-8 -*-
from enum import Enum

from sqlalchemy import Column, String, Integer, case, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType


class Category(Enum):

    PUBLIC = "public"
    PRIVATE = "private"
    PREMIUM = "premium"


SORTER_MAPPING = {
    Category.PREMIUM.value: 1,
    Category.PRIVATE.value: 2,
    Category.PUBLIC.value: 3,
}


DeclarativeBase = declarative_base()


class ProductInfo(DeclarativeBase):

    __tablename__ = "product_info"

    id = Column(Integer, primary_key=True)
    category = Column(ChoiceType(Category, impl=String(16)))


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/demo")
    DeclarativeBase.metadata.create_all(engine)
    connection = engine.connect()
    DeclarativeBase.metadata.bind = engine
    Session = sessionmaker(bind=connection)

    session = Session()
    for product in [
        ProductInfo(id=1, category=Category.PRIVATE),
        ProductInfo(id=2, category=Category.PUBLIC),
        ProductInfo(id=3, category=Category.PREMIUM),
    ]:
        session.add(product)

    sorter = case(value=ProductInfo.category, whens=SORTER_MAPPING)
    query = session.query(ProductInfo)

    result1 = query.all()
    result2 = query.order_by(sorter.asc()).all()


    print([product.id for product in result1])
    print([product.id for product in result2])


    session.close()
    DeclarativeBase.metadata.drop_all()
