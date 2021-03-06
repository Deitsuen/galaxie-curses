#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

from GLXCurses import Application
from GLXCurses.Utils import new_id

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

        """
        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.Adjustment'

        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.name = 'Box'

        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = new_id()

        self.lower = float(0.0)
        self.page_increment = float(0.0)
        self.page_size = float(0.0)
        self.step_increment = float(0.0)
        self.minimum_increment = float(0.0)
        self.upper = float(0.0)
        self.value = float(0.0)

        self.two = None
        self.average = None

    def get_value(self):
        """
        :Methods:

        Gets the current value of the adjustment. See set_value()

        :return: A current value Adjustment
        :rtype: float
        """
        return self.value

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
            # Clamp Value
            # value = max(min(self.get_upper(), value), self.get_lower())

            if value != self.get_value():
                self.value = value
                self.emit_value_changed()
        else:
            raise TypeError(u'>value< argument must be a float')

    def clamp_page(self, lower, upper):
        """
        Updates the :py:attr:`value` attribute to ensure that the range between ``lower`` and ``upper`` parameters
        is in the current page
        (i.e. between :py:attr:`value` and :py:attr:`value` + :py:attr:`page_size`).

        If the range is larger than the page size, then only the start of it will be in the current page.
        A **value-changed** signal will be emitted if the value is changed.

        :param lower: the lower value
        :param upper: the upper value
        :type lower: float
        :type upper: float
        :raise TypeError: when every parameters are not :py:data:`float` type
        """
        # https://github.com/GNOME/gtk/blob/master/gtk/gtkadjustment.c line 880
        # Try to not execute the code
        if type(upper) == float and type(lower) == float:

            # control
            need_emission = False

            # Clamp
            lower = max(min(self.get_upper(), lower), self.get_lower())
            upper = max(min(self.get_upper(), upper), self.get_lower())

            if self.get_value() + self.get_page_size() < upper:
                self.value = upper - self.get_page_size()
                need_emission = True
            if self.get_value() > lower:
                self.value = lower
                need_emission = True

            if need_emission:
                self.emit_value_changed()
        else:
            raise TypeError(u'both parameters >lower< and >upper< must be a float type')

    def emit_changed(self):
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

        #adjustment_signals[VALUE_CHANGED] =
        # g_signal_new(I_("value-changed"),
        #              G_OBJECT_CLASS_TYPE(class ),
        #             G_SIGNAL_RUN_FIRST | G_SIGNAL_NO_RECURSE,
        #             G_STRUCT_OFFSET (GtkAdjustmentClass, value_changed),
        #             NULL, NULL,
        #             NULL,
        #             G_TYPE_NONE, 0);
        #             }

        # EVENT EMIT
        Application.emit(instance)

    def emit_value_changed(self):
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

        # Example from Gtk Source
        # instance = [I_("value-changed"),
        #             G_OBJECT_CLASS_TYPE(class ),
        #             G_SIGNAL_RUN_FIRST | G_SIGNAL_NO_RECURSE,
        #             G_STRUCT_OFFSET (GtkAdjustmentClass, value_changed),
        #             NULL, NULL,
        #             NULL,
        #             G_TYPE_NONE, 0]

        # EVENT EMIT
        Application.emit(instance)

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

        # Check if we execute the code or raise a error
        if (
            type(lower) == float and
            type(page_increment) == float and
            type(value) == float and
            type(lower) == float and
            type(upper) == float and
            type(step_increment) == float and
            type(page_increment) == float and
            type(page_size) == float
           ):

            # Controls
            value_changed = False
            attribute_changed = False

            # Check if something will change except for value attribute
            if lower != self.get_lower():
                self.set_lower(lower)
                attribute_changed = True
            if upper != self.get_upper():
                self.set_upper(upper)
                attribute_changed = True
            if step_increment != self.get_step_increment():
                self.set_step_increment(step_increment)
                attribute_changed = True
            if page_increment != self.get_page_increment():
                self.set_page_increment(page_increment)
                attribute_changed = True
            if page_size != self.get_page_size():
                self.set_page_size(page_size)
                attribute_changed = True

            # Check for value attribute
            # don't use CLAMP() so we don't end up below lower if upper - page_size
            value = min(value, upper - page_size)
            value = max(value, lower)

            if value != self.get_value():
                # set value manually to make sure "changed" is emitted with the
                # new value in place and is emitted before "value-changed"
                self.value = value
                value_changed = True

            # Signal emission
            if attribute_changed:
                self.emit_changed()

            if value_changed:
                self.emit_value_changed()
        else:
            raise TypeError(u'parameters must be float type')

    def get_lower(self):
        """
        Retrieves the minimum value of the adjustment.

        :return: The current minimum value of the adjustment
        :rtype: float
        """
        return self.lower

    def get_page_increment(self):
        """
        Retrieves the page increment of the adjustment.

        :return: The current page increment of the adjustment
        :rtype: float
        """
        return self.page_increment

    def get_page_size(self):
        """
        Retrieves the page size of the adjustment.

        :return: The current page size of the adjustment
        :rtype: float
        """
        return self.page_size

    def get_step_increment(self):
        """
        Retrieves the step increment of the adjustment.

        :return: The current step increment of the adjustment.
        :rtype: float
        """
        return self.step_increment

    def get_minimum_increment(self):
        """
        Get the smaller of step increment and page increment. Note that value is compute, then it have no need of a
        set_minimum_increment() method.

        :return: the minimum increment of adjustment
        :rtype: float
        """

        # Source: https://github.com/GNOME/gtk/blob/master/gtk/gtkadjustment.c line 931
        if self.get_step_increment() != 0 and self.page_increment != 0:
            if abs(self.get_step_increment()) < abs(self.get_page_increment()):
                minimum_increment = self.get_step_increment()
            else:
                minimum_increment = self.get_page_increment()
        elif self.get_step_increment() == 0 and self.get_page_increment() == 0:
            minimum_increment = 0
        elif self.get_step_increment() == 0:
            minimum_increment = self.get_page_increment()
        else:
            minimum_increment = self.get_step_increment()

        return minimum_increment

    def get_upper(self):
        """
        Retrieves the maximum value of the adjustment.

        :return: The current maximum value of the adjustment
        :rtype: float
        """
        return self.upper

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
            if lower != self.get_lower():
                self.lower = lower
        else:
            raise TypeError(u'>lower< argument must be a float')

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
            if page_increment != self.get_page_increment():
                self.page_increment = page_increment
        else:
            raise TypeError(u'>page_increment< argument must be a float')
        # Emit a changed signal
        self.emit_changed()

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
            if page_size != self.get_page_size():
                self.page_size = page_size
        else:
            raise TypeError(u'Value of >page_size< argument must be a float')

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
            if step_increment != self.get_step_increment():
                self.step_increment = step_increment
        else:
            raise TypeError(u'>step_increment< argument must be a float')

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
            if upper != self.get_upper():
                self.upper = upper
        else:
            raise TypeError(u'>upper< argument must be a float')


