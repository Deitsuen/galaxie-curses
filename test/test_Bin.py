#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
import os

# Require when you haven't GLXBob as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses


# Unittest
class TestBin(unittest.TestCase):

    def setUp(self):
        # Before the test start
        self.bin = GLXCurses.Bin()

    # Test
    def test_destroy(self):
        """Test Bin.destroy()"""
        self.assertRaises(NotImplementedError, self.bin.destroy)

    def test_add(self):
        """Test Bin.add()"""
        # Test add method for None parameter
        self.bin.add(None)
        # chek if it's None
        self.assertEqual(self.bin.get_child(), None)
        # Create a child
        child = GLXCurses.Bin()
        # Add the child
        self.bin.add(child)
        # We must have the child inside the child list
        self.assertEqual(self.bin.get_child()['WIDGET'], child)
        # Reset to None for be sur it remove the child
        self.bin.add(None)
        # We must have the None ins the child list
        self.assertEqual(self.bin.get_child(), None)
        # Test type error
        self.assertRaises(TypeError, self.bin.add, int())

    def test_get_child(self):
        """Test Bin.get_child()"""
        self.assertEqual(self.bin.get_child(), None)

if __name__ == '__main__':
    unittest.main()
