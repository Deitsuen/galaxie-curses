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
        count = 1
        self.colors = []
        self.colors.append(0)

        # Clean Up color, should be BLACK, BLACK
        curses.init_pair(count, curses.COLOR_BLACK, curses.COLOR_BLACK)
        self.colors.append('Screen')

        # Menu color
        count += 1
        self.colors.append('MenuModel')
        curses.init_pair(count, curses.COLOR_BLACK, curses.COLOR_CYAN)

        # Tool Bar Color
        count += 1
        self.colors.append('ToolbarText')
        curses.init_pair(count, curses.COLOR_BLACK, curses.COLOR_CYAN)

        count += 1
        self.colors.append('ToolbarPrefix')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Status Bar
        count += 1
        self.colors.append('Statusbar')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Windows
        count += 1
        self.colors.append('Window')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # VBox
        count += 1
        self.colors.append('VBox')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # HBox
        count += 1
        self.colors.append('HBox')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Label
        count += 1
        self.colors.append('Label')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # ProgressBar
        count += 1
        self.colors.append('ProgressBarBG')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Dialog File Selection
        # curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        # curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLUE)
        # curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLUE)
        # Debug color
        # Dialog File Selection
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
        curses.init_pair(12, curses.COLOR_RED, curses.COLOR_RED)




