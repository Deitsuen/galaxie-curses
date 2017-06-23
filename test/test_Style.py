#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string

import sys
import os
import uuid

# Require when you haven't GLXCurses as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses

# Unittest
class TestStyle(unittest.TestCase):

    def setUp(self):
        # Before the test start
        # Require for init the screen
        self.application = GLXCurses.Application()
        # The component to test
        self.style = GLXCurses.Style()

        # Display thing that because curses have flush the screen
        rows, columns = os.popen('stty size', 'r').read().split()
        self.columns = int(columns)
        self.width = self.columns - 7
        sys.stdout.write('\r')
        sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.columns))
        sys.stdout.flush()

    def tearDown(self):
        # When the test is finish
        # Require for ask to curse to clean up it
        self.application.close()

        # Display thing that because curses have flush the screen
        sys.stdout.write('\r')
        sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.width))
        sys.stdout.write(' ')
        sys.stdout.write('[ ')
        sys.stdout.write('\033[92m')
        sys.stdout.write('OK')
        sys.stdout.write('\033[0m')
        sys.stdout.write(' ]')
        sys.stdout.write('\n\r')
        sys.stdout.flush()

    # Tests
    def test_get_default_style(self):
        """Test Style.get_default_style() return a dictionary"""
        self.assertEqual(type(self.style.get_default_style()), type(dict()))

    def test_get_default_style_dictionary_text_fg(self):
        """Test Style.get_default_style() 'text_fg' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['text_fg']), type(dict()))

    def test_get_default_style_dictionary_text_fg_states(self):
        """Test Style.get_default_style() 'text_fg' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['text_fg'][state]), type(str()))

    def test_get_default_style_dictionary_bg(self):
        """Test Style.get_default_style() 'bg' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['bg']), type(dict()))

    def test_get_default_style_dictionary_bg_states(self):
        """Test Style.get_default_style() 'bg' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['bg'][state]), type(str()))

    def test_get_default_style_dictionary_light(self):
        """Test Style.get_default_style() 'light' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['light']), type(dict()))

    def test_get_default_style_dictionary_light_states(self):
        """Test Style.get_default_style() 'light' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['light'][state]), type(str()))

    def test_get_default_style_dictionary_dark(self):
        """Test Style.get_default_style() 'dark' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['dark']), type(dict()))

    def test_get_default_style_dictionary_dark_states(self):
        """Test Style.get_default_style() 'dark' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['dark'][state]), type(str()))

    def test_get_default_style_dictionary_mid(self):
        """Test Style.get_default_style() 'mid' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['mid']), type(dict()))

    def test_get_default_style_dictionary_mid_states(self):
        """Test Style.get_default_style() 'mid' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['mid'][state]), type(str()))

    def test_get_default_style_dictionary_text(self):
        """Test Style.get_default_style() 'text' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['text']), type(dict()))

    def test_get_default_style_dictionary_text_states(self):
        """Test Style.get_default_style() 'text' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['text'][state]), type(str()))

    def test_get_default_style_dictionary_base(self):
        """Test Style.get_default_style() 'base' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['base']), type(dict()))

    def test_get_default_style_dictionary_base_states(self):
        """Test Style.get_default_style() 'base' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['base'][state]), type(str()))

    def test_get_default_style_dictionary_black(self):
        """Test Style.get_default_style() 'black' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['black']), type(dict()))

    def test_get_default_style_dictionary_black_states(self):
        """Test Style.get_default_style() 'black' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['black'][state]), type(str()))

    def test_get_default_style_dictionary_white(self):
        """Test Style.get_default_style() 'white' dictionary key"""
        self.assertEqual(type(self.style.get_default_style()['white']), type(dict()))

    def test_get_default_style_dictionary_white_states(self):
        """Test Style.get_default_style() 'white' states dictionary key's"""
        for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
            self.assertEqual(type(self.style.get_default_style()['white'][state]), type(str()))

    # Internal Method test
    def test__get__set_curses_colors(self):
        """Test Style allowed curses colors internal list 'get' and 'set' method's"""
        tested_colors_list = ['BLACK', 'WHITE']
        self.style._set_curses_colors(curses_colors_list=tested_colors_list)
        self.assertEqual(tested_colors_list, self.style._get_curses_colors())

    def test__set_curses_colors_raise(self):
        """Test Style raise TypeError of _set_curses_colors()"""
        self.assertRaises(TypeError, self.style._set_curses_colors, float(randint(1, 42)))

    def test__gen_curses_colors(self):
        """Test Style allowed curses colors list generation method"""
        # Set a empty list as curses colors
        self.style._set_curses_colors(curses_colors_list=list())
        # The curses_colors_list should be empty
        self.assertEqual(list(), self.style._get_curses_colors())
        # Generate the curses colors list
        self.style._gen_curses_colors()
        # The curses_colors_list should still be a list type
        self.assertEqual(type(list()), type(self.style._get_curses_colors()))
        # The curses_colors_list should not be a empty list
        self.assertGreater(len(self.style._get_curses_colors()), len(list()))

    def test__get__set_curses_colors_pairs(self):
        """Test Style allowed curses colors pairs internal list 'get' and 'set' method's"""
        tested_colors_list = ['BLACK', 'WHITE']
        self.style._set_curses_colors_pairs(curses_colors_pairs_list=tested_colors_list)
        self.assertEqual(tested_colors_list, self.style._get_curses_colors_pairs())

    def test__set_curses_colors_pairs_raise(self):
        """Test Style raise TypeError of _set_curses_colors_pairs()"""
        self.assertRaises(TypeError, self.style._set_curses_colors_pairs, float(randint(1, 42)))

    def test__gen_curses_colors_pairs(self):
        """Test Style allowed curses colors pairs list generation method"""
        # Set a empty list as curses colors
        self.style._set_curses_colors_pairs(curses_colors_pairs_list=list())
        # The curses_colors_list should be empty
        self.assertEqual(list(), self.style._get_curses_colors_pairs())
        # Generate the curses colors list
        self.style._gen_curses_colors_pairs()
        # The curses_colors_list should still be a list type
        self.assertEqual(type(list()), type(self.style._get_curses_colors_pairs()))
        # The curses_colors_list should not be a empty list
        self.assertGreater(len(self.style._get_curses_colors_pairs()), len(list()))

if __name__ == '__main__':
    unittest.main()
