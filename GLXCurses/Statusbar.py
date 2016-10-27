#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Statusbar(object):
    def __init__(self, application):
        self.statusbar_stack = []
        self.width = ''
        self.height = ''
        self.application = application

        self.draw_statusbar()

    def draw_statusbar(self):
        screen = self.application.screen
        screen_height, screen_width = screen.getmaxyx()

        # Place the status bar from the end of the screen by look if it have a tool bar before
        if not self.application.tool_bar == '':
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1
        statusbar = screen.subwin(
            0,
            0,
            screen_height - line_from_max_screen_height,
            0
        )
        # Get the Status Bar size
        self.height, self.width = statusbar.getmaxyx()

        # Clean the entire line
        if curses.has_colors():
                statusbar.addstr(
                    0,
                    0,
                    str(' ' * (self.width - 1)),
                    curses.color_pair(2)
                )
                statusbar.insstr(
                    str(' '),
                    curses.color_pair(2)
                )

        # If it have something inside the Statusbar stack they display it but care about the display size
        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1]
            if not len(message_to_display) <= self.width - 1:
                start, end = message_to_display[:self.width - 1], message_to_display[self.width - 1:]
                statusbar.addstr(
                    0,
                    0,
                    str(start)
                )
                statusbar.insstr(
                    0,
                    self.width - 1,
                    str(message_to_display[:self.width][-1:])
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
