# -*- coding: utf-8 -*-


from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


search = Search(using=Elasticsearch("localhost:9201"), index="property")


if __name__ == "__main__":
    print(search.execute().to_dict())
