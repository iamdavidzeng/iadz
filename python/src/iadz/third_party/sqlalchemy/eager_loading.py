# -*- coding: utf-8 -*-

from iadz.third_party.sqlalchemy.models import session, Storage, Foo, Baz
from sqlalchemy.orm import contains_eager, joinedload, selectinload


class Loader:
    def __init__(self, storage) -> None:
        self.query = storage.query

    def selectinload(self):
        resource = (
            self.query.options(selectinload(Foo.bazs)).filter(Foo.name == "david").one()
        )
        return resource

    def joinedload(self):
        resource = (
            self.query.options(joinedload(Foo.bazs)).filter(Foo.name == "david").one()
        )
        return resource

    def explicit_join_and_eagerload(self):
        resource = (
            self.query.join(Foo.bazs)
            .filter(Foo.name == "david")
            .options(contains_eager(Foo.bazs))
            .one()
        )
        return resource


if __name__ == "__main__":
    storage = Storage(session, Foo)
    loader = Loader(storage)

    foo = loader.selectinload()

    print(foo)

    print(foo.bazs)
