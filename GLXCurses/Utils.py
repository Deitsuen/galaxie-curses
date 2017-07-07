#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re
import time
import hashlib

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved


def glxc_type(thing_to_test=None):
    """
    Internal method for check if object pass as argument is GLXCurses Type Object

    :param thing_to_test = A object to test
    :type thing_to_test: object
    :return: True or False
    :rtype: bool
    """
    if hasattr(thing_to_test, 'glxc_type') and (thing_to_test.glxc_type == str(
                'GLXCurses.' + thing_to_test.__class__.__name__)):
        return True
    else:
        return False


def resize_text(text='', max_width=0, separator='~'):
    """
    Resize the text , and return a new text

    example: return '123~789' for '123456789' where max_width = 7 or 8

    :param text: the original text to resize
    :type text: str
    :param max_width: the size of the text
    :type max_width: int
    :param separator: a separator a in middle of the resize text
    :type separator: str
    :return: a resize text
    :rtype: str
    """
    # Try to quit as soon of possible
    if type(text) != str:
        raise TypeError('"text" must be a str type')
    if type(max_width) != int:
        raise TypeError('"max_width" must be a int type')
    if type(separator) != str:
        raise TypeError('"separator" must be a str type')

    # If we are here we haven't quit
    if max_width < len(text):
        if max_width <= 0:
            return str('')
        elif max_width == 1:
            return str(text[:1])
        elif max_width == 2:
            return str(text[:1] + text[-1:])
        elif max_width == 3:
            return str(text[:1] + separator[:1] + text[-1:])
        else:
            max_width -= len(separator[:1])
            max_div = int(max_width / 2)
            return str(text[:max_div] + separator[:1] + text[-max_div:])
    else:
        return str(text)


def clamp_to_zero(value=None):
    """
    Convert any value to positive integer

    :param value: a integer
    :type value: int
    :return: a integer
    :rtype: int
    """
    if type(value) == int or value is None:
        if value is None:
            return 0
        elif value <= 0:
            return 0
        else:
            return value
    else:
        raise TypeError(u'>value< must be a int or None type')


def new_id():
    """
    Generate a ID like u'E59E8457' , two chars by two chars it's a random HEX

    Default size : 8
    Default chars: 'ABCDEF0123456789'

    max_iteration = 10000000 - Take 99.114s  on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
    max_iteration = 1000000  - Take 9.920s   on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
    max_iteration = 100000   - Take 0.998s   on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz
    max_iteration = 10000    - Take 0.108s   on Intel(R) Core(TM) i7-2860QM CPU @ 2.50GHz

    :return: a string it represent a unique ID
    :rtype: str
    """
    return '%02x%02x%02x%02x'.upper() % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def is_valid_id(value):
    """
    Check if it's a valid id

    :param value: a id to verify
    :return: bool
    """
    allowed = re.compile(r"""
                         (
                             ^([0-9A-F]{8})$
                         )
                         """,
                         re.VERBOSE | re.IGNORECASE)
    try:
        if allowed.match(value) is None:
            return False
        else:
            return True
    except TypeError:
        return False
