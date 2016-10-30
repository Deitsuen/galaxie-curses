#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

from Style import Style
class MenuModel(Widget):
    def __init__(self, parent):
        Widget.__init__(self)
        self.set_parent(parent)

        # Internal Widget Setting
        self.app_info_label = ''
        self.type = 'MenuModel'
        # Mandatory Method
        self.draw()

    def draw(self):
        actual_x_size, actual_y_size = self.screen.getmaxyx()
        app_info_label = self.app_info_label
        self.widget = self.screen.subwin(0, 0, 0, 0)
        if curses.has_colors():
            self.widget.addstr(
                    0,
                    0,
                    str(" " * int(actual_y_size)),
                    curses.color_pair(self.get_style_by_type(self.type))
                )
            self.widget.bkgdset(
                    ord(' '),
                    curses.color_pair(self.get_style_by_type(self.type))
                )
        if len(self.app_info_label) > 0:
            if not actual_y_size + 1 <= len(app_info_label):
                self.widget.addstr(
                    0,
                    (actual_y_size - 1) - len(str(app_info_label[:-1])),
                    app_info_label[:-1],
                    curses.color_pair(self.get_style_by_type(self.type))
                )
                self.widget.insstr(
                    0,
                    actual_y_size - 1,
                    app_info_label[-1:],
                    curses.color_pair(self.get_style_by_type(self.type))
                )
