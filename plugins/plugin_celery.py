#!/usr/bin/env python
# coding: utf-8

from plugins import MonyPlugin
from plugin_redis import MonyRedis


class MonyCelery(MonyPlugin, MonyRedis):

    def __init__(self):
        MonyPlugin.__init__(self)
        MonyRedis.__init__(self, db=2)

    def getPendingTasks(self):
        return self.r.llen('celery')

    def process(self):
        data = {
            self.getPluginName(): {
                "pending_taks": self.getPendingTasks()}
        }
        return data
