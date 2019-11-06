# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


client = Elasticsearch()

s = Search(using=client, index="en-us") \
    .filter("term", slug="iq-shoreditch")


response = s.execute()

print(response.to_dict())
