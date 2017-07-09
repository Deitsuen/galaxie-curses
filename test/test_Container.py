#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Container
from GLXCurses import Box
from GLXCurses.Utils import glxc_type


# Unittest
class TestBin(unittest.TestCase):

    # Test
    def test_type(self):
        """Test Container type"""
        self.assertTrue(glxc_type(Container()))

    def test_add(self):
        """Test Container.add()"""
        container = Container()
        # Test add method for None parameter
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
        # Test type error
        self.assertRaises(TypeError, container.add, int())
        self.assertRaises(TypeError, container.add)

    def test_remove(self):
        """Test Container.remove()"""
        # create our tested container
        container = Container()

        # Create a child
        child1 = Container()
        child2 = Box()

        # Add the child and test
        container.add(child1)
        self.assertEqual(container._get_child()['widget'], child1)

        # remove and test
        container.remove(child1)
        self.assertEqual(container._get_child(), None)

        # Add the child and test
        container.add(child2)
        self.assertEqual(container._get_child()['widget'], child2)

        child2.pack_start(child1)
        self.assertEqual(child2.get_children()[0]['widget'], child1)

        # remove and test
        child2.remove(child1)
        self.assertEqual(len(child2.get_children()), 0)

        # we still have the child 2
        self.assertEqual(container._get_child()['widget'], child2)

        # we remove child 2
        container.remove(child2)
        self.assertEqual(container._get_child(), None)
