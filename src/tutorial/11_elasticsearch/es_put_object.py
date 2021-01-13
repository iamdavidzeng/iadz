# -*- coding: utf-8 -*-

from es_fields import create_connection, Post, INDEX


if __name__ == "__main__":
    client = create_connection()
    post = {
        "title": "foo",
        "title_suggest": "foo",
        "published": False,
        "category": "bar",
        "comments": [
            {
                "author": "david",
                "content": "baz",
            }
        ],
    }
    posts = [
        {
            "title": "foo_1",
            "title_suggest": "foo_1",
            "published": False,
            "category": "bar_1",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "baz_1",
                }
            ],
        },
        {
            "title": "foo_2",
            "title_suggest": "foo_2",
            "published": True,
            "category": "bar_1",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "baz_2",
                }
            ],
        },
        {
            "title": "foo_3",
            "title_suggest": "foo_3",
            "published": False,
            "category": "bar_1",
            "comments": [
                {
                    "author": "iamdavidzeng",
                    "content": "baz_3",
                }
            ],
        },
    ]

    for id_, post in enumerate(posts):
        Post(**post, meta={"id": id_}).save(index=INDEX)
