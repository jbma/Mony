#!/usr/bin/env python
# coding: utf-8
from core import settings

"""
Base Class for all transporters
"""
class MonyTransport():

    def __init__(self):
        self.transport_name = self.__class__.__module__
        self.host = settings.HOST
        self.port = settings.PORT


    def getTransportName(self):
        return self.transport_name

