#!/usr/bin/env python
# coding: utf-8
import socket

from plugins import MonyPlugin


class MonyHost(MonyPlugin):

    def __init__(self):
        MonyPlugin.__init__(self)

    def getHostName(self):
        return socket.gethostname()

    def process(self):
        data = {
            self.getPluginName(): {
                "host_name": self.getHostName()}
        }
        return data
