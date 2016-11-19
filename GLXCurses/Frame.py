#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Bin import Bin

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class Frame(Bin):
    def __init__(self):
        Bin.__init__(self)
        self.set_name('Frame')

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

        self.preferred_height = 2
        self.preferred_width = 2

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
        self.shadow_type = 'SHADOW_NONE'

    # GLXC Frame Functions
    def draw_widget_in_area(self):

        # Apply the Background color
        self.get_curses_subwin().bkgdset(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        self.get_curses_subwin().bkgd(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

        # Check widgets to display
        if bool(self.get_child()):
            self.get_child().set_style(self.get_style())
            self.get_child().draw()

        # Create a box and add the name of the windows like a king, who trust that !!!
        if self.get_decorated():
            self.get_curses_subwin().box()
            if self.get_label():
                self.get_curses_subwin().addstr(
                    0,
                    1,
                    resize_text(self.get_label(), self.get_width() - 2, '~')
                )
        else:
            if self.get_label():
                self.get_curses_subwin().addstr(
                    0,
                    0,
                    resize_text(self.get_label(), self.get_width() - 1, '~')
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
        if not self.get_label_widget() or not self.get_label():
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
        return tuple((self.label_xalign, self.label_yalign))

    def set_shadow_type(self, type):
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
    def get_attr(self, elem, state):
        return self.attribute[elem][state]
