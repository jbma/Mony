#!/usr/bin/env python
# coding: utf-8
import psutil

from plugins import MonyPlugin


class MonyMemory(MonyPlugin):

    def __init__(self):
        MonyPlugin.__init__(self)

    def getUsedMemory(self):
        return psutil.virtual_memory()[2]

    def process(self):
        data = {
            self.getPluginName(): {
                "percent_memory_used": self.getUsedMemory()}
        }
        return data
