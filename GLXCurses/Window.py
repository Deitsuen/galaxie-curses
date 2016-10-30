#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
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
        self.type = 'Window'
        # Internal Widget Setting
        self.title = ''

        self.widget_to_display = {}
        self.widget_to_display_id = ''

    # GLXC Window Functions
    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.parent_spacing = self.parent.get_spacing()

        self.widget = self.parent.widget.subwin(
            parent_height - (self.widget_spacing * 2),
            parent_width - (self.widget_spacing * 2),
            parent_y + self.widget_spacing,
            parent_x + self.widget_spacing
        )

        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()
        min_size_width = (self.widget_spacing * 2) + self.widget_spacing
        min_size_height = (self.widget_spacing * 2)
        if (widget_height >= min_size_height) and (widget_width >= min_size_width):
            if curses.has_colors():
                self.widget.bkgdset(ord(' '), curses.color_pair(self.get_style_by_type(self.type)))
                self.widget.bkgd(ord(' '), curses.color_pair(self.get_style_by_type(self.type)))
                for I in range(widget_y, widget_height):
                    self.widget.addstr(
                        I,
                        0,
                        str(' ' * int(widget_width - 1)),
                        curses.color_pair(self.get_style_by_type(self.type))
                    )
                    self.widget.insstr(
                        I,
                        int(widget_width - 1),
                        str(' '),
                        curses.color_pair(self.get_style_by_type(self.type))
                    )

                # Check widgets to display
                if bool(self.widget_to_display):
                    self.widget_to_display[self.widget_to_display_id].draw()

            # Creat a box and add the name of the windows like a king, who trust that !!!
            if self.widget_decorated > 0:
                self.widget.box()
                if not self.title == '':
                    self.widget.addstr(
                        0,
                        1,
                        resize_text(self.title, widget_width - 2, '~')
                    )
            else:
                if not self.title == '':
                    self.widget.addstr(
                        0,
                        0,
                        resize_text(self.title, widget_width - 1, '~')
                    )

    def set_title(self, title):
        self.title = title

    def add(self, widget):
        widget.set_parent(self)
        id_max = len(self.widget_to_display.keys())
        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = widget
            self.widget_to_display_id = id_max
        else:
            self.widget_to_display[id_max + 1] = widget
            self.widget_to_display_id = id_max + 1




