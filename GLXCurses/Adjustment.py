#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved

from GLXCurses import Application
import uuid

__author__ = 'Deitsuen'


class Adjustment(object):
    """
    The Adjustment
    object represents a value which has an associated lower and upper bound,
    together with step and page increments,and a page size.It is used within several  widgets,
    including SpinButton, Viewport, and Range (which is a base class for Scrollbar and Scale).
    The Adjustment object does not update the value itself.
    Instead it is left up to the owner of the GtkAdjustment to control the value.
    """

    def __init__(self):
        # Creates a new Adjustment
        self.value = 2.0
        self.lower = 1.0
        self.upper = 15.0
        self.step_increment = 1.0
        self.page_increment = 10.0
        self.page_size = 20.0
        self.id = uuid.uuid1().int

        self.two = None
        self.average = None

    def get_value(self):
        """
        Gets the current value of the adjustment. See set_value()

        :return: A current value Adjustment
        :rtype: GLXCurses.Adjustment.set_value()
        """
        return float(self.value)

    def set_value(self):
        """
        Sets the Adjustment value.The value is clamped to lie between “lower” and “upper”.
        Note that for adjustments which are used in a Scrollbar,
        the effective range of allowed values goes from “lower” to “upper” - “page-size”.

        """
        if self.value > self.upper:
            self.value = self.upper

        elif self.value < self.lower:
            self.value = self.lower

        else:
            self.value = self.value

    def clamp_page(self):
        """
        Updates the “value” property to ensure that the range between lower and upper is in the current page
        (i.e. between “value” and “value” + “page-size”).
        If the range is larger than the page size, then only the start of it will be in the current page.
        A “value-changed” signal will be emitted if the value is changed.
        """
        self.two = self.lower and self.upper
        self.average = self.two + self.page_size

        step = 0.1

        if self.two >= self.page_size:
            self.upper = self.lower
            self.lower = self.upper

        while self.lower <= self.upper:
            yield self.lower

            self.lower += step

        self.value_changed()

    def changed(self):
        """
        Emits a “changed” signal from the Adjustment.
        This is typically called by the owner of the Adjustment,
        after it has changed any of the Adjustment properties other than the value.
        """

        instance = {
            'class': self.__class__.__name__,
            'type': 'changed',
            'id': self.id
        }
        # EVENT EMIT
        Application.emit('SIGNALS', instance)

    def value_changed(self):
        """
        Emits a “value-changed” signal from the Adjustment.
        This is typically called by the owner of the Adjustment
        after it has changed the “value” property.
        """

        instance = {
            'class': self.__class__.__name__,
            'type': 'value-changed',
            'id': self.id
        }
        # EVENT EMIT

        Application.emit('SIGNALS', instance)

    def configure(self):
        """
        Sets all properties of the adjustment at once.
        Use this function to avoid multiple emissions of the “changed” signal.
        """
        default_value = 10

        d = default_value

        self.value = d
        self.lower = d
        self.upper = d
        self.page_size = d
        self.step_increment = d
        self.page_increment = d

        self.changed()
        self.value_changed()

    def get_lower(self):
        """
        Get the lower value.

        :return: The minimum value of the adjustment.
        :rtype: GLXCurses.Adjustment().lower
        """
        raise NotImplementedError

    def get_page_increment(self):
        """
        Get the page_increment value.

        :return: Retrieves the page increment of the adjustment.
        :rtype: GLXCurses.Adjustment().page_increment
        """
        raise NotImplementedError

    def get_page_size(self):
        """
        Get the page_size value.

        :return: Retrieves the page size of the adjustment.
        :rtype: GLXCurses.Adjustment().page_size
        """
        # truc = Adjustment()
        # print truc.get_lower()
        # tesst = ["%g" % x for x in truc.clamp_page()]   #Sa test la fonction#
        # print tesst
        raise NotImplementedError

    def get_step_increment(self):
        """
        Get the step_increment value.

        :return: Retrieves the step increment of the adjustment.
        :rtype: GLXCurses.Adjustment().step_increment
        """
        raise NotImplementedError

    def get_upper(self):
        """
        Get upper value

        :return: Retrieves the maximum value of the adjustment.
        :rtype: GLXCurses.Adjustment().upper
        """
        raise NotImplementedError
