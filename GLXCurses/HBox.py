#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Box

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class HBox(Box):
    """
    :Description:

    The :class:`HBox <GLXCurses.HBox.HBox>` is a container that organizes child widgets into a single row.

    Use the :class:`Box <GLXCurses.Box.Box>`  packing interface to determine the arrangement, spacing, width,
    and alignment of :class:`HBox <GLXCurses.HBox.HBox>` children.

    All children are allocated the same height.
    """

    def destroy(self):
        raise NotImplementedError

    def __init__(self):
        """
        :Attributes Details:

        .. py:attribute:: homogeneous

           TRUE if all children are to be given equal space allotments.

              +---------------+-------------------------------+
              | Type          | :py:data:`bool`               |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | TRUE                          |
              +---------------+-------------------------------+

        .. py:attribute:: spacing

           The number of char to place by default between children.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+
        """

        Box.__init__(self)
        self.set_name('HBox')

        self.preferred_height = 2
        self.preferred_width = 2

        self.homogeneous = True
        self.spacing = 0

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
                for children in self.get_children():

                    # Check if that the first element
                    if index == 0:
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children['WIDGET'].get_spacing() * 2,
                            devised_box_size - children['WIDGET'].get_spacing(),
                            self.get_y() + children['WIDGET'].get_spacing(),
                            self.get_x() + children['WIDGET'].get_spacing()
                        )
                        total_horizontal_spacing += children['WIDGET'].get_spacing()
                    # Normal
                    elif 1 <= index <= len(self.get_children()) - 2:
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children['WIDGET'].get_spacing() * 2,
                            devised_box_size - (children['WIDGET'].get_spacing() / 2),
                            self.get_y() + children['WIDGET'].get_spacing(),
                            self.get_x() + (devised_box_size * index) + (children['WIDGET'].get_spacing() / 2)
                        )
                        total_horizontal_spacing += children['WIDGET'].get_spacing() / 2
                    else:
                        # Check if that the last element
                        last_element_horizontal_size = self.get_width()
                        last_element_horizontal_size -= (devised_box_size * index)
                        last_element_horizontal_size -= total_horizontal_spacing
                        last_element_horizontal_size -= children['WIDGET'].get_spacing()
                        sub_win = self.get_curses_subwin().subwin(
                            self.get_height() - children['WIDGET'].get_spacing() * 2,
                            last_element_horizontal_size,
                            self.get_y() + children['WIDGET'].get_spacing(),
                            self.get_x() + (devised_box_size * index) + (children['WIDGET'].get_spacing() / 2)
                        )

                    index += 1

                    # Drawing
                    children['WIDGET'].set_curses_subwin(sub_win)
                    children['WIDGET'].draw_widget_in_area()
