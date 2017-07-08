#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

from GLXCurses import Container
from GLXCurses import glxc
from GLXCurses.Utils import glxc_type
from GLXCurses.Utils import clamp_to_zero

# https://developer.gnome.org/gtk3/stable/GtkBox.html
class Box(Container):
    """
    :Description:

    The :class:`Box <GLXCurses.Box.Box>` widget organizes child widgets into a rectangular area.
    """

    def __init__(self):
        """
        :Attributes Details:

        .. py:attribute:: base_position

           The position of the baseline aligned widgets if extra space is available.

              :Type: :py:const:`BaselinePosition`
              :Flags: Read / Write
              :Default value: :py:const:`BASELINE_POSITION_CENTER`

        .. py:attribute:: base_position

           Whether the children should all be the same size.

              :Type: :py:obj:`bool`
              :Flags: Read / Write
              :Default value: :py:obj:`False`

        .. py:attribute:: spacing

           The amount of space between children.

              :Type: :py:obj:`int`
              :Flags: Read / Write
              :Allowed values: >= 0
              :Default value: 0

        :Child Attributes Details:

        .. py:attribute:: expand

           Whether the child should receive extra space when the parent grows.

           Note that the default value for this property is :py:obj:`False` for :class:`Box <GLXCurses.Box.Box>`,
           but :class:`HBox <GLXCurses.HBox.HBox>`, :class:`VBox <GLXCurses.VBox.VBox>` and other subclasses use the
           old default of :py:obj:`True`.

           Note that the **halign**, **valign**, **hexpand** and **vexpand** attribute are the preferred way to
           influence child size allocation in containers

           In contrast to **hexpand**, the expand child attribute does not cause the box to expand itself.

              :Type: :py:obj:`bool`
              :Flags: Read / Write
              :Default value: :py:obj:`False`

        .. py:attribute:: fill

           Whether the child should receive extra space when the parent grows.

           Note that the **halign**, **valign**, **hexpand** and **vexpand** properties are the preferred way to
           influence child size allocation in containers.

              :Type: :py:obj:`bool`
              :Flags: Read / Write
              :Default value: :py:obj:`True`

        .. py:attribute:: pack_type

           A PackType indicating whether the child is packed with reference to the start or end of the parent.

              :Type: :py:const:`PackType`
              :Flags: Read / Write
              :Default value: :py:const:`PACK_START`

        .. py:attribute:: padding

           Extra space to put between the child and its neighbors, in chars.

              :Type: :py:obj:`int`
              :Flags: Read / Write
              :Allowed values: <= G_MAXINT
              :Default value: 0

        .. py:attribute:: position

           The index of the child in the parent.

              :Type: :py:obj:`int`
              :Flags: Read / Write
              :Allowed values: >= -1
              :Default value: 0
        """
        # Load heritage
        Container.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.Box'

        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.set_name('Box')

        # Make a Widget Style heritage attribute as local attribute
        if self.get_style().get_attribute_states():
            self.set_attribute_states(self.get_style().get_attribute_states())

        # Attributes
        self.base_position = glxc.BASELINE_POSITION_CENTER
        self.base_position = None
        self.homogeneous = False

        # Child Attributes
        self.expend = False
        self.fill = True
        self.orientation = glxc.ORIENTATION_HORIZONTAL
        self.pack_type = glxc.PACK_START
        self.padding = 0
        self.position = 0
        self.spacing = 0

        # orientation

    def new(self, orientation=glxc.ORIENTATION_HORIZONTAL, spacing=None):
        """
        Creates a new :class:`Box <GLXCurses.Box.Box>`.
        
        :param orientation: the box’s orientation. Default: ORIENTATION_HORIZONTAL
        :type orientation: Orientation
        :param spacing: the number of characters to place by default between children. Default: 0
        :type spacing: int or None
        :return: a new :class:`Box <GLXCurses.Box.Box>`.
        """
        if orientation not in [glxc.ORIENTATION_HORIZONTAL, glxc.ORIENTATION_VERTICAL]:
            raise TypeError('"orientation" must be glxc.ORIENTATION_HORIZONTAL or glxc.ORIENTATION_VERTICAL')
        if spacing is not None:
            if type(spacing) != int:
                raise TypeError('"spacing" must be int type or None')

        self.__init__()
        self.set_spacing(clamp_to_zero(spacing))
        self.orientation = orientation
        return self

    def pack_start(self, child=None, expand=True, fill=True, padding=None):
        """
        Adds child to :class:`Box <GLXCurses.Box.Box>` , packed with reference to the start of
        :class:`Box <GLXCurses.Box.Box>`.

        :param child: the widget to be added to :class:`Box <GLXCurses.Box.Box>`
        :type child: a GLXCures Object
        :param expand: ``True`` if the new child is to be given extra space allocated to \
        `Box <GLXCurses.Box.Box>`. The extra space will be divided evenly between all children that use this option
        :type expand: bool
        :param fill: ``True`` if space given to :py:obj:`child` by the :py:attr:`expend` option is actually \
        allocated to :py:obj:`child`, rather than just padding it. This parameter has no effect if :py:attr:`expend` \
        is set to :py:obj:`False`. A child is always allocated the full height of a horizontal \
        :class:`Box <GLXCurses.Box.Box>` and the full width of a vertical :class:`Box <GLXCurses.Box.Box>`. \
        This option affects the other dimension.
        :type fill: bool
        :param padding: extra space in characters to put between this child and its neighbors, over and above \
        the global amount specified by :py:attr:`spacing` attribute. If child is a widget at one of the reference \
        ends of box , then padding pixels are also put between child and the reference edge of box
        :type padding: int or None
        """
        # Try to exit as soon of possible
        if not glxc_type(child):
            raise TypeError('"child" argument must be a GLXCurses object type')
        if type(expand) != bool:
            raise TypeError('"expand" argument must be a bool')
        if type(fill) != bool:
            raise TypeError('"fill" argument must be a bool')
        if padding is not None:
            if type(padding) != int:
                raise TypeError('"spacing" must be int type or None')

        # If we are here everything look ok
        # Create a dict for store information's about packing
        child_info = dict()
        child_info['widget'] = child
        child_info['expand'] = expand
        child_info['fill'] = fill
        child_info['padding'] = clamp_to_zero(padding)

        self.get_children().insert(0, child_info)

        self.emit_pack_start(data=child_info)

    def pack_end(self, child=None, expand=True, fill=True, padding=None):
        """
        Adds child to :class:`Box <GLXCurses.Box.Box>` , packed with reference to the end of
        :class:`Box <GLXCurses.Box.Box>`.

        :param child: the widget to be added to :class:`Box <GLXCurses.Box.Box>`
        :type child: a GLXCures Object
        :param expand: ``True`` if the new child is to be given extra space allocated to \
        `Box <GLXCurses.Box.Box>`. The extra space will be divided evenly between all children that use this option
        :type expand: bool
        :param fill: ``True`` if space given to :py:obj:`child` by the :py:attr:`expend` option is actually \
        allocated to :py:obj:`child`, rather than just padding it. This parameter has no effect if :py:attr:`expend` \
        is set to :py:obj:`False`. A child is always allocated the full height of a horizontal \
        :class:`Box <GLXCurses.Box.Box>` and the full width of a vertical :class:`Box <GLXCurses.Box.Box>`. \
        This option affects the other dimension.
        :type fill: bool
        :param padding: extra space in characters to put between this child and its neighbors, over and above \
        the global amount specified by :py:attr:`spacing` attribute. If child is a widget at one of the reference ends \
        of box , then padding pixels are also put between child and the reference edge of box
        :type padding: int or None
        """
        # Try to exit as soon of possible
        if not glxc_type(child):
            raise TypeError('"child" argument must be a GLXCurses object type')
        if type(expand) != bool:
            raise TypeError('"expand" argument must be a bool type')
        if type(fill) != bool:
            raise TypeError('"fill" argument must be a bool type')
        if padding is not None:
            if type(padding) != int:
                raise TypeError('"spacing" must be int type or None')

        # If we are here everything look ok
        # Create a dict for store information's about packing
        child_info = dict()
        child_info['widget'] = child
        child_info['expand'] = expand
        child_info['fill'] = fill
        child_info['padding'] = clamp_to_zero(padding)

        self.get_children().append(child_info)

        self.emit_pack_end(data=child_info)

    def set_homogeneous(self, homogeneous=True):
        """
        Sets the :py:attr:`homogeneous` attribute of :class:`Box <GLXCurses.Box.Box>`, controlling whether or not all
        children of :class:`Box <GLXCurses.Box.Box>` are given equal space in the box.

        :param homogeneous: ``True`` to create equal allotments, ``False`` for variable allotments
        :type homogeneous: bool
        """
        self.homogeneous = bool(homogeneous)

    def get_homogeneous(self):
        """
        Returns whether the :class:`Box <GLXCurses.Box.Box>` is homogeneous (all children's have the same size).

        .. seealso:: :func:`Box.set_homogeneous() <GLXCurses.Box.Box.set_homogeneous>`

        :return: ``True`` if the :class:`Box <GLXCurses.Box.Box>` is homogeneous.
        :rtype: bool
        """
        return self.homogeneous

    def set_spacing(self, spacing=None):
        """
        Sets the “spacing” property of box , which is the number of characters to place between children of box .

        :param spacing: the number of character to put between children
        :type spacing: int or None
        """
        # Try to exit as soon of possible
        if spacing is not None:
            if type(spacing) != int:
                raise TypeError('"spacing" must be int type or None')

        spacing = clamp_to_zero(spacing)
        if spacing != self.get_spacing():
            self.spacing = spacing

    def get_spacing(self):
        """
        Gets the value set by :func:`Box.set_spacing() <GLXCurses.Box.Box.set_spacing>`.

        :return: spacing between children
        :rtype: int
        """
        return self.spacing

    def reorder_child(self, child, position):
        """
        Moves :py:obj:`child` to a new :py:obj:`position` in the list of :class:`Box <GLXCurses.Box.Box>` children.
        The list contains widgets packed :py:const:`PACK_START` as well as widgets packed :py:const:`PACK_END`,
        in the order that these widgets were added to :class:`Box <GLXCurses.Box.Box>`.

        A widget’s position in the :class:`Box <GLXCurses.Box.Box>` children list determines where the widget is
        packed into :class:`Box <GLXCurses.Box.Box>`. A child widget at some position in the list will be packed
        just after all other widgets of the same packing type that appear earlier in the list.

        :param child: the widget to move
        :type child: :class:`Widget <GLXCurses.Widget.Widget>`
        :param position: the new position for :py:obj:`child` in the list of children of \
        :class:`Box <GLXCurses.Box.Box>`, starting from 0. If negative, indicates the end of the list.
        :type position: list.index()
        """
        self.get_children().remove(child)

        # If negative, indicates the end of the list
        if position < 0:
            self.get_children().append(child)
        else:
            self.get_children().insert(position, child)

    def query_child_packing(self, child):
        """
        Obtains information about how child is packed into box .

        :param child: the :class:`Widget <GLXCurses.Widget.Widget>` of the :py:obj:`child` to query
        :type child: :class:`Widget <GLXCurses.Widget.Widget>`
        :return: information about how child is packed into box
        :rtype: tuple(:py:attr:`expand`, :py:attr:`fill`, :py:attr:`padding`, :py:attr:`pack_type`)
        """
        raise NotImplementedError

    def set_child_packing(self, child, expand, fill, padding, pack_type):
        """
        Sets the way child is packed into box .

        :param child: the :class:`Widget <GLXCurses.Widget.Widget>` of the child to set
        :type child: :class:`Widget <GLXCurses.Widget.Widget>`
        :param expand: the new value of the expand child property
        :type expand: bool
        :param fill: the new value of the fill child property
        :type fill: bool
        :param padding: the new value of the padding child property
        :type padding: int
        :param pack_type: the new value of the pack-type child property
        :type pack_type: :py:const:`PackType`
        """
        raise NotImplementedError

    # Internal
    def emit_pack_end(self, data=None):
        """
        Is emitted whenever a new child is pack_end on the Box.

        :param data: user data, what you want store
        :type data: dict
        """
        if data is None:
            data = dict()

        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'pack-end',
            'id': self.get_widget_id(),
            'data': data
        }
        # EVENT EMIT
        self.emit('SIGNALS', instance)

    def emit_pack_start(self, data=None):
        """
        Is emitted whenever a new child is pack_start on the Box.

        :param data: user data, what you want store
        :type data: dict
        """
        if data is None:
            data = dict

        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'pack-start',
            'id': self.get_widget_id(),
            'data': data
        }
        # EVENT EMIT
        self.emit('SIGNALS', instance)
