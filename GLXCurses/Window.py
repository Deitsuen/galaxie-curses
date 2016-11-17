#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class Window(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.set_name('Window')

        # Internal Widget Setting
        self.title = None

        self.widget_to_display = {}
        self.widget_to_display_id = ''

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        self.preferred_height = 2
        self.preferred_width = 2

    # GLXC Window Functions
    def draw_widget_in_area(self):

        # Apply the Background color
        self.get_curses_subwin().bkgdset(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        self.get_curses_subwin().bkgd(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

        # Check widgets to display
        if bool(self.widget_to_display):
            self.widget_to_display[self.widget_to_display_id].set_style(self.get_style())
            self.widget_to_display[self.widget_to_display_id].draw()

        # Create a box and add the name of the windows like a king, who trust that !!!
        if self.get_decorated():
            self.get_curses_subwin().box()
            if self.get_title():
                self.get_curses_subwin().addstr(
                    0,
                    1,
                    resize_text(self.get_title(), self.get_width() - 2, '~')
                )
        else:
            if self.get_title():
                self.get_curses_subwin().addstr(
                    0,
                    0,
                    resize_text(self.get_title(), self.get_width() - 1, '~')
                )

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def add(self, widget):
        # set_parent is the set_parent from Widget common method
        # information's will be transmit by it method
        widget.set_parent(self)
        id_max = len(self.widget_to_display.keys())

        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = widget
            self.widget_to_display_id = id_max
        else:
            self.widget_to_display[id_max + 1] = widget
            self.widget_to_display_id = id_max + 1

    def get_attr(self, elem, state):
        return self.attribute[elem][state]
