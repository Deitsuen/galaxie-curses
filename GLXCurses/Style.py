#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Style(object):
    def __init__(self):
        self.colors = []
        self.style = self.get_default_style()

        self.default()

    def default(self):
        count = 1
        self.colors.append(0)

        # Clean Up color, should be BLACK, BLACK
        curses.init_pair(count, -1, -1)
        self.colors.append('Screen')

        # Each Widget have Transparent Background (Default Terminal) and white foreground
        count += 1
        self.colors.append('Widget')
        curses.init_pair(count, curses.COLOR_WHITE, -1)

        # Menu color
        count += 1
        self.colors.append('MenuModel')
        curses.init_pair(count, curses.COLOR_BLACK, curses.COLOR_CYAN)

        # Tool Bar Color
        count += 1
        self.colors.append('ToolbarText')
        curses.init_pair(count, curses.COLOR_BLACK, curses.COLOR_CYAN)

        count += 1
        self.colors.append('ToolbarPrefix')
        curses.init_pair(count, curses.COLOR_WHITE, -1)

        # Status Bar
        count += 1
        self.colors.append('Statusbar')
        curses.init_pair(count, curses.COLOR_WHITE, -1)

        # Windows
        count += 1
        self.colors.append('Window')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # VBox
        count += 1
        self.colors.append('VBox')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # HBox
        count += 1
        self.colors.append('HBox')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Label
        count += 1
        self.colors.append('Label')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # ProgressBar
        count += 1
        self.colors.append('ProgressBar')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        count += 1
        self.colors.append('ProgressBarBG')
        curses.init_pair(count, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        count += 1
        self.colors.append('ProgressBarFG')
        curses.init_pair(count, curses.COLOR_WHITE, curses.COLOR_BLUE)

        # Dialog File Selection
        # curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        # curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_BLUE)
        # curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLUE)
        # Debug color
        # Dialog File Selection

        count += 1
        self.colors.append('FullGreen')
        curses.init_pair(count, curses.COLOR_GREEN, curses.COLOR_GREEN)

        count += 1
        self.colors.append('FullYellow')
        curses.init_pair(count, curses.COLOR_YELLOW, curses.COLOR_YELLOW)

        count += 1
        self.colors.append('FullRed')
        curses.init_pair(count, curses.COLOR_RED, curses.COLOR_RED)

        # curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_GREEN)
        # curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
        # curses.init_pair(12, curses.COLOR_RED, curses.COLOR_RED)

    def get_default_style(self):
        style = dict()

        # GLXCurses States Type:
        # STATE_NORMAL      - The state during normal operation.
        # STATE_ACTIVE      - The widget is currently active, such as a button pushed
        # STATE_PRELIGHT    - The mouse pointer is over the widget.
        # STATE_SELECTED    - The widget is selected
        # STATE_INSENSITIVE - The widget is disabled

        # GLXCurses Attributes Type:
        # fg     - a list of 5 foreground colors - one for each state
        # bg     - a list of 5 background colors
        # light  - a list of 5 colors - created during set_style() method
        # dark   - a list of 5 colors - created during set_style() method
        # mid    - a list of 5 colors - created during set_style() method
        # text   - a list of 5 colors
        # base   - a list of 5 colors
        # black  - the black color
        # white  - the white color

        # An curses.color to be used for the foreground colors in each widget state.
        style['fg'] = dict()
        style['fg']['STATE_NORMAL'] = curses.COLOR_WHITE
        style['fg']['STATE_ACTIVE'] = curses.COLOR_WHITE
        style['fg']['STATE_PRELIGHT'] = curses.COLOR_WHITE
        style['fg']['STATE_SELECTED'] = curses.COLOR_WHITE
        style['fg']['STATE_INSENSITIVE'] = curses.COLOR_WHITE

        # An curses.color to be used for the background colors in each widget state.
        style['bg'] = dict()
        style['bg']['STATE_NORMAL'] = curses.COLOR_BLUE
        style['bg']['STATE_ACTIVE'] = curses.COLOR_BLUE
        style['bg']['STATE_PRELIGHT'] = curses.COLOR_BLUE
        style['bg']['STATE_SELECTED'] = curses.COLOR_BLUE
        style['bg']['STATE_INSENSITIVE'] = curses.COLOR_BLUE

        # An curses.color to be used for the light colors in each widget state.
        # The light colors are slightly lighter than the bg colors and used for creating shadows.
        style['light'] = dict()
        style['light']['STATE_NORMAL'] = curses.COLOR_BLUE
        style['light']['STATE_ACTIVE'] = curses.COLOR_BLUE
        style['light']['STATE_PRELIGHT'] = curses.COLOR_BLUE
        style['light']['STATE_SELECTED'] = curses.COLOR_BLUE
        style['light']['STATE_INSENSITIVE'] = curses.COLOR_BLUE

        # An curses.color to be used for the dark colors in each widget state.
        # The dark colors are slightly darker than the bg colors and used for creating shadows.
        style['dark'] = dict()
        style['dark']['STATE_NORMAL'] = curses.COLOR_BLACK
        style['dark']['STATE_ACTIVE'] = curses.COLOR_BLACK
        style['dark']['STATE_PRELIGHT'] = curses.COLOR_BLACK
        style['dark']['STATE_SELECTED'] = curses.COLOR_BLACK
        style['dark']['STATE_INSENSITIVE'] = curses.COLOR_BLACK

        # An curses.color to be used for the mid colors (between light and dark) in each widget state
        style['mid'] = dict()
        style['mid']['STATE_NORMAL'] = curses.COLOR_BLUE
        style['mid']['STATE_ACTIVE'] = curses.COLOR_BLUE
        style['mid']['STATE_PRELIGHT'] = curses.COLOR_BLUE
        style['mid']['STATE_SELECTED'] = curses.COLOR_BLUE
        style['mid']['STATE_INSENSITIVE'] = curses.COLOR_BLUE

        # An curses.color to be used for the text colors in each widget state.
        style['text'] = dict()
        style['text']['STATE_NORMAL'] = curses.COLOR_WHITE
        style['text']['STATE_ACTIVE'] = curses.COLOR_WHITE
        style['text']['STATE_PRELIGHT'] = curses.COLOR_WHITE
        style['text']['STATE_SELECTED'] = curses.COLOR_WHITE
        style['text']['STATE_INSENSITIVE'] = curses.COLOR_WHITE

        # An curses.color to be used for the base colors in each widget state.
        style['base'] = dict()
        style['base']['STATE_NORMAL'] = curses.COLOR_BLUE
        style['base']['STATE_ACTIVE'] = curses.COLOR_BLUE
        style['base']['STATE_PRELIGHT'] = curses.COLOR_BLUE
        style['base']['STATE_SELECTED'] = curses.COLOR_BLUE
        style['base']['STATE_INSENSITIVE'] = curses.COLOR_BLUE

        # Used for the black color.
        style['black'] = dict()
        style['black']['STATE_NORMAL'] = curses.COLOR_BLACK
        style['black']['STATE_ACTIVE'] = curses.COLOR_BLACK
        style['black']['STATE_PRELIGHT'] = curses.COLOR_BLACK
        style['black']['STATE_SELECTED'] = curses.COLOR_BLACK
        style['black']['STATE_INSENSITIVE'] = curses.COLOR_BLACK

        # Used for the white color.
        style['white'] = dict()
        style['white']['STATE_NORMAL'] = curses.COLOR_WHITE
        style['white']['STATE_ACTIVE'] = curses.COLOR_WHITE
        style['white']['STATE_PRELIGHT'] = curses.COLOR_WHITE
        style['white']['STATE_SELECTED'] = curses.COLOR_WHITE
        style['white']['STATE_INSENSITIVE'] = curses.COLOR_WHITE

        return style
