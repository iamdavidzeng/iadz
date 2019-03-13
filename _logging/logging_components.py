#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@name: logging_components.py
@author: Aeiou
@time: 18-10-7 下午3:50
"""

import logging
import logging.handlers
import datetime


logger = logging.getLogger('tmp_logger')
logger.setLevel(logging.DEBUG)

first_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7,
    atTime=datetime.time(0, 0, 0, 0)
)
first_handler.setFormatter(
    logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
)


second_handler = logging.FileHandler('error.log')
second_handler.setLevel(logging.ERROR)
second_handler.setFormatter(
    logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'
    )
)


if __name__ == '__main__':
    logger.addHandler(first_handler)
    logger.addHandler(second_handler)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
