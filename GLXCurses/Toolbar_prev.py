#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Toolbar(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.set_name('Toolbar')

        # Widget setting
        if self.style.attribute:
            self.text_fg = self.style.attribute['dark']['STATE_NORMAL']
            self.text_bg = self.style.attribute['light']['STATE_NORMAL']
            self.text_prefix_fg = self.style.attribute['text']['STATE_NORMAL']
            self.text_prefix_bg = self.style.attribute['dark']['STATE_NORMAL']
            self.widget_fg = self.style.attribute['dark']['STATE_NORMAL']
            self.widget_bg = self.style.attribute['dark']['STATE_NORMAL']

            self.color_text_normal = self.style.get_curses_pairs(fg=self.text_fg, bg=self.text_bg)
            self.color_text_prefix = self.style.get_curses_pairs(fg=self.text_prefix_fg, bg=self.text_prefix_bg)
            self.color_normal = self.style.get_curses_pairs(fg=self.widget_fg, bg=self.widget_bg)
        else:
            self.color_text_normal = 0
            self.color_text_prefix = 0
            self.color_normal = 0

        self.max_button_number = 10
        self.button_list = [
            'Help',
            'Options',
            'View',
            'Modif',
            'Copy',
            'Move',
            'Mkdir',
            'Sup',
            'Menu',
            'Quit'
        ]

    def draw(self):
        item_list = self.button_list
        labels_end_coord = ['', '', '', '', '', '', '', '', '', '', '', '']
        screen_height, screen_width = self.get_screen().getmaxyx()

        drawing_area = self.get_screen().subwin(
            0,
            0,
            screen_height - 1,
            0
        )

        self.draw_in_area(drawing_area, item_list, labels_end_coord, screen_width)

    def draw_in_area(self, drawing_area, item_list, labels_end_coord, screen_width):
        self.set_widget(drawing_area)
        widget_height, widget_width = self.get_curses_subwin().getmaxyx()
        widget_width -= 1
        req_button_number = len(item_list) + 1
        pos = 0
        if widget_width < req_button_number * 7:
            for i in range(0, req_button_number):
                if pos + 7 <= widget_width:
                    pos += 7
                labels_end_coord[i] = pos
        else:
            dv = widget_width / req_button_number + 1
            md = widget_width % req_button_number + 1
            i = 0
            for i in range(0, req_button_number / 2):
                pos += dv
                if req_button_number / 2 - 1 - i < md / 2:
                    pos += 1
                labels_end_coord[i] = pos
            for i in range(i + 1, req_button_number):
                pos += dv
                if req_button_number - 1 - i < (md + 1) / 2:
                    pos += 1
                labels_end_coord[i] = pos
        if req_button_number > self.max_button_number:
            req_button_number = self.max_button_number

        # Limit crash about display size, by reduce the number of button's it can be display
        max_can_be_display = 1
        for I in range(1, req_button_number + 1):
            cumul = 0
            for U in range(0, max_can_be_display):
                cumul += len(str(item_list[U]))
            if widget_width - 1 > cumul + int((3 * max_can_be_display) - 0):
                max_can_be_display += 1
                self.curses_subwin.addstr(
                    0,
                    0,
                    str(" " * int(widget_width)),
                    curses.color_pair(self.color_text_normal)
                )
                self.curses_subwin.insstr(
                    0,
                    widget_width - 1,
                    " ",
                    curses.color_pair(self.color_text_normal)
                )
                self.curses_subwin.addstr(
                    0,
                    0,
                    "",
                    curses.color_pair(self.color_text_normal)
                )
        count = 0
        for num in range(0, max_can_be_display - 1):
            if count == 0:
                self.curses_subwin.addstr(
                    str('{0: >2}'.format(count + 1)),
                    curses.color_pair(self.color_text_prefix)
                )
                self.curses_subwin.addstr(
                    str(item_list[count]),
                    curses.color_pair(self.color_text_normal)
                )
            elif 0 <= count < max_can_be_display - 1:
                if screen_width - (labels_end_coord[count - 1] + 0) >= len(item_list[count]) + 3:
                    self.curses_subwin.addstr(
                        0,
                        (labels_end_coord[count - 1] + 0),
                        "",
                        curses.color_pair(self.color_text_normal)
                    )
                    self.curses_subwin.addstr(
                        str('{0: >2}'.format(count + 1)),
                        curses.color_pair(self.color_text_prefix)
                    )
                    self.curses_subwin.addstr(
                        str(item_list[count]),
                        curses.color_pair(self.color_text_normal)
                    )
            elif count >= max_can_be_display - 1:
                if screen_width - (labels_end_coord[count - 1] + 1) >= len(item_list[count]) + 3:
                    self.curses_subwin.addstr(
                        0,
                        (labels_end_coord[count - 1] + 1),
                        str('{0: >2}'.format(count + 1)),
                        curses.color_pair(self.color_text_prefix)
                    )
                    self.curses_subwin.addstr(
                        item_list[count],
                        curses.color_pair(self.color_text_normal)
                    )
            count += 1

class ToolbarButton(Widget):
    def __init__(self):
        Widget.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle

        self.set_name('ToolbarButton')
        self.set_can_focus(0)
        self.set_can_default(0)
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

    def update_preferred_sizes(self):
        if self.get_text():
            self.preferred_width = 0
            self.preferred_width += len(self.get_text())
            self.preferred_width += len(self.button_border)
            self.preferred_width += self.get_spacing() * 2

    def draw(self):
        parent_height, parent_width = self.get_parent().get_size()
        parent_y, parent_x = self.get_parent().get_origin()

        min_size_width = (self.get_spacing() * 2) + 1
        min_size_height = (self.get_spacing() * 2) + 1
        height_ok = self.get_parent().get_height() >= min_size_height
        width_ok = self.get_parent().get_width() >= min_size_width
        if not height_ok or not width_ok:
            return

        drawing_area = self.get_parent().widget.subwin(
            parent_height - (self.get_spacing() * 2),
            parent_width - (self.get_spacing() * 2),
            parent_y + self.get_spacing(),
            parent_x + self.get_spacing()
        )

        self.draw_widget_in_area(drawing_area)

    def draw_widget_in_area(self, drawing_area):
        self.set_widget(drawing_area)

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
        self.check_selected()
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
        # Interface management
        self.get_curses_subwin().addstr(
            self.label_y,
            self.label_x,
            self.button_border[:len(self.button_border) / 2],
            color
        )
        # Draw the Horizontal Button with Justification and PositionType
        message_to_display = resize_text(self.get_text(), self.get_width(), '~')
        self.get_curses_subwin().addstr(
            self.label_y,
            self.label_x + len(self.button_border) / 2,
            message_to_display,
            color
        )
        # Interface management
        self.get_curses_subwin().insstr(
            self.label_y,
            self.label_x + (len(self.button_border) / 2) + len(message_to_display),
            self.button_border[-len(self.button_border) / 2:],
            color
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
        if self.get_sensitive():
            # Read the mouse event information's
            (mouse_event_id, x, y, z, event) = mouse_event
            # Be sure we select really the Button
            if self.label_y + self.get_preferred_height() >= y >= self.label_y + self.get_preferred_height():
                if self.label_x <= x <= self.label_x + len(self.button_border) + len(self.get_text()) - 1:
                    # We are sure about the button have been clicked
                    #
                    self.states_list = '; '.join(state_string for state, state_string
                                                 in self.curses_mouse_states.viewitems()
                                                 if event & state)
                    if event == curses.BUTTON1_PRESSED:
                        self.set_is_focus(1)
                        self.check_selected()
                        self.state['PRELIGHT'] = True
                    elif event == curses.BUTTON1_RELEASED:
                        self.state['PRELIGHT'] = False
                    if event == curses.BUTTON1_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON1_DOUBLE_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON1_TRIPLE_CLICKED:
                        self.set_is_focus(1)

                    if event == curses.BUTTON2_PRESSED:
                        self.set_is_focus(1)
                        self.check_selected()
                        self.state['PRELIGHT'] = True
                    elif event == curses.BUTTON2_RELEASED:
                        self.state['PRELIGHT'] = False
                    if event == curses.BUTTON2_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON2_DOUBLE_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON2_TRIPLE_CLICKED:
                        self.set_is_focus(1)

                    if event == curses.BUTTON3_PRESSED:
                        self.set_is_focus(1)
                        self.check_selected()
                        self.state['PRELIGHT'] = True
                    elif event == curses.BUTTON3_RELEASED:
                        self.state['PRELIGHT'] = False
                    if event == curses.BUTTON3_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON3_DOUBLE_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON3_TRIPLE_CLICKED:
                        self.set_is_focus(1)

                    if event == curses.BUTTON4_PRESSED:
                        self.set_is_focus(1)
                        self.check_selected()
                        self.state['PRELIGHT'] = True
                    elif event == curses.BUTTON4_RELEASED:
                        self.state['PRELIGHT'] = False
                    if event == curses.BUTTON4_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON4_DOUBLE_CLICKED:
                        self.set_is_focus(1)
                    if event == curses.BUTTON4_TRIPLE_CLICKED:
                        self.set_is_focus(1)

                    if event == curses.BUTTON_SHIFT:
                        pass
                    if event == curses.BUTTON_CTRL:
                        pass
                    if event == curses.BUTTON_ALT:
                        pass
                    return 1
            else:
                self.state['PRELIGHT'] = False
                return 0

    # Internal curses_subwin functions
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
    def get_states_list(self):
        return self.states_list

    def check_selected(self):
        if self.get_can_focus():
            if self.get_is_focus():
                self.button_border = self.interface_selected
            else:
                self.button_border = self.interface
        else:
            pass
