# -*- coding: utf-8 -*-


from iadz.third_party.elasticsearch.es_fields import INDEX, Post, create_connection


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
                    "price_min": 10,
                    "price_max": 100,
                },
                {
                    "author": "iamdavidzeng",
                    "content": "foo",
                    "price_min": 100,
                    "price_max": 200,
                },
                {
                    "author": "iamdavidzeng",
                    "content": "foo",
                    "price_min": 50,
                    "price_max": 100,
                },
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
                    "price_min": 10,
                    "price_max": 100,
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
                    "price_min": 10,
                    "price_max": 100,
                }
            ],
        },
    ]

    for id_, post in enumerate(posts):
        Post(**post, meta={"id": id_ + 1}).save(using=client, index=INDEX)
        print(f"Post: {id_} put into es successfully!")
