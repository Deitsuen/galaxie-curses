#!/usr/bin/env python
# -*- coding: utf-8 -*-


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


def resize_text(text, max_width, separator='~'):
    """
    Resize the text , and return a new text

    exemple: return '123~789' for '123456789' where max_width = 7 or 8

    :param text: the original text to resize
    :type text: str
    :param max_width: the size of the text
    :type max_width: int
    :param separator: a separator a in middle of the resize text
    :type separator: str
    :return: a resize text
    :rtype: str
    """
    if max_width < len(text):
        if max_width <= 0:
            return str('')
        elif max_width == 1:
            return str(text[:1])
        elif max_width == 2:
            return str(text[:1] + text[-1:])
        elif max_width == 3:
            return str(text[:1] + separator + text[-1:])
        else:
            max_width -= len(separator)
            max_div = int((max_width / 2))
            return str(text[:max_div] + separator + text[-max_div:])
    else:
        return text


def clamp_to_zero(value=None):
    """
    Convert any value to positive integer

    :param value: a interger
    :type value: int
    :return: int
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