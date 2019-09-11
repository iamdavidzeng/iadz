# -*- coding: utf-8

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

# situation 1:
client = Elasticsearch()

response = client.search(
    inde="my_index",
    body={
        "query": {
            "bool": {
                "must": [{"match": {"title": "python"}}],
                "must_not": [{"match": {"description": "beta"}}],
                "filter": [{"term": {"category": "search"}}],
            }
        },
        "aggs": {
            "per_tag": {
                "terms": {"field": "tags"},
                "aggs": {"max_lines": {"max": {"field": "lines"}}},
            }
        }
    }
)

for hit in response["hits"]["hits"]:
    print(hit["_score"], hit["_source"]["title"])

for tag in response["aggregations"]["per_tag"]["buckets"]:
    print(tag["key"], tag["max_lines"]["value"])


# situation2:
client = Elasticsearch()

s = Search(using=client, index="my_index") \
    .filter("term", category="search") \
    .query("match", title="python") \
    .exclude("match", description="beta")

s.aggs.bucket("per_tag", "terms", field="tags") \
    .metric("max_lines", "max", field="lines")

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

for tag in response.aggregations.per_tag.buckets:
    print(tag.key, tag.max_lines.value)
