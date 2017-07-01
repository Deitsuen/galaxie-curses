#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string
from GLXCurses import glxc
from GLXCurses.Utils import glxc_type
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
    def test_glxc_type(self):
        """Test if VSeparator is GLXCurses Type"""
        vline = GLXCurses.VSeparator()
        self.assertTrue(glxc_type(vline))

    def test_draw_widget_in_area(self):
        """Test VSeparator.draw_widget_in_area()"""
        vline = GLXCurses.VSeparator()
        vline.draw_widget_in_area()

    def test_set_get_justify(self):
        """Test VSeparator.set_justify() and VSeparator.get_justify()"""
        vline = GLXCurses.VSeparator()

        vline.set_justify('CENTER')
        self.assertEqual(vline.get_justify(), glxc.JUSTIFY_CENTER)

        vline.set_justify('LEFT')
        self.assertEqual(vline.get_justify(), glxc.JUSTIFY_LEFT)

        vline.set_justify('RIGHT')
        self.assertEqual(vline.get_justify(), glxc.JUSTIFY_RIGHT)

        vline.set_justify(glxc.JUSTIFY_CENTER)
        self.assertEqual(vline.get_justify(), 'CENTER')

        vline.set_justify(glxc.JUSTIFY_LEFT)
        self.assertEqual(vline.get_justify(), 'LEFT')

        vline.set_justify(glxc.JUSTIFY_RIGHT)
        self.assertEqual(vline.get_justify(), 'RIGHT')

        self.assertRaises(TypeError, vline.get_justify, 'HELLO')

    # Internal
    def test__check_justify(self):
        """Test VSeparator._check_justify()"""
        vline = GLXCurses.VSeparator()

        # glxc.JUSTIFY_CENTER -> (self.get_width() / 2) - (self.get_preferred_width() / 2)
        vline._justify = glxc.JUSTIFY_CENTER
        vline.width = 124
        vline.preferred_width = 40
        vline._check_justify()
        self.assertEqual(vline._vseperator_x, 42)

        # glxc.JUSTIFY_LEFT -> self.get_spacing()
        vline._justify = glxc.JUSTIFY_LEFT
        vline.spacing = 24
        vline._check_justify()
        self.assertEqual(vline._vseperator_x, 24)

        # glxc.JUSTIFY_RIGHT -> self.get_width() - self.get_preferred_width() - self.get_spacing()
        vline._justify = glxc.JUSTIFY_RIGHT
        vline.width = 124
        vline.preferred_width = 80
        vline.spacing = 2
        vline._check_justify()
        self.assertEqual(vline._vseperator_x, 42)

    def test__get_estimated_preferred_width(self):
        """Test VSeparator._get_estimated_preferred_width()"""
        vline = GLXCurses.VSeparator()
        vline.spacing = 20
        self.assertEqual(vline._get_estimated_preferred_width(), 41)

    def test__get_estimated_preferred_height(self):
        """Test VSeparator._get_estimated_preferred_height()"""
        vline = GLXCurses.VSeparator()
        vline.y = 20
        vline.height = 20
        vline.spacing = 20
        self.assertEqual(vline._get_estimated_preferred_height(), 80)

    def test__set__get_vseperator_x(self):
        """Test VSeparator._set_vseperator_x() and VSeparator._get_vseperator_x()"""
        vline = GLXCurses.VSeparator()
        # call set_decorated() with 0 as argument
        vline._set_vseperator_x(0)
        # verify we go back 0
        self.assertEqual(vline._get_vseperator_x(), 0)
        # call set_decorated() with 0 as argument
        vline._set_vseperator_x(42)
        # verify we go back 0
        self.assertEqual(vline._get_vseperator_x(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, vline._set_vseperator_x, 'Galaxie')

    def test__set__get_vseperator_y(self):
        """Test VSeparator._set_vseperator_y() and VSeparator._get_vseperator_y()"""
        vline = GLXCurses.VSeparator()
        # call set_decorated() with 0 as argument
        vline._set_vseperator_y(0)
        # verify we go back 0
        self.assertEqual(vline._get_vseperator_y(), 0)
        # call set_decorated() with 0 as argument
        vline._set_vseperator_y(42)
        # verify we go back 0
        self.assertEqual(vline._get_vseperator_y(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, vline._set_vseperator_y, 'Galaxie')

if __name__ == '__main__':
    unittest.main()
