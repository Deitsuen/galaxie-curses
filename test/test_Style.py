#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest2 as unittest
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
class TestEventBus(unittest.TestCase):
    def setUp(self):
        # Before the test start
        self.style = GLXCurses.Style()
        rows, columns = os.popen('stty size', 'r').read().split()
        self.columns = int(columns)
        self.width = self.columns - 7
        sys.stdout.write('\r')
        sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.columns))
        sys.stdout.flush()

    def tearDown(self):
        # When the test is finish
        # self.application.refresh()
        # self.application.close()
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

    def test_get_default_style(self):
        """Test Style.get_default_style() return a dictionnaty"""
        self.assertEqual(type(self.style.get_default_style()), type(dict()))

    def test_get_default_style_dictionarys(self):
        """Test Style.get_default_style() dictionary contain specific keys"""
        # text_fg     - a list of 5 foreground colors - one for each state
        self.assertEqual(type(self.style.get_default_style()['text_fg']), type(dict()))
        # bg     - a list of 5 background colors
        self.assertEqual(type(self.style.get_default_style()['bg']), type(dict()))
        # light  - a list of 5 colors - created during set_style() method
        self.assertEqual(type(self.style.get_default_style()['light']), type(dict()))
        # dark   - a list of 5 colors - created during set_style() method
        self.assertEqual(type(self.style.get_default_style()['dark']), type(dict()))
        # mid    - a list of 5 colors - created during set_style() method
        self.assertEqual(type(self.style.get_default_style()['mid']), type(dict()))
        # text   - a list of 5 colors
        self.assertEqual(type(self.style.get_default_style()['text']), type(dict()))
        # base   - a list of 5 colors
        self.assertEqual(type(self.style.get_default_style()['base']), type(dict()))
        # black  - the black color
        self.assertEqual(type(self.style.get_default_style()['black']), type(dict()))
        # white  - the white color
        self.assertEqual(type(self.style.get_default_style()['white']), type(dict()))

if __name__ == '__main__':
    unittest.main()
