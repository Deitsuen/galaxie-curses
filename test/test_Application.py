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
        self.width = self.columns - 9
        sys.stdout.write('\r')
        sys.stdout.write('{:{width}.{width}}'.format(self.shortDescription(), width=self.width))
        sys.stdout.write(' ... ')


    def tearDown(self):
        # When the test is finish
        self.application.close()
        sys.stdout.write('OK\n\r')
        sys.stdout.flush()

    # Test Size management
    def test_get_set_width(self):
        """Test 'Application.set_width()' and 'Application.get_width()' method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_width(value_random_1)
        self.assertEqual(self.application.get_width(), value_random_1)

    def test_get_set_height(self):
        """Test 'Application.set_height()' and 'Application.get_height()' method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_height(value_random_1)
        self.assertEqual(self.application.get_height(), value_random_1)

if __name__ == '__main__':
    unittest.main()
