#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


# The Misc widget is an abstract widget used to derive subclasses which have alignment and padding attributes.
# The horizontal and vertical padding attributes allow extra space to be added around the widget.
# The horizontal and vertical alignment attributes enable the widget to be positioned within its allocated area.
# The alignment values represent the fraction of available free space (allocation minus the widget size)
#  to place to the left or above the widget for x and y alignment respectively.
# Note that if the widget is added to a container in such a way that it expands automatically
#  to fill its allocated area, the alignment settings will have no effect.

class Misc(Widget):
    def __init__(self):
        Widget.__init__(self)

        # Misc Properties
        # The horizontal alignment, from 0.0 to 1.0
        self.xalign = 0.0

        # The amount of space to add on the left and right of the widget, in characters
        self.xpad = 0

        # The vertical alignment, from 0.0 to 1.0
        self.yalign = 0.0

        # The amount of space to add above and below the widget, in characters
        self.ypad = 0

    def set_alignment(self, xalign, yalign):
        # xalign :
        xalign = float(xalign)
        if xalign >= 1.0:
            xalign = 1.0
        elif xalign < 0.0:
            xalign = 0.0

        # yalign :
        yalign = float(yalign)
        if yalign >= 1.0:
            yalign = 1.0
        elif yalign < 0.0:
            yalign = 0.0

        self.xalign = xalign
        self.yalign = yalign

    def get_alignment(self):
        return self.xalign, self.yalign

    def set_padding(self, xpad, ypad):
        self.xpad = int(xpad)
        self.ypad = int(ypad)

    def get_padding(self):
        return self.xpad, self.ypad

