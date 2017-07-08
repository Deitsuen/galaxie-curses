#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Container
from GLXCurses.Utils import glxc_type

__author__ = 'Tuux'


class Bin(Container):
    """
    The :class:`Bin <GLXCurses.Bin.Bin>` widget is a container with just one child. It is not very useful itself,
    but it is useful for deriving subclasses, since it provides common code needed for handling a single child widget.

    Many GLXCurses widgets are subclasses of :class:`Bin <GLXCurses.Bin.Bin>`, including
     * :class:`Window <GLXCurses.Window.Window>`
     * :class:`Button <GLXCurses.Button.Button>`
     * :class:`Frame <GLXCurses.Frame.Frame>`
     * :class:`HandleBox <GLXCurses.HandleBox.HandleBox>`
     * :class:`ScrolledWindow <GLXCurses.ScrolledWindow.ScrolledWindow>`

    """

    def destroy(self):
        """
        Destroys a widget.

        When a widget is destroyed all references it holds on other objects will be released:

        * if the widget is inside a container, it will be removed from its parent
        * if the widget is a container, all its children will be destroyed, recursively
        * if the widget is a top level, it will be removed from the list of top level widgets \
        that :class:`Application <GLXCurses.Application.Application>` maintains internally

        :raise NotImplementedError: Method or function hasn't been implemented yet.
        """
        raise NotImplementedError

    def __init__(self):
        Container.__init__(self)
        self.glxc_type = 'GLXCurses.Bin'
        self.set_name('Bin')

        self.child = None

    def add(self, child=None):
        """
        Add a widget as child, only if the :class:`Bin <GLXCurses.Bin.Bin>` haven't any child

        :param child: A child
        :type child: GLXCurses Type
        """
        if glxc_type(child) or child is None:
            if child is not None:
                if self.get_child() is not None:
                    self.get_child()['widget'].set_parent(None)

                # The added widget recive a parent
                child.set_parent(self)

                child_info = dict()
                child_info['widget'] = child
                child_info['type'] = child.glxc_type
                child_info['id'] = child.get_widget_id()

                # The parent recive a new child
                self.child = child_info

                # Try to emit add signal
                self._emit_add_signal()
            else:
                if self.get_child() is not None:
                    self.get_child()['widget'].set_parent(None)
                self.child = None
        else:
            raise TypeError(u'>style< is not a GLXCurses.Style type or None')

    def get_child(self):
        """
        Get the child of the :class:`Bin <GLXCurses.Bin.Bin>`, or :py:obj:`None` if the
        :class:`Bin <GLXCurses.Bin.Bin>` contains no child widget.

        The returned widget does not have a reference added, so you do not need to unref it.

        :return: child widget of the :class:`Bin <GLXCurses.Bin.Bin>`
        :rtype: :class:`Box <GLXCurses.Box.Box>` or :py:obj:`None`
        """
        return self.child

