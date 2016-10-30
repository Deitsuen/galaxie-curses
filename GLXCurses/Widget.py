#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Widget(object):
    def __init__(self):
        self.widget = ''
        self.widget_spacing = 0
        self.widget_decorated = 0

        self.parent = ''
        self.parent_spacing = 0

    # Common Widget mandatory
    def get(self):
        return self.widget

    def get_origin(self):
        return self.widget.getbegyx()

    def get_size(self):
        return self.widget.getmaxyx()

    def set_spacing(self, spacing):
        self.widget_spacing = spacing

    def get_spacing(self):
        return self.widget_spacing

    def set_decorated(self, decorated):
        self.widget_decorated = decorated

    def get_decorated(self, decorated):
        return self.widget_decorated

    # Each Galaxie Curses Compoment must have a draw method
    def refresh(self):
        self.draw()

    # Parent Management
    def get_parent(self):
        return self.parent

    def get_parent_size(self):
        return self.parent.widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def set_parent(self, parent):
        self.parent = parent

    def get_parent_spacing(self):
        return self.parent_spacing

    def remove_parent(self):
        self.parent = ''
