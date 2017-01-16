#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import curses
import logging


class Singleton(object):
    """Singleton decorator."""

    def __init__(self, cls):
        self.__dict__['cls'] = cls

    instances = {}

    def __call__(self):
        if self.cls not in self.instances:
            self.instances[self.cls] = self.cls()
        return self.instances[self.cls]

    def __getattr__(self, attr):
        return getattr(self.__dict__['cls'], attr)

    def __setattr__(self, attr, value):
        return setattr(self.__dict__['cls'], attr, value)


@Singleton
class MainLoop(object):
    def __init__(self):
        self.event_buffer = list()
        self.started = False
        self.data = dict()

    def set_event_buffer(self, event_buffer=None):
        if event_buffer is None:
            event_buffer = dict()
        self.event_buffer = event_buffer

    def get_event_buffer(self):
        return self.event_buffer

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

    # detailed_signal: a string containing the signal name
    # *args: additional parameters arg1, arg2
    def emit(self, detailed_signal, args=None):
        if args is None:
            args = dict()
        logging.debug(detailed_signal + ' ' + str(args))
        self.get_event_buffer().insert(0, [detailed_signal, args])
        GLXCurses.application.refresh()

    def handle_curses_input(self, input_event):
        if input_event == curses.KEY_MOUSE:
            self.emit('MOUSE_EVENT', curses.getmouse())
        elif input_event == curses.KEY_RESIZE:
            self.emit('RESIZE', [])
        else:
            self.emit('CURSES', input_event)

    # Internal
    def _get_data_dict(self):
        return self.data

    def _pop_last_event(self):
        try:
            if len(self.get_event_buffer()) > 0:
                return self.get_event_buffer().pop()
        except:
            pass

    def _handle_event(self):
        # Check Event on MainLoop (That Bad :) )
        try:
            event = self._pop_last_event()
            while event:
                # If it have event dispatch it
                GLXCurses.application.dispatch(event[0], event[1])
                # Delete the last event inside teh event list
                event = self._pop_last_event()
                # In case it was a graphic event we refresh the screen
                GLXCurses.application.refresh()
        except:
            pass

    def _run(self):
        if self.get_started():
            # A bit light for notify about we are up and runing, but we are really inside the main while(1) loop
            logging.debug(self.__class__.__name__ + ': Started')
            # That in theory the first refresh of the application

            GLXCurses.application.refresh()

        # Main while 1
        while self.get_started():
            # logging.debug(self.__class__.__name__ + ': Waiting event\'s')
            input_event = GLXCurses.application.getch()

            if input_event != -1:
                self.handle_curses_input(input_event)

            self._handle_event()


        # Here self.get_started() == False , then the GLXCurse.Mainloop() should be close
        GLXCurses.application.close()
