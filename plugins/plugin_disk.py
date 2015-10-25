#!/usr/bin/env python
# coding: utf-8
import psutil

from plugins import MonyPlugin


class MonyDisk(MonyPlugin):

    def __init__(self):
        MonyPlugin.__init__(self)

    def getUsedDisk(self):
        return psutil.disk_usage('/')[-1]

    def process(self):
        data = {
            self.getPluginName(): {
                "percent_disk_used": self.getUsedDisk()}
        }
        return data
