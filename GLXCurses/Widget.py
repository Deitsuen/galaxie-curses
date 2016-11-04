#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Style import Style
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Widget(object):
    def __init__(self):
        self.type = 'Widget'

        # Widget Setting
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.name = 'Widget'

        # Color's and Style
        self.override_background_color = 0

        # State
        self.state = dict()
        self.state['NORMAL'] = 1
        self.state['ACTIVE'] = 0
        self.state['PRELIGHT'] = 0
        self.state['SELECTED'] = 0
        self.state['INSENSITIVE'] = 0
        self.state['INCONSISTENT'] = 0
        self.state['FOCUSED'] = 0

        self.widget = ''
        self.widget_spacing = 0
        self.widget_decorated = 0
        self.screen = ''
        self.style = Style()

        # Widget Parent Information's
        self.parent = ''
        self.parent_spacing = 0
        self.parent_style = Style()

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
        if parent.style:
            self.parent_style = parent.style
        else:
            self.parent_style = self.style

    def get_parent_spacing(self):
        self.parent_spacing = self.parent.parent_spacing
        return self.parent_spacing

    def get_parent_style(self):
        self.parent_style = self.parent.parent_style
        return self.parent.parent_style

    def un_parent(self):
        self.parent = ''
        self.parent_spacing = 0

    def get_screen(self):
        return self.screen

    def set_widget(self, widget):
        self.widget = widget

    # Name management use for GLXCStyle color's
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def get_style_by_type(self, type):
        return self.style.get_style_by_type(type)

    # Method for override color's
    # def override_background_color(self, background_color=0):
    #     self.override_background_color = background_color
