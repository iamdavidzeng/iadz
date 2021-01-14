# -*- coding: utf-8 -*-
import json

from elasticsearch_dsl.query import Q

from es_fields import create_search, create_connection


if __name__ == "__main__":

    client = create_connection()

    publish_query = Q("term", **{"published": True})

    s = create_search(filter_=[publish_query])

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
