#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import sys
import os
from GLXCurses import glxc
from GLXCurses.Style import Style
import locale

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Application(object):
    def __init__(self):
        try:
            # Initialize curses
            os.environ["NCURSES_NO_UTF8_ACS"] = '1'
            self.screen = curses.initscr()

            # Turn off echoing of keys, and enter cbreak mode,
            # where no buffering is performed on keyboard input
            curses.noecho()
            curses.cbreak()

            # In keypad mode, escape sequences for special keys
            # (like the cursor keys) will be interpreted and
            # a special value like curses.KEY_LEFT will be returned
            self.screen.keypad(1)

        except ValueError:
            sys.stdout.write("Curses library not installed defaulting to standard console output\n")
            sys.stdout.write("Error initializing screen.\n")
            sys.stdout.flush()
            self.close()
            sys.exit(1)

        if not curses.has_colors():
            sys.stdout.write("Your terminal does not support color\n")
            sys.stdout.flush()
            self.close()
            sys.exit(1)
        else:
            curses.start_color()
            curses.use_default_colors()
            self.style = Style()
        self.screen.clear()

        curses.curs_set(0)
        curses.mousemask(-1)

        # Store GLXC object
        self.menubar = None
        self.main_window = None
        self.statusbar = None
        self.message_bar = None
        self.toolbar = None

        # Store Variables
        self.name = 'Application'
        self.windows_id_number = None
        self.active_window_id = None
        self.windows = {}
        self.attribute = self.style.get_default_style()

        # Controller
        self.widget_it_have_default = None
        self.widget_it_have_focus = None
        self.widget_it_have_tooltip = None

        # Fake Widget
        self.curses_subwin = None
        self.spacing = 0
        self.decorated = 0
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

        self.parent_spacing = 0
        self.parent_style = self.style

    # Parent
    def set_parent(self, parent):
        pass

    def get_parent(self):
        return self.curses_subwin

    def get_parent_size(self):
        return self.get_parent().getmaxyx()

    def get_parent_origin(self):
        return self.get_parent().getbegyx()

    def get_parent_spacing(self):
        return self.get_parent().spacing

    def get_parent_style(self):
        return self.style

    # Widget
    def get_curses_subwin(self):
        return self.curses_subwin

    def get_origin(self):
        return self.curses_subwin.getbegyx()

    def get_spacing(self):
        return self.spacing

    def get_decorated(self):
        return self.decorated

    def remove_parent(self):
        pass

    def get_screen(self):
        return self.screen

    def set_screen(self, screen):
        pass

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

    # GLXCApplication function
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def add_window(self, glxc_window):
        # set_parent is the set_parent from Widget common method
        # information's will be transmit by it method
        glxc_window.set_parent(self)

        # Display only one active window
        id_max = len(self.windows.keys())
        if id_max == 0:
            self.windows[id_max] = glxc_window
            self.active_window_id = id_max
        else:
            self.windows[id_max + 1] = glxc_window
            self.active_window_id = id_max + 1

    def add_menubar(self, glxc_menu_bar):
        glxc_menu_bar.set_parent(self)
        self.menubar = glxc_menu_bar

    def remove_menubar(self):
        self.menubar = None

    def add_statusbar(self, glx_statusbar):
        glx_statusbar.set_parent(self)
        self.statusbar = glx_statusbar

    def remove_statusbar(self, glx_statusbar):
        glx_statusbar.un_parent()
        self.statusbar = None

    def add_toolbar(self, glx_toolbar):
        glx_toolbar.set_parent(self)
        self.toolbar = glx_toolbar

    def remove_toolbar(self, glx_toolbar):
        glx_toolbar.un_parent()
        self.toolbar = None

    def refresh(self):
        # Clean the screen
        self.screen.clear()

        # Calculate the Main Window size
        self.draw()

        # Check main curses_subwin to display
        if self.curses_subwin:
            self.windows[self.active_window_id].draw()

        if self.menubar:
            self.menubar.draw()

        if self.statusbar:
            self.statusbar.draw()

        if self.toolbar:
            self.toolbar.draw()

        # After have redraw everything it's time to refresh the screen
        self.get_screen().refresh()

    def draw(self):
        parent_height, parent_width = self.screen.getmaxyx()
        if self.menubar:
            menu_bar_height = 1
        else:
            menu_bar_height = 0
        if self.statusbar:
            status_bar_height = 1
        else:
            status_bar_height = 0
        if self.message_bar:
            message_bar_height = 1
        else:
            message_bar_height = 0
        if self.toolbar:
            tool_bar_height = 1
        else:
            tool_bar_height = 0

        interface_elements_height = 0
        interface_elements_height += menu_bar_height
        interface_elements_height += message_bar_height
        interface_elements_height += status_bar_height
        interface_elements_height += tool_bar_height

        self.set_height(parent_height - interface_elements_height)
        self.set_width(0)
        begin_y = menu_bar_height
        begin_x = 0
        self.curses_subwin = self.screen.subwin(
            self.get_height(),
            self.get_width(),
            begin_y,
            begin_x
        )
        self.set_preferred_height(self.get_height())
        self.set_preferred_width(self.get_width())
        self.x = begin_x
        self.y = begin_y

    def getch(self):
        return self.screen.getch()

    def close(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    # Focus and Selection
    def get_application(self):
        return self

    def set_application(self, application):
        pass

    def get_default(self):
        return self.widget_it_have_default

    def set_default(self, widget_unique_id):
        self.widget_it_have_default = widget_unique_id

    def get_is_focus(self):
        return self.widget_it_have_focus

    def set_is_focus(self, widget_unique_id):
        self.widget_it_have_focus = widget_unique_id

    def get_tooltip(self):
        return self.widget_it_have_tooltip

    def set_tooltip(self, widget_unique_id):
        self.widget_it_have_tooltip = widget_unique_id
