#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses


class EventBusClient(object):

    def __init__(self):
        self.events_list = dict()
        self.children = list()

    def emit(self, detailed_signal, args=None):
        if args is None:
            args = list()
        GLXCurses.mainloop.emit(detailed_signal, args)

    def connect(self, signal, handler, args=None):

        if args is None:
            args = list()

        if signal not in self.get_events_list():
            self.get_events_list()[signal] = list()

        self.get_events_list()[signal].append(handler)

        if args:
            self.get_events_list()[signal].append(args)

    def disconnect(self, signal, handler):

        if signal in self.get_events_list():
            self.get_events_list()[signal].remove(handler)

    def dispatch(self, signal, args=None):

        if args is None:
            args = []

        if signal in self.get_events_list():
            for handler in self.get_events_list()[signal]:
                handler(self, signal, args)

        for children in self.children:
            children['WIDGET'].dispatch(signal, args)

    def get_events_list(self):
        # return Application().event_handlers
        return self.events_list
