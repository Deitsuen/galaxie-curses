#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses


class EventBus(object):
    def __init__(self):
        self.event_handlers = dict()

    @staticmethod
    def adopt(orphan):
        """
        not implemented yesr
        :param orphan: a poor widget orphan
        """
        pass

    @staticmethod
    def emit(detailed_signal, args=None):
        if args is None:
            args = list()
        GLXCurses.mainloop.emit(detailed_signal, args)

    def connect(self, detailed_signal, handler, args=None):
        if args is None:
            args = list()

        # check if it's all ready connect if not create it
        if detailed_signal not in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal] = list()

        self._get_signal_handlers_dict()[detailed_signal].append(handler)

        if args:
            self._get_signal_handlers_dict()[detailed_signal].append(args)

            # Test about EventBus
            # GLXCurses.signal.connect(detailed_signal, handler, args)

    def disconnect(self, detailed_signal, handler):

        if detailed_signal in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal].remove(handler)

    def dispatch(self, detailed_signal, args=None):
        if args is None:
            args = []

        if detailed_signal in self._get_signal_handlers_dict():
            for handler in self._get_signal_handlers_dict()[detailed_signal]:
                handler(self, detailed_signal, args)

        if self.get_active_window():
            self.get_active_window().handle_and_dispatch_event(detailed_signal, args)

    def _get_signal_handlers_dict(self):
        return self.event_handlers

