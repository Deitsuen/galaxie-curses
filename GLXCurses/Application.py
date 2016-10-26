#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Application(object):
    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        self.screen.clear()

        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.curs_set(0)
        curses.mousemask(-1)

        self.menu_bar = ''
        self.main_window = ''
        self.windows_id_number = ''
        self.active_window_id = ''
        self.windows = {}

        # Next it's dead
        self.init_colors()
        self.screen.keypad(True)

    def init_colors(self):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # Dialog Windows Buttons
        curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_CYAN)
        # Dialog File Selection
        curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLUE)
        curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLUE)
        self.screen.refresh()

    def add_window(self, glxc_window):
        id_max = len(self.windows.keys())
        if id_max == 0:
            self.windows[id_max] = glxc_window
            self.active_window_id = id_max
        else:
            self.windows[id_max + 1] = glxc_window
            self.active_window_id = id_max + 1

    def get_size(self):
        return self.screen.getmaxyx()

    def set_menubar(self, glxc_menu_bar):
        self.menu_bar = glxc_menu_bar

    def refresh(self):
        self.screen.clear()
        if not self.menu_bar == '':
            self.windows[self.active_window_id].refresh()
        if not self.menu_bar == '':
            self.menu_bar.refresh()
        self.screen.refresh()

    def getch(self):
        return self.screen.getch()

    def close(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

