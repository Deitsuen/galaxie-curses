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

if __name__ == '__main__':
    unittest.main()
