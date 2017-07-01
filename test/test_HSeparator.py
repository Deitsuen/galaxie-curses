#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string
from GLXCurses import glxc
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
    def test_set_get_position_type(self):
        """Test HSeparator.set_position_type() and HSeparator.get_position_type()"""
        hline = GLXCurses.HSeparator()

        hline.set_position_type('CENTER')
        self.assertEqual(hline.get_position_type(), glxc.POS_CENTER)

        hline.set_position_type('TOP')
        self.assertEqual(hline.get_position_type(), glxc.POS_TOP)

        hline.set_position_type('BOTTOM')
        self.assertEqual(hline.get_position_type(), glxc.POS_BOTTOM)

        hline.set_position_type(glxc.POS_CENTER)
        self.assertEqual(hline.get_position_type(), 'CENTER')

        hline.set_position_type(glxc.POS_TOP)
        self.assertEqual(hline.get_position_type(), 'TOP')

        hline.set_position_type(glxc.POS_BOTTOM)
        self.assertEqual(hline.get_position_type(), 'BOTTOM')

        self.assertRaises(TypeError, hline.set_position_type, 'HELLO')

if __name__ == '__main__':
    unittest.main()
