#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string

import sys
import os

# Require when you haven't GLXBob as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses


# Unittest
class TestWindow(unittest.TestCase):

    def setUp(self):
        # Before the test start
        self.application = GLXCurses.Application()
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
        self.application.close()
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

    # Test
    def test_new(self):
        """Test Window.new()"""
        # create a window instance
        window = GLXCurses.Window()
        # get the window id
        window_id_take1 = window.get_widget_id()
        # get must be a long
        self.assertEqual(type(window_id_take1), unicode)
        # use new() method
        window.new()
        # re get the window id
        window_id_take2 = window.get_widget_id()
        # get must be a long
        self.assertEqual(type(window_id_take2), unicode)
        # id's must be different
        self.assertNotEqual(window_id_take1, window_id_take2)

    def test_set_get_application(self):
        """Test Window.set_application() and Window.get_application()"""
        window = GLXCurses.Window()
        window.set_application(None)
        self.assertEqual(None, window.get_application())
        window.set_application(self.application)
        self.assertEqual(self.application, window.get_application())

    def test_set_application_raise(self):
        """Test Window.set_application() TypeError"""
        window = GLXCurses.Window()
        self.assertRaises(TypeError, window.set_application, int(42))

if __name__ == '__main__':
    unittest.main()
