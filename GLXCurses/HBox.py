#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Box

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class HBox(Box):
    def destroy(self):
        raise NotImplementedError

    def __init__(self):
        Box.__init__(self)
        self.set_name('HBox')

        self.preferred_height = 2
        self.preferred_width = 2

    # GLXC HBox Functions called by GLXCurse.Widget.draw()
    def draw_widget_in_area(self):

        # Check widgets to display
        is_large_enough = (self.get_width() > 2)
        is_high_enough = (self.get_height() > 2)

        if is_high_enough and is_large_enough:
            if self.get_children():
                devised_box_size = int(self.get_width() / len(self.get_children()))
                index = 0
                total_horizontal_spacing = 0
                for children_info in self.get_children():
                    # Check if that the first element
                    if index == 0:
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children_info['WIDGET'].get_spacing() * 2,
                            devised_box_size - children_info['WIDGET'].get_spacing(),
                            self.get_y() + children_info['WIDGET'].get_spacing(),
                            self.get_x() + children_info['WIDGET'].get_spacing()
                        )
                        total_horizontal_spacing += children_info['WIDGET'].get_spacing()
                    # Normal
                    elif 1 <= index <= len(self.get_children()) - 2:
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children_info['WIDGET'].get_spacing() * 2,
                            devised_box_size - (children_info['WIDGET'].get_spacing() / 2),
                            self.get_y() + children_info['WIDGET'].get_spacing(),
                            self.get_x() + (devised_box_size * index) + (children_info['WIDGET'].get_spacing() / 2)
                        )
                        total_horizontal_spacing += children_info['WIDGET'].get_spacing() / 2
                    else:
                        # Check if that the last element
                        last_element_horizontal_size = self.get_width()
                        last_element_horizontal_size -= (devised_box_size * index)
                        last_element_horizontal_size -= total_horizontal_spacing
                        last_element_horizontal_size -= children_info['WIDGET'].get_spacing()
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children_info['WIDGET'].get_spacing() * 2,
                            last_element_horizontal_size,
                            self.get_y() + children_info['WIDGET'].get_spacing(),
                            self.get_x() + (devised_box_size * index) + (children_info['WIDGET'].get_spacing() / 2)
                        )

                    index += 1

                    # Drawing
                    children_info['WIDGET'].set_curses_subwin(sub_win)
                    children_info['WIDGET'].draw_widget_in_area()
