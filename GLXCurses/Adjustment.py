#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import GLXCurses



class Adjustment(object):


    def __init__(self):
        self.value = 1.0
        self.lower = 1.0
        self.upper = 110.0
        self.step_increment=1
        self.page_size=10

    def get_value(self):
        return int(self.value)

    def set_value(self):

        if self.value > self.upper:
            self.value = self.upper

        elif self.value < self.lower:
            self.value = self.lower
        else:
            self.value = self.value

                def clamp_page(self):
        if self.value <= self.lower <= self.upper:
            self.value = self.value + self.page_size
        if self.upper and self.lower <= self.page_size:
            self.page_size = self.lower

            self.value_changed()


    def changed(self):
        instance = {
            'class': self.__class__.__name__,
            'type': 'changed',
            'id': self.id
        }
        # EVENT EMIT
        GLXCurses.application.emit('SIGNALS', instance)

    def value_changed(self):
            instance = {
                'class': self.__class__.__name__,
                'type': 'value-changed',
                'id': self.id
            }
            # EVENT EMIT
            GLXCurses.application.emit('SIGNALS', instance)


