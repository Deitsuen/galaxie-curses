#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses import glxc
from GLXCurses.Misc import Misc
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


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


class Label(Misc):
    def __init__(self):
        Misc.__init__(self)
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('Label')

        # Label Properties
        # The current position of the insertion cursor in chars. Allowed values: >= 0. Default value: 0
        self.cursor_position = 0

        # justify
        # The alignment of the lines in the text of the label relative to each other.
        # The possible values are:
        # glxc.JUSTIFY_LEFT,
        # glxc.JUSTIFY_RIGHT,
        # glxc.JUSTIFY_CENTER,
        # glxc.JUSTIFY_FILL.
        # This does NOT affect the alignment of the label within its allocation.
        # Default value: glxc.JUSTIFY_LEFT
        self.justify = glxc.JUSTIFY_CENTER

        # The text of the label.
        # Default value: None
        self.label = None

        # The desired maximum width of the label, in characters.
        # If this property is set to -1, the width will be calculated automatically,
        # otherwise the label will request space for no more than the requested number of characters.
        # If the "width-chars" property is set to a positive value, then the "max-width-chars" property is ignored.
        # Allowed values: >= -1.
        # Default value: -1
        self.max_width_chars = -1

        # The mnemonic accelerator key for this label.
        # Default value: 16777215
        self.mnemonic_keyval = 16777215

        # The widget to be activated when the label's mnemonic key is pressed.
        self.mnemonic_widget = None

        # A string with _ characters in positions used to identify to characters in the text to underline.
        # Default value: None
        self.pattern = '_'

        # If True, the label text can be selected with the mouse.
        # Default value: False
        self.selectable = False

        # The position of the opposite end of the selection from the cursor in chars.
        # Allowed values: >= 0.
        # Default value: 0.
        self.selection_bound = 0

        # If True the label is in single line mode.
        # In single line mode, the height of the label does not depend on the actual text,
        # it is always set to ascent + descent of the font. This can be an advantage
        # in situations where resizing the label because of text changes would be distracting, e.g. in a statusbar.
        # Default value: False
        self.single_line_mode = False

        # If True the label tracks which links have been clicked.
        # It will then apply the "visited-link-color" color, instead of "link-color". False
        self.track_visited_links = False

        # If True, an underscore in the text indicates the next character should be used
        # for the mnemonic accelerator key.
        # Default value: False
        self.use_underline = False

        # The desired width of the label, in characters.
        # If this property is set to -1, the width will be calculated automatically,
        # otherwise the label will request either 3 characters or the property value, whichever is greater.
        # Allowed values: >= -1.
        # Default value: -1.
        self.width_chars = -1

        # If True, wrap lines if the text becomes too wide.
        # Default value: False
        self.wrap = False

        # If line wrapping is on, this controls how the line wrapping is done.
        # The default is glxc.WRAP_WORD, which means wrap on word boundaries.
        self.wrap_mode = glxc.WRAP_WORD

        self.text_x = 0
        self.text_y = 0
        
        # Size management
        self.set_preferred_height(1)
        self.update_preferred_sizes()

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = glxc.JUSTIFY_CENTER

    ###########
    # Methods #
    ###########
    # The set_text() method sets the text within the Label widget.
    # It replaces any text that was there before and will clear any previously set mnemonic accelerators.
    def set_text(self, text):
        self.label = text
        self.update_preferred_sizes()

    # The get_text() method fetches the text from a label widget, as displayed on the screen.
    # This does not include any markup or embedded underscore characters indicating mnemonics. (See get_label()).
    def get_text(self):
        return self.label

    # The set_label() method sets the text of the label.
    # The label is parsed for embedded underscores and markup depending on
    # the values of the "use-underline" and "use-markup" properties.
    def set_label(self, text):
        self.label = text
        self.update_preferred_sizes()

    # The get_label() method returns the text from a label widget including any markup
    # and embedded underscores indicating mnemonics. (See get_text() that just returns the text).
    def get_label(self):
        return self.label

    # set_markup
    # set_use_markup
    # get_use_markup

    # The set_use_underline() method sets the "use-underline" property to the value of setting.
    # If setting is True,
    # an underscore in the text indicates the next character should be used for the mnemonic accelerator key.
    def set_use_underline(self, setting):
        if bool(setting):
            self.use_underline = True
        else:
            self.use_underline = False

    # The get_use_underline() method returns the value of the "use-underline" property.
    # If True an embedded underscore in the label indicates the next character is a mnemonic. See set_use_underline().
    def get_use_underline(self):
        return bool(self.use_underline)

    # set_markup_with_mnemonic

    # The get_mnemonic_keyval() method returns the value of the "mnemonic-keyval" property that contains the keyval
    # used for the mnemonic accelerator if one has been set on the label.
    # If there is no mnemonic set up it returns the void symbol keyval.
    def get_mnemonic_keyval(self):
        if self.mnemonic_keyval:
            return self.mnemonic_keyval
        else:
            return None

    # The set_mnemonic_widget() method sets the "mnemonic-widget" property using the value of widget.
    # This method associates the label mnemonic with a widget that will be activated
    #   when the mnemonic accelerator is pressed.
    # When the label is inside a widget (like a Button or a Notebook tab) it is automatically associated
    #  with the correct widget, but sometimes (i.e. when the target is a gtk.Entry next to the label)
    #  you need to set it explicitly using this function.
    # The target widget will be activated by emitting "mnemonic_activate" on it.
    def set_mnemonic_widget(self, widget):
        self.mnemonic_widget = widget
        # emitting "mnemonic_activate"

    # The get_mnemonic_widget() method retrieves the value of the "mnemonic-widget" property which is the target
    # of the mnemonic accelerator of this label.
    # See set_mnemonic_widget().
    def get_mnemonic_widget(self):
        return self.mnemonic_widget

    # The set_text_with_mnemonic() method sets the label's text from the string str.
    # If characters in str are preceded by an underscore,
    # they are underlined indicating that they represent a mnemonic accelerator.
    # The mnemonic key can be used to activate another widget, chosen automatically,
    # or explicitly using the set_mnemonic_widget() method.
    def set_text_with_mnemonic(self, string):
        mnemonic_index = str.find(self.pattern)
        if string.find("_") > 0:
            newstring = string.replace('_', '')
            self.set_text(newstring)

    def draw_widget_in_area(self):
        if self.get_text():
            # Check if the text can be display
            text_have_necessary_width = (self.get_preferred_width() + self.get_spacing() >= 1)
            text_have_necessary_height = (self.get_preferred_height() + self.get_spacing() >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                self.text_x = self.check_horizontal_justification()
                self.text_y = self.check_horizontal_position_type()
                self.draw_label()

    def check_horizontal_justification(self):
        # Check Justification
        self.text_x = 0
        if self.get_justify() == glxc.JUSTIFY_CENTER:
            self.text_x = (self.get_width() / 2) - (self.get_preferred_width() / 2)
        elif self.get_justify() == glxc.JUSTIFY_LEFT:
            self.text_x = 0 + self.get_spacing()
        elif self.get_justify() == glxc.JUSTIFY_RIGHT:
            self.text_x = self.get_width() - self.get_preferred_width()

        return self.text_x

    def check_horizontal_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        self.text_y = 0
        if self.get_position_type().upper() == glxc.JUSTIFY_CENTER:
            if (self.get_height() / 2) > self.get_preferred_height():
                self.text_y = (self.get_height() / 2) - self.get_preferred_height()
            else:
                self.text_y = 0
        elif self.get_position_type() == 'TOP':
            self.text_y = 0
        elif self.get_position_type() == 'BOTTOM':
            self.text_y = self.get_height() - self.get_preferred_height()

        return self.text_y

    def draw_label(self):
        # Draw the Horizontal Label with Justification and PositionType
        message_to_display = resize_text(self.get_text(), self.get_width() - (self.get_spacing() * 2), '~')
        self.get_curses_subwin().addstr(
            self.text_y,
            self.text_x,
            message_to_display,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_style().get_attr('text', 'STATE_NORMAL'),
                bg=self.get_style().get_attr('bg', 'STATE_NORMAL'))
            )
        )

    def update_preferred_sizes(self):
        if self.get_text():
            preferred_width = 0
            preferred_height = 1

            preferred_width += len(self.get_text())
            preferred_width += self.get_spacing() * 2

            self.set_preferred_height(preferred_height)
            self.set_preferred_width(preferred_width)
        else:
            return

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justify):
        justify = str(justify).upper()
        if justify == 'LEFT':
            self.justify = glxc.JUSTIFY_LEFT
        elif justify == 'CENTER':
            self.justify = glxc.JUSTIFY_CENTER
        elif justify == 'RIGHT':
            self.justify = glxc.JUSTIFY_RIGHT
        elif justify == glxc.JUSTIFY_LEFT:
            self.justify = glxc.JUSTIFY_LEFT
        elif justify == glxc.JUSTIFY_CENTER:
            self.justify = glxc.JUSTIFY_CENTER
        elif justify == glxc.JUSTIFY_RIGHT:
            self.justify = glxc.JUSTIFY_RIGHT
        else:
            self.justify = glxc.JUSTIFY_CENTER
        self.update_preferred_sizes()

    def get_justify(self):
        return self.justify

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = str(orientation).upper()
        self.update_preferred_sizes()

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self.update_preferred_sizes()

    def get_position_type(self):
        return self.position_type

    # Internal
    def _get_label_x(self):
        xalign, _ = self.get_alignment()
        xpadd, _ = self.get_padding()
        value = 0
        value += int((self.get_width() - len(self.get_label())) * xalign)
        if value <= 0:
            value = xpadd
            return value
        if 0 < xalign <= 0.5:
            value += xpadd
        elif 0.5 <= xalign <= 1.0:
            value -= xpadd
        return value

    def _get_label_y(self):
        _, yalign = self.get_alignment()
        _, ypadd = self.get_padding()

        value = int(self.get_height() * yalign)
        if value <= 0:
            value = ypadd
            return value
        if 0 < ypadd <= 0.5:
            value += ypadd
        elif 0.5 <= yalign <= 1.0:
            value -= ypadd
        return value

    def _get_resided_label_text(self, separator='~'):
        xpadd, _ = self.get_padding()
        border_width = self.get_width() - len(self.get_label()) + (xpadd * 2)
        max_width = self.get_width() - (xpadd * 2)
        if border_width <= xpadd * 2 + 1:
            text_to_return = self.get_label()[:(max_width / 2) - 1] + separator + self.get_label()[-max_width / 2:]
            return text_to_return
        else:
            return self.get_label()
