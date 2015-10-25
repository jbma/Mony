#!/usr/bin/env python
# coding: utf-8
import redis

from plugins import MonyPlugin


class MonyRedis(MonyPlugin):

    def __init__(self, db=1):
        MonyPlugin.__init__(self)
        self.r = redis.StrictRedis(host='localhost', port=6379, db=db)

    def getRedisStat(self, interval=3):
        return self.r.info()

    def process(self):
        data = {
            self.getPluginName(): {
                "redis_infos": self.getCpuStat()}
        }
        return data
