#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
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
        sys.stdout.write('[ OK ]')
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
        """Test Application.get_x()"""
        pass

    def test_get_y(self):
        """Test Application.get_y()"""
        pass

    def test_set_name(self):
        """Test Application.set_name()"""
        pass

    def test_get_name(self):
        """Test Application.get_name()"""
        pass

    def test_draw(self):
        """Test Application.draw()method's """
        self.application.draw()

if __name__ == '__main__':
    unittest.main()
