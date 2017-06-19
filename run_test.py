#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Found on the web

import unittest
import test.all_tests
import sys
import os

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)

sys.stdout.write('\r')
sys.stdout.write('{:{width}.{width}}'.format(str('_' * columns), width=columns))
sys.stdout.write('\n\n\r')
sys.stdout.write('{:{width}.{width}}'.format('Galaxie-Curses Unit Test script'.upper(), width=columns))
sys.stdout.write('\n\r')
sys.stdout.write('{:{width}.{width}}'.format(str('_' * columns), width=columns))
sys.stdout.write('\n\r')
sys.stdout.flush()


testSuite = test.all_tests.create_test_suite()
text_runner = unittest.TextTestRunner(verbosity=0).run(testSuite)


