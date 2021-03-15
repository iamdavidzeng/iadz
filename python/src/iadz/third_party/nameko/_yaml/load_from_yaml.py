# -*- coding: utf-8 -*-
import re
import logging
import argparse
from datetime import datetime, timedelta

import yaml
from nameko import config
from nameko.cli.utils.config import setup_yaml_parser
from nameko.standalone.rpc import ClusterRpcClient


MATCHER = r"^[a-z]*now([\+|\-]{1}\d+)d*$"


def setup_parser():

    parser = argparse.ArgumentParser("Create PaymentItems load from yaml.")
    parser.add_argument("-c", "--config", help="config file to use", type=str)
    parser.add_argument("-l", "--load-from", help="yaml file to use", type=str)
    return parser


def get_config(config_path):
    with open(config_path, "r") as stream:
        return yaml.unsafe_load(stream.read())


def get_payment_items(yaml_path):
    with open(yaml_path, "r") as stream:
        result = yaml.unsafe_load(stream.read())

    payment_items = result["payment_items"]
    payments = result["payments"]

    print(payments)

    for payment_item in payment_items:
        due_datetime = payment_item["due_datetime"]
        invoice_datetime = payment_item["invoice_datetime"]

        if not due_datetime:
            pass
        else:
            match_obj = re.search(MATCHER, due_datetime)
            if match_obj:
                days = int(match_obj.groups()[0])
                due_datetime = datetime.utcnow() + timedelta(days=days)
            else:
                due_datetime = datetime.utcnow()
            payment_item.update(due_datetime=due_datetime.isoformat())

        if not invoice_datetime:
            pass
        else:
            match_obj = re.search(MATCHER, invoice_datetime)
            if match_obj:
                days = int(match_obj.groups()[0])
                invoice_datetime = datetime.utcnow() + timedelta(days=days)
            else:
                invoice_datetime = datetime.utcnow()
            payment_item.update(invoice_datetime=invoice_datetime.isoformat())
    return payment_items


if __name__ == "__main__":

    parser = setup_parser()
    args = parser.parse_args()

    override_config = get_config(args.config)
    payment_items = get_payment_items(args.load_from)

    # with config.patch(override_config, clear=True):
    #     with ClusterRpcClient() as proxy:
    #         proxy.billing.create_payment_items(payment_items)
