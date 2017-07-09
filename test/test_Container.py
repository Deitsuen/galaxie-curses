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

    def test_child_get(self):
        """Test Container.remove()"""
        # Use Container as main container (single child)
        # create our tested container
        container = Container()

        # Create a child
        child1 = Container()
        child2 = Container()

        # Add the child and test
        container.add(child1)
        self.assertEqual(container._get_child()['widget'], child1)

        # check if we receive a dict type
        self.assertEqual(type(container.child_get(child1)), type(dict()))

        self.assertEqual(container.child_get(child1), container._get_child()['properties'])

        # return None if child is not found
        self.assertEqual(None, container.child_get(child2))

        # Use Box as main container (multiple child)
        # create our tested container
        container_to_test = Box()

        # Create a child
        child_to_test1 = Container()
        child_to_test2 = Container()
        child_to_test3 = Container()

        # Add the child and test
        container_to_test.pack_start(child_to_test2)
        container_to_test.pack_start(child_to_test1)
        self.assertEqual(container_to_test.get_children()[0]['widget'], child_to_test1)
        self.assertEqual(
            container_to_test.get_children()[0]['properties'],
            container_to_test.child_get(child_to_test1)
        )
        # return None if child is not found
        self.assertEqual(None, container_to_test.child_get(child_to_test3))

        # check if we receive a dict type
        self.assertEqual(type(container_to_test.child_get(child_to_test1)), type(dict()))



