#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved

from GLXCurses import Application
import uuid

__author__ = u'the Galaxie Curses Project'


# Reference Document: https://developer.gnome.org/gtk3/stable/GtkAdjustment.html
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

    def get_value(self):
        """
        Gets the current value of the adjustment. See set_value()

        :return: A current value Adjustment
        :rtype: float
        """
        return float(self.value)

    def set_value(self, value):
        """
        Set the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>` :py:attr:`value` attribute.

        The ``value`` passed as argument is clamped to lie between :py:attr:`lower` and :py:attr:`lower` attributes.

        .. note:: For adjustments which are used in a :class:`Scrollbar <GLXCurses.Scrollbar.Scrollbar>`, \
        the effective range of allowed values goes from \
        :py:attr:`lower` to :py:attr:`upper` - :py:attr:`page_size`.

        :raise TypeError: when ``value`` passed as argument is not a :py:data:`float`
        """
        if type(value) == float:
            if value < self.get_lower():
                self.value = self.get_lower()
            elif value > self.get_upper():
                self.value = self.get_upper()
            else:
                self.value = value
        else:
            raise TypeError(u'>value< argument must be a float')

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
        Emits a “changed” signal from the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>`.

        This is typically called by the owner of the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>`,
        after it has changed any of the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>`
        attributes other than the value.
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
        Emits a “value-changed” signal from the :class:`Adjustment <GLXCurses.Adjustment.Adjustment>`.
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

        # Check if the lower value is a float or raise a error
        if type(lower) == float:
            self.lower = lower
        else:
            raise TypeError(u'>lower argument< must be a float')

        # Check if the page_increment value is a float or raise a error
        if type(page_increment) == float:
            self.page_increment = page_increment
        else:
            raise TypeError(u'>page_increment< argument must be a float')

        # Check if the page_size value is a float or raise a error
        if type(page_size) == float:
            self.page_size = page_size
        else:
            raise TypeError(u'>page_size< argument must be a float')

        # Check if the step_increment value is a float or raise a error
        if type(step_increment) == float:
            self.step_increment = step_increment
        else:
            raise TypeError(u'>step_increment< argument must be a float')

        # Check if the upper value is a float or raise a error
        if type(upper) == float:
            self.upper = upper
        else:
            raise TypeError(u'>upper< argument must be a float')

        # Check if the value value is a float or raise a error
        if type(value) == float:
            self.value = value
        else:
            raise TypeError(u'>value< argument must be a float')

        # emit only on changed signal for all they allocation's
        self.changed()
        self.value_changed()

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

        When setting multiple adjustment properties via their individual setters, multiple
        :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` signals will be emitted. However,
        since the emission of the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` signal
        is tied to the emission of the ``notify`` signals of the changed properties, it’s possible to compress
        the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` signals into one by calling
        ``object_freeze_notify()`` and ``object_thaw_notify()`` around the calls to the individual setters.

        Alternatively, using :func:`Adjustment.configure() <GLXCurses.Adjustment.Adjustment.configure()>`
        has the same effect of compressing :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>`
        emissions.

        .. warning:: Unfortunately ``object_freeze_notify()`` and ``object_thaw_notify()`` don't exist yet. \
        then only :func:`Adjustment.configure() <GLXCurses.Adjustment.Adjustment.configure()>` will make the work.

        :param lower: the new minimum value
        :type lower: float
        :raise TypeError: when "lower" argument is not a :py:data:`float`
        """
        # Check if lower is a float before assign it or raise an error
        if type(lower) == float:
            self.lower = lower
        else:
            raise TypeError(u'>lower< argument must be a float')
        # Emit a changed signal
        self.changed()

    def set_page_increment(self, page_increment):
        """
        Sets the page increment of the adjustment.

        .. seealso:: :func:`Adjustment.set_lower() <GLXCurses.Adjustment.Adjustment.set_lower()>` about how to \
        compress multiple emissions of the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` \
        signal when setting multiple adjustment attributes.

        :param page_increment: the new page increment
        :type page_increment: float
        :raise TypeError: when "page_increment" argument is not a :py:data:`float`
        """
        # Check if page_increment is a float before assign it or raise an error
        if type(page_increment) == float:
            self.page_increment = page_increment
        else:
            raise TypeError(u'>page_increment< argument must be a float')
        # Emit a changed signal
        self.changed()

    def set_page_size(self, page_size):
        """
        Sets the page size of the adjustment.

        .. seealso:: :func:`Adjustment.set_lower() <GLXCurses.Adjustment.Adjustment.set_lower()>` about how to \
        compress multiple emissions of the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` \
        signal when setting multiple adjustment attributes.

        :param page_size: the new page size
        :type page_size: float
        :raise TypeError: when "page_size" argument is not a :py:data:`float`
        """
        # Check if page_size is a float before assign it or raise an error
        if type(page_size) == float:
            self.page_size = page_size
        else:
            raise TypeError(u'Value of >page_size< argument must be a float')
        # Emit a changed signal
        self.changed()

    def set_step_increment(self, step_increment):
        """
        Sets the step increment of the adjustment.

        .. seealso:: :func:`Adjustment.set_lower() <GLXCurses.Adjustment.Adjustment.set_lower()>` about how to \
        compress multiple emissions of the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` \
        signal when setting multiple adjustment attributes.

        :param step_increment: the new step increment
        :type step_increment: float
        :raise TypeError: when "step_increment" argument is not a :py:data:`float`
        """
        # Check if step_increment is a float before assign it or raise an error
        if type(step_increment) == float:
            self.step_increment = step_increment
        else:
            raise TypeError(u'>step_increment< argument must be a float')
        # Emit a changed signal
        self.changed()

    def set_minimum_increment(self, minimum_increment):
        """
        Sets the minimum_increment attribute value of the adjustment.

        .. note:: That methode don't exist inside GTK3 doc, when get_minimum_increment() exist ... \
        It's more logic to have the capability to set the minimum_increment attribute.

        .. warning:: That attribute is not use by the \
        :func:`Adjustment.configure() <GLXCurses.Adjustment.Adjustment.configure()>` method

        :param minimum_increment: the new minimum value
        :type minimum_increment: float
        :raise TypeError: when ``minimum_increment`` passed as argument is not a :py:data:`float`
        """
        # Check if minimum_increment is a float before assign it or raise an error
        if type(minimum_increment) == float:
            self.minimum_increment = minimum_increment
        else:
            raise TypeError(u'>minimum_increment< argument must be a float')
        # Emit a changed signal
        self.changed()

    def set_upper(self, upper):
        """
        Sets the maximum value of the adjustment.

        .. seealso:: :func:`Adjustment.set_lower() <GLXCurses.Adjustment.Adjustment.set_lower()>` about how to \
        compress multiple emissions of the :func:`Adjustment.changed() <GLXCurses.Adjustment.Adjustment.changed()>` \
        signal when setting multiple adjustment attributes.

        :param upper: the new maximum value
        :type upper: float
        :raise TypeError: when "upper" argument is not a :py:data:`float`
        """
        # Check if upper is a float before assign it or raise an error
        if type(upper) == float:
            self.upper = upper
        else:
            raise TypeError(u'>upper< argument must be a float')
        # Emit a changed signal
        self.changed()
