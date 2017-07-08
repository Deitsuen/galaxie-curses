#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from GLXCurses import Box
from GLXCurses.Utils import glxc_type
from GLXCurses import glxc


# Unittest
class TestBox(unittest.TestCase):

    # Test
    def test_glxc_type(self):
        """Test StatusBar type"""
        box = Box()
        self.assertTrue(glxc_type(box))

    def test_new(self):
        """Test Box.new()"""
        # check default value
        box1 = Box().new()
        self.assertEqual(glxc.ORIENTATION_HORIZONTAL, box1.orientation)
        self.assertEqual(0, box1.spacing)

        # check with value
        box1 = Box().new(orientation=glxc.ORIENTATION_VERTICAL, spacing=4)
        self.assertEqual(glxc.ORIENTATION_VERTICAL, box1.orientation)
        self.assertEqual(4, box1.spacing)

        # check error Type
        self.assertRaises(TypeError, box1.new, orientation='Galaxie', spacing=4)
        self.assertRaises(TypeError, box1.new, orientation=glxc.ORIENTATION_HORIZONTAL, spacing='Galaxie')

    def test_pack_start(self):
        """Test Box type"""
        box1 = Box()
        box2 = Box()
        box3 = Box()

        # If child is worng
        self.assertRaises(TypeError, box1.pack_start, child=None, expand=True, fill=True, padding=0)
        self.assertRaises(TypeError, box1.pack_start, child=box2, expand='Galaxie', fill=True, padding=0)
        self.assertRaises(TypeError, box1.pack_start, child=box2, expand=True, fill='Galaxie', padding=0)
        self.assertRaises(TypeError, box1.pack_start, child=box2, expand=True, fill=True, padding='Galaxie')

        # Can i get children list ?
        self.assertEqual(type(list()), type(box1.get_children()))

        # pack the child
        box1.pack_start(child=box2, expand=False, fill=False, padding=4)
        box1.pack_start(child=box3, expand=False, fill=False, padding=2)

        self.assertEqual(type(dict()), type(box1.get_children()[0]))

        self.assertEqual(box3, box1.get_children()[0]['widget'])
        self.assertEqual(False, box1.get_children()[0]['expand'])
        self.assertEqual(False, box1.get_children()[0]['fill'])
        self.assertEqual(2, box1.get_children()[0]['padding'])

    def test_pack_end(self):
        """Test Box.pack_end()"""
        box1 = Box()
        box2 = Box()
        box3 = Box()

        # If child is worng
        self.assertRaises(TypeError, box1.pack_end, child=None, expand=True, fill=True, padding=0)
        self.assertRaises(TypeError, box1.pack_end, child=box2, expand='Galaxie', fill=True, padding=0)
        self.assertRaises(TypeError, box1.pack_end, child=box2, expand=True, fill='Galaxie', padding=0)
        self.assertRaises(TypeError, box1.pack_end, child=box2, expand=True, fill=True, padding='Galaxie')

        # Can i get children list ?
        self.assertEqual(type(list()), type(box1.get_children()))

        # pack the child
        box1.pack_end(child=box2, expand=True, fill=True, padding=4)
        box1.pack_end(child=box3, expand=False, fill=False, padding=2)

        self.assertEqual(type(dict()), type(box1.get_children()[-1]))

        self.assertEqual(box3, box1.get_children()[-1]['widget'])
        self.assertEqual(False, box1.get_children()[-1]['expand'])
        self.assertEqual(False, box1.get_children()[-1]['fill'])
        self.assertEqual(2, box1.get_children()[-1]['padding'])

    def test_set_get_homogeneous(self):
        """Test Box.set_homogeneous() and Box.get_homogeneous()"""
        box1 = Box()

        box1.set_homogeneous(False)
        self.assertFalse(box1.get_homogeneous())
        box1.set_homogeneous(True)
        self.assertTrue(box1.get_homogeneous())
