#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import time
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

class Statusbar(object):
    def __init__(self, application):
        self.statusbar_stack = []
        self.main_window = ''
        self.parent_num_lines = ''
        self.parent_num_cols = ''
        self.parent_x = ''
        self.parent_y = ''
        self.application = application
        self.draw_statusbar()

    def draw_statusbar(self):
        application = self.application
        main_window = self.application.main_window
        self.parent_num_lines, self.parent_num_cols = main_window.getmaxyx()
        self.parent_y, self.parent_x = main_window.getbegyx()
        statusbar = application.screen.subwin(
            0,
            0,
            self.parent_y + self.parent_num_lines - 1,
            0
        )
        actual_y_size, actual_x_size = statusbar.getmaxyx()

        if curses.has_colors():
                statusbar.addstr(
                    0,
                    0,
                    str(' ' * (actual_x_size - 1)),
                    curses.color_pair(2)
                )
                statusbar.insstr(
                    str(' '),
                    curses.color_pair(2)
                )

        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1]
            if not len(message_to_display) <= actual_x_size - 1:
                start, end = message_to_display[:actual_x_size - 1], message_to_display[actual_x_size - 1:]
                statusbar.addstr(
                    0,
                    0,
                    str(start)
                )
                statusbar.insstr(
                    0,
                    actual_x_size - 1,
                    str(message_to_display[:actual_x_size][-1:])
                )
            else:
                statusbar.addstr(
                    0,
                    0,
                    str(message_to_display)
                )

    def refresh(self):
        self.draw_statusbar()

    def push(self, text):
        self.statusbar_stack.append(text)

    def pop(self):
        self.statusbar_stack.pop()
