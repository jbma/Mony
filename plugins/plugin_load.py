#!/usr/bin/env python
# coding: utf-8
import os

from plugins import MonyPlugin


class MonyLoad(MonyPlugin):

    def __init__(self):
        MonyPlugin.__init__(self)

    def getLoadAverage(self):
        return os.getloadavg()[0]

    def process(self):
        data = {
            self.getPluginName(): {
                "load_average": self.getLoadAverage()}
        }
        return data
