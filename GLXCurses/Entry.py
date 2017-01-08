#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Widget import Widget
from GLXCurses import glxc

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Entry(Widget):
    def __init__(self):
        Widget.__init__(self)

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

        # The invisible character is used when masking entry contents (in \"password mode\")").
        # When it is not explicitly set with the “invisible-char” property, GLXCurses determines the character
        # to use from a list of possible candidates, depending on availability in the current font.
        # This style property allows the theme to prepend a character to the list of candidates.
        # Default value: *
        self.invisible_char = '*'

        # Whether the invisible char has been set for the GLXCurses.Entry
        # Default value: False
        self.invisible_char_set = False

        # Maximum number of characters for this entry. Zero if no maximum.
        # Allowed values: [0,65535]
        # Default value: 0
        self.max_length = 0

        # The desired maximum width of the entry, in characters.
        # If this property is set to -1, the width will be calculated automatically.
        # Allowed values: >= -1
        # Default value: -1
        self.max_width_chars = -1

        # If text is overwritten when typing in the GLXCurses.Entry.
        # Default value: False
        self.overwrite_mode = False

        # The text that will be displayed in the GtkEntry when it is empty and unfocused.
        # Default value: None
        self.placeholder_text = None

        # If :populate-all is TRUE, the “populate-popup” signal is also emitted for touch popups.
        # Default Value: False
        self.populate_all = False

        # The current fraction of the task that's been completed.
        # Allowed values: [0,1]
        # Default value: 0
        self.progress_fraction = 0

        # The fraction of total entry width to move the progress bouncing block for each call
        # to self.progress_pulse
        # Allowed values: [0,1]().
        # Default value: 0.1
        self.progress_pulse_step = 0.1

        # Number of pixels of the entry scrolled off the screen to the left.
        # Allowed values: >= 0
        # Default Value: 0
        self.scroll_offset = 0

        # The position of the opposite end of the selection from the cursor in chars.
        # Allowed values: [0,65535]
        # Default Value: 0
        self.selection_bound = 0

        # Which kind of shadow to draw around the entry when “has-frame” is set to True.
        self.shadow_type = glxc.SHADOW_IN

        # A list of tabstop locations to apply to the text of the entry.
        self.tabs = list()

        # The contents of the entry.
        self.text = ""

        # The length of the text in the GLXCurses.Entry.
        # Allowed values: <= 65535
        # Default Value: 0
        self.text_length = 0

        # When True, pasted multi-line text is truncated to the first line.
        # Default value: False
        self.truncate_multiline = False

        # False displays the "invisible char" instead of the actual text (password mode).
        # Default Value: True
        self.visibility = True

        # Number of characters to leave space for in the entry.
        # Allowed Value: >= -1
        # Default Value: -1
        self.width_chars = -1

        # The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.
        # Allowed values: [0,1]
        # Default Value: 0
        self.xalign = 0

