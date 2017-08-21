#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Box
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class VBox(Box):
    def destroy(self):
        raise NotImplementedError

    def __init__(self):
        # Load heritage
        Box.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.VBox'

        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('VBox')

        # Make a Widget Style heritage attribute as local attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

        self.preferred_height = 2
        self.preferred_width = 2

    # GLXC VBox Functions
    def draw_widget_in_area(self):

        # Check widgets to display
        is_large_enough = (self.get_width() > 2)
        is_high_enough = (self.get_height() > 2)

        if is_high_enough and is_large_enough:
            if self.get_children():
                devised_box_size = int(self.get_height() / len(self.get_children()))
                index = 0
                total_vertical_spacing = 0
                for children in self.get_children():

                    # Check if that the first element
                    if index == 0:
                        sub_win = self.get_curses_subwin().subwin(
                            devised_box_size - self.get_spacing(),
                            self.get_width() - self.get_spacing() * 2,
                            self.get_y() + self.get_spacing(),
                            self.get_x() + self.get_spacing()
                        )
                        total_vertical_spacing += self.get_spacing()
                    # Normal
                    elif 1 <= index <= len(self.get_children())-2:
                        sub_win = self.get_curses_subwin().subwin(
                            devised_box_size - (self.get_spacing() / 2),
                            self.get_width() - self.get_spacing() * 2,
                            self.get_y() + (devised_box_size * index) + (self.get_spacing() / 2),
                            self.get_x() + self.get_spacing()
                        )
                        total_vertical_spacing += self.get_spacing() / 2
                    # Check if that the last element
                    else:
                        last_element_vertical_size = self.get_height()
                        last_element_vertical_size -= (devised_box_size * index)
                        last_element_vertical_size -= total_vertical_spacing
                        try:
                            sub_win = self.get_curses_subwin().subwin(
                                    last_element_vertical_size,
                                    self.get_width() - self.get_spacing() * 2,
                                    self.get_y() + (devised_box_size * index),
                                    self.get_x() + self.get_spacing()
                            )
                        except curses.error:
                            pass
                    index += 1

                    # Drawing
                    children['widget'].set_curses_subwin(sub_win)
                    children['widget'].draw_widget_in_area()
