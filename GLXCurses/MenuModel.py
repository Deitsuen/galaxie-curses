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
        self.app_info_label = self.application.application_name
        self.draw_menubar()

    def draw_menubar(self):
        actual_x_size, actual_y_size = self.application.screen.getmaxyx()
        app_info_label = self.app_info_label
        top_menu_box = self.application.screen.subwin(0, 0, 0, 0)
        if curses.has_colors():
                top_menu_box.addstr(
                    0,
                    0,
                    str(" " * int(actual_y_size)),
                    curses.color_pair(1)
                )
                top_menu_box.bkgdset(
                    ord(' '),
                    curses.color_pair(1)
                )
        if len(self.app_info_label) > 0:
            if not actual_y_size + 1 <= len(app_info_label):
                top_menu_box.addstr(
                    0,
                    (actual_y_size - 1) - len(str(app_info_label[:-1])),
                    app_info_label[:-1],
                    curses.color_pair(1)
                )
                top_menu_box.insstr(
                    0,
                    actual_y_size - 1,
                    app_info_label[-1:],
                    curses.color_pair(1)
                )

    def refresh(self):
        self.draw_menubar()
