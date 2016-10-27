#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Window(object):
    def __init__(self, application):
        self.title = ''
        self.decorated = 0
        self.application = application
        self.main_window = application.main_window
        self.parent_num_lines, self.parent_num_cols = self.main_window.getmaxyx()
        self.parent_y, self.parent_x = self.main_window.getbegyx()

    def draw_window(self):
        self.main_window = self.application.main_window
        self.parent_num_lines, self.parent_num_cols = self.main_window.getmaxyx()
        self.parent_y, self.parent_x = self.main_window.getbegyx()
        window = self.main_window.subwin(
            self.parent_num_lines,
            self.parent_num_cols,
            self.parent_y,
            self.parent_x
        )

        window_num_lines, window_num_cols = window.getmaxyx()
        window_y, window_x = window.getbegyx()

        if curses.has_colors():
            window.bkgdset(ord(' '), curses.color_pair(3))
            window.bkgd(ord(' '), curses.color_pair(3))
            for I in range(window_y, window_num_lines):
                window.addstr(I, 0, str(' ' * int(window_num_cols - 1)), curses.color_pair(3))
                window.insstr(I, int(window_num_cols - 1), str(' '), curses.color_pair(3))

        # Creat a box and add the name of the windows like a king, who trust that !!!
        if self.decorated > 0:
            window.box()
            if not self.title == '':
                window.addstr(0, 1, self.title)
        else:
            if not self.title == '':
                window.addstr(0, 0, self.title)

    def set_title(self, title):
        self.title = title

    def set_decorated(self, boolean):
        self.decorated = int(boolean)

    def refresh(self):
        self.draw_window()


