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

    def connect(self, detailed_signal, handler, args=None):
        """
        The connect() method adds a function or method (handler) to the end of the event list
        for the named detailed_signal but before the default class signal handler.
        An optional set of parameters may be specified after the handler parameter.
        These will all be passed to the signal handler when invoked.

        :param detailed_signal: a string containing the signal name
        :type detailed_signal: str
        :param handler: a function handler
        :type handler: handler
        :param args: additional parameters arg1, arg2
        :type args: list
         """

        # If args is still None replace it by a empty list
        if args is None:
            args = list()

        # If detailed_signal is not in the event list create it
        if detailed_signal not in self.get_events_list():
            self.get_events_list()[detailed_signal] = list()

        self.get_events_list()[detailed_signal].append(handler)

        if args:
            self.get_events_list()[detailed_signal].append(args)

    def disconnect(self, detailed_signal, handler):
        """
        The disconnect() method removes the signal handler with the specified handler
        from the list of signal handlers for the object.

        :param detailed_signal: a string containing the signal name
        :type detailed_signal: str
        :param handler: a function handler
        :type handler: handler
        """
        if detailed_signal in self.get_events_list():
            self.get_events_list()[detailed_signal].remove(handler)

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
