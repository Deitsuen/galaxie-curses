#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import itertools

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Style(object):
    def __init__(self):
        self.curses_colors = list()
        self.curses_colors_pairs = list()
        self.attribute = self.get_default_style()
        self.init_curses_pairs()

    def get_default_style(self):
        style = dict()

        # GLXCurses States Type:
        # STATE_NORMAL      - The state during normal operation.
        # STATE_ACTIVE      - The widget is currently active, such as a button pushed
        # STATE_PRELIGHT    - The mouse pointer is over the widget.
        # STATE_SELECTED    - The widget is selected
        # STATE_INSENSITIVE - The widget is disabled

        # GLXCurses Attributes Type:
        # text_fg     - a list of 5 foreground colors - one for each state
        # bg     - a list of 5 background colors
        # light  - a list of 5 colors - created during set_style() method
        # dark   - a list of 5 colors - created during set_style() method
        # mid    - a list of 5 colors - created during set_style() method
        # text   - a list of 5 colors
        # base   - a list of 5 colors
        # black  - the black color
        # white  - the white color

        # An color to be used for the foreground colors in each widget state.
        style['text_fg'] = dict()
        style['text_fg']['STATE_NORMAL'] = 'WHITE'
        style['text_fg']['STATE_ACTIVE'] = 'WHITE'
        style['text_fg']['STATE_PRELIGHT'] = 'WHITE'
        style['text_fg']['STATE_SELECTED'] = 'WHITE'
        style['text_fg']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the background colors in each widget state.
        style['bg'] = dict()
        style['bg']['STATE_NORMAL'] = 'BLUE'
        style['bg']['STATE_ACTIVE'] = 'BLUE'
        style['bg']['STATE_PRELIGHT'] = 'CYAN'
        style['bg']['STATE_SELECTED'] = 'CYAN'
        style['bg']['STATE_INSENSITIVE'] = 'BLUE'

        # An color to be used for the light colors in each widget state.
        # The light colors are slightly lighter than the bg colors and used for creating shadows.
        style['light'] = dict()
        style['light']['STATE_NORMAL'] = 'CYAN'
        style['light']['STATE_ACTIVE'] = 'WHITE'
        style['light']['STATE_PRELIGHT'] = 'WHITE'
        style['light']['STATE_SELECTED'] = 'WHITE'
        style['light']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the dark colors in each widget state.
        # The dark colors are slightly darker than the bg colors and used for creating shadows.
        style['dark'] = dict()
        style['dark']['STATE_NORMAL'] = 'BLACK'
        style['dark']['STATE_ACTIVE'] = 'BLACK'
        style['dark']['STATE_PRELIGHT'] = 'BLACK'
        style['dark']['STATE_SELECTED'] = 'BLACK'
        style['dark']['STATE_INSENSITIVE'] = 'BLACK'

        # An color to be used for the mid colors (between light and dark) in each widget state
        style['mid'] = dict()
        style['mid']['STATE_NORMAL'] = 'YELLOW'
        style['mid']['STATE_ACTIVE'] = 'WHITE'
        style['mid']['STATE_PRELIGHT'] = 'WHITE'
        style['mid']['STATE_SELECTED'] = 'WHITE'
        style['mid']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the text colors in each widget state.
        style['text'] = dict()
        style['text']['STATE_NORMAL'] = 'WHITE'
        style['text']['STATE_ACTIVE'] = 'WHITE'
        style['text']['STATE_PRELIGHT'] = 'WHITE'
        style['text']['STATE_SELECTED'] = 'WHITE'
        style['text']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the base colors in each widget state.
        style['base'] = dict()
        style['base']['STATE_NORMAL'] = 'WHITE'
        style['base']['STATE_ACTIVE'] = 'WHITE'
        style['base']['STATE_PRELIGHT'] = 'WHITE'
        style['base']['STATE_SELECTED'] = 'WHITE'
        style['base']['STATE_INSENSITIVE'] = 'WHITE'

        # Used for the black color.
        style['black'] = dict()
        style['black']['STATE_NORMAL'] = 'BLACK'
        style['black']['STATE_ACTIVE'] = 'BLACK'
        style['black']['STATE_PRELIGHT'] = 'BLACK'
        style['black']['STATE_SELECTED'] = 'BLACK'
        style['black']['STATE_INSENSITIVE'] = 'BLACK'

        # Used for the white color.
        style['white'] = dict()
        style['white']['STATE_NORMAL'] = 'WHITE'
        style['white']['STATE_ACTIVE'] = 'WHITE'
        style['white']['STATE_PRELIGHT'] = 'WHITE'
        style['white']['STATE_SELECTED'] = 'WHITE'
        style['white']['STATE_INSENSITIVE'] = 'WHITE'

        return style

    def init_curses_pairs(self):

        # Prepare a list with the palette
        self.curses_colors = list()
        self.curses_colors.append(curses.COLOR_BLACK)
        self.curses_colors.append(curses.COLOR_WHITE)
        self.curses_colors.append(curses.A_BOLD | curses.COLOR_WHITE)
        self.curses_colors.append(curses.COLOR_BLUE)
        self.curses_colors.append(curses.COLOR_RED)
        self.curses_colors.append(curses.COLOR_MAGENTA)
        self.curses_colors.append(curses.COLOR_CYAN)
        self.curses_colors.append(curses.COLOR_GREEN)
        self.curses_colors.append(curses.COLOR_YELLOW)
        self.curses_colors.append(curses.A_BOLD | curses.COLOR_YELLOW)
        self.curses_colors.append(curses.A_BOLD | curses.COLOR_RED)

        # Prepare a Combination List for each Color
        curses_colors_pairs = list(itertools.product(self.curses_colors, self.curses_colors))
        curses_colors_pairs.insert(0, [curses.COLOR_WHITE, curses.COLOR_BLACK])

        # Add Default setting and mer
        #curses_colors_pairs.append((black, white))
        #curses_colors_pairs += fb

        index = 1
        for I in curses_colors_pairs:
            curses.init_pair(index, int(I[0]), int(I[1]))
            index += 1

    def get_curses_pairs(self, fg='WHITE', bg='BLACK'):
        fg = fg.upper()
        bg = bg.upper()

        def get_int_to_color(integer):
            if integer == curses.COLOR_BLACK:
                return 'BLACK'
            elif integer == curses.COLOR_WHITE:
                return 'GRAY'
            elif integer == curses.A_BOLD | curses.COLOR_WHITE:
                return 'WHITE'
            elif integer == curses.COLOR_BLUE:
                return 'BLUE'
            elif integer == curses.COLOR_RED:
                return 'RED'
            elif integer == curses.COLOR_MAGENTA:
                return 'MAGENTA'
            elif integer == curses.COLOR_CYAN:
                return 'CYAN'
            elif integer == curses.COLOR_GREEN:
                return 'GREEN'
            elif integer == curses.COLOR_YELLOW:
                return 'ORANGE'
            elif integer == curses.A_BOLD | curses.COLOR_YELLOW:
                return 'YELLOW'
            elif integer == curses.A_BOLD | curses.COLOR_RED:
                return 'PINK'

        def get_color_to_int(color):
            if color == 'BLACK':
                return curses.COLOR_BLACK
            if color == 'GRAY':
                return curses.COLOR_WHITE
            if color == 'WHITE':
                return curses.A_BOLD | curses.COLOR_WHITE
            if color == 'BLUE':
                return curses.COLOR_BLUE
            if color == 'RED':
                return curses.COLOR_RED
            if color == 'MAGENTA':
                return curses.COLOR_MAGENTA
            if color == 'CYAN':
                return curses.COLOR_CYAN
            if color == 'GREEN':
                return curses.COLOR_GREEN
            if color == 'ORANGE':
                return curses.COLOR_YELLOW
            if color == 'YELLOW':
                return curses.A_BOLD | curses.COLOR_YELLOW
            if color == 'PINK':
                return curses.A_BOLD | curses.COLOR_RED

        fg = get_color_to_int(fg)
        bg = get_color_to_int(bg)

        if self.curses_colors_pairs.index((fg, bg)):
            pairs = self.curses_colors_pairs.index((fg, bg))
            return pairs
        else:
            return 0

    def get_style(self):
        return self.style

