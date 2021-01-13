# -*- coding: utf-8 -*-
import json
from elasticsearch_dsl.query import Q

from elasticsearch_dsl.search import Search
from es_fields import create_connection, INDEX

if __name__ == "__main__":

    client = create_connection()

    s = Search(using=client, index=INDEX)

    match_all_query = Q("match_all")
    publish_query = Q("term", **{"published": True})
    comment_query = Q(
        "nested",
        path="comments",
        query=Q("bool", must=[Q("term", **{"comments.author": "iamdavidzeng"})]),
    )

    s = s.query("bool", must=[match_all_query, publish_query, comment_query], should=[])

    print(f"Query: {json.dumps(s.to_dict())}")

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
