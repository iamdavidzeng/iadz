# -*- coding: utf-8 -*-


from nameko.rpc import rpc
from nameko.messaging import Publisher
from nameko_amqp_retry.messaging import Consumer as NamekoConsumer
from platform_common.entrypoints.messaging import QueueConsumer
from kombu import Queue, Exchange


COMMUTE_TIME_EXCHANGE_NAME = "commute-time"
EXCHANGE_NAMEKO_RPC_NAME = "nameko-rpc"

ROUTING_KEY_GET_COMMUTE_TIME_NAME = "get_commute_times"
ROUTING_KEY_CONSUME_COMMUTE_TIME_NAME = "ap-southeast-1_commute_times_reply_es5"
ROUTING_KEY_RPC_BACK_NAME = "demo123456"


exchange_commute_times = Exchange(name=COMMUTE_TIME_EXCHANGE_NAME)
exchange_nameko_rpc = Exchange(name=EXCHANGE_NAMEKO_RPC_NAME, type="topic")

queue_get_commute_times = Queue(
    exchange=exchange_commute_times,
    routing_key=ROUTING_KEY_GET_COMMUTE_TIME_NAME,
    name="fed.{}".format(ROUTING_KEY_GET_COMMUTE_TIME_NAME)
)

queue_consume_commute_times = Queue(
    exchange=exchange_commute_times,
    routing_key=ROUTING_KEY_CONSUME_COMMUTE_TIME_NAME,
    name="fed.{}".format(ROUTING_KEY_CONSUME_COMMUTE_TIME_NAME),
)


class Consumer(NamekoConsumer):

    def setup(self):

        self.queue = queue_consume_commute_times
        super(Consumer, self).setup()


def consumer_factory(prefetch_count):

    class MessageConsumer(Consumer):

        queue_consumer = QueueConsumer(prefetch_count)

    return MessageConsumer


def consume_commute_time_reply(prefetch_count, **kwargs):

    cls = consumer_factory(prefetch_count)
    return cls.decorator(queue=None, **kwargs)


class PublishService:

    name = "publish"

    commute_time_publisher = Publisher(
        exchange=exchange_commute_times,
        declare=[queue_consume_commute_times]
    )

    nameko_rpc_publisher = Publisher(
        exchange=exchange_nameko_rpc,
        declare=[]
    )

    @rpc
    def publish_commute_times(self, payload):

        self.commute_time_publisher(
            payload,
            routing_key=ROUTING_KEY_GET_COMMUTE_TIME_NAME,
            reply_to=ROUTING_KEY_CONSUME_COMMUTE_TIME_NAME,
        )

    @consume_commute_time_reply(prefetch_count=1)
    def handle_commute_time_reply(self, payload):

        print(payload)

