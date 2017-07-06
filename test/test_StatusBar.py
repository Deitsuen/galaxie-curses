#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string

import sys
import os

# Require when you haven't GLXBob as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses
from GLXCurses.Utils import glxc_type


# Unittest
class TestStatusBar(unittest.TestCase):

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
    def test_glxc_type(self):
        """Test StatusBar type"""
        statusbar = GLXCurses.StatusBar()
        self.assertTrue(glxc_type(statusbar))

    def test_new(self):
        """Test StatusBar.new()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()
        # get the window id
        statusbar_id_take1 = statusbar.get_widget_id()
        # get must be a long
        self.assertEqual(type(statusbar_id_take1), unicode)
        # use new() method
        statusbar.new()
        # re get the window id
        statusbar_id_take2 = statusbar.get_widget_id()
        # get must be a long
        self.assertEqual(type(statusbar_id_take2), unicode)
        # id's must be different
        self.assertNotEqual(statusbar_id_take1, statusbar_id_take2)

    def test_get_context_id(self):
        """Test StatusBar.get_context_id()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()
        # generate a random string
        context_text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        # get the window id
        statusbar_context_id_take1 = statusbar.get_context_id(context_description=context_text)
        # get must be a long
        self.assertEqual(type(statusbar_context_id_take1), unicode)
        # test raises
        self.assertRaises(TypeError, statusbar.get_context_id, context_description=int())

    def test_push(self):
        """Test StatusBar.push()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()
        # generate a random string
        text_take1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        text_take2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        # get the window id
        context_id = statusbar.get_context_id(context_description=text_take1)
        # get stack size
        stack_len = len(statusbar.statusbar_stack)
        # call StatusBar.push() suppose to return a message id
        message_id = statusbar.push(context_id=context_id, text=text_take2)
        # check if returned value is a long type
        self.assertEqual(type(message_id), unicode)
        # compare stack size suppose to grow
        self.assertGreater(len(statusbar.statusbar_stack), stack_len)
        # compare last element
        self.assertEqual(statusbar.statusbar_stack[-1][0], context_id)
        self.assertEqual(statusbar.statusbar_stack[-1][1], text_take2)
        self.assertEqual(statusbar.statusbar_stack[-1][2], message_id)
        # test raises
        self.assertRaises(TypeError, statusbar.push, context_id=str(), text=text_take2)
        self.assertRaises(TypeError, statusbar.push, context_id=context_id, text=float())

    def test_pop(self):
        """Test StatusBar.pop()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()
        # Preparation push completely a thing and save every value's
        context_description_1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        text_1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        context_id_1 = statusbar.get_context_id(context_description=context_description_1)
        message_id_1 = statusbar.push(context_id=context_id_1, text=text_1)

        # compare last element
        self.assertEqual(statusbar.statusbar_stack[-1][0], context_id_1)
        self.assertEqual(statusbar.statusbar_stack[-1][1], text_1)
        self.assertEqual(statusbar.statusbar_stack[-1][2], message_id_1)

        # Preparation push completely a thing and save every value's
        context_description_2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        text_2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        context_id_2 = statusbar.get_context_id(context_description=context_description_2)
        message_id_2 = statusbar.push(context_id=context_id_2, text=text_2)

        # compare last element
        self.assertEqual(statusbar.statusbar_stack[-1][0], context_id_2)
        self.assertEqual(statusbar.statusbar_stack[-1][1], text_2)
        self.assertEqual(statusbar.statusbar_stack[-1][2], message_id_2)

        # POP
        statusbar.pop(context_id=context_id_2)

        # check if are back to previous element
        self.assertEqual(statusbar.statusbar_stack[-1][0], context_id_1)
        self.assertEqual(statusbar.statusbar_stack[-1][1], text_1)
        self.assertEqual(statusbar.statusbar_stack[-1][2], message_id_1)

    def test_remove(self):
        """Test StatusBar.remove()"""
        # create a window instance
        statusbar = GLXCurses.StatusBar()

        # get stack size
        stack_len = len(statusbar.statusbar_stack)

        # Preparation push completely a thing and save every value's
        context_description_1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        text_1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        context_id_1 = statusbar.get_context_id(context_description=context_description_1)
        message_id_1 = statusbar.push(context_id=context_id_1, text=text_1)

        # compare last element
        self.assertEqual(statusbar.statusbar_stack[-1][0], context_id_1)
        self.assertEqual(statusbar.statusbar_stack[-1][1], text_1)
        self.assertEqual(statusbar.statusbar_stack[-1][2], message_id_1)

        # compare stack size suppose to grow
        self.assertGreater(len(statusbar.statusbar_stack), stack_len)

        # remove
        statusbar.remove(context_id=context_id_1, message_id=message_id_1)

        # compare stack size suppose to grow
        self.assertEqual(len(statusbar.statusbar_stack), stack_len)

        # test raises
        self.assertRaises(TypeError, statusbar.remove, context_id=int(), message_id=message_id_1)
        self.assertRaises(TypeError, statusbar.remove, context_id=context_id_1, message_id=float())
        self.assertRaises(TypeError, statusbar.remove, context_id=context_id_1)
        self.assertRaises(TypeError, statusbar.remove, message_id=message_id_1)

if __name__ == '__main__':
    unittest.main()
