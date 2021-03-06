#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Application
from GLXCurses import Widget
from GLXCurses import EntryBuffer
from GLXCurses import glxc
from GLXCurses.Utils import clamp_to_zero
from GLXCurses.Utils import resize_text
import curses
import logging
import GLXCurses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author:the Galaxie Curses Team, all rights reserved
__author__ = u'the Galaxie Curses Project'


def _put(item):
    entries = list(item)
    return entries


class Entry(Widget):
    def __init__(self):
        Widget.__init__(self)
        ##############
        # Property's #
        ##############

        self.glxc_type = 'GLXCurses.Entry'

        # Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed.
        # Default value: False
        self.activates_default = False

        # Pango thing don't know if i'll kepp it
        self.attributes = None

        # Text buffer object which actually stores entry text.
        self.buffer = EntryBuffer()

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

        # Additional hints (beyond 'purpose') that allow input methods to fine-tune their behaviour
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
        self.invisible_char = unicode('*')

        # Whether the invisible char has been set for the GLXCurses.Entry
        # Default value: False
        self.invisible_char_set = False

        # Maximum number of characters for this entry. Zero if no maximum.
        # Allowed values: [0,65535]
        # Default value: 0
        self.max_length = 0

        # The desired maximum width of the entry, in characters.
        # If this property is set to -1, the width will be calculated aumovtomatically.
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

        # Number of the cursor position in the buffer
        self.position = 0

        # Subscribtions
        self.connect('active', Entry._emit_activate_signal(self))
        self.connect('backspace', Entry._emit_backspace_signal(self))
        self.connect('copy-clipboard', Entry._emit_copy_clipboard_signal(self))
        self.connect('cut-clipboard', Entry._emit_cut_clipboard_signal(self))
        self.connect('delete-from-cursor', Entry._emit_delete_from_cursor_signal(self))
        self.connect('icon-press', Entry._emit_icon_press_signal(self))
        self.connect('icon-release', Entry._emit_icon_release_signal(self))
        self.connect('insert-at-cursor', Entry._emit_insert_at_cursor_signal(self))
        self.connect('move-cursor', Entry._emit_move_cursor_signal(self))
        self.connect('paste-clipboard', Entry._emit_paste_clipboard_signal(self))
        self.connect('populate-popup', Entry._emit_populate_popup_signal(self))
        self.connect('preedit-changed', Entry._emit_preedit_changed_signal(self))
        self.connect('toggle-overwrite', Entry._emit_toggle_overwrite_signal(self))

        # Internal Widget Setting
        self.text = None
        self._x_offset = 0
        self._y_offset = 0

        # Interface
        self.interface = '|'
        self.interface_selected = '|>'
        self.button_border = self.interface

        # Size management
        self._update_preferred_sizes()

        # Justification: LEFT, RIGHT, CENTER
        self._justify = glxc.JUSTIFY_CENTER

        # PositionType: CENTER, TOP, BOTTOM
        self._position_type = glxc.POS_CENTER

        ############
        # Internal #
        ############
        # Widget
        # Make a Style heritage attribute

        # Size management
        self.set_preferred_height(1)

        # Sensitive
        self.set_can_focus(1)
        self.set_can_default(1)
        self.set_sensitive(1)
        self.states_list = None
        self.position = 0

        # Subscription
        self.connect('MOUSE_EVENT', Entry._handle_mouse_event)

        # States
        self.curses_mouse_states = {
            curses.BUTTON1_PRESSED: 'BUTTON1_PRESS',
            curses.BUTTON1_RELEASED: 'BUTTON1_RELEASED',
            curses.BUTTON1_CLICKED: 'BUTTON1_CLICKED',
            curses.BUTTON1_DOUBLE_CLICKED: 'BUTTON1_DOUBLE_CLICKED',
            curses.BUTTON1_TRIPLE_CLICKED: 'BUTTON1_TRIPLE_CLICKED',

            curses.BUTTON2_PRESSED: 'BUTTON2_PRESSED',
            curses.BUTTON2_RELEASED: 'BUTTON2_RELEASED',
            curses.BUTTON2_CLICKED: 'BUTTON2_CLICKED',
            curses.BUTTON2_DOUBLE_CLICKED: 'BUTTON2_DOUBLE_CLICKED',
            curses.BUTTON2_TRIPLE_CLICKED: 'BUTTON2_TRIPLE_CLICKED',

            curses.BUTTON3_PRESSED: 'BUTTON3_PRESSED',
            curses.BUTTON3_RELEASED: 'BUTTON3_RELEASED',
            curses.BUTTON3_CLICKED: 'BUTTON3_CLICKED',
            curses.BUTTON3_DOUBLE_CLICKED: 'BUTTON3_DOUBLE_CLICKED',
            curses.BUTTON3_TRIPLE_CLICKED: 'BUTTON3_TRIPLE_CLICKED',

            curses.BUTTON4_PRESSED: 'BUTTON4_PRESSED',
            curses.BUTTON4_RELEASED: 'BUTTON4_RELEASED',
            curses.BUTTON4_CLICKED: 'BUTTON4_CLICKED',
            curses.BUTTON4_DOUBLE_CLICKED: 'BUTTON4_DOUBLE_CLICKED',
            curses.BUTTON4_TRIPLE_CLICKED: 'BUTTON4_TRIPLE_CLICKED',

            curses.BUTTON_SHIFT: 'BUTTON_SHIFT',
            curses.BUTTON_CTRL: 'BUTTON_CTRL',
            curses.BUTTON_ALT: 'BUTTON_ALT'
        }

        self.EntryBuffer = EntryBuffer()

        ############
        # Internal #
        ############

        self.cursor = '|'

    def draw_widget_in_area(self):

        # Many Thing's
        # Check if the text can be display
        text_have_necessary_width = (self.get_preferred_width() >= 1)
        text_have_necessary_height = (self.get_preferred_height() >= 1)
        if not text_have_necessary_height or not text_have_necessary_width:
            return

        if self.get_text():

            # Check if the text can be display
            text_have_necessary_width = (self.get_preferred_width() >= 1)
            text_have_necessary_height = (self.get_preferred_height() >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                self._draw_button()

    def _draw_button(self):
        self._check_selected()
        self._update_preferred_sizes()
        self._check_justify()
        self._check_position_type()

        if self.state['UNSELECTED']:
            self._draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_text('dark', 'STATE_INSENSITIVE'),
                    background=self.get_style().get_color_text('bg', 'STATE_PRELIGHT')
                )
            )

        elif self.state['PRELIGHT']:
            self._draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_text('dark', 'STATE_INSENSITIVE'),
                    background=self.get_style().get_color_text('bg', 'STATE_PRELIGHT')
                )
            )
        elif self.state['NORMAL']:
            self._draw_the_good_button(
                color=self.get_style().get_color_pair(
                    foreground=self.get_style().get_color_text('text', 'STATE_NORMAL'),
                    background=self.get_style().get_color_text('bg', 'STATE_PRELIGHT')
                )
            )

    def _draw_the_good_button(self, color):
        try:
            # Interface management
            self.get_curses_subwin().addstr(
                self._y_offset,
                self._x_offset,
                self.button_border,
                color
            )

        except curses.error:
            pass
        try:

            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = resize_text(self.get_text(), self.get_width() - len(self.button_border), '~')
            self.get_curses_subwin().addstr(
                self._y_offset,
                self._x_offset,
                message_to_display,
                color
            )
        except curses.error:
            pass
        try:
            # Interface management
            message_to_display = resize_text(self.get_text(), self.get_width() - len(self.button_border), '~')
            self.get_curses_subwin().insstr(
                self._y_offset,
                self._x_offset,
                self.button_border,
                color
            )

        except curses.error:
            pass

    def _check_selected(self):
        if self.get_can_focus():
            if Application().get_is_focus() == self.get_widget_id():
                self.set_is_focus(True)
                self.button_border = self.interface_selected
                self._update_preferred_sizes()
                self.state['UNSELECTED'] = False
            else:
                self.state['UNSELECTED'] = True
                self.set_is_focus(False)
                self.button_border = self.interface
                self._update_preferred_sizes()
        else:
            pass

    def _update_preferred_sizes(self):
        self.set_preferred_width(self._get_estimated_preferred_width())
        self.set_preferred_height(self._get_estimated_preferred_height())

    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width

        :return: a estimated preferred width
        :rtype: int
        """
        if self.get_text():
            estimated_preferred_width = 0
            estimated_preferred_width += len(self.get_text())
            estimated_preferred_width += len(self.button_border)
        else:
            estimated_preferred_width = 0
            estimated_preferred_width += len(self.button_border)

        return estimated_preferred_width

    def _get_estimated_preferred_height(self):
        """
        Estimate a preferred height, by consider Y Location

        :return: a estimated preferred height
        :rtype: int
        """
        estimated_preferred_height = 1
        return estimated_preferred_height

    def _check_justify(self):
        """Check the justification of the X axe"""
        width = self.get_width()
        preferred_width = self.get_preferred_width()

        self._set_x_offset(0)
        if self.get_justify() == glxc.JUSTIFY_CENTER:
            # Clamp value and impose the center
            if width is None:
                estimated_width = 0
            elif width <= 0:
                estimated_width = 0
            elif width == 1:
                estimated_width = 0
            else:
                estimated_width = int(width / 2)

            # Clamp value and impose the center
            if preferred_width is None:
                estimated_preferred_width = 0
            elif preferred_width <= 0:
                estimated_preferred_width = 0
            elif preferred_width == 1:
                estimated_preferred_width = 0
            else:
                estimated_preferred_width = int(preferred_width / 2)

            # Make the compute
            final_value = int(estimated_width - estimated_preferred_width)

            # clamp the result
            if final_value <= 0:
                final_value = 0

            # Finally set the value
            self._set_x_offset(final_value)

        elif self.get_justify() == glxc.JUSTIFY_LEFT:

            # Finally set the value
            self._set_x_offset(0)

        elif self.get_justify() == glxc.JUSTIFY_RIGHT:
            # Clamp estimated_width
            estimated_width = clamp_to_zero(width)

            # Clamp preferred_width
            estimated_preferred_width = clamp_to_zero(preferred_width)

            # Make the compute
            final_value = int(estimated_width - estimated_preferred_width)

            # clamp the result
            if final_value <= 0:
                final_value = 0

            # Finally set the value
            self._x_offset = final_value

    def _check_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        height = self.get_height()
        preferred_height = self.get_preferred_height()

        if self.get_position_type() == glxc.POS_CENTER:
            # Clamp height
            if height is None:
                estimated_height = 0
            elif height <= 0:
                estimated_height = 0
            elif height == 1:
                # prevent a 1/2 = float(0.5) case
                estimated_height = 0
            else:
                estimated_height = int(height / 2)

            # Clamp preferred_height
            if preferred_height is None:
                estimated_preferred_height = 0
            elif preferred_height <= 0:
                estimated_preferred_height = 0
            elif preferred_height == 1:
                # prevent a 1/2 = float(0.5) case
                estimated_preferred_height = 0
            else:
                estimated_preferred_height = int(preferred_height / 2)

            # Make teh compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            self._set_y_offset(final_value)

        elif self.get_position_type() == glxc.POS_TOP:
            self._set_y_offset(0)

        elif self.get_position_type() == glxc.POS_BOTTOM:
            # Clamp height
            estimated_height = clamp_to_zero(height)

            # Clamp preferred_height
            estimated_preferred_height = clamp_to_zero(preferred_height)

            # Make the compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            # Clamp height
            estimated_height = clamp_to_zero(height)

            # Clamp preferred_height
            estimated_preferred_height = clamp_to_zero(preferred_height)

            # Make the compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            self._set_y_offset(final_value)

    def _set_x_offset(self, value=None):
        """
        Set _x

        :param value: A value to set to _x attribute
        :type value: int or None
        :raise TypeError: when value is not int or None
        """
        if type(value) is None or type(value) == int:
            self._x_offset = value
        else:
            raise TypeError(u'>value< must be a int or None type')

    def get_justify(self):
        """
        Return the Justify of the CheckButton

         Justify:
          - LEFT
          - CENTER
          - RIGHT

        :return: str
        """
        return self._justify

    def get_position_type(self):
        """
        Return the Position Type

        PositionType:
         .glxc.POS_TOP
         .glxc.POS_CENTER
         .glxc.POS_BOTTOM

        :return: str
        """
        return self._position_type

    def _set_y_offset(self, value=None):
        """
        Set _y

        :param value: A value to set to _y attribute
        :type value: int or None
        :raise TypeError: when value is not int or None
        """
        if type(value) is None or type(value) == int:
            self._y_offset = value
        else:
            raise TypeError(u'>y< must be a int or None type')

    def _set_state_prelight(self, value):
        if bool(value):
            self.state['PRELIGHT'] = True
        else:
            self.state['PRELIGHT'] = False

    def _get_y_offset(self):
        """
        Return the _y space add to text for position computation

        :return: y attribute
        """
        return self._y_offset

    def _get_x_offset(self):
        """
        Return the x space add to text for justify computation

        :return: _label_x attribute
        """
        return self._x_offset

    def _handle_mouse_event(self, event_signal, event_args):
        if self.get_sensitive():
            (mouse_event_id, x, y, z, event) = event_args
            # Be sure we select really the Button
            y -= self.y
            x -= self.x
            if self._get_y_offset() >= y > self._get_y_offset() - self.get_preferred_height():
                if (self._get_x_offset() - 1) + len(self.button_border) + len(self.get_text()) >= x > (
                            self._get_x_offset() - 1):
                    # We are sure about the button have been clicked
                    self.states_list = '; '.join(state_string for state,
                                                                  state_string in
                                                 self.curses_mouse_states.viewitems()
                                                 if event & state)
                    # INTERNAL METHOD
                    # BUTTON1
                    if event == curses.BUTTON1_PRESSED:
                        Application().set_is_focus(self)
                        self._check_selected()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON1_RELEASED:
                        Application().set_is_focus(self)
                        self._check_selected()
                        self._set_state_prelight(False)
                    if event == curses.BUTTON1_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON1_DOUBLE_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON1_TRIPLE_CLICKED:
                        Application().set_is_focus(self)

                    # BUTTON2
                    if event == curses.BUTTON2_PRESSED:
                        Application().set_is_focus(self)
                        self._check_selected()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON2_RELEASED:
                        self._set_state_prelight(False)
                        Application().set_is_focus(self)
                    if event == curses.BUTTON2_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON2_DOUBLE_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON2_TRIPLE_CLICKED:
                        Application().set_is_focus(self)

                    # BUTTON3
                    if event == curses.BUTTON3_PRESSED:
                        Application().set_is_focus(self)
                        self._check_selected()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON3_RELEASED:
                        self._set_state_prelight(False)
                        Application().set_is_focus(self)
                    if event == curses.BUTTON3_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON3_DOUBLE_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON3_TRIPLE_CLICKED:
                        Application().set_is_focus(self)

                    # BUTTON4
                    if event == curses.BUTTON4_PRESSED:
                        Application().set_is_focus(self)
                        self._check_selected()
                        self._set_state_prelight(True)
                    elif event == curses.BUTTON4_RELEASED:
                        self._set_state_prelight(False)
                        Application().set_is_focus(self)
                    if event == curses.BUTTON4_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON4_DOUBLE_CLICKED:
                        Application().set_is_focus(self)
                    if event == curses.BUTTON4_TRIPLE_CLICKED:
                        Application().set_is_focus(self)

                    if event == curses.BUTTON_SHIFT:
                        pass
                    if event == curses.BUTTON_CTRL:
                        pass
                    if event == curses.BUTTON_ALT:
                        pass

                    # Create a Dict with everything
                    instance = {
                        'class': self.__class__.__name__,
                        'label': self.get_text(),
                        'id': self.get_widget_id()
                    }
                    # EVENT EMIT
                    # Application().emit(self.curses_mouse_states[event], instance)
                    self.emit(self.curses_mouse_states[event], instance)
            else:
                # Nothing the better is to clean the prelight
                self._set_state_prelight(False)
        else:
            logging.debug(
                self.__class__.__name__ + ': ' + self.get_text() + ' ' + self.get_widget_id() + 'is not sensitive.')

    def set_statusbar(self, context_id, signal_context_id, button_context_id, arrow_pressed_context_id, select_id):
        statusbar = GLXCurses.StatusBar()

        statusbar_context_id = {"context_id": statusbar.get_context_id(context_id),
                                "signal_context_id": statusbar.get_context_id(signal_context_id),

                                "button_context_id": statusbar.get_context_id(button_context_id),
                                "arrow_pressed_context_id": statusbar.get_context_id(arrow_pressed_context_id)
                                }
        return statusbar_context_id[select_id]

    def get_statusbar(self, choice_id):
        status = self.set_statusbar('exemple', 'SIGNAL', 'BUTTON', 'ARROW_PRESSED', choice_id)
        return status

    def add_text(self, chars):
        hash_list = str(self.get_text())

        # Emit a signal

        self.emit_add_text()

        # Because we are like that we return something
        return self.set_text((hash_list + chars))

    def emit_add_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'add-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    def remove_text(self):

        # Convert the string to a list like a master ...
        hash_list = list(self.get_text())

        del hash_list[-1]

        # Emit a signal
        self.emit_deleted_text()

        # Because we are like that we return something
        return self.set_text(''.join(hash_list))

    def emit_deleted_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'deleted-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    def move_cursor(self, pos):
        """
        This function "move_cursor()"
        pops a cursor and moves the cursor left and right of the buffer

        :param pos: determines the direction of the cursor in the buffer
        """

        hash_list = _put(self.get_text())

        if pos == glxc.PROGRESS_LEFT_TO_RIGHT:  # pops a cursor and moves the cursor only to the right of the buffer

            if self.cursor in hash_list:
                self.position += 1
                hash_list.insert(self.position, self.cursor)
                if self.cursor in hash_list:
                    hash_list.remove(self.cursor)
            else:
                self.get_text()
                hash_list.insert(self.position, self.cursor)

            return self.set_text(''.join(hash_list))

        else:
            pass

        if pos == glxc.PROGRESS_RIGHT_TO_LEFT:  # pops a cursor and move the cursor only the left of the buffer

            if self.cursor in hash_list:
                hash_list.remove(self.cursor)
                if not self.cursor in hash_list:
                    self.position -= 1
                    hash_list.insert(self.position, self.cursor)

            else:
                hash_list.insert(self.position, self.cursor)

            return self.set_text(''.join(hash_list))

        else:
            pass

    def destroy(self):
        raise NotImplementedError

    def new(self):
        """
        Creates a new entry.

        :return: A new GLXCurse Entry Widget
        :rtype: GLXCurse.Widget
        """
        self.__init__()
        return self

    def new_with_buffer(self, buffer):
        """
        Creates a new entry with the specified text buffer.

        :param buffer: The buffer to use for the new GLXCurses.Entry.
        :return: A Entry Buffer object.
        :rtype: GLXCurse.Widget
        """
        self.__init__()
        self.set_buffer(buffer)
        return self

    def get_buffer(self):
        """
        Get the GLXCurses.EntryBuffer object which holds the text for this widget.

        :return: A EntryBuffer object.
        :rtype: GLXCurse.Widget
        """
        return self.buffer

    def set_buffer(self, buffer):
        """
        Set the EntryBuffer object which holds the text for this widget.

        :param buffer: The buffer to use for the GLXCurses.Entry.
        """
        self.buffer = buffer

    def set_text(self, text=None):
        """
        Sets the text in the widget to the given value, replacing the current contents.

        :param text: The new text
        :type text: String

        .. seealso:: GLXCurses.EntryBuffer().set_text()
        """

        self.get_buffer().set_text(text)

    def get_text(self):
        """
        Retrieves the contents of the entry widget. See also gtk_editable_get_chars().

        This is equivalent to:
        ``
        self.buffer = GLXCurses.EntryBuffer()
        self.buffer.get_text()
        ``
        :return: A pointer to the contents of the widget as a string. \
        This string points to internally allocated storage in the widget and must not be freed, \
        modified or stored.
        :rtype: String
        """
        return self.get_buffer().get_text()

    def get_text_length(self):
        """
        Retrieves the current length of the text in entry .

        This is equivalent to:
        ``
        self.buffer = GLXCurses.EntryBuffer()
        self.buffer.get_length()
        ``

        :return: The current number of characters in GtkEntry, or 0 if there are none.
        :rtype: Int in range 0-65536
        """
        return self.get_buffer().get_length()

    def get_text_area(self):
        """
        Gets the area where the entry’s text is drawn.
        This function is useful when drawing something to the entry in a draw callback.

        If the entry is not realized, text_area is filled with zeros.

        :return: A list of information X, Y and Size Width, Height . returned information are the complet allowed area,
        :rtype: List(X, Y , Width, Height)
        """
        padding = 0
        self.get_height() - (padding * 2),
        self.get_width() - (padding * 2),
        self.get_y() + padding,
        self.get_x() + padding

        raise NotImplementedError

    def set_visibility(self, visible):
        """
        Sets whether the contents of the entry are visible or not.

        When visibility is set to FALSE, characters are displayed as the invisible char, and will also appear that
        way when the text in the entry widget is copied elsewhere.

        By default, GLXCurse picks the best invisible character available in the current font,
        but it can be changed with set_invisible_char().

        .. note:: You probably want to set “input_purpose” to glx.INPUT_PURPOSE_PASSWORD or glx.INPUT_PURPOSE_PIN to \
        inform input methods about the purpose of this entry, in addition to setting visibility to FALSE.

        """
        if bool(visible):
            self.visibility = True
        else:
            self.visibility = False

    def set_invisible_char(self, ch=u'*'):
        """
        Sets the character to use in place of the actual text when set_visibility() has been called to set text
        visibility to FALSE.

        .. note:: this is the character used in “password mode” to show the user how many characters have been typed.

        By default, GLXCurse picks the best invisible char available in the current font.

        .. note:: If you set the invisible char to 0, then the user will get no feedback at all; \
        there will be no text on the screen as they type

        :param ch: a Unicode character
        """
        self.invisible_char = unicode(ch)

    def unset_invisible_char(self):
        """"
        Unsets the invisible char previously set with set_invisible_char().
        So that the default invisible char is used again.

        """
        self.invisible_char = unicode('*')

    def set_max_length(self, max):
        """
        Sets the maximum allowed length of the contents of the widget.
        If the current contents are longer than the given length, then they will be truncated to fit.

        This is equivalent to:
        ``
        self.buffer = GLXCurses.EntryBuffer()
        self.buffer.set_max_length()
        ``

        :param max: The maximum length of the entry, or 0 for no maximum. (other than the maximum length of entries.) \
        The value passed in will be clamped to the range 0-65536.
        """
        self.get_buffer().set_max_length(max)

    def get_activates_default(self):
        """
        Retrieves the value set by set_activates_default().

        :return: TRUE if the entry will activate the default widget
        :rtype: Boolean
        """
        return bool(self.activates_default)

    def get_has_frame(self):
        """
        Gets the value set by set_has_frame().

        :return: whether the entry has a beveled frame
        """
        return self.has_frame

    def get_inner_border(self, border):
        """
        This function returns the entry’s “inner-border” property. See set_inner_border() for more information.

        BorderStyle Members:
        glxc.BORDER_STYLE_NONE      No visible border
        glxc.BORDER_STYLE_SOLID     A single line segment
        glxc.BORDER_STYLE_INSET     Looks as if the content is sunken into the canvas
        glxc.BORDER_STYLE_OUTSET    Looks as if the content is coming out of the canvas
        glxc.BORDER_STYLE_HIDDEN    Same as glxc.BORDER_STYLE_NONE
        glxc.BORDER_STYLE_DOTTED    A series of round dots
        glxc.BORDER_STYLE_DASHED    A series of square-ended dashes
        glxc.BORDER_STYLE_DOUBLE    Two parallel lines with some space between them
        glxc.BORDER_STYLE_GROOVE    Looks as if it were carved in the canvas
        glxc.BORDER_STYLE_RIDGE     Looks as if it were coming out of the canvas

        :return: a BorderStyle Constant or None if none was set
        """
        available_border_style = [
            glxc.BORDER_STYLE_NONE,
            glxc.BORDER_STYLE_SOLID,
            glxc.BORDER_STYLE_INSET,
            glxc.BORDER_STYLE_OUTSET,
            glxc.BORDER_STYLE_HIDDEN,
            glxc.BORDER_STYLE_DOTTED,
            glxc.BORDER_STYLE_DASHED,
            glxc.BORDER_STYLE_DOUBLE,
            glxc.BORDER_STYLE_GROOVE,
            glxc.BORDER_STYLE_RIDGE,
        ]
        if border in available_border_style:
            return self.inner_border
        elif border is None:
            return None
        else:
            self.set_inner_border(None)

    def get_width_chars(self):
        """
        Gets the value set by set_width_chars()

        :return: number of chars to request space for, or negative if unset
        """
        return self.width_chars

    def get_max_width_chars(self):
        """
        Retrieves the desired maximum width of entry , in characters.

        set_max_width_chars().

        :return: the maximum width of the entry, in characters
        """
        return self.max_width_chars

    def set_activates_default(self, setting):
        """
        If setting is TRUE, pressing Enter in the entry will activate the default widget for the window containing
        the entry.

        This usually means that the dialog box containing the entry will be closed, since the default
        widget is usually one of the dialog buttons.

        (For experts: if setting is TRUE, the entry calls activate_default() on the window containing the entry,
        in the default handler for the “activate” signal.)

        :param setting: TRUE to activate window’s default widget on Enter keypress
        :type setting: Boolean
        """
        self.activates_default = bool(setting)

    def set_has_frame(self, setting):
        """
        Sets whether the entry has a beveled frame around it.

        :param setting:
        :type setting: object
        """
        self.has_frame = setting

    def set_inner_border(self, border):
        """
        Sets entry’s inner-border property to border , or clears it if None is passed.
        The inner-border is the area around the entry’s text, but inside its frame.

        If set, this property overrides the inner-border style property. Overriding the style-provided border is
        useful when you want to do in-place editing of some text in a canvas or list widget, where pixel-exact
        positioning of the entry is important.

        :param border: a BorderStyle
        :type border: a BorderStyle Constant

        BorderStyle Members:
        glxc.BORDER_STYLE_NONE      No visible border
        glxc.BORDER_STYLE_SOLID     A single line segment
        glxc.BORDER_STYLE_INSET     Looks as if the content is sunken into the canvas
        glxc.BORDER_STYLE_OUTSET    Looks as if the content is coming out of the canvas
        glxc.BORDER_STYLE_HIDDEN    Same as glxc.BORDER_STYLE_NONE
        glxc.BORDER_STYLE_DOTTED    A series of round dots
        glxc.BORDER_STYLE_DASHED    A series of square-ended dashes
        glxc.BORDER_STYLE_DOUBLE    Two parallel lines with some space between them
        glxc.BORDER_STYLE_GROOVE    Looks as if it were carved in the canvas
        glxc.BORDER_STYLE_RIDGE     Looks as if it were coming out of the canvas

        """
        available_border_style = [
            glxc.BORDER_STYLE_NONE,
            glxc.BORDER_STYLE_SOLID,
            glxc.BORDER_STYLE_INSET,
            glxc.BORDER_STYLE_OUTSET,
            glxc.BORDER_STYLE_HIDDEN,
            glxc.BORDER_STYLE_DOTTED,
            glxc.BORDER_STYLE_DASHED,
            glxc.BORDER_STYLE_DOUBLE,
            glxc.BORDER_STYLE_GROOVE,
            glxc.BORDER_STYLE_RIDGE,
        ]
        if border in available_border_style:
            self.inner_border = border
        else:
            self.inner_border = None

    def set_width_chars(self, n_chars):
        """
        Changes the size request of the entry to be about the right size for n_chars characters. Note that it changes
        the size request, the size can still be affected by how you pack the widget into containers.

        If n_chars is -1, the size reverts to the default entry size.

        :param n_chars: width in chars
        """
        self.width_chars = n_chars

    def set_max_width_chars(self, n_chars):
        """
        Sets the desired maximum width in characters of entry

        :param n_chars: the new desired maximum width, in characters
        """
        self.max_width_chars = n_chars

    def get_invisible_char(self):
        """
        Retrieves the character displayed in place of the real characters for entries with visibility set to false.

        .. seealso:: set_invisible_char().

        :return: the current invisible char, or 0, if the entry does not show invisible text at all.
        """
        return self.invisible_char

    def set_alignment(self):
        pass

    def get_alignment(self):
        pass

    def set_placeholder_text(self):
        pass

    def get_placeholder_text(self):
        pass

    def set_overwrite_mode(self):
        pass

    def get_overwrite_mode(self):
        pass

    def get_layout(self):
        pass

    def get_layout_offsets(self):
        pass

    def layout_index_to_text_index(self):
        pass

    def text_index_to_layout_index(self):
        pass

    def set_attributes(self):
        pass

    def get_attributes(self):
        pass

    def get_max_length(self):
        """
        Retrieves the maximum allowed length of the text in buffer .

        .. seealso:: EntryBuffer.set_max_length().

        :return: the maximum allowed number of characters in EntryBuffer, or 0 if there is no maximum.
        :rtype: standard C int type
        """
        if 0 >= self.max_length:
            return 0
        else:
            return int(self.max_length)

    def get_visibility(self):
        pass

    def set_completion(self):
        pass

    def get_completion(self):
        pass

    def set_cursor_hadjustment(self):
        pass

    def get_cursor_hadjustment(scelf):
        pass

    def set_progress_fraction(self):
        pass

    def get_progress_fraction(self):
        pass

    def set_progress_pulse_step(self):
        pass

    def get_progress_pulse_step(self):
        pass

    def progress_pulse(self):
        pass

    def im_context_filter_keypress(self):
        pass

    def reset_im_context(self):
        pass

    def get_tabs(self):
        pass

    def set_tabs(self):
        pass

    def set_icon_from_pixbuf(self):
        pass

    def set_icon_from_stock(self):
        pass

    def set_icon_from_icon_name(self):
        pass

    def set_icon_from_gicon(self):
        pass

    def get_icon_storage_type(self):
        pass

    def get_icon_pixbuf(self):
        pass

    def get_icon_stock(self):
        pass

    def get_icon_name(self):
        pass

    def get_icon_gicon(self):
        pass

    def set_icon_activatable(self):
        pass

    def get_icon_activatable(self):
        pass

    def set_icon_sensitive(self):
        pass

    def get_icon_sensitive(self):
        pass

    def get_icon_at_pos(self):
        pass

    def set_icon_tooltip_text(self):
        pass

    def get_icon_tooltip_text(self):
        pass

    def set_icon_tooltip_markup(self):
        pass

    def get_icon_tooltip_markup(self):
        pass

    def set_icon_drag_source(self):
        pass

    def get_current_icon_drag_source(self):
        pass

    def get_icon_area(self):
        pass

    def set_input_purpose(self):
        pass

    def get_input_purpose(self):
        pass

    def set_input_hints(self):
        pass

    def get_input_hints(self):
        pass

    def grab_focus_without_selecting(self):
        pass

    # Signals

    def _emit_activate_signal(self, user_data=None):
        """
        The ::activate signal is emitted when the user hits the Enter key.

        While this signal is used as a keybinding signal, it is also commonly used by applications to intercept activation of entries.

        The default bindings for this signal are all forms of the Enter key.

        :param self: the object which received the signal
        :param user_data: user data set when the signal handler was connected.
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_backspace_signal(self, user_data=None):
        """
        The ::backspace signal is a keybinding signal which gets emitted when the user asks for it.

        The default bindings for this signal are Backspace and Shift-Backspace

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_copy_clipboard_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_cut_clipboard_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_delete_from_cursor_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_icon_press_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_icon_release_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_insert_at_cursor_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_move_cursor_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_paste_clipboard_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_populate_popup_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_preedit_changed_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        # TODO: Everything cher's
        pass

    def _emit_toggle_overwrite_signal(self, user_data=None):
        """
        The “toggle-overwrite” signal

        The ::toggle-overwrite signal is a keybinding signal which gets emitted to toggle the overwrite mode of the
        entry.

        The default bindings for this signal is Insert.

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()

        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'toggle-overwrite',
            'id': self.id,
            'user_data': user_data
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)
