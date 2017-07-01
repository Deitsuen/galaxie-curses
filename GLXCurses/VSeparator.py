#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Widget
from GLXCurses import glxc
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class VSeparator(Widget):
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

        .. py:data:: Justify

            Justify: CENTER, LEFT, RIGHT

              +---------------+-------------------------------+
              | Type          | :py:data:`Justify`            |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | CENTER                        |
              +---------------+-------------------------------+

        """
        # Load heritage
        Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.VSeparator'

        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('VSeparator')

        # Make a Widget Style heritage attribute as local attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

        # Size management
        self.set_preferred_width(1)

        # Justification: LEFT, RIGHT, CENTER
        self.justify = glxc.JUSTIFY_CENTER

        # Internal Widget Setting
        self._vseperator_x = 0
        self._vseperator_y = 0

    def draw_widget_in_area(self):
        self.set_preferred_width(self._get_estimated_preferred_width())
        self.set_preferred_height(self._get_estimated_preferred_height())
        self._check_justification()
        if self.get_height() >= 1 + (self.get_spacing() * 2):
            if self.get_width() >= 1 + (self.get_spacing() * 2):
                self._draw_vertical_separator()

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justify):
        allowed_value = [glxc.JUSTIFY_LEFT, glxc.JUSTIFY_CENTER, glxc.JUSTIFY_RIGHT]
        if justify in allowed_value:
            self.justify = str(justify).upper()
            self.set_preferred_width(self._get_estimated_preferred_width())
            self.set_preferred_height(self._get_estimated_preferred_height())
        else:
            raise TypeError(u'PositionType must be LEFT or CENTER or RIGHT')

    def get_justify(self):
        return self.justify

    # Internal
    def _check_justification(self):
        """Check the justification of the X axe"""
        if self.get_justify() == glxc.JUSTIFY_CENTER:
            self._set_vseperator_x((self.get_width() / 2) - (self.get_preferred_width() / 2))
        elif self.get_justify() == glxc.JUSTIFY_LEFT:
            self._set_vseperator_x(0 + self.get_spacing())
        elif self.get_justify() == glxc.JUSTIFY_RIGHT:
            self._set_vseperator_x(self.get_width() - self.get_preferred_width() - self.get_spacing())

    def _draw_vertical_separator(self):
        """Draw the Vertical Label with Justification and PositionType"""
        if self.get_height() >= 1 + (self.get_spacing() * 2):
            for y in range(self._get_vseperator_y(), self.get_height() - self.get_spacing()):
                self.get_curses_subwin().insch(
                    int(self._get_vseperator_y() + y),
                    int(self._get_vseperator_x()),
                    curses.ACS_VLINE,
                    self.get_style().get_color_pair(
                        foreground=self.get_style().get_color_text('text', 'STATE_NORMAL'),
                        background=self.get_style().get_color_text('bg', 'STATE_NORMAL')
                    )
                )

    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width and spacing

        :return: a estimated preferred width
        :rtype: int
        """
        estimated_preferred_width = 1
        estimated_preferred_width += self.get_spacing() * 2
        return estimated_preferred_width

    def _get_estimated_preferred_height(self):
        """
        Estimate a preferred height, by consider Y Location, and spacing

        :return: a estimated preferred height
        :rtype: int
        """
        estimated_preferred_height = self.get_y()
        estimated_preferred_height += self.get_height()
        estimated_preferred_height += self.get_spacing() * 2
        return estimated_preferred_height

    def _set_vseperator_x(self, number):
        """
        Set the Vertical Axe Separator

        :param number: the new value of vseperator_x
        :type number: int
        """
        if type(number) == int:
            if self._get_vseperator_x() != number:
                self._vseperator_x = number
        else:
            raise TypeError(u'>number< is not a int type')

    def _get_vseperator_x(self):
        """
        Return Vertical Axe Separator

        :return: vseperator_x
        :rtype: int
        """
        return self._vseperator_x

    def _set_vseperator_y(self, number):
        """
        Set the Horizontal Axe Separator

        :param number: the new value of vseperator_x
        :type number: int
        """
        if type(number) == int:
            if self._get_vseperator_y() != number:
                self._vseperator_y = number
        else:
            raise TypeError(u'>number< is not a int type')

    def _get_vseperator_y(self):
        """
        Return Horizontal Axe Separator

        :return: vseperator_x
        :rtype: int
        """
        return self._vseperator_y
