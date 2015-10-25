#!/usr/bin/env python
# coding: utf-8
import importlib

import settings

class Mony():

    def getPluginsEnabled(self):
        data = list()

        for plugin in settings.ACTIVATED_PLUGINS:
            data.append(plugin)
        return data

    def getDataFromPlugins(self):

        data = dict()

        for plugin in settings.ACTIVATED_PLUGINS:
            __import__('plugins.plugin_' + plugin)
            module = importlib.import_module('plugins.plugin_' + plugin)
            plugin_class = getattr(module, 'Mony' + plugin.title())
            instance = plugin_class()
            data.update(instance.process())

        return data

    def getTransportEnabled(self):
        return settings.TRANSPORT


    def sendData(self):
        transport_enabled = self.getTransportEnabled()
        __import__('transports.transport_' + transport_enabled)
        module = importlib.import_module('transports.transport_' + transport_enabled)
        transport_class = getattr(module, 'Mony' + transport_enabled.title())
        instance = transport_class()
        data = self.getDataFromPlugins()
        return instance.send(data)


