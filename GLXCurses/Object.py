#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Object(object):
    def __init__(self):

        # Object flags
        self.flags = None

        # Signal
        self.signal_handlers = dict()
        self.blocked_handler = list()
        self.blocked_function = list()
        self.data = dict()

    def set_flags(self):
        flags = dict()

        # The object is currently being destroyed.
        flags['IN_DESTRUCTION'] = False

        # The object is orphaned.
        flags['FLOATING'] = True

        # Widget flags
        # widgets without a real parent (e.g. Window and Menu) have this flag set throughout their lifetime.
        flags['TOPLEVEL'] = False

        # A widget that does not provide its own Window.
        # Visible action (e.g. drawing) is performed on the parent's Window.
        flags['NO_WINDOW'] = True

        # The widget has an associated Window.
        flags['REALIZED'] = False

        # The widget can be displayed on the screen.
        flags['MAPPED'] = False

        # The widget will be mapped as soon as its parent is mapped.
        flags['VISIBLE'] = True

        # The sensitivity of a widget determines whether it will receive certain events (e.g. button or key presses).
        # One requirement for the widget's sensitivity is to have this flag set.
        flags['SENSITIVE'] = True

        # This is the second requirement for the widget's sensitivity.
        # Once a widget has SENSITIVE and PARENT_SENSITIVE set, its state is effectively sensitive.
        flags['PARENT_SENSITIVE'] = True

        # The widget is able to handle focus grabs.
        flags['CAN_FOCUS'] = True

        # The widget has the focus - assumes that CAN_FOCUS is set
        flags['HAS_FOCUS'] = True

        # The widget is allowed to receive the default action.
        flags['CAN_DEFAULT'] = True

        # The widget currently will receive the default action.
        flags['HAS_DEFAULT'] = False

        # The widget is in the grab_widgets stack, and will be the preferred one for receiving events.
        flags['HAS_GRAB'] = False

        # The widgets style has been looked up through the RC mechanism.
        # It does not imply that the widget actually had a style defined through the RC mechanism.
        flags['RC_STYLE'] = 'Default.yml'

        # The widget is a composite child of its parent.
        flags['COMPOSITE_CHILD'] = False

        # unused
        flags['NO_REPARENT'] = 'unused'

        # Set on widgets whose window the application directly draws on,
        # in order to keep GLXCurse from overwriting the drawn stuff.
        flags['APP_PAINTABLE'] = False

        # The widget when focused will receive the default action and have HAS_DEFAULT set
        # even if there is a different widget set as default.
        flags['RECEIVES_DEFAULT'] = False

        # Exposes done on the widget should be double-buffered.
        flags['DOUBLE_BUFFERED'] = False

        self.flags = flags

    def unset_flags(self, flags):
        self.flags = None

    def destroy(self):
        raise NotImplementedError

    # The get_data() method returns the Python object associated with the specified key or
    # None if there is no data associated with the key or if there is no key associated with the object.
    # key : a string used as the key
    # data : a Python object that is the value to be associated with the key
    def get_data(self, key):
        if key not in self._get_data_dict():
            return None
        elif not len(self._get_data_dict()[key]):
            return None
        else:
            return self._get_data_dict()[key]

    # The set_data() method associates the specified Python object (data) with key.
    # key : a string used as the key
    # data : a Python object that is the value to be associated with the key
    def set_data(self, key, data):
        self._get_data_dict()[key] = data

    # The connect() method adds a function or method (handler)to the end of the list of signal handlers
    # for the named detailed_signal but before the default class signal handler.
    # An optional set of parameters may be specified after the handler parameter.
    # These will all be passed to the signal handler when invoked.
    # detailed_signal: a string containing the signal name
    # *args: additional parameters arg1, arg2
    def connect(self, detailed_signal, handler, *args):
        if detailed_signal not in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal] = {}

        subscription = {
            'handler': handler,
            'argvs': args
        }
        handler_id = uuid.uuid1().int
        self._get_signal_handlers_dict()[detailed_signal][handler_id] = subscription
        return handler_id

    # The disconnect() method removes the signal handler with the specified handler_id
    # from the list of signal handlers for the object.
    # handler_id: an integer handler identifier
    def disconnect(self, handler_id):
        for detailed_signal, infos in self._get_signal_handlers_dict().iteritems():
            for id, infos2 in infos.iteritems():
                if id == handler_id:
                    del self._get_signal_handlers_dict()[detailed_signal][handler_id]
                    break

    # The handler_disconnect() method removes the signal handler with the specified handler_id
    # from the list of signal handlers for the object.
    # handler_id: an integer handler identifier
    def handler_disconnect(self, handler_id):
        self.disconnect(handler_id)

    # The handler_is_connected() method returns True
    # if the signal handler with the specified handler_id is connected to the object.
    def handler_is_connected(self, handler_id):
        for detailed_signal, infos in self._get_signal_handlers_dict().iteritems():
            for id, infos in infos.iteritems():
                if id == handler_id:
                    return True
        return False

    # The handler_block() method blocks the signal handler with the specified handler_id
    # from being invoked until it is unblocked.
    # handler_id: an integer handler identifier
    def handler_block(self, handler_id):
        if handler_id not in self.blocked_handler:
            self._get_blocked_handler().append(handler_id)
        else:
            pass

    # handler_id: an integer handler identifier
    def handler_unblock(self, handler_id):
        # noinspection PyBroadException
        try:
            self._get_blocked_handler().pop(self._get_blocked_handler().index(handler_id))
        except:
            pass

    # The handler_block_by_func() method blocks
    # the all signal handler connected to a specific callable from being invoked until the callable is unblocked.
    # callable : a callable python object
    def handler_block_by_func(self, callable):
        if callable not in self.blocked_handler:
            self._get_blocked_function().append(callable)
        else:
            pass

    # The handler_unblock_by_func() method unblocks all signal handler connected to a specified callable there
    # by allowing it to be invoked when the associated signals are emitted.
    # callback : a callable python object
    def handler_unblock_by_func(self, callback):
        # noinspection PyBroadException
        try:
            self._get_blocked_function().pop(self._get_blocked_function().index(callback))
        except:
            pass

    # detailed_signal: a string containing the signal name
    # *args: additional parameters arg1, arg2
    def emit(self, detailed_signal, *args):
        for subscription, infos in self._get_signal_handlers_dict().iteritems():
            if subscription == detailed_signal:
                for id, infos in infos.iteritems():
                    if id not in self._get_blocked_handler():
                        if id not in self._get_blocked_handler():
                            self._get_signal_handlers_dict()[subscription][id]['handler'](*args)

    # Internal Function
    def _reset(self):
        # All subscribers will be cleared.
        self.signal_handlers = dict()
        self.blocked_handler = list()
        self.blocked_function = list()
        self.data = dict()

    def _get_signal_handlers_dict(self):
        return self.signal_handlers

    def _get_data_dict(self):
        return self.data

    def _get_blocked_handler(self):
        return self.blocked_handler

    def _get_blocked_function(self):
        return self.blocked_function