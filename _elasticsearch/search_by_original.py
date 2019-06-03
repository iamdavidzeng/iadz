# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


client = Elasticsearch()

response = client.search(
    index="en-us",
    body={
        "query": {
            "bool": {
                "must": [
                    {"match_all": {}},
                ],
                "filter": [
                    {"term": {"slug": "iq-shoreditch"}},
                ]
            }
        }
    }
)

for hit in response["hits"]["hits"]:
    print(hit["_score"], hit["_source"])
