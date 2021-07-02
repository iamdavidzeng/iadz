# -*- coding: utf-8 -*-

import json
from elasticsearch_dsl.query import Q
from elasticsearch_dsl.search import Search

from iadz.third_party.elasticsearch.es_fields import create_connection, create_search


def create_sort() -> Search:
    """
    Apply sort for Search object.

    Return:
        Search object
    """
    must_query = Q("term", published=False)

    s = create_search(must=[must_query], sort={"_score": {"order": "desc"}})

    return s


if __name__ == "__main__":

    create_connection()

    s = create_sort()

    response = s.execute()

    print(f"Response: {json.dumps(response.to_dict())}")
