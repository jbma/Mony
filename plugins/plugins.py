#!/usr/bin/env python
# coding: utf-8

"""
Base Class for all plugins
"""
class MonyPlugin():

    def __init__(self):
        self.plugin_name = self.__class__.__module__

    def getPluginName(self):
        return self.plugin_name
