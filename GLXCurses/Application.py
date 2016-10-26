#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import time
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

        self.init_colors()
        self.screen.keypad(True)

        self.draw_screen_background()
        self.screen.refresh()

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
        self.refresh()

    def get_size(self):
        return self.screen.getmaxyx()

    def refresh(self):
        #self.screen.clear()
        actual_x_size, actual_y_size = self.screen.getmaxyx()
        resize = curses.is_term_resized(actual_y_size, actual_x_size)
        curses.resizeterm(actual_x_size, actual_y_size)
        if resize is True:
            self.draw_screen_background()
        self.screen.refresh()

    def set_menubar(self):
        self.screen.refresh()

    def getch(self):
        return self.screen.getch()

    def draw_screen_background(self):
        num_lines, num_cols = self.screen.getmaxyx()
        if curses.has_colors():
            for I in range(0, num_lines - 1):
                self.screen.addstr(
                    I,
                    0,
                    str(" " * int(num_cols)),
                    curses.color_pair(3)
                )
                self.screen.bkgdset(
                    ord(' '),
                    curses.color_pair(3)
                )
        self.screen.refresh()

    def close(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

