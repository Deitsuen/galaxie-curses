#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class EventBus(object):
    def __init__(self):
        self.subscriptions = {}

    def connect(self, detailed_signal, handler, *args, **kwargs):
        if detailed_signal not in self.subscriptions:
            self.subscriptions[detailed_signal] = dict()
            self.subscriptions[detailed_signal]['handler'] = handler
            self.subscriptions[detailed_signal]['handler_id'] = uuid.uuid1().int
        return self.subscriptions[detailed_signal]['handler_id']

    def reset(self):
        # Resets the eventbus. All subscribers will be cleared.
        self.subscriptions = {}

    def get_subscriptions(self):
        return self.subscriptions

    def disconnect(self, handler_id):
        for subscription in self.get_subscriptions():
            if self.get_subscriptions()[subscription]['handler_id'] == handler_id:
                del self.get_subscriptions()[subscription]
                break



def print_hello1():
    print ('Hello1')


def print_hello2():
    print ('Hello2')


def print_hello3():
    print ('Hello3')


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
    for subcription in event.get_subscriptions():
        print(subcription + ": " + str(event.get_subscriptions()[subcription]))

