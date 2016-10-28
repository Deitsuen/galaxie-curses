#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Window(object):
    def __init__(self, parent):
        self.title = ''
        self.main_window = ''
        self.parent_height = ''
        self.parent_width = ''
        self.parent_x = ''
        self.parent_y = ''
        self.decorated = 0

        self.parent = parent
        self.widget = ''
        self.active_content = ''
        self.widget_content = {}

        # Mehe Meheuu
        # self.application = application

        self.draw_window()

    # Common Widget mandatory
    def get_origin(self):
        return self.widget.getbegyx()

    def get_size(self):
        return self.widget.getmaxyx()

    def get_widget(self):
        return self.widget

    def get_parent_size(self):
        return self.parent.get_size()

    def get_parent_origin(self):
        return self.parent.get_origin()

    def set_parent(self, parent):
        self.parent = parent

    def remove_parent(self):
        self.parent = ''

    # GLXC Window Functions
    def draw_window(self):
        self.parent_height, self.parent_width = self.parent.get_size()
        self.parent_y, self.parent_x = self.parent.get_origin()
        self.widget = self.parent.get_parent().subwin(
            self.parent_height,
            self.parent_width,
            self.parent_y,
            self.parent_x
        )

        widget_height,widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        if curses.has_colors():
            self.widget.bkgdset(ord(' '), curses.color_pair(3))
            self.widget.bkgd(ord(' '), curses.color_pair(3))
            for I in range(widget_y, widget_height):
                self.widget.addstr(I, 0, str(' ' * int(widget_width - 1)), curses.color_pair(3))
                self.widget.insstr(I, int(widget_width - 1), str(' '), curses.color_pair(3))

        # Creat a box and add the name of the windows like a king, who trust that !!!
        if self.decorated > 0:
            self.widget.box()
            if not self.title == '':
                self.widget.addstr(0, 1, self.title)
        else:
            if not self.title == '':
                self.widget.addstr(0, 0, self.title)

    def set_title(self, title):
        self.title = title

    def set_decorated(self, boolean):
        self.decorated = int(boolean)

    def add(self, widget):
        id_max = len(self.widget_content.keys())
        if id_max == 0:
            self.widget_content[id_max] = widget
        else:
            self.widget_content[id_max + 1] = widget
        self.refresh()

    def refresh(self):
        self.draw_window()


