#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import logging
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
        # Widgets can be named, which allows you to refer to them from a GLXCStyle

        self.set_name('Button')
        self.set_can_focus(1)
        self.set_can_default(1)
        # Internal Widget Setting
        self.text = None
        self.label_x = 0
        self.label_y = 0

        # Interface
        self.interface = '[  ]'
        self.interface_selected = '[<  >]'
        self.button_border = self.interface

        # Size management
        self.set_preferred_height(1)
        self.update_preferred_sizes()

        # States
        self.curses_mouse_states = {
            curses.BUTTON1_PRESSED: 'BUTTON1_PRESS',
            curses.BUTTON1_RELEASED: 'BUTTON1_RELEASED',
            curses.BUTTON1_CLICKED: 'BUTTON1_CLICKED',
            curses.BUTTON1_DOUBLE_CLICKED: 'BUTTON1_DOUBLE_CLICKED',
            curses.BUTTON1_TRIPLE_CLICKED: 'BUTTON1_TRIPLE_CLICKED',

            curses.BUTTON2_PRESSED: 'BUTTON2_PRESSED',
            curses.BUTTON2_RELEASED: 'BUTTON2_RELEASED',
            curses.BUTTON2_CLICKED: 'BUTTON2_CLICKED',
            curses.BUTTON2_DOUBLE_CLICKED: 'BUTTON2_DOUBLE_CLICKED',
            curses.BUTTON2_TRIPLE_CLICKED: 'BUTTON2_TRIPLE_CLICKED',

            curses.BUTTON3_PRESSED: 'BUTTON3_PRESSED',
            curses.BUTTON3_RELEASED: 'BUTTON3_RELEASED',
            curses.BUTTON3_CLICKED: 'BUTTON3_CLICKED',
            curses.BUTTON3_DOUBLE_CLICKED: 'BUTTON3_DOUBLE_CLICKED',
            curses.BUTTON3_TRIPLE_CLICKED: 'BUTTON3_TRIPLE_CLICKED',

            curses.BUTTON4_PRESSED: 'BUTTON4_PRESSED',
            curses.BUTTON4_RELEASED: 'BUTTON4_RELEASED',
            curses.BUTTON4_CLICKED: 'BUTTON4_CLICKED',
            curses.BUTTON4_DOUBLE_CLICKED: 'BUTTON4_DOUBLE_CLICKED',
            curses.BUTTON4_TRIPLE_CLICKED: 'BUTTON4_TRIPLE_CLICKED',

            curses.BUTTON_SHIFT: 'BUTTON_SHIFT',
            curses.BUTTON_CTRL: 'BUTTON_CTRL',
            curses.BUTTON_ALT: 'BUTTON_ALT'
        }

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

        # Sensitive
        self.set_sensitive(1)
        self.states_list = None

        self.subscribe('MOUSE_EVENT', Button._handle_mouse_event)

    def _handle_mouse_event(self, event_signal, event_args):
        if self.get_sensitive():
            (mouse_event_id, x, y, z, event) = event_args
            y -= self.y
            x -= self.x

            if self.is_my_click(event_args[1], event_args[2]):
                #logging.debug(self.__class__.__name__ + ': ' + '_handle_mouse_event ==> click is for me')
                self.states_list = '; '.join(state_string for state, state_string
                                             in self.curses_mouse_states.viewitems()
                                             if event & state)

                if event in [curses.BUTTON1_PRESSED,
                             curses.BUTTON2_PRESSED,
                             curses.BUTTON3_PRESSED,
                             curses.BUTTON4_PRESSED]:
                    self._check_selected()
                    self._set_state_prelight(True)

                if event in [curses.BUTTON1_RELEASED,
                             curses.BUTTON2_RELEASED,
                             curses.BUTTON3_RELEASED,
                             curses.BUTTON4_RELEASED]:
                    self.get_application().emit('BUTTON_CLICKED', [self.get_name()])
                    self._set_state_prelight(False)
                    self.get_application().set_is_focus(self.id)

                if event in [curses.BUTTON1_CLICKED,
                             curses.BUTTON2_CLICKED,
                             curses.BUTTON3_CLICKED,
                             curses.BUTTON4_CLICKED]:
                    self.get_application().emit('BUTTON_CLICKED', [self.get_name()])
                    self._set_state_prelight(False)
                    self.get_application().set_is_focus(self.id)
            else:
                self._set_state_prelight(False)
        else:
            logging.debug(self.__class__.__name__ + ': ' + self.get_name() + ' is not sensitive.')

    def update_preferred_sizes(self):
        if self.get_text():
            self.preferred_width = 0
            self.preferred_width += len(self.get_text())
            self.preferred_width += len(self.button_border)
            self.preferred_width += self.get_spacing() * 2

    def draw_widget_in_area(self):

        # Many Thing's
        # Check if the text can be display
        text_have_necessary_width = (self.get_preferred_width() >= 1)
        text_have_necessary_height = (self.get_preferred_height() >= 1)
        if not text_have_necessary_height or not text_have_necessary_width:
            return

        if self.get_text():

            # Check if the text can be display
            text_have_necessary_width = (self.get_preferred_width() >= 1)
            text_have_necessary_height = (self.get_preferred_height() >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                self.draw_button()

    def check_horizontal_justification(self):
        # Check Justification
        self.label_x = 0
        if self.get_justify() == 'CENTER':
            self.label_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == 'LEFT':
            self.label_x = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            self.label_x = self.get_width() - self.get_preferred_width()

        return self.label_x

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.label_y = 0
        if self.get_position_type() == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                self.label_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self.label_y = 0
        elif self.get_position_type() == 'TOP':
            self.label_y = 0
        elif self.get_position_type() == 'BOTTOM':
            self.label_y = self.get_height() - self.get_preferred_height()

        return self.label_y

    def draw_button(self):
        self._check_selected()
        self.update_preferred_sizes()
        self.label_x = self.check_horizontal_justification()
        self.label_y = self.check_horizontal_position_type()

        if not self.get_sensitive():
            self.draw_the_good_button(
                color=curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_style().get_attr('bg', 'STATE_NORMAL'),
                    bg=self.get_style().get_attr('bg', 'STATE_NORMAL'))
                ) | curses.A_BOLD
            )
        elif self.state['PRELIGHT']:
            self.draw_the_good_button(
                color=curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_style().get_attr('dark', 'STATE_NORMAL'),
                    bg=self.get_style().get_attr('bg', 'STATE_PRELIGHT'))
                )
            )
        elif self.state['NORMAL']:
            self.draw_the_good_button(
                color=curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_style().get_attr('text', 'STATE_NORMAL'),
                    bg=self.get_style().get_attr('bg', 'STATE_NORMAL'))
                )
            )

    def draw_the_good_button(self, color):
        try:
            # Interface management
            self.get_curses_subwin().addstr(
                self.label_y,
                self.label_x,
                self.button_border[:len(self.button_border) / 2],
                color
            )
        except curses.error:
            pass
        try:
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_curses_subwin().addstr(
                self.label_y,
                self.label_x + len(self.button_border) / 2,
                message_to_display,
                color
            )
        except curses.error:
            pass
        try:
            # Interface management
            self.get_curses_subwin().insstr(
                self.label_y,
                self.label_x + (len(self.button_border) / 2) + len(message_to_display),
                self.button_border[-len(self.button_border) / 2:],
                color
            )
        except curses.error:
            pass

    def enter(self):
        raise NotImplementedError

    def leave(self):
        raise NotImplementedError

    def key_pressed(self, char):
        if char > 255:
            return 0  # skip control-characters
        # if chr(char).upper() == self.LabelButton[self.Underline]:
        #     return 1
        else:
            return 0

    def is_my_click(self, coord_x=-1, coord_y=-1):
        greatest_x = self.label_x - 1 + len(self.button_border) + len(self.get_text())
        lowest_x = self.label_x - 1

        greatest_y = self.y + self.label_y
        lowest_y = self.y - self.label_y

        x_is_in_range = lowest_x <= coord_x <= greatest_x
        y_is_in_range = lowest_y <= coord_y <= greatest_y

        return x_is_in_range and y_is_in_range

    # Internal Widget functions
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
        return self.states_list

    # Internal
    def get_widget_id(self):
        return self.id

    def _check_selected(self):
        if self.get_can_focus():
            if self.get_application():
                if self.get_application().get_is_focus() == self.id:
                    self.set_is_focus(True)
                    self.button_border = self.interface_selected
                else:
                    self.set_is_focus(False)
                    self.button_border = self.interface
        else:
            pass

    def _set_state_prelight(self, value):
        if bool(value):
            self.state['PRELIGHT'] = True
        else:
            self.state['PRELIGHT'] = False

    def _get_state_prelight(self):
        return self.state['PRELIGHT']
