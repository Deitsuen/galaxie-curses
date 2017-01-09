#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
import logging

import GLXCurses
from GLXCurses import glxc

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Entry(GLXCurses.Widget):

    def __init__(self):
        GLXCurses.Widget.__init__(self)

        # Property's
        # Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed.
        # Default value: False
        self.activates_default = False

        # Pango thing don't know if i'll kepp it
        self.attributes = None

        # Text buffer object which actually stores entry text.
        self.buffer = None

        # Whether password entries will show a warning when Caps Lock is on.
        # Note that the warning is shown using a secondary icon,
        # and thus does not work if you are using the secondary icon position for some other purpose.
        # Default value: TRUE
        self.caps_locks_warning = True

        # The auxiliary completion object to use with the entry. See GLX.Completion
        self.completion = None

        # The current position of the insertion cursor in chars.
        # Allowed values: [0,65535]
        # Default value: 0
        self.cursor_position = 0

        # Whether the entry contents can be edited.
        # Default value: TRUE
        self.editable = True

        # FALSE removes outside bevel from entry.
        # Default value: TRUE
        self.has_frame = True

        # Sets the text area's border between the text and the frame.
        self.inner_border = 0

        # Additionan hints (beyond 'purpose') that allow input methods to fine-tune their behaviour
        self.input_hints = None

        # The purpose of this text field.
        # This property can be used by on-screen keyboards and other input methods to adjust their behaviour.
        # ote that setting the purpose to GTK_INPUT_PURPOSE_PASSWORD or glxc.INPUT_PURPOSE_PIN
        # is independent from setting “visibility”.
        # Default value: glxc.INPUT_PURPOSE_FREE_FORM
        self.purpose = glxc.INPUT_PURPOSE_FREE_FORM


