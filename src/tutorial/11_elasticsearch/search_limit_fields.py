# -*- coding: utf-8 -*-
import json

from elasticsearch_dsl.query import Q

from es_fields import create_search, create_connection


if __name__ == "__main__":

    client = create_connection()

    limit_fields = {"includes": ["title", "category"], "excludes": ["comments"]}

    s = create_search(source=limit_fields)

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
