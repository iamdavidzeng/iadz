# -*- coding: utf-8 -*-
import json
from elasticsearch_dsl.query import Q

from es_fields import create_connection, create_search


if __name__ == "__main__":

    client = create_connection()

    publish_query = Q("term", **{"published": True})
    comment_query = Q(
        "nested",
        path="comments",
        query=Q("bool", must=[Q("term", **{"comments.author": "iamdavidzeng"})]),
    )

    s = create_search(must=[publish_query, comment_query])

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
