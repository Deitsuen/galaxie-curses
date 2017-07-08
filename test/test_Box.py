#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Box
from GLXCurses.Utils import glxc_type


# Unittest
class TestBox(unittest.TestCase):

    def setUp(self):
        # Before the test start
        self.box = Box()

    # Test
    def test_glxc_type(self):
        """Test StatusBar type"""
        box = Box()
        self.assertTrue(glxc_type(box))
