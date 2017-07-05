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
class TestMessageBar(unittest.TestCase):

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
        messagebar = GLXCurses.MessageBar()
        self.assertTrue(glxc_type(messagebar))

    def test_new(self):
        """Test StatusBar.new()"""
        # create a window instance
        messagebar = GLXCurses.MessageBar()
        # get the window id
        messagebar_id_take1 = messagebar.get_widget_id()
        # get must be a long
        self.assertEqual(type(messagebar_id_take1), long)
        # use new() method
        messagebar.new()
        # re get the window id
        messagebar_id_take2 = messagebar.get_widget_id()
        # get must be a long
        self.assertEqual(type(messagebar_id_take2), long)
        # id's must be different
        self.assertNotEqual(messagebar_id_take1, messagebar_id_take2)

    def test_get_context_id(self):
        """Test MessageBar.get_context_id()"""
        # create a window instance
        messagebar = GLXCurses.MessageBar()
        # generate a random string
        context_text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        # get the window id
        messagebar_context_id_take1 = messagebar.get_context_id(context_description=context_text)
        # get must be a long
        self.assertEqual(type(messagebar_context_id_take1), long)
        # test raises
        self.assertRaises(TypeError, messagebar.get_context_id, context_description=int())

    def test_push(self):
        """Test MessageBar.push()"""
        # create a window instance
        messagebar = GLXCurses.MessageBar()
        # generate a random string
        text_take1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        text_take2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        # get the window id
        context_id = messagebar.get_context_id(context_description=text_take1)
        # get stack size
        stack_len = len(messagebar.messagebar_stack)
        # call StatusBar.push() suppose to return a message id
        message_id = messagebar.push(context_id=context_id, text=text_take2)
        # check if returned value is a long type
        self.assertEqual(type(message_id), long)
        # compare stack size suppose to grow
        self.assertGreater(len(messagebar.messagebar_stack), stack_len)
        # compare last element
        self.assertEqual(messagebar.messagebar_stack[-1][0], context_id)
        self.assertEqual(messagebar.messagebar_stack[-1][1], text_take2)
        self.assertEqual(messagebar.messagebar_stack[-1][2], message_id)
        # test raises
        self.assertRaises(TypeError, messagebar.push, context_id=str(), text=text_take2)
        self.assertRaises(TypeError, messagebar.push, context_id=context_id, text=float())

if __name__ == '__main__':
    unittest.main()
