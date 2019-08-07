# -*- coding: utf-8 -*-


import os
import yaml
import logging
from logging import config as logger_config


config_file = os.path.join(os.path.dirname(__file__), "config.yaml")

if os.path.exists("mylog"):
    pass
else:
    os.mkdir("mylog")

with open(config_file, "rt") as stream:
    config = yaml.unsafe_load(stream.read())

logger_config.dictConfig(config)
logger = logging.getLogger()


if __name__ == "__main__":
    logger.error("This is a test error message for my first logger.")