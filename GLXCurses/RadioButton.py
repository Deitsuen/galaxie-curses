#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import curses

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


class RadioButton(GLXCurses.Widget):
    def __init__(self):
        GLXCurses.Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle

        self.set_name('RadioButton')
        self.set_can_focus(1)
        self.set_can_default(1)
        # Internal Widget Setting
        self.text = None
        self.label_x = 0
        self.label_y = 0

        # Interface
        self.interface_unactivated = '( ) '
        self.interface_active = '(*) '
        self.interface = self.interface_unactivated

        # Size management
        self.set_preferred_height(1)
        self.update_preferred_sizes()

        # Make a Style heritage attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

        # Sensitive
        self.set_sensitive(1)
        self.set_can_focus(1)
        self.set_is_focus(1)
        self.states_list = None

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

        # Subscibtion
        self.subscribe('MOUSE_EVENT', RadioButton._handle_mouse_event)

    def update_preferred_sizes(self):
        if self.get_text():
            self.preferred_width = 0
            self.preferred_width += len(self.get_text())
            self.preferred_width += len(self.interface)
            self.preferred_width += self.get_spacing() * 2

    def draw_widget_in_area(self):
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

    def check_justification(self):
        # Check Justification
        self.label_x = 0
        if self.get_justify() == 'CENTER':
            self.label_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == 'LEFT':
            self.label_x = 0 + self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            self.label_x = self.get_width() - self.get_preferred_width()

        return self.label_x

    def check_position_type(self):
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

    def set_active(self, boolean):
        self.state['ACTIVE'] = bool(boolean)
        self._check_active()

    def get_active(self):
        self._check_active()
        return self.state['ACTIVE']

    def draw_button(self):
        self._check_active()
        self.update_preferred_sizes()
        self.label_x = self.check_justification()
        self.label_y = self.check_position_type()

        if not self.get_sensitive():
            self.draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_by_attribute_state('bg', 'STATE_NORMAL'),
                    background=self.get_style().get_color_by_attribute_state('bg', 'STATE_NORMAL')
                )
            )
        elif self.state['PRELIGHT']:
            self.draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_by_attribute_state('dark', 'STATE_NORMAL'),
                    background=self.get_style().get_color_by_attribute_state('bg', 'STATE_PRELIGHT')
                )
            )
        elif self.state['NORMAL']:
            self.draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_by_attribute_state('text', 'STATE_NORMAL'),
                    background=self.get_style().get_color_by_attribute_state('bg', 'STATE_NORMAL')
                )
            )

    def draw_the_good_button(self, color):
        # Interface management
        try:
            self.get_curses_subwin().addstr(
                self.label_y,
                self.label_x,
                self.interface,
                color
            )
        except curses.error:
            pass
        try:
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width(), '~')
            self.get_curses_subwin().addstr(
                self.label_y,
                self.label_x + len(self.interface),
                message_to_display,
                color
            )
        except curses.error:
            pass

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

    def _handle_mouse_event(self, event_signal, event_args):
        if self.get_sensitive():
            # Read the mouse event information's
            (mouse_event_id, x, y, z, event) = event_args
            # Be sure we select really the Button
            y -= self.y
            x -= self.x
            if self.label_y >= y > self.label_y - self.get_preferred_height():
                if (self.label_x - 1) + len(self.interface) + len(self.get_text()) >= x > (self.label_x - 1):
                    # We are sure about the button have been clicked
                    self.states_list = '; '.join(state_string for state, state_string
                                                 in self.curses_mouse_states.viewitems()
                                                 if event & state)
                    # INTERNAL METHOD
                    # BUTTON1
                    if event == curses.BUTTON1_PRESSED:
                        GLXCurses.application.set_is_focus(self)
                        self._check_active()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON1_RELEASED:
                        GLXCurses.application.set_is_focus(self)
                        self._check_active()
                        self.set_active(not self.get_active())
                        self._set_state_prelight(False)
                    if event == curses.BUTTON1_CLICKED:
                        self.set_active(not self.get_active())
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON1_DOUBLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON1_TRIPLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)

                    # BUTTON2
                    if event == curses.BUTTON2_PRESSED:
                        GLXCurses.application.set_is_focus(self)
                        self._check_active()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON2_RELEASED:
                        self._set_state_prelight(False)
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON2_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON2_DOUBLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON2_TRIPLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)

                    # BUTTON3
                    if event == curses.BUTTON3_PRESSED:
                        GLXCurses.application.set_is_focus(self)
                        self._check_active()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON3_RELEASED:
                        self._set_state_prelight(False)
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON3_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON3_DOUBLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON3_TRIPLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)

                    # BUTTON4
                    if event == curses.BUTTON4_PRESSED:
                        GLXCurses.application.set_is_focus(self)
                        self._check_active()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON4_RELEASED:
                        self._set_state_prelight(False)
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON4_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON4_DOUBLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)
                    if event == curses.BUTTON4_TRIPLE_CLICKED:
                        GLXCurses.application.set_is_focus(self)

                    if event == curses.BUTTON_SHIFT:
                        pass
                    if event == curses.BUTTON_CTRL:
                        pass
                    if event == curses.BUTTON_ALT:
                        pass

                    # Create a Dict with everything
                    instance = {
                        'class': self.__class__.__name__,
                        'label': self.get_text(),
                        'id': self.get_widget_id()
                    }
                    # EVENT EMIT
                    GLXCurses.application.emit(self.curses_mouse_states[event], instance)
            else:
                self.state['PRELIGHT'] = False
                return 0

    # Internal curses_subwin functions
    def set_text(self, text):
        self.text = text
        self.update_preferred_sizes()

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

    def _check_active(self):
        if self.state['ACTIVE']:
            self.interface = self.interface_active
        else:
            self.interface = self.interface_unactivated

    def _set_state_prelight(self, value):
        if bool(value):
            self.state['PRELIGHT'] = True
        else:
            self.state['PRELIGHT'] = False

    def _get_state_prelight(self):
        return self.state['PRELIGHT']


