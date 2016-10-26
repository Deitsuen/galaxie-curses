#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import time
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class MenuModel(object):
    def __init__(self, application):

        self.application = application
        self.draw_menubar()

    def draw_menubar(self):
        num_lines, num_cols = self.application.get_size()
        app_info_label = "test"
        top_menu_box = self.application.screen.subwin(0, 0, 0, 0)
        if curses.has_colors():
                top_menu_box.addstr(
                    0,
                    0,
                    str(" " * int(num_cols)),
                    curses.color_pair(1)
                )
                top_menu_box.bkgdset(
                    ord(' '),
                    curses.color_pair(1)
                )
        if not num_cols + 1 <= len(app_info_label):
            top_menu_box.addstr(
                0,
                (num_cols - 1) - len(app_info_label[:-1]),
                app_info_label[:-1],
                curses.color_pair(1)
            )
            top_menu_box.insstr(
                0,
                num_cols - 1,
                app_info_label[-1:],
                curses.color_pair(1)
            )

    def refresh(self):
        self.draw_menubar()
