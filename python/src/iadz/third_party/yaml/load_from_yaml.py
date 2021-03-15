# -*- coding: utf-8 -*-

import yaml


def load_from_yaml(path):

    with open(path) as stream:
        result = yaml.unsafe_load(stream)

    return result


if __name__ == "__main__":
    path = "demo.yaml"
    result = load_from_yaml(path)

    for key, value in result.items():
        print(f"{key}: {value}")
