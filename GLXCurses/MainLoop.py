#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Application
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
    """
    ********
    MainLoop
    ********

    The MainLoop is something close to a infinity loop with a start() and stop() method
     #. Refresh the Application for the frist time
     #. Start the Loop
     #. Wait for a Curses events then dispatch events and signals over Application Children's
     #. Refresh the Application if a event or a signal have been detect
     #. If MainLoop is stop the Application will close and should be follow by a sys.exit()

    Attributes:
        event_buffer       -- A List, Default Value: list()
        started            -- A Boolean, Default Value: False

    Methods:
        get_event_buffer() -- get the event_buffer attribute
        get_started()      -- get the started attribute
        start()            -- start the mainloop
        stop()             -- stop the mainloop
        emit()             -- emit a signal

    .. warning:: you have to start the mainloop from you application via MainLoop().start()
    """

    def __init__(self):
        self.event_buffer = list()
        self.started = False

    def get_event_buffer(self):
        """
        Return the event_buffer list attribute, it lis can be edited or modify as you need

        :return: event buffer
        :rtype: list()
        """
        return self.event_buffer

    def get_started(self):
        """
        Return the started pointer it contain a boolean value

        :return: started value
        :rtype: Boolean
        """
        return self.started

    def start(self):
        """
        Start the main loop

        That method have role to update the started status and run the mainloop
        """
        self._set_started(True)
        logging.info('Starting ' + self.__class__.__name__)
        self._run()

    def stop(self):
        """
        Stop the main loop

        That method have role to update the started status and stop the mainloop.
        If the MainLoop is stop a Application().close() will case the end of you programme
        """
        self._set_started(False)
        logging.info('Stopping ' + self.__class__.__name__)

    def emit(self, detailed_signal, args=None):
        """
        Emit a signal, it consist to add the signal structure inside a global event list

        .. code-block:: python
        args = dict(
            'uuid': Widget().get_widget_id()
            'key1': value1
            'key2': value2
        )
        structure = list(
            detailed_signal,
            args
        )

        :param detailed_signal: a string containing the signal name
        :param args: additional parameters arg1, arg2
        """
        if args is None:
            args = dict()
        logging.debug(detailed_signal + ' ' + str(args))
        self.get_event_buffer().insert(0, [detailed_signal, args])
        Application().refresh()

    # Internal Method's
    def _set_started(self, boolean):
        """
        Set the started status

        :param boolean: 0 or True
        :type boolean: Boolean
        """
        self.started = bool(boolean)

    def _pop_last_event(self):
        # noinspection PyBroadException
        try:
            if len(self.get_event_buffer()) > 0:
                return self.get_event_buffer().pop()
        except:
            pass

    def _handle_curses_input(self, input_event):
        if input_event == curses.KEY_MOUSE:
            self.emit('MOUSE_EVENT', curses.getmouse())
        elif input_event == curses.KEY_RESIZE:
            self.emit('RESIZE', [])
        else:
            self.emit('CURSES', input_event)

    def _handle_event(self):
        # noinspection PyBroadException
        try:
            event = self._pop_last_event()
            while event:
                # If it have event dispatch it
                Application().dispatch(event[0], event[1])
                # Delete the last event inside teh event list
                event = self._pop_last_event()
        except:
            pass

    def _run(self):
        if self.get_started():
            # A bit light for notify about we are up and runing, but we are really inside the main while(1) loop
            logging.debug(self.__class__.__name__ + ': Started')
            # That in theory the first refresh of the application

            Application().refresh()

        # Main while 1
        while self.get_started():
            input_event = Application().getch()

            if input_event != -1:
                self._handle_curses_input(input_event)

            self._handle_event()

            # In case it was a graphic event we refresh the screen
            Application().refresh()

        # Here self.get_started() == False , then the GLXCurse.Mainloop() should be close
        Application().close()
