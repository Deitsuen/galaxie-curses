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

        if self.style.attribute:
            self.color_text = self.style.attribute['light']['STATE_NORMAL']
            self.color_bg = self.style.attribute['dark']['STATE_NORMAL']
            self.color_normal = self.get_style().get_curses_pairs(fg=self.color_text, bg=self.color_bg)

        else:
            self.color_normal = 0

    def draw(self):

        screen_height, screen_width = self.get_screen().getmaxyx()

        # Place the status bar from the end of the screen by look if it have a tool bar before
        if not self.parent.toolbar == '':
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1
        self.widget = self.get_screen().subwin(
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
                    curses.color_pair(self.color_normal)
                )
            self.widget.insstr(
                    str(' '),
                    curses.color_pair(self.color_normal)
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
