# -*- coding: utf-8 -*-


import json

import requests

CITY_NAMES = [
    "london",
    "manchester",
    "coventry",
    "nottingham",
    "sydney",
    "new-york-city",
    "montreal",
    "paris",
    "singapore",
    "melbourne",
]

# stage
ELASTICSEARCH_SEARCH_URL = "http://10.20.2.10:8200/autocomplete/doc/_search"

# prod
# ELASTICSEARCH_SEARCH_URL = "http://10.20.2.10:8201/autocomplete/doc/_search"

# stage
ELASTICSEARCH_UPDATE_URL = "http://10.20.2.10:8200/autocomplete/doc/{}/_update"

# prod
# ELASTICSEARCH_UPDATE_URL = "http://10.20.2.10:8201/autocomplete/doc/{}/_update"


def update_city_autocomplete():

    for city_name in CITY_NAMES:

        # 构造query通过slug查询city
        city_query = {"query": {"bool": {"must": {"term": {"slug": city_name}}}}}

        response = requests.get(ELASTICSEARCH_SEARCH_URL, json=city_query)
        result = response.json()

        autocomplete_lst = result["hits"]["hits"]

        if not autocomplete_lst:
            print(f"Autocomplete[{city_name}] Not Found.")
            continue

        autocomplete_obj = autocomplete_lst[0]
        autocomplete_id = autocomplete_obj["_id"]
        autocomplete_data = autocomplete_obj["_source"]["autocomplete"]

        # 给autocomplete添加重复值
        for translation, common_names in autocomplete_data.items():
            autocomplete_data[translation] += [common_names[0]] * 4

        update_data = {"doc": {"autocomplete": autocomplete_data}}

        # 发送请求更新city的autocomplete值
        response = requests.post(
            ELASTICSEARCH_UPDATE_URL.format(autocomplete_id), json=update_data
        )

        print(f"Autocomplete[{city_name}]:\n {update_data}")
        print(f"Get Elasticsearch Response: {response.json()}")


if __name__ == "__main__":
    update_city_autocomplete()
