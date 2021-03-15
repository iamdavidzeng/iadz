# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Creator(ABC):
    """
    抽象一个创建类，申明工厂方法以及一个行为方法
    """

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        product = self.factory_method()

        result = product.operation()

        return result


class Product(ABC):
    """
    抽象一个产品类，为子类定义行为
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteCreator1(Creator):
    """
    继承创建类，重写工厂方法，根据业务需求返回一个具体的产品类
    """

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    同上
    """

    def factory_method(self):
        return ConcreteProduct2()


class ConcreteProduct1(Product):
    """
    继承产品类，根据业务逻辑重写行为方法
    """

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    """
    同上
    """

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    客户端可以不用关注具体的产品，具体需要使用到的产品可以在外部恐怖，客户端只需要执行行为就可以
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
