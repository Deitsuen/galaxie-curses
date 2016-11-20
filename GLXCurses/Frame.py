#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses import glxc
from GLXCurses.Bin import Bin

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Frame(Bin):
    def __init__(self):
        Bin.__init__(self)
        self.set_name('Frame')

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        self.preferred_height = 2
        self.preferred_width = 2

        self.set_decorated(1)
        self.imposed_spacing = 1

        ####################
        # Frame Properties #
        ####################

        # The text of the frame's label
        self.label = ''

        # The widget to display in place of the usual frame label.
        self.label_widget = None

        # The horizontal alignment of the label widget in the range of 0.0 to 1.0
        self.label_xalign = 0

        # The vertical alignment of the decoration within the label widget height in the range of 0.0 to 1.0
        self.label_yalign = 0

        # The style of the frame's border; one of:
        # SHADOW_NONE
        # SHADOW_IN
        # SHADOW_OUT
        # SHADOW_ETCHED_IN
        # SHADOW_ETCHED_OUT
        self.shadow_type = glxc.SHADOW_NONE

    # GLXC Frame Functions
    def draw_widget_in_area(self):

        # Apply the Background color
        self.get_curses_subwin().bkgdset(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_style().get_attr('text', 'STATE_NORMAL'),
                bg=self.get_style().get_attr('bg', 'STATE_NORMAL'))
            )
        )
        self.get_curses_subwin().bkgd(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_style().get_attr('text', 'STATE_NORMAL'),
                bg=self.get_style().get_attr('bg', 'STATE_NORMAL'))
            )
        )

        # Check widgets to display
        if bool(self.get_child()):
            self.get_child().set_style(self.get_style())
            self.get_child().draw()

        # Create a box and add the name of the windows like a king, who trust that !!!
        self.get_curses_subwin().box()

        # Add the Label
        if self.get_label():
            self.get_curses_subwin().addstr(
                self._get_label_y(),
                self._get_label_x(),
                self._get_resided_label_text()
            )

    # The set_label() method sets the text of the label as specified by label.
    # If label is None the current label is removed.
    def set_label(self, label):
        if bool(label):
            self.label = label
        else:
            self.label = None

    # The get_label() method returns the text in the label widget.
    # If there is no label widget or the label widget is not a Label the method returns None.
    def get_label(self):
        if self.get_label_widget():
            return None
        else:
            return self.label

    # The set_label_widget() method set the label widget (usually to something other than a Label widget) for the frame.
    # This widget will appear embedded in the top edge of the frame as a title.
    def set_label_widget(self, label_widget):
        self.label_widget = label_widget

    # The get_label_widget() method retrieves the label widget for the frame. See set_label_widget().
    def get_label_widget(self):
        return self.label_widget

    def set_label_align(self, xalign, yalign):
        # xalign :
        # the horizontal alignment of the label widget along the top edge of the frame (in the range of 0.0 to 1.0)
        xalign = float(xalign)
        if xalign > 1.0:
            xalign = 1.0
        elif xalign < 0.0:
            xalign = 0.0
        # yalign :
        # the vertical alignment of the decoration with respect to the label widget (in the range 0.0 to 1.0)
        yalign = float(yalign)
        if yalign > 1.0:
            yalign = 1.0
        elif yalign < 0.0:
            yalign = 0.0

        self.label_xalign = xalign
        self.label_yalign = yalign

    def get_label_align(self):
        return self.label_xalign, self.label_yalign

    def set_shadow_type(self, type):
        type = str(type).upper()
        # The set_shadow_type() method sets the frame's shadow type to the value of type.
        # The type must be one of:
        # SHADOW_NONE
        # SHADOW_IN
        # SHADOW_OUT
        # SHADOW_ETCHED_IN
        # SHADOW_ETCHED_OUT
        self.shadow_type = type

    def get_shadow_type(self):
        return self.shadow_type

    # Internal
    def _get_label_x(self):
        xalign, yalign = self.get_label_align()
        value = 0
        value += int((self.get_width() - len(self.get_label())) * xalign)
        if value <= 0:
            value = self._get_imposed_spacing()
            return value
        if 0 < xalign <= 0.5:
            value += self._get_imposed_spacing()
        elif 0.5 <= xalign <= 1.0:
            value -= self._get_imposed_spacing()
        return value

    def _get_label_y(self):
        xalign, yalign = self.get_label_align()
        value = int(self.get_height() * yalign)
        if value < 0:
            value = 0
        return value

    def _get_resided_label_text(self, separator='~'):
        border_width = self.get_width() - len(self.get_label()) + (self._get_imposed_spacing() * 2)
        max_width = self.get_width() - (self._get_imposed_spacing() * 2)
        if border_width <= self._get_imposed_spacing() * 2 + 1:
            text_to_return = self.get_label()[:(max_width / 2) - 1] + separator + self.get_label()[-max_width / 2:]
            return text_to_return
        else:
            return self.get_label()

    def _get_imposed_spacing(self):
        return int(self.imposed_spacing)

    def _set_imposed_spacing(self, spacing):
        self.imposed_spacing = int(spacing)
