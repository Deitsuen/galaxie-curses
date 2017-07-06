#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
from GLXCurses.Utils import clamp_to_zero
from GLXCurses.Utils import resize_text
from GLXCurses.Utils import glxc_type
from GLXCurses.Utils import id_generator
from GLXCurses import Window


# Unittest
class TestUtils(unittest.TestCase):

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

    def test_glxc_type(self):
        """Test Utils.glxc_type()"""
        self.assertTrue(glxc_type(Window()))
        self.assertFalse(glxc_type(int()))
        self.assertFalse(glxc_type())

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
        width = -1
        self.assertEqual('', resize_text(text, width, '~'))

        # Test Error
        self.assertRaises(TypeError, resize_text, (int(), width, '~'))
        self.assertRaises(TypeError, resize_text, (text, str(), '~'))
        self.assertRaises(TypeError, resize_text, (text, width, int()))

    def test_id_generator(self):
        """Test Utils.id_generator()"""
        id_1 = id_generator()
        self.assertEqual(type(id_1), type(unicode()))
        # max_iteration = 10000000 - Take 185.928s on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
        # max_iteration = 1000000  - Take 19.109s  on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
        # max_iteration = 100000   - Take 2.154    on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
        # max_iteration = 10000    - Take 0.515    on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz

        max_iteration = 10000
        for _ in range(1, max_iteration):
            id_2 = id_generator()
            self.assertEqual(type(id_2), type(unicode()))
            self.assertNotEqual(id_1, id_2)
