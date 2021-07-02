# -*- coding: utf-8 -*-
import json
from datetime import datetime

from elasticsearch_dsl import (
    Document,
    Date,
    Nested,
    Boolean,
    analyzer,
    InnerDoc,
    Completion,
    Text,
    connections,
    Index,
    Float,
)
from elasticsearch_dsl.document import MetaField
from elasticsearch_dsl.field import Keyword
from elasticsearch_dsl.query import Q
from elasticsearch_dsl.search import Search

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


INDEX = "blog"


class Comment(InnerDoc):

    author = Text()
    content = Text()
    created_at = Date()
    price_min = Float()
    price_max = Float()

    def age(self):
        return datetime.now() - self.created_at


class Post(Document):
    class Meta:
        dynamic = MetaField("strict")

    title = Text()
    title_suggest = Completion()
    published = Boolean()
    category = Keyword()
    comments = Nested(Comment)

    created_at = Date()

    def add_comment(self, author, content):
        self.comments.append(
            Comment(author=author, content=content, created_at=datetime.now())
        )

    def save(self, **kwargs):
        self.created_at = datetime.now()
        return super().save(**kwargs)


def create_connection():
    """
    Initate a global elasticsearch connection.
    """
    client = connections.create_connection(hosts=["localhost"], timeout=10)
    return client


def create_post_index():
    """
    Create a new Index post and select Post as document.
    """
    post_index = Index(INDEX)

    if post_index.exists():
        return post_index

    post_index.settings(number_of_shards=1, number_of_replicas=0)
    post_index.document(Post)

    post_index.create()

    return post_index


def create_search(
    must: list = None,
    should: list = None,
    filter_: list = None,
    must_not: list = None,
    source: dict = None,
    sort=None,
) -> Search:
    """
    Search index by construct query.

    Kwargs:
        must: list of the must satisfied query
        should: list of the should satisfied query
        sort: sort statement

    Return:
        Search object.
    """
    s = Search(index=INDEX)

    match_all = Q("match_all")

    must = must + [match_all] if must else [match_all]
    should = should if should else []
    filter_ = filter_ if filter_ else []
    must_not = must_not if must_not else []

    s = s.query("bool", must=must, should=should, filter=filter_, must_not=must_not)

    if sort:
        s = s.sort(sort)

    if source:
        s = s.source(**source)

    print(f"Query: {json.dumps(s.to_dict())}")

    return s


if __name__ == "__main__":
    client = create_connection()
    create_post_index()
