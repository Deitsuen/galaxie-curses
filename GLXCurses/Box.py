#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Container
from GLXCurses import Application
from GLXCurses import glxc

__author__ = 'Tuux'


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
        Container.__init__(self)

        # Attributes
        self.base_position = glxc.BASELINE_POSITION_CENTER
        self.base_position = None
        self.homogeneous = False
        self.spacing = 0

        # Child Attributes
        self.expend = False
        self.fill = True
        self.pack_type = glxc.PACK_START
        self.padding = 0
        self.position = 0

    def pack_start(self, child, expand=True, fill=True, padding=0):
        """
        Adds child to :class:`Box <GLXCurses.Box.Box>` , packed with reference to the start of
        :class:`Box <GLXCurses.Box.Box>`.

        :param child: the widget to be added to :class:`Box <GLXCurses.Box.Box>`
        :type child: :class:`Widget <GLXCurses.Widget.Widget>`
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
        :type padding: bool
        """
        # Try to exit as soon of possible
        if type(expand) != bool:
            raise TypeError(u'>expand< argument must be a bool')
        elif type(fill) != bool:
            raise TypeError(u'>fill< argument must be a bool')
        elif type(padding) != int and padding < 0:
            raise TypeError(u'>fill< padding must be a positive int')
        else:
            # Except the child everything look OK , then
            # Create a dict for store information's about packing
            # We'll store it as a list elment later
            child_info = dict()
            child_info['WIDGET'] = child
            child_info['EXPAND'] = expand
            child_info['FILL'] = fill
            child_info['PADDING'] = padding

            self.get_children().insert(0, child_info)

            self._emit_pack_start_signal()

    def pack_end(self, child, expand=True, fill=True, padding=0):
        """
        Adds child to :class:`Box <GLXCurses.Box.Box>` , packed with reference to the end of
        :class:`Box <GLXCurses.Box.Box>`.

        :param child: the widget to be added to :class:`Box <GLXCurses.Box.Box>`
        :type child: :class:`Widget <GLXCurses.Widget.Widget>`
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
        :type padding: bool
        """
        # Try to exit as soon of possible
        if type(expand) != bool:
            raise TypeError(u'>expand< argument must be a bool')
        elif type(fill) != bool:
            raise TypeError(u'>fill< argument must be a bool')
        elif type(padding) != int and padding < 0:
            raise TypeError(u'>fill< padding must be a positive int')
        else:
            # Except the child everything look OK , then
            # Create a dict for store information's about packing
            # We'll store it as a list elment later
            child_info = dict()
            child_info['WIDGET'] = child
            child_info['EXPAND'] = expand
            child_info['FILL'] = fill
            child_info['PADDING'] = padding

            self.get_children().append(child_info)

            self._emit_pack_end_signal()

    def pack_start_defaults(self, widget):
        pass

    def pack_end_defaults(self, widget):
        pass

    def set_homogeneous(self, homogeneous):
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

    def get_spacing(self):
        """
        Gets the value set by :func:`Box.set_spacing() <GLXCurses.Box.Box.set_spacing>`.

        :return: spacing between children
        :rtype: int
        """
        return self.spacing

    def set_spacing(self, spacing):
        """
        Sets the "spacing" attribute of :class:`Box <GLXCurses.Box.Box>`, which is the number of character to place
        between children of :class:`Box <GLXCurses.Box.Box>`.

        :param spacing: the number of char to put between children
        :type spacing: int
        """
        self.spacing = int(spacing)

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
    def _emit_pack_end_signal(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'pack-end',
            'id': self.id,
            'user_data': self.get_children()[-1]
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    def _emit_pack_start_signal(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'pack-start',
            'id': self.id,
            'user_data': self.get_children()[0]
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)