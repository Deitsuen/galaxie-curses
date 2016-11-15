#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class HSeparator(Widget):
    def __init__(self):
        Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('HSeparator')

        # Internal Widget Setting
        self.hseperator_x = 0
        self.hseperator_y = 0
        
        # Size management
        self.set_preferred_height(1)

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

    def draw_widget_in_area(self, drawing_area):
        self.set_curses_subwin(drawing_area)
        self.update_preferred_sizes()
        self.check_horizontal_position_type()
        if (self.get_height() >= self.get_preferred_height()) and (self.get_width() >= self.get_preferred_width()):
            self.draw_horizontal_separator()

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.hseperator_y = 0
        if self.get_position_type() == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                self.hseperator_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self.hseperator_y = 0
        elif self.get_position_type() == 'TOP':
            self.hseperator_y = 0
        elif self.get_position_type() == 'BOTTOM':
            self.hseperator_y = self.get_height() - self.get_preferred_height()

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_horizontal_separator(self):
        # Draw the Horizontal Separator with PositionType
        for x in range(self.get_x(), self.get_width()):
            self.get_curses_subwin().insch(
                self.hseperator_y,
                self.hseperator_x + x,
                curses.ACS_HLINE,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )

    def update_preferred_sizes(self):
        preferred_width = self.get_x()
        preferred_height = 1 + self.get_spacing() * 2
        preferred_width += self.get_width()
        preferred_width += self.get_spacing() * 2
        self.set_preferred_height(preferred_height)
        self.set_preferred_width(preferred_width)

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self.update_preferred_sizes()

    def get_position_type(self):
        return self.position_type
