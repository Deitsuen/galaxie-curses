#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved

from GLXCurses import Application
import uuid

__author__ = u'the Galaxie Curses Project'


class Adjustment(object):
    """
    :Description:

    The :class:`Adjustment <GLXCurses.Adjustment.Adjustment>` object represents a value which has an associated
    lower and upper bound, together with step and page increments,and a page size.It is used within several widgets,
    including :class:`SpinButton <GLXCurses.SpinButton.SpinButton>`, :class:`Viewport <GLXCurses.Viewport.Viewport>`,
    and :class:`Range <GLXCurses.Range.Range>` (which is a base class for
    :class:`Scrollbar <GLXCurses.Scrollbar.Scrollbar>` and :class:`Scale <GLXCurses.Scale.Scale>`).

    The Adjustment object does not update the value itself.
    Instead it is left up to the owner of the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>`
    to control the value.
    """
    def __init__(self):
        """
        :Attributes Details:

        .. py:attribute:: lower

           The minimum value of the adjustment.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: page_increment

           The page increment of the adjustment.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: page_size

           The page size of the adjustment. Note that the page-size is irrelevant and should be set to zero if the
           adjustment is used for a simple scalar value, e.g. in a
           :class:`SpinButton <GLXCurses.SpinButton.SpinButton>`.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: step_increment

           The step increment of the adjustment.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: minimum_increment

           The smaller of step increment and page increment.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: upper

           The maximum value of the adjustment.

           Note that values will be restricted by ``upper - page-size`` if the page-size property is nonzero.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        .. py:attribute:: value

           The value of the adjustment.

              +---------------+-------------------------------+
              | Type          | :py:data:`float`              |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0.0                           |
              +---------------+-------------------------------+

        :Methods:
        """
        self.lower = float(0.0)
        self.page_increment = float(0.0)
        self.page_size = float(0.0)
        self.step_increment = float(0.0)
        self.minimum_increment = float(0.0)
        self.upper = float(0.0)
        self.value = float(0.0)

        # Internal
        self.id = uuid.uuid1().int

        self.two = None
        self.average = None

    def get_lower(self):
        """
        Retrieves the minimum value of the adjustment.

        :return: The current minimum value of the adjustment
        :rtype: float
        """
        return float(self.lower)

    def get_page_increment(self):
        """
        Retrieves the page increment of the adjustment.

        :return: The current page increment of the adjustment
        :rtype: float
        """
        return float(self.page_increment)

    def get_page_size(self):
        """
        Retrieves the page size of the adjustment.

        :return: The current page size of the adjustment
        :rtype: float
        """
        return float(self.page_size)

    def get_step_increment(self):
        """
        Retrieves the step increment of the adjustment.

        :return: The current step increment of the adjustment.
        :rtype: float
        """
        return float(self.step_increment)

    def get_minimum_increment(self):
        """
        Gets the smaller of step increment and page increment.

        :return: the minimum increment of adjustment
        :rtype: float
        """
        return float(self.minimum_increment)

    def get_value(self):
        """
        Gets the current value of the adjustment. See set_value()

        :return: A current value Adjustment
        :rtype: float
        """
        return float(self.value)

    def get_upper(self):
        """
        Retrieves the maximum value of the adjustment.

        :return: The current maximum value of the adjustment
        :rtype: float
        """
        return float(self.upper)

    def set_lower(self, lower):
        """
        Sets the minimum value of the adjustment.
        """
        self.lower = lower

    def set_value(self, value):
        """
        Sets the Adjustment value. The value is clamped to lie between “lower” and “upper”.

        Note that for adjustments which are used in a :class:`Scrollbar <GLXCurses.Scrollbar.Scrollbar>`,
        the effective range of allowed values goes from
        :py:attr:`lower` to :py:attr:`upper` - :py:attr:`page_size`.

        """
        if value < self.get_lower():
            self.value = self.get_lower()
        elif value > self.get_upper():
            self.value = self.get_upper()
        else:
            self.value = value

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

    def configure(self, value, lower, upper, step_increment, page_increment, page_size):
        """
        Sets all properties of the adjustment at once.

        Use this function to avoid multiple emissions of the “changed” signal.
        See :func:`Adjustment.set_lower() <GLXCurses.Adjustment.Adjustment.set_lower()>` for
        an alternative way of compressing multiple emissions of “changed” into one.

        :param value: the new value
        :param lower: the new minimum value
        :param upper: the new maximum value
        :param step_increment: the new step increment
        :param page_increment: the new page increment
        :param page_size: the new page size
        :type value: float
        :type lower: float
        :type upper: float
        :type step_increment: float
        :type page_increment: float
        :type page_size: float
        """
        self.set_value(value)
        self.set_lower(lower)
        # self.set_upper(upper)
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

