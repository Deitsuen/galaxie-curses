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

        # State
        self.state = dict()
        self.state['NORMAL'] = True
        self.state['ACTIVE'] = None
        self.state['PRELIGHT'] = None
        self.state['SELECTED'] = None
        self.state['INSENSITIVE'] = None
        self.state['INCONSISTENT'] = None
        self.state['FOCUSED'] = None

        # Widget
        self.widget = None
        self.widget_spacing = 0
        self.widget_decorated = 0

        # Widget Parent
        self.parent = None
        self.screen = None
        self.attribute = None

        # Each Widget come with it own Style by default
        # It can receive parent Style() or a new Style() during a set_parent() / un_parent() call
        # GLXCApplication is a special case where it have no parent, it role is to impose it own style to each Widget
        self.style = Style()
        self.style_backup = None

        # Size Management
        self.width = 0
        self.height = 0
        self.preferred_height = 0
        self.preferred_width = 0
        self.natural_height = 0
        self.natural_width = 0
        self.preferred_size = 0

    # Common Widget mandatory
    def get(self):
        return self.widget

    def get_origin(self):
        return self.widget.getbegyx()

    def set_spacing(self, spacing):
        self.widget_spacing = spacing

    def get_spacing(self):
        return self.widget_spacing

    def set_decorated(self, decorated):
        self.widget_decorated = decorated

    def get_decorated(self):
        return self.widget_decorated

    def refresh(self):
        self.draw()

    # Each Galaxie Curses Component's must have a draw method
    def show(self):
        self.draw()

    def show_all(self):
        self.draw()
        self.parent.draw()

    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return self

    # Parent Management
    def get_parent_size(self):
        return self.get_parent().widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def _set_parent(self, parent):
        self.parent = parent

    def set_parent(self, parent):

        self._set_parent(parent)

        self.screen = self.get_parent().get_screen()

        # Widget start with own Style, and will use the Style of it parent when it add to a contener
        # GLXCApplication Widget is a special case where it parent is it self.

        self.style_backup = self.get_style()
        self.set_style(self.get_parent().get_style())

    def un_parent(self):
        self.parent = None
        self.set_style(self.style_backup)

    def get_parent_spacing(self):
        return self.get_parent().get_spacing()

    def get_parent_style(self):
        return self.get_parent().get_style()

    def get_screen(self):
        return self.screen

    def set_widget(self, widget):
        self.widget = widget

    def set_name(self, name):
        self.name = name

    # Name management use for GLXCStyle color's
    def get_name(self):
        return self.name

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def override_color(self, color):
        self.style.attribute['text']['STATE_NORMAL'] = str(color).upper()

    def override_background_color(self, color):
        self.style.attribute['bg']['STATE_NORMAL'] = str(color).upper()

    # Size management
    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_preferred_height(self):
        return self.preferred_height

    def set_preferred_height(self, height):
        self.preferred_height = height

    def get_preferred_width(self):
        return self.preferred_width

    def set_preferred_width(self, preferred_width):
        self.preferred_width = preferred_width

    def get_preferred_size(self):
        # should preserve the Y X of ncuses ?
        return self.preferred_size

    def set_preferred_size(self):
        # should preserve the Y X of ncuses ?
        return self.preferred_size

    def get_size(self):
        return self.widget.getmaxyx()





