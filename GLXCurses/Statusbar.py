#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Statusbar(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'Statusbar'

        # Widget Setting
        self.statusbar_stack = []

    def draw(self):

        screen_height, screen_width = self.screen.getmaxyx()

        # Place the status bar from the end of the screen by look if it have a tool bar before
        if not self.parent.toolbar == '':
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1
        self.widget = self.screen.subwin(
            0,
            0,
            screen_height - line_from_max_screen_height,
            0
        )
        # Get the Status Bar size
        height, width = self.widget.getmaxyx()

        # Clean the entire line
        if curses.has_colors():
            self.widget.addstr(
                    0,
                    0,
                    str(' ' * (width - 1)),
                    curses.color_pair(self.style.colors.index('Statusbar'))
                )
            self.widget.insstr(
                    str(' '),
                    curses.color_pair(self.style.colors.index('Statusbar'))
                )

        # If it have something inside the Statusbar stack they display it but care about the display size
        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1]
            if not len(message_to_display) <= width - 1:
                start, end = message_to_display[:width - 1], message_to_display[width - 1:]
                self.widget.addstr(
                    0,
                    0,
                    str(start)
                )
                self.widget.insstr(
                    0,
                    width - 1,
                    str(message_to_display[:width][-1:])
                )
            else:
                self.widget.addstr(
                    0,
                    0,
                    str(message_to_display)
                )

    def push(self, text):
        self.statusbar_stack.append(text)

    def pop(self):
        self.statusbar_stack.pop()
