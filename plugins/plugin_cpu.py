#!/usr/bin/env python
# coding: utf-8
import psutil

from plugins import MonyPlugin


class MonyCpu(MonyPlugin):

    def __init__(self):
        MonyPlugin.__init__(self)

    def getCpuStat(self, interval=3):
        return psutil.cpu_percent(interval=interval)

    def process(self):
        data = {
            self.getPluginName(): {
                "percent_cpu_used": self.getCpuStat()}
        }
        return data
