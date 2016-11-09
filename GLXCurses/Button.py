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


class Button(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'Button'

        # Internal Widget Setting
        self.text = None
        self.text_x = 0
        self.text_y = 0

        # Interface
        self.button_border = '[  ]'
        self.button_border_selected = '[<  >]'
        # Size management
        self.preferred_height = 1
        if self.get_text():
            self.preferred_width = 0
            self.preferred_width += len(self.get_text())
            self.preferred_width += len(self.button_border)
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

        # State
        self.state['NORMAL'] = True
        self.state['ACTIVE'] = False
        self.state['PRELIGHT'] = False
        self.state['SELECTED'] = False
        self.state['INSENSITIVE'] = False

        self.states = None

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
        self.set_widget(drawing_area)

        min_size_width = (self.get_spacing() * 2) + 3
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
                self.text_x = self.check_horizontal_justification()
                self.text_y = self.check_horizontal_position_type()
                self.draw_button()

    def check_horizontal_justification(self):
        # Check Justification
        self.text_x = 0
        if self.get_justify() == 'CENTER':
            self.text_x = (self.get_width() / 2) - (self.get_preferred_width() / 2) - (len(self.button_border) / 2)
        elif self.get_justify() == 'LEFT':
            self.text_x = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            self.text_x = self.get_width() - self.get_preferred_width()

        return self.text_x

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.text_y = 0
        if self.get_position_type() == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                self.text_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self.text_y = 0
        elif self.get_position_type() == 'TOP':
            self.text_y = 0
        elif self.get_position_type() == 'BOTTOM':
            self.text_y = self.get_height() - self.get_preferred_height()

        return self.text_y

    def draw_button(self):
        if self.state['PRELIGHT']:
            self.prelight()
        elif self.state['NORMAL']:
            self.normal()

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def normal(self):
        # Interface management
        if self.state['SELECTED']:
            # Interface management
            self.get_widget().addstr(
                self.text_y,
                self.text_x,
                self.button_border_selected[:len(self.button_border_selected) / 2],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_widget().addstr(
                self.text_y,
                self.text_x + len(self.button_border_selected) / 2,
                message_to_display,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('text', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
            # Interface management
            self.get_widget().insstr(
                self.text_y,
                self.text_x + (len(self.button_border_selected) / 2) + len(message_to_display),
                self.button_border_selected[-len(self.button_border_selected) / 2:],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
        else:
            # Interface management
            self.get_widget().addstr(
                self.text_y,
                self.text_x,
                self.button_border[:len(self.button_border) / 2],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_widget().addstr(
                self.text_y,
                self.text_x + len(self.button_border) / 2,
                message_to_display,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('text', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
            # Interface management
            self.get_widget().insstr(
                self.text_y,
                self.text_x + (len(self.button_border) / 2) + len(message_to_display),
                self.button_border[-len(self.button_border) / 2:],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )

    def prelight(self):
        # Interface management
        if self.state['SELECTED']:
            # Interface management
            self.get_widget().addstr(
                self.text_y,
                self.text_x,
                self.button_border_selected[:len(self.button_border_selected) / 2],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_widget().addstr(
                self.text_y,
                self.text_x + len(self.button_border_selected) / 2,
                message_to_display,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
            # Interface management
            self.get_widget().insstr(
                self.text_y,
                self.text_x + (len(self.button_border_selected) / 2) + len(message_to_display),
                self.button_border_selected[-len(self.button_border_selected) / 2:],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
        else:
            # Interface management
            self.get_widget().addstr(
                self.text_y,
                self.text_x,
                self.button_border[:len(self.button_border) / 2],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_widget().addstr(
                self.text_y,
                self.text_x + len(self.button_border) / 2,
                message_to_display,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
            # Interface management
            self.get_widget().insstr(
                self.text_y,
                self.text_x + (len(self.button_border) / 2) + len(message_to_display),
                self.button_border[-len(self.button_border) / 2:],
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_PRELIGHT'))
                )
            )



    def enter(self):
        pass

    def leave(self):
        pass

    def key_pressed(self, char):
        if char > 255:
            return 0  # skip control-characters
        # if chr(char).upper() == self.LabelButton[self.Underline]:
        #     return 1
        else:
            return 0

    def mouse_event(self, mouse_event):
        # Read the mouse event information's
        (mouse_event_id, x, y, z, event) = mouse_event
        # Be sure we select really the Button
        if self.text_y + self.get_preferred_height() >= y >= self.text_y + self.get_preferred_height():
            if self.text_x <= x <= self.text_x + len(self.button_border) + len(self.get_text()) - 1:
                # We are sure about the button have been clicked
                #
                self.states = '; '.join(state_string for state, state_string
                                        in self.curses_mouse_states.viewitems()
                                        if event & state)
                if event == curses.BUTTON1_PRESSED:
                    self.state['SELECTED'] = True
                    self.state['PRELIGHT'] = True
                    self.state['NORMAL'] = False
                if event == curses.BUTTON1_RELEASED:
                    self.state['PRELIGHT'] = False
                    self.state['NORMAL'] = True
                return 1
        else:
            self.state['PRELIGHT'] = False
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

    # State
    def get_states(self):
        return self.states
