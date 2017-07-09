#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Container


# Unittest
class TestBin(unittest.TestCase):

    # Test
    def test_add(self):
        """Test Container.add()"""
        container = Container()
        # Test add method for None parameter
        container.add(None)
        # chek if it's None
        self.assertEqual(container._get_child(), None)
        # Create a child
        child1 = Container()
        child2 = Container()
        # Add the child
        container.add(child1)
        # We must have the child inside the child list
        self.assertEqual(container._get_child()['widget'], child1)
        # Add the child
        container.add(child2)
        # We must have the child inside the child list
        self.assertEqual(container._get_child()['widget'], child2)
        # Reset to None for be sur it remove the child
        container.add(None)
        # We must have the None ins the child list
        self.assertEqual(container._get_child(), None)
        # Test type error
        self.assertRaises(TypeError, container.add, int())

