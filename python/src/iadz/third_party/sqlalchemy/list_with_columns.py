# -*- coding: utf-8 -*-


from iadz.third_party.sqlalchemy.models import session, Storage, Foo, Baz

if __name__ == "__main__":
    storage = Storage(session, Foo)

    query = storage.query.outerjoin(Foo.bazs).with_entities(Foo.id, Baz.slug)

    print(query.all())
