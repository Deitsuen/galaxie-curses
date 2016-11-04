#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

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
        # fg     - a list of 5 foreground colors - one for each state
        # bg     - a list of 5 background colors
        # light  - a list of 5 colors - created during set_style() method
        # dark   - a list of 5 colors - created during set_style() method
        # mid    - a list of 5 colors - created during set_style() method
        # text   - a list of 5 colors
        # base   - a list of 5 colors
        # black  - the black color
        # white  - the white color

        # An color to be used for the foreground colors in each widget state.
        style['fg'] = dict()
        style['fg']['STATE_NORMAL'] = 'WHITE'
        style['fg']['STATE_ACTIVE'] = 'WHITE'
        style['fg']['STATE_PRELIGHT'] = 'WHITE'
        style['fg']['STATE_SELECTED'] = 'WHITE'
        style['fg']['STATE_INSENSITIVE'] = 'WHITE'

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
        style['light']['STATE_NORMAL'] = 'WHITE'
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
        self.curses_colors = list()
        self.curses_colors.append('BLACK')
        self.curses_colors.append('RED')
        self.curses_colors.append('GREEN')
        self.curses_colors.append('YELLOW')
        self.curses_colors.append('BLUE')
        self.curses_colors.append('MAGENTA')
        self.curses_colors.append('CYAN')
        self.curses_colors.append('WHITE')

        self.curses_colors_pairs = list()
        self.curses_colors_pairs.append('WHITE' + '/' + 'BLACK')

        counter = 1
        for foreground in self.curses_colors:
            for background in self.curses_colors:
                self.curses_colors_pairs.append(str(foreground) + '/' + str(background))
                curses.init_pair(counter, self.curses_colors.index(foreground), self.curses_colors.index(background))
                counter += 1

    def get_curses_pairs(self, fg='WHITE', bg='BLACK'):
        if fg in self.curses_colors and bg in self.curses_colors:
            pairs = self.curses_colors_pairs.index(str(fg).upper() + '/' + str(bg).upper())
            return pairs
        else:
            return 0

    def get_style(self):
        return self.style

