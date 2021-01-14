# -*- coding: utf-8 -*-
import json
from elasticsearch_dsl.aggs import A

from elasticsearch_dsl.query import Q

from es_fields import create_search, create_connection


if __name__ == "__main__":

    client = create_connection()

    s = create_search()

    a = A("terms", field="category")
    s.aggs.bucket("category_terms", a)

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
