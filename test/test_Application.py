#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string

import sys
import os
import uuid

# Require when you haven't GLXBob as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses

# Unittest
class TestEventBus(unittest.TestCase):
    def setUp(self):
        # Before the test start
        self.application = GLXCurses.Application()
        rows, columns = os.popen('stty size', 'r').read().split()
        self.columns = int(columns)
        self.width = self.columns - 7
        sys.stdout.write('\r')
        sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.columns))
        sys.stdout.flush()

    def tearDown(self):
        # When the test is finish
        self.application.close()
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

    # Test Size management
    # width
    def test_raise_typeerror_set_width(self):
        """Test raise TypeError of Application.set_width()"""
        self.assertRaises(TypeError, self.application.set_width, float(randint(1, 250)))

    def test_get_set_width(self):
        """Test Application.set_width() and Application.get_width() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_width(value_random_1)
        self.assertEqual(self.application.get_width(), value_random_1)

    # height
    def test_raise_typeerror_set_height(self):
        """Test raise TypeError of Application.set_height()"""
        self.assertRaises(TypeError, self.application.set_height, float(randint(1, 250)))

    def test_get_set_height(self):
        """Test Application.set_height() and Application.get_height() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_height(value_random_1)
        self.assertEqual(self.application.get_height(), value_random_1)

    # preferred_height
    def test_raise_typeerror_set_preferred_height(self):
        """Test raise TypeError of Application.set_preferred_height()"""
        self.assertRaises(TypeError, self.application.set_preferred_height, float(randint(1, 250)))

    def test_get_set_preferred_height(self):
        """Test Application.set_preferred_height() and Application.get_preferred_height() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_preferred_height(value_random_1)
        self.assertEqual(self.application.get_preferred_height(), value_random_1)

    # preferred_width
    def test_raise_typeerror_set_preferred_width(self):
        """Test raise TypeError of Application.set_preferred_width()"""
        self.assertRaises(TypeError, self.application.set_preferred_width, float(randint(1, 250)))

    def test_get_set_preferred_width(self):
        """Test Application.set_preferred_width() and Application.get_preferred_width() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_preferred_width(value_random_1)
        self.assertEqual(self.application.get_preferred_width(), value_random_1)

    def test_get_preferred_size(self):
        """Test Application.get_preferred_size()"""
        pass

    def test_set_preferred_size(self):
        """Test Application.set_preferred_size()"""
        pass

    def test_get_size(self):
        """Test Application.get_size()"""
        pass

    def test_get_x(self):
        """Test Application.get_x() return a int after Application.draw() call"""
        # That the Application.draw() it set value to Application.x attribute
        self.application.draw()
        self.assertIsInstance(self.application.get_x(), int)

        # Create the main Application
        app = GLXCurses.Application()
        app.set_name('Galaxie-Curse Demo')

        # Create a Menu
        menu = GLXCurses.MenuModel()
        menu.app_info_label = app.get_name()

    def test_get_y(self):
        """Test Application.get_y() return a int after Application.draw() call"""
        # That the Application.draw() it set value to Application.y attribute
        # Test default value -> 0
        self.assertIsInstance(self.application.get_y(), int)
        self.assertEqual(self.application.get_y(), 0)

        # Create a Menu
        menu = GLXCurses.MenuModel()
        menu.app_info_label = self.application.get_name()

        self.application.add_menubar(menu)
        self.application.draw()
        self.assertEqual(self.application.get_y(), 1)

    def test_set_get_name(self):
        """Test Application.set_name() and Application.get_name()"""
        try:
            # Python 2.7
            value_random_1 = u''.join(random.sample(string.letters, 52))
        except AttributeError:
            # Python 3
            value_random_1 = u''.join(random.sample(string.ascii_letters, 52))

        self.application.set_name(value_random_1)
        self.assertEqual(self.application.get_name(), value_random_1)

    def test_set_name_max_size(self):
        """Test Application.set_name() maximum size"""
        # Create a random string it have a len superior to 256 chars
        value_random_1 = u''
        try:
            # Python 2.7
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
        except AttributeError:
            # Python 3
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))

        # Try to set name with the to long string
        self.assertRaises(ValueError, self.application.set_name, value_random_1)

    def test_set_name_type(self):
        """Test Application.set_name() maximum size"""
        value_random_1 = float(1.4)
        self.assertRaises(TypeError, self.application.set_name, int(randint(1, 42)))

    def test_draw(self):
        """Test Application.draw()method's """
        self.application.draw()


if __name__ == '__main__':
    unittest.main()
