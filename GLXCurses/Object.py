#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Object(object):
    def __init__(self):

        # Object flags
        self.flags = None

        # Signal
        self.list_of_signal_handlers = {}

    def set_flags(self):
        flags = dict()

        # The object is currently being destroyed.
        flags['IN_DESTRUCTION'] = False

        # The object is orphaned.
        flags['FLOATING'] = True

        # Widget flags
        # widgets without a real parent (e.g. Window and Menu) have this flag set throughout their lifetime.
        flags['TOPLEVEL'] = False

        # A widget that does not provide its own Window.
        # Visible action (e.g. drawing) is performed on the parent's Window.
        flags['NO_WINDOW'] = True

        # The widget has an associated Window.
        flags['REALIZED'] = False

        # The widget can be displayed on the screen.
        flags['MAPPED'] = False

        # The widget will be mapped as soon as its parent is mapped.
        flags['VISIBLE'] = True

        # The sensitivity of a widget determines whether it will receive certain events (e.g. button or key presses).
        # One requirement for the widget's sensitivity is to have this flag set.
        flags['SENSITIVE'] = True

        # This is the second requirement for the widget's sensitivity.
        # Once a widget has SENSITIVE and PARENT_SENSITIVE set, its state is effectively sensitive.
        flags['PARENT_SENSITIVE'] = True

        # The widget is able to handle focus grabs.
        flags['CAN_FOCUS'] = True

        # The widget has the focus - assumes that CAN_FOCUS is set
        flags['HAS_FOCUS'] = True

        # The widget is allowed to receive the default action.
        flags['CAN_DEFAULT'] = True

        # The widget currently will receive the default action.
        flags['HAS_DEFAULT'] = False

        # The widget is in the grab_widgets stack, and will be the preferred one for receiving events.
        flags['HAS_GRAB'] = False

        # The widgets style has been looked up through the RC mechanism.
        # It does not imply that the widget actually had a style defined through the RC mechanism.
        flags['RC_STYLE'] = 'Default.yml'

        # The widget is a composite child of its parent.
        flags['COMPOSITE_CHILD'] = False

        # unused
        flags['NO_REPARENT'] = 'unused'

        # Set on widgets whose window the application directly draws on,
        # in order to keep GLXCurse from overwriting the drawn stuff.
        flags['APP_PAINTABLE'] = False

        # The widget when focused will receive the default action and have HAS_DEFAULT set
        # even if there is a different widget set as default.
        flags['RECEIVES_DEFAULT'] = False

        # Exposes done on the widget should be double-buffered.
        flags['DOUBLE_BUFFERED'] = False

        self.flags = flags

    def unset_flags(self, flags):
        self.flags = None

    def destroy(self):
        pass

    # Object Signal Prototypes
    # The connect() method adds a function or method (handler)to the end
    # of the list of signal handlers for the named detailed_signal but before the default class signal handler.
    # An optional set of parameters may be specified after the handler parameter.
    # These will all be passed to the signal handler when invoked.
    def connect(self, detailed_signal, handler):
        # At first generate a unique uuid
        handler_id = uuid.uuid1().int
        if detailed_signal not in self.list_of_signal_handlers:
            self.list_of_signal_handlers[detailed_signal] = []

        subscription = {
            'detailed_signal': detailed_signal,
            'handler': handler,
            'handler_id': handler_id
        }

        if not self._has_subscription(detailed_signal, handler, handler_id):
            self.list_of_signal_handlers[detailed_signal].append(subscription)

    def _has_subscription(self, detailed_signal, handler, handler_id):
        """
        This method shows whether a function has subscriptions or not.

        :param key: The event key.
        :param callback: The callback function.
        :return: True if there is an subscription.
        """
        if detailed_signal not in self.list_of_signal_handlers:
            return False

        subscription = {
            'detailed_signal': detailed_signal,
            'handler': handler,
            'handler_id': handler_id
        }

        return subscription in self.list_of_signal_handlers[detailed_signal]