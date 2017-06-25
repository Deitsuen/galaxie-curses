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
    def test_get_default_attribute_states(self):
        """Test Style.get_default_attribute_states()"""
        default_attribute_states = self.style.get_default_attribute_states()
        # Check first level dictionary
        self.assertEqual(type(default_attribute_states), type(dict()))
        # For each key's
        for attribute in ['text_fg', 'bg', 'light', 'dark', 'mid', 'text', 'base', 'black', 'white']:
            # Check if the key value is a dictionary
            self.assertEqual(type(default_attribute_states[attribute]), type(dict()))
            # For each key value, in that case a sub dictionary
            for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
                # Check if the key value is a string
                self.assertEqual(type(default_attribute_states[attribute][state]), type(str()))

    def test_get_curses_color_pair(self):
        """Test Style.get_curses_color_pair()"""
        # Check if fg='WHITE', bg='BLACK' first in the list
        self.assertEqual(self.style.get_color_pair(foreground='WHITE', background='BLACK'), 0)

        # Check if fg='WHITE', bg='BLUE' return a int type
        self.assertEqual(type(self.style.get_color_pair(foreground='WHITE', background='BLUE')), type(int()))

        # Check if fg='WHITE', bg='BLUE' return a value > 0
        self.assertGreater(self.style.get_color_pair(foreground='WHITE', background='BLUE'), 0)

    def test_get_attribute_states(self):
        """Test Style.get_attribute_states()"""
        attribute_states = self.style.get_attribute_states()
        # Check first level dictionary
        self.assertEqual(type(attribute_states), type(dict()))
        # For each key's
        for attribute in ['text_fg', 'bg', 'light', 'dark', 'mid', 'text', 'base', 'black', 'white']:
            # Check if the key value is a dictionary
            self.assertEqual(type(attribute_states[attribute]), type(dict()))
            # For each key value, in that case a sub dictionary
            for state in ['STATE_NORMAL', 'STATE_ACTIVE', 'STATE_PRELIGHT', 'STATE_SELECTED', 'STATE_INSENSITIVE']:
                # Check if the key value is a string
                self.assertEqual(type(attribute_states[attribute][state]), type(str()))

    # Internal Method test
    # Curses colors
    def test__get__set_allowed_fg_colors(self):
        """Test Style curses colors internal list 'get' and 'set' method's"""
        tested_colors_list = ['BLACK', 'WHITE']
        self.style._set_allowed_fg_colors(allowed_fg_colors=tested_colors_list)
        self.assertEqual(tested_colors_list, self.style._get_allowed_fg_colors())

    def test__set_allowed_fg_colors_raise(self):
        """Test Style raise TypeError of _set_curses_colors()"""
        self.assertRaises(TypeError, self.style._set_allowed_fg_colors, float(randint(1, 42)))

    def test__gen_allowed_fg_colors(self):
        """Test Style allowed foreground colors list generation method"""
        # Set a empty list as curses colors
        self.style._set_allowed_fg_colors(allowed_fg_colors=list())
        # The curses_colors_list should be empty
        self.assertEqual(list(), self.style._get_allowed_fg_colors())
        # Generate the curses colors list
        self.style._gen_allowed_fg_colors()
        # The curses_colors_list should still be a list type
        self.assertEqual(type(list()), type(self.style._get_allowed_fg_colors()))
        # The curses_colors_list should not be a empty list
        self.assertGreater(len(self.style._get_allowed_fg_colors()), len(list()))

    # Curses Colors pairs
    def test__get__set_curses_colors_pairs(self):
        """Test Style allowed curses colors pairs internal list 'get' and 'set' method's"""
        tested_colors_list = ['BLACK', 'WHITE']
        self.style._set_text_pairs(text_pairs=tested_colors_list)
        self.assertEqual(tested_colors_list, self.style._get_text_pairs())

    def test__set_curses_colors_pairs_raise(self):
        """Test Style raise TypeError of _set_curses_colors_pairs()"""
        self.assertRaises(TypeError, self.style._set_text_pairs, float(randint(1, 42)))

    def test__gen_curses_colors_pairs(self):
        """Test Style allowed curses colors pairs list generation method"""
        # Set a empty list as curses colors
        self.style._set_text_pairs(text_pairs=list())
        # The curses_colors_list should be empty
        self.assertEqual(list(), self.style._get_text_pairs())
        # Generate the curses colors list
        self.style._gen_curses_colors_pairs()
        # The curses_colors_list should still be a list type
        self.assertEqual(type(list()), type(self.style._get_text_pairs()))
        # The curses_colors_list should not be a empty list
        self.assertGreater(len(self.style._get_text_pairs()), len(list()))

if __name__ == '__main__':
    unittest.main()
