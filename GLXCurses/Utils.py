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
    if max_width < len(text):
        text_to_return = text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
        if len(text_to_return) == 1:
            text_to_return = text[:1]
        elif len(text_to_return) == 2:
            text_to_return = str(text[:1] + text[-1:])
        elif len(text_to_return) == 3:
            text_to_return = str(text[:1] + separator + text[-1:])
        return text_to_return
    else:
        return text
