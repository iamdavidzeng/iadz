# -*- coding: utf-8 -*-

from es_fields import create_connection, Post, INDEX


if __name__ == "__main__":
    client = create_connection()
    posts = [
        {
            "title": "foo",
            "title_suggest": "foo",
            "published": False,
            "category": "foo",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "foo",
                }
            ],
        },
        {
            "title": "bar",
            "title_suggest": "bar",
            "published": True,
            "category": "bar",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "bar",
                }
            ],
        },
        {
            "title": "baz",
            "title_suggest": "baz",
            "published": False,
            "category": "baz",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "baz",
                }
            ],
        },
    ]

    for id_, post in enumerate(posts):
        Post(**post, meta={"id": id_}).save(index=INDEX)
