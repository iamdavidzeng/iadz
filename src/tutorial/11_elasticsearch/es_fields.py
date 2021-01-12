# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch_dsl import (
    Document,
    Date,
    Nested,
    Boolean,
    analyzer,
    InnerDoc,
    Completion,
    Keyword,
    Text,
    connections,
    Index,
)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


class Comment(InnerDoc):

    author = Text()
    content = Text()
    created_at = Date()

    def age(self):
        return datetime.now() - self.created_at


class Post(Document):
    title = Text()
    title_suggest = Completion()
    published = Boolean()
    category = Text()
    comments = Nested(Comment)

    created_at = Date()

    def add_comment(self, author, content):
        self.comments.append(
            Comment(author=author, content=content, created_at=datetime.now())
        )

    def save(self, **kwargs):
        self.created_at = datetime.now()
        return super().save()


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
    post_index = Index("post")

    if post_index.exists():
        return post_index

    post_index.document(Post)

    post_index.create()

    return post_index


if __name__ == "__main__":
    client = create_connection()
    create_post_index()
