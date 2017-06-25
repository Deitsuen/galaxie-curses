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
        Box.__init__(self)
        self.set_name('VBox')

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
                            devised_box_size - children['WIDGET'].get_spacing(),
                            self.get_width() - children['WIDGET'].get_spacing() * 2,
                            self.get_y() + children['WIDGET'].get_spacing(),
                            self.get_x() + children['WIDGET'].get_spacing()
                        )
                        total_vertical_spacing += children['WIDGET'].get_spacing()
                    # Normal
                    elif 1 <= index <= len(self.get_children())-2:
                        sub_win = self.get_curses_subwin().subwin(
                            devised_box_size - (children['WIDGET'].get_spacing() / 2),
                            self.get_width() - children['WIDGET'].get_spacing() * 2,
                            self.get_y() + (devised_box_size * index) + (children['WIDGET'].get_spacing() / 2),
                            self.get_x() + children['WIDGET'].get_spacing()
                        )
                        total_vertical_spacing += children['WIDGET'].get_spacing() / 2
                    # Check if that the last element
                    else:
                        last_element_vertical_size = self.get_height()
                        last_element_vertical_size -= (devised_box_size * index)
                        last_element_vertical_size -= total_vertical_spacing
                        try:
                            sub_win = self.get_curses_subwin().subwin(
                                    last_element_vertical_size,
                                    self.get_width() - children['WIDGET'].get_spacing() * 2,
                                    self.get_y() + (devised_box_size * index),
                                    self.get_x() + children['WIDGET'].get_spacing()
                            )
                        except curses.error:
                            pass
                    index += 1

                    # Drawing
                    children['WIDGET'].set_curses_subwin(sub_win)
                    children['WIDGET'].draw_widget_in_area()
