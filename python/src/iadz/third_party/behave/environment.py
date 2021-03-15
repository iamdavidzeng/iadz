# -*- coding: utf-8 -*-
from nameko.cli.utils.config import setup_config
from nameko.standalone.rpc import ClusterRpcProxy


def before_all(context):
    with open("./config.yaml") as fp:
        config = setup_config(fp)
    config.update(context.config.userdata)
    context.config.userdata = config


def before_feature(context, feature):
    if "AMQP_URI" not in context.config.userdata:
        context.config.userdata["AMQP_URI"] = "amqp://guest:guest@localhost:5672/"
    context.cluster_rpc_proxy = ClusterRpcProxy(context.config.userdata)
    context.rpc = context.cluster_rpc_proxy.start()


def after_feature(context, feature):
    context.cluster_rpc_proxy.stop()
