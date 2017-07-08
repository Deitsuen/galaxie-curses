#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Bin


# Unittest
class TestBin(unittest.TestCase):

    def setUp(self):
        # Before the test start
        self.bin = Bin()

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
        child1 = Bin()
        child2 = Bin()
        # Add the child
        self.bin.add(child1)
        # We must have the child inside the child list
        self.assertEqual(self.bin.get_child()['widget'], child1)
        # Add the child
        self.bin.add(child2)
        # We must have the child inside the child list
        self.assertEqual(self.bin.get_child()['widget'], child2)
        # Reset to None for be sur it remove the child
        self.bin.add(None)
        # We must have the None ins the child list
        self.assertEqual(self.bin.get_child(), None)
        # Test type error
        self.assertRaises(TypeError, self.bin.add, int())

    def test_get_child(self):
        """Test Bin.get_child()"""
        self.assertEqual(self.bin.get_child(), None)
