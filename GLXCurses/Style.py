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
        """
        Galaxie Curses Style is equivalent to a skin feature, the entire API receive a common Style from Application \
        and each individual Widget can use it own separate one.

        Yet it's a bit hard to explain how create you own Style, in summary it consist to a dict() it have keys \
        with a special name call ``Attribute``, inside that dictionary we create a second level of dict() dedicated \
        to store color value of each ``States``

        :GLXCurses Style Attributes Type:

        +---------+---------------------------------------------------------------------------------------------+
        | text_fg | An color to be used for the foreground colors in each curses_subwin state.                  |
        +-------------------+-----------------------------------------------------------------------------------+
        | bg      | An color to be used for the background colors in each curses_subwin state.                  |
        +---------+---------------------------------------------------------------------------------------------+
        | light   | An color to be used for the light colors in each curses_subwin state.                       |
        +---------+---------------------------------------------------------------------------------------------+
        | dark    | An color to be used for the dark colors in each curses_subwin state.                        |
        +---------+---------------------------------------------------------------------------------------------+
        | mid     | An color to be used for the mid colors (between light and dark) in each curses_subwin state |
        +---------+---------------------------------------------------------------------------------------------+
        | text    | An color to be used for the text colors in each curses_subwin state.                        |
        +---------+---------------------------------------------------------------------------------------------+
        | base    | An color to be used for the base colors in each curses_subwin state.                        |
        +---------+---------------------------------------------------------------------------------------------+
        | black   | Used for the black color.                                                                   |
        +---------+---------------------------------------------------------------------------------------------+
        | white   | Used for the white color.                                                                   |
        +---------+---------------------------------------------------------------------------------------------+

        :GLXCurses States Type:

        +-------------------+----------------------------------------------------------------+
        | STATE_NORMAL      | The state during normal operation                              |
        +-------------------+----------------------------------------------------------------+
        | STATE_ACTIVE      | The curses_subwin is currently active, such as a button pushed |
        +-------------------+----------------------------------------------------------------+
        | STATE_PRELIGHT    | The mouse pointer is over the curses_subwin                    |
        +-------------------+----------------------------------------------------------------+
        | STATE_SELECTED    | The curses_subwin is selected                                  |
        +-------------------+----------------------------------------------------------------+
        | STATE_INSENSITIVE | The curses_subwin is disabled                                  |
        +---------------+--------------------------------------------------------------------+

        """
        # The White is CRAY and YELLOW is ORANGE
        self.curses_native_colormap = {
            'BLACK': curses.COLOR_BLACK,
            'RED': curses.COLOR_RED,
            'GREEN': curses.COLOR_GREEN,
            'YELLOW': curses.COLOR_YELLOW,
            'BLUE': curses.COLOR_BLUE,
            'MAGENTA': curses.COLOR_MAGENTA,
            'CYAN': curses.COLOR_CYAN,
            'WHITE': curses.COLOR_WHITE,
        }
        self.curses_colors = list()
        self.curses_colors_pairs = list()
        self.attribute = self.get_default_style()
        self.init_curses_pairs()

    @staticmethod
    def get_default_style():
        """
        Return a default style, that will be use by the entire GLXCurses API via the ``attribute`` object. \
        every Widget's  will receive it style by default.

        :return: A Galaxie Curses Style dictionary
        :rtype: dict
        """
        style = dict()

        # An color to be used for the foreground colors in each curses_subwin state.
        style['text_fg'] = dict()
        style['text_fg']['STATE_NORMAL'] = 'WHITE'
        style['text_fg']['STATE_ACTIVE'] = 'WHITE'
        style['text_fg']['STATE_PRELIGHT'] = 'WHITE'
        style['text_fg']['STATE_SELECTED'] = 'WHITE'
        style['text_fg']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the background colors in each curses_subwin state.
        style['bg'] = dict()
        style['bg']['STATE_NORMAL'] = 'BLUE'
        style['bg']['STATE_ACTIVE'] = 'BLUE'
        style['bg']['STATE_PRELIGHT'] = 'CYAN'
        style['bg']['STATE_SELECTED'] = 'CYAN'
        style['bg']['STATE_INSENSITIVE'] = 'BLUE'

        # An color to be used for the light colors in each curses_subwin state.
        # The light colors are slightly lighter than the bg colors and used for creating shadows.
        style['light'] = dict()
        style['light']['STATE_NORMAL'] = 'CYAN'
        style['light']['STATE_ACTIVE'] = 'WHITE'
        style['light']['STATE_PRELIGHT'] = 'WHITE'
        style['light']['STATE_SELECTED'] = 'WHITE'
        style['light']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the dark colors in each curses_subwin state.
        # The dark colors are slightly darker than the bg colors and used for creating shadows.
        style['dark'] = dict()
        style['dark']['STATE_NORMAL'] = 'BLACK'
        style['dark']['STATE_ACTIVE'] = 'BLACK'
        style['dark']['STATE_PRELIGHT'] = 'BLACK'
        style['dark']['STATE_SELECTED'] = 'BLACK'
        style['dark']['STATE_INSENSITIVE'] = 'BLACK'

        # An color to be used for the mid colors (between light and dark) in each curses_subwin state
        style['mid'] = dict()
        style['mid']['STATE_NORMAL'] = 'YELLOW'
        style['mid']['STATE_ACTIVE'] = 'WHITE'
        style['mid']['STATE_PRELIGHT'] = 'WHITE'
        style['mid']['STATE_SELECTED'] = 'WHITE'
        style['mid']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the text colors in each curses_subwin state.
        style['text'] = dict()
        style['text']['STATE_NORMAL'] = 'WHITE'
        style['text']['STATE_ACTIVE'] = 'WHITE'
        style['text']['STATE_PRELIGHT'] = 'WHITE'
        style['text']['STATE_SELECTED'] = 'WHITE'
        style['text']['STATE_INSENSITIVE'] = 'WHITE'

        # An color to be used for the base colors in each curses_subwin state.
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
        """
        Create big matrix of each color combination
        """

        self.curses_colors = list()
        self.curses_colors.append('BLACK')
        self.curses_colors.append('RED')
        self.curses_colors.append('GREEN')
        self.curses_colors.append('YELLOW')
        self.curses_colors.append('BLUE')
        self.curses_colors.append('MAGENTA')
        self.curses_colors.append('CYAN')
        self.curses_colors.append('WHITE')
        #
        # self.curses_colors.append('GRAY')
        # self.curses_colors.append('ORANGE')
        #self.curses_colors.append('PINK')

        self.curses_colors_pairs = list()
        self.curses_colors_pairs.append('WHITE' + '/' + 'BLACK')

        counter = 1
        for foreground in self.curses_colors:
            for background in self.curses_colors:
                self.curses_colors_pairs.append(str(foreground) + '/' + str(background))
                curses.init_pair(counter, self.curses_colors.index(foreground), self.curses_colors.index(background))
                counter += 1

    def get_color_to_int(self, color):
        color = str(color).upper()
        if color in self.curses_native_colormap.keys():
            return self.curses_native_colormap[color]
        else:
            return None

    def get_int_to_color(self, integer):
        for color in self.curses_native_colormap.keys():
            if integer == self.curses_native_colormap[color]:
                return color
            else:
                pass

    def get_generated_pairs(self):
        return list(itertools.product(self.curses_native_colormap.values(), self.curses_native_colormap.values()))

    def get_curses_pairs(self, fg='WHITE', bg='BLACK'):
        if fg in self.curses_colors and bg in self.curses_colors:
            pairs = self.curses_colors_pairs.index(str(fg).upper() + '/' + str(bg).upper())
            return pairs
        else:
            return 0

    # Internal
    def get_attr(self, elem, state):
        return self.attribute[elem][state]