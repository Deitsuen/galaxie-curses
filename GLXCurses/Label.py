#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
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
        self.name = 'Label'

        # Internal Widget Setting
        self.text = ''

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
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()

        drawing_area = self.parent.widget.subwin(
                parent_height - (self.get_spacing() * 2),
                parent_width - (self.get_spacing() * 2),
                parent_y + self.get_spacing(),
                parent_x + self.get_spacing()
        )

        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):
        self.widget = drawing_area

        widget_height, widget_width = drawing_area.getmaxyx()
        min_size_width = (self.get_spacing() * 2) + self.get_spacing()
        min_size_height = (self.get_spacing() * 2)
        if (widget_height >= min_size_height) and (widget_width >= min_size_width):
            if self.get_text():
                # Check if the text can be display
                text_have_necessary_width = (self.preferred_width + self.get_spacing() >= 1)
                text_have_necessary_height = (self.preferred_height + self.get_spacing() >= 1)
                if text_have_necessary_width and text_have_necessary_height:

                    # Orientation: HORIZONTAL, VERTICAL
                    if self.get_orientation().upper() == 'HORIZONTAL':
                        x_text = self.check_horizontal_justification(widget_width)
                        y_text = self.check_horizontal_position_type(widget_height)
                        self.draw_horizontal(widget_width, x_text, y_text)

                    elif self.get_orientation().upper() == 'VERTICAL':
                        x_text = self.check_vertical_justification(widget_width)
                        y_text = self.check_vertical_position_type(widget_height)
                        self.draw_vertical(widget_height, x_text, y_text)

    def check_vertical_justification(self, widget_width):
        # Check Justification
        if self.get_justify().upper() == 'CENTER':
            x_text = (widget_width - self.get_spacing() / 2) - (self.preferred_width - self.get_spacing() / 2)
        elif self.get_justify().upper() == 'LEFT':
            x_text = 0 + self.get_spacing()
        elif self.get_justify().upper() == 'RIGHT':
            x_text = widget_width - self.preferred_width - self.get_spacing()

        return x_text

    def check_vertical_position_type(self, widget_height):
        # PositionType: CENTER, TOP, BOTTOM
        if self.get_position_type().upper() == 'CENTER':
            # y_text = (widget_height / 2) - (self.preferred_height / 2)
            if (widget_height / 2) > (self.preferred_height / 2):
                y_text = (widget_height / 2) - (self.preferred_height / 2)
            else:
                y_text = 0
        elif self.get_position_type().upper() == 'TOP':
            y_text = 0
        elif self.get_position_type().upper() == 'BOTTOM':
            y_text = widget_height - self.preferred_height
        return y_text

    def check_horizontal_justification(self, widget_width):
        # Check Justification
        x_text = 0
        if self.get_justify().upper() == 'CENTER':
            x_text = (widget_width / 2) - (self.preferred_width / 2)
        elif self.get_justify().upper() == 'LEFT':
            x_text = 0 + self.get_spacing()
        elif self.get_justify().upper() == 'RIGHT':
            x_text = widget_width - self.preferred_width

        return x_text

    def check_horizontal_position_type(self, widget_height):
        # PositionType: CENTER, TOP, BOTTOM
        y_text = 0
        if self.get_position_type().upper() == 'CENTER':
            if (widget_height / 2) > self.preferred_height:
                y_text = (widget_height / 2) - self.preferred_height
            else:
                y_text = 0
        elif self.get_position_type().upper() == 'TOP':
            y_text = 0
        elif self.get_position_type().upper() == 'BOTTOM':
            y_text = widget_height - self.preferred_height

        return y_text

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_vertical(self, widget_height, x_text, y_text):
        # Draw the Vertical Label with Justification and PositionType
        if widget_height - 1 > 2:
            message_to_display = resize_text(self.get_text(), widget_height - 1, '~')
            if len(message_to_display) > 2:
                count = 0
                for CHAR in message_to_display:
                    self.widget.insch(
                        y_text + count,
                        x_text,
                        CHAR,
                        curses.color_pair(self.get_style().get_curses_pairs(
                            fg=self.get_attr('text', 'STATE_NORMAL'),
                            bg=self.get_attr('bg', 'STATE_NORMAL'))
                        )
                    )
                    count += 1

    def draw_horizontal(self, widget_width, x_text, y_text):
        # Draw the Horizontal Label with Justification and PositionType
        message_to_display = resize_text(self.get_text(), widget_width - self.get_spacing(), '~')
        self.widget.insstr(
            y_text,
            x_text,
            message_to_display,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

    # Internal widget functions
    def set_text(self, text):
        self.text = text
        if self.orientation == 'HORIZONTAL':
            self.preferred_width = len(self.get_text())
            self.preferred_height = 1
        elif self.orientation == 'VERTICAL':
            self.preferred_width = 1
            self.preferred_height = len(self.get_text())

    def get_text(self):
        return self.text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = justification

    def get_justify(self):
        return self.justification

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = orientation
        if self.orientation == 'HORIZONTAL':
            self.preferred_width = len(self.get_text())
            self.preferred_height = 1
        elif self.orientation == 'VERTICAL':
            self.preferred_width = 1
            self.preferred_height = len(self.get_text())

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = position_type

    def get_position_type(self):
        return self.position_type



