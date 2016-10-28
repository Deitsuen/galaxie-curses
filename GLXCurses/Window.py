#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class Window(object):
    def __init__(self, parent):
        self.title = ''
        self.decorated = 0
        self.spacing = 0

        self.widget = ''
        self.widget_to_display = {}
        self.widget_to_display_id = ''
        self.parent = parent

        self.draw()

    # Common Widget mandatory
    def get(self):
        return self.widget

    def get_origin(self):
        return self.widget.getbegyx()

    def get_size(self):
        return self.widget.getmaxyx()

    def get_parent(self):
        return self.parent

    def get_parent_size(self):
        return self.parent.widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def set_parent(self, parent):
        self.parent = parent

    def remove_parent(self):
        self.parent = ''

    # GLXC Window Functions
    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.widget = self.parent.widget.subwin(
            parent_height - (self.spacing * 2),
            parent_width - (self.spacing * 2),
            parent_y + self.spacing,
            parent_x + self.spacing
        )

        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        if curses.has_colors():
            self.widget.bkgdset(ord(' '), curses.color_pair(3))
            self.widget.bkgd(ord(' '), curses.color_pair(3))
            for I in range(widget_y, widget_height):
                self.widget.addstr(I, 0, str(' ' * int(widget_width - 1)), curses.color_pair(3))
                self.widget.insstr(I, int(widget_width - 1), str(' '), curses.color_pair(3))

            # Check widgets to display
            if not len(self.widget_to_display.keys()) == 0:
                self.widget_to_display[self.widget_to_display_id].draw()

        # Creat a box and add the name of the windows like a king, who trust that !!!
        if self.decorated > 0:
            self.widget.box()
            if not self.title == '':
                self.widget.addstr(0, 1, resize_text(self.title, widget_width - 2, '~'))
        else:
            if not self.title == '':
                self.widget.addstr(0, 0, resize_text(self.title, widget_width - 1, '~'))

    def set_title(self, title):
        self.title = title

    def set_decorated(self, boolean):
        self.decorated = int(boolean)

    def add(self, widget):
        id_max = len(self.widget_to_display.keys())
        if id_max == 0:
            self.widget_to_display[id_max] = widget
            self.widget_to_display_id = id_max
        else:
            self.widget_to_display[id_max + 1] = widget
            self.widget_to_display_id = id_max + 1

    def refresh(self):
        self.draw()



