# -*- coding: utf-8 -*-
import json

from iadz.third_party.elasticsearch.es_fields import create_connection, create_search


if __name__ == "__main__":

    client = create_connection()

    limit_fields = {"includes": ["title", "category"], "excludes": ["comments"]}

    s = create_search(source=limit_fields)

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
