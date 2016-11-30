#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class EventBus(object):
    def __init__(self):
        self.subscriptions = dict()
        self.blocked_handler = list()
        self.blocked_function = list()
    # The connect_after() method is similar to the connect() method
    # except that the handler is added to the signal handler list after the default class signal handler.
    # Otherwise the details of handler definition and invocation are the same.
    # detailed_signal: a string containing the signal name
    # *args: additional parameters arg1, arg2
    def connect(self, detailed_signal, handler, *args):
        # That IF preserve the handler_id
        if detailed_signal not in self.subscriptions:
            self.subscriptions[detailed_signal] = dict()
            self.subscriptions[detailed_signal]['handler'] = handler
            self.subscriptions[detailed_signal]['handler_id'] = uuid.uuid1().int
            self.subscriptions[detailed_signal]['argvs'] = args
        return self.subscriptions[detailed_signal]['handler_id']

    def reset(self):
        # All subscribers will be cleared.
        self.subscriptions = dict()
        self.blocked_handler = dict()

    def get_subscriptions(self):
        return self.subscriptions

    # The disconnect() method removes the signal handler with the specified handler_id
    # from the list of signal handlers for the object.
    # handler_id: an integer handler identifier
    def disconnect(self, handler_id):
        for subscription in self.get_subscriptions():
            if self.get_subscriptions()[subscription]['handler_id'] == handler_id:
                del self.get_subscriptions()[subscription]
                break

    # The handler_disconnect() method removes the signal handler with the specified handler_id
    # from the list of signal handlers for the object.
    # handler_id: an integer handler identifier
    def handler_disconnect(self, handler_id):
        self.disconnect(handler_id)

    # The handler_is_connected() method returns True
    # if the signal handler with the specified handler_id is connected to the object.
    def handler_is_connected(self, handler_id):
        for subscription in self.get_subscriptions():
            if self.get_subscriptions()[subscription]['handler_id'] == handler_id:
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
        for subscription in self.get_subscriptions():
            if subscription == detailed_signal:
                if self.get_subscriptions()[subscription]['handler_id'] not in self._get_blocked_handler():
                    if self.get_subscriptions()[subscription]['handler'] not in self._get_blocked_function():
                        self.get_subscriptions()[subscription]['handler'](*args)

    # Internal Function
    def _get_blocked_handler(self):
        return self.blocked_handler

    def _get_blocked_function(self):
        return self.blocked_function


def print_hello1(text=None):
    if text:
        print (text)


def print_hello2(text=None):
    if text:
        print (text)


def print_hello3(text=None):
    if text:
        print (text)


if __name__ == '__main__':
    event = EventBus()
    handle_1 = event.connect("coucou1", print_hello1)
    handle_2 = event.connect("coucou2", print_hello2)
    handle_3 = event.connect("coucou3", print_hello3)
    print('Before')
    for subcription in event.get_subscriptions():
        print(subcription + ": " + str(event.get_subscriptions()[subcription]))

    print('After')
    event.disconnect(handle_1)
    handle_1 = event.connect("coucou1", print_hello1, '1', '2', '3')
    event.handler_block(handle_1)
    event.handler_unblock(handle_1)
    event.handler_block_by_func(print_hello2)
    event.handler_unblock_by_func(print_hello2)
    for subcription in event.get_subscriptions():
        print(subcription + ": " + str(event.get_subscriptions()[subcription]))
    if event.handler_is_connected(handle_1):
        event.emit('coucou1', 'comment la vie est belle')
    event.emit('coucou2', 'ben on sait pas')
    event.emit('coucou3', 'mais si on sait')
