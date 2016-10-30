#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Statusbar(Widget):
    def __init__(self, parent):
        Widget.__init__(self)
        self.set_parent(parent)
        self.statusbar_stack = []
        self.width = ''
        self.height = ''
        self.type = 'Statusbar'

        self.draw()

    def draw(self):
        screen = self.screen
        screen_height, screen_width = screen.getmaxyx()

        # Place the status bar from the end of the screen by look if it have a tool bar before
        if not self.parent.toolbar == '':
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1
        self.widget = screen.subwin(
            0,
            0,
            screen_height - line_from_max_screen_height,
            0
        )
        # Get the Status Bar size
        self.height, self.width = self.widget.getmaxyx()

        # Clean the entire line
        if curses.has_colors():
            self.widget.addstr(
                    0,
                    0,
                    str(' ' * (self.width - 1)),
                    curses.color_pair(self.get_style_by_type(self.type))
                )
            self.widget.insstr(
                    str(' '),
                    curses.color_pair(self.get_style_by_type(self.type))
                )

        # If it have something inside the Statusbar stack they display it but care about the display size
        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1]
            if not len(message_to_display) <= self.width - 1:
                start, end = message_to_display[:self.width - 1], message_to_display[self.width - 1:]
                self.widget.addstr(
                    0,
                    0,
                    str(start)
                )
                self.widget.insstr(
                    0,
                    self.width - 1,
                    str(message_to_display[:self.width][-1:])
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
