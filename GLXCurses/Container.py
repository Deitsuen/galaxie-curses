#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

from GLXCurses import Widget
from GLXCurses import glxc
from GLXCurses.Utils import glxc_type


# Reference Document: https://developer.gnome.org/gtk3/stable/GtkContainer.html
class Container(Widget):
    """
    GLXCurses.Container — Base class for widgets which contain other widgets

    Description:

    A GLXCurse user interface is constructed by nesting widgets inside widgets. Container widgets are the
    inner nodes in the resulting tree of widgets: they contain other widgets. So, for example, you might have a
    GLXCurse.Window containing a GLXCurse.Frame containing a GLXCurse.Label. If you wanted an image instead of a
    textual label inside the frame, you might replace the GLXCurse.Label widget with a GLXCurse.Image widget.

    There are two major kinds of container widgets in GLXCurses. Both are subclasses of the abstract GLXCurse.Container
    base class.

    The first type of container widget has a single child widget and derives from GLXCurses.Bin. These containers are
    decorators, which add some kind of functionality to the child. For example, a GLXCurses.Button makes its child
    into a clickable button; a GLXCurses.Frame draws a frame around its child and a GLXCurses.Window places its child
    widget inside a top-level window.

    The second type of container can have more than one child; its purpose is to manage layout. This means that these
    containers assign sizes and positions to their children. For example, a GLXCurses.HBox arranges its children in a
    horizontal row, and a GLXCurses.Grid arranges the widgets it contains in a two-dimensional grid.

    For implementations of GLXCurses.Container the virtual method GLXCurses.Container.forall() is always required,
    since it's used for drawing and other internal operations on the children. If the GLXCurses.Container
    implementation expect to have non internal children it's needed to implement both GLXCurses.Container.add() and
    GLXCurses.Container.remove(). If the GLXCurses.Container implementation has internal children, they should be
    added widget.set_parent() on __init__() and removed with widget.unparent() in the GLXCurses.Widget.destroy()
    implementation. See more about implementing custom widgets at https://wiki.gnome.org/HowDoI/CustomWidgets
    """

    def __init__(self):
        # Load heritage
        Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.Container'

        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('Container')

        # Make a Widget Style heritage attribute as local attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

        # Properties

        # Can be used to add a new child to the container.
        self.child = None
        # Specify how resize events are handled.
        # One of: glxc.RESIZE_PARENT, glxc.RESIZE_QUEUE or glxc.RESIZE_IMMEDIATE
        self.resize_mode = glxc.RESIZE_PARENT
        # The width of the empty border outside the containers children.
        self.border_width = 0

        # Internal Properties
        # The child widget that has the focus
        self.focus_child = None
        # If True the container needs resizing
        self.need_resize = False
        # if True redraw the container when a child gets reallocated
        self.reallocate_redraws = True
        # If True the container had its focus chain explicitly set
        self.has_focus_chain = False

        # Subscibtions
        #self.subscribe('add', self._emit_add_signal())
        # self.subscribe('check-resize', Container._emit_check_resize_signal(self))
        # self.subscribe('remove', Container._emit_remove_signal(self))
        # self.subscribe('set-focus-child', Container._emit_set_focus_child_signal(self))

    # The amount of blank space to leave outside the container.
    def set_border_width(self, border_width):
        self.border_width = int(border_width)

    # The current border width
    def get_border_width(self):
        return self.border_width

    def add(self, widget=None):
        """
        Adds widget to container .

        Typically used for simple containers such as Window, Frame, or Button;

        For more complicated layout containers such as Box or Grid, this function will pick default packing
        parameters that may not be correct.

        So consider functions such as
        :func:`GLXCurses.Box.pack_start() <GLXCurses.Box.Box.pack_start>` and
        :func:`GLXCurses.Grid.attach() <GLXCurses.Grid.Grid.attach>` as an alternative to
        :func:`GLXCurses.Container.add() <GLXCurses.Container.Container.add>` in those cases.

        A widget may be added to only one container at a time;
        you (should not) place the same widget inside two different containers.

        :param widget: a current child of container
        :type widget: GLXCurses Widget
        """
        # Try to exit as soon of possible
        if not glxc_type(widget):
            raise TypeError('"widget" argument must be a GLXCurses object type')

        # If we are here everything look ok
        if bool(self._get_child()):
            if callable(getattr(self._get_child()['widget'], 'unparent')):
                self._get_child()['widget'].unparent()

        # The added widget receive a parent
        widget.set_parent(self)

        child_property = {
            'position': 0
        }

        child_info = {
            'widget': widget,
            'type': widget.glxc_type,
            'id': widget.get_widget_id(),
            'property': child_property
        }

        # The parent receive a new child
        self.child = child_info

        # Try to emit add signal
        self._emit_add_signal(child_info)

    def remove(self, widget):
        """
        Removes widget from container .

        Widget must be inside container .

        Note that container will own a reference to widget , and that this may be the last reference held; so
        removing a widget from its container can destroy that widget. If you want to use widget again, you need to
        add a reference to it before removing it from a container, using g_object_ref(). If you don’t want to use
        widget again it’s usually more efficient to simply destroy it directly using Widget.destroy() since this
        will remove it from the container and help break any circular reference count cycles.

        :param widget: a current child of container
        :type widget: GLXCurses Widget
        """
        if hasattr(self, 'children'):
            if bool(self.children):
                count = 0
                last_found = None
                for children in self.get_children():
                    if widget == children['widget']:
                        last_found = count
                    count += 1
                if last_found is not None:
                    self.get_children().pop(last_found)
                    if callable(getattr(widget, 'unparent')):
                        widget.unparent()

        if hasattr(self, 'child'):
            if bool(self.child):
                if self.child['widget'] == widget:
                    self.child = None
                    if callable(getattr(widget, 'unparent')):
                        widget.unparent()

    def add_with_properties(self, widget, first_prop_name, null_terminated_list=None):
        """
        Adds widget to container , setting child properties at the same time. See GLXCurses.Container.add() and
        GLXCurses.Container.child_set() for more details.

        :param widget: a widget to be placed inside container
        :param first_prop_name: the name of the first child property to set
        :param null_terminated_list: a NULL-terminated list of property names and values, starting with first_prop_name
        :type widget: GLXCurses.Widget
        :type first_prop_name: str
        :type null_terminated_list: list()
        """
        if null_terminated_list is None:
            null_terminated_list = list()
        self.add(widget)
        self.child_set(widget, first_prop_name, null_terminated_list)

    def get_resize_mode(self):
        """
        Returns the resize mode for the container.

        Allowed value:
            * :func:`glxc.RESIZE_PARENT <GLXCurses.Constants.Constants.RESIZE_PARENT>`
            * :func:`glxc.RESIZE_QUEUE <GLXCurses.Constants.Constants.RESIZE_QUEUE>`
            * :func:`glxc.RESIZE_IMMEDIATE <GLXCurses.Constants.Constants.RESIZE_IMMEDIATE>`

        .. seealso:: :func:`GLXCurses.Container.set_resize_mode() <GLXCurses.Constants.Constants.set_resize_mode>`.

        .. warning:: :func:`GLXCurses.Container.get_resize_mode() <GLXCurses.Container.Container.get_resize_mode>`\
        has been deprecated since version 3.12 of GTK+, if will be remove as soon of possible.

        :return: the current resize mode
        :rtype: GLXCurses.Constants
        """
        return self.resize_mode

    def set_resize_mode(self, resize_mode):
        """
        Sets the resize mode for the container.

        The resize mode of a container determines whether a resize request will be passed to the container’s parent,
        queued for later execution or executed immediately.

        Allowed value:
            * :func:`glxc.RESIZE_PARENT <GLXCurses.Constants.Constants.RESIZE_PARENT>`
            * :func:`glxc.RESIZE_QUEUE <GLXCurses.Constants.Constants.RESIZE_QUEUE>`
            * :func:`glxc.RESIZE_IMMEDIATE <GLXCurses.Constants.Constants.RESIZE_IMMEDIATE>`

        .. seealso:: :func:`GLXCurses.Container.get_resize_mode() <GLXCurses.Container.Container.get_resize_mode>`.

        .. warning:: :func:`GLXCurses.Container.set_resize_mode() <GLXCurses.Container.Container.set_resize_mode>`\
        has been deprecated since version 3.12 of GTK+, if will be remove as soon of possible.

        :param resize_mode: the new resize mode
        :type resize_mode: GLXCurses.Constants
        """
        available_resize_mode = [
            glxc.RESIZE_PARENT,
            glxc.RESIZE_QUEUE,
            glxc.RESIZE_IMMEDIATE
        ]
        if resize_mode in available_resize_mode:
            self.resize_mode = resize_mode
        else:
            pass

    def check_resize(self):
        """
        The check_resize() method emits the "check-resize" signal on the container.
        """
        raise NotImplementedError

    def foreach(self, callback, callback_data):
        """
        Invokes callback on each non-internal child of container . See GLXCurses.Container.forall() for details on
        what constitutes an “internal” child. For all practical purposes, this function should iterate over precisely
        those child widgets that were added to the container by the application with explicit add() calls.

        Most applications should use GLXCurses.Container.foreach(), rather than GLXCurses.Container.forall().

        :param callback: a callback.
        :param callback_data: callback user data
        """
        for widget in self.child:
            widget.refresh()

    def forall(self, callback, callback_data):
        pass

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

    def child_set(self, child, **kwargs):
        """
        Sets one or more child properties for child and container .

        :param child: a widget which is a child of container
        :type child: A GLXCurses object
        :param property: property to set
        :type property: dict
        """


    def child_get(self, child, first_prop_name, additional_property):
        pass

    def child_set_property(self, child, property_name, value):
        pass

    def child_get_property(self, child, property_name):
        pass

    # Internal
    def _emit_add_signal(self, data=None):
        """
        Emit the **add** signal, all widget it have subcribe to it signal will be in touch
        """
        if data is not None:
            # Create a Dict with everything
            instance = {
                'widget': ' '.join([self.__class__.__name__, self.id]),
                'child': ' '.join([data['widget'].__class__.__name__, data['widget'].id]),
                'child_property': data['property']
            }
            # EVENT EMIT
            self.emit('ADD', instance)

    def _emit_check_resize_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        pass

    def _emit_remove_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        pass

    def _emit_set_focus_child_signal(self, user_data=None):
        """

        :param user_data: the object which received the signal
        """
        if user_data is None:
            user_data = list()
        pass

    def _get_child(self):
        return self.child

    def _set_child(self, child=None):
        self.child = child
