#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Container(Widget):
    def __init__(self):
        Widget.__init__(self)

        self.child = None
        self.children_list = list()

        # Container Properties
        # Attributes

        # The width of the empty border outside the containers children.
        self.border_width = 0

        # Specify how resize events are handled. One of: RESIZE_PARENT, RESIZE_QUEUE or RESIZE_IMMEDIATE
        self.resize_mode = 'RESIZE_PARENT'

        # The child widget that has the focus
        self.focus_child = None

        # If True the container needs resizing
        self.need_resize = False

        # if True redraw the container when a child gets reallocated
        self.reallocate_redraws = True

        # If True the container had its focus chain explicitly set
        self.has_focus_chain = False

    # The amount of blank space to leave outside the container.
    def set_border_width(self, border_width):
        self.border_width = int(border_width)

    # The current border width
    def get_border_width(self):
        return self.border_width

    # The add() method adds widget to the container.
    # This method is typically used for simple containers such as Window, Frame, or Button
    # that hold a single child widget.
    # Containers that handle multiple children usually have additional methods
    # such as Box.pack_start() and Table.attach() as an alternative to add().
    # Adding a widget to a container usually results in the resizing and redrawing of the container contents.
    def add(self, widget):
        widget.set_parent(self)
        self.child = widget

    def remove(self, widget):
        self.child = None
        widget.set_visible(False)

    # The set-resize_mode() method sets the "resize=mode" property of the container.
    # he resize mode of a container determines whether a resize request will be passed to the container's parent
    # (RESIZE_PARENT), queued for later execution (RESIZE_QUEUE) or executed immediately (RESIZE_IMMEDIATE).
    def set_resize_mode(self, resize_mode):
        self.resize_mode = str(resize_mode).upper

    # The get_resize_mode() method returns the value of the "resize-mode" property for of the container.
    # See set_resize_mode().
    def get_resize_mode(self):
        return self.resize_mode

    # The check_resize() method emits the "check-resize" signal on the container.
    def check_resize(self):
        pass

    def forall(self, callback, callback_data):
        pass

    def foreach(self, callback, callback_data):
        pass

    def get_children(self):
        return self.child

    def propagate_expose(self, child, event):
        pass

    def set_focus_chain(self, focusable_widgets):
        pass

    def get_focus_chain(self):
        pass

    def unset_focus_chain(self):
        pass

    def set_reallocate_redraws(self, needs_redraws):
        pass

    def set_focus_child(self, child):
        pass

    def get_focus_child(self):
        pass

    def set_focus_vadjustment(self, adjustment):
        pass

    def get_focus_vadjustment(self):
        pass

    def set_focus_hadjustment(self, adjustment):
        pass

    def get_focus_hadjustment(self):
        pass

    def resize_children(self):
        pass

    def child_type(self):
        pass

    def add_with_properties(self, widget, first_prop_name, first_prop_value, additional_property):
        pass

    def child_set(self, child, first_prop_name, first_prop_value, additional_property):
        pass

    def child_get(self, child, first_prop_name, additional_property):
        pass

    def child_set_property(self, child, property_name, value):
        pass

    def child_get_property(self, child, property_name):
        pass
