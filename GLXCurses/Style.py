#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Style(object):
    """
    :Description:

    Galaxie Curses Style is equivalent to a skin feature, the entire API receive a common Style from Application
    and each individual Widget can use it own separate one.

    Yet it's a bit hard to explain how create you own Style, in summary it consist to a dict() it have keys
    with a special name call ``Attribute``, inside that dictionary we create a second level of dict() dedicated
    to store color value of each ``States``
    """
    def __init__(self):
        """
        :GLXCurses Style Attributes Type:

         +-------------+---------------------------------------------------------------------------------------------+
         | ``text_fg`` | An color to be used for the foreground colors in each curses_subwin state.                  |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``bg``      | An color to be used for the background colors in each curses_subwin state.                  |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``light``   | An color to be used for the light colors in each curses_subwin state.                       |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``dark``    | An color to be used for the dark colors in each curses_subwin state.                        |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``mid``     | An color to be used for the mid colors (between light and dark) in each curses_subwin state |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``text``    | An color to be used for the text colors in each curses_subwin state.                        |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``base``    | An color to be used for the base colors in each curses_subwin state.                        |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``black``   | Used for the black color.                                                                   |
         +-------------+---------------------------------------------------------------------------------------------+
         | ``white``   | Used for the white color.                                                                   |
         +-------------+---------------------------------------------------------------------------------------------+

        :GLXCurses States Type:

         +------------------------+----------------------------------------------------------------+
         | ``STATE_NORMAL``       | The state during normal operation                              |
         +------------------------+----------------------------------------------------------------+
         | ``STATE_ACTIVE``       | The curses_subwin is currently active, such as a button pushed |
         +------------------------+----------------------------------------------------------------+
         | ``STATE_PRELIGHT``     | The mouse pointer is over the curses_subwin                    |
         +------------------------+----------------------------------------------------------------+
         | ``STATE_SELECTED``     | The curses_subwin is selected                                  |
         +------------------------+----------------------------------------------------------------+
         | ``STATE_INSENSITIVE``  | The curses_subwin is disabled                                  |
         +------------------------+----------------------------------------------------------------+

        """
        # Internal storage
        self._curses_native_colormap = dict()
        self._curses_colors_allowed = list()
        self._curses_colors_pairs = list()

        # Internal init
        self._gen_curses_native_colormap_dict()
        self._gen_curses_colors()
        self._gen_curses_colors_pairs()

        # init
        self.attribute = self.get_default_style()

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

    def get_curses_pairs(self, fg='WHITE', bg='BLACK'):
        if fg in self._get_curses_colors() and bg in self._get_curses_colors():
            pairs = self._get_curses_colors_pairs().index(str(fg).upper() + '/' + str(bg).upper())
            return pairs
        else:
            return 0

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    # Internal
    def _set_curses_native_colormap(self, curses_native_colormap_dict=dict()):
        """
        Internal method for set ``_curses_native_colormap`` attribute

        :param curses_native_colormap_dict: A list of color name
        :type curses_native_colormap_dict: list
        :raise TypeError: if ``curses_native_colormap_dict`` parameter is not a :py:data:`dict` type
        """
        if type(curses_native_colormap_dict) == dict:
            if curses_native_colormap_dict != self._get_curses_native_colormap():
                self._curses_native_colormap = curses_native_colormap_dict
                # Can emit modification signal here
        else:
            raise TypeError(u'>curses_native_colormap_dict< argument must be a dict type')

    def _get_curses_native_colormap(self):
        """
        Internal method for return ``_curses_native_colormap`` attribute

        :return the _curses_native_colormap attribute
        :rtype: dict
        """
        return self._curses_native_colormap

    def _gen_curses_native_colormap_dict(self):
        """
        Internal it generate curses native colormap dictionary , the method work directly with \
        other internal method's and have no parameter or return.
        """
        self._set_curses_native_colormap(dict())
        self._get_curses_native_colormap()['BLACK'] = curses.COLOR_BLACK
        self._get_curses_native_colormap()['RED'] = curses.COLOR_RED
        self._get_curses_native_colormap()['GREEN'] = curses.COLOR_GREEN
        self._get_curses_native_colormap()['YELLOW'] = curses.COLOR_YELLOW
        self._get_curses_native_colormap()['BLUE'] = curses.COLOR_BLUE
        self._get_curses_native_colormap()['MAGENTA'] = curses.COLOR_MAGENTA
        self._get_curses_native_colormap()['CYAN'] = curses.COLOR_CYAN
        self._get_curses_native_colormap()['WHITE'] = curses.COLOR_WHITE

    def _get_curses_colors(self):
        """
        Internal method for return ``_curses_colors_allowed`` attribute

        :return the curses_colors attribute
        :rtype: list
        """
        return self._curses_colors_allowed

    def _set_curses_colors(self, curses_colors_list=list()):
        """
        Internal method for set ``_curses_colors`` attribute

        :param curses_colors_list: A list of color name
        :type curses_colors_list: list
        :raise TypeError: if ``curses_colors_list`` parameter is not a :py:data:`list` type
        """
        if type(curses_colors_list) == list:
            if curses_colors_list != self._get_curses_colors():
                self._curses_colors_allowed = curses_colors_list
                # Can emit modification signal here
        else:
            raise TypeError(u'>curses_colors_list< argument must be a list type')

    def _gen_curses_colors(self):
        """
        Internal it generate color list name of supported color by Galaxie Curses, the method work directly with \
        other internal method's and have no parameter or return.

        That list will be use as source for generate a color pair.
        """

        # Start by clean the list
        self._set_curses_colors(list())

        # Appen allowed colors
        self._get_curses_colors().append('BLACK')
        self._get_curses_colors().append('RED')
        self._get_curses_colors().append('GREEN')
        self._get_curses_colors().append('YELLOW')
        self._get_curses_colors().append('BLUE')
        self._get_curses_colors().append('MAGENTA')
        self._get_curses_colors().append('CYAN')
        self._get_curses_colors().append('WHITE')

        # unimplemented colors
        # self._get_curses_colors.append('GRAY')
        # self._get_curses_colors.append('ORANGE')
        # self._get_curses_colors.append('PINK')

    def _set_curses_colors_pairs(self, curses_colors_pairs_list):
        """
        Internal method for set ``_curses_colors_pairs`` attribute

        :param curses_colors_pairs_list: A list of color name
        :type curses_colors_pairs_list: list
        :raise TypeError: if ``curses_colors_pairs_list`` parameter is not a :py:data:`list` type
        """

        if type(curses_colors_pairs_list) == list:
            if curses_colors_pairs_list != self._get_curses_colors():
                self._curses_colors_pairs = curses_colors_pairs_list
                # Can emit modification signal here
        else:
            raise TypeError(u'>curses_colors_pairs_list< argument must be a list type')

    def _get_curses_colors_pairs(self):
        """
        Internal method for return ``_curses_colors_pairs`` attribute

        :return curses_colors_pairs list ex: ['WHITE/BLACK', 'WHITE/RED']
        :rtype: list
        """
        return self._curses_colors_pairs

    def _gen_curses_colors_pairs(self):
        """
        Internal it generate color list pair name of supported color by Galaxie Curses, the method work directly with \
        other internal method's and have no parameter or return.

        That list index number match with the curses colors pair number.
        """
        # Start by clean the list
        self._set_curses_colors_pairs(list())
        # The first color pair is WHITE/BLACK for no color support
        self._get_curses_colors_pairs().append('WHITE' + '/' + 'BLACK')

        # Init a counter it start to 1 and not 0
        counter = 1
        # For each foreground colors
        for foreground in self._get_curses_colors():
            # And each background colors
            for background in self._get_curses_colors():

                # Generate a colors pair like 'WHITE/RED' and ad
                self._get_curses_colors_pairs().append(str(foreground) + '/' + str(background))

                # Curses pair provisioning it have a index it match with the curses_colors_pairs list index
                curses.init_pair(
                    counter, self._get_curses_colors().index(foreground), self._get_curses_colors().index(background)
                )
                # The curses pair number match  with the curses_colors_pairs list index
                counter += 1
