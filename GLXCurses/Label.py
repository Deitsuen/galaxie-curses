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

    def draw(self):
        parent_height, parent_width = self.get_parent().get_size()
        parent_y, parent_x = self.get_parent().get_origin()

        min_size_width = (self.get_spacing() * 2) + 1
        min_size_height = (self.get_spacing() * 2) + 1
        height_ok = self.get_parent().get_height() >= min_size_height
        width_ok = self.get_parent().get_width() >= min_size_width
        if not height_ok or not width_ok:
            return

        drawing_area = self.get_parent().get_widget().subwin(
                parent_height - (self.get_spacing() * 2),
                parent_width - (self.get_spacing() * 2),
                parent_y + self.get_spacing(),
                parent_x + self.get_spacing()
        )

        self.draw_widget_in_area(drawing_area)

    def draw_widget_in_area(self, drawing_area):
        self.set_widget(drawing_area)

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
                        x_text = self.check_horizontal_justification()
                        y_text = self.check_horizontal_position_type()
                        self.draw_horizontal(x_text, y_text)

                    elif self.get_orientation() == 'VERTICAL':
                        x_text = self.check_vertical_justification()
                        y_text = self.check_vertical_position_type()
                        self.draw_vertical(x_text, y_text)

    def check_vertical_justification(self):
        # Check Justification
        if self.get_justify().upper() == 'CENTER':
            x_text = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify().upper() == 'LEFT':
            x_text = 0 + self.get_spacing()
        elif self.get_justify().upper() == 'RIGHT':
            x_text = self.get_width() - self.get_preferred_width() - self.get_spacing()

        return x_text

    def check_vertical_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        y_text = 0
        if self.get_position_type().upper() == 'CENTER':
            # y_text = (widget_height / 2) - (self.preferred_height / 2)
            if (self.get_height() / 2) > (self.preferred_height / 2):
                y_text = (self.get_height() / 2) - (self.get_preferred_height() / 2)
            else:
                y_text = 0
        elif self.get_position_type().upper() == 'TOP':
            y_text = 0
        elif self.get_position_type().upper() == 'BOTTOM':
            y_text = self.get_height() - self.get_preferred_height()
        return y_text

    def check_horizontal_justification(self):
        # Check Justification
        x_text = 0
        if self.get_justify() == 'CENTER':
            x_text = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == 'LEFT':
            x_text = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            x_text = self.get_width() - self.get_preferred_width()

        return x_text

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        y_text = 0
        if self.get_position_type().upper() == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                y_text = (self.get_height() / 2) - self.get_preferred_height()
            else:
                y_text = 0
        elif self.get_position_type() == 'TOP':
            y_text = 0
        elif self.get_position_type() == 'BOTTOM':
            y_text = self.get_height() - self.get_preferred_height()

        return y_text

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_vertical(self, x_text, y_text):
        # Draw the Vertical Label with Justification and PositionType
        if self.get_height() - 1 > 2:
            message_to_display = resize_text(self.get_text(), self.get_height() - (self.get_spacing() * 2), '~')
            if len(message_to_display) > 2:
                increment = 0
                for CHAR in message_to_display:
                    self.get_widget().insch(
                        y_text + increment,
                        x_text,
                        CHAR,
                        curses.color_pair(self.get_style().get_curses_pairs(
                            fg=self.get_attr('text', 'STATE_NORMAL'),
                            bg=self.get_attr('bg', 'STATE_NORMAL'))
                        )
                    )
                    increment += 1

    def draw_horizontal(self, x_text, y_text):
        # Draw the Horizontal Label with Justification and PositionType
        message_to_display = resize_text(self.get_text(), self.get_width() - (self.get_spacing() * 2), '~')
        self.get_widget().addstr(
            y_text,
            x_text,
            message_to_display,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

    def update_preferred_sizes(self):
        if self.get_text():
            if self.get_orientation() == 'VERTICAL':
                self.preferred_width = 1
                self.preferred_height = 0
                self.preferred_height += len(self.get_text())
                self.preferred_height += self.get_spacing() * 2
            else:
                self.preferred_height = 1
                self.preferred_width = 0
                self.preferred_width += len(self.get_text())
                self.preferred_width += self.get_spacing() * 2
        else:
            return

    # Internal widget functions
    def set_text(self, text):
        self.text = text
        if self.get_orientation() == 'HORIZONTAL':
            self.set_preferred_width(len(self.get_text()) + (self.get_spacing() * 2))
            self.set_preferred_height(1)
        elif self.get_orientation() == 'VERTICAL':
            self.set_preferred_width(1)
            self.set_preferred_height(len(self.get_text()) + (self.get_spacing() * 2))
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
        if self.get_orientation() == 'HORIZONTAL':
            self.set_preferred_width(len(self.get_text()) + (self.get_spacing() * 2))
            self.set_preferred_height(1)
        elif self.get_orientation() == 'VERTICAL':
            self.set_preferred_width(1)
            self.set_preferred_height(len(self.get_text()) + (self.get_spacing() * 2))
        self.update_preferred_sizes()

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self.update_preferred_sizes()

    def get_position_type(self):
        return self.position_type



