#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import GLXCurses



class Adjustment(object):


    def __init__(self):
        self.value = 1.0
        self.lower = 1.0
        self.upper = 110.0

    def get_value(self):
        return int(self.value)

    def set_value(self):

        if self.value > self.upper:
            self.value = self.upper

        elif self.value < self.lower:
            self.value = self.lower
        else:
            self.value = self.value


