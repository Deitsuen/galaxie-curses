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
        self.name = 'VBox'

        self.widget_to_display = []
        self.widget_subwins = {}
        self.h_widget_list = {}
        self.widget_to_display_id = ''
        self.number_of_widget_to_display = 0

    # GLXC VBox Functions
    def draw(self):
        parent_height, parent_width = self.get_parent_size()
        parent_y, parent_x = self.get_parent_origin()
        spacing = self.get_spacing()

        drawing_area = self.parent.widget.subwin(
            parent_height - (spacing * 2),
            parent_width - (spacing * 2),
            parent_y + spacing,
            parent_x + spacing
        )
        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):

        self.widget = drawing_area

        widget_height, widget_width = self.get_size()
        widget_y, widget_x = self.get_origin()

        # Check widgets to display
        is_large_enough = (widget_width >= self.number_of_widget_to_display + 1)
        is_high_enough = (widget_height >= self.number_of_widget_to_display + 1)

        if is_high_enough and is_large_enough:
            if self.widget_to_display:
                devised_box_size = int(widget_height / len(self.widget_to_display))
                index = 0
                for widget in self.widget_to_display:
                    # Get the Children Spacing
                    spacing = widget.get_spacing()

                    # Check if that the frist element
                    if index == 0:
                        subwin = self.widget.subwin(
                                devised_box_size - spacing,
                                widget_width - spacing * 2,
                                widget_y + spacing,
                                widget_x + spacing
                        )
                    # Normal
                    elif 1 <= index <= len(self.widget_to_display)-2:
                        subwin = self.widget.subwin(
                                devised_box_size - (spacing / 2),
                                widget_width - spacing * 2,
                                widget_y + (devised_box_size * index) + (spacing / 2),
                                widget_x + spacing
                        )
                    # Check if that the last element
                    else:
                        subwin = self.widget.subwin(
                                0,
                                widget_width - spacing * 2,
                                widget_y + (devised_box_size * index) + (spacing / 2),
                                widget_x + spacing
                        )

                    index += 1

                    # Finally
                    widget.draw_in_area(subwin)

    def add(self, widget):
        widget.set_parent(self)
        self.widget_to_display.append(widget)
