#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Container import Container

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Box(Container):
    def __init__(self):
        Container.__init__(self)

        # Properties
        # The amount of space between children.
        self.spacing = 0

        # If True the children should all be the same size.
        self.homogeneous = False

        # Box Child Properties

        # If True the child should receive extra space when the parent grows
        self.expend = None

        # If True extra space given to the child should be allocated to the child;
        # if False extra space given to the child should be used as padding
        self.fill = True

        # The amount of extra space to put between the child and its neighbors, in char
        self.padding = 0

        # Indicates whether the child is packed with reference to the start (PACK_START) or end (PACK_END) of the parent
        self.pack_type = 'PACK_START'

        # The index of the child in the parent
        self.position = 0

    def pack_start(self, child, expand=True, fill=True, padding=0):
        self.get_children().insert(0, child)

    def pack_end(self, child, expand=True, fill=True, padding=0):
        self.get_children().append(child)

    def pack_start_defaults(self, widget):
        pass

    def pack_end_defaults(self, widget):
        pass

    # Sets the “homogeneous” property of box ,
    # controlling whether or not all children of box are given equal space in the box.
    # homogeneous a boolean value, TRUE to create equal allotments, FALSE for variable allotments
    def set_homogeneous(self, homogeneous):
        self.homogeneous = bool(homogeneous)

    # Returns whether the box is homogeneous (all children are the same size). See gtk_box_set_homogeneous().
    # TRUE if the box is homogeneous.
    def get_homogeneous(self):
        return self.homogeneous

    # Sets the "spacing" property of box , which is the number of character to place between children of box .
    # spacing the number of pixels to put between children
    def set_spacing(self, spacing):
        self.spacing = int(spacing)

    # Gets the value set by set_spacing().
    def get_spacing(self):
        return self.spacing

    def reorder_child(self, child, position):
        self.get_children().remove(child)
        self.get_children().insert(position, child)

    def query_child_packing(self, child):
        pass

    def set_child_packing(self, child, expand, fill, padding, pack_type):
        pass
