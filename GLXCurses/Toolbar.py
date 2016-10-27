#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Toolbar(object):
    def __init__(self, application):
        self.max_button_number = 10
        self.bottom_button_list = [
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
        self.application = application
        self.draw_toolbar()

    def draw_toolbar(self):
        screen = self.application.screen
        item_list = self.bottom_button_list
        labels_end_coord = ['', '', '', '', '', '', '', '', '', '', '', '']
        screen_height, screen_width = screen.getmaxyx()

        toolbar = screen.subwin(0, 0, screen_height - 1, 0)
        toolbar_height, toolbar_width = toolbar.getmaxyx()
        toolbar_width -= 1
        req_button_number = len(item_list) + 1

        pos = 0
        if toolbar_width < req_button_number * 7:
            for i in range(0, req_button_number):
                if pos + 7 <= toolbar_width:
                    pos += 7
                labels_end_coord[i] = pos
        else:
            dv = toolbar_width / req_button_number + 1
            md = toolbar_width % req_button_number + 1
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
            if toolbar_width - 1 > cumul + int((3 * max_can_be_display) - 0):
                max_can_be_display += 1
                toolbar.addstr(
                    0,
                    0,
                    str(" " * int(toolbar_width)),
                    curses.color_pair(1)
                )
                toolbar.insstr(
                    0,
                    toolbar_width - 1,
                    " ",
                    curses.color_pair(1)
                )
                toolbar.addstr(
                    0,
                    0,
                    ""
                )
        count = 0
        for num in range(0, max_can_be_display - 1):
            if count == 0:
                toolbar.addstr(
                    0,
                    0,
                    ""
                )
                toolbar.addstr(
                    0,
                    0,
                    " ",
                    curses.COLOR_WHITE | curses.COLOR_BLACK
                )
                toolbar.addstr(
                    str(count + 1),
                    curses.COLOR_WHITE | curses.COLOR_BLACK
                )
                toolbar.addstr(
                    str(item_list[count]),
                    curses.color_pair(1)
                )

            elif 1 <= count < 9:
                if screen_width - (labels_end_coord[count - 1] + 0) >= len(item_list[count]) + 3:
                    toolbar.addstr(
                        0,
                        (labels_end_coord[count - 1] + 0),
                        " ",
                        curses.COLOR_WHITE | curses.COLOR_BLACK
                    )
                    toolbar.addstr(
                        str(count + 1),
                        curses.COLOR_WHITE | curses.COLOR_BLACK
                    )
                    toolbar.addstr(
                        str(item_list[count]),
                        curses.color_pair(1)
                    )
            elif count >= 9:
                if screen_width - (labels_end_coord[count - 1] + 1) >= len(item_list[count]) + 3:
                    toolbar.addstr(
                        0,
                        (labels_end_coord[count - 1] + 1),
                        str(count + 1),
                        curses.COLOR_WHITE | curses.COLOR_BLACK
                    )
                    toolbar.addstr(
                        item_list[count],
                        curses.color_pair(1)
                    )
            count += 1
            # toolbar.refresh()

    def refresh(self):
        self.draw_toolbar()
