#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Window(object):
    def __init__(self, application):
        self.application = application
        self.draw_window()

    def draw_window(self):
        num_lines, _ = self.application.screen.getmaxyx()
        summary_box = self.application.screen.subwin(num_lines - 4, 0, 1, 0)
        summary_box_num_lines, summary_box_num_cols = summary_box.getmaxyx()

        # Start to draw the summary contener
        if curses.has_colors():
            for I in range(1, summary_box_num_lines):
                summary_box.addstr(I, 0, str(" " * int(summary_box_num_cols - 1)), curses.color_pair(3))
            summary_box.bkgdset(ord(' '), curses.color_pair(3))
        # Creat a box and add the name of the windows like a king, who trust that !!!
        summary_box.box()

    def refresh(self):
        self.draw_window()


