#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Container

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
        * if the widget is a top level, it will be removed from the list of top level widgets
        that :class:`Application <GLXCurses.Application.Application>` maintains internally

        :raise NotImplementedError: Method or function hasn't been implemented yet.
        """
        raise NotImplementedError

    def __init__(self):
        Container.__init__(self)
        self.child = None

    def get_child(self):
        """
        Get the child of the :class:`Bin <GLXCurses.Bin.Bin>`, or :py:obj:`None` if the
        :class:`Bin <GLXCurses.Bin.Bin>` contains no child widget.

        The returned widget does not have a reference added, so you do not need to unref it.

        :return: child widget of the :class:`Bin <GLXCurses.Bin.Bin>`
        :rtype: :class:`Box <GLXCurses.Box.Box>` or :py:obj:`None`
        """
        return self.child
