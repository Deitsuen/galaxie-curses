#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Widget

__author__ = 'Tuux'


class Misc(Widget):
    """
    The Misc widget is an abstract widget which is not useful itself, but is used to derive subclasses which have
    alignment and padding attributes.

    The horizontal and vertical padding attributes allows extra space to be added around the widget.

    The horizontal and vertical alignment attributes enable the widget to be positioned within its allocated area.
    Note that if the widget is added to a container in such a way that it expands automatically to fill its allocated
    area, the alignment settings will not alter the widget's position.

    Note that the desired effect can in most cases be achieved by using the “halign”, “valign” and “margin”
    properties on the child widget

    .. warning:: To reflect this fact, all Misc API will be deprecated soon.
    """
    def __init__(self):
        """
        .. py:attribute:: xalign - The horizontal alignment, from 0.0 to 1.0
        .. py:attribute:: yalign - The vertical alignment, from 0.0 to 1.0
        .. py:attribute:: xpad   - The amount of space to add on the left and right of the widget, in characters
        .. py:attribute:: ypad   - The amount of space to add above and below the widget, in characters
        """
        Widget.__init__(self)
        self.xalign = 0.0
        self.xpad = 0
        self.yalign = 0.0
        self.ypad = 0

    def set_alignment(self, xalign, yalign):
        """
        Sets the alignment of the widget.

        :param xalign: the horizontal alignment, from 0 (left) to 1 (right).
        :param yalign:the vertical alignment, from 0 (top) to 1 (bottom).
        :type xalign: Float
        :type yalign: Float
        """
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
        """
        Gets the X and Y alignment of the widget within its allocation.

        .. seealso:: set_alignment()

        .. py:attribute:: xalign - location to store X alignment of misc , or NULL.
        .. py:attribute:: yalign - location to store Y alignment of misc , or NULL.

        :return: xalign, yalign
        :rtype: float, float
        """
        return self.xalign, self.yalign

    def set_padding(self, xpad, ypad):
        """
        Sets the amount of space to add around the widget.

        :param xpad: the amount of space to add on the left and right of the widget, in char.
        :param ypad: the amount of space to add on the top and bottom of the widget, in char.
        :type xpad: Float
        :type ypad: Float
        """
        self.xpad = int(xpad)
        self.ypad = int(ypad)

    def get_padding(self):
        """
        Gets the padding in the X and Y directions of the widget.

        .. seealso:: set_padding().

        .. py:attribute:: xpad   - location to store padding in the X direction, or NULL.
        .. py:attribute:: ypad - location to store padding in the Y direction, or NULL.

        :return: xpad, ypad
        :rtype: float, float        """
        return self.xpad, self.ypad
