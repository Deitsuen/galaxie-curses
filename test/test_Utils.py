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

from GLXCurses.Utils import clamp_to_zero
from GLXCurses.Utils import resize_text

# Unittest
class TestStyle(unittest.TestCase):

    def setUp(self):
        # Before the test start
        # Require for init the screen

        # The component to test

        # Display thing that because curses have flush the screen
        rows, columns = os.popen('stty size', 'r').read().split()
        self.columns = int(columns)
        self.width = self.columns - 7
        try:
            sys.stdout.write('\r')
            sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.columns))
            sys.stdout.flush()
        except ValueError:
            pass

    def tearDown(self):
        # When the test is finish
        # Require for ask to curse to clean up it

        # Display thing that because curses have flush the screen
        try:
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
        except ValueError:
            pass

    def test_clamp_to_zero(self):
        """Test Utils.clamp_to_zero()"""
        self.assertEqual(0, clamp_to_zero(None))
        self.assertEqual(0, clamp_to_zero(-42))
        self.assertEqual(0, clamp_to_zero(0))
        self.assertEqual(42, clamp_to_zero(42))
        self.assertRaises(TypeError, clamp_to_zero, float(42.42))

    def test_resize_text(self):
        """Test Utils.clamp_to_zero()"""
        text = "123456789"
        width = 10
        self.assertEqual(text, resize_text(text, width, '~'))
        width = 9
        self.assertEqual(text, resize_text(text, width, '~'))
        width = 8
        self.assertEqual('123~789', resize_text(text, width, '~'))
        width = 7
        self.assertEqual('123~789', resize_text(text, width, '~'))
        width = 6
        self.assertEqual('12~89', resize_text(text, width, '~'))
        width = 5
        self.assertEqual('12~89', resize_text(text, width, '~'))
        width = 4
        self.assertEqual('1~9', resize_text(text, width, '~'))
        width = 3
        self.assertEqual('1~9', resize_text(text, width, '~'))
        width = 2
        self.assertEqual('19', resize_text(text, width, '~'))
        width = 1
        self.assertEqual('1', resize_text(text, width, '~'))
        width = 0
        self.assertEqual('', resize_text(text, width, '~'))

