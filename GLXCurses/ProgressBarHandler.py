#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GLXCurses.Object import Object
from GLXCurses.ProgressBar import ProgressBar

class ProgressBarHandler(Object):

    def __init__(self, progressbar):
        Object.__init__(self)
        self._progressbar = progressbar

    def handleUpButtonClicked(self, event):
        current = self._progressbar.get_value()
        self._progressbar.set_value(current+1)
        value = '{0:}{1:}'.format(self._progressbar.get_value(), '%')
        self._progressbar.set_text(value)