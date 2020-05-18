# -*- coding: utf-8 -*-
import logging
import argparse
from datetime import datetime, timedelta

import yaml
from nameko import config
from nameko.cli.utils.config import setup_yaml_parser
from nameko.standalone.rpc import ClusterRpcClient


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

    for payment_item in payment_items:

        import re

        due_datetime = payment_item["due_datetime"]
        invoice_datetime = payment_item["invoice_datetime"]

        if not due_datetime:
            pass
        else:
            days = re.findall(r"\d+", due_datetime)
            days = int(days[0]) if days else 0
            due_datetime = datetime.utcnow() + timedelta(days=days)

            payment_item.update(
                due_datetime=due_datetime.isoformat()
            )
        
        if not invoice_datetime:
            pass
        else:
            days = re.findall(r"\d+", invoice_datetime)
            days = int(days[0]) if days else 0
            invoice_datetime = datetime.utcnow() + timedelta(days=days)

            payment_item.update(
                invoice_datetime=invoice_datetime.isoformat()
            )
    return payment_items


if __name__ == "__main__":


    parser = setup_parser()
    args = parser.parse_args()

    override_config = get_config(args.config)
    payment_items = get_payment_items(args.load_from)

    print(payment_items)

    # with config.patch(override_config, clear=True):
    #     with ClusterRpcClient() as proxy:
    #         proxy.billing.create_payment_items(payment_items)