#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


from GLXCurses.Style import Style
class Widget(object):
    def __init__(self):

        # Widget Setting
        self.widget = ''
        self.widget_spacing = 0
        self.widget_decorated = 0
        self.screen = ''
        self.style = Style()
        self.type = 'Widget'

        # Widget Parent Information's
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

    # Each Galaxie Curses Component's must have a draw method
    def refresh(self):
        self.draw()

    def show(self):
        self.draw()

    def show_all(self):
        self.draw()
        self.parent.draw()

    # Parent Management
    def get_parent(self):
        return self.parent

    def get_parent_size(self):
        return self.parent.widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def set_parent(self, parent):
        self.parent = parent
        self.parent_spacing = self.parent.parent_spacing
        self.screen = self.parent.screen
        self.style = self.parent.style

    def get_parent_spacing(self):
        self.parent_spacing = self.parent.parent_spacing
        return self.parent_spacing

    def un_parent(self):
        self.parent = ''
        self.parent_spacing = 0

    def get_screen(self):
        return self.screen

    def set_style(self, style_name):
        self.style = style_name

    def get_style(self):
        return self.style

    def get_style_by_type(self, type):
        return self.style.get_style_by_type(type)

    def set_widget(self, widget):
        self.widget = widget