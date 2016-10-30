#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Style(object):
    def __init__(self):
        self.style = self.default()

    def default(self):
        # Clean Up color, should be BLACK, BLACK
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)

        # Top Menu color
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

        # Tool Bar Color
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Status Bar
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Windows
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Dialog File Selection
        curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLUE)
        curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLUE)
        # Debug color
        # Dialog File Selection
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
        curses.init_pair(12, curses.COLOR_RED, curses.COLOR_RED)

    def get_style_by_type(self, type):
        if type == 'Black':
            return 1
        elif type == 'MenuModel':
            return 2
        elif type == 'ToolbarText':
            return 3
        elif type == 'ToolbarPrefix':
            return 4
        elif type == 'Statusbar':
            return 5
        elif type == 'Window':
            return 6
        elif type == 'Debug':
            return 10

