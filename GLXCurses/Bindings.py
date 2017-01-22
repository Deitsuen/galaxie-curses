#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Binding(object):
    """
    **Bindings**

    Bindings — Key bindings for individual widgets

    **Description**:

    """
    def __init__(self):
        self.binding_set = None  # a GtkBindingSet to add a signal to
        self.keyval = None       # key value
        self.modifiers = None    # key modifier
        self.signal_name = None  # signal name to be bound
        self.binding_args = None # lis of BindingArg signal arguments.

    def add_signal(self, binding_set, keyval, modifiers, signal_name, binding_args=None):
        """
        Override or install a new key binding for keyval with modifiers on binding_set .

        :param binding_set: a BindingSet to add a signal to
        :param keyval: key value
        :param modifiers: key modifier
        :param signal_name: signal name to be bound
        :param binding_args: list of BindingArg signal arguments.
        :type binding_args: list
        """
        if binding_args is None:
            binding_args = list()

        self.binding_set = binding_set
        self.keyval = keyval
        self.modifiers = modifiers
        self.signal_name = signal_name
        self.binding_args = binding_args

