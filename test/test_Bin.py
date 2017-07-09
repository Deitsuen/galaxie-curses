#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Bin


# Unittest
class TestBin(unittest.TestCase):

    # Test
    def test_get_child(self):
        """Test Bin.get_child()"""
        glxc_bin = Bin()
        self.assertEqual(glxc_bin.get_child(), None)
