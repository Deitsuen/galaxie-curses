#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import curses
from GLXCurses import glxc

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class HSeparator(GLXCurses.Widget):
    def __init__(self):
        """
        The GLXCurses.HSeparator widget is a horizontal separator, used to visibly separate the widgets within a \
        window. It displays a horizontal line.

        :Property's Details:

        .. py:data:: name

            The widget can be named, which allows you to refer to them from a GLXCurses.Style

              +---------------+-------------------------------+
              | Type          | :py:data:`str`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | HSeparator                    |
              +---------------+-------------------------------+

        .. py:data:: set_preferred_height

            Size management

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 1                             |
              +---------------+-------------------------------+

        .. py:data:: position_type

            PositionType: CENTER, TOP, BOTTOM

              +---------------+-------------------------------+
              | Type          | :py:data:`PositionType`       |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | CENTER                        |
              +---------------+-------------------------------+

        """

        GLXCurses.Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('HSeparator')

        # Size management
        self.set_preferred_height(1)

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = glxc.BASELINE_POSITION_CENTER

        # Internal Widget Setting
        self._hseperator_x = 0
        self._hseperator_y = 0

        # Make a Style heritage attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

    def draw_widget_in_area(self):
        self.set_preferred_width(self._get_estimated_preferred_width())
        self.set_preferred_height(self._get_estimated_preferred_height())
        self.check_horizontal_position_type()
        if (self.get_height() >= self.get_preferred_height()) and (self.get_width() >= self.get_preferred_width()):
            self.draw_horizontal_separator()

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self._hseperator_y = 0
        if self.get_position_type() == glxc.BASELINE_POSITION_CENTER:
            if (self.get_height() / 2) > self.get_preferred_height():
                self._hseperator_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self._hseperator_y = 0
        elif self.get_position_type() == glxc.BASELINE_POSITION_TOP:
            self._hseperator_y = 0
        elif self.get_position_type() == glxc.BASELINE_POSITION_BOTTOM:
            self._hseperator_y = self.get_height() - self.get_preferred_height()

    def draw_horizontal_separator(self):
        # Draw the Horizontal Separator with PositionType
        for x in range(self.get_x(), self.get_width()):
            self.get_curses_subwin().insch(
                self._hseperator_y,
                self._hseperator_x + x,
                curses.ACS_HLINE,
                self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_by_attribute_state('base', 'STATE_NORMAL'),
                    background=self.get_style().get_color_by_attribute_state('bg', 'STATE_NORMAL')
                )
            )

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self.set_preferred_width(self._get_estimated_preferred_width())
        self.set_preferred_height(self._get_estimated_preferred_height())

    def get_position_type(self):
        return self.position_type

    # Internal
    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width and spacing

        :return: a estimated preferred width
        :rtype: int
        """
        estimated_preferred_width = self.get_x()
        estimated_preferred_width += self.get_width()
        estimated_preferred_width += self.get_spacing() * 2
        return estimated_preferred_width

    def _get_estimated_preferred_height(self):
        """
        Estimate a preferred height, by consider Y Location, and spacing

        :return: a estimated preferred height
        :rtype: int
        """
        estimated_preferred_height = 1
        estimated_preferred_height += self.get_spacing() * 2
        return estimated_preferred_height
