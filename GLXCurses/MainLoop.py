#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GLXCurses.MyEventBus import MyEventBus
import curses

class MainLoop():

    def __init__(self, app):
        self.event_bus = MyEventBus()
        self.app = app
        self.started = False

    def start(self):
        self.started = True
        self._run()

    def stop(self):
        self.started = False

    def _handle_events(self):
        try:
            event_signal, event_args = self.event_bus.pop_last_event()
            self.app.dispatch(event_signal, event_args)
        except:
            pass

    def handle_resize(self):
        self.event_bus.emit('RESIZED')

    def handle_mouse(self, input_event):
        if input_event == curses.KEY_MOUSE:
            self.event_bus.emit('MOUSE_EVENT', curses.getmouse())

    def handle_keyboard(self, input_event):
        self.event_bus.emit('KEY_PRESSED', input_event)


    def _run(self):
        self.app.refresh()
        while self.started:
            input_event = self.app.getch()
            self._handle_events()
            self.handle_resize()
            self.handle_keyboard(input_event)
            self.handle_mouse(input_event)
            self.app.refresh()
        # App Close
        self.app.close()
