#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import logging


class MainLoop:

    def __init__(self, app):
        self.event_buffer = list()
        self.app = app
        self.started = False

    def _pop_last_event(self):
        try:
            if len(self.event_buffer) > 0:
                return self.event_buffer.pop()
        except IndexError:
            pass

    def emit(self, detailed_signal, args=[]):
        logging.debug('>>EMIT>>'+detailed_signal+' '+str(args))
        self.event_buffer.insert(0, [detailed_signal, args])

    def start(self):
        self.started = True
        self._run()

    def stop(self):
        self.started = False

    def _handle_event(self):
        try:
            event = self._pop_last_event()
            while event:
                self.app.dispatch(event[0], event[1])
                event = self._pop_last_event()
            return True
        except:
            return False

    def handle_curses_input(self, input_event):
        if input_event == curses.KEY_MOUSE:
            self.emit('MOUSE_EVENT', curses.getmouse())
        elif input_event == curses.KEY_RESIZE:
            self.emit('RESIZE')
        else:
            self.emit('CURSES', input_event)

    def _run(self):
        self.app.refresh()
        while self.started:
            input_event = self.app.getch()

            if input_event != -1:
                self.handle_curses_input(input_event)

            if self._handle_event() or input_event != -1 or input_event == curses.KEY_RESIZE:
                self.app.refresh()

            if input_event == curses.KEY_F10 or input_event == ord("q"):
                break

        self.app.close()
