#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        text_to_return = text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
        if len(text_to_return) == 1:
            text_to_return = text[:1]
        elif len(text_to_return) == 2:
            text_to_return = str(text[:1] + text[-1:])
        elif len(text_to_return) == 3:
            text_to_return = str(text[:1] + separator + text[-1:])
        return text_to_return
    else:
        return text


class VSeparator(Widget):
    def __init__(self):
        Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('VSeparator')

        # Internal Widget Setting
        self.vseperator_x = 0
        self.vseperator_y = self.get_spacing()

        # Size management
        #self.set_preferred_height(1)

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        self.update_preferred_sizes()

    def draw(self):
        parent_height, parent_width = self.get_parent().get_curses_subwin().getmaxyx()
        parent_y, parent_x = self.get_parent().get_curses_subwin().getbegyx()

        min_size_width = (self.get_spacing() * 2) + 1
        min_size_height = (self.get_spacing() * 2) + 1
        height_ok = self.get_parent().get_height() >= min_size_height
        width_ok = self.get_parent().get_width() >= min_size_width
        if not height_ok or not width_ok:
            return

        drawing_area = self.get_parent().get_curses_subwin().subwin(
            parent_height - (self.get_spacing()),
            parent_width - (self.get_spacing() * 2),
            parent_y + self.get_spacing(),
            parent_x + self.get_spacing()
        )

        self.draw_widget_in_area(drawing_area)

    def draw_widget_in_area(self, drawing_area):
        self.set_curses_subwin(drawing_area)

        if (self.get_height() >= 1 + (self.get_spacing() * 2)) and (self.get_width() >= 1 + (self.get_spacing() * 2)):
            self.vseperator_x = self.check_justification()
            self.draw_vertical_separator()

    def check_justification(self):
        # Check Justification
        if self.get_justify() == 'CENTER':
            self.vseperator_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == 'LEFT':
            self.vseperator_x = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            self.vseperator_x = self.get_width() - self.get_preferred_width() - self.get_spacing()
        return self.vseperator_x

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_vertical_separator(self):
        # Draw the Vertical Label with Justification and PositionType
        if self.get_height() >= 1 + (self.get_spacing() * 2):
            increment = 0
            for y in range(self.vseperator_y, self.get_height() - self.get_spacing()):
                self.get_curses_subwin().insch(
                    self.vseperator_y + increment,
                    self.vseperator_x,
                    curses.ACS_VLINE,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('text', 'STATE_NORMAL'),
                        bg=self.get_attr('bg', 'STATE_NORMAL'))
                    )
                )
                increment += 1

    def update_preferred_sizes(self):
        preferred_height = 0
        preferred_width = 1
        preferred_height += self.get_height() - (self.get_spacing() * 2)
        self.set_preferred_height(preferred_height)
        self.set_preferred_width(preferred_width)

    # Internal curses_subwin functions
    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = str(justification).upper()
        self.update_preferred_sizes()

    def get_justify(self):
        return self.justification


