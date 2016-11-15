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


class Label(Widget):
    def __init__(self):
        Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('Label')

        # Internal Widget Setting
        self.text = ''
        self.text_x = 0
        self.text_y = 0
        
        # Size management
        self.set_preferred_height(1)
        self.update_preferred_sizes()

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

    def draw_widget_in_area(self, drawing_area):
        self.set_curses_subwin(drawing_area)

        min_size_width = (self.get_spacing() * 2) + self.get_spacing()
        min_size_height = (self.get_spacing() * 2)
        if (self.get_height() >= min_size_height) and (self.get_width() >= min_size_width):
            if self.get_text():
                # Check if the text can be display
                text_have_necessary_width = (self.get_preferred_width() + self.get_spacing() >= 1)
                text_have_necessary_height = (self.get_preferred_height() + self.get_spacing() >= 1)
                if text_have_necessary_width and text_have_necessary_height:

                    # Orientation: HORIZONTAL, VERTICAL
                    if self.get_orientation() == 'HORIZONTAL':
                        self.text_x = self.check_horizontal_justification()
                        self.text_y = self.check_horizontal_position_type()
                        self.draw_horizontal_label()

                    elif self.get_orientation() == 'VERTICAL':
                        self.text_x = self.check_vertical_justification()
                        self.text_y = self.check_vertical_position_type()
                        self.draw_vertical_label()

    def check_vertical_justification(self):
        # Check Justification
        if self.get_justify().upper() == 'CENTER':
            self.text_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify().upper() == 'LEFT':
            self.text_x = 0 + self.get_spacing()
        elif self.get_justify().upper() == 'RIGHT':
            self.text_x = self.get_width() - self.get_preferred_width() - self.get_spacing()

        return self.text_x

    def check_vertical_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.text_y = 0
        if self.get_position_type().upper() == 'CENTER':
            if (self.get_height() / 2) > (self.preferred_height / 2):
                self.text_y = (self.get_height() / 2) - (self.get_preferred_height() / 2)
            else:
                self.text_y = 0
        elif self.get_position_type().upper() == 'TOP':
            self.text_y = 0
        elif self.get_position_type().upper() == 'BOTTOM':
            self.text_y = self.get_height() - self.get_preferred_height()
        return self.text_y

    def check_horizontal_justification(self):
        # Check Justification
        self.text_x = 0
        if self.get_justify() == 'CENTER':
            self.text_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == 'LEFT':
            self.text_x = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            self.text_x = self.get_width() - self.get_preferred_width()

        return self.text_x

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.text_y = 0
        if self.get_position_type().upper() == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                self.text_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self.text_y = 0
        elif self.get_position_type() == 'TOP':
            self.text_y = 0
        elif self.get_position_type() == 'BOTTOM':
            self.text_y = self.get_height() - self.get_preferred_height()

        return self.text_y

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_vertical_label(self):
        # Draw the Vertical Label with Justification and PositionType
        if self.get_height() - 1 > 2:
            message_to_display = resize_text(self.get_text(), self.get_height() - (self.get_spacing() * 2), '~')
            if len(message_to_display) > 2:
                increment = 0
                for CHAR in message_to_display:
                    self.get_curses_subwin().insch(
                        self.text_y + increment,
                        self.text_x,
                        CHAR,
                        curses.color_pair(self.get_style().get_curses_pairs(
                            fg=self.get_attr('text', 'STATE_NORMAL'),
                            bg=self.get_attr('bg', 'STATE_NORMAL'))
                        )
                    )
                    increment += 1

    def draw_horizontal_label(self):
        # Draw the Horizontal Label with Justification and PositionType
        message_to_display = resize_text(self.get_text(), self.get_width() - (self.get_spacing() * 2), '~')
        self.get_curses_subwin().addstr(
            self.text_y,
            self.text_x,
            message_to_display,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

    def update_preferred_sizes(self):
        if self.get_text():
            preferred_width = 0
            preferred_height = 0
            if self.get_orientation() == 'VERTICAL':
                preferred_width = 1
                preferred_height += len(self.get_text())
                preferred_height += self.get_spacing() * 2
            else:
                preferred_height = 1
                preferred_width += len(self.get_text())
                preferred_width += self.get_spacing() * 2
            self.set_preferred_height(preferred_height)
            self.set_preferred_width(preferred_width)
        else:
            return

    # Internal curses_subwin functions
    def set_text(self, text):
        self.text = text
        self.update_preferred_sizes()

    def get_text(self):
        return self.text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = str(justification).upper()
        self.update_preferred_sizes()

    def get_justify(self):
        return self.justification

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = str(orientation).upper()
        self.update_preferred_sizes()

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self.update_preferred_sizes()

    def get_position_type(self):
        return self.position_type
