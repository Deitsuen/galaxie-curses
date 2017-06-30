#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

class EventBusClient:
    def __init__(self):
        self.event_handlers = dict()
        self.children = list()

    def subscribe(self, event_signal, event_handler):
        if event_signal not in self.event_handlers:
            self.event_handlers[event_signal] = list()

        self.event_handlers[event_signal].append(event_handler)

    def unsubscribe(self, event_signal, event_handler):
        if event_signal in self.event_handlers:
            self.event_handlers[event_signal].remove(event_handler)

    def handle_and_dispatch_event(self, event_signal, args=None):
        if args is None:
            args = []
        if event_signal in self.event_handlers:
            for handler in self.event_handlers[event_signal]:
                handler(self, event_signal, args)

        for children in self.children:
            children['WIDGET'].handle_and_dispatch_event(event_signal, args)