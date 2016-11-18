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
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('VBox')

        self.children_list = list()

        self.preferred_height = 2
        self.preferred_width = 2

    # GLXC VBox Functions
    def draw_widget_in_area(self):

        # Check widgets to display
        is_large_enough = (self.get_width() > 2)
        is_high_enough = (self.get_height() > 2)

        if is_high_enough and is_large_enough:
            if self.children_list:
                devised_box_size = int(self.get_height() / len(self.children_list))
                index = 0
                total_vertical_spacing = 0
                for glxc_widget in self.children_list:
                    # Check if that the frist element
                    if index == 0:
                        sub_win = self.get_curses_subwin().subwin(
                                devised_box_size - glxc_widget.get_spacing(),
                                self.get_width() - glxc_widget.get_spacing() * 2,
                                self.get_y() + glxc_widget.get_spacing(),
                                self.get_x() + glxc_widget.get_spacing()
                        )
                        total_vertical_spacing += glxc_widget.get_spacing()
                    # Normal
                    elif 1 <= index <= len(self.children_list)-2:
                        sub_win = self.get_curses_subwin().subwin(
                                devised_box_size - (glxc_widget.get_spacing() / 2),
                                self.get_width() - glxc_widget.get_spacing() * 2,
                                self.get_y() + (devised_box_size * index) + (glxc_widget.get_spacing() / 2),
                                self.get_x() + glxc_widget.get_spacing()
                        )
                        total_vertical_spacing += glxc_widget.get_spacing() / 2
                    # Check if that the last element
                    else:
                        last_element_vertical_size = self.get_height()
                        last_element_vertical_size -= (devised_box_size * index)
                        last_element_vertical_size -= total_vertical_spacing
                        #last_element_vertical_size -= glxc_widget.get_spacing()
                        sub_win = self.get_curses_subwin().subwin(
                                last_element_vertical_size,
                                self.get_width() - glxc_widget.get_spacing() * 2,
                                self.get_y() + (devised_box_size * index) + (glxc_widget.get_spacing() / 2),
                                self.get_x() + glxc_widget.get_spacing()
                        )

                    index += 1

                    # Drawing
                    glxc_widget.set_curses_subwin(sub_win)
                    glxc_widget.draw_widget_in_area()
                    #widget.set_parent


    def add(self, widget):
        #widget.set_parent(self)
        self.children_list.append(widget)
