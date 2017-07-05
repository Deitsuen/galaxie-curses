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
from GLXCurses.Utils import glxc_type


# Unittest
class TestStatusBar(unittest.TestCase):

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
    def test_glxc_type(self):
        """Test StatusBar type"""
        statusbar = GLXCurses.StatusBar()
        self.assertTrue(glxc_type(statusbar))

    def test_new(self):
        """Test StatusBar.new()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()
        # get the window id
        statusbar_id_take1 = statusbar.get_widget_id()
        # get must be a long
        self.assertEqual(type(statusbar_id_take1), long)
        # use new() method
        statusbar.new()
        # re get the window id
        statusbar_id_take2 = statusbar.get_widget_id()
        # get must be a long
        self.assertEqual(type(statusbar_id_take2), long)
        # id's must be different
        self.assertNotEqual(statusbar_id_take1, statusbar_id_take2)

if __name__ == '__main__':
    unittest.main()
