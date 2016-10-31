#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class VBox(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.type = 'VBox'
        self.title = ''

        self.subwins_spacing = 0

        self.widget_to_display = []
        self.widget_subwins = {}
        self.h_widget_list = {}
        self.widget_to_display_id = ''
        self.number_of_widget_to_display = 0


    # GLXC VBox Functions
    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()

        self.widget = self.parent.widget.subwin(
            parent_height - (self.widget_spacing * 2),
            parent_width - (self.widget_spacing * 2),
            parent_y + self.widget_spacing,
            parent_x + self.widget_spacing
        )

        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        # Check widgets to display
        is_large_enough = (widget_width >= self.number_of_widget_to_display + 1)
        is_high_enough = (widget_height >= self.number_of_widget_to_display + 1)

        if is_high_enough and is_large_enough:
            if self.widget_to_display:
                devised_box_size = int(widget_height / len(self.widget_to_display))
                index = 0
                for widget in self.widget_to_display:

                    if index == 0:
                        drawing_area = self.widget.subwin(
                                devised_box_size - self.subwins_spacing,
                                widget_width - self.subwins_spacing * 2,
                                widget_y + self.subwins_spacing,
                                widget_x + self.subwins_spacing
                        )
                    else:
                        drawing_area = self.widget.subwin(
                                devised_box_size - (self.subwins_spacing / 2),
                                widget_width - self.subwins_spacing * 2,
                                widget_y + (devised_box_size * index) + (self.subwins_spacing / 2),
                                widget_x + self.subwins_spacing
                        )

                    widget.draw_in_area(drawing_area)

                    index += 1

    def set_title(self, title):
        self.title = title

    def add(self, widget):
        widget.set_parent(self)
        self.widget_to_display.append(widget)
