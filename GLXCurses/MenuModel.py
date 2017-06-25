#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class MenuModel(GLXCurses.Widget):
    def __init__(self):
        GLXCurses.Widget.__init__(self)
        self.set_name('MenuModel')

        # Internal Widget Setting
        self.app_info_label = None

        # Make a Style heritage attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

    def draw(self):
        app_info_label = self.app_info_label
        drawing_area = self.get_screen().subwin(
            0,
            0,
            0,
            0
        )
        self.set_curses_subwin(drawing_area)

        if curses.has_colors():
            self.get_curses_subwin().addstr(
                    0,
                    0,
                    str(' ' * (self.get_width() - 1)),
                    self.get_style().get_color_pair(
                        fg=self.get_style().get_color_by_attribute_state('dark', 'STATE_NORMAL'),
                        bg=self.get_style().get_color_by_attribute_state('light', 'STATE_NORMAL')
                    )
                )
            self.get_curses_subwin().bkgdset(
                    ord(' '),
                    self.get_style().get_color_pair(
                        fg=self.get_style().get_color_by_attribute_state('dark', 'STATE_NORMAL'),
                        bg=self.get_style().get_color_by_attribute_state('light', 'STATE_NORMAL')
                    )
                )
        if self.app_info_label:
            if not self.get_height() + 1 <= len(app_info_label):
                try:
                    self.get_curses_subwin().addstr(
                        0,
                        (self.get_width() - 1) - len(str(app_info_label[:-1])),
                        app_info_label[:-1],
                        self.get_style().get_color_pair(
                            fg=self.get_style().get_color_by_attribute_state('dark', 'STATE_NORMAL'),
                            bg=self.get_style().get_color_by_attribute_state('light', 'STATE_NORMAL')
                        )
                    )
                    self.get_curses_subwin().insstr(
                        0,
                        self.get_width() - 1,
                        app_info_label[-1:],
                        self.get_style().get_color_pair(
                            fg=self.get_style().get_color_by_attribute_state('dark', 'STATE_NORMAL'),
                            bg=self.get_style().get_color_by_attribute_state('light', 'STATE_NORMAL')
                        )
                    )
                except curses.error:
                    pass
