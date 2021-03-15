# -*- coding: utf-8 -*-

from nameko.timer import timer


class AlertService:

    name = "platform_alert"

    @timer(interval=1)
    def ping(self):
        print("pong")
