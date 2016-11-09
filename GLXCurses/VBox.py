#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class VBox(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'VBox'

        self.widget_to_display = list()
        self.h_widget_list = list()
        self.widget_to_display_id = None
        self.number_of_widget_to_display = 0

    # GLXC VBox Functions
    def draw(self):
        parent_height, parent_width = self.get_parent().get_size()
        parent_y, parent_x = self.get_parent().get_origin()

        drawing_area = self.get_parent().get_widget().subwin(
            parent_height - (self.get_spacing() * 2),
            parent_width - (self.get_spacing() * 2),
            parent_y + self.get_spacing(),
            parent_x + self.get_spacing()
        )
        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):
        self.set_widget(drawing_area)

        # Check widgets to display
        is_large_enough = (self.get_width() >= self.number_of_widget_to_display + 1)
        is_high_enough = (self.get_height() >= self.number_of_widget_to_display + 1)

        if is_high_enough and is_large_enough:
            if self.widget_to_display:
                devised_box_size = int(self.get_height() / len(self.widget_to_display))
                index = 0
                for widget in self.widget_to_display:
                    # Check if that the frist element
                    if index == 0:
                        sub_win = self.get_widget().subwin(
                                devised_box_size - widget.get_spacing(),
                                self.get_width() - widget.get_spacing() * 2,
                                self.get_y() + widget.get_spacing(),
                                self.get_x() + widget.get_spacing()
                        )
                    # Normal
                    elif 1 <= index <= len(self.widget_to_display)-2:
                        sub_win = self.get_widget().subwin(
                                devised_box_size - (widget.get_spacing() / 2),
                                self.get_width() - widget.get_spacing() * 2,
                                self.get_y() + (devised_box_size * index) + (widget.get_spacing() / 2),
                                self.get_x() + widget.get_spacing()
                        )
                    # Check if that the last element
                    else:
                        sub_win = self.get_widget().subwin(
                                0,
                                self.get_width() - widget.get_spacing() * 2,
                                self.get_y() + (devised_box_size * index) + (widget.get_spacing() / 2),
                                self.get_x() + widget.get_spacing()
                        )

                    index += 1

                    # Finally
                    widget.draw_in_area(sub_win)

    def add(self, widget):
        widget.set_parent(self)
        self.widget_to_display.append(widget)
