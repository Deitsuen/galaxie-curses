#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Toolbar(Widget):
    def __init__(self):
        Widget.__init__(self)
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
        screen_height, screen_width = self.screen.getmaxyx()

        self.widget = self.screen.subwin(0, 0, screen_height - 1, 0)
        widget_height, widget_width = self.widget.getmaxyx()
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
                self.widget.addstr(
                    0,
                    0,
                    str(" " * int(widget_width)),
                    curses.color_pair(self.get_style_by_type('ToolbarText'))
                )
                self.widget.insstr(
                    0,
                    widget_width - 1,
                    " ",
                    curses.color_pair(self.get_style_by_type('ToolbarText'))
                )
                self.widget.addstr(
                    0,
                    0,
                    ""
                )
        count = 0
        for num in range(0, max_can_be_display - 1):
            if count == 0:
                self.widget.addstr(
                    str('{0: >2}'.format(count + 1)),
                    curses.color_pair(self.get_style_by_type('ToolbarPrefix'))
                )
                self.widget.addstr(
                    str(item_list[count]),
                    curses.color_pair(self.get_style_by_type('ToolbarText'))
                )
            elif 0 <= count < max_can_be_display - 1:
                if screen_width - (labels_end_coord[count - 1] + 0) >= len(item_list[count]) + 3:
                    self.widget.addstr(
                        0,
                        (labels_end_coord[count - 1] + 0),
                        "",
                        curses.color_pair(self.get_style_by_type('ToolbarPrefix'))
                    )
                    self.widget.addstr(
                        str('{0: >2}'.format(count + 1)),
                        curses.color_pair(self.get_style_by_type('ToolbarPrefix'))
                    )
                    self.widget.addstr(
                        str(item_list[count]),
                        curses.color_pair(self.get_style_by_type('ToolbarText'))
                    )
            elif count >= max_can_be_display - 1:
                if screen_width - (labels_end_coord[count - 1] + 1) >= len(item_list[count]) + 3:
                    self.widget.addstr(
                        0,
                        (labels_end_coord[count - 1] + 1),
                        str('{0: >2}'.format(count + 1)),
                        curses.color_pair(self.get_style_by_type('ToolbarPrefix'))
                    )
                    self.widget.addstr(
                        item_list[count],
                        curses.color_pair(self.get_style_by_type('ToolbarText'))
                    )
            count += 1
