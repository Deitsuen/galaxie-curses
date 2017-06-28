#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import randint
import random
import string
import uuid
import sys
import os

# Require when you haven't GLXBob as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

import GLXCurses


# Unittest
class TestApplication(unittest.TestCase):

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

    # Test Size management
    # width
    def test_raise_typeerror_set_width(self):
        """Test raise TypeError of Application.set_width()"""
        self.assertRaises(TypeError, self.application.set_width, float(randint(1, 250)))

    def test_get_set_width(self):
        """Test Application.set_width() and Application.get_width() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_width(value_random_1)
        self.assertEqual(self.application.get_width(), value_random_1)

    # height
    def test_raise_typeerror_set_height(self):
        """Test raise TypeError of Application.set_height()"""
        self.assertRaises(TypeError, self.application.set_height, float(randint(1, 250)))

    def test_get_set_height(self):
        """Test Application.set_height() and Application.get_height() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_height(value_random_1)
        self.assertEqual(self.application.get_height(), value_random_1)

    # preferred_height
    def test_raise_typeerror_set_preferred_height(self):
        """Test raise TypeError of Application.set_preferred_height()"""
        self.assertRaises(TypeError, self.application.set_preferred_height, float(randint(1, 250)))

    def test_get_set_preferred_height(self):
        """Test Application.set_preferred_height() and Application.get_preferred_height() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_preferred_height(value_random_1)
        self.assertEqual(self.application.get_preferred_height(), value_random_1)

    # preferred_width
    def test_raise_typeerror_set_preferred_width(self):
        """Test raise TypeError of Application.set_preferred_width()"""
        self.assertRaises(TypeError, self.application.set_preferred_width, float(randint(1, 250)))

    def test_get_set_preferred_width(self):
        """Test Application.set_preferred_width() and Application.get_preferred_width() method's """
        value_random_1 = int(randint(8, 250))
        self.application.set_preferred_width(value_random_1)
        self.assertEqual(self.application.get_preferred_width(), value_random_1)

    def test_get_preferred_size(self):
        """Test Application.get_preferred_size()"""
        pass

    def test_set_preferred_size(self):
        """Test Application.set_preferred_size()"""
        pass

    def test_get_size(self):
        """Test Application.get_size()"""
        pass

    def test_set_get_x(self):
        """Test Application.set_y() and  Application.get_y()"""
        self.application.set_x(1)
        self.assertEqual(self.application.get_x(), 1)
        self.application.set_x(2)
        self.assertEqual(self.application.get_x(), 2)

    def test_set_get_y(self):
        """Test Application.set_y() and  Application.get_y()"""
        self.application.set_y(1)
        self.assertEqual(self.application.get_y(), 1)
        self.application.set_y(2)
        self.assertEqual(self.application.get_y(), 2)

    def test_set_get_name(self):
        """Test Application.set_name() and Application.get_name()"""
        try:
            # Python 2.7
            value_random_1 = u''.join(random.sample(string.letters, 52))
        except AttributeError:
            # Python 3
            value_random_1 = u''.join(random.sample(string.ascii_letters, 52))

        self.application.set_name(value_random_1)
        self.assertEqual(self.application.get_name(), value_random_1)

    def test_set_name_max_size(self):
        """Test Application.set_name() maximum size"""
        # Create a random string it have a len superior to 256 chars
        value_random_1 = u''
        try:
            # Python 2.7
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
            value_random_1 += u''.join(random.sample(string.letters, 52))
        except AttributeError:
            # Python 3
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))
            value_random_1 += u''.join(random.sample(string.ascii_letters, 52))

        # Try to set name with the to long string
        self.assertRaises(ValueError, self.application.set_name, value_random_1)

    def test_set_name_type(self):
        """Test Application.set_name() maximum size"""
        self.assertRaises(TypeError, self.application.set_name, int(randint(1, 42)))

    def test_set_get_style(self):
        """Test Application.set_style()"""
        style = GLXCurses.Style()

        self.application.set_style(style)
        self.assertEqual(style, self.application.get_style())

    def test_set_style_raise(self):
        """Test Application.set_style() raise TypeError"""
        self.assertRaises(TypeError, self.application.set_style, int())

    def test_add_window(self):
        """Test Application.add_window()"""
        # create a new window
        window = GLXCurses.Window()

        # check if window parent is not self.application
        self.assertNotEqual(window.get_parent(), self.application)

        # check the size of the children windows list before add a window
        windows_list_size_before = len(self.application._get_windows_list())

        # add a window to the application
        self.application.add_window(window)

        # check the size of the children windows list after add a window
        windows_list_size_after = len(self.application._get_windows_list())

        # we must have one more children on the list
        self.assertGreater(windows_list_size_after, windows_list_size_before)

        # we get the last windows children element
        the_last_children_on_list = self.application._get_windows_list()[-1]

        # the last list element must contain the same reference to our window
        self.assertEqual(the_last_children_on_list['WIDGET'], window)

        # check if the application is the parent of our window
        self.assertEqual(window.get_parent(), self.application)

    def test_add_window_raise(self):
        """Test Application.add_window() raise TypeError"""
        self.assertRaises(TypeError, self.application.add_window, int())

    def test_remove_window(self):
        """Test Application.remove_window()"""
        # create a new window
        window1 = GLXCurses.Window()
        window2 = GLXCurses.Window()

        # add a window to the application
        self.application.add_window(window1)

        # add a second window to the application
        self.application.add_window(window2)

        # the last list element must contain the same reference to our window
        self.assertEqual(self.application._get_active_window(), window2)

        self.application.remove_window(window2)

        # we get again the last windows children element
        self.assertEqual(self.application._get_active_window(), window1)

    def test_refresh(self):
        """Test Application.refresh() method """
        self.application.refresh()

    def test_draw(self):
        """Test Application.draw() method """
        self.application.draw()

    # def test_getch(self):
    #     """Test Application.getch() method"""
    #     pass

    def test_close(self):
        """Test Application.close() method """
        self.application.close()

    # Test Internal methode
    def test__set__get_windows_list(self):
        """Test Application children windows list"""
        # List creation
        tested_list = [1, 2, 3]

        # flush teh children windows list with our list
        self.application._set_windows_list(tested_list)

        # list must be equal
        self.assertEqual(self.application._get_windows_list(), tested_list)

        # check if worng type is detected
        self.assertRaises(TypeError, self.application._set_windows_list, int())

        # Let the Application children list to None
        self.application._set_windows_list(list())

    def test__add_child_to_windows_list(self):
        """Test Application child add to the children windows list"""
        # create a new window
        window = GLXCurses.Window()

        # check the size of the children windows list before add a window
        windows_list_size_before = len(self.application._get_windows_list())

        # add a window to the children window list
        self.application._add_child_to_windows_list(window)

        # check the size of the children windows list after add a window
        windows_list_size_after = len(self.application._get_windows_list())

        # we must have one more children on the list
        self.assertGreater(windows_list_size_after, windows_list_size_before)

        # let list of children empty
        self.application._set_windows_list(list())

    def test__set_get_active_window_id(self):
        """Test Application._set_active_window_id() and Application._get_active_window_id()"""
        value1 = uuid.uuid1().int
        value2 = uuid.uuid1().int
        self.application._set_active_window_id(value1)
        self.assertEqual(self.application._get_active_window_id(), value1)
        self.assertNotEqual(self.application._get_active_window_id(), value2)

    def test__set__get_active_window_id_raise(self):
        """Test Application._set_active_window_id() TypeError"""
        self.assertRaises(TypeError, self.application._set_active_window_id, float())

    def test__set__get_active_window(self):
        """Test Application displayed Window"""
        # let list of children empty
        self.application._set_windows_list(list())

        # create a new window
        window = GLXCurses.Window()

        # add a window
        self.application.add_window(window)

        # _get_displayed_window() must return the last added window
        self.assertEqual(self.application._get_active_window(), window)

    def test__set__get_menubar(self):
        """Test Application._set_menubar() and Application._get_menubar()"""
        menubar = GLXCurses.MenuBar()

        self.assertEqual(self.application._get_menubar(), None)

        self.application.add_menubar(menubar)

        self.application._set_menubar(menubar)
        self.assertEqual(self.application._get_menubar(), menubar)

    def test__set__get_statusbar(self):
        """Test Application._set_statusbar() and Application._get_statusbar()"""
        statusbar = GLXCurses.StatusBar()

        self.assertEqual(self.application._get_statusbar(), None)

        self.application.add_statusbar(statusbar)

        self.application._set_statusbar(statusbar)
        self.assertEqual(self.application._get_statusbar(), statusbar)

    def test__set__get_toolbar(self):
        """Test Application._set_toolbar() and Application._get_toolbar()"""
        toolbar = GLXCurses.ToolBar()

        self.assertEqual(self.application._get_toolbar(), None)

        self.application.add_toolbar(toolbar)

        self.application._set_toolbar(toolbar)
        self.assertEqual(self.application._get_toolbar(), toolbar)

if __name__ == '__main__':
    unittest.main()
