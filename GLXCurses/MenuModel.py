#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class MenuModel(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'MenuModel'

        # Internal Widget Setting
        self.app_info_label = ''

        if self.style.attribute:
            self.color_text = self.style.attribute['dark']['STATE_NORMAL']
            self.color_bg = self.style.attribute['bg']['STATE_PRELIGHT']
            self.color_normal = self.style.get_curses_pairs(fg=self.color_text, bg=self.color_bg)

        else:
            self.color_normal = 0

    def draw(self):
        actual_x_size, actual_y_size = self.screen.getmaxyx()
        app_info_label = self.app_info_label
        self.widget = self.screen.subwin(0, 0, 0, 0)
        if curses.has_colors():
            self.widget.addstr(
                    0,
                    0,
                    str(" " * int(actual_y_size)),
                    curses.color_pair(self.color_normal)
                )
            self.widget.bkgdset(
                    ord(' '),
                    curses.color_pair(self.color_normal)
                )
        if len(self.app_info_label) > 0:
            if not actual_y_size + 1 <= len(app_info_label):
                self.widget.addstr(
                    0,
                    (actual_y_size - 1) - len(str(app_info_label[:-1])),
                    app_info_label[:-1],
                    curses.color_pair(self.color_normal)
                )
                self.widget.insstr(
                    0,
                    actual_y_size - 1,
                    app_info_label[-1:],
                    curses.color_pair(self.color_normal)
                )
