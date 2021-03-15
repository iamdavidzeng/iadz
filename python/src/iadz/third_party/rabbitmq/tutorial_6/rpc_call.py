# -*- coding: utf-8 -*-

import uuid
import json

import pika


class RpcProxy(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost"),
        )
        self.routing_key = str(uuid.uuid4())
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(
            "rpc.reply-proxy-%s" % self.routing_key, auto_delete=True
        )
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def on_response(self, ch, method, props, body):
        if props.correlation_id == self.correlation_id:
            self.response = body

    def call(self, server, mehtod, *args, **kwargs):
        self.response = None
        self.correlation_id = str(uuid.uuid4())

        payload = {"args": [], "kwargs": {}}

        payload["args"].extend(args)
        payload["kwargs"].update(kwargs)

        self.channel.queue_bind(
            exchange="nameko-rpc",
            queue=self.callback_queue,
            routing_key=self.routing_key,
        )

        self.channel.basic_publish(
            exchange="nameko-rpc",
            routing_key="%s.%s" % (server, mehtod),
            properties=pika.BasicProperties(
                reply_to=self.routing_key,
                correlation_id=self.correlation_id,
                content_encoding="utf-8",
                content_type="application/json",
                priority=0,
                delivery_mode=2,
            ),
            body=json.dumps(payload),
        )
        while self.response is None:
            self.connection.process_data_events()
        return json.loads(self.response)


rpc = RpcProxy()

print("requesting.......")
response = rpc.call(
    "bookings", "get_student", **{"email_address": "david.zengzz@student.com"}
)
print("response: %s" % response)
