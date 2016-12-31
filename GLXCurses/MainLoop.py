#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
from curses import ascii
import logging


class MainLoop:
    def __init__(self, app):
        self.event_buffer = list()
        self.application = app
        self.started = False

    def set_event_buffer(self, list):
        self.event_buffer = list

    def get_event_buffer(self):
        return self.event_buffer

    def set_application(self, application):
        self.application = application

    def get_application(self):
        return self.application

    def set_started(self, boolean):
        self.started = bool(boolean)

    def get_started(self):
        return self.started

    def start(self):
        self.set_started(True)
        logging.info('Starting ' + self.__class__.__name__)
        self._run()

    def stop(self):
        self.set_started(False)
        logging.info('Stopping ' + self.__class__.__name__)

    def emit(self, detailed_signal, args=[]):
        logging.debug(self.__class__.__name__ + ': ' + detailed_signal + ' ' + str(args))
        self.get_event_buffer().insert(0, [detailed_signal, args])

    def handle_curses_input(self, input_event):
        if input_event == curses.KEY_MOUSE:
            self.emit('MOUSE_EVENT', curses.getmouse())
        elif input_event == curses.KEY_RESIZE:
            self.emit('RESIZE', [])
        else:
            self.emit('CURSES', input_event)

    # Internal
    def _pop_last_event(self):
        try:
            if len(self.get_event_buffer()) > 0:
                return self.get_event_buffer().pop()
        except IndexError:
            pass

    def _handle_event(self):
        try:
            event = self._pop_last_event()
            while event:
                self.get_application().dispatch(event[0], event[1])
                event = self._pop_last_event()
            return True
        except:
            return False

    def _run(self):
        if self.get_started():
            logging.debug(self.__class__.__name__ + ': Started')
            self.get_application().refresh()

        # Main while 1
        while self.get_started():
            # logging.debug(self.__class__.__name__ + ': Waiting event\'s')
            input_event = self.get_application().getch()

            if input_event != -1:
                self.handle_curses_input(input_event)

            if self._handle_event():
                self.get_application().refresh()

        self.get_application().close()
