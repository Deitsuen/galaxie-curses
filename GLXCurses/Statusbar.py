#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Statusbar(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.set_name('Statusbar')

        # Widget Setting
        self.statusbar_stack = []

        # Make a Style heritage attribute
        if self.get_style().attribute:
            self.attribute = self.get_style().attribute

    def draw(self):

        # Place the status bar from the end of the screen by look if it have a tool bar before
        if self.parent.toolbar:
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1

        drawing_area = self.get_screen().subwin(
            0,
            0,
            self.get_screen_height() - line_from_max_screen_height,
            self.get_screen_x()
        )
        self.set_curses_subwin(drawing_area)

        # Clean the entire line
        if curses.has_colors():
            self.curses_subwin.addstr(
                    0,
                    0,
                    str(' ' * (self.get_width() - 1)),
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('white', 'STATE_NORMAL'),
                        bg=self.get_attr('black', 'STATE_NORMAL'))
                    )
                )
            self.curses_subwin.insstr(
                    str(' '),
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('white', 'STATE_NORMAL'),
                        bg=self.get_attr('black', 'STATE_NORMAL'))
                    )
                )

        # If it have something inside the Statusbar stack they display it but care about the display size
        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1]
            if not len(message_to_display) <= self.get_width() - 1:
                start, end = message_to_display[:self.get_width() - 1], message_to_display[self.get_width() - 1:]
                self.curses_subwin.addstr(
                    0,
                    0,
                    str(start)
                )
                self.curses_subwin.insstr(
                    0,
                    self.get_width() - 1,
                    str(message_to_display[:self.get_width()][-1:])
                )
            else:
                self.curses_subwin.addstr(
                    0,
                    0,
                    str(message_to_display)
                )

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def push(self, text):
        self.statusbar_stack.append(text)

    def pop(self):
        self.statusbar_stack.pop()
