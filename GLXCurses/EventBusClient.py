#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

from GLXCurses import MainLoop
from GLXCurses import Application


class EventBusClient(object):

    def __init__(self):
        self.event_handlers = dict()
        self.children = list()

    def emit(self, detailed_signal, args=None):
        if args is None:
            args = list()
        MainLoop().emit(detailed_signal, args)

    def connect(self, signal, handler, args=None):

        if args is None:
            args = list()

        if signal not in self._get_signal_handlers():
            self._get_signal_handlers()[signal] = list()

        self._get_signal_handlers()[signal].append(handler)

        if args:
            self._get_signal_handlers()[signal].append(args)

    def disconnect(self, signal, handler):

        if signal in self._get_signal_handlers():
            self._get_signal_handlers()[signal].remove(handler)

    def dispatch(self, signal, args=None):

        if args is None:
            args = []

        if signal in self._get_signal_handlers():
            for handler in self._get_signal_handlers()[signal]:
                handler(self, signal, args)

        for children in self.children:
            children['WIDGET'].dispatch(signal, args)

    def _get_signal_handlers(self):
        # return Application().event_handlers
        return self.event_handlers
