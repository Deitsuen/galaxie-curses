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

    # detailed_signal: a string containing the signal name
    # *args: additional parameters arg1, arg2
    def emit(self, detailed_signal, *args):
        for subscription in self.get_subscriptions():
            if subscription == detailed_signal:
                self.get_subscriptions()[subscription]['handler'](*args)


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
    for subcription in event.get_subscriptions():
        print(subcription + ": " + str(event.get_subscriptions()[subcription]))
    if event.handler_is_connected(handle_1):
        event.emit('coucou1', 'comment la vie est belle')
    event.emit('coucou2', 'ben on sait pas')
    event.emit('coucou3', 'mais si on sait')
