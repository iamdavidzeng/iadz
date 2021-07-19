# -*- coding: utf-8 -*-

import abc


class AbstractRequestor(metaclass=abc.ABCMeta):

    must_fn = ["get_properties"]

    @classmethod
    def __subclasshook_(cls, subclass):
        for fn in cls.must_fn:
            return (
                hasattr(subclass, fn)
                and callable(getattr(subclass, fn))
                or NotImplemented
            )

    @abc.abstractmethod
    def get_properties(self, **kwargs: dict) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def get_unit_types(self, **kwargs: dict) -> dict:
        raise NotImplementedError


class BaseRequestor(AbstractRequestor):
    def __init__(self, url: str, version: str) -> None:
        self.url = url + version
        super().__init__()

    def get_properties(self, **kwargs: dict) -> dict:

        properties = self.get_request(**kwargs)

        return properties


class StudentSuiteRequestor(BaseRequestor):
    def get_properties(self, **kwargs: dict) -> dict:
        pass


if __name__ == "__main__":
    ss = StudentSuiteRequestor("https://api.project-g66.com", "/v1")

    ss.get_properties()
