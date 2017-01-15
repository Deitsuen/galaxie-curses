#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Container

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Bin(Container):
    """
    The GtkBin widget is a container with just one child. It is not very useful itself, but it is useful for deriving
    subclasses, since it provides common code needed for handling a single child widget.

    Many GTK+ widgets are subclasses of GtkBin, including
    GLXCurses.Window,
    GLXCurses.Button,
    GLXCurses.Frame,
    GLXCurses.HandleBox,
    GLXCurses.ScrolledWindow.
    """
    def destroy(self):
        raise NotImplementedError

    def __init__(self):
        Container.__init__(self)
        self.child = None

    def get_child(self):
        """
        Gets the child of the GtkBin, or None if the bin contains no child widget.
        The returned widget does not have a reference added, so you do not need to unref it.

        :return: pointer to child of the GLXCurses.Bin
        """
        return self.child
