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

        # Store GLXC object
        self.menubar = ''
        self.main_window = ''
        self.statusbar = ''
        self.message_bar = ''
        self.toolbar = ''

        # Store Variables
        self.application_name = ''
        self.windows_id_number = ''
        self.active_window_id = ''
        self.windows = {}

        # Next it's dead
        self.init_colors()
        self.screen.keypad(True)

        self.draw_main_window()

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

    def set_name(self, name):
        self.application_name = name

    def add_window(self, glxc_window):
        id_max = len(self.windows.keys())
        if id_max == 0:
            self.windows[id_max] = glxc_window
            self.active_window_id = id_max
        else:
            self.windows[id_max + 1] = glxc_window
            self.active_window_id = id_max + 1
        self.refresh()

    def get_size(self):
        return self.screen.getmaxyx()

    def add_menubar(self, glxc_menu_bar):
        self.menubar = glxc_menu_bar

    def remove_menubar(self, glxc_menu_bar):
        self.menubar = ''
        self.refresh()

    def add_statusbar(self, glx_statusbar):
        self.statusbar = glx_statusbar
        self.refresh()

    def remove_statusbar(self, glx_statusbar):
        self.statusbar = ''
        self.refresh()

    def add_toolbar(self, glx_toolbar):
        self.toolbar = glx_toolbar
        self.refresh()

    def remove_toolbar(self, glx_toolbar):
        self.toolbar = ''
        self.refresh()

    def refresh(self):
        # Clean the screen
        self.screen.clear()

        # Calculate the Main Window size
        self.draw_main_window()

        # Check main widget to display
        if not self.main_window == '':
            self.windows[self.active_window_id].refresh()

        if not self.menubar == '':
            self.menubar.refresh()

        if not self.statusbar == '':
            self.statusbar.refresh()

        if not self.toolbar == '':
            self.toolbar.refresh()

        # After have redraw everything it's time to refresh the screen
        self.screen.refresh()

    def draw_main_window(self):
        screen = self.screen
        screen_num_lines, _ = screen.getmaxyx()
        if not self.menubar == '':
            menu_bar_num_lines = 1
        else:
            menu_bar_num_lines = 0
        if not self.statusbar == '':
            status_bar_num_lines = 1
        else:
            status_bar_num_lines = 0
        if not self.message_bar == '':
            message_bar_num_lines = 1
        else:
            message_bar_num_lines = 0
        if not self.toolbar == '':
            tool_bar_num_lines = 1
        else:
            tool_bar_num_lines = 0

        interface_elements_num_lines = 0
        interface_elements_num_lines += menu_bar_num_lines
        interface_elements_num_lines += message_bar_num_lines
        interface_elements_num_lines += status_bar_num_lines
        interface_elements_num_lines += tool_bar_num_lines

        window = self.screen.subwin(screen_num_lines - interface_elements_num_lines, 0, menu_bar_num_lines, 0)
        self.main_window = window

    def getch(self):
        return self.screen.getch()

    def close(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

