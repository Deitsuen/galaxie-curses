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
        self_num_lines, selft_num_cols = self.application.get_size()
        app_info_label = "test"
        top_menu_box = self.application.screen.subwin(0, 0, 0, 0)
        _, top_menu_box_num_cols = top_menu_box.getmaxyx()
        if curses.has_colors():
                top_menu_box.addstr(
                    0,
                    0,
                    str(" " * int(top_menu_box_num_cols)),
                    curses.color_pair(1)
                )
                top_menu_box.bkgdset(
                    ord(' '),
                    curses.color_pair(1)
                )
        if not top_menu_box_num_cols + 1 <= len(app_info_label):
            top_menu_box.addstr(
                0,
                (top_menu_box_num_cols - 1) - len(app_info_label[:-1]),
                app_info_label[:-1],
                curses.color_pair(1)
            )
            top_menu_box.insstr(
                0,
                top_menu_box_num_cols - 1,
                app_info_label[-1:],
                curses.color_pair(1)
            )

    def refresh(self):
        self.draw_menubar()
