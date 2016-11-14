#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Style import Style
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Widget(object):
    def __init__(self):
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.name = 'Widget'

        # Widget Setting
        self.state = dict()
        self.state['NORMAL'] = True
        self.state['ACTIVE'] = False
        self.state['PRELIGHT'] = False
        self.state['SELECTED'] = False
        self.state['INSENSITIVE'] = False

        # Widget
        self.curses_subwin = None
        self.spacing = 0
        self.widget_decorated = None
        self.sensitive = None

        # Widget Parent
        self.screen = None
        self.attribute = None

        # Size Management
        self.screen_height = 0
        self.screen_width = 0
        self.screen_y = 0
        self.screen_x = 0
        self.parent_y = 0
        self.parent_x = 0
        self.parent_width = 0
        self.parent_height = 0
        self.y = 0
        self.x = 0
        self.width = 0
        self.height = 0
        self.preferred_height = 0
        self.preferred_width = 0
        self.natural_height = 0
        self.natural_width = 0
        self.preferred_size = 0

        # Property
        # If True, the application will paint directly on the curses_subwin
        self.app_paintable = False

        # If True, the curses_subwin can be the default curses_subwin
        self.can_default = False

        # If True, the curses_subwin can accept the input focus
        self.can_focus = False

        # If True, the curses_subwin is part of a composite curses_subwin
        self.composite_child = False

        # If True, the curses_subwin is double buffered
        self.double_buffered = False

        # The event mask that decides what kind of Event this curses_subwin gets.
        self.events = None

        # The mask that decides what kind of extension events this curses_subwin gets.
        self.extension_events = None

        # If True, the curses_subwin is the default curses_subwin
        self.has_default = False

        # If True, the curses_subwin has the input focus
        self.has_focus = False

        # A value of True indicates that curses_subwin can have a tooltip
        self.has_tooltip = False

        # The height request of the curses_subwin, or -1 if natural request should be used.
        self.height_request = -1

        # If True, the curses_subwin is the focus curses_subwin within the toplevel
        self.is_focus = False

        # The name of the curses_subwin
        self.name = None

        # If True show_all() should not affect this curses_subwin
        self.no_show_all = False

        # The parent curses_subwin of this curses_subwin. Must be a Container curses_subwin.
        self.parent = None

        # If True, the curses_subwin will receive the default action when it is focused.
        self.receives_default = None

        # If True, the curses_subwin responds to input
        self.sensitive = False

        # The style of the curses_subwin, which contains information about how it will look (colors etc).
        # Each Widget come with it own Style by default
        # It can receive parent Style() or a new Style() during a set_parent() / un_parent() call
        # GLXCApplication is a special case where it have no parent, it role is to impose it own style to each Widget
        self.style = Style()
        self.style_backup = None

        # Sets the text of tooltip to be the given string.
        self.tooltip_text = None

        # If True, the curses_subwin is visible
        self.visible = True

        # The width request of the curses_subwin, or -1 if natural request should be used.
        self.width_request = -1

        # The curses_subwin's window if realized, None otherwise.
        self.window = None

    # Common Widget mandatory

    # Screen
    def get_screen_height(self):
        self.screen_height, self.screen_width = self.get_screen().getmaxyx()
        return self.screen_height

    def get_screen_width(self):
        self.screen_height, self.screen_width = self.get_screen().getmaxyx()
        return self.screen_width

    def get_screen_x(self):
        self.screen_y, self.screen_x = self.get_screen().getbegyx()
        return self.screen_x

    def gef_screen_y(self):
        self.screen_y, self.screen_x = self.get_screen().getbegyx()
        return self.screen_y

    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return self

    # Parent Management
    def get_parent_size(self):
        return self.get_parent().curses_subwin.getmaxyx()

    def get_parent_origin(self):
        return self.get_parent().curses_subwin.getbegyx()

    # This function is useful only when implementing subclasses of GtkContainer.
    # Sets the container as the parent of curses_subwin , and takes care of some details such as updating the state
    # and style of the child to reflect its new location. The opposite function is gtk_widget_unparent().
    def _set_parent(self, parent):
        self.parent = parent

    def set_parent(self, parent):

        self._set_parent(parent)

        self.screen = self.get_parent().get_screen()

        # Widget start with own Style, and will use the Style of it parent when it add to a contener
        # GLXCApplication Widget is a special case where it parent is it self.

        self.style_backup = self.get_style()
        self.set_style(self.get_parent().get_style())

        # POUR MO
        #self.parent_height, self.parent_width = self.get_parent().get_size()
        #self.parent_y, self.parent_x = self.get_parent().get_origin()

    def unparent(self):
        self.parent = None
        self.set_style(self.style_backup)

    def get_parent_spacing(self):
        return self.get_parent().get_spacing()

    def get_parent_style(self):
        return self.get_parent().get_style()

    def get_screen(self):
        return self.screen

    # Widget
    def get_curses_subwin(self):
        return self.curses_subwin

    def set_curses_subwin(self, subwin):
        self.curses_subwin = subwin
        self.height, self.width = self.get_size()
        self.y, self.x = self.get_origin()

    def get_origin(self):
        return self.get_curses_subwin().getbegyx()

    def set_spacing(self, spacing):
        self.spacing = spacing

    def get_spacing(self):
        return self.spacing

    def set_decorated(self, decorated):
        self.widget_decorated = decorated

    def get_decorated(self):
        return self.widget_decorated

    def refresh(self):
        self.draw()

    def show(self):
        self.draw()

    def show_all(self):
        self.draw()
        self.get_parent().draw()

    # Name management use for GLXCStyle color's
    def override_color(self, color):
        self.get_style().attribute['text']['STATE_NORMAL'] = str(color).upper()

    def override_background_color(self, color):
        self.get_style().attribute['bg']['STATE_NORMAL'] = str(color).upper()

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
        return self.get_curses_subwin().getmaxyx()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # State
    # Sets the sensitivity of a curses_subwin.
    # A curses_subwin is sensitive if the user can interact with it. Insensitive widgets are “grayed out”
    # and the user can’t interact with them.
    # Properties
    def set_app_paintable(self, boolean):
        self.app_paintable = bool(boolean)

    def get_app_paintable(self):
        return self.app_paintable

    def set_can_default(self, boolean):
        self.can_default = bool(boolean)

    def get_can_default(self):
        return self.can_default

    def set_can_focus(self, boolean):
        self.can_focus = bool(boolean)

    def get_can_focus(self):
        return self.can_focus

    def set_composite_child(self, boolean):
        self.composite_child = bool(boolean)

    def get_composite_child(self):
        return self.composite_child

    def set_double_buffered(self, boolean):
        self.double_buffered = bool(boolean)

    def get_double_buffered(self):
        return self.double_buffered

    def set_events(self, events):
        self.events = events

    def get_events(self):
        return self.events

    def set_extension_events(self, extension_events):
        self.extension_events = extension_events

    def get_extension_events(self):
        return self.extension_events

    def set_has_default(self, boolean):
        self.has_default = bool(boolean)

    def get_has_default(self):
        return self.has_default

    def set_has_focus(self, boolean):
        self.has_focus = bool(boolean)

    def get_has_focus(self):
        return self.has_focus

    def set_has_tooltip(self, boolean):
        self.has_tooltip = bool(boolean)

    def get_has_tooltip(self):
        return self.has_tooltip

    def set_height_request(self, height):
        self.height_request = height

    def get_height_request(self):
        return self.height_request

    def set_is_focus(self, boolean):
        if not self.get_sensitive():
            self.is_focus = False
        else:
            self.is_focus = bool(boolean)

    def get_is_focus(self):
        return self.is_focus

    def set_name(self, string):
        self.name = string

    def get_name(self):
        return self.name

    def set_no_show_all(self, boolean):
        self.no_show_all = bool(boolean)

    def get_no_show_all(self):
        return self.no_show_all

    def set_receives_default(self, boolean):
        self.receives_default = bool(boolean)

    def get_receives_default(self):
        return self.receives_default

    def set_sensitive(self, boolean):
        self.sensitive = bool(boolean)
        self.state['INSENSITIVE'] = bool(boolean)
        if not self.get_sensitive():
            self.set_is_focus(0)

    def get_sensitive(self):
        return self.sensitive

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def set_tooltip_text(self, text):
        self.tooltip_text = text

    def get_tooltip_text(self):
        return self.tooltip_text

    def set_visible(self, boolean):
        self.visible = bool(boolean)

    def get_visible(self):
        return self.visible

    def set_width_request(self, width):
        self.width_request = width

    def get_width_request(self):
        return self.width_request

    def get_window(self):
        return self.window
