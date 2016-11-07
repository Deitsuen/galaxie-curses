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


class Button(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'Button'

        # Internal Widget Setting
        self.text = None
        # Interface
        self.button_border = '[  ]'
        self.button_border_selected = '[<  >]'
        # Size management
        self.preferred_height = 1
        if self.get_text():
            self.preferred_width = 0
            self.preferred_width += len(self.get_text())
            self.preferred_width += len(self.button_border) / 2
            self.preferred_width += self.get_spacing() * 2

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

        drawing_area = self.get_parent().widget.subwin(
                parent_height - (self.get_spacing() * 2),
                parent_width - (self.get_spacing() * 2),
                parent_y + self.get_spacing(),
                parent_x + self.get_spacing()
        )

        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):
        self.widget = drawing_area

        self.height, self.width = self.get_size()
        min_size_width = (self.get_spacing() * 2) + self.get_spacing()
        min_size_height = (self.get_spacing() * 2)
        height_ok = self.get_height() >= min_size_height
        width_ok = self.get_width() >= min_size_width
        if not height_ok or not width_ok:
            return

        # Many Thing's
        # Check if the text can be display
        text_have_necessary_width = (self.get_preferred_width() >= 1)
        text_have_necessary_height = (self.get_preferred_height() >= 1)
        if not text_have_necessary_height or not text_have_necessary_width:
            return

        if self.get_text():

            # Check if the text can be display
            text_have_necessary_width = (self.preferred_width >= 1)
            text_have_necessary_height = (self.preferred_height >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                x_text = self.check_horizontal_justification()
                y_text = self.check_horizontal_position_type()
                self.draw_button(x_text, y_text)

    def check_horizontal_justification(self):
        # Check Justification
        x_text = 0
        if self.get_justify().upper() == 'CENTER':
            x_text = (self.get_width() / 2) - (self.get_preferred_width() / 2) - (len(self.button_border)/2)
        elif self.get_justify().upper() == 'LEFT':
            x_text = 0 + self.get_spacing()
        elif self.get_justify().upper() == 'RIGHT':
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
        elif self.get_position_type().upper() == 'TOP':
            y_text = 0
        elif self.get_position_type().upper() == 'BOTTOM':
            y_text = self.get_height() - self.get_preferred_height()

        return y_text

    def draw_button(self, x_text, y_text):
        # Interface management
        self.widget.addstr(
            y_text,
            x_text,
            self.button_border[:len(self.button_border) / 2],
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('base', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        # Draw the Horizontal Button with Justification and PositionType
        message_to_display = resize_text(self.get_text(), self.get_width(), '~')
        self.widget.addstr(
            y_text,
            x_text + len(self.button_border) / 2,
            message_to_display,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        # Interface management
        self.widget.insstr(
            y_text,
            x_text + (len(self.button_border) / 2) + len(message_to_display),
            self.button_border[-len(self.button_border) / 2:],
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('base', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def select(self):
        self.widget.addstr(
            self.Y + 1,
            self.X + 1,
            self.LabelButton,
            curses.color_pair(1)
        )
        self.widget.addstr(
            self.Y + 1,
            self.X + self.Underline + 1,
            self.LabelButton[self.Underline],
            curses.A_REVERSE | curses.color_pair(3)
        )
        self.widget.move(
            self.Y + 1,
            self.X + self.Underline + 1
        )
        self.Selected = 1

    def unselected(self):
        self.widget.addstr(
            self.Y + 1,
            self.X + 1,
            self.LabelButton,
            curses.color_pair(4)
        )
        self.widget.addstr(
            self.Y + 1,
            self.X + self.Underline + 1,
            self.LabelButton[self.Underline],
            curses.A_REVERSE | curses.color_pair(3)
        )
        self.Selected = 0

    def state(self):
        if self.Selected:
            return 1
        else:
            return 0

    def key_pressed(self, char):
        if char > 255:
            return 0  # skip control-characters
        if chr(char).upper() == self.LabelButton[self.Underline]:
            return 1
        else:
            return 0

    def mouse_clicked(self, mouse_event):
        (mouse_event_id, x, y, z, event) = mouse_event
        if (self.YParent + 3) <= y <= (self.YParent + 3):
            if self.X + self.XParent <= x < (self.X + self.XParent + self.Width - 1):
                return 1
        else:
            return 0


    # Internal widget functions
    def set_text(self, text):
        self.text = text
        self.preferred_width = len(self.get_text())

    def get_text(self):
        return self.text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = justification

    def get_justify(self):
        return self.justification

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = position_type

    def get_position_type(self):
        return self.position_type
